#!/usr/bin/env python3
"""fixed_groups.py: gradebook groups an import can always match (Adam chose this one-time switch, 2026-10-05).

Canvas finds a gradebook group by the id it stored when an import made it. A group made in Canvas (DAPR 2020's
"Assignments") or one two packages claimed (DAPR 2255's) has no id a package can name, so every import moved the
graded items it updated into "Imported Assignments" (0% in a weighted course).

This gives the package each group its items use under a FIXED id ("dapr-group-assignments"), with the live group's
weight and position, and points every graded item at it. The first import makes a second group of that name; in
Canvas, delete the OLD one and choose "Move its assignments to" the new one. From then on every import matches it.

    python3 fixed_groups.py apply <package.imscc> <live export.imscc> <out.imscc>

Never overwrites. Groups are named by the live course; an item whose group the package does not define goes to
Assignments.
"""
import sys, os, re, html, zipfile, shutil, tempfile

NS = ('<assignmentGroups xmlns="http://canvas.instructure.com/xsd/cccv1p0" '
      'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
      'xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">')


def fixed_id(title):
    return "dapr-group-" + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def groups(xml):
    out = {}
    for m in re.finditer(r'(?s)<assignmentGroup identifier="([^"]+)">(.*?)</assignmentGroup>', xml):
        g = lambda k: (re.search(r"<%s>([^<]*)</%s>" % (k, k), m.group(2)) or [None, ""])[1]
        out[m.group(1)] = dict(title=" ".join(html.unescape(g("title")).split()), position=g("position"), weight=g("group_weight"))
    return out


def apply(pkg, export, out):
    assert not os.path.exists(out), "never overwrite: " + out
    live = groups(zipfile.ZipFile(export).read("course_settings/assignment_groups.xml").decode("utf8", "ignore"))
    live_by_title = {v["title"].lower(): v for v in live.values()}
    w = tempfile.mkdtemp(prefix="groups-")
    zipfile.ZipFile(pkg).extractall(w)
    shutil.rmtree(os.path.join(w, "__MACOSX"), ignore_errors=True)
    gpath = os.path.join(w, "course_settings/assignment_groups.xml")
    mine = groups(open(gpath, encoding="utf8").read()) if os.path.exists(gpath) else {}
    # every group id an item names -> the live title it belongs to
    title_of = {i: (mine[i]["title"] if i in mine else live[i]["title"] if i in live else "Assignments") for i in []}
    used, moved = {}, 0
    for root, _, fs in os.walk(w):
        for f in fs:
            if not f.endswith((".xml", ".qti")):
                continue
            p = os.path.join(root, f)
            t = open(p, encoding="utf8", errors="ignore").read()
            if "<assignment_group_identifierref>" not in t:
                continue
            def sub(m):
                nonlocal moved
                i = m.group(1)
                title = mine[i]["title"] if i in mine else live[i]["title"] if i in live else "Assignments"
                if title.lower() not in live_by_title:
                    title = "Assignments"
                fid = fixed_id(title)
                used[fid] = title
                if i != fid:
                    moved += 1
                return "<assignment_group_identifierref>%s</assignment_group_identifierref>" % fid
            t2 = re.sub(r"<assignment_group_identifierref>([^<]+)</assignment_group_identifierref>", sub, t)
            if t2 != t:
                open(p, "w", encoding="utf8").write(t2)
    body = ""
    for fid, title in sorted(used.items(), key=lambda x: int(live_by_title[x[1].lower()]["position"] or 0)):
        lv = live_by_title[title.lower()]
        body += ('\n  <assignmentGroup identifier="%s">\n    <title>%s</title>\n    <position>%s</position>\n'
                 '    <group_weight>%s</group_weight>\n  </assignmentGroup>' % (fid, html.escape(title), lv["position"] or "1", lv["weight"] or "0"))
    os.makedirs(os.path.dirname(gpath), exist_ok=True)
    open(gpath, "w", encoding="utf8").write('<?xml version="1.0" encoding="UTF-8"?>\n' + NS + body + "\n</assignmentGroups>\n")
    man_p = os.path.join(w, "imsmanifest.xml")
    man = open(man_p, encoding="utf8").read()
    if "course_settings/assignment_groups.xml" not in man:
        # the course settings resource lists its files; a partial package without one needs the file listed
        man = re.sub(r'(<file href="course_settings/module_meta.xml"\s*/>)', r'\1<file href="course_settings/assignment_groups.xml"/>', man, count=1)
        open(man_p, "w", encoding="utf8").write(man)
    cwd = os.getcwd()
    os.chdir(w)
    os.system('zip -q -r -D -X "%s" . -x "*.DS_Store" "__MACOSX/*"' % (out + ".partial"))
    os.chdir(cwd)
    os.rename(out + ".partial", out)
    shutil.rmtree(w, ignore_errors=True)
    return used, moved


if __name__ == "__main__":
    if sys.argv[1] == "apply":
        used, moved = apply(sys.argv[2], sys.argv[3], sys.argv[4])
        print("groups:", ", ".join("%s (%s)" % (t, i) for i, t in used.items()), "| item references changed:", moved)
