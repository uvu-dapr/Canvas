#!/usr/bin/env python3
"""
deck_pair.py: every teaching deck as a Linked deck Adam edits and an Embedded deck built from it (Adam, 2026-09-30).

  <Base>-Linked.pptx    the one Adam edits. Each teaching picture is a relative link to Images/<Base>-<Subject>.<ext>
                        (nothing embedded for it).
  <Base>-Embedded.pptx  built from the Linked deck: every picture inside the file. Never edited by hand. Students get
                        its PDF: PDF/<Base>.pdf.
  <Base>-README.txt     where the deck's pictures live, beside the deck. Never a slide, never uploaded (Adam,
                        2026-10-03: "I don't need this kind of stuff in the PowerPoint"). Older Linked decks carried it
                        as slides at the end; `strip` moves them into the README.
  Presentations/Images  shared by every deck in the module; each file starts with its deck's base name.

The two decks are the same file apart from how pictures are stored: slides, order, text,
notes, animations, transitions, crops, alt text and layout are copied, never rebuilt. Icons, checkmarks, warning marks
and pictures in masters and layouts are design, not teaching pictures: they stay inside both decks (Adam, 2026-09-30),
and the README counts them. A picture's subject comes from its alt text, else its slide title; names are never
numbered, and a picture Adam replaces keeps its exact name, so the Linked deck shows it and the Embedded deck is out of
date until it is built again.

    python3 deck_pair.py split  <deck.pptx | folder> [--dry]    make the pair from a single deck (the deck goes to Archive)
    python3 deck_pair.py embed  <Base-Linked.pptx | folder>     build the Embedded deck again from the Linked deck
    python3 deck_pair.py status <folder>                         which Embedded decks are out of date, and why
    python3 deck_pair.py verify <Base-Linked.pptx | folder>      check a pair against the rules
    python3 deck_pair.py uncopy <Base-Linked.pptx | folder>      take out picture copies put inside a Linked deck
    python3 deck_pair.py strip  <Base-Linked.pptx | folder>      reference slides out of the deck, into <Base>-README.txt
    python3 deck_pair.py addpics <Base-Linked.pptx> <spec.json>  pictures with captions onto one slide (see add_pictures)
    python3 deck_pair.py mirror  <Base-Linked.pptx | folder> [--dry]  every link into the PowerPoint mirror; Canvas copies to GitHub
    python3 deck_pair.py place   <Base-Linked.pptx> <slide> <new picture> [--old <file>]  a new picture onto a slide, by link
    python3 deck_pair.py sync                                    refresh the mirror's clones whose files changed
    python3 deck_pair.py unique [folder]                         slide pictures still linked to GitHub: ChatGPT's next work

Mirror (Adam, 2026-10-02: "get them all working with the linked ... so they actually open and show the images").
PowerPoint's sandbox may always read ~/Library/Application Support/Microsoft/, and nothing else without a Grant File
Access click per folder. So every link points at an APFS clone of its picture in MIRROR (no extra disk space, nothing
inside the deck): MIRROR/GitHub/<Classes path> for a Canvas picture, MIRROR/Canvas Links/<path> for the deck's own
picture in Images. The real file is the truth: embed, status and verify read it, and `mirror` refreshes a clone whenever
its file changes. A link into MIRROR/GitHub means the slide still repeats the Canvas picture: ChatGPT makes it a unique
one, and `place` points the slide at the new file in Images (a GitHub picture is never written over).

Links only (Adam, 2026-09-30): a copy of each picture inside the Linked deck made PowerPoint show pictures, but the deck
became Embedded-size and a replaced picture never showed until the copy was refreshed, so copies are not used. On the
Mac, PowerPoint's sandbox cannot follow these links (its Grant File Access panel grants one file at a time); the
pictures show in the Embedded deck and the PDF.

Never touches a deck open in PowerPoint, or anything in Archive, _unused, PDF or Images.
"""
import sys, os, re, io, glob, zipfile, hashlib, html, json, datetime, subprocess, urllib.parse, posixpath, shutil, tempfile

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

# ---------------------------------------------------------------- the PowerPoint mirror (2026-10-02)

MIRROR = os.path.expanduser("~/Library/Application Support/Microsoft/Canvas Preview Pictures")
GITHUB_CLASSES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Classes")
LINKS_ROOT = os.path.expanduser("~/Library/CloudStorage/Dropbox/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links")
ROOTS = (("GitHub", GITHUB_CLASSES), ("Canvas Links", LINKS_ROOT))

def mirror_path(real):
    real = os.path.abspath(real)
    for name, root in ROOTS:
        if real.startswith(root + "/"): return os.path.join(MIRROR, name, real[len(root) + 1:])
    return os.path.join(MIRROR, "Other", real.lstrip("/"))

def real_path(p):
    """A mirror clone's own file; any other path is already real."""
    if not p.startswith(MIRROR + "/"): return p
    rest = p[len(MIRROR) + 1:]
    for name, root in ROOTS:
        if rest.startswith(name + "/"): return os.path.join(root, rest[len(name) + 1:])
    return "/" + rest[len("Other/"):] if rest.startswith("Other/") else p

def mirror_sync(real):
    """Clones the file into the mirror when the clone is missing or older; returns the clone's path."""
    m = mirror_path(real)
    if os.path.exists(real):
        st = os.stat(real)
        if not os.path.exists(m) or os.path.getsize(m) != st.st_size or abs(os.path.getmtime(m) - st.st_mtime) > 1:
            os.makedirs(os.path.dirname(m), exist_ok=True)
            tmp = m + ".part"
            if subprocess.run(["cp", "-c", "-p", real, tmp]).returncode != 0: shutil.copy2(real, tmp)
            os.replace(tmp, m)
    return m

def mirror_link(real): return "file://" + urllib.parse.quote(mirror_sync(real))
def is_github(real): return os.path.abspath(real).startswith(GITHUB_CLASSES + "/")

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

NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main", "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
      "p": "http://schemas.openxmlformats.org/presentationml/2006/main", "a14": "http://schemas.microsoft.com/office/drawing/2010/main",
      "p14": "http://schemas.microsoft.com/office/powerpoint/2010/main", "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006"}

def fix_ns(x):
    # a slide whose root does not declare a prefix its shapes use is refused by PowerPoint (2026-10-10: decks saved by
    # ElementTree declare a: on each element, so a picture inserted without its own xmlns:a / xmlns:r broke the file)
    m = re.search(r"<p:sld\b[^>]*>", x)
    if not m: return x
    root = m.group(0); add = "".join(' xmlns:%s="%s"' % (k, v) for k, v in NS.items() if ("<%s:" % k in x or " %s:" % k in x) and "xmlns:%s=" % k not in root)
    return x if not add else x.replace(root, root[:-1] + add + ">", 1) if not root.endswith("/>") else x

def write(path, infos, data):
    for n in list(data):
        if re.match(r"ppt/slides/slide\d+\.xml$", n): data[n] = fix_ns(data[n].decode("utf-8")).encode("utf-8")
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

def slide_title(xml):
    """The title placeholder's words, or else the first words on the slide that are not the footer or a page number."""
    t = title_of(xml)
    if t: return t
    for x in re.findall(r"<a:t>([^<]*)</a:t>", xml):
        x = html.unescape(x).strip()
        if x and not x.startswith("DAPR") and not x.isdigit(): return x
    return ""

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
            new_rels.append('<Relationship Id="%s" Type="%s" Target="%s" TargetMode="External"/>' % (lid, REL_IMG, mirror_link(os.path.join(images, name))))
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
    result = dict(deck=deck, base=base, linked=linked_path, embedded=emb_path, pictures_linked=len(listing), files=len(used),
                  design_marks_inside=design, not_linked=not_linked, kept_existing=kept_existing)
    if dry: result["dry"] = True; result["names"] = sorted(set(n for _, n in listing)); return result
    arch = os.path.join(pres_dir, "Archive"); os.makedirs(arch, exist_ok=True)
    keep = os.path.join(arch, "%s (before Linked and Embedded %s).pptx" % (stem, datetime.date.today().isoformat()))
    if not os.path.exists(keep): shutil.move(deck, keep)
    write(linked_path, infos, data)
    write_note(linked_path, course, module, base, listing, design, not_linked)
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

NOTE_SUFFIX = "-README.txt"     # never uploaded: CloudflareChanges.localFiles skips it (Canvas Preview)

def note_path(deck): return os.path.join(os.path.dirname(os.path.abspath(deck)), base_of(deck) + NOTE_SUFFIX)

def write_note(deck, course, module, base, listing, design, not_linked):
    """<Base>-README.txt beside the deck: where its pictures live. It is never a slide (Adam, 2026-10-03: "put it in a
    note somewhere ... next to the PowerPoint in a read me"); students never see it and Canvas Preview never uploads it.
    Written only when its words change, so Dropbox and the deck dates stay quiet."""
    readable = lambda s: s.replace("--", " - ").replace("__", ": ").replace("_", " ")
    lines = ["%s: linked picture reference" % base,
             "Notes for Adam only. Not part of the deck, never uploaded, never seen by students. Canvas Preview rewrites this file.",
             "",
             "Course: %s" % readable(course), "Module: %s" % readable(module),
             "Presentation: %s-Linked.pptx (edit this one)" % base,
             "Built from it: %s-Embedded.pptx (all pictures inside) and PDF/%s.pdf (what students get)" % (base, base),
             "PowerPoint base name: %s" % base,
             "Image folder: Images/ beside this deck",
             "Full path: Canvas Links/%s/%s/Presentations/Images/" % (course, module),
             "Image file name prefix: %s-" % base,
             "Replace a picture by saving over its file under the same name. Canvas Preview then shows %s-Embedded.pptx as out of date: Update rebuilds it and its PDF." % base,
             "Pictures linked: %d, in %d file(s). Design marks kept inside the deck (icons, checkmarks, warning marks, master and layout pictures): %d." % (len(listing), len(set(n for _, n in listing)), design),
             ("Not linked (kept inside): " + "; ".join(not_linked)) if not_linked else "Unusual dependencies: none. Every teaching picture is a linked file in Images/.",
             "", "Linked pictures, by slide:"] + ["Slide %d: %s" % (p, n) for p, n in listing]
    text = "\n".join(lines) + "\n"; path = note_path(deck)
    try:
        if open(path, encoding="utf-8").read() == text: return path
    except OSError: pass
    open(path, "w", encoding="utf-8").write(text)
    return path

def note_counts(deck):
    """The design-mark count and not-linked list the README (or an older reference slide) recorded: only split can count them."""
    try: old = open(note_path(deck), encoding="utf-8").read()
    except OSError: return 0, []
    m = re.search(r"master and layout pictures\): (\d+)", old); n = re.search(r"Not linked \(kept inside\): (.*)", old)
    return (int(m.group(1)) if m else 0), (n.group(1).split("; ") if n else [])

def remove_reference_slides(data):
    """Takes the old reference slides out of a deck. Returns how many, with the counts they recorded (or None)."""
    pres = data["ppt/presentation.xml"].decode("utf-8"); prels = data["ppt/_rels/presentation.xml.rels"].decode("utf-8")
    ct = data["[Content_Types].xml"].decode("utf-8"); k = 0; counts = None
    for rid, sx in slide_order(data):
        if sx in data and REF_MARK in data[sx].decode("utf-8"):
            old = data[sx].decode("utf-8"); k += 1
            m = re.search(r"master and layout pictures\): (\d+)", old); n = re.search(r"Not linked \(kept inside\): ([^<]*)", old)
            if m or n: counts = (int(m.group(1)) if m else 0, [html.unescape(x) for x in n.group(1).split("; ")] if n else [])
            pres = re.sub(r'<p:sldId [^>]*r:id="%s"\s*/>' % re.escape(rid), "", pres)
            prels = re.sub(r'<Relationship [^>]*Id="%s"[^>]*/>' % re.escape(rid), "", prels)
            ct = ct.replace('<Override PartName="/%s" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>' % sx, "")
            data.pop(sx, None); data.pop(rels_name(sx), None)
    data["ppt/presentation.xml"] = pres.encode("utf-8"); data["ppt/_rels/presentation.xml.rels"] = prels.encode("utf-8"); data["[Content_Types].xml"] = ct.encode("utf-8")
    return k, counts

# ---------------------------------------------------------------- addpics

def slide_size(data):
    m = re.search(r'<p:sldSz cx="(\d+)" cy="(\d+)"', data["ppt/presentation.xml"].decode("utf-8"))
    return (int(m.group(1)), int(m.group(2))) if m else (9144000, 6858000)

def title_bottom(data, sx):
    """Where the slide's title ends: its own box, else its layout's, else a fifth of the way down"""
    body = data[sx].decode("utf-8")
    for xml in [body] + [data.get(posixpath.normpath(posixpath.join(posixpath.dirname(sx), t)), b"").decode("utf-8")
                         for t in re.findall(r'Target="(\.\./slideLayouts/[^"]+)"', data.get(rels_name(sx), b"").decode("utf-8"))]:
        for m in shapes(xml):
            if re.search(r'<p:ph [^>]*type="(title|ctrTitle)"', m.group(0)):
                g = re.search(r'<a:off x="\d+" y="(\d+)"/><a:ext cx="\d+" cy="(\d+)"', m.group(0))
                if g: return int(g.group(1)) + int(g.group(2))
    return slide_size(data)[1] // 5

def body_top(data, sx):
    """The top of the slide's body text placeholder: on the slide, else its layout, else the master"""
    def find(xml, master=False):
        for m in shapes(xml):
            if re.search(r'<p:ph (?:type="body" )?idx="1"' if not master else r'<p:ph type="body"', m.group(0)):
                g = re.search(r'<a:off x="\d+" y="(\d+)"/>', m.group(0))
                if g: return int(g.group(1))
        return None
    y = find(data[sx].decode("utf-8"))
    if y: return y
    for t in re.findall(r'Target="(\.\./slideLayouts/[^"]+)"', data.get(rels_name(sx), b"").decode("utf-8")):
        lay = posixpath.normpath(posixpath.join(posixpath.dirname(sx), t))
        y = find(data.get(lay, b"").decode("utf-8"))
        if y: return y
        for mt in re.findall(r'Target="(\.\./slideMasters/[^"]+)"', data.get(rels_name(lay), b"").decode("utf-8")):
            y = find(data.get(posixpath.normpath(posixpath.join(posixpath.dirname(lay), mt)), b"").decode("utf-8"), master=True)
            if y: return y
    return None

def content_crop(path):
    """The empty (transparent or near-white) margins around a picture, as a srcRect crop, so a generated diagram fills
    its space (imgbounds.swift beside this file, built once into the cache). {} when there is nothing to trim."""
    tool = os.path.expanduser("~/Library/Caches/CanvasPreview/imgbounds")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgbounds.swift")
    if not os.path.exists(tool) or os.path.getmtime(tool) < os.path.getmtime(src):
        os.makedirs(os.path.dirname(tool), exist_ok=True)
        subprocess.run(["swiftc", "-O", src, "-o", tool], capture_output=True)
    try: v = [int(x) for x in subprocess.run([tool, path], capture_output=True, text=True, timeout=60).stdout.split()]
    except Exception: return {}
    if len(v) != 4 or max(v) < 1500: return {}
    return dict(zip(("l", "t", "r", "b"), v))

def image_size(path):
    r = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path], capture_output=True, text=True).stdout
    w = re.search(r"pixelWidth: (\d+)", r); h = re.search(r"pixelHeight: (\d+)", r)
    return (int(w.group(1)), int(h.group(1))) if w and h else (4, 3)

def refresh_reference(data, deck):
    """The README again, from the links the deck has now (after pictures are added or removed); any old reference
    slide leaves the deck. Returns the listing."""
    _, counts = remove_reference_slides(data)
    design, not_linked = counts or note_counts(deck)
    listing = []
    for pos, (rid, sx) in enumerate(slide_order(data), 1):
        rels = data.get(rels_name(sx), b"").decode("utf-8"); body = data.get(sx, b"").decode("utf-8")
        for r in re.findall(r"<Relationship [^>]*/>", rels):
            if 'TargetMode="External"' in r and 'relationships/image"' in r:
                lid = re.search(r'Id="([^"]+)"', r).group(1)
                if re.search(r'r:link="%s"' % re.escape(lid), body):
                    real = link_target_path(deck, re.search(r'Target="([^"]+)"', r).group(1))
                    listing.append((pos, ("Canvas picture, make unique: " if is_github(real) else "") + os.path.basename(real)))
    course, module = course_and_module(deck)
    write_note(deck, course, module, base_of(deck), listing, design, not_linked)
    return listing

def strip(linked):
    """Old reference slides out of a Linked deck and into its README, keeping the deck's date: the slides students see
    are unchanged, so the Embedded deck and PDF stay current."""
    if is_open(linked): return dict(linked=linked, skipped="open in PowerPoint; close it and run again")
    infos, data = read(linked)
    refs = sum(1 for _, sx in slide_order(data) if REF_MARK in data.get(sx, b"").decode("utf-8", "ignore"))
    if not refs and os.path.exists(note_path(linked)): return dict(linked=linked, slides_removed=0)    # nothing to do (every launch)
    refresh_reference(data, linked)
    if refs:
        st = os.stat(linked); write(linked, infos, data); os.utime(linked, (st.st_atime, st.st_mtime))
    return dict(linked=linked, slides_removed=refs, readme=note_path(linked))

def resize_body(body, xfrm, title_y, keep_y=False):
    """Moves the slide's body text into xfrm: its body placeholder, else (decks built from text boxes) the text box
    with the most words below the title"""
    def place(sp):
        x = xfrm
        g = geom(sp)
        if keep_y and g:   # a text box keeps its own top and height; only its width changes (subtitles above stay clear)
            n = re.search(r'<a:off x="(\d+)" y="\d+"/><a:ext cx="(\d+)" cy="\d+"', xfrm)
            x = '<a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>' % (g[0], g[1], int(n.group(1)) + int(n.group(2)) - g[0], g[3])
        if re.search(r"<p:spPr\s*/>", sp): return re.sub(r"<p:spPr\s*/>", "<p:spPr>%s</p:spPr>" % x, sp, count=1)
        if "<a:xfrm" in sp: return re.sub(r"(?s)<a:xfrm.*?</a:xfrm>", x, sp, count=1)
        return sp.replace("<p:spPr>", "<p:spPr>" + x, 1)
    m = re.search(r'(?s)<p:sp>(?:(?!</p:sp>).)*?<p:ph (?:type="body" )?idx="1"[^>]*/>.*?</p:sp>', body)
    if m: return body[:m.start()] + place(m.group(0)) + body[m.end():]
    m = text_body(body, title_y)
    if m: return body[:m.start()] + place(m.group(0)) + body[m.end():]
    return body

def text_body(body, title_y):
    """The bullets of a slide built from text boxes: the text box with the most words below the title"""
    best = None
    for m in shapes(body):
        sp = m.group(0)
        if not sp.startswith("<p:sp>") or re.search(r'<p:ph [^>]*type="(title|ctrTitle)"', sp): continue
        g = geom(sp); words = len(" ".join(re.findall(r"<a:t>([^<]*)</a:t>", sp)).split())
        if g and g[1] >= title_y * 0.8 and words > 3 and (best is None or words > best[0]): best = (words, m)
    return best[1] if best else None

def add_pictures(linked, spec, archive=True, build=True):
    """Pictures onto one slide of a Linked deck (Adam, 2026-10-01: "Show a picture"). spec: {"slide": 7, "layout":
    "rows" | "columns" | "side" (bullets kept on the left, pictures stacked on the right with a label) | "below" (bullets
    kept on top, body_frac of the space, a wide picture under them), "trim": true (empty margins cropped), "replace_body": true, "pictures": [{"src": <image file>, "subject": "RODE_SoundField_NT_SF1",
    "title": "RØDE SoundField NT-SF1", "text": "...", "alt": "...", "crop": {"t": 0, "b": 35000, "l": 0, "r": 0},
    "source": "where it came from"}]}. Each picture is copied to Images/<Base>-<Subject>.<ext> (never over a
    different file) and linked; with replace_body the slide's bullet text box gives way to the pictures and their
    captions, which carry its facts. The deck before goes to Archive; the README and the Embedded deck are
    built again."""
    if is_open(linked): return dict(deck=linked, skipped="open in PowerPoint; close it and run again")
    infos, data = read(linked)
    order = slide_order(data); n = spec["slide"]
    if not 1 <= n <= len(order): return dict(deck=linked, error="no slide %d" % n)
    sx = order[n - 1][1]; body = data[sx].decode("utf-8"); rn = rels_name(sx); rels = data.get(rn, b"").decode("utf-8")
    base = base_of(linked); images = os.path.join(os.path.dirname(os.path.abspath(linked)), "Images")
    W, H = slide_size(data)
    pics = spec["pictures"]
    # the files, one per deck: Images/<Base>-<Subject>.<ext>
    names = []
    for p in pics:
        ext = os.path.splitext(p["src"])[1].lower().replace(".jpeg", ".jpg")
        name = "%s-%s%s" % (base, p["subject"], ext); dst = os.path.join(images, name)
        blob = open(p["src"], "rb").read()
        if os.path.exists(dst) and sha(open(dst, "rb").read()) != sha(blob): return dict(deck=linked, error="%s already exists with a different picture" % name)
        names.append((name, dst, blob))
    # the area the slide's bullet text had (its body placeholder, from the slide, its layout or the master), else
    # under the title: a design's banner can reach below the title box (3340's purple band, 2026-10-01)
    bt = body_top(data, sx)
    top = bt if bt else title_bottom(data, sx) + int(H * 0.03)
    if not re.search(r'<p:ph (?:type="body" )?idx="1"', body):
        # bullets in a text box: they start at their own top, not at the layout's or master's placeholder, which can
        # sit above a subtitle line (3340 The_Dolby_Atmos_Renderer slide 19, 2026-10-01)
        tb = text_body(body, top); g = geom(tb.group(0)) if tb else None
        if g: top = max(top, g[1])
    bottom = H - int(H * 0.06); left = int(W * 0.06); right = W - int(W * 0.06)
    layout = spec.get("layout", "rows"); side = layout == "side"; below = layout == "below"; placed = layout == "place"
    if below:
        # the bullets stay on top; a wide picture (or two) goes under them, full width (a strip-shaped diagram)
        body_h = int((bottom - top) * spec.get("body_frac", 0.5))
        bx = '<a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>' % (left, top, right - left, body_h)
        body = resize_body(body, bx, top)
        ptop = top + body_h + int(H * 0.02)
    if side:
        # the bullets stay, in the left part; the pictures go on the right (one or two, each with a short label)
        split_x = left + int((right - left) * 0.54)
        bx = '<a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>' % (left, top, split_x - left - int(W * 0.02), bottom - top)
        body = resize_body(body, bx, top, keep_y=bt is None)
    elif not below and not placed and spec.get("replace_body", True):
        body = re.sub(r'(?s)<p:sp>(?:(?!</p:sp>).)*?<p:ph (?:type="body" )?idx="1"[^>]*/>.*?</p:sp>', "", body, count=1)
    ids = [int(x) for x in re.findall(r'<p:cNvPr id="(\d+)"', body)] or [1]
    nid = max(ids) + 1
    k = len(pics); gap = int(H * 0.02); xml = []; new_rels = []; placed_boxes = []
    rows = spec.get("layout", "rows") == "rows"
    for i, (p, (name, dst, blob)) in enumerate(zip(pics, names)):
        if placed:
            # an exact spot (fractions of the slide) where the slide has room; nothing else on the slide moves
            fx, fy, fw, fh = p.get("box", spec.get("box"))
            cap = int(H * 0.05) if p.get("title") else 0
            box = (int(W * fx), int(H * fy), int(W * fw), int(H * fh) - cap); tbox = (box[0], box[1] + box[3], box[2], cap)
        elif below:
            cw = (right - left - gap * (k - 1)) // k; cap = int(H * 0.055); x0 = left + i * (cw + gap)
            box = (x0, ptop, cw, bottom - ptop - cap); tbox = (x0, bottom - cap, cw, cap)
        elif side:
            sh = (bottom - top - gap * (k - 1)) // k; y = top + i * (sh + gap); cap = int(H * 0.055)
            box = (split_x, y, right - split_x, sh - cap); tbox = (split_x, y + sh - cap, right - split_x, cap)
        elif rows:
            ch = (bottom - top - gap * (k - 1)) // k; y = top + i * (ch + gap)
            box = (left, y, int((right - left) * 0.5), ch); tbox = (left + int((right - left) * 0.53), y, int((right - left) * 0.47), ch)
        else:
            cw = (right - left - gap * (k - 1)) // k; x = left + i * (cw + gap); ih = int((bottom - top) * 0.62)
            box = (x, top, cw, ih); tbox = (x, top + ih + gap, cw, bottom - top - ih - gap)
        pw, ph = image_size(p["src"])
        c = p["crop"] if "crop" in p else (content_crop(p["src"]) if spec.get("trim", True) else {})
        vw = pw * (1 - (c.get("l", 0) + c.get("r", 0)) / 100000); vh = ph * (1 - (c.get("t", 0) + c.get("b", 0)) / 100000)
        scale = min(box[2] / vw, box[3] / vh); w, h = int(vw * scale), int(vh * scale)
        x = box[0] + (box[2] - w) // 2; y = box[1] + (box[3] - h) // 2
        if side or below or placed:   # the label right under its picture, the two centered in their space
            y = box[1] + max(0, (box[3] + tbox[3] - (h + tbox[3])) // 2)
            tbox = (tbox[0], y + h, tbox[2], tbox[3])
        lid = "rIdLk%d" % (i + 1)
        while lid in rels or any(lid in r for r in new_rels): lid += "x"
        new_rels.append('<Relationship Id="%s" Type="%s" Target="%s" TargetMode="External"/>' % (lid, REL_IMG, mirror_link(os.path.join(os.path.dirname(os.path.abspath(linked)), "Images", name))))
        src_rect = ('<a:srcRect%s/>' % "".join(' %s="%d"' % (kk, vv) for kk, vv in c.items() if vv)) if c else ""
        alt = html.escape(p.get("alt") or p.get("title", ""), quote=True)
        xml.append('<p:pic><p:nvPicPr><p:cNvPr id="%d" name="Picture %d" descr="%s"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>'
                   '<p:blipFill><a:blip r:link="%s"/>%s<a:stretch><a:fillRect/></a:stretch></p:blipFill><p:spPr><a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
                   '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>' % (nid, nid, alt, lid, src_rect, x, y, w, h))
        nid += 1; placed_boxes.append((x, y, w, h))
        if side or below or placed:
            paras = '<a:p><a:pPr algn="ctr"/><a:r><a:rPr lang="en-US" sz="%d" dirty="0"><a:solidFill><a:srgbClr val="595959"/></a:solidFill></a:rPr><a:t>%s</a:t></a:r></a:p>' % (spec.get("label_size", 1200), html.escape(p.get("title", ""), quote=False))
        else:
            paras = '<a:p><a:r><a:rPr lang="en-US" sz="%d" b="1" dirty="0"/><a:t>%s</a:t></a:r></a:p>' % (spec.get("title_size", 2000), html.escape(p.get("title", ""), quote=False))
        if p.get("text") and not (side or below or placed): paras += '<a:p><a:spcBef><a:spcPts val="300"/></a:spcBef><a:r><a:rPr lang="en-US" sz="%d" dirty="0"/><a:t>%s</a:t></a:r></a:p>' % (spec.get("text_size", 1600), html.escape(american(p["text"]), quote=False))
        if placed and not p.get("title"): continue
        xml.append('<p:sp><p:nvSpPr><p:cNvPr id="%d" name="Caption %d"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
                   '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr wrap="square" anchor="%s"><a:normAutofit/></a:bodyPr><a:lstStyle/>%s</p:txBody></p:sp>'
                   % (nid, nid, tbox[0], tbox[1], tbox[2], tbox[3], "ctr" if rows else "t", paras))
        nid += 1
    # Never a postage stamp: on a table slide the "room beside the text" is a footnote strip, and the picture came out a
    # few percent of the slide (2026-10-06, Transistors "Three Amplifier Configurations"); a new slide after is better
    if not placed and any(ph < H * 0.18 for (_, _, _, ph) in placed_boxes):
        return dict(deck=linked, error="slide %d has no room: the picture would be too small to read; pick a box (layout place) or another slide" % n)
    # Never over another shape: card layouts (boxes spread across the slide) have no room the body can give up, and a
    # picture placed there covered a worked example (2026-10-06, Surround_Recording slide 14 and seven more)
    for sp in re.findall(r"(?s)<p:(?:sp|pic|graphicFrame|grpSp)>.*?</p:(?:sp|pic|graphicFrame|grpSp)>", body):
        g = re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"/><a:ext cx="(\d+)" cy="(\d+)"/>', sp)
        if not g: continue
        ox, oy, ow, oh = (int(v) for v in g.groups())
        if oy > H * 0.92 or ow * oh > W * H * 0.9: continue          # footer band, or a full-slide background
        for (px, py, pw_, ph_) in placed_boxes:
            if px < ox + ow - W * 0.01 and ox < px + pw_ - W * 0.01 and py < oy + oh - H * 0.01 and oy < py + ph_ - H * 0.01:
                nm = re.search(r'name="([^"]*)"', sp)
                return dict(deck=linked, error="slide %d has no room: the picture would cover %s; pick a box (layout place) or another slide" % (n, nm.group(1) if nm else "a shape"))
    body = body.replace("</p:spTree>", "".join(xml) + "</p:spTree>", 1)
    data[sx] = body.encode("utf-8")
    data[rn] = (rels or '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"></Relationships>').replace("</Relationships>", "".join(new_rels) + "</Relationships>").encode("utf-8")
    listing = refresh_reference(data, linked)
    for name, dst, blob in names:
        if not os.path.exists(dst): os.makedirs(images, exist_ok=True); open(dst, "wb").write(blob)
    arch = os.path.join(os.path.dirname(os.path.abspath(linked)), "Archive"); os.makedirs(arch, exist_ok=True)
    keep = os.path.join(arch, "%s (before pictures %s).pptx" % (os.path.splitext(os.path.basename(linked))[0], datetime.datetime.now().strftime("%Y-%m-%d %H%M")))
    if archive and not os.path.exists(keep): shutil.copy2(linked, keep)
    write(linked, infos, data)
    return dict(deck=linked, slide=n, pictures=[x[0] for x in names], linked_now=len(listing), archived=keep if archive else None, embed=embed(linked) if build else None)

# ---------------------------------------------------------------- unpic

def remove_picture(linked, slide, subject, build=True):
    """Takes one addpics picture back off a slide: the picture linked to Images/<Base>-<Subject>.*, the caption box
    right after it, and its link; the bullets keep the size addpics gave them (a later addpics or picslide redoes it)."""
    if is_open(linked): return dict(deck=linked, skipped="open in PowerPoint; close it and run again")
    infos, data = read(linked); order = slide_order(data); sx = order[slide - 1][1]; rn = rels_name(sx)
    body = data[sx].decode("utf-8"); rels = data.get(rn, b"").decode("utf-8")
    ids = [m.group(1) for m in re.finditer(r'<Relationship Id="([^"]+)"[^>]*Target="[^"]*%s-%s\.[a-z]+"' % (re.escape(urllib.parse.quote(base_of(linked))), re.escape(subject)), rels)]
    ids += [m.group(1) for m in re.finditer(r'<Relationship Id="([^"]+)"[^>]*Target="[^"]*%s-%s\.[a-z]+"' % (re.escape(base_of(linked)), re.escape(subject)), rels)]
    if not ids: return dict(deck=linked, error="no picture %s on slide %d" % (subject, slide))
    for rid in set(ids):
        body = re.sub(r'(?s)<p:pic>(?:(?!</p:pic>).)*?r:link="%s".*?</p:pic>(<p:sp><p:nvSpPr><p:cNvPr id="\d+" name="Caption \d+"/>.*?</p:sp>)?' % re.escape(rid), "", body, count=1)
        rels = re.sub(r'<Relationship Id="%s"[^>]*/>' % re.escape(rid), "", rels)
    data[sx] = body.encode("utf-8"); data[rn] = rels.encode("utf-8")
    write(linked, infos, data)
    return dict(deck=linked, slide=slide, removed=subject, embed=embed(linked) if build else None)

# ---------------------------------------------------------------- picslide

def layout_title_bottom(data, sx, H):
    """Where a title that takes its position from the layout (or the master) ends; 20% of the height when neither says."""
    def part_of(src, kind):
        rels = data.get(rels_name(src), b"").decode("utf-8")
        m = re.search(r'<Relationship [^>]*relationships/%s"[^>]*/>' % kind, rels)
        return posixpath.normpath(posixpath.join(posixpath.dirname(src), re.search(r'Target="([^"]+)"', m.group(0)).group(1))) if m else None
    lay = part_of(sx, "slideLayout"); mas = part_of(lay, "slideMaster") if lay else None
    for p in (lay, mas):
        if not p or p not in data: continue
        for sp in re.findall(r"(?s)<p:sp>.*?</p:sp>", data[p].decode("utf-8")):
            if re.search(r'<p:ph [^>]*type="(title|ctrTitle)"', sp):
                g = re.search(r'<a:off x="-?\d+" y="(-?\d+)"/><a:ext cx="\d+" cy="(\d+)"/>', sp)
                if g: return int(g.group(1)) + int(g.group(2))
    return int(H * 0.2)

def picture_slide(linked, after, pic, archive=True, build=True):
    """A new slide right after slide `after`, for a picture that has no room on a card-layout slide (Adam, 2026-10-06:
    "new slide right after"). It copies that slide's background, its title (and anything above the cards) and its
    footer, then shows the picture large under the title. Every later slide's page number footer moves down one.
    pic: {"src", "subject", "alt"}; the file is copied to Images/<Base>-<Subject>.<ext> and linked like addpics."""
    if is_open(linked): return dict(deck=linked, skipped="open in PowerPoint; close it and run again")
    infos, data = read(linked); order = slide_order(data)
    if not 1 <= after <= len(order): return dict(deck=linked, error="no slide %d" % after)
    W, H = slide_size(data); sx = order[after - 1][1]; body = data[sx].decode("utf-8")
    # the slide may already have its picture slide right after it (2026-10-06: seven MIDI duplicates)
    if after < len(order):
        nxt = data[order[after][1]].decode("utf-8")
        if "<p:pic>" in nxt and slide_title(nxt) and slide_title(nxt) == slide_title(body):
            return dict(deck=linked, error="slide %d already has a picture slide right after it" % after)
    base = base_of(linked); images = os.path.join(os.path.dirname(os.path.abspath(linked)), "Images")
    ext = os.path.splitext(pic["src"])[1].lower().replace(".jpeg", ".jpg"); name = "%s-%s%s" % (base, pic["subject"], ext); dst = os.path.join(images, name)
    blob = open(pic["src"], "rb").read()
    if os.path.exists(dst) and sha(open(dst, "rb").read()) != sha(blob): return dict(deck=linked, error="%s already exists with a different picture" % name)
    def pagenum(xml, old, new):
        # the footer text box that holds only this slide's number
        def fix(m):
            sp = m.group(0); g = re.search(r'<a:off x="-?\d+" y="(\d+)"', sp)
            if g and int(g.group(1)) > H * 0.9 and re.sub(r"<[^>]+>", "", re.search(r"(?s)<p:txBody>.*</p:txBody>", sp).group(0) if "<p:txBody>" in sp else "").strip() == str(old):
                return sp.replace("<a:t>%d</a:t>" % old, "<a:t>%d</a:t>" % new, 1)
            return sp
        return re.sub(r"(?s)<p:sp>.*?</p:sp>", fix, xml)
    # the new slide: background, the shapes above the cards, the footer; then the picture
    keep, top = [], int(H * 0.12)
    for m in re.finditer(r"(?s)<p:(sp|pic|grpSp|graphicFrame|cxnSp)>.*?</p:\1>", body):
        sp = m.group(0); g = re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"/><a:ext cx="(\d+)" cy="(\d+)"/>', sp)
        # a title placeholder that takes its position from the layout (older 4:3 decks) still comes along
        if not g and re.search(r'<p:ph [^>]*type="(title|ctrTitle)"', sp): keep.append(sp); top = max(top, layout_title_bottom(data, sx, H)); continue
        if not g: continue
        oy, oh = int(g.group(2)), int(g.group(4))
        if oy >= H * 0.9: keep.append(sp)
        elif oy + oh <= H * 0.19: keep.append(sp); top = max(top, oy + oh)
    tree_open = re.search(r"(?s)<p:spTree>.*?(?:</p:grpSpPr>|<p:grpSpPr/>)", body).group(0)
    new = body[:body.index("<p:spTree>")] + tree_open + "".join(keep) + "</p:spTree>" + body[body.index("</p:spTree>") + len("</p:spTree>"):]
    new = re.sub(r'<p:cSld name="[^"]*">', "<p:cSld>", new)
    # copied shapes keep no links: the new slide's rels carry only its layout and picture (2026-10-09: a copied arrow
    # button's slide-jump link pointed at a missing rId and PowerPoint refused the whole deck)
    new = re.sub(r'<a:hlink(?:Click|Hover) r:id="[^"]*"[^>]*?(?:/>|>.*?</a:hlink(?:Click|Hover)>)', "", new, flags=re.S)
    new = pagenum(new, after, after + 1)
    ptop = top + int(H * 0.04); pbot = int(H * 0.9); left = int(W * 0.06); right = W - int(W * 0.06)
    pw, ph = image_size(pic["src"]); c = content_crop(pic["src"])
    vw = pw * (1 - (c.get("l", 0) + c.get("r", 0)) / 100000); vh = ph * (1 - (c.get("t", 0) + c.get("b", 0)) / 100000)
    sc = min((right - left) / vw, (pbot - ptop) / vh); w, h = int(vw * sc), int(vh * sc)
    x = left + (right - left - w) // 2; y = ptop + (pbot - ptop - h) // 2
    ids = [int(v) for v in re.findall(r'<p:cNvPr id="(\d+)"', new)] or [1]
    src_rect = ('<a:srcRect%s/>' % "".join(' %s="%d"' % (kk, vv) for kk, vv in c.items() if vv)) if c else ""
    new = new.replace("</p:spTree>", '<p:pic><p:nvPicPr><p:cNvPr id="%d" name="Picture %d" descr="%s"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>'
        '<p:blipFill><a:blip r:link="rIdLk1"/>%s<a:stretch><a:fillRect/></a:stretch></p:blipFill><p:spPr><a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic></p:spTree>' % (max(ids) + 1, max(ids) + 1, html.escape(pic.get("alt", ""), quote=True), src_rect, x, y, w, h), 1)
    # its part, relationships and content type
    nums = [int(v) for v in re.findall(r"ppt/slides/slide(\d+)\.xml$", "\n".join(data), re.M)]
    part = "ppt/slides/slide%d.xml" % (max(nums) + 1)
    lay = re.search(r'<Relationship [^>]*relationships/slideLayout"[^>]*/>', data[rels_name(sx)].decode("utf-8")).group(0)
    data[part] = new.encode("utf-8")
    # anything else the copied slide still points at (a picture background, 2026-10-09) brings its relationship along
    src_rels = data[rels_name(sx)].decode("utf-8"); extra = ""
    for r_id in sorted(set(re.findall(r'r:(?:id|embed|link)="([^"]+)"', new)) - {"rIdLk1"}):
        m = re.search(r'<Relationship (?=[^>]*Id="%s")[^>]*/>' % re.escape(r_id), src_rels)
        if m and "slideLayout" not in m.group(0): extra += m.group(0)
    data[rels_name(part)] = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">%s%s'
        '<Relationship Id="rIdLk1" Type="%s" Target="%s" TargetMode="External"/></Relationships>' % (lay, extra, REL_IMG, mirror_link(dst))).encode("utf-8")
    ct = data["[Content_Types].xml"].decode("utf-8")
    data["[Content_Types].xml"] = ct.replace("</Types>", '<Override PartName="/%s" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/></Types>' % part, 1).encode("utf-8")
    prels = data["ppt/_rels/presentation.xml.rels"].decode("utf-8"); rid = "rIdPs1"
    while rid in prels: rid += "x"
    data["ppt/_rels/presentation.xml.rels"] = prels.replace("</Relationships>", '<Relationship Id="%s" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/%s"/></Relationships>' % (rid, posixpath.basename(part)), 1).encode("utf-8")
    pres = data["ppt/presentation.xml"].decode("utf-8")
    sid = max(int(v) for v in re.findall(r'<p:sldId id="(\d+)"', pres)) + 1
    prev = re.findall(r'<p:sldId [^>]*/>', pres)[after - 1]
    data["ppt/presentation.xml"] = pres.replace(prev, prev + '<p:sldId id="%d" r:id="%s"/>' % (sid, rid), 1).encode("utf-8")
    # later slides' page numbers move down one
    for k, (_, p) in enumerate(order[after:], start=after + 1):
        data[p] = pagenum(data[p].decode("utf-8"), k, k + 1).encode("utf-8")
    app = data.get("docProps/app.xml")
    if app: data["docProps/app.xml"] = re.sub(r"<Slides>\d+</Slides>", "<Slides>%d</Slides>" % (len(order) + 1), app.decode("utf-8")).encode("utf-8")
    listing = refresh_reference(data, linked)
    if not os.path.exists(dst): os.makedirs(images, exist_ok=True); open(dst, "wb").write(blob)
    arch = os.path.join(os.path.dirname(os.path.abspath(linked)), "Archive"); os.makedirs(arch, exist_ok=True)
    keepf = os.path.join(arch, "%s (before pictures %s).pptx" % (os.path.splitext(os.path.basename(linked))[0], datetime.datetime.now().strftime("%Y-%m-%d %H%M")))
    if archive and not os.path.exists(keepf): shutil.copy2(linked, keepf)
    write(linked, infos, data)
    return dict(deck=linked, new_slide=after + 1, picture=name, linked_now=len(listing), embed=embed(linked) if build else None)

# ---------------------------------------------------------------- unpicslide

def remove_picture_slide(linked, slide, build=True):
    """Takes out a picture slide that picslide made (one linked picture, nothing else but the copied title and
    footer) and moves every later slide's page number footer back up one. The reverse of picture_slide."""
    if is_open(linked): return dict(deck=linked, skipped="open in PowerPoint; close it and run again")
    infos, data = read(linked); order = slide_order(data)
    if not 2 <= slide <= len(order): return dict(deck=linked, error="no slide %d" % slide)
    W, H = slide_size(data); rid, part = order[slide - 1]; body = data[part].decode("utf-8")
    rels = data.get(rels_name(part), b"").decode("utf-8")
    if body.count("<p:pic>") != 1 or 'Id="rIdLk1"' not in rels: return dict(deck=linked, error="slide %d is not a picture slide made by picslide" % slide)
    def pagenum(xml, old, new):
        def fix(m):
            sp = m.group(0); g = re.search(r'<a:off x="-?\d+" y="(\d+)"', sp)
            if g and int(g.group(1)) > H * 0.9 and re.sub(r"<[^>]+>", "", re.search(r"(?s)<p:txBody>.*</p:txBody>", sp).group(0) if "<p:txBody>" in sp else "").strip() == str(old):
                return sp.replace("<a:t>%d</a:t>" % old, "<a:t>%d</a:t>" % new, 1)
            return sp
        return re.sub(r"(?s)<p:sp>.*?</p:sp>", fix, xml)
    pres = data["ppt/presentation.xml"].decode("utf-8")
    data["ppt/presentation.xml"] = re.sub(r'<p:sldId [^>]*r:id="%s"/>' % re.escape(rid), "", pres, count=1).encode("utf-8")
    prels = data["ppt/_rels/presentation.xml.rels"].decode("utf-8")
    data["ppt/_rels/presentation.xml.rels"] = re.sub(r'<Relationship [^>]*Id="%s"[^>]*/>' % re.escape(rid), "", prels, count=1).encode("utf-8")
    ct = data["[Content_Types].xml"].decode("utf-8")
    data["[Content_Types].xml"] = re.sub(r'<Override PartName="/%s"[^>]*/>' % re.escape(part), "", ct, count=1).encode("utf-8")
    data.pop(part, None); data.pop(rels_name(part), None)
    for k, (_, p) in enumerate(order[slide:], start=slide + 1):
        data[p] = pagenum(data[p].decode("utf-8"), k, k - 1).encode("utf-8")
    app = data.get("docProps/app.xml")
    if app: data["docProps/app.xml"] = re.sub(r"<Slides>\d+</Slides>", "<Slides>%d</Slides>" % (len(order) - 1), app.decode("utf-8")).encode("utf-8")
    refresh_reference(data, linked)
    arch = os.path.join(os.path.dirname(os.path.abspath(linked)), "Archive"); os.makedirs(arch, exist_ok=True)
    keepf = os.path.join(arch, "%s (before removing slide %d %s).pptx" % (os.path.splitext(os.path.basename(linked))[0], slide, datetime.datetime.now().strftime("%Y-%m-%d %H%M")))
    if not os.path.exists(keepf): shutil.copy2(linked, keepf)
    write(linked, infos, data)
    return dict(deck=linked, removed_slide=slide, embed=embed(linked) if build else None)

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
    """The real file a link shows: a mirror clone resolves to its own file."""
    if target.startswith("file://"): return real_path(urllib.parse.unquote(urllib.parse.urlparse(target).path))
    return os.path.join(os.path.dirname(os.path.abspath(deck)), urllib.parse.unquote(target))

def embed(linked, out=None):
    """<Base>-Embedded.pptx from <Base>-Linked.pptx: each linked picture put inside (any old reference slide left out)."""
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
    nothing external in Embedded, the same slides and notes, no reference slides, a README beside it."""
    emb = linked.replace("-Linked.pptx", "-Embedded.pptx"); base = base_of(linked); problems = []
    if not os.path.exists(emb): return dict(linked=linked, problems=["no Embedded deck"])
    _, L = read(linked); _, E = read(emb)
    lo = [sx for _, sx in slide_order(L) if REF_MARK not in L[sx].decode("utf-8", "ignore")]; eo = [sx for _, sx in slide_order(E)]
    refs = len(slide_order(L)) - len(lo)
    if refs: problems.append("%d reference slide(s) inside the Linked deck: they belong in %s (run strip)" % (refs, os.path.basename(note_path(linked))))
    if not os.path.exists(note_path(linked)): problems.append("no %s beside the deck (run strip)" % os.path.basename(note_path(linked)))
    if len(lo) != len(eo): problems.append("slide counts differ: Linked %d, Embedded %d" % (len(lo), len(eo)))
    strip = lambda x: re.sub(r'\s*r:(embed|link)="[^"]+"', "", x)
    for a, b in zip(lo, eo):
        if strip(L[a].decode("utf-8")) != strip(E[b].decode("utf-8")): problems.append("%s differs from its Embedded slide beyond picture storage" % posixpath.basename(a))
        na, nb = rels_name(a), rels_name(b)
        la = re.findall(r'relationships/notesSlide" Target="([^"]+)"', L.get(na, b"").decode()); lb = re.findall(r'relationships/notesSlide" Target="([^"]+)"', E.get(nb, b"").decode())
        if la and lb and L[posixpath.normpath(posixpath.join("ppt/slides", la[0]))] != E[posixpath.normpath(posixpath.join("ppt/slides", lb[0]))]: problems.append("notes differ on " + posixpath.basename(a))
    links = github = 0
    for n, b in L.items():
        if not n.startswith("ppt/slides/_rels/"): continue
        for r in re.findall(r"<Relationship [^>]*/>", b.decode("utf-8", "ignore")):
            if 'relationships/image"' not in r or 'TargetMode="External"' not in r: continue
            t = re.search(r'Target="([^"]+)"', r).group(1); links += 1
            real = link_target_path(linked, t)
            clone = urllib.parse.unquote(urllib.parse.urlparse(t).path) if t.startswith("file://") else ""
            if not clone.startswith(MIRROR + "/"): problems.append("not through the PowerPoint mirror (red X in PowerPoint; run mirror): " + t)
            elif not os.path.exists(real): problems.append("missing picture: " + real)
            elif not os.path.exists(clone) or os.path.getsize(clone) != os.path.getsize(real): problems.append("mirror out of date (run mirror): " + os.path.basename(real))
            elif not is_github(real) and not os.path.basename(real).startswith(base + "-"): problems.append("picture name does not start with %s-: %s" % (base, os.path.basename(real)))
            if is_github(real): github += 1
    for n, b in E.items():
        if n.endswith(".rels") and re.search(r'relationships/image" Target="[^"]+" TargetMode="External"', b.decode("utf-8", "ignore")):
            problems.append("Embedded deck still links a picture: " + n)
    st = pair_state(linked)
    if st["state"] != "current": problems.append("Embedded deck out of date: " + st["state"])
    return dict(linked=linked, embedded=emb, linked_pictures=links, canvas_pictures=github, reference_slides=refs, slides=len(lo), problems=problems)

# ---------------------------------------------------------------- mirror and place (2026-10-02)

SOURCES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "slide_picture_sources.json")

def mirror_deck(linked, dry=False, sources=None):
    """Every picture link into the PowerPoint mirror. A picture in Images that is a copy of a Canvas picture (Build-Tools/
    slide_picture_sources.py, a sure match only) is linked to the Canvas picture in GitHub instead, so the link itself
    says the slide still needs a unique picture. Slides, text and the deck's date stay as they are."""
    if is_open(linked): return dict(linked=linked, skipped="open in PowerPoint; close it and run again")
    sources = sources if sources is not None else (json.load(open(SOURCES)) if os.path.exists(SOURCES) else {})
    infos, data = read(linked); changed = to_github = 0; freed = []; missing = []
    for n in list(data):
        if not re.match(r"ppt/slides/_rels/slide\d+\.xml\.rels$", n): continue
        rels = data[n].decode("utf-8"); new = rels
        for r in re.findall(r"<Relationship [^>]*/>", rels):
            if 'relationships/image"' not in r or 'TargetMode="External"' not in r: continue
            t = re.search(r'Target="([^"]+)"', r).group(1); real = link_target_path(linked, t)
            canvas = (sources.get(real) or {}).get("canvas") or ""
            if canvas and os.path.exists(canvas) and not is_github(real): freed.append(real); real = canvas; to_github += 1
            if not os.path.exists(real): missing.append(os.path.basename(real)); continue
            tgt = "file://" + urllib.parse.quote(mirror_path(real)) if dry else mirror_link(real)
            if tgt != t: new = new.replace(r, r.replace('Target="%s"' % t, 'Target="%s"' % tgt)); changed += 1
        data[n] = new.encode("utf-8")
    if changed and not dry:
        refresh_reference(data, linked)
        st = os.stat(linked); write(linked, infos, data); os.utime(linked, (st.st_atime, st.st_mtime))   # same slides: same date
    return dict(linked=linked, relinked=changed, to_github=to_github, freed=sorted(set(freed)), missing=missing)

def sync_mirror():
    """Refreshes every clone whose file changed (a picture fixed in GitHub, a new one saved over in Images), so the
    Linked decks show it in PowerPoint at once. Fast: no deck is opened."""
    fresh = 0
    for d, _, fs in os.walk(MIRROR):
        for f in fs:
            if f.endswith(".part"): continue
            m = os.path.join(d, f); real = real_path(m)
            if not os.path.exists(real): continue
            st = os.stat(real)
            if os.path.getsize(m) != st.st_size or abs(os.path.getmtime(m) - st.st_mtime) > 1: mirror_sync(real); fresh += 1
    return dict(refreshed=fresh)

# Real things are never generated (Standards 20.1 rule 3): software screens, named products and gear, real people and
# photos of real parts keep the Canvas picture. The briefs' Keep tables are Adam's own list (2026-09-26).
REAL = re.compile(r"\b(screen ?shots?|screens?|window|windows|menu|menus|dialog|tab|toolbar|inspector|preferences|settings|"
                  r"session|plug-?ins?|interface|ui|app|software|portrait|photo of|tesla|edison|faraday|ohm\b|volta\b|"
                  r"pro ?tools|logic|ableton|reaper|cubase|nuendo|studio one|dolby|avid|waves|fabfilter|izotope|universal audio|uad|"
                  r"neve|ssl|api|akg|neumann|shure|sennheiser|yamaha|behringer|focusrite|apogee|audient|rme|genelec|adam audio|krk|"
                  r"auratone|logitech|maag|wwise|fmod|unity|unreal|macos|mac os|disk utility|finder|apple|iphone|ipad|dante|soundgrid|"
                  r"midi ?controller|keyboard controller|2n2222a?|lm741|ne5532|tl07\d|model|logos?|renderer|panner|grids?|"
                  r"indicators?|meter bank|layout map|room view|hand-?built|supercaps?|buttons?|playlists?|lanes|zoom h\d|marked)\b", re.I)

def keep_tables():
    """Canvas pictures the briefs' Keep tables say stay on their slides: {(course folder, picture name)}"""
    out = set()
    for bf in glob.glob(os.path.join(GITHUB_CLASSES, "*", "_briefs", "ChatGPT Image Creation - DAPR * Presentations.md")):
        course = os.path.basename(os.path.dirname(os.path.dirname(bf))); txt = open(bf, encoding="utf-8").read()
        for sec in re.findall(r"(?ms)^#+ Keep.*?(?=^# (?!Keep)|\Z)", txt):
            for name in re.findall(r"Canvas pictures? `([^`]+)`", sec) + re.findall(r"\| `([^`]+\.(?:png|jpe?g|gif))`", sec, re.I): out.add((course, name))
    return out

def keep_reason(real, alt, title, kept):
    course = os.path.relpath(real, GITHUB_CLASSES).split(os.sep)[0]
    if (course, os.path.basename(real)) in kept: return "Keep table in the brief (Adam, 2026-09-26)"
    words = " ".join([alt, title, os.path.splitext(os.path.basename(real))[0]]).replace("_", " ")
    split = re.sub(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])", " ", words)   # NeumannKU100 -> Neumann KU 100
    m = REAL.search(words) or REAL.search(split)          # both: iZotope and 2N2222A stay whole
    return "real %s (20.1 rule 3)" % m.group(0).lower() if m else ""

def unique(target):
    """Every slide picture that is still the Canvas picture (its link goes into GitHub): what ChatGPT makes next so the
    deck is its own. The new file reuses the name the deck's copy had (now in Images/Archive), else a name from the alt
    text; the size keeps the Canvas picture's shape, because `place` only swaps the link and the frame stays."""
    srcs = json.load(open(SOURCES)) if os.path.exists(SOURCES) else {}
    kept = keep_tables()
    by_canvas = {}
    for copy, v in srcs.items():
        if v.get("canvas"): by_canvas.setdefault(v["canvas"], []).append(copy)
    out = []
    for d in decks(target, r"-Linked\.pptx$"):
        base = base_of(d); images = os.path.join(os.path.dirname(d), "Images")
        z = zipfile.ZipFile(d); names = set(z.namelist())
        order = [sx for _, sx in slide_order({n: z.read(n) for n in ("ppt/presentation.xml", "ppt/_rels/presentation.xml.rels")})]
        for k, sx in enumerate(order, 1):
            rn = rels_name(sx)
            if rn not in names or sx not in names: continue
            rels = z.read(rn).decode("utf-8", "ignore"); body = z.read(sx).decode("utf-8", "ignore")
            if REF_MARK in body: continue
            for r in re.findall(r"<Relationship [^>]*/>", rels):
                if 'relationships/image"' not in r or 'TargetMode="External"' not in r: continue
                lid = re.search(r'Id="([^"]+)"', r).group(1); real = link_target_path(d, re.search(r'Target="([^"]+)"', r).group(1))
                if not is_github(real): continue
                pic = re.search(r'<p:pic>(?:(?!</p:pic>).)*?r:link="%s"' % re.escape(lid), body, re.S)
                alt = html.unescape(re.search(r'descr="([^"]*)"', pic.group(0)).group(1)) if pic and re.search(r'descr="([^"]*)"', pic.group(0)) else ""
                old = [c for c in by_canvas.get(real, []) if os.path.basename(c).startswith(base + "-")]
                name = os.path.basename(old[0]) if old else "%s-%s%s" % (base, subject_candidates(alt, title_of(body), None)[0] if alt or title_of(body) else "Picture_%d" % k, os.path.splitext(real)[1])
                keep = keep_reason(real, alt, title_of(body), kept)
                w, h = (1600, 900) if keep else (image_size(real) or (1600, 900))    # only ChatGPT's work needs the shape
                W = 1920 if name.lower().endswith((".jpg", ".jpeg")) else 1600; H = int(round(W * h / float(w))) if w else 900
                out.append(dict(deck=d, base=base, slide=k, title=title_of(body), alt=alt, github=real, new=os.path.join(images, name),
                                width=W, height=H, made=os.path.exists(os.path.join(images, name)), keep=keep))
    return out

def archive_freed(results):
    """Copies in Images that no deck links any more go to Images/Archive (kept, never deleted)."""
    linked_now = set()
    for d in decks(LINKS_ROOT, r"-Linked\.pptx$"):
        z = zipfile.ZipFile(d)
        for n in z.namelist():
            if n.startswith("ppt/slides/_rels/"):
                for t in re.findall(r'Target="([^"]+)" TargetMode="External"', z.read(n).decode("utf-8", "ignore")): linked_now.add(link_target_path(d, t))
    moved = []
    for r in results:
        for f in r.get("freed", []):
            if f in linked_now or not os.path.exists(f): continue
            arch = os.path.join(os.path.dirname(f), "Archive"); os.makedirs(arch, exist_ok=True)
            shutil.move(f, os.path.join(arch, os.path.basename(f))); moved.append(f)
    return moved

def place(linked, slide, new, old=None):
    """Points one picture on a slide at a new file (in Images): the link whose file is `old`, else the slide's only link,
    else its one link into GitHub. The old file is never written over; the Embedded deck is built again."""
    if is_open(linked): return dict(linked=linked, skipped="open in PowerPoint; close it and run again")
    infos, data = read(linked)
    order = [sx for _, sx in slide_order(data)]
    if not (1 <= slide <= len(order)): return dict(error="no slide %d" % slide)
    rn = rels_name(order[slide - 1]); rels = data.get(rn, b"").decode("utf-8")
    links = [(r, re.search(r'Target="([^"]+)"', r).group(1)) for r in re.findall(r"<Relationship [^>]*/>", rels)
             if 'relationships/image"' in r and 'TargetMode="External"' in r]
    pick = [x for x in links if old and os.path.abspath(link_target_path(linked, x[1])) == os.path.abspath(old)] or \
           (links if len(links) == 1 else [x for x in links if is_github(link_target_path(linked, x[1]))])
    if len(pick) != 1: return dict(error="slide %d has %d pictures that could be the one; name it with --old" % (slide, len(links)))
    r, t = pick[0]; was = link_target_path(linked, t)
    # A brief's picture keeps its brief name (the Images to Fix list finds it there); the deck links a copy named
    # Images/<Base>-<name>, as every deck picture is named (2026-10-03: 79 approved slide pictures had brief names only)
    base = base_of(linked); images = os.path.join(os.path.dirname(os.path.abspath(linked)), "Images")
    if not os.path.basename(new).startswith(base + "-"):
        named = os.path.join(images, base + "-" + os.path.basename(new))
        if os.path.exists(named) and sha(open(named, "rb").read()) != sha(open(new, "rb").read()):
            return dict(error="%s already holds a different picture" % named)
        if not os.path.exists(named): os.makedirs(images, exist_ok=True); shutil.copy2(new, named)
        new = named
    data[rn] = rels.replace(r, r.replace('Target="%s"' % t, 'Target="%s"' % mirror_link(new))).encode("utf-8")
    refresh_reference(data, linked); write(linked, infos, data)
    return dict(linked=linked, slide=slide, was=was, now=os.path.abspath(new), embed=embed(linked))

def decks(target, pattern):
    if target.lower().endswith(".pptx"): return [target]
    out = []
    for root, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        if os.path.basename(root) == "Presentations": out += [os.path.join(root, f) for f in files if re.search(pattern, f) and not f.startswith("~$")]
    return sorted(out)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["sync"]: print(json.dumps([sync_mirror()])); sys.exit(0)
    if a[:1] == ["unique"]: print(json.dumps(unique(a[1] if len(a) > 1 else LINKS_ROOT), indent=1)); sys.exit(0)
    if len(a) < 2 or a[0] not in ("split", "embed", "status", "verify", "clean", "uncopy", "strip", "addpics", "mirror", "place", "picslide", "unpic", "unpicslide"): print(__doc__); sys.exit(2)
    t = a[1]
    if a[0] == "split": res = [split(d, "--dry" in a) for d in decks(t, r"(?<!-Linked)(?<!-Embedded)\.pptx$")]
    elif a[0] == "embed": res = [embed(d) for d in decks(t, r"-Linked\.pptx$")]
    elif a[0] == "uncopy": res = [uncopy(d) for d in decks(t, r"-Linked\.pptx$")]
    elif a[0] == "strip": res = [strip(d) for d in decks(t, r"-Linked\.pptx$")]
    elif a[0] == "unpic":          # unpic <Linked.pptx> <slide> <Subject>
        res = [remove_picture(a[1], int(a[2]), a[3])]
    elif a[0] == "unpicslide":     # unpicslide <Linked.pptx> <slide>
        res = [remove_picture_slide(a[1], int(a[2]))]
    elif a[0] == "picslide":       # picslide <Linked.pptx> <after slide> <spec.json {"src","subject","alt"}>
        res = [picture_slide(a[1], int(a[2]), json.load(open(a[3], encoding="utf-8")))]
    elif a[0] == "addpics":
        spec = json.load(open(a[2], encoding="utf-8")); specs = spec if isinstance(spec, list) else [spec]
        # several slides in one go: one copy to Archive first, one Embedded build at the end
        res = []
        for i, sp in enumerate(specs):
            r = add_pictures(t, sp, archive=(i == 0), build=(i == len(specs) - 1)); res.append(r)
            if r.get("error") or r.get("skipped"): break
    elif a[0] == "clean":
        res = []
        for d in decks(t, r"-Linked\.pptx$"):
            infos, data = read(d); drop_unused_media(data); write(d, infos, data); res.append(dict(cleaned=d, embed=embed(d)))
    elif a[0] == "mirror":
        srcs = json.load(open(SOURCES)) if os.path.exists(SOURCES) else {}
        res = [mirror_deck(d, "--dry" in a, srcs) for d in decks(t, r"-Linked\.pptx$")]
        if "--dry" not in a: res.append(dict(archived=archive_freed(res)))
    elif a[0] == "place":
        res = [place(t, int(a[2]), a[3], a[a.index("--old") + 1] if "--old" in a else None)]
    elif a[0] == "status": res = [pair_state(d) for d in decks(t, r"-Linked\.pptx$")]
    else: res = [verify(d) for d in decks(t, r"-Linked\.pptx$")]
    print(json.dumps(res, indent=1))
