#!/usr/bin/env python3
"""Bring the graded work into a pages-only LIVE package, so moving a module can move its due dates (Adam, 2026-10-01).

    python3 bring_graded.py <working folder> <full package .imscc or folder> [--live <Canvas export.imscc>] [--dry-run]

A pages-only package (Standards 16b) carries pages and modules but no quizzes or assignments, so Canvas Preview's
Week Planner could only list the due dates to change by hand. This copies every quiz, assignment and graded
discussion from the class's full package (the one already imported, whose identifiers are the ones Canvas matches,
Standards 16a) into the working folder, and links each one into the module of the same title, after the item it
followed in the full package:

- Items the full package carries (files and manifest resource): copied with the same identifier, so the import
  updates the live item in place. A due date moved in the Week Planner then moves in Canvas.
- Items the full package only links (taken work it left out on purpose): linked the same way, by the same id.
- With --live, taken work whose link carries an export label (an id Canvas cannot match, so the import would drop
  the link) is not linked; it stays where it is in the live course.
- Their assignment group and rubric references are dropped when the working folder has no assignment_groups.xml or
  rubrics.xml: Canvas then keeps each item's live group and rubric (a reference to a group the package does not
  carry would put the item in a new default group).
- Each module item gets a new identifier (the item lands in the new module; the old module keeps its own link until
  it is deleted).

Never overwrites an item already in the working folder. Prints what it added, then RESULT.
"""
import os, re, sys, shutil, zipfile, tempfile, hashlib, html

def read(p): return open(p, encoding="utf-8").read()
def write(p, s): open(p, "w", encoding="utf-8").write(s)
def U(s): return " ".join(html.unescape(s).split())

def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    work, full = sys.argv[1], sys.argv[2]
    dry = "--dry-run" in sys.argv
    labels = set()
    if "--live" in sys.argv:
        z = zipfile.ZipFile(sys.argv[sys.argv.index("--live") + 1])
        labels = set(re.findall(r'identifier="([^"]+)"', z.read("imsmanifest.xml").decode("utf-8", "ignore")))
        if "course_settings/module_meta.xml" in z.namelist():
            labels |= set(re.findall(r'identifier="([^"]+)"', z.read("course_settings/module_meta.xml").decode("utf-8", "ignore")))
    tmp = None
    if os.path.isfile(full):
        tmp = tempfile.mkdtemp(prefix="bring_graded_")
        zipfile.ZipFile(full).extractall(tmp)
        src = tmp
    else:
        src = full
    try:
        run(work, src, dry, labels)
    finally:
        if tmp: shutil.rmtree(tmp, ignore_errors=True)

def run(work, src, dry, labels=set()):
    sman, wman = read(os.path.join(src, "imsmanifest.xml")), read(os.path.join(work, "imsmanifest.xml"))
    smm, wmm_path = read(os.path.join(src, "course_settings/module_meta.xml")), os.path.join(work, "course_settings/module_meta.xml")
    wmm = read(wmm_path)
    keep_groups = os.path.exists(os.path.join(work, "course_settings/assignment_groups.xml"))
    keep_rubrics = os.path.exists(os.path.join(work, "course_settings/rubrics.xml"))
    wres = set(re.findall(r'<resource identifier="([^"]+)"', wman))
    sres = {m.group(1): m.group(0) for m in re.finditer(r'(?s)<resource identifier="([^"]+)"[^>]*>.*?</resource>|<resource identifier="([^"]+)"[^>]*/>', sman) if m.group(1)}
    wmods = {U(m.group(2)): m.group(1) for m in re.finditer(r'(?s)<module identifier="([^"]+)">\s*<title>([^<]*)</title>', wmm)}
    graded = ("Assignment", "Quizzes::Quiz", "DiscussionTopic")
    added, linked, skipped, new_res = [], [], [], []
    copied = set()

    def copy_resource(rid):
        """The resource, its files and its dependencies (a quiz's _meta, a discussion's topicMeta)."""
        if rid in wres or rid in copied or rid not in sres: return
        block = sres[rid]
        copied.add(rid)
        for href in re.findall(r'<file href="([^"]+)"', block):
            a, b = os.path.join(src, href), os.path.join(work, href)
            if not os.path.exists(a): continue
            if os.path.exists(b): continue
            if not dry:
                os.makedirs(os.path.dirname(b), exist_ok=True)
                shutil.copy2(a, b)
                if b.endswith((".xml",)) and (not keep_groups or not keep_rubrics):
                    x = read(b); y = x
                    if not keep_groups: y = re.sub(r"\s*<assignment_group_identifierref>[^<]*</assignment_group_identifierref>", "", y)
                    if not keep_rubrics:
                        y = re.sub(r"\s*<rubric_identifierref>[^<]*</rubric_identifierref>", "", y)
                        y = re.sub(r"\s*<rubric_external_identifier>[^<]*</rubric_external_identifier>", "", y)
                    if y != x: write(b, y)
        new_res.append(block)
        for dep in re.findall(r'<dependency identifierref="([^"]+)"', block): copy_resource(dep)
        # the other half of a quiz or discussion: a resource whose files sit in this one's folder
        for other, ob in sres.items():
            if other != rid and other not in copied and re.search(r'<file href="%s/' % re.escape(rid), ob): copy_resource(other)

    out = wmm
    for m in re.finditer(r'(?s)<module identifier="([^"]+)">\s*<title>([^<]*)</title>(.*?)</module>', smm):
        title = U(m.group(2)); target = wmods.get(title)
        items = list(re.finditer(r'(?s)<item identifier="([^"]+)">(.*?)</item>', m.group(3)))
        prev_title = None
        for it in items:
            body = it.group(2)
            ct = (re.search(r"<content_type>([^<]*)", body) or [None, ""])[1]
            ititle = U((re.search(r"<title>([^<]*)", body) or [None, ""])[1])
            ref = (re.search(r"<identifierref>([^<]*)", body) or [None, ""])[1]
            if ct not in graded or not ref:
                prev_title = ititle; continue
            if target is None:
                skipped.append("%s (no module named %s in this package)" % (ititle, title)); continue
            wmod = re.search(r'(?s)(<module identifier="%s">.*?)(</items>|</module>)' % re.escape(target), out)
            if re.search(r"<identifierref>%s</identifierref>" % re.escape(ref), wmod.group(1)):
                prev_title = ititle; continue          # already linked here
            if ref in sres: copy_resource(ref); added.append(ititle)
            elif ref in labels:
                skipped.append("%s (taken work linked by an export label Canvas cannot match: left where it is)" % ititle); prev_title = ititle; continue
            else: linked.append(ititle)
            iid = "i" + hashlib.md5((target + ref).encode()).hexdigest()[:12]
            item = '<item identifier="%s">%s</item>' % (iid, body)
            # after the item it followed in the full package, else at the end of the module's items
            mod = wmod.group(1)
            spot = None
            if prev_title:
                for pm in re.finditer(r'(?s)<item identifier="[^"]+">.*?<title>([^<]*)</title>.*?</item>', mod):
                    if U(pm.group(1)) == prev_title: spot = wmod.start(1) + pm.end()
            if spot is None:
                spot = wmod.end(1)                      # just before </items> (or </module> when it has none)
                if wmod.group(2) == "</module>":
                    item = "<items>" + item + "</items>"
            out = out[:spot] + "\n      " + item + out[spot:]
            prev_title = ititle
    # renumber positions inside each module
    def renumber(mm):
        def mod(mx):
            n = [0]
            def pos(px): n[0] += 1; return "<position>%d</position>" % n[0]
            return re.sub(r"<position>\d+</position>", pos, mx.group(0))
        return re.sub(r'(?s)<module identifier="[^"]+">.*?</module>', mod, mm)
    out = renumber(out)
    if not dry:
        write(wmm_path, out)
        if new_res:
            wman2 = wman.replace("</resources>", "\n    " + "\n    ".join(new_res) + "\n  </resources>", 1)
            write(os.path.join(work, "imsmanifest.xml"), wman2)
    for t in added: print("added: " + t)
    for t in linked: print("linked (taken work, by its id): " + t)
    for t in skipped: print("skipped: " + t)
    print("RESULT: %d graded item(s) added, %d linked by id, %d skipped%s%s" % (len(added), len(linked), len(skipped),
          "" if keep_groups else "; their live assignment groups and rubrics are kept", " (dry run)" if dry else ""))

if __name__ == "__main__":
    main()
