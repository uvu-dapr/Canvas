"""LIVE-Import builder (Standards 0a live import, 2026-09-24; Adam 2026-09-28). Platform Reference 21.1d gate 12k.

Usage (never overwrites; then run preflight.py . --live <export> on a fresh unzip of --out):
  python3 live_import.py --pkg <newest build .imscc> --export <fresh Canvas export .imscc> --out <next free LIVE-Import .imscc>
      --work <empty scratch folder> [--tiebreak <an earlier LIVE-Import that carried live ids>]
      [--rename "package title=>live title"] [--rename "module:package module=>live module"] [--now 2026-09-28T23:59]
Writes <out>.report.json: mapped count, skipped matches, quizzes left out, pages left out, items kept published,
and the live modules and items the cartridge does not contain.

Every module, module item, page, assignment, quiz, discussion, assignment group and rubric that already exists in the
live course gets its live identifier, matched by title, so the import updates it instead of adding a copy.
Quizzes students have already reached (unlocked or past due) are left out: Adam never replaces those.
Items published in live stay published; everything else keeps the package's (unpublished) state.
"""
import zipfile, re, html, sys, os, shutil, json, argparse
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument("--pkg"); ap.add_argument("--export"); ap.add_argument("--out"); ap.add_argument("--work")
ap.add_argument("--tiebreak", action="append", default=[])
ap.add_argument("--rename", action="append", default=[], help="package title=>live title (modules or items)")
import datetime
ap.add_argument("--now", default=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M"))
a = ap.parse_args()
assert not os.path.exists(a.out), "never overwrite: " + a.out

def U(s): return html.unescape(s or "").strip()
renames = dict(r.split("=>", 1) for r in a.rename if not r.startswith("module:"))
mod_renames = dict(r[7:].split("=>", 1) for r in a.rename if r.startswith("module:"))
def live_title(t): return renames.get(t, t)
def live_module(t): return mod_renames.get(t, t)

P = zipfile.ZipFile(a.pkg); E = zipfile.ZipFile(a.export)
def rd(z, n):
    try: return z.read(n).decode("utf8", "ignore")
    except KeyError: return ""
pman, eman = rd(P, "imsmanifest.xml"), rd(E, "imsmanifest.xml")
tb = [rd(zipfile.ZipFile(t), "imsmanifest.xml") for t in a.tiebreak]

def resources(man):
    out = {}
    for r in re.finditer(r'<resource\b([^>]*)>(.*?)</resource>|<resource\b([^>]*)/>', man, re.S):
        attrs = r.group(1) or r.group(3); body = r.group(2) or ""
        rid = re.search(r'identifier="([^"]+)"', attrs).group(1)
        typ = (re.search(r'type="([^"]+)"', attrs) or [None, ""])[1]
        href = (re.search(r'href="([^"]+)"', attrs) or [None, ""])[1]
        deps = re.findall(r'<dependency identifierref="([^"]+)"', body)
        files = re.findall(r'<file href="([^"]+)"', body)
        out[rid] = dict(type=typ, href=href, deps=deps, files=files)
    return out
pres, eres = resources(pman), resources(eman)

def modules(z):
    mm = rd(z, "course_settings/module_meta.xml"); out = []
    for m in re.finditer(r'<module identifier="([^"]+)">\s*<title>([^<]*)</title>(.*?)</module>', mm, re.S):
        items = []
        for it in re.finditer(r'<item identifier="([^"]+)">(.*?)</item>', m.group(3), re.S):
            b = it.group(2)
            g = lambda k: U((re.search(r"<%s>([^<]*)</%s>" % (k, k), b) or [None, ""])[1])
            items.append(dict(id=it.group(1), title=g("title"), ref=g("identifierref"), type=g("content_type"), state=g("workflow_state")))
        st = U((re.search(r"<workflow_state>([^<]*)</workflow_state>", m.group(3).split("<items>")[0]) or [None, ""])[1])
        out.append(dict(id=m.group(1), title=U(m.group(2)), state=st, items=items))
    return out
pmods, emods = modules(P), modules(E)

# A quiz's settings file, whichever layout: <id>/assessment_meta.xml (Canvas export) or quizzes/quiz_<name>_meta.xml
_names = {}
def meta_path(z, res, rid):
    names = _names.setdefault(id(z), set(z.namelist()))
    r = res.get(rid, {"files": [], "deps": []})
    for c in [f"{rid}/assessment_meta.xml"] + [f for d in [rid] + r["deps"] for f in res.get(d, {}).get("files", []) if f.endswith("meta.xml")]:
        if c in names: return c
    return ""

# Titles of every resource, from its own file (page meta title, assignment, quiz, discussion) and from module items
def res_titles(z, res, mods):
    t = defaultdict(set)
    deps = {d for r in res.values() for d in r["deps"]}   # a quiz's or discussion's settings file: mapped through its parent
    for mo in mods:
        for it in mo["items"]:
            # A link or subheader is a module item, not a resource: Canvas's module_meta points an ExternalUrl item at
            # itself, so by title its own id would be taken for the link resource's (DAPR 2020, 2026-09-28)
            if it["ref"] and it["type"] not in ("ExternalUrl", "ContextModuleSubHeader", "ContextExternalTool"): t[it["title"]].add(it["ref"])
    for rid, r in res.items():
        if rid in deps: continue
        txt = ""
        if r["href"].endswith(".html") and ("wiki_content/" in r["href"]) : txt = rd(z, r["href"])
        for f in r["files"]:
            if f.endswith("assignment_settings.xml"): txt = rd(z, f)
        if "assessment" in r["type"]: txt = rd(z, meta_path(z, res, rid))
        if r["type"] == "imsdt_xmlv1p1" and r["files"]: txt = rd(z, r["files"][0])
        m = re.search(r"<title>([^<]*)</title>", txt)
        if m and U(m.group(1)): t[U(m.group(1))].add(rid)
    return t
ptit, etit = res_titles(P, pres, pmods), res_titles(E, eres, emods)

skipped, mp = [], {}
def choose(cands, mine_href):
    c = sorted(cands)
    if len(c) == 1: return c[0]
    t = [x for x in c if any(x in m for m in tb)]
    if len(t) == 1: return t[0]
    kind = "wiki_content/" if mine_href.startswith("wiki_content/") else None
    if kind:
        k = [x for x in (t or c) if eres.get(x, {}).get("href", "").startswith(kind)]
        if len(k) == 1: return k[0]
    return None

# 1. Resources by title
for title, mine in ptit.items():
    if len(mine) != 1:
        if title and etit.get(live_title(title)): skipped.append(f'"{title}": {len(mine)} items with this title in the package')
        continue
    old = next(iter(mine)); cands = etit.get(live_title(title), set())
    if not cands or old in cands: continue
    new = choose(cands, pres.get(old, {}).get("href", ""))
    if new is None: skipped.append(f'"{title}": {len(cands)} copies in Canvas, none clearly the live one'); continue
    mp[old] = new
# 2. Modules by title, module items by module and title
for m in pmods:
    same_id = [e for e in emods if e["id"] == m["id"]]   # already carries the live id, whatever its title is now
    cands = same_id or [e for e in emods if e["title"] == live_module(m["title"])]
    ids = [e["id"] for e in cands]
    if not ids or m["id"] in ids: target = next((e for e in cands if e["id"] == m["id"]), None)
    else:
        pick = choose(set(ids), "")
        if pick is None:
            # Two live modules with one title: the one whose pages this package already shares
            refs = {it["ref"] for it in m["items"] if it["ref"]}
            share = sorted(cands, key=lambda e: -len(refs & {x["ref"] for x in e["items"]}))
            if len(share) > 1 and len(refs & {x["ref"] for x in share[0]["items"]}) > len(refs & {x["ref"] for x in share[1]["items"]}): pick = share[0]["id"]
        if pick is None: skipped.append(f'Module "{m["title"]}": {len(ids)} in Canvas'); continue
        mp[m["id"]] = pick; target = next(e for e in cands if e["id"] == pick)
    if not target: continue
    for it in m["items"]:
        cx = [x for x in target["items"] if x["title"] == live_title(it["title"]) and x["type"] == it["type"]]
        if not cx and it["ref"]:   # retitled since: the live item that points at the same page, assignment or quiz
            cx = [x for x in target["items"] if x["ref"] == it["ref"] and x["type"] == it["type"]]
        c = [x["id"] for x in cx]
        if len(c) == 1 and c[0] != it["id"]: mp[it["id"]] = c[0]
        # What students see is what the live module item points at: that copy gets updated, even when another
        # copy with the same title (an orphan the module no longer uses) has this package's id
        if len(cx) == 1 and it["ref"] and cx[0]["ref"] and it["ref"] != cx[0]["ref"] and it["type"] != "ExternalUrl":
            mp[it["ref"]] = cx[0]["ref"]
        elif len(c) > 1: skipped.append(f'Module item "{it["title"]}" in "{m["title"]}": {len(c)} in Canvas')
# 3. Companions of each mapped resource (quiz settings, discussion settings) and a quiz's gradebook assignment
for old, new in list(mp.items()):
    po, eo = pres.get(old), eres.get(new)
    if not po or not eo: continue
    if len(po["deps"]) == len(eo["deps"]):
        for x, y in zip(po["deps"], eo["deps"]):
            if x != y: mp[x] = y
    if "assessment" in po["type"]:
        pa = re.search(r'<assignment identifier="([^"]+)"', rd(P, meta_path(P, pres, old)))
        ea = re.search(r'<assignment identifier="([^"]+)"', rd(E, meta_path(E, eres, new)))
        if pa and ea and pa.group(1) != ea.group(1): mp[pa.group(1)] = ea.group(1)
# 4. Assignment groups and rubrics by title
for f, tag in [("course_settings/assignment_groups.xml", "assignmentGroup"), ("course_settings/rubrics.xml", "rubric")]:
    pat = r'<%s identifier="([^"]+)"[^>]*>\s*(?:<[^>]+>[^<]*</[^>]+>\s*)*?<title>([^<]*)</title>' % tag
    pe, ee = defaultdict(set), defaultdict(set)
    for i, t in re.findall(pat, rd(P, f)): pe[U(t)].add(i)
    for i, t in re.findall(pat, rd(E, f)): ee[U(t)].add(i)
    # Several live groups with one title: the one the live assignments and quizzes actually sit in
    used = defaultdict(int)
    for n in E.namelist():
        if n.endswith("assignment_settings.xml") or n.endswith("assessment_meta.xml"):
            for g in re.findall(r"<assignment_group_identifierref>([^<]+)<", rd(E, n)): used[g] += 1
    for t, s in pe.items():
        c = ee.get(t, set())
        if len(s) == 1 and len(c) > 1 and tag == "assignmentGroup":
            best = sorted(c, key=lambda g: -used[g])
            if used[best[0]] > used[best[1]]:
                c = {best[0]}; skipped.append(f'{tag} "{t}": {len(ee[t])} in Canvas, used the one holding {used[best[0]]} live items')
        if len(s) == 1 and len(c) == 1 and s != c: mp[next(iter(s))] = next(iter(c))
        elif c and not (s & c): skipped.append(f'{tag} "{t}": {len(s)} here, {len(c)} in Canvas')
# One to one, and never onto an id this package already uses
used_pkg = set(re.findall(r'identifier(?:ref)?="([^"]+)"', pman))
count = defaultdict(int)
for v in mp.values(): count[v] += 1
# A target this package already uses is fine when that use is itself moving away (ids swapped between items: all
# rewrites happen in one pass); repeated until stable, since dropping one mapping can strand another
while True:
    bad = [k for k in mp if count[mp[k]] > 1 or (mp[k] in used_pkg and mp[k] not in mp)]
    if not bad: break
    for k in bad:
        skipped.append(f"{k} -> {mp[k]}: clash, left alone"); count[mp[k]] -= 1; del mp[k]

# 5. Unzip, leave out quizzes students have reached, mirror live publish state, rewrite ids, zip
w = a.work; shutil.rmtree(w, ignore_errors=True); P.extractall(w)
shutil.rmtree(os.path.join(w, "__MACOSX"), ignore_errors=True)
def rp(p): return os.path.join(w, p)
def read(p): return open(rp(p), encoding="utf8").read()
def write(p, s): open(rp(p), "w", encoding="utf8").write(s)

alt0 = "|".join(re.escape(k) for k in sorted(mp, key=len, reverse=True))
rx0 = re.compile(r"(?<![A-Za-z0-9_])(%s)(?![A-Za-z0-9_])" % alt0) if mp else None
left_out = []; left_ids = set()
man = read("imsmanifest.xml"); mm = read("course_settings/module_meta.xml")
for rid, r in pres.items():
    if "assessment" not in r["type"]: continue
    meta = rd(P, meta_path(P, pres, rid))
    g = lambda k: (re.search(r"<%s>([^<]*)</%s>" % (k, k), meta) or [None, ""])[1]
    title, un, due = U(g("title")), g("unlock_at"), g("due_at")
    if not due:
        m = re.search(r"<assignment[^>]*>.*?<due_at>([^<]*)</due_at>", meta, re.S); due = m.group(1) if m else ""
    # Only a quiz students can reach in live is left out: published there, or already past due there
    lid = mp.get(rid, rid)
    lmeta = rd(E, meta_path(E, eres, lid)) if lid in eres else ""
    lg = lambda k: (re.search(r"<%s>([^<]*)</%s>" % (k, k), lmeta) or [None, ""])[1]
    live_seen = bool(lmeta) and ("<available>true</available>" in lmeta or (lg("due_at") and lg("due_at") < a.now))
    if live_seen:
        left_out.append((title, un[:10], due[:10])); left_ids.add(rid)
        for f in r["files"]:
            if os.path.exists(rp(f)): os.remove(rp(f))
        for x in [rid] + r["deps"]:
            man = re.sub(r'\s*<resource\b[^>]*identifier="%s"[^>]*>.*?</resource>' % re.escape(x), "", man, flags=re.S)
        man = re.sub(r'\s*<item identifier="[^"]+" identifierref="%s">\s*<title>[^<]*</title>\s*</item>' % re.escape(rid), "", man)
        mm = re.sub(r'\s*<item identifier="[^"]+">(?:(?!</item>).)*?<identifierref>%s</identifierref>.*?</item>' % re.escape(rid), "", mm, flags=re.S)
        shutil.rmtree(rp(rid), ignore_errors=True)
        for f in [f"non_cc_assessments/{rid}.xml.qti"]:
            if os.path.exists(rp(f)): os.remove(rp(f))
        for d in r["deps"]:
            for f in pres.get(d, {}).get("files", []):
                if os.path.exists(rp(f)): os.remove(rp(f))

# Pages that link to a left-out quiz: unchanged from live, they stay out too (the live page already links to it);
# changed ones stay in and are reported, because their quiz link may not resolve
def words(s): return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<head.*?</head>", "", s))).split())
kept_with_links, dropped_pages = [], []
for rid, r in pres.items():
    if not r["href"].startswith("wiki_content/") or not os.path.exists(rp(r["href"])): continue
    s = read(r["href"])
    # A real quiz link to a left-out quiz ($CANVAS_OBJECT_REFERENCE$/quizzes/<id>), by its id here or its live id
    hits = [q for q in left_ids if re.search(r"quizzes/(%s)(?![A-Za-z0-9_])" % "|".join(re.escape(x) for x in {q, mp.get(q, q)}), s)]
    if not hits: continue
    er = eres.get(mp.get(rid, rid)); live = rd(E, er["href"]) if er and er["href"] else ""
    title = U((re.search(r"<title>([^<]*)", s) or [0, rid])[1])
    if live and words(live) == words(rx0.sub(lambda m: mp[m.group(1)], s) if rx0 else s):
        man = re.sub(r'\s*<resource\b[^>]*identifier="%s"[^>]*>.*?</resource>' % re.escape(rid), "", man, flags=re.S)
        man = re.sub(r'\s*<item identifier="[^"]+" identifierref="%s">\s*<title>[^<]*</title>\s*</item>' % re.escape(rid), "", man)
        mm = re.sub(r'\s*<item identifier="[^"]+">(?:(?!</item>).)*?<identifierref>%s</identifierref>.*?</item>' % re.escape(rid), "", mm, flags=re.S)
        os.remove(rp(r["href"])); dropped_pages.append(title)
    else:
        # Changed since live, but its quiz link could not resolve without the quiz: the live page (whose link works)
        # stays, and the page is listed so the change can be made by hand
        man = re.sub(r'\s*<resource\b[^>]*identifier="%s"[^>]*>.*?</resource>' % re.escape(rid), "", man, flags=re.S)
        man = re.sub(r'\s*<item identifier="[^"]+" identifierref="%s">\s*<title>[^<]*</title>\s*</item>' % re.escape(rid), "", man)
        mm = re.sub(r'\s*<item identifier="[^"]+">(?:(?!</item>).)*?<identifierref>%s</identifierref>.*?</item>' % re.escape(rid), "", mm, flags=re.S)
        os.remove(rp(r["href"])); kept_with_links.append(title)

# Publish state: what students can see in live stays visible
published = []
live_mod_state = {m["id"]: m["state"] for m in emods}
for m in pmods:
    lid = mp.get(m["id"], m["id"])
    if live_mod_state.get(lid) == "active":
        # The module's own state sits before <items> in any field order (Canvas: title then state; v90: title, position, state)
        mm, n = re.subn(r'(<module identifier="%s">(?:(?!<items>|</module>).)*?<workflow_state>)unpublished' % re.escape(m["id"]), r"\1active", mm, flags=re.S)
        if n: published.append("module " + m["title"])
write("imsmanifest.xml", man); write("course_settings/module_meta.xml", mm)
for rid, r in pres.items():
    lid = mp.get(rid, rid); er = eres.get(lid)
    if not er or not os.path.exists(rp(r["href"] or "x")) and not r["files"]: continue
    if r["href"].startswith("wiki_content/") and er["href"]:
        if re.search(r'name="workflow_state" content="active"', rd(E, er["href"])) and os.path.exists(rp(r["href"])):
            s = read(r["href"]); s2 = re.sub(r'(name="workflow_state" content=")unpublished', r"\1active", s)
            if s2 != s: write(r["href"], s2); published.append("page " + (re.search(r"<title>([^<]*)", s) or [0, rid])[1])
    for f in r["files"]:
        if f.endswith("assignment_settings.xml") and os.path.exists(rp(f)):
            lf = next((x for x in er["files"] if x.endswith("assignment_settings.xml")), None)
            if lf and "<workflow_state>published</workflow_state>" in rd(E, lf):
                s = read(f); s2 = s.replace("<workflow_state>unpublished</workflow_state>", "<workflow_state>published</workflow_state>", 1)
                if s2 != s: write(f, s2); published.append("assignment " + U((re.search(r"<title>([^<]*)", s) or [0, rid])[1]))
    if "assessment" in r["type"] and rid not in left_ids and meta_path(P, pres, rid) and os.path.exists(rp(meta_path(P, pres, rid))):
        lm = rd(E, meta_path(E, eres, lid))
        if "<available>true</available>" in lm:
            f = meta_path(P, pres, rid); s = read(f); s2 = s.replace("<available>false</available>", "<available>true</available>").replace("<workflow_state>unpublished</workflow_state>", "<workflow_state>active</workflow_state>", 1)
            if s2 != s: write(f, s2); published.append("quiz " + U((re.search(r"<title>([^<]*)", s) or [0, rid])[1]))

# Rewrite ids in every text file, then in file and folder names (deepest first)
alt = "|".join(re.escape(k) for k in sorted(mp, key=len, reverse=True))
rx = re.compile(r"(?<![A-Za-z0-9_])(%s)(?![A-Za-z0-9_])" % alt) if mp else None
changed = 0
for root, dirs, files in os.walk(w):
    for f in files:
        p = os.path.join(root, f)
        if rx and f.rsplit(".", 1)[-1].lower() in ("xml", "html", "htm", "qti", "json", "txt", "css"):
            s = open(p, encoding="utf8", errors="ignore").read(); t = rx.sub(lambda m: mp[m.group(1)], s)
            if t != s: open(p, "w", encoding="utf8").write(t); changed += 1
paths = []
for root, dirs, files in os.walk(w):
    for n in dirs + files: paths.append(os.path.join(root, n))
for p in sorted(paths, key=lambda x: -x.count(os.sep)):
    n = os.path.basename(p); t = rx.sub(lambda m: mp[m.group(1)], n) if rx else n
    if t != n: os.rename(p, os.path.join(os.path.dirname(p), t))
for root, dirs, files in os.walk(w):
    for f in files:
        if f == ".DS_Store": os.remove(os.path.join(root, f))
import subprocess
subprocess.run(["zip", "-q", "-r", "-D", "-X", a.out, ".", "-x", "*.DS_Store", "__MACOSX/*"], cwd=w, check=True)

# 6. What is in live but not in this cartridge (for Adam to review by hand)
out_titles = set(res_titles(zipfile.ZipFile(a.out), resources(rd(zipfile.ZipFile(a.out), "imsmanifest.xml")), modules(zipfile.ZipFile(a.out))))
not_in = sorted(t for t in etit if t not in out_titles and t not in {live_title(x) for x in out_titles})
live_mods_not_in = sorted({e["title"] for e in emods} - {live_title(m["title"]) for m in modules(zipfile.ZipFile(a.out))})
json.dump(dict(dropped_unchanged_pages=dropped_pages, changed_pages_left_out_for_quiz_links=kept_with_links, mapped=len(mp), changed_files=changed, skipped=skipped, left_out=left_out, published=published,
               live_items_not_in=not_in, live_modules_not_in=live_mods_not_in), open(a.out + ".report.json", "w"), indent=1)
print(f"mapped {len(mp)} ids in {changed} files; skipped {len(skipped)}; quizzes left out {len(left_out)}; kept published {len(published)}")
