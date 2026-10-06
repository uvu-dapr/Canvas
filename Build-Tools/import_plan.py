#!/usr/bin/env python3
"""import_plan.py: what to do in Canvas around one class's import, from its package and live export (J77, 2026-10-05).

Adam got three hand-written pages for one 2020 import (Blueprint copies to delete, the gradebook switch, the guide).
This works it out from the checks, for Canvas Preview's Upload and Import Checklist:

  before   live items to delete first: class copies of Blueprint content already in the course (blueprint_copies.py
           run on the export itself), and old class pages with Essentials names outside the synced modules
  package  copies the package itself still carries (Blueprint content, taken work under a new name): rebuild first
  replaced live pages the package brings again under a new name: delete the old ones after the import
  after    the one-time gradebook switch (a fixed-id group the live course doesn't have yet), and an
           "Imported Assignments" group to empty and delete

    python3 import_plan.py <package.imscc> <live export.imscc>      prints JSON
"""
import sys, os, re, json, zipfile, html

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import blueprint_copies as bc
import taken_renames as tr
import fixed_groups as fg


def U(s):
    return " ".join(html.unescape(s or "").split())


def main(pkg, export):
    out = dict(before=[], package=[], after=[])
    # publish state from the export: a page's meta workflow_state; graded work students can reach (taken_renames)
    zx = zipfile.ZipFile(export)
    def page_pub(slug):
        try:
            m = re.search(r'name="workflow_state" content="(\w+)"', zx.read("wiki_content/%s.html" % slug)[:3000].decode("utf8", "ignore"))
            return (m.group(1) if m else "active") == "active"
        except KeyError:
            return False
    reach = {v["title"]: v["reachable"] for v in tr.graded(export).values()}
    # before: Blueprint copies already in the live course (outside the synced modules)
    for c in bc.plan(export, export):
        out["before"].append(dict(kind=c["kind"], title=c["title"], slug=c["slug"], why="a class copy of the Blueprint's \"%s\": students already get that one" % c["copies"],
                                  published=page_pub(c["slug"]) if c["slug"] else reach.get(c["title"], False)))
    seen = {b["title"] for b in out["before"]}
    ref = bc.read_items(export)
    synced = {k[1] for k, v in ref.items() if "Unified Class Content" in v["module"]}
    for k, v in ref.items():
        if k[0] == "page" and v["title"].startswith("Essentials:") and "Unified Class Content" not in v["module"] and v["title"] not in seen and v["title"] not in synced:
            out["before"].append(dict(kind="page", title=v["title"], slug=v["slug"], why="an old class page with a Blueprint name; the Blueprint's version is the one students use", published=page_pub(v["slug"])))
    # old live modules the package replaces (not Blueprint, not in the package): delete them after the import, or, when
    # they hold work students took, move that work into its new module first (Adam, 2026-10-05: "I will move the quizzes")
    def nm(t): return re.sub(r"[^a-z0-9]+", " ", re.sub(r"^(week|module) \d+: ", "", t.lower().replace("&", "and"))).strip()
    pm = zipfile.ZipFile(pkg).read("course_settings/module_meta.xml").decode("utf8", "ignore")
    pkg_mods = {nm(html.unescape(m)) for m in re.findall(r'<module identifier="[^"]+">\s*<title>([^<]*)', pm)}
    lm = zx.read("course_settings/module_meta.xml").decode("utf8", "ignore")
    taken_titles = {v["title"] for v in tr.graded(export).values() if v["reachable"]}
    for m in re.finditer(r'(?s)<module identifier="[^"]+">(.*?)</module>', lm):
        t = U(re.search(r"<title>([^<]*)", m.group(1)).group(1))
        if "Unified Class Content" in t: continue
        if nm(t) in pkg_mods:
            # the package has this module: taken work the live module holds but the package's module doesn't link stays
            # in Canvas outside it after the import (Canvas drops a link it can't match): move it in by hand
            pblk = [b for b in re.finditer(r'(?s)<module identifier="[^"]+">(.*?)</module>', pm) if nm(U(re.search(r"<title>([^<]*)", b.group(1)).group(1))) == nm(t)]
            ptitles = {U(x) for b in pblk for x in re.findall(r"<title>([^<]*)</title>", b.group(1))}
            for x in [U(x) for x in re.findall(r"<title>([^<]*)</title>", m.group(1))[1:]]:
                if x in taken_titles and x not in ptitles:
                    out.setdefault("moves", []).append(dict(item=x, module=U(re.search(r"<title>([^<]*)", pblk[0].group(1)).group(1)) if pblk else t))
            continue
        if "instructor use only" in t.lower() and any("instructor use only" in x for x in pkg_mods): pass
        items = [U(x) for x in re.findall(r"<title>([^<]*)</title>", m.group(1))[1:]]
        took = [x for x in items if x in taken_titles]
        out["modules"] = out.get("modules", [])
        out["modules"].append(dict(title=t, items=len(items), taken=took))

    # live pages the package brings again under a new name (2020 v89: the 24 "macOS: P1: Finder Deep Dive" pages come in as
    # "macOS: Finder Deep Dive" with fixed pictures, and Canvas keeps the old ones published beside them): delete the old
    # ones after the import (J92, 2026-10-06). Same words (Jaccard 0.6, as Blueprint copies), a title the package lacks.
    P = {k: v for k, v in bc.read_items(pkg).items() if k[0] == "page"}
    ptitles = {k[1] for k in P}
    blue = {b["title"] for b in out["before"]}
    out["replaced"] = []
    for k, v in ref.items():
        if k[0] != "page" or v["title"] in ptitles or v["title"] in blue or "Unified Class Content" in v["module"] or "Instructor Use Only" in v["module"] or len(v["words"]) < 20:
            continue
        best, bt = 0.0, None
        for pk, pv in P.items():
            j = len(v["words"] & pv["words"]) / max(1, len(v["words"] | pv["words"]))
            if j > best:
                best, bt = j, pv
        if bt is not None and best >= bc.PAGE_MATCH:
            out["replaced"].append(dict(title=v["title"], slug=v["slug"], new=bt["title"], share=round(best, 2), published=page_pub(v["slug"])))
    out["replaced"].sort(key=lambda r: r["title"])

    for c in bc.plan(pkg, export):
        out["package"].append("Blueprint copy: %s" % c["title"])
    for p in tr.plan(pkg, export):
        out["package"].append("second copy of taken work: %s (live \"%s\")" % (p["package"], p["live"]))
    # after: gradebook
    z = zipfile.ZipFile(pkg)
    mine = fg.groups(z.read("course_settings/assignment_groups.xml").decode("utf8", "ignore")) if "course_settings/assignment_groups.xml" in z.namelist() else {}
    live = fg.groups(zipfile.ZipFile(export).read("course_settings/assignment_groups.xml").decode("utf8", "ignore"))
    live_titles = {}
    for v in live.values():
        live_titles.setdefault(v["title"].lower(), []).append(v)
    fixed = {gid: g for gid, g in mine.items() if gid.startswith("dapr-group-")}
    if fixed:
        # done when the live group of that name is the one an earlier package made under the fixed id
        import match_ids as mi
        _, lv, _ = mi.lineage(export, [mi.class_folder(export)])
        stored = {v["title"].lower(): v["candidates"] for v in lv.values() if v["kind"] == "assignment group"}
        for gid, g in fixed.items():
            if gid not in stored.get(g["title"].lower(), []):
                out["after"].append(dict(step="switch", title=g["title"], weight=g["weight"]))
    if "imported assignments" in live_titles:
        out["after"].append(dict(step="imported", title="Imported Assignments"))
    # graded work students took is unpublished, never deleted (deleting removes their grades)
    for b in out["before"]:
        b["action"] = "unpublish" if b["kind"] == "quiz" and b["published"] else "delete"
    print(json.dumps(out))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
