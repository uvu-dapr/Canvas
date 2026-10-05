#!/usr/bin/env python3
"""
match_ids.py: give a LIVE-Import the identifiers Canvas really matches on (Adam, 2026-09-29).

Why: a Canvas export labels each item "g" + md5(the item's own database id) (CC::CCHelper.create_key). An import
finds an existing item only by the migration id stored when the item was created: the identifier of the package
(or source course) whose import made it (Importers::WikiPageImporter.import_from_migration and friends). The export
never shows that stored id. A package that copies the export's labels matches nothing, and the import adds copies.

How: every live item that one of our earlier imports created was created under the identifier an earlier package
gave it. For each item in the package that carries an export label, the earlier packages' identifiers for the same
title (other than the label itself) name the one to use. Exactly one earlier identifier: use it (the import updates
the live item in place). None: the item is original to the course (made in Canvas or copied from another term) and
no import can update it; it is listed.

    python3 match_ids.py plan <package.imscc> <Canvas export.imscc> <older package or folder>... [--json plan.json]
    python3 match_ids.py apply <package.imscc> <plan.json> <out.imscc>
    python3 match_ids.py stored <Canvas export.imscc>

apply never overwrites: it refuses when out exists. Taken items the LIVE-Import leaves out are not touched.
"""
import sys, os, re, json, zipfile, html, collections, glob

def U(s): return " ".join(html.unescape(s).split())

def titles(path):
    """identifier -> (kind, title) for pages, assignments, quizzes, discussions and modules."""
    z = zipfile.ZipFile(path); names = set(z.namelist())
    man = z.read("imsmanifest.xml").decode("utf-8", "ignore"); out = {}
    for m in re.finditer(r'<resource identifier="([^"]+)"[^>]*>', man):
        rid = m.group(1); h = re.search(r'href="([^"]+)"', m.group(0)); href = h.group(1) if h else ""
        tries = []
        if href.startswith("wiki_content/"): tries.append((href, "page"))
        tries += [(f"{rid}/assignment_settings.xml", "assignment"), (f"{rid}/assessment_meta.xml", "quiz")]
        if href.startswith("assignments/") and href.endswith(".html"): tries.append((href[:-5] + ".xml", "assignment"))
        if "imsdt_xmlv1p1" in m.group(0): tries.append((href, "discussion"))
        # the other quiz layout Canvas and our older packages write: an assessment resource whose href is the QTI file
        # (quizzes/quiz_x.xml), titled in <assessment title="...">
        if re.search(r'type="imsqti_xmlv1p2/imscc_xmlv1p1/assessment"', m.group(0)) and href and href in names and f"{rid}/assessment_meta.xml" not in names:
            q = re.search(r'<assessment\b[^>]*\btitle="([^"]*)"', z.read(href)[:20000].decode("utf-8", "ignore"))
            if q: out[rid] = ("quiz", U(q.group(1))); continue
        for n, k in tries:
            if n in names:
                t = re.search(r"<title>([^<]*)", z.read(n)[:6000].decode("utf-8", "ignore"))
                if t: out[rid] = (k, U(t.group(1)))
                break
    if "course_settings/module_meta.xml" in names:
        mm = z.read("course_settings/module_meta.xml").decode("utf-8", "ignore")
        for m in re.finditer(r'(?s)<module identifier="([^"]+)">\s*<title>([^<]*)</title>(.*?)</module>', mm):
            mt = U(m.group(2)); out[m.group(1)] = ("module", mt)
            # module items are matched by their own stored id too: key them by module and item title
            for it in re.finditer(r'(?s)<item identifier="([^"]+)">.*?<title>([^<]*)</title>', m.group(3)):
                out[it.group(1)] = ("module item", mt + " | " + U(it.group(2)))
    for f, tag, kind in (("course_settings/assignment_groups.xml", "assignmentGroup", "assignment group"), ("course_settings/rubrics.xml", "rubric", "rubric")):
        if f in names:
            x = z.read(f).decode("utf-8", "ignore")
            for m in re.finditer(r'(?s)<%s identifier="([^"]+)"[^>]*>\s*<title>([^<]*)</title>' % tag, x): out[m.group(1)] = (kind, U(m.group(2)))
    return out

def class_folder(export):
    """The class folder above an export ("DAPR 2000 - ..."): every tool reads the same older packages from it."""
    d = os.path.dirname(os.path.abspath(export))
    while d != "/" and not re.match(r"DAPR \d", os.path.basename(d)): d = os.path.dirname(d)
    return d if d != "/" else os.path.dirname(os.path.abspath(export))

def packages(args):
    out = []
    for a in args:
        if os.path.isdir(a): out += [f for f in glob.glob(os.path.join(a, "**", "*.imscc"), recursive=True) if os.path.getsize(f) < 400_000_000]
        elif a.lower().endswith(".imscc"): out.append(a)
    return sorted(set(out))

def lineage(export, older, skip=()):
    """For every live item in the export: (kind, title), its export label, and the id Canvas stored when an earlier
    import created it (None when no earlier package names it: original to the course).

    Only packages made before the label first appears in a package count: a label copied into later packages (the
    2026-09-28 LIVE-Imports did that) is not how the item was made. Two live pages with one title (an original and
    the copy an import made of it) otherwise point at each other."""
    ex = titles(export)
    order = []
    cutoff = os.path.getmtime(export)      # only a package made before the export can have made a live item in it
    for f in sorted(packages(older), key=os.path.getmtime):
        if os.path.abspath(f) in {os.path.abspath(x) for x in skip} | {os.path.abspath(export)}: continue
        if os.path.getmtime(f) >= cutoff: continue
        try: order.append((os.path.basename(f), titles(f)))
        except Exception: continue
    first_seen = {}
    for k, (_, t) in enumerate(order):
        for rid in t: first_seen.setdefault(rid, k)
    live = {}
    for rid, kt in ex.items():
        cut = first_seen.get(rid, len(order))
        seen = collections.OrderedDict()
        for k in range(cut):
            for c, ckt in order[k][1].items():
                if ckt == kt and c != rid: seen[c] = seen.get(c, 0) + 1
        cands = list(seen)
        live[rid] = dict(kind=kt[0], title=kt[1], stored=cands[-1] if len(cands) == 1 else None, candidates=cands)
    # An id another live item was already made from can't be how this one was made: Canvas would have matched that
    # item instead of making a new one (live 2000 had three "Assignments" groups, 2026-09-29)
    taken = {v["stored"] for v in live.values() if v["stored"]}
    for v in live.values():
        if not v["stored"] and len(v["candidates"]) > 1:
            left = [c for c in v["candidates"] if c not in taken]
            if len(left) == 1: v["stored"] = left[0]
    return ex, live, [n for n, _ in order]

def plan(pkg, export, older):
    pk = titles(pkg)
    ex, live, used = lineage(export, older, skip=[pkg])
    by_stored = {v["stored"]: e for e, v in live.items() if v["stored"]}
    rows = []
    for rid, kt in pk.items():
        # The live item this label names comes first: it is the one its module shows (module items are matched only
        # inside their own module). Its label may also be the stored id of a copy an earlier import made of it.
        if rid in live and live[rid]["stored"] and live[rid]["stored"] not in pk:
            v = live[rid]
            rows.append(dict(id=rid, kind=kt[0], title=v["title"], status="swap", use=v["stored"], live_label=rid)); continue
        if rid in by_stored:        # already the id Canvas matches: the import updates that live item in place
            e = by_stored[rid]
            rows.append(dict(id=rid, kind=kt[0], title=live[e]["title"], status="update", use=rid, live_label=e)); continue
        if rid not in live:
            rows.append(dict(id=rid, kind=kt[0], title=kt[1], status="new", use=rid)); continue
        v = live[rid]
        if v["stored"] and v["stored"] not in pk:
            rows.append(dict(id=rid, kind=kt[0], title=v["title"], status="swap", use=v["stored"], live_label=rid))
        elif not v["candidates"]:
            rows.append(dict(id=rid, kind=kt[0], title=v["title"], status="original", use=rid,
                             why="made in Canvas or copied from another term: no import can update it, it arrives as a copy"))
        else:
            rows.append(dict(id=rid, kind=kt[0], title=v["title"], status="unsure", use=rid, candidates=v["candidates"],
                             why="several earlier identifiers, or one the package already uses: needs a look"))
    # Live items the package only links to (work students took is placed by its live id, never carried): a module item
    # whose linked item Canvas can't find by its stored id is dropped from a module the import matches
    z = zipfile.ZipFile(pkg); text = ""
    for n in z.namelist():
        if n.endswith((".xml", ".html")) and not n.startswith("web_resources/"): text += z.read(n).decode("utf-8", "ignore")
    done = {r["id"] for r in rows}
    for lab in sorted(set(re.findall(r"\bg[0-9a-f]{32}\b", text)) & set(live) - done):
        v = live[lab]
        if v["stored"] and v["stored"] not in pk:
            rows.append(dict(id=lab, kind=v["kind"], title=v["title"], status="swap", use=v["stored"], live_label=lab, linked_only=True))
    # A module linking a live item Canvas can't find by a known stored id would lose that link on import (the module
    # importer drops a module item whose linked item it can't find, then clears missing items): such a module is left
    # out, so Canvas keeps it exactly as it is; its pages still update (2000 Pro Tools, 2255 Ohm's Law, 2026-09-29)
    unsure_ids = set()
    shared0 = collections.Counter(v["stored"] for v in live.values() if v["stored"])
    for lab, v in live.items():
        if v["kind"] in ("page", "assignment", "quiz", "discussion") and (not v["stored"] or shared0[v["stored"]] > 1): unsure_ids.add(lab)
    leave_out, carry = [], {}
    try:
        sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
        import taken_renames as _tr
        reach = {k for k, v in _tr.graded(export).items() if v["reachable"]}
    except Exception:
        reach = set()
    rep = pkg + ".report.json"
    taken_titles = {" ".join(t.get("title", "").split()) for t in (json.load(open(rep)).get("taken_items", []) if os.path.exists(rep) else [])}
    if "course_settings/module_meta.xml" in z.namelist():
        mm = z.read("course_settings/module_meta.xml").decode("utf-8", "ignore")
        for m in re.finditer(r'(?s)<module identifier="([^"]+)">\s*<title>([^<]*)</title>(.*?)</module>', mm):
            bad = []
            for it in re.finditer(r'(?s)<item identifier="[^"]+">(.*?)</item>', m.group(3)):
                ref = re.search(r"<identifierref>([^<]+)</identifierref>", it.group(1)); t = re.search(r"<title>([^<]*)</title>", it.group(1))
                if ref and ref.group(1) in unsure_ids and ref.group(1) not in pk and not (ref.group(1) in by_stored and shared0[ref.group(1)] == 1): bad.append(U(t.group(1)) if t else ref.group(1))
            if not bad: continue
            # Untaken items can come along from the export as fresh copies (the module then links the copy and the old
            # one goes on the delete list); only work students took keeps its module exactly as it is
            badref = {}
            for it in re.finditer(r'(?s)<item identifier="[^"]+">(.*?)</item>', m.group(3)):
                ref = re.search(r"<identifierref>([^<]+)</identifierref>", it.group(1))
                if ref and ref.group(1) in unsure_ids and ref.group(1) not in pk and not (ref.group(1) in by_stored and shared0[ref.group(1)] == 1): badref[ref.group(1)] = live[ref.group(1)]["title"]
            # taken: on the LIVE-Import's report, or published in the export (a Full package has no report; 3340 v83's
            # Intro quiz was copied instead of left alone, 2026-10-05)
            took = {r: t for r, t in badref.items() if t in taken_titles or (live[r]["stored"] and shared0[live[r]["stored"]] > 1) or r in reach}
            if took: leave_out.append(dict(id=m.group(1), title=U(m.group(2)), because=sorted(set(took.values()))))
            else: carry.update(badref)
    # Two live items made from the same id: Canvas takes whichever it finds first, so a swap to that id is not safe
    shared = collections.Counter(v["stored"] for v in live.values() if v["stored"])
    for r in rows:
        if r["status"] in ("swap", "update") and shared[r["use"]] > 1:
            twins = [e for e, v in live.items() if v["stored"] == r["use"]]
            r.update(status="unsure", use=r["id"], candidates=twins,
                     why="%d live copies were made from the same id (%s); Canvas would pick one of them" % (len(twins), r["use"]))
    c = collections.Counter(r["status"] for r in rows)
    return dict(package=pkg, export=export, older=sorted(used), counts=dict(c), items=rows, leave_out_modules=leave_out,
                carry_from_export=[dict(id=k, title=v) for k, v in sorted(carry.items(), key=lambda x: x[1])])

def apply(pkg, planfile, out):
    if os.path.exists(out): sys.exit(f"refusing to overwrite {out}")
    p = json.load(open(planfile))
    swap = {r["id"]: r["use"] for r in p["items"] if r["status"] == "swap"}
    # An assignment group whose stored id is unsure stays out, and items stop naming it: Canvas then keeps each live
    # assignment and quiz in the group it is in now (AssignmentImporter.associate_assignment_group uses ||=; the quiz
    # importer sets a group only when it finds one), so no grade moves between groups (live 2000, 2026-09-29)
    keep_groups = {r["id"] for r in p["items"] if r["kind"] == "assignment group" and r["status"] in ("unsure", "original")}
    new_items = {r["id"] for r in p["items"] if r["kind"] in ("assignment", "quiz") and r["status"] == "new"}
    pat = re.compile("|".join(map(re.escape, sorted(swap, key=len, reverse=True)))) if swap else None
    zin = zipfile.ZipFile(pkg); n_text = 0
    # A group the import updates keeps the weight it has in Canvas: a package that says 0 would zero out the live
    # grading scheme (2255 v100 carried Assignments at 0 against the live 75%, 2026-09-30)
    live_weight = {}
    try:
        eg = zipfile.ZipFile(p["export"]).read("course_settings/assignment_groups.xml").decode("utf-8", "ignore")
        for m in re.finditer(r'(?s)<assignmentGroup identifier="([^"]+)">(.*?)</assignmentGroup>', eg):
            w = re.search(r"<group_weight>([^<]*)</group_weight>", m.group(2))
            if w: live_weight[m.group(1)] = w.group(1)
    except Exception:
        pass
    group_target = {r["use"]: r.get("live_label") or r["id"] for r in p["items"] if r["kind"] == "assignment group" and r["status"] in ("swap", "update")}
    weights_kept = []
    drop = {m["id"] for m in p.get("leave_out_modules", [])}
    def cut_module(name, t):
        for mid in drop:
            if name.endswith("module_meta.xml"):
                t = re.sub(r'(?s)\s*<module identifier="%s">.*?</module>' % re.escape(mid), "", t)
            elif name == "imsmanifest.xml":
                st = t.find('<item identifier="%s">' % mid)
                if st < 0: continue
                depth = 0
                for x in re.finditer(r'<item\b[^>]*?(/?)>|</item>', t[st:]):
                    if x.group(0).startswith("</"): depth -= 1
                    elif not x.group(1): depth += 1
                    if depth == 0: t = t[:st] + t[st + x.end():]; break
        return t
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zo:
        for info in zin.infolist():
            name = info.filename; data = zin.read(name)
            if drop and (info.filename.endswith("module_meta.xml") or info.filename == "imsmanifest.xml"):
                data = cut_module(info.filename, data.decode("utf-8", "ignore")).encode("utf-8")
            if info.filename.endswith("assignment_groups.xml") and group_target:
                t = data.decode("utf-8", "ignore")
                def keepw(m):
                    gid = pat.sub(lambda x: swap[x.group(0)], m.group(1)) if pat else m.group(1)
                    lab = group_target.get(gid)
                    if lab in live_weight:
                        new = re.sub(r"<group_weight>[^<]*</group_weight>", "<group_weight>%s</group_weight>" % live_weight[lab], m.group(0))
                        if new != m.group(0): weights_kept.append(lab)
                        return new
                    return m.group(0)
                t = re.sub(r'(?s)<assignmentGroup identifier="([^"]+)">.*?</assignmentGroup>', keepw, t)
                data = t.encode("utf-8")
            if keep_groups and re.search(r"\.(xml|qti)$", info.filename):
                t = data.decode("utf-8", "ignore"); t0 = t
                if info.filename.endswith("assignment_groups.xml"):
                    for g in keep_groups: t = re.sub(r'(?s)\s*<assignmentGroup identifier="%s">.*?</assignmentGroup>' % re.escape(g), "", t)
                elif not any(x in info.filename for x in new_items):
                    t = re.sub(r"\s*<assignment_group_identifierref>(%s)</assignment_group_identifierref>" % "|".join(map(re.escape, keep_groups)), "", t)
                if t != t0: data = t.encode("utf-8")
            if pat:
                name = pat.sub(lambda m: swap[m.group(0)], name)
                if re.search(r"\.(xml|html|htm|qti|json|txt|css)$", info.filename, re.I):
                    s = data.decode("utf-8", "ignore"); s2 = pat.sub(lambda m: swap[m.group(0)], s)
                    if s2 != s: n_text += 1; data = s2.encode("utf-8")
            zi = zipfile.ZipInfo(name, date_time=info.date_time); zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = info.external_attr
            zo.writestr(zi, data)
    carried = [c["id"] for c in p.get("carry_from_export", [])]
    if carried:
        ez = zipfile.ZipFile(p["export"]); eman = ez.read("imsmanifest.xml").decode("utf-8", "ignore")
        blocks, files, todo = [], [], list(carried)
        while todo:
            rid = todo.pop()
            rb = re.search(r'(?s)<resource identifier="%s"[^>]*>.*?</resource>' % re.escape(rid), eman)
            if not rb or rb.group(0) in blocks: continue
            blocks.append(rb.group(0)); files += re.findall(r'<file href="([^"]+)"', rb.group(0))
            todo += re.findall(r'<dependency identifierref="([^"]+)"', rb.group(0))
        tmp = out + ".carry"
        with zipfile.ZipFile(out) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
            for info in zi.infolist():
                data = zi.read(info.filename)
                if info.filename == "imsmanifest.xml":
                    data = data.decode("utf-8").replace("</resources>", "".join("  " + b + "\n  " for b in blocks) + "</resources>", 1).encode("utf-8")
                zo.writestr(info, data)
            for f in sorted(set(files)):
                if f in ez.namelist():
                    t = ez.read(f)
                    if pat and f.endswith((".xml", ".qti", ".html")): t = pat.sub(lambda m: swap[m.group(0)], t.decode("utf-8", "ignore")).encode("utf-8")
                    if keep_groups and f.endswith(".xml"):
                        t = re.sub(r"\s*<assignment_group_identifierref>(%s)</assignment_group_identifierref>" % "|".join(map(re.escape, keep_groups)), "", t.decode("utf-8", "ignore")).encode("utf-8")
                    zo.writestr(f, t)
        os.replace(tmp, out)
    print(json.dumps(dict(out=out, carried_from_export=len(carried), identifiers_swapped=len(swap), files_changed=n_text, groups_left_as_they_are=sorted(keep_groups), live_weights_kept=len(weights_kept), modules_left_as_they_are=[m["title"] for m in p.get("leave_out_modules", [])])))

if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) >= 3 and a[0] == "plan":
        rest = [x for x in a[3:] if x != "--json"]
        jpath = a[a.index("--json") + 1] if "--json" in a else None
        if jpath: rest = [x for x in rest if x != jpath]
        res = plan(a[1], a[2], rest)
        if jpath: json.dump(res, open(jpath, "w"), indent=1)
        print(json.dumps(res if not jpath else dict(counts=res["counts"], older=len(res["older"])), indent=1))
    elif len(a) == 2 and a[0] == "stored":
        # every stored id of a live item in this export (the app accepts a module item that links one)
        _, lv, _ = lineage(a[1], [class_folder(a[1])])
        print(json.dumps(sorted({v["stored"] for v in lv.values() if v["stored"]})))
    elif len(a) == 4 and a[0] == "apply":
        apply(a[1], a[2], a[3])
    else:
        print(__doc__); sys.exit(2)
