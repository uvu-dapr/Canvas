#!/usr/bin/env python3
"""
deck_fonts.py: every font a deck names that LibreOffice cannot use on this Mac (J558, 2026-10-18).

LibreOffice builds each deck's tagged PDF (Standards 2a.1). When a deck names a font this Mac lacks, LibreOffice swaps
in another one and the PDF no longer matches the deck. This lists, for each -Linked and -Embedded deck, every font its
text, bullets and theme name that `fc-list` does not have, with the characters those text runs hold.

  used      a font named on a run, bullet, table cell or a slide theme's heading/body font. Missing = a real swap.
  notes     named only in speaker notes or the notes/handout theme: the slides' PDF never shows it (listed, not a fail).
  fallback  a theme's per-script fallback (<a:font script="Nkoo" typeface="Ebrima"/> in Office's own theme). PowerPoint
            and LibreOffice use it only for text in that script, so it is listed only when the deck holds such text.

    python3 deck_fonts.py [deck.pptx | folder ...]     default: every Presentations folder under Canvas Links
    python3 deck_fonts.py --all ...                     also list fallback-only fonts that no text uses
    python3 deck_fonts.py --pdf ...                     also each deck's PDF: LibreOffice stand-in fonts in it
    python3 deck_fonts.py --json ...                    machine readable

Exit 1 when any deck uses a missing font. Read only: never writes a deck. Skips Archive, _unused, PDF and Images.
"""
import sys, os, re, glob, json, zipfile, subprocess, unicodedata, collections

LINKS_ROOT = os.path.expanduser("~/Library/CloudStorage/Dropbox/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links")
SKIP_DIRS = ("Archive", "_unused", "PDF", "Images")
# theme script tags (ISO 15924) -> Unicode ranges; only scripts Office's theme sends to a font this Mac may lack
SCRIPT_RANGES = {
    "Nkoo": [(0x07C0, 0x07FF)], "Osma": [(0x10480, 0x104AF)], "Tfng": [(0x2D30, 0x2D7F)], "Ethi": [(0x1200, 0x139F)],
    "Hebr": [(0x0590, 0x05FF)], "Arab": [(0x0600, 0x06FF)], "Thai": [(0x0E00, 0x0E7F)], "Hang": [(0xAC00, 0xD7AF)],
    "Jpan": [(0x3040, 0x30FF)], "Hans": [(0x4E00, 0x9FFF)], "Hant": [(0x4E00, 0x9FFF)], "Deva": [(0x0900, 0x097F)],
    "Cher": [(0x13A0, 0x13FF)], "Yiii": [(0xA000, 0xA4CF)], "Tibt": [(0x0F00, 0x0FFF)], "Mong": [(0x1800, 0x18AF)],
}
FONT_ATTR = re.compile(r'<a:(latin|ea|cs|sym|buFont)\b[^>]*?\btypeface="([^"]*)"')
SCRIPT_FONT = re.compile(r'<a:font\s+script="(\w+)"\s+typeface="([^"]*)"')
RUN = re.compile(r'<a:(?:r|fld)>(.*?)</a:(?:r|fld)>', re.S)
TEXT = re.compile(r'<a:t>(.*?)</a:t>', re.S)

def installed_families():
    """the fonts LibreOffice sees when a11y_files.export_tagged builds a PDF: its font list (the Mac's font folders plus
    PowerPoint's own, where Aptos lives), read with fc-list"""
    env = dict(os.environ)
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from a11y_files import lo_fonts_conf
        env["FONTCONFIG_FILE"] = lo_fonts_conf()
    except Exception: pass
    out = subprocess.run(["fc-list", ":", "family"], capture_output=True, text=True, env=env).stdout
    fams = set()
    for line in out.splitlines():
        for f in line.split(","): fams.add(f.strip().lower())
    return fams

def has_font(name, fams):
    n = name.strip().lower()
    # PowerPoint names a style as part of the family at times ("Calibri Light", "Gill Sans MT Condensed")
    return n in fams or n.replace(" ", "") in {f.replace(" ", "") for f in fams}

def unescape(t): return t.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'").replace("&amp;", "&")

def scan(deck, fams, show_all=False):
    z = zipfile.ZipFile(deck)
    used = collections.defaultdict(collections.Counter)   # font -> character counts in its runs
    places = collections.defaultdict(set)
    fallback = collections.defaultdict(set)              # font -> scripts
    all_text = collections.Counter()
    names = z.namelist()
    # which masters use each theme: a theme only notes or handout masters use never reaches the slides' PDF
    theme_users = collections.defaultdict(set)
    for n in names:
        m = re.match(r"ppt/(slideMasters|notesMasters|handoutMasters)/_rels/.*\.rels$", n)
        if not m: continue
        for t in re.findall(r'Target="\.\./theme/(theme\d+\.xml)"', z.read(n).decode("utf8", "replace")): theme_users[t].add(m.group(1))
    notes_parts = {t for t, u in theme_users.items() if "slideMasters" not in u}
    for n in names:
        if not n.endswith(".xml") or not n.startswith("ppt/"): continue
        x = z.read(n).decode("utf8", "replace")
        if "typeface=" not in x and "<a:t>" not in x: continue
        for s, f in SCRIPT_FONT.findall(x):
            if f: fallback[f].add(s)
        # theme heading and body fonts: <a:majorFont><a:latin typeface=.../> outside runs
        for kind, f in FONT_ATTR.findall(x):
            if f and not f.startswith("+"): places[f].add(n.split("/")[-1])
        for r in RUN.findall(x):
            fonts = {f for k, f in FONT_ATTR.findall(r) if f and not f.startswith("+")}
            chars = "".join(unescape(t) for t in TEXT.findall(r))
            all_text.update(chars)
            for f in fonts: used[f].update(chars)
    report = []
    for f in sorted(places):
        if has_font(f, fams): continue
        slide_parts = {p for p in places[f] if p not in notes_parts and not p.startswith(("notesSlide", "notesMaster", "handoutMaster"))}
        report.append({"font": f, "kind": "used" if slide_parts else "notes", "parts": sorted(places[f]), "chars": dict(used.get(f, {}))})
    for f, scripts in sorted(fallback.items()):
        if f in places or has_font(f, fams): continue
        hit = {s for s in scripts for ch in all_text for lo, hi in SCRIPT_RANGES.get(s, []) if lo <= ord(ch) <= hi}
        if hit or show_all:
            report.append({"font": f, "kind": "fallback" + ("" if hit else " (no text in " + ", ".join(sorted(scripts)) + ")"),
                           "scripts": sorted(scripts), "used_by_text": bool(hit)})
    return report

def decks(args):
    roots = args or sorted(glob.glob(os.path.join(LINKS_ROOT, "*", "**", "Presentations"), recursive=True))
    for a in roots:
        if os.path.isfile(a): yield a; continue
        for dirpath, dirs, files in os.walk(a):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for f in sorted(files):
                if re.search(r"-(Linked|Embedded)\.pptx$", f) and not f.startswith("~$"): yield os.path.join(dirpath, f)

def describe(chars):
    """one line: how many characters, the plain ones as a set, anything outside ASCII by name (symbols matter most)"""
    if not chars: return []
    plain = "".join(sorted(ch for ch in chars if 32 < ord(ch) < 127))
    odd = ["%s U+%04X %s x%d" % (ch if ch.isprintable() else " ", ord(ch), unicodedata.name(ch, "?"), c)
           for ch, c in sorted(chars.items(), key=lambda kv: -kv[1]) if ord(ch) >= 127]
    out = ["%d characters; plain: %s" % (sum(chars.values()), plain or "none")]
    return out + ["other: " + o for o in odd]

# LibreOffice's own fonts. One of these in a deck's PDF where the deck names another font means LibreOffice could not
# see that font when it exported (2026-10-18: every LibreOffice PDF had Carlito for Calibri and Liberation Sans for
# Arial although both are installed). OpenSymbol is LibreOffice's bullet font and is fine.
LO_STANDINS = ("Carlito", "Caladea", "LiberationSans", "LiberationSerif", "LiberationMono", "LinuxLibertine", "LinuxBiolinum",
               "DejaVu", "FrankRuhlHofshi", "Gentium", "SourceSans", "SourceSerif", "SourceCode", "NotoSans", "NotoSerif", "Amiri", "Scheherazade")

def pdf_fonts(path):
    import zlib
    d = open(path, "rb").read(); blobs = [d]; fs = set()
    for m in re.finditer(rb"stream\r?\n", d):
        try: blobs.append(zlib.decompressobj().decompress(d[m.end():m.end() + 4000000]))
        except Exception: pass
    for b in blobs:
        fs |= {x.decode("latin-1").split("+")[-1] for x in re.findall(rb"/(?:BaseFont|FontName)\s*/([A-Za-z0-9+#\-_,]+)", b)}
    return fs

def pdf_check(deck):
    """the deck's PDF (Presentations/PDF/<Base>.pdf): LibreOffice stand-in fonts in it"""
    base = re.sub(r"-(Linked|Embedded)$", "", os.path.splitext(os.path.basename(deck))[0])
    pdf = os.path.join(os.path.dirname(deck), "PDF", base + ".pdf")
    if not os.path.exists(pdf): return None, []
    return pdf, sorted(f for f in pdf_fonts(pdf) if f.startswith(LO_STANDINS))

def main():
    argv = sys.argv[1:]
    show_all = "--all" in argv; as_json = "--json" in argv; with_pdf = "--pdf" in argv
    args = [a for a in argv if not a.startswith("--")]
    fams = installed_families()
    results, seen, bad, pdfs = {}, set(), 0, {}
    for d in decks(args):
        if d in seen: continue
        seen.add(d)
        try: r = scan(d, fams, show_all)
        except Exception as e: r = [{"font": "?", "kind": "error", "error": str(e)}]
        if r: results[d] = r
        if any(x["kind"] == "used" or x.get("used_by_text") for x in r): bad += 1
        if with_pdf and d.endswith("-Linked.pptx"):
            pdf, standins = pdf_check(d)
            if standins: pdfs[pdf] = standins
    if as_json:
        print(json.dumps({"decks": len(seen), "missing": results, "pdf_standins": pdfs}, indent=1)); return 1 if bad else 0
    for d, r in results.items():
        print(os.path.relpath(d, LINKS_ROOT) if d.startswith(LINKS_ROOT) else d)
        for x in r:
            print("  %-8s %s%s" % (x["kind"], x["font"], ("  in " + ", ".join(x["parts"][:6])) if x.get("parts") else ""))
            for line in describe(x.get("chars", {}))[:20]: print("           " + line)
    print("RESULT %s: %d decks, %d use a font this Mac lacks" % ("PASS" if not bad else "FAIL", len(seen), bad))
    if with_pdf:
        for p, f in sorted(pdfs.items()): print("PDF stand-in  %s: %s" % (os.path.relpath(p, LINKS_ROOT) if p.startswith(LINKS_ROOT) else p, ", ".join(f)))
        print("PDF %s: %d deck PDFs carry LibreOffice stand-in fonts (LibreOffice did not see the deck's fonts)" % ("PASS" if not pdfs else "WARN", len(pdfs)))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
