"""J130 (Adam, 2026-10-06: "put a different background or template on them so they have different themes ... something a
little less bland"; chose "Rotate tints by module"). Hand-built -Linked decks set their own white background on each slide,
so a PowerPoint theme cannot show through: this gives those white slide backgrounds one soft tint per module (dark slides,
words, pictures and layout untouched), keeps the original in the module's Presentations/Archive, then rebuilds the Embedded
deck with deck_pair.py embed. PDFs follow with Slides > Update.
    tint_plain_decks_j130.py plan.json [--dry] [index ...]"""
import sys, os, re, json, zipfile, shutil, subprocess, html, datetime
TINTS = [("Sand", "F3EEE4"), ("Sage", "EBF1EA"), ("Sky", "E8F0F8"), ("Lavender", "EFECF5"), ("Blush", "F6ECEC"), ("Mist", "E9F1F2"), ("Butter", "F6F2E2"), ("Stone", "EEEDEA")]
BT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "deck_pair.py")
a = sys.argv[1:]; dry = "--dry" in a; a = [x for x in a if x != "--dry"]
plan = json.load(open(a[0])); idx = [int(x) for x in a[1:]] or range(len(plan))
mods = []
for e in plan:
    if e["module"] not in mods: mods.append(e["module"])
def slides(z): return sorted(n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n))
def facts(p):
    z = zipfile.ZipFile(p); s = slides(z)
    text = sorted(" ".join(t for t in (html.unescape(x).strip() for x in re.findall(r"<a:t>([^<]*)</a:t>", z.read(n).decode("utf8", "ignore"))) if t) for n in s)
    ext = sum(len(re.findall(r'TargetMode="External"', z.read(n).decode("utf8", "ignore"))) for n in z.namelist() if n.startswith("ppt/slides/_rels/"))
    return len(s), text, ext, sum(z.read(n).decode("utf8", "ignore").count("<p:pic>") for n in s)
WHITE = re.compile(r'(<p:bg><p:bgPr><a:solidFill>)(?:<a:srgbClr val="(?:FFFFFF|ffffff)"/>|<a:schemeClr val="bg1"/>)')
stamp = datetime.date.today().isoformat()
for i in idx:
    e = plan[i]; deck = e["deck"]; d, base = os.path.split(deck)
    name, tint = TINTS[mods.index(e["module"]) % len(TINTS)]
    if os.path.exists(os.path.join(d, "~$" + base)): print(i, "SKIP open in PowerPoint", base); continue
    z = zipfile.ZipFile(deck); s = slides(z)
    own = sum(1 for n in s if "<p:bg>" in z.read(n).decode("utf8", "ignore"))
    if own <= len(s) / 2: print(i, "THEME (follows its master)", base); continue
    white = sum(1 for n in s if WHITE.search(z.read(n).decode("utf8", "ignore")))
    if dry: print(i, name, tint, base, "white slides", white, "of", len(s)); continue
    tmp = deck + ".tinting"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
        for it in z.infolist():
            data = z.read(it.filename)
            if it.filename in s: data = WHITE.sub(lambda m: m.group(1) + '<a:srgbClr val="%s"/>' % tint, data.decode("utf8")).encode("utf8")
            zo.writestr(it, data)
    if facts(deck) != facts(tmp): os.remove(tmp); print(i, "FAILED CHECK, unchanged", base); continue
    arch = os.path.join(d, "Archive"); os.makedirs(arch, exist_ok=True)
    shutil.copy2(deck, os.path.join(arch, base.replace("-Linked.pptx", "-Linked-%s-before-tint.pptx" % stamp)))
    os.replace(tmp, deck)
    r = subprocess.run(["python3", BT, "embed", deck], capture_output=True, text=True)
    print(i, name, base, "tinted", white, "of", len(s), "| embed", "ok" if r.returncode == 0 else "FAILED " + (r.stderr or r.stdout)[-200:], flush=True)
