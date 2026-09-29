#!/usr/bin/env python3
"""module_order.py: every module in the order Adam set on 2026-09-29, and graded items named to match.

    Readings first. Graded work at the very end of each module: assignments, then the quiz. One CONTENT AND
    RESOURCES and one QUIZZES AND ASSIGNMENTS heading per module (no lab sections in any class). Graded items are
    "Topic: Assignment - Name" and "Topic: Quiz - Name", Topic being the prefix the module's own pages use.
    Repeated links in a module are removed. Work students took is never renamed by a package: it is listed for
    Adam to rename by hand. DAPR Canvas Standards 6.9 and 16a.

    python3 module_order.py plan  <package .imscc or folder> [--live <Canvas export .imscc>] [--report <.report.json>] [--out plan.json]
    python3 module_order.py apply <unzipped folder> <plan.json> [--live <Canvas export .imscc>] [--all]

plan prints (or writes) a JSON plan: per module its items now, the new order, removals and renames. Canvas Preview's
Workbench > Module Order shows it side by side and lets Adam adjust it. apply writes a plan into an unzipped package
(a working copy, never the package itself) and stops without writing if any module does not hold exactly the plan's
items. --all also renames work students took (for a full teaching copy, never a LIVE-Import).
"""
import sys, re, os, json, zipfile, html, collections

GRADED = ("Assignment", "Quizzes::Quiz", "DiscussionTopic")
MODULE = [""]
STD = ("CONTENT AND RESOURCES", "QUIZZES AND ASSIGNMENTS")

def e(s): return html.escape(s)

def object_titles(z):
    """Assignment, quiz and graded discussion titles by identifier, from their own files (a module item's title can differ)."""
    out = {}
    for n in z.namelist():
        if n.endswith(("/assignment_settings.xml", "/assessment_meta.xml")) or (n.startswith("discussions/") or re.match(r"^[^/]+\.xml$", n)):
            try: s = z.read(n).decode("utf-8", "ignore")
            except KeyError: continue
            m = re.search(r'<(?:assignment|quiz|topicMeta)\b[^>]*\bidentifier="([^"]+)"', s); t = re.search(r"<title>([^<]*)</title>", s)
            if m and t: out[m.group(1)] = html.unescape(t.group(1)); out["file:" + n] = out[m.group(1)]
    # a module item points at a manifest resource, whose files may sit in a folder with another name (3340)
    man = z.read("imsmanifest.xml").decode("utf-8", "ignore")
    for r in re.finditer(r'(?s)<resource identifier="([^"]+)"[^>]*>(.*?)</resource>', man):
        for f in re.findall(r'href="([^"]+)"', r.group(0)):
            if "file:" + f in out: out.setdefault(r.group(1), out["file:" + f])
    return out

def modules(p):
    z = zipfile.ZipFile(p); OT = object_titles(z)
    mm = z.read("course_settings/module_meta.xml").decode("utf-8", "ignore")
    out = []
    for m in re.finditer(r'(?s)<module identifier="([^"]+)">(.*?)</module>', mm):
        t = html.unescape(re.search(r"<title>([^<]*)", m.group(2)).group(1))
        items = []
        for i in re.finditer(r'(?s)<item identifier="([^"]+)">(.*?)</item>', m.group(2)):
            g = lambda k: html.unescape((re.search(r"<%s>([^<]*)" % k, i.group(2)) or [None, ""])[1])
            it = dict(id=i.group(1), k=g("content_type"), t=g("title"), ref=g("identifierref"), url=g("url"))
            if it["k"] in GRADED and it["ref"] in OT: it["t"] = OT[it["ref"]]; it["own"] = True
            items.append(it)
        out.append((m.group(1), t, items))
    return out

def _n(s): return re.sub(r"[^a-z0-9]+", " ", s.lower().replace("&", " and ")).strip()

def prefix_of(mt, items):
    """The module's topic prefix. Its own items' prefixes decide; spelled as the module title spells it (with &)."""
    short = mt.split(":", 1)[1].strip() if ":" in mt else mt
    # A graded item already in the right form names the prefix ("Sound: Assignment - The Decibel in the Real World")
    good = collections.Counter(m.group(1).strip() for x in items if x["k"] in GRADED for m in [re.match(r"^([^:]{2,60}): (?:Assignment|Quiz)( - |$)", x["t"])] if m)
    c = collections.Counter()
    for x in items:
        if x["k"] != "WikiPage": continue          # readings decide; slide link titles use the short module name
        m = re.match(r"^([^:]{2,60}):\s", x["t"])
        if m:
            k = m.group(1).strip()
            fam = mt.split(":", 1)[0].strip() if ":" in mt else ""
            if fam and _n(fam).startswith(_n(k)): k = fam          # 3255's "Network:" pages in the "Networking:" family
            c[k] += 1
    if any(_n(k) == _n(short) for k in c): return short, False
    near = [k for k in c if (_n(short) in _n(k) or _n(k) in _n(short)) and len(_n(k)) >= 0.6 * len(_n(short))]
    if near: return max(near, key=lambda k: (c[k], len(k))), False
    if c and c.most_common(1)[0][1] >= 2: return c.most_common(1)[0][0], False
    if good: return good.most_common(1)[0][0], False     # no reading prefixes: a graded item already in the right form
    return short, True

def new_name(x, pre):
    t = x["t"]
    if x["k"] == "Assignment" and re.search(r"^%s: Assignment( - |$)" % re.escape(pre), t): return None
    if x["k"] == "Quizzes::Quiz" and (re.search(r"^%s: Quiz( - |$)" % re.escape(pre), t) or "Final Exam" in t): return None
    if x["k"] == "DiscussionTopic": return None
    # Attendance and Bonus work keep their own forms (Standards 6: "[Normal Name] (Bonus)")
    if re.search(r"(?i)attendance|roll call|\(Bonus\)|^Bonus:", t) or pre.lower().startswith(("optional builds", "bonus")): return None
    kind = "Assignment" if x["k"] == "Assignment" else "Quiz"
    name = t
    if name.startswith(pre + ":"): name = name[len(pre) + 1:].strip()
    fam = re.match(r"^([^:]{2,40}):\s+(.+)$", name)
    if fam and re.match(r"^(Assignment|Quiz)\b", fam.group(2)): name = fam.group(2); fam = None
    name = re.sub(r"^(Assignment|Quiz)\s*-\s*", "", name)
    if fam and not re.match(r"^P\d", fam.group(1)) and (_n(fam.group(1)) in _n(MODULE[0]) or _n(fam.group(1)) in _n(pre)): name = fam.group(2)
    name = re.sub(r"^(Assignment|Quiz)\s*-\s*", "", name)
    name = re.sub(r"^Exercise\s*-\s*(.+)$", r"\1 Exercise", name)      # 3340's "Exercise - Surround Monitoring"
    name = re.sub(r"\s*(Assignment|Quiz)$", "", name).strip(" -:")
    if kind == "Quiz" and name.lower() in ("", pre.lower()): return "%s: Quiz" % pre
    return "%s: %s - %s" % (pre, kind, name) if name else "%s: %s" % (pre, kind)

def plan_module(mt, items, taken):
    real = [x for x in items]
    # 1. repeated links (same url or same target) in one module: keep the first
    seen, drop = set(), []
    for x in real:
        key = x["url"] or x["ref"]
        if x["k"] != "ContextModuleSubHeader" and key:
            if key in seen: drop.append(x); continue
            seen.add(key)
    keep = [x for x in real if x not in drop]
    # 2. split: the top (items before the first heading, not graded), readings with any custom headings, graded work
    first_h = next((i for i, x in enumerate(keep) if x["k"] == "ContextModuleSubHeader"), len(keep))
    slides = lambda x: x["k"] == "ExternalUrl" and re.search(r"Slides\b.*\(PDF\)", x["t"])
    if first_h < len(keep):
        top = [x for x in keep[:first_h] if x["k"] not in GRADED]      # the overview and slides above the first heading
    else:
        top = []                                                        # no headings: the leading overview and slides
        for x in keep:
            if x["k"] in GRADED or not (slides(x) or "overview" in x["t"].lower() or not top and x["k"] == "WikiPage"): break
            top.append(x)
    # every slide deck link belongs at the top with the first one (2255 had its second deck after the quiz)
    top += [x for x in keep if slides(x) and x not in top]
    rest = [x for x in keep if x not in top]
    std_heads = [x for x in rest if x["k"] == "ContextModuleSubHeader" and x["t"] in STD]
    graded = [x for x in rest if x["k"] in GRADED]
    readings = [x for x in rest if x["k"] not in GRADED and not (x["k"] == "ContextModuleSubHeader" and x["t"] in STD)]
    # a custom heading that only introduced graded work ("P6: Project and Quiz") goes down with it
    tail_heads = []
    while readings and readings[-1]["k"] == "ContextModuleSubHeader":
        tail_heads.insert(0, readings.pop())
    assign = [x for x in graded if x["k"] != "Quizzes::Quiz"]
    quizzes = sorted([x for x in graded if x["k"] == "Quizzes::Quiz"], key=lambda x: "Final Exam" in x["t"])
    c_head = next((x for x in std_heads if x["t"] == STD[0]), None)
    q_head = next((x for x in std_heads if x["t"] == STD[1]), None)
    extra_heads = [x for x in std_heads if x is not c_head and x is not q_head]
    if std_heads:
        after = top + ([c_head] if c_head else []) + readings + tail_heads + ([q_head] if q_head else []) + assign + quizzes
    else:
        after = top + readings + tail_heads + assign + quizzes
    drop += extra_heads
    pre, guessed = prefix_of(mt, items); MODULE[0] = mt
    renames = {}
    for x in graded:
        n = new_name(x, pre)
        if n and n != x["t"]: renames[x["id"]] = n
    # moved = the fewest items that really change place: everything outside the longest run kept in the same order
    b = [x["id"] for x in keep if x not in extra_heads]; a = [x["id"] for x in after]
    rank = [b.index(i) for i in a]; best = [1] * len(rank); prev = [-1] * len(rank)
    for i in range(len(rank)):
        for j in range(i):
            if rank[j] < rank[i] and best[j] + 1 > best[i]: best[i], prev[i] = best[j] + 1, j
    stay = set(); i = max(range(len(rank)), key=lambda k: best[k]) if rank else -1
    while i >= 0: stay.add(a[i]); i = prev[i]
    moved = set(a) - stay
    return dict(after=after, drop=drop, renames=renames, moved=moved, prefix=pre, guessed=guessed)


def plan_package(pkg, live=None, report=None):
    """The plan for one package (an .imscc or an unzipped folder). report: the LIVE-Import's .report.json, which names
    the work students took (a working folder has none of its own)."""
    src = zip_or_dir(pkg)
    taken = set(); rep = report or pkg + ".report.json"
    if os.path.exists(rep):
        taken = {t.get("title") for t in json.load(open(rep)).get("taken_items", [])}
    liveids = {x["id"] for _, _, its in modules(live) for x in its} if live else set()
    OTL = object_titles(zipfile.ZipFile(live)) if live else {}
    out = {"package": pkg, "live": live, "modules": {}}
    for mid, mt, items in modules(src):
        if "Instructor Use Only" in mt: continue
        p = plan_module(mt, items, taken)
        hand = {x["id"] for x in items if x["id"] in p["renames"] and (x["t"] in taken or OTL.get(x["ref"]) in taken)}
        fromexport = {x["id"] for x in items if x["id"] in p["renames"] and x["id"] not in hand and live and not x.get("own")}
        out["modules"][mid] = dict(
            title=mt, prefix=p["prefix"], guessed=p["guessed"],
            now=[dict(id=x["id"], kind=x["k"], title=x["t"], live=x["id"] in liveids, taken=x["id"] in hand or x["t"] in taken) for x in items],
            order=[x["id"] for x in p["after"]], drop=[x["id"] for x in p["drop"]],
            drop_live=[x["id"] for x in p["drop"] if x["id"] in liveids], moved=sorted(p["moved"]),
            renames={k: v for k, v in p["renames"].items() if k not in hand},
            by_hand={k: v for k, v in p["renames"].items() if k in hand}, from_export=sorted(fromexport))
    return out

def zip_or_dir(pkg):
    """modules() and object_titles() read a zip; a folder is read through a zip made in memory."""
    if not os.path.isdir(pkg): return pkg
    import io
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for root, _, fs in os.walk(pkg):
            for f in fs:
                if f.endswith((".xml", ".qti")): z.write(os.path.join(root, f), os.path.relpath(os.path.join(root, f), pkg))
    buf.seek(0); return buf


def apply_plan(W, plan, LIVE=None, ALL=False):
    """Writes a plan's order, removals and renames into the unzipped package W. Returns what it did."""
    def rd(p): return open(os.path.join(W, p), encoding="utf-8").read()
    def wr(p, s): open(os.path.join(W, p), "w", encoding="utf-8").write(s)
    def xesc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    def aesc(t): return xesc(t).replace('"', "&quot;")

    mm, man = rd("course_settings/module_meta.xml"), rd("imsmanifest.xml")
    report = {"renamed": [], "removed": [], "copied_from_export": [], "moved_modules": 0, "text_links": 0}

    def block_end(s, start, tag="item"):
        """Index just past the </item> matching the <item ...> that opens at start (items nest in the manifest)."""
        depth, i = 0, start
        for m in re.compile(r"<%s\b[^>]*?(/?)>|</%s>" % (tag, tag)).finditer(s, start):
            if m.group(0).startswith("</"): depth -= 1
            elif not m.group(1): depth += 1
            if depth == 0: return m.end()
        raise ValueError("unclosed item")

    renames_all, refs = {}, {}
    RESFILES = {r.group(1): re.findall(r'href="([^"]+)"', r.group(0)) for r in re.finditer(r'(?s)<resource identifier="([^"]+)"[^>]*>.*?</resource>', man)}
    def settings_for(ref, name):
        """The settings file of the object a module item points at: <ref>/<name>, or wherever the manifest puts it."""
        if os.path.exists(os.path.join(W, ref, name)): return ref + "/" + name
        for f in RESFILES.get(ref, []):
            if f.endswith("/" + name) and os.path.exists(os.path.join(W, f)): return f
        return None
    export = zipfile.ZipFile(LIVE) if LIVE else None
    export_man = export.read("imsmanifest.xml").decode("utf-8", "ignore") if export else ""

    for mid, p in plan.items():
        # a module the plan leaves as it is is not touched (its manifest entry may list things differently, harmlessly)
        if not p.get("drop") and not p.get("renames") and not (ALL and p.get("by_hand")) and p["order"] == [x["id"] for x in p.get("now", [])]:
            continue
        # ---- module_meta.xml
        m = re.search(r'(?s)<module identifier="%s">.*?</module>' % re.escape(mid), mm)
        assert m, "module %s not in module_meta" % mid
        mod = m.group(0)
        its = {i.group(1): i.group(0) for i in re.finditer(r'(?s)<item identifier="([^"]+)">.*?</item>', mod)}
        want, drop = p["order"], set(p["drop"])
        assert set(its) == set(want) | drop and not (set(want) & drop), "module %s items differ from the plan (%s)" % (p["title"], sorted(set(its) ^ (set(want) | drop))[:4])
        ren = dict(p["renames"])                     # by_hand items (students took them) are never renamed by a LIVE-Import
        if ALL: ren.update(p.get("by_hand", {}))      # a full teaching copy carries every new name
        items_xml = []
        for n, iid in enumerate(want, 1):
            b = its[iid]
            b = re.sub(r"<position>\d+</position>", "<position>%d</position>" % n, b)
            if iid in ren:
                b = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % xesc(ren[iid]), b, count=1)
            r = re.search(r"<identifierref>([^<]*)</identifierref>", b)
            if r: refs[iid] = r.group(1)
            items_xml.append(b)
        body = mod[mod.index("<items>") + len("<items>"):mod.index("</items>")]
        indent = re.match(r"\s*", body).group(0) or "\n      "
        new_mod = mod[:mod.index("<items>") + len("<items>")] + indent + indent.join(items_xml) + re.sub(r"^.*?(\s*)$", r"\1", body, flags=re.S) + mod[mod.index("</items>"):]
        mm = mm.replace(mod, new_mod)
        report["moved_modules"] += 1
        for iid in drop: report["removed"].append((p["title"], re.search(r"<title>([^<]*)</title>", its[iid]).group(1)))
        for iid, t in ren.items(): renames_all[iid] = (t, html.unescape(re.search(r"<title>([^<]*)</title>", its[iid]).group(1)))
        # ---- imsmanifest.xml organization: the module's children in the same order
        s = man.find('<item identifier="%s">' % mid)
        if s >= 0:
            e = block_end(man, s); org = man[s:e]
            first = re.search(r"<item identifier=", org[1:])
            if first:
                head_end = first.start() + 1                          # where the first child starts
                sep = re.search(r"(\s*)<item identifier=", org[1:]).group(1)   # the spacing before each child
                kids, k = {}, head_end
                while True:
                    mk = re.compile(r'<item identifier="([^"]+)"').search(org, k)
                    if not mk: break
                    ke = block_end(org, mk.start()); kids[mk.group(1)] = org[mk.start():ke]; k = ke
                closing = org[k:]                                     # spacing and </item> after the last child
                # the manifest's own item ids can differ from module_meta's (2255): match by target, then by title
                byref, bytitle = {}, {}
                for iid in set(want) | drop:
                    r = re.search(r"<identifierref>([^<]*)</identifierref>", its[iid]); t = re.search(r"<title>([^<]*)</title>", its[iid]).group(1)
                    if r: byref.setdefault(r.group(1), []).append(iid)
                    else: bytitle.setdefault(t, []).append(iid)
                kid_for = {}
                for kid, kb in kids.items():
                    if kid in its: kid_for[kid] = kid; continue
                    r = re.search(r'identifierref="([^"]+)"', kb[:300]); t = re.search(r"<title>([^<]*)</title>", kb).group(1)
                    pool = byref.get(r.group(1), []) if r else bytitle.get(t, [])
                    pool = [x for x in pool if x not in kid_for.values()]
                    assert pool, "manifest item %s matches nothing in the module (%s)" % (kid, t)
                    kid_for[kid] = pool[0]
                kids = {kid_for[k]: v for k, v in kids.items()}
                out = []
                for iid in want:
                    if iid not in kids: continue
                    b = kids[iid]
                    if iid in ren: b = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % xesc(ren[iid]), b, count=1)
                    out.append(b)
                new_org = org[:head_end] + sep.join(out) + closing if out else org[:head_end - len(sep)] + closing
            else:
                new_org = org
            man = man[:s] + new_org + man[e:]
        # ---- removed repeats: a web link used only by the removed item goes too
        for iid in drop:
            r = re.search(r"<identifierref>([^<]*)</identifierref>", its[iid])
            if not r: continue
            ref = r.group(1)
            if mm.count(ref) == 0 and man.count('identifierref="%s"' % ref) == 0:
                rm = re.search(r'(?s)\n?[ \t]*<resource identifier="%s"[^>]*>.*?</resource>' % re.escape(ref), man)
                if rm and "imswl" in rm.group(0):
                    f = re.search(r'href="([^"]+)"', rm.group(0)).group(1)
                    man = man.replace(rm.group(0), "")
                    if os.path.exists(os.path.join(W, f)): os.remove(os.path.join(W, f))

    # ---- live items the package left out unchanged: copy them from the Canvas export so the import can rename them
    for mid, p in plan.items():
        for iid in p.get("from_export", []):
            if iid not in renames_all: continue
            ref = refs.get(iid)
            if not ref or os.path.exists(os.path.join(W, ref)) or ref in RESFILES: continue
            assert export, "a Canvas export is needed to copy %s" % ref
            rm = re.search(r'(?s)<resource identifier="%s"[^>]*>.*?</resource>' % re.escape(ref), export_man)
            assert rm, "%s is not in the Canvas export" % ref
            files = re.findall(r'<file href="([^"]+)"', rm.group(0))
            for f in files + ["non_cc_assessments/%s.xml.qti" % ref]:
                if f in export.namelist():
                    os.makedirs(os.path.dirname(os.path.join(W, f)) or W, exist_ok=True)
                    open(os.path.join(W, f), "wb").write(export.read(f))
            man = man.replace("</resources>", "  " + rm.group(0) + "\n  </resources>", 1)
            report["copied_from_export"].append(renames_all[iid][1])

    # ---- the objects themselves, their page heading, and link text elsewhere
    def replace_text_nodes(s, old, new):
        n = 0
        for o in {old, xesc(old)}:
            pat = ">" + o + "<"
            if pat in s: n += s.count(pat); s = s.replace(pat, ">" + xesc(new) + "<")
        return s, n

    olds = {}
    for iid, (new, old_item) in renames_all.items():
        ref = refs.get(iid)
        old_obj = None
        fa, fq = (settings_for(ref, "assignment_settings.xml"), settings_for(ref, "assessment_meta.xml")) if ref else (None, None)
        if fa:
            f = fa; s = rd(f); ref = os.path.dirname(fa)
            old_obj = html.unescape(re.search(r"<title>([^<]*)</title>", s).group(1))
            wr(f, re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % xesc(new), s, count=1))
            for h in os.listdir(os.path.join(W, ref)):
                if h.endswith(".html"):
                    t = rd(ref + "/" + h); t2, n = replace_text_nodes(t, old_obj, new)
                    t2 = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % xesc(new), t2, count=1)
                    if t2 != t: wr(ref + "/" + h, t2)
        elif fq:
            f = fq; s = rd(f); ref = os.path.dirname(fq)
            old_obj = html.unescape(re.search(r"<title>([^<]*)</title>", s).group(1))
            wr(f, s.replace("<title>%s</title>" % xesc(old_obj), "<title>%s</title>" % xesc(new)))
            for q in (ref + "/assessment_qti.xml", "non_cc_assessments/%s.xml.qti" % ref):
                if os.path.exists(os.path.join(W, q)):
                    s = rd(q); wr(q, re.sub(r'(<assessment [^>]*?\btitle=")[^"]*(")', lambda m: m.group(1) + aesc(new) + m.group(2), s, count=1))
        report["renamed"].append((old_obj or old_item, new))
        for o in {old_obj, old_item} - {None, ""}: olds[o] = new

    # link text on every page: a text node that is exactly an old name
    for root, _, fs in os.walk(W):
        for f in fs:
            if not f.endswith(".html"): continue
            p = os.path.relpath(os.path.join(root, f), W); s = rd(p); s0 = s
            for o, n in olds.items():
                s, k = replace_text_nodes(s, o, n); report["text_links"] += k
            if s != s0: wr(p, s)

    wr("course_settings/module_meta.xml", mm); wr("imsmanifest.xml", man)
    return report


def main():
    a = sys.argv[1:]
    opt = lambda k: a[a.index(k) + 1] if k in a else None
    if a[:1] == ["plan"] and len(a) > 1:
        p = plan_package(a[1], opt("--live"), opt("--report"))
        js = json.dumps(p, indent=1)
        if opt("--out"): open(opt("--out"), "w").write(js)
        else: print(js)
    elif a[:1] == ["apply"] and len(a) > 2:
        plan = json.load(open(a[2]))
        r = apply_plan(a[1], plan["modules"] if "modules" in plan else plan, opt("--live"), "--all" in a)
        print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in r.items()}))
    else:
        print(__doc__); sys.exit(2)

if __name__ == "__main__":
    main()
