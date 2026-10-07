# J149 (2026-10-07): the whole Blueprint (BLU_Olson_Course Resources) as one Full package, reorganized, for Adam to
# see every change in Canvas Preview. Built from the 2026-10-07 export:
#   - Student Essentials keeps 1A to 2C, 3A Resources & Links, 3B Course Media, 3C Course Legend (was 3E), 4A, 4B
#   - NEW "Protocols and Standards" and "General Reference" modules right after it, holding the moved pages
#     (renamed Protocols: / Reference:) and the three new pages (blueprint_j144/*.body.html)
#   - the app session's 9 fixes (Blueprint Fixes copy page textareas: BOAA pictures from Cloudflare, banners,
#     3A dead links, Name and time note) applied as written
# All 72 Blueprint items were made in Canvas (match_ids: original), so importing this on top of the live Blueprint
# would add copies; it is for preview, or for an empty course.
# Usage: python3 blueprint_full_j149.py <export .imscc> <Blueprint Fixes copy page .html> <output .imscc> <empty work folder>
# Extracts and repacks with zipfile, keeping every original entry name (zip/unzip mangle the U+202F in a course image name).
import sys, os, re, html, hashlib, urllib.parse
SRC, FIXES, OUT, W = sys.argv[1:5]
import zipfile
zipfile.ZipFile(SRC).extractall(W)
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blueprint_j144")
U = html.unescape
def gid(*p): return "g" + hashlib.md5("|".join(("blu-j144",) + p).encode()).hexdigest()   # same ids as v7's new items
MM = os.path.join(W, "course_settings/module_meta.xml"); MAN = os.path.join(W, "imsmanifest.xml")
mm = open(MM).read(); man = open(MAN).read()
def title_of(block): return U(re.search(r"<title>([^<]*)</title>", block).group(1)).strip()
def modblock(prefix): return next(b for b in re.findall(r'<module identifier="[^"]+">.*?</module>', mm, re.S) if title_of(b).startswith(prefix))
def items(b): return re.findall(r'<item identifier=.*?</item>', b, re.S)
def settitle(block, t): return re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % html.escape(t, quote=False), block, count=1)
def setind(it, n): return re.sub(r"<indent>\d+</indent>", "<indent>%d</indent>" % n, it)
def renum(lst): return [re.sub(r"<position>\d+</position>", "<position>%d</position>" % k, it, count=1) for k, it in enumerate(lst, 1)]
def page_file(ref):
    return re.search(r'<resource identifier="%s"[^>]*href="([^"]+)"' % re.escape(ref), man).group(1)
def ref_of(it): m = re.search(r"<identifierref>([^<]*)</identifierref>", it); return m and m.group(1)

# ---------- 1. the app session's 9 fixes, as written
fx = open(FIXES).read()
bodies = [U(b) for b in re.findall(r'<textarea id="t\d+"[^>]*>(.*?)</textarea>', fx, re.S)]
assert len(bodies) == 9, len(bodies)
def all_files():
    for d, _, fs in os.walk(W):
        for f in fs:
            if f.endswith(".html"): yield os.path.join(d, f)
fixed = []
titles = {}
for p in all_files():
    s = open(p).read(); m = re.search(r"<title>([^<]*)</title>", s)
    if m: titles[re.sub(r"^Assignment: ", "", U(m.group(1)).strip())] = p
FIX_TITLES = ["BOAA Lab: Lesson 01: Studio Login and File Access", "BOAA Lab: Lesson 02: Understanding Output Paths and Monitoring",
    "BOAA Lab: Lesson 03: First Launch of Pro Tools", "BOAA Lab: Lesson 06: Optional PreSonus FaderPort 8 Configuration",
    "Essentials: 1A) Universal Class Policies & Expectations - Content", "Essentials: 2B) Canvas Student Orientation",
    "Essentials: 3A) Resources & Links", "Bonus: Student Rating of Instructor", "BOAA Lab: LC623a Studio Proficiency Assessment"]
for t, body in zip(FIX_TITLES, bodies):
    key = next((k for k in titles if k.lower() == t.lower()), None)
    assert key, "not found: " + t
    p = titles[key]; s = open(p).read()
    s2 = re.sub(r"(<body>\s*).*?(\s*</body>)", lambda m: m.group(1) + body.strip() + m.group(2), s, count=1, flags=re.S)
    assert s2 != s, "unchanged: " + t
    open(p, "w").write(s2); fixed.append(t)

# Pro Tools Cleanup asks for before.jpg / after.jpg; the repo renamed them Before.jpg / After.jpg (case sync), so the
# live page shows two broken pictures (checked 2026-10-07: lowercase 404, capitalized 200)
pc = titles[next(k for k in titles if k.startswith("Essentials: 3D) Pro Tools Cleanup"))]
s = open(pc).read(); s2 = s.replace("Pro_Tools_Cleanup/before.jpg", "Pro_Tools_Cleanup/Before.jpg").replace("Pro_Tools_Cleanup/after.jpg", "Pro_Tools_Cleanup/After.jpg")
assert s2 != s; open(pc, "w").write(s2); fixed.append("Pro Tools Cleanup: Before.jpg / After.jpg")

# Canvas writes quiz assessment_meta.xml with the schema location in xmlns:xsi (an invalid namespace URI), so strict XML
# readers (Canvas Preview's XMLDocument) can't read the quiz and show "Missing content". Write the header the way Canvas
# writes every other settings file (xmlns:xsi = XMLSchema-instance, xsi:schemaLocation = the pair).
BADXSI = 'xmlns:xsi="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd"'
GOODXSI = 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd"'
for d, _, fs in os.walk(W):
    for fn in fs:
        if fn == "assessment_meta.xml":
            p = os.path.join(d, fn); s0 = open(p).read()
            if BADXSI in s0: open(p, "w").write(s0.replace(BADXSI, GOODXSI)); fixed.append("quiz header: " + os.path.basename(d))

# GitHub picture links whose file was renamed only in capitals (the 2026-09 naming audit: "file name case synced").
# raw.githubusercontent.com is case-sensitive, so the old lowercase links 404 (Pro Tools Cleanup, Introduce Yourself).
REPO = "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/"
RAW = "https://raw.githubusercontent.com/uvu-dapr/Canvas/main/"
def case_fix(rel):
    # the Mac disk ignores capitals, so compare each name exactly against the folder listing
    parts, cur, out = rel.split("/"), REPO.rstrip("/"), []
    for p in parts:
        try: m = next((e for e in os.listdir(cur) if e.lower() == p.lower()), None)
        except FileNotFoundError: return None
        if m is None: return None
        out.append(m); cur = os.path.join(cur, m)
    good = "/".join(out)
    return good if good != rel else None
for d, _, fs in os.walk(W):
    for fn in fs:
        if not fn.endswith((".html", ".xml")): continue
        p = os.path.join(d, fn); s0 = open(p, encoding="utf-8").read(); s1 = s0
        for url in set(re.findall(re.escape(RAW) + r'[^"\'<>\s?#]+', s0)):
            rel = urllib.parse.unquote(url[len(RAW):]); good = case_fix(rel)
            if good: s1 = s1.replace(url, RAW + urllib.parse.quote(good)); fixed.append("case: " + good)
        if s1 != s0: open(p, "w", encoding="utf-8").write(s1)

# ---------- 2. new pages (same files and ids as v7)
NEW = {"Protocols: Delivery and File Naming Standards": "protocols-delivery-and-file-naming-standards",
       "Protocols: Delivery Recommendations for Recorded Music Projects": "protocols-delivery-recommendations-for-recorded-music-projects",
       "Reference: PreSonus FaderPort Quick Start for Pro Tools": "reference-presonus-faderport-quick-start-for-pro-tools"}
newitem = {}
for t, slug in NEW.items():
    rid = gid("page", t)
    open(os.path.join(W, "wiki_content", slug + ".html"), "w").write(
        '<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n<title>%s</title>\n<meta name="identifier" content="%s"/>\n<meta name="editing_roles" content="teachers"/>\n<meta name="workflow_state" content="unpublished"/>\n</head>\n<body>\n%s\n</body>\n</html>\n' % (html.escape(t, quote=False), rid, open(os.path.join(HERE, slug + ".body.html")).read().strip()))
    man = man.replace("</resources>", '  <resource identifier="%s" type="webcontent" href="wiki_content/%s.html">\n      <file href="wiki_content/%s.html"/>\n    </resource>\n  </resources>' % (rid, slug, slug), 1)
    newitem[t] = ('<item identifier="%s">\n        <content_type>WikiPage</content_type>\n        <workflow_state>unpublished</workflow_state>\n        <title>%s</title>\n        <identifierref>%s</identifierref>\n        <position>0</position>\n        <new_tab>false</new_tab>\n        <indent>0</indent>\n        <link_settings_json>null</link_settings_json>\n      </item>') % (gid("item", t), html.escape(t, quote=False), rid)

# ---------- 3. move and rename
MOVES = {"Essentials: 3C) How to Make a PDF": "Protocols: How to Make a PDF",
         "Essentials: 3D) Pro Tools Cleanup": "Protocols: Pro Tools Cleanup",
         "Essentials: 3G) Formatting a Drive That Works on Both Mac and Windows": "Protocols: Formatting a Drive That Works on Both Mac and Windows",
         "Essentials: 3F) Metric Standards": "Reference: Metric Standards",
         "Essentials: 3H) Apogee Boom": "Reference: Apogee BOOM Quick Start"}
RENAME = {"Essentials: 3E) Course Legend": "Essentials: 3C) Course Legend"}
se = modblock("Student Essentials"); its = items(se); keep = []; moved = {}
for it in its:
    t = title_of(it)
    if t in MOVES:
        nt = MOVES[t]; moved[nt] = setind(settitle(it, nt), 0)
        pf = os.path.join(W, page_file(ref_of(it))); s = open(pf).read()
        open(pf, "w").write(re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % html.escape(nt, quote=False), s, count=1))
    elif t in RENAME:
        nt = RENAME[t]; keep.append(settitle(it, nt))
        pf = os.path.join(W, page_file(ref_of(it))); s = open(pf).read()
        open(pf, "w").write(re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % html.escape(nt, quote=False), s, count=1))
    else: keep.append(it)
assert len(moved) == 5, sorted(moved)
se2 = se.split("<items>")[0] + "<items>\n      " + "\n      ".join(renum(keep)) + "\n    </items>\n  </module>"
mm = mm.replace(se, se2)
def module(title, its, pos):
    return '<module identifier="%s">\n    <title>%s</title>\n    <workflow_state>unpublished</workflow_state>\n    <position>%d</position>\n    <require_sequential_progress>false</require_sequential_progress>\n    <locked>false</locked>\n    <items>\n      %s\n    </items>\n  </module>' % (gid("module", title), html.escape(title, quote=False), pos, "\n      ".join(renum(its)))
prot = [moved["Protocols: How to Make a PDF"], moved["Protocols: Pro Tools Cleanup"], moved["Protocols: Formatting a Drive That Works on Both Mac and Windows"],
        newitem["Protocols: Delivery and File Naming Standards"], newitem["Protocols: Delivery Recommendations for Recorded Music Projects"]]
ref = [moved["Reference: Metric Standards"], moved["Reference: Apogee BOOM Quick Start"], newitem["Reference: PreSonus FaderPort Quick Start for Pro Tools"]]
# new modules go right after Student Essentials; renumber every module's position in document order
mm = mm.replace(se2, se2 + "\n  " + module("Protocols and Standards - (Unified Class Content)", prot, 0) + "\n  " + module("General Reference - (Unified Class Content)", ref, 0))
blocks = re.findall(r'<module identifier="[^"]+">.*?</module>', mm, re.S)
for k, b in enumerate(blocks, 1):
    mm = mm.replace(b, re.sub(r"(<title>[^<]*</title>\s*<workflow_state>[^<]*</workflow_state>\s*)<position>\d+</position>", r"\g<1><position>%d</position>" % k, b, count=1))
open(MM, "w").write(mm); open(MAN, "w").write(man)
print("fixed", len(fixed), "| new pages", len(NEW), "| moved", len(moved), "| renamed", len(RENAME))
print([title_of(b) for b in re.findall(r'<module identifier="[^"]+">.*?</module>', mm, re.S)])

zin = zipfile.ZipFile(SRC); names = set(zin.namelist()); changed = added = 0
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for n in sorted(names, key=lambda n: (n != "imsmanifest.xml", n)):
        data = zin.read(n); p = os.path.join(W, n)
        if not n.endswith("/") and os.path.exists(p):
            nd = open(p, "rb").read()
            if nd != data: data = nd; changed += 1
        z.writestr(n, data)
    for root, _, fs in os.walk(W):
        for f in fs:
            rel = os.path.relpath(os.path.join(root, f), W)
            if rel not in names and not f.startswith("."): z.write(os.path.join(root, f), rel); added += 1
print("files changed", changed, "| files added", added, "->", OUT)

# Standards 12s (Adam 2026-10-07): no file nothing uses. unused_files.py decides "used" the same way preflight does.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import unused_files
tmp = OUT + ".tmp"; os.replace(OUT, tmp)
dupes, d = unused_files.fix(tmp, OUT); os.remove(tmp)
print("left out", len(d), "unused files; repointed", len(dupes), "duplicate picture group(s) (Standards 12s)")
