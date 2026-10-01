#!/usr/bin/env python3
"""
deck_pair.py: every teaching deck as a Linked deck Adam edits and an Embedded deck built from it (Adam, 2026-09-30).

  <Base>-Linked.pptx    the one Adam edits. Each teaching picture is a relative link to Images/<Base>-<Subject>.<ext>
                        (nothing embedded for it); the last slides document where the pictures live.
  <Base>-Embedded.pptx  built from the Linked deck: every picture inside the file, no reference slides. Never edited by
                        hand. Students get its PDF: PDF/<Base>.pdf.
  Presentations/Images  shared by every deck in the module; each file starts with its deck's base name.

The two decks are the same file apart from how pictures are stored and the reference slides: slides, order, text,
notes, animations, transitions, crops, alt text and layout are copied, never rebuilt. Icons, checkmarks, warning marks
and pictures in masters and layouts are design, not teaching pictures: they stay inside both decks (Adam, 2026-09-30),
and the reference slide counts them. A picture's subject comes from its alt text, else its slide title; names are never
numbered, and a picture Adam replaces keeps its exact name, so the Linked deck shows it and the Embedded deck is out of
date until it is built again.

    python3 deck_pair.py split  <deck.pptx | folder> [--dry]    make the pair from a single deck (the deck goes to Archive)
    python3 deck_pair.py embed  <Base-Linked.pptx | folder>     build the Embedded deck again from the Linked deck
    python3 deck_pair.py status <folder>                         which Embedded decks are out of date, and why
    python3 deck_pair.py verify <Base-Linked.pptx | folder>      check a pair against the rules
    python3 deck_pair.py uncopy <Base-Linked.pptx | folder>      take out picture copies put inside a Linked deck

Links only (Adam, 2026-09-30): a copy of each picture inside the Linked deck made PowerPoint show pictures, but the deck
became Embedded-size and a replaced picture never showed until the copy was refreshed, so copies are not used. On the
Mac, PowerPoint's sandbox cannot follow these links (its Grant File Access panel grants one file at a time); the
pictures show in the Embedded deck and the PDF.

Never touches a deck open in PowerPoint, or anything in Archive, _unused, PDF or Images.
"""
import sys, os, re, io, zipfile, hashlib, html, json, datetime, subprocess, urllib.parse, posixpath, shutil, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_names import deck_base, subject_candidates, is_design
from merge_decks import american, shapes, geom

REL_IMG = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"
REL_SLIDE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide"
REF_MARK = "Canvas Preview: linked picture reference"
# alt text and subjects written for pictures that had none (viewed one by one, 2026-09-30), keyed by SHA-1
try: PICTURE_TEXT = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "deck_picture_text.json")))["pictures"]
except Exception: PICTURE_TEXT = {}
SKIP_DIRS = ("Archive", "_unused", "PDF", "Images")
MIME = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "gif": "image/gif", "svg": "image/svg+xml", "tif": "image/tiff",
        "tiff": "image/tiff", "bmp": "image/bmp", "webp": "image/webp", "emf": "image/x-emf", "wmf": "image/x-wmf"}

def sha(b): return hashlib.sha1(b).hexdigest()
def base_of(path): return re.sub(r"-(Linked|Embedded)$", "", os.path.splitext(os.path.basename(path))[0])
def rels_name(part): return posixpath.join(posixpath.dirname(part), "_rels", posixpath.basename(part) + ".rels")

OPEN = None
def is_open(deck):
    global OPEN
    if OPEN is None:
        try:
            r = subprocess.run(["osascript", "-e", 'if application "Microsoft PowerPoint" is running then tell application "Microsoft PowerPoint" to get name of every presentation'],
                               capture_output=True, text=True, timeout=20)
            OPEN = {x.strip() for x in r.stdout.split(",") if x.strip()}
        except Exception: OPEN = set()
    return os.path.exists(os.path.join(os.path.dirname(deck), "~$" + os.path.basename(deck))) or os.path.basename(deck) in OPEN

def read(deck):
    z = zipfile.ZipFile(deck); infos = [i for i in z.infolist() if not i.filename.endswith("/")]
    data = {i.filename: z.read(i.filename) for i in infos}; z.close(); return infos, data

def write(path, infos, data):
    buf = io.BytesIO(); done = set()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as o:
        o.writestr("[Content_Types].xml", data["[Content_Types].xml"]); done.add("[Content_Types].xml")
        for i in infos:
            if i.filename in data and i.filename not in done: o.writestr(i.filename, data[i.filename]); done.add(i.filename)
        for n in data:
            if n not in done: o.writestr(n, data[n])
    tmp = path + ".building"; open(tmp, "wb").write(buf.getvalue()); os.replace(tmp, path)

def slide_order(data):
    pres = data["ppt/presentation.xml"].decode("utf-8"); rels = data["ppt/_rels/presentation.xml.rels"].decode("utf-8")
    tgt = {}
    for r in re.findall(r"<Relationship [^>]*/>", rels):
        if 'relationships/slide"' in r:
            tgt[re.search(r'Id="([^"]+)"', r).group(1)] = posixpath.normpath(posixpath.join("ppt", re.search(r'Target="([^"]+)"', r).group(1)))
    return [(rid, tgt[rid]) for rid in re.findall(r'<p:sldId [^>]*r:id="([^"]+)"', pres) if rid in tgt]

def title_of(xml):
    for m in shapes(xml):
        sp = m.group(0)
        if re.search(r'<p:ph [^>]*type="(title|ctrTitle)"', sp): return " ".join(html.unescape(x) for x in re.findall(r"<a:t>([^<]*)</a:t>", sp)).strip()
    best = None                                   # generated decks: the large text near the top
    for m in shapes(xml):
        g = geom(m.group(0)); sz = re.search(r'sz="(\d+)"', m.group(0)); t = " ".join(re.findall(r"<a:t>([^<]*)</a:t>", m.group(0))).strip()
        if g and sz and t and g[1] < 1300000 and int(sz.group(1)) >= 2400 and (best is None or int(sz.group(1)) > best[0]): best = (int(sz.group(1)), html.unescape(t))
    return best[1] if best else ""

def real_kind(blob):
    """What a picture file really is, whatever its name says"""
    head = blob[:300]
    if head.startswith(b"\x89PNG"): return ".png"
    if head[:3] == b"\xff\xd8\xff": return ".jpg"
    if head[:4] == b"GIF8": return ".gif"
    if b"<svg" in head or head.lstrip().startswith(b"<?xml"): return ".svg"
    return None

def svg_to_png(blob):
    """An SVG rendered to PNG at three times its size (svg2png.swift beside this file, built once into the cache).
    Some generated decks store an SVG where the PNG copy should be (2000 Polar Patterns, 2026-09-30)."""
    tool = os.path.expanduser("~/Library/Caches/CanvasPreview/svg2png")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg2png.swift")
    if not os.path.exists(tool) or os.path.getmtime(tool) < os.path.getmtime(src):
        os.makedirs(os.path.dirname(tool), exist_ok=True)
        subprocess.run(["swiftc", "-O", src, "-o", tool], capture_output=True)
    d = tempfile.mkdtemp(); i = os.path.join(d, "in.svg"); o = os.path.join(d, "out.png")
    t = blob.decode("utf-8", "ignore").replace(" \u2014 ", ": ").replace("\u2014", ": ").replace("\u2013", "-")
    open(i, "w", encoding="utf-8").write(t)
    subprocess.run([tool, i, o, "3"], capture_output=True)
    out = open(o, "rb").read() if os.path.exists(o) else None
    shutil.rmtree(d, ignore_errors=True); return out

def to_png(blob, ext):
    """TIFF, GIF, BMP and WebP pictures become PNG (Standards: PNG or JPG only)"""
    d = tempfile.mkdtemp(); src = os.path.join(d, "in" + ext); dst = os.path.join(d, "out.png")
    open(src, "wb").write(blob)
    r = subprocess.run(["sips", "-s", "format", "png", src, "--out", dst], capture_output=True)
    out = open(dst, "rb").read() if r.returncode == 0 and os.path.exists(dst) else None
    shutil.rmtree(d, ignore_errors=True); return out

def course_and_module(deck):
    pres = os.path.dirname(os.path.abspath(deck)); module = os.path.basename(os.path.dirname(pres)); course = os.path.basename(os.path.dirname(os.path.dirname(pres)))
    return course, module

# ---------------------------------------------------------------- split

def split(deck, dry=False):
    pres_dir = os.path.dirname(os.path.abspath(deck)); stem = os.path.splitext(os.path.basename(deck))[0]
    if re.search(r"-(Linked|Embedded)$", stem): return dict(deck=deck, skipped="already a Linked or Embedded deck")
    if is_open(deck): return dict(deck=deck, skipped="open in PowerPoint; close it and run again")
    base = deck_base(stem); images = os.path.join(pres_dir, "Images")
    linked_path = os.path.join(pres_dir, base + "-Linked.pptx"); emb_path = os.path.join(pres_dir, base + "-Embedded.pptx")
    if os.path.exists(linked_path) or os.path.exists(emb_path): return dict(deck=deck, skipped="%s-Linked or -Embedded already exists" % base)
    infos, data = read(deck)
    # the rules for every word on every slide and note: American spelling, no em or en dashes
    for n in list(data):
        if re.match(r"ppt/(slides|notesSlides)/\w+\.xml$", n): data[n] = american(data[n].decode("utf-8")).encode("utf-8")
    # the file's own title loses any module number ("M17 Power")
    if "docProps/core.xml" in data:
        data["docProps/core.xml"] = re.sub(r"(<dc:title>)\s*M\d{1,2}[:\-\s]+", r"\1", data["docProps/core.xml"].decode("utf-8")).encode("utf-8")
    used = {}; taken = {}; listing = []; design = 0; not_linked = []; files_written = []; kept_existing = []
    order = slide_order(data)
    for pos, (rid, sx) in enumerate(order, 1):
        if sx not in data: continue
        body = data[sx].decode("utf-8"); rn = rels_name(sx); rels = data.get(rn, b"").decode("utf-8"); title = title_of(body)
        body = re.sub(r'(<a:blip r:embed="[^"]+") r:link="[^"]+"', r"\1", body)       # an earlier embed-plus-link picture: the new link replaces it
        target = {}
        for r in re.findall(r"<Relationship [^>]*/>", rels):
            if 'relationships/image"' in r and 'TargetMode="External"' not in r:
                target[re.search(r'Id="([^"]+)"', r).group(1)] = re.search(r'Target="([^"]+)"', r).group(1)
        new_rels = []; k = [0]
        def one(el):
            nonlocal design
            m = re.search(r'<a:blip r:embed="([^"]+)"', el)
            if not m or m.group(1) not in target: return el
            d = re.search(r'<p:cNvPr [^>]*descr="([^"]*)"', el); alt = d.group(1) if d else ""
            media = posixpath.normpath(posixpath.join(posixpath.dirname(sx), target[m.group(1)]))
            if media not in data: return el
            blob = data[media]; ext = os.path.splitext(media)[1].lower()
            kind = real_kind(blob)
            if kind == ".svg":
                png = svg_to_png(blob)
                if png is None: not_linked.append("slide %d: %s (an SVG that could not be drawn as PNG)" % (pos, os.path.basename(media))); return el
                blob, ext = png, ".png"
            elif kind and kind != ext and not (kind == ".jpg" and ext == ".jpeg"): ext = kind       # a JPG named .png keeps what it is
            known = PICTURE_TEXT.get(sha(blob))
            if known:
                # the picture had no alt text: the written one goes into the deck (both versions), and names the file
                alt = known["alt"]; subj = known["subject"]
                el = set_alt(el, alt)
                if known.get("decorative"): design += 1; return el
            else: subj = None
            if is_design(alt, 'decorative val="1"' in el): design += 1; return el
            if ext in (".emf", ".wmf", ".wdp"): not_linked.append("slide %d: %s (%s cannot be a linked picture)" % (pos, os.path.basename(media), ext)); return el
            if ext in (".tif", ".tiff", ".gif", ".bmp", ".webp"):
                png = to_png(blob, ext)
                if png is None: not_linked.append("slide %d: %s (could not convert to PNG)" % (pos, os.path.basename(media))); return el
                blob, ext = png, ".png"
            if ext == ".jpeg": ext = ".jpg"
            h = sha(blob)
            if h in used: name = used[h]
            else:
                for cand in ([subj] if subj else []) + subject_candidates(alt, title, geom(el)):
                    name = "%s-%s%s" % (base, cand, ext)
                    if name not in taken: break
                else:
                    not_linked.append("slide %d: no unique name for %s" % (pos, cand)); return el
                used[h] = name; taken[name] = h
                if not dry:
                    os.makedirs(images, exist_ok=True); p = os.path.join(images, name)
                    if os.path.exists(p):
                        if sha(open(p, "rb").read()) != h: kept_existing.append(name)     # a picture Adam already replaced is his
                    else: open(p, "wb").write(blob); files_written.append(name)
            listing.append((pos, name))
            k[0] += 1; lid = "rIdLk%d" % k[0]
            while lid in rels: lid += "x"
            new_rels.append('<Relationship Id="%s" Type="%s" Target="Images/%s" TargetMode="External"/>' % (lid, REL_IMG, urllib.parse.quote(name)))
            el = re.sub(r'<a:blip r:embed="[^"]+"', '<a:blip r:link="%s"' % lid, el, count=1)
            # an SVG layered over the picture would stay embedded: the linked PNG or JPG is the picture
            return re.sub(r'(?s)<a:ext uri="\{96DAC541-7B7A-43D3-8B79-37D633B846F1\}">.*?</a:ext>', "", el)
        body2 = re.sub(r"(?s)<p:pic>.*?</p:pic>|<p:sp>(?:(?!</p:sp>).)*?<a:blipFill.*?</p:sp>", lambda m: one(m.group(0)), body)
        body2 = re.sub(r"<a:extLst>\s*</a:extLst>", "", body2)
        if new_rels:
            data[sx] = body2.encode("utf-8")
            data[rn] = rels.replace("</Relationships>", "".join(new_rels) + "</Relationships>").encode("utf-8")
    drop_unused_media(data)
    course, module = course_and_module(deck)
    add_reference_slides(data, course, module, base, listing, design, not_linked)
    result = dict(deck=deck, base=base, linked=linked_path, embedded=emb_path, pictures_linked=len(listing), files=len(used),
                  design_marks_inside=design, not_linked=not_linked, kept_existing=kept_existing)
    if dry: result["dry"] = True; result["names"] = sorted(set(n for _, n in listing)); return result
    arch = os.path.join(pres_dir, "Archive"); os.makedirs(arch, exist_ok=True)
    keep = os.path.join(arch, "%s (before Linked and Embedded %s).pptx" % (stem, datetime.date.today().isoformat()))
    if not os.path.exists(keep): shutil.move(deck, keep)
    write(linked_path, infos, data)
    result["archived"] = keep
    result["embed"] = embed(linked_path)
    return result

def prune_picture_rels(data):
    """A slide's picture relationships that nothing on the slide uses any more (the embedded copy a link replaced, an
    earlier absolute link) leave the file, so the Linked deck carries no stray pictures or paths."""
    for n in list(data):
        m = re.match(r"ppt/slides/_rels/(slide\d+\.xml)\.rels$", n)
        if not m or ("ppt/slides/" + m.group(1)) not in data: continue
        body = data["ppt/slides/" + m.group(1)].decode("utf-8"); rels = data[n].decode("utf-8")
        for r in re.findall(r"<Relationship [^>]*/>", rels):
            if 'relationships/image"' not in r: continue
            rid = re.search(r'Id="([^"]+)"', r).group(1)
            if not re.search(r'r:(embed|link|id|pict)="%s"' % re.escape(rid), body): rels = rels.replace(r, "")
        data[n] = rels.encode("utf-8")

def set_alt(el, alt):
    """Puts alt text on a picture's cNvPr (replacing an empty or file name one)"""
    a = html.escape(alt, quote=True)
    if re.search(r'<p:cNvPr [^>]*descr="', el): return re.sub(r'(<p:cNvPr [^>]*descr=")[^"]*"', r'\g<1>%s"' % a.replace("\\", "\\\\"), el, count=1)
    return re.sub(r"<p:cNvPr ", '<p:cNvPr descr="%s" ' % a, el, count=1)

def drop_unused_media(data):
    prune_picture_rels(data)
    refs = set()
    for n, b in data.items():
        if n.endswith(".rels"):
            d2 = posixpath.dirname(posixpath.dirname(n))
            for r in re.findall(r"<Relationship [^>]*/>", b.decode("utf-8", "ignore")):
                if 'TargetMode="External"' in r: continue
                refs.add(posixpath.normpath(posixpath.join(d2, re.search(r'Target="([^"]+)"', r).group(1))))
    for n in [x for x in data if x.startswith("ppt/media/") and x not in refs]: data.pop(n)

def add_reference_slides(data, course, module, base, listing, design, not_linked):
    order = slide_order(data)
    last = order[-1][1]
    layout = re.search(r'Target="(\.\./slideLayouts/[^"]+)"', data.get(rels_name(last), b"").decode("utf-8"))
    readable = lambda s: s.replace("--", " - ").replace("__", ": ").replace("_", " ")
    head = [("Linked Picture Reference", 2800, True),
            ("Course: %s" % readable(course), 1400, False), ("Module: %s" % readable(module), 1400, False),
            ("Presentation: %s-Linked.pptx (edit this one)" % base, 1400, False),
            ("Built from it: %s-Embedded.pptx (all pictures inside) and PDF/%s.pdf (what students get)" % (base, base), 1400, False),
            ("PowerPoint base name: %s" % base, 1400, False),
            ("Image reference folder: Images/ beside this deck, linked by relative path (Images/<file name>)", 1400, False),
            ("Full path: Canvas Links/%s/%s/Presentations/Images/" % (course, module), 1400, False),
            ("Image file name prefix: %s-" % base, 1400, False),
            ("Replace a picture by saving over its file under the same name. Canvas Preview then shows %s-Embedded.pptx as out of date: Update rebuilds it and its PDF." % base, 1400, False),
            ("Pictures linked: %d, in %d file(s). Design marks kept inside the deck (icons, checkmarks, warning marks, master and layout pictures): %d." % (len(listing), len(set(n for _, n in listing)), design), 1400, False)]
    if not_linked: head.append(("Not linked (kept inside): " + "; ".join(not_linked), 1200, False))
    else: head.append(("Unusual dependencies: none. Every teaching picture is a linked file in Images/.", 1400, False))
    pages = [head]
    lines = ["Slide %d: %s" % (p, n) for p, n in listing]
    for i in range(0, len(lines), 22):
        pages.append([("Linked Pictures (%s)" % ("slides %d to %d" % (listing[i][0], listing[min(i + 21, len(lines) - 1)][0])), 2400, True)] + [(l, 1100, False) for l in lines[i:i + 22]])
    for page in pages:
        nums = [int(m) for m in re.findall(r"ppt/slides/slide(\d+)\.xml$", "\n".join(data), re.M)]
        num = max(nums) + 1; sx = "ppt/slides/slide%d.xml" % num
        paras = "".join('<a:p><a:r><a:rPr lang="en-US" sz="%d"%s dirty="0"><a:solidFill><a:srgbClr val="1F2A25"/></a:solidFill></a:rPr><a:t>%s</a:t></a:r></a:p>' % (sz, ' b="1"' if b else "", html.escape(t, quote=False)) for t, sz, b in page)
        xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
               'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
               '<p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:effectLst/></p:bgPr></p:bg><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr/>'
               '<p:sp><p:nvSpPr><p:cNvPr id="2" name="%s" descr="%s"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="457200" y="365760"/><a:ext cx="11277600" cy="6126480"/></a:xfrm>'
               '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr><p:txBody><a:bodyPr wrap="square"><a:normAutofit/></a:bodyPr><a:lstStyle/>%s</p:txBody></p:sp></p:spTree></p:cSld>'
               '<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>') % (REF_MARK, REF_MARK, paras)
        data[sx] = xml.encode("utf-8")
        if layout:
            data[rels_name(sx)] = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="%s"/></Relationships>' % layout.group(1)).encode("utf-8")
        prels = data["ppt/_rels/presentation.xml.rels"].decode("utf-8"); rid = "rIdRef%d" % num
        data["ppt/_rels/presentation.xml.rels"] = prels.replace("</Relationships>", '<Relationship Id="%s" Type="%s" Target="slides/slide%d.xml"/></Relationships>' % (rid, REL_SLIDE, num)).encode("utf-8")
        pres = data["ppt/presentation.xml"].decode("utf-8"); ids = [int(x) for x in re.findall(r'<p:sldId\b[^>]*?\bid="(\d+)"', pres)]
        data["ppt/presentation.xml"] = pres.replace("</p:sldIdLst>", '<p:sldId id="%d" r:id="%s"/></p:sldIdLst>' % (max(ids) + 1, rid)).encode("utf-8")
        ct = data["[Content_Types].xml"].decode("utf-8")
        data["[Content_Types].xml"] = ct.replace("</Types>", '<Override PartName="/ppt/slides/slide%d.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/></Types>' % num).encode("utf-8")

# ---------------------------------------------------------------- uncopy

def uncopy(linked):
    """Takes out the copies a Linked deck carried next to its links (2026-09-30), keeping the file's date."""
    if is_open(linked): return dict(linked=linked, skipped="open in PowerPoint; close it and run again")
    infos, data = read(linked); k = 0
    for n in list(data):
        m = re.match(r"ppt/slides/(slide\d+\.xml)$", n)
        if not m: continue
        body = data[n].decode("utf-8")
        body2, c = re.subn(r'<a:blip r:embed="[^"]+" (r:link=")', r"<a:blip \1", body)
        if c: data[n] = body2.encode("utf-8"); k += c
    if not k: return dict(linked=linked, copies_removed=0)
    drop_unused_media(data)                         # the copies' relationships and files leave with them
    st = os.stat(linked); write(linked, infos, data); os.utime(linked, (st.st_atime, st.st_mtime))
    return dict(linked=linked, copies_removed=k)

# ---------------------------------------------------------------- embed

def link_target_path(deck, target):
    if target.startswith("file://"): return urllib.parse.unquote(urllib.parse.urlparse(target).path)
    return os.path.join(os.path.dirname(os.path.abspath(deck)), urllib.parse.unquote(target))

def embed(linked, out=None):
    """<Base>-Embedded.pptx from <Base>-Linked.pptx: each linked picture put inside, the reference slides left out."""
    out = out or re.sub(r"-Linked\.pptx$", "-Embedded.pptx", linked)
    if out == linked: return dict(error="not a -Linked deck")
    infos, data = read(linked); missing = []; k = 0; exts = set()
    for rid, sx in slide_order(data):
        if REF_MARK not in data.get(sx, b"").decode("utf-8", "ignore"): continue
        num = re.search(r"slide(\d+)\.xml$", sx).group(1)
        prels = data["ppt/_rels/presentation.xml.rels"].decode("utf-8")
        data["ppt/_rels/presentation.xml.rels"] = re.sub(r'<Relationship Id="%s" [^>]*/>' % re.escape(rid), "", prels).encode("utf-8")
        data["ppt/presentation.xml"] = re.sub(r'<p:sldId id="\d+" r:id="%s"/>' % re.escape(rid), "", data["ppt/presentation.xml"].decode("utf-8")).encode("utf-8")
        data.pop(sx, None); data.pop(rels_name(sx), None)
        data["[Content_Types].xml"] = re.sub(r'<Override PartName="/ppt/slides/slide%s\.xml"[^>]*/>' % num, "", data["[Content_Types].xml"].decode("utf-8")).encode("utf-8")
    for n in list(data):
        m = re.match(r"ppt/slides/_rels/(slide\d+\.xml)\.rels$", n)
        if not m or ("ppt/slides/" + m.group(1)) not in data: continue
        rels = data[n].decode("utf-8"); sx = "ppt/slides/" + m.group(1); body = data[sx].decode("utf-8")
        for r in re.findall(r"<Relationship [^>]*/>", rels):
            if 'relationships/image"' not in r or 'TargetMode="External"' not in r: continue
            lid = re.search(r'Id="([^"]+)"', r).group(1); tgt = re.search(r'Target="([^"]+)"', r).group(1)
            if 'r:link="%s"' % lid not in body: continue
            p = link_target_path(linked, tgt)
            if not os.path.exists(p): missing.append(os.path.basename(p)); continue
            k += 1; ext = os.path.splitext(p)[1].lower(); exts.add(ext.lstrip("."))
            media = "ppt/media/linked-%d%s" % (k, ext)
            while media in data: k += 1; media = "ppt/media/linked-%d%s" % (k, ext)
            data[media] = open(p, "rb").read()
            eid = lid.replace("Lk", "Em")
            rels = rels.replace(r, '<Relationship Id="%s" Type="%s" Target="../media/%s"/>' % (eid, REL_IMG, posixpath.basename(media)))
            body = body.replace('r:link="%s"' % lid, 'r:embed="%s"' % eid)
        data[n] = rels.encode("utf-8"); data[sx] = body.encode("utf-8")
    if missing: return dict(error="pictures not found in Images", missing=sorted(set(missing)))
    ct = data["[Content_Types].xml"].decode("utf-8")
    for e in exts:
        if not re.search(r'Extension="%s"' % e, ct, re.I) and e in MIME: ct = ct.replace("</Types>", '<Default Extension="%s" ContentType="%s"/></Types>' % (e, MIME[e]))
    data["[Content_Types].xml"] = ct.encode("utf-8")
    write(out, infos, data)
    return dict(embedded=out, pictures=k)

# ---------------------------------------------------------------- status and verify

def pair_state(linked):
    emb = linked.replace("-Linked.pptx", "-Embedded.pptx"); z = zipfile.ZipFile(linked); changed = []; missing = []
    for n in z.namelist():
        if n.startswith("ppt/slides/_rels/"):
            for t in re.findall(r'Target="([^"]+)" TargetMode="External"', z.read(n).decode("utf-8", "ignore")):
                p = link_target_path(linked, t)
                if not os.path.exists(p): missing.append(os.path.basename(p))
                elif os.path.exists(emb) and os.path.getmtime(p) > os.path.getmtime(emb): changed.append(os.path.basename(p))
    if not os.path.exists(emb): state = "no Embedded deck"
    elif os.path.getmtime(linked) > os.path.getmtime(emb): state = "Linked deck changed"
    elif changed: state = "%d picture(s) changed" % len(set(changed))
    else: state = "current"
    return dict(linked=linked, embedded=emb, state=state, changed=sorted(set(changed)), missing=sorted(set(missing)))

def verify(linked):
    """The rules, checked on the files: suffixes, links relative and resolving, nothing teaching embedded in Linked,
    nothing external in Embedded, the same slides and notes apart from the reference slides."""
    emb = linked.replace("-Linked.pptx", "-Embedded.pptx"); base = base_of(linked); problems = []
    if not os.path.exists(emb): return dict(linked=linked, problems=["no Embedded deck"])
    _, L = read(linked); _, E = read(emb)
    lo = [sx for _, sx in slide_order(L) if REF_MARK not in L[sx].decode("utf-8", "ignore")]; eo = [sx for _, sx in slide_order(E)]
    refs = len(slide_order(L)) - len(lo)
    if refs == 0: problems.append("the Linked deck has no reference slide")
    if len(lo) != len(eo): problems.append("slide counts differ: Linked %d (without reference slides), Embedded %d" % (len(lo), len(eo)))
    strip = lambda x: re.sub(r'\s*r:(embed|link)="[^"]+"', "", x)
    for a, b in zip(lo, eo):
        if strip(L[a].decode("utf-8")) != strip(E[b].decode("utf-8")): problems.append("%s differs from its Embedded slide beyond picture storage" % posixpath.basename(a))
        na, nb = rels_name(a), rels_name(b)
        la = re.findall(r'relationships/notesSlide" Target="([^"]+)"', L.get(na, b"").decode()); lb = re.findall(r'relationships/notesSlide" Target="([^"]+)"', E.get(nb, b"").decode())
        if la and lb and L[posixpath.normpath(posixpath.join("ppt/slides", la[0]))] != E[posixpath.normpath(posixpath.join("ppt/slides", lb[0]))]: problems.append("notes differ on " + posixpath.basename(a))
    links = 0
    for n, b in L.items():
        if not n.startswith("ppt/slides/_rels/"): continue
        for r in re.findall(r"<Relationship [^>]*/>", b.decode("utf-8", "ignore")):
            if 'relationships/image"' not in r or 'TargetMode="External"' not in r: continue
            t = re.search(r'Target="([^"]+)"', r).group(1); links += 1
            if t.startswith("file:") or t.startswith("/"): problems.append("absolute link: " + t)
            elif not t.startswith("Images/"): problems.append("link outside Images/: " + t)
            elif not os.path.exists(link_target_path(linked, t)): problems.append("missing picture: " + t)
            elif not urllib.parse.unquote(t[7:]).startswith(base + "-"): problems.append("picture name does not start with %s-: %s" % (base, t))
    for n, b in E.items():
        if n.endswith(".rels") and re.search(r'relationships/image" Target="[^"]+" TargetMode="External"', b.decode("utf-8", "ignore")):
            problems.append("Embedded deck still links a picture: " + n)
    st = pair_state(linked)
    if st["state"] != "current": problems.append("Embedded deck out of date: " + st["state"])
    return dict(linked=linked, embedded=emb, linked_pictures=links, reference_slides=refs, slides=len(lo), problems=problems)

def decks(target, pattern):
    if target.lower().endswith(".pptx"): return [target]
    out = []
    for root, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        if os.path.basename(root) == "Presentations": out += [os.path.join(root, f) for f in files if re.search(pattern, f) and not f.startswith("~$")]
    return sorted(out)

if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 2 or a[0] not in ("split", "embed", "status", "verify", "clean", "uncopy"): print(__doc__); sys.exit(2)
    t = a[1]
    if a[0] == "split": res = [split(d, "--dry" in a) for d in decks(t, r"(?<!-Linked)(?<!-Embedded)\.pptx$")]
    elif a[0] == "embed": res = [embed(d) for d in decks(t, r"-Linked\.pptx$")]
    elif a[0] == "uncopy": res = [uncopy(d) for d in decks(t, r"-Linked\.pptx$")]
    elif a[0] == "clean":
        res = []
        for d in decks(t, r"-Linked\.pptx$"):
            infos, data = read(d); drop_unused_media(data); write(d, infos, data); res.append(dict(cleaned=d, embed=embed(d)))
    elif a[0] == "status": res = [pair_state(d) for d in decks(t, r"-Linked\.pptx$")]
    else: res = [verify(d) for d in decks(t, r"-Linked\.pptx$")]
    print(json.dumps(res, indent=1))
