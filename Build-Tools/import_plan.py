#!/usr/bin/env python3
"""import_plan.py: what to do in Canvas around one class's import, from its package and live export (J77, 2026-10-05).

Adam got three hand-written pages for one 2020 import (Blueprint copies to delete, the gradebook switch, the guide).
This works it out from the checks, for Canvas Preview's Upload and Import Checklist:

  before   live items to delete first: class copies of Blueprint content already in the course (blueprint_copies.py
           run on the export itself), and old class pages with Essentials names outside the synced modules
  package  copies the package itself still carries (Blueprint content, taken work under a new name): rebuild first
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
    # package: what the package would still bring twice
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
