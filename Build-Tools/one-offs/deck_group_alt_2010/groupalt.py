"""Alt text on untitled shape groups (and SmartArt frames) of -Linked decks, then the Build-Tools route:
deck_pair.embed, a11y_files.export_tagged (lo_fonts_conf real fonts), fix_meta like today's PDF, checks, in place."""
import sys, os, re, json, shutil, html, time, datetime
BT = "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Build-Tools"; sys.path.insert(0, BT)
import a11y_files as A, deck_pair as dp, deck_fonts as df
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from groupexport import export_with_group_alt
C = "/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links/DAPR-2010--Core_Recording"
BK = "/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses/DAPR 2010 - Core Recording/Instructor Stuff/Deck Backups/2026-10-18 before group alt text"
SCR = sys.argv[1]; MODE = sys.argv[2]; ONLY = sys.argv[3:]   # MODE: scratch | inplace
spec = json.load(open(os.path.join(os.path.dirname(__file__), "alts.json")))

def apply(data, slides):
    n = 0
    for sx, ids in slides.items():
        x = data[sx].decode("utf-8")
        for i, alt in ids.items():
            pat = re.compile(r'(<p:nv(?:GrpSp|GraphicFrame)Pr>\s*<p:cNvPr\b)([^>]*?\bid="%s"[^>]*?)(/?>)' % i)
            m = pat.search(x)
            if not m: raise SystemExit("no group/frame id %s in %s" % (i, sx))
            attrs = m.group(2)
            if re.search(r'\bdescr="', attrs): raise SystemExit("id %s in %s already has descr" % (i, sx))
            x = x[:m.start()] + m.group(1) + attrs + ' descr="%s"' % html.escape(alt, quote=True) + m.group(3) + x[m.end():]
            n += 1
        data[sx] = x.encode("utf-8")
    return n

rows = []
for rel, slides in spec.items():
    L = os.path.join(C, rel); base = dp.base_of(L)
    if ONLY and base not in ONLY: continue
    pres = os.path.dirname(L); E = os.path.join(pres, base + "-Embedded.pptx"); pdf = os.path.join(pres, "PDF", base + ".pdf")
    row = dict(base=base)
    w = os.path.join(SCR, base); os.makedirs(w, exist_ok=True)
    if dp.is_open(L) or dp.is_open(E): row["stop"] = "open in PowerPoint"; rows.append(row); print(row); continue
    if time.time() - max(os.path.getmtime(L), os.path.getmtime(E), os.path.getmtime(pdf)) < 900: row["stop"] = "changed in the last 15 minutes"; rows.append(row); print(row); continue
    lm = os.path.getmtime(L)
    infos, data = dp.read(L); before_xml = {k: v for k, v in data.items()}
    row["alts"] = apply(data, slides)
    # only the named slide parts changed
    changed = [k for k in data if data[k] != before_xml[k]]
    assert set(changed) <= set(slides), changed
    nl = os.path.join(w, base + "-Linked.pptx"); dp.write(nl, infos, data)
    # dp.write runs fix_ns on every slide: make sure no OTHER slide changed byte for byte
    _, back = dp.read(nl); _, orig = dp.read(L)
    other = [k for k in orig if k not in slides and orig[k] != back.get(k)]
    row["other_parts_changed"] = other
    ne = os.path.join(w, base + "-Embedded.pptx"); e = dp.embed(nl, ne)
    if e.get("error"): row["stop"] = "embed %s" % e; rows.append(row); print(row); continue
    A.wait_load(60)
    made, gr = export_with_group_alt(ne, w); row["lo_groups"] = gr
    if not made: row["stop"] = "no PDF"; rows.append(row); print(row); continue
    A.fix_meta(made, like=pdf)
    o, n = A.pdf_facts(pdf), A.pdf_facts(made)
    worst, bad, pages_differ = A.look_diff(pdf, made)
    st = sorted(f for f in df.pdf_fonts(made) if f.startswith(A.LO_STANDIN_PREFIXES))
    row.update(pages=(o["pages"], n["pages"]), figures=(o["figures"], n["figures"]), with_alt=(o["figures_with_alt"], n["figures_with_alt"]),
               headings=(o["headings"], n["headings"]), bookmarks=(o["bookmarks"], n["bookmarks"]), title=n["title"], lang=n["lang"], tagged=n["tagged"],
               look_worst=worst, look_bad=bad, standins=st, issues=n["issues"])
    probs = []
    if o["pages"] != n["pages"] or pages_differ: probs.append("pages")
    if n["figures"] != n["figures_with_alt"]: probs.append("figures without alt %d" % (n["figures"] - n["figures_with_alt"]))
    if not n["tagged"] or n["lang"] != "en-US" or n["title"] != o["title"]: probs.append("tags/lang/title")
    for k in ("headings", "tables", "table_headers", "bookmarks"):
        if o.get(k) != n.get(k): probs.append(k)
    if bad: probs.append("look")
    if st: probs.append("stand-in fonts")
    if os.path.getmtime(L) != lm: probs.append("Linked changed while running")
    row["problems"] = probs
    if probs or MODE != "inplace": rows.append(row); print(json.dumps(row)); continue
    # in place: back up Linked, Embedded and PDF outside GitHub and Cloudflare, then put the new files in
    os.makedirs(BK, exist_ok=True)
    for f in (L, E, pdf): shutil.copy2(f, os.path.join(BK, os.path.basename(f)))
    shutil.copyfile(nl, L)
    e = dp.embed(L)
    if e.get("error"): row["error"] = "embed in place %s" % e; rows.append(row); print(row); continue
    fin = os.path.join(w, "final"); os.makedirs(fin, exist_ok=True)
    A.wait_load(60); made2, gr2 = export_with_group_alt(E, fin)
    if not made2: row["error"] = "final export %s" % gr2; rows.append(row); print(row); continue
    A.fix_meta(made2, like=pdf)
    f2 = A.pdf_facts(made2); w2, bad2, pd2 = A.look_diff(made, made2)
    if f2["pages"] != n["pages"] or f2["figures"] != f2["figures_with_alt"] or bad2 or pd2 or not f2["tagged"]:
        row["error"] = "final export differs from scratch: %s" % ((f2["pages"], f2["figures"], f2["figures_with_alt"], bad2),); rows.append(row); print(row); continue
    shutil.copyfile(made2, pdf)
    row["verify"] = dp.verify(L).get("problems") or "OK"; row["done"] = True
    rows.append(row); print(json.dumps(row))
json.dump(rows, open(os.path.join(SCR, "groupalt-%s.json" % MODE), "w"), indent=1, default=str)
