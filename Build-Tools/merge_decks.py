#!/usr/bin/env python3
"""
merge_decks.py: fold an older deck's slides into a newer deck of the same lecture, in the newer deck's look (Adam, 2026-09-30).

"Merge them all now so we have the max amount of information and content." A plan says where each older slide goes:
    {"order": [["N",1],["N",2],["O",7],["N",3], ...], "dropped_old": [{"slide": 1, "why": "..."}]}
Every newer slide once, in its order; every older slide either placed or dropped with a reason (checked before writing).

The merged deck is the newer deck plus the placed older slides (with their pictures and speaker notes). Each placed older
slide takes the newer deck's footer ("DAPR 2255  |  Power" and the page number), its title position and size, and a Title
Case title; every page number is renumbered in the merged order. Written beside the newer deck as <out>; nothing is
overwritten.

    python3 merge_decks.py <newer.pptx> <older.pptx> <plan.json> <out.pptx>
"""
import sys, os, re, json, zipfile, posixpath, html, io

# American spellings only (Standards 8.0.1); the older decks used some British ones
AMERICAN = [(r"\b([Rr])ecognis(e|es|ed|ing)\b", r"\1ecogniz\2"), (r"\b([Aa])nalogue\b", r"\1nalog"), (r"\b([Mm])oulded\b", r"\1olded"),
            (r"\b([Cc])olour(s|ed|ing)?\b", r"\1olor\2"), (r"\b([Ll])abelled\b", r"\1abeled"), (r"\b([Ll])abelling\b", r"\1abeling"),
            (r"\b([Bb])ehaviour(s)?\b", r"\1ehavior\2"), (r"\b([Cc])entre(s|d)?\b", r"\1enter\2"), (r"\b([Oo])rganis(e|es|ed|ing|ation)\b", r"\1rganiz\2"),
            (r"\b([Mm])inimis(e|es|ed|ing)\b", r"\1inimiz\2"), (r"\b([Mm])aximis(e|es|ed|ing)\b", r"\1aximiz\2"), (r"\b([Ss])ynchronis(e|es|ed|ing|ation)\b", r"\1ynchroniz\2"),
            (r"\b([Ii])nitialis(e|es|ed|ing|ation)\b", r"\1nitializ\2"), (r"\b([Nn])ormalis(e|es|ed|ing|ation)\b", r"\1ormaliz\2"), (r"\b([Pp])olaris(e|es|ed|ing|ation)\b", r"\1olariz\2"),
            (r"\b([Cc])alibre\b", r"\1aliber"), (r"\b([Mm])etre(s)?\b", r"\1eter\2"), (r"\b([Ff])ibre(s)?\b", r"\1iber\2"), (r"\b([Gg])rey\b", r"\1ray"),
            (r"\b([Aa])luminium\b", r"\1luminum"), (r"\b([Ll])icence\b", r"\1icense"), (r"\b([Dd])efence\b", r"\1efense"), (r"\b([Tt])ravell(ed|ing|er)\b", r"\1ravel\2"),
            (r"\b([Mm])odell(ed|ing)\b", r"\1odel\2"), (r"\b([Cc])ancell(ed|ing)\b", r"\1ancel\2"), (r"\b([Pp])rogramme(s)?\b", r"\1rogram\2")]
# words that really end in -ise, so the general -ise to -ize rule leaves them alone
ISE_OK = set("""otherwise wise advise rise raise noise precise promise exercise expertise surprise comprise compromise revise supervise
paradise concise premise enterprise franchise televise merchandise despise devise improvise arise poise guise disguise cruise praise
reprise chastise demise excise incise treatise vise mortise bruise anise clockwise counterclockwise likewise lengthwise crosswise
advertise sunrise uprise circumcise""".split())
def ize(m):
    w = m.group(0); stem, end = m.group(1), m.group(2)
    base = (stem + "ise").lower()
    if base in ISE_OK or stem.lower() + "ise" in ISE_OK: return w
    return stem + "iz" + end[2:] if end.startswith("is") else w
AMERICAN.append((r"\b(\w{3,}?)(ise|ised|ises|ising|isation|isations)\b", ize))

# no em dashes, en dashes or double hyphens (All AI Projects 1): a number range reads "to", a spaced dash a colon
AMERICAN += [(r"(\d)\s*[\u2013\u2014]\s*(\d)", r"\1 to \2"), (r"\s+[\u2013\u2014]\s+|\s+--\s+", ": "), (r"[\u2013\u2014]", "-")]

def american(xml):
    def fix(m): 
        t = m.group(1)
        for a, b in AMERICAN: t = re.sub(a, b, t)
        return "<a:t>%s</a:t>" % t
    xml = re.sub(r"<a:t>([^<]*)</a:t>", fix, xml)
    return re.sub(r'descr="([^"]*)"', lambda m: 'descr="%s"' % american_plain(m.group(1)), xml)
def american_plain(t):
    for a, b in AMERICAN: t = re.sub(a, b, t)
    return t

SMALL = {"a", "an", "the", "is", "and", "or", "to", "of", "in", "for", "on", "at", "by", "vs", "via", "per", "with", "from", "as", "but", "nor"}
REL_SLIDE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide"

def load(p):
    z = zipfile.ZipFile(p); d = {i.filename: z.read(i.filename) for i in z.infolist() if not i.filename.endswith("/")}; return d

def order_of(d):
    pres = d["ppt/presentation.xml"].decode(); rels = d["ppt/_rels/presentation.xml.rels"].decode()
    tgt = {}
    for r in re.findall(r"<Relationship [^>]*/>", rels):
        i = re.search(r'Id="([^"]+)"', r).group(1); t = re.search(r'Target="([^"]+)"', r).group(1)
        if "/slide\"" in r or 'relationships/slide"' in r: tgt[i] = posixpath.normpath(posixpath.join("ppt", t))
    return [tgt[r] for r in re.findall(r'<p:sldId [^>]*r:id="([^"]+)"', pres) if r in tgt]

def rels_name(part): return posixpath.join(posixpath.dirname(part), "_rels", posixpath.basename(part) + ".rels")

def title_case(t):
    out = []; first = True
    for tok in re.split(r"(\s+)", t):
        if not tok.strip(): out.append(tok); continue
        core = re.sub(r"^[^\w]+|[^\w]+$", "", tok)
        if core and not first and core.lower() in SMALL and core == core.lower(): out.append(tok)
        elif core and (any(c.isupper() for c in core[1:]) or core[0].isdigit() or core[0].isupper()): out.append(tok)
        else:
            i = next((k for k, c in enumerate(tok) if c.isalpha()), None)
            out.append(tok if i is None else tok[:i] + tok[i].upper() + tok[i + 1:])
        first = tok.endswith(":")
    return "".join(out)

def shapes(xml): return list(re.finditer(r"(?s)<p:sp>.*?</p:sp>", xml))
def geom(sp):
    m = re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"/><a:ext cx="(\d+)" cy="(\d+)"', sp)
    return tuple(int(x) for x in m.groups()) if m else None
def text(sp): return "".join(html.unescape(x) for x in re.findall(r"<a:t>([^<]*)</a:t>", sp))

def newer_footer(d, order):
    """The two footer shapes of a newer content slide: ("DAPR 2255  |  Power", "5")"""
    for part in order:
        xml = d[part].decode("utf-8")
        low = [m.group(0) for m in shapes(xml) if geom(m.group(0)) and geom(m.group(0))[1] > 6000000]
        num = [s for s in low if text(s).strip().isdigit()]; lab = [s for s in low if "|" in text(s)]
        if num and lab: return lab[0], num[0]
    return None, None

def newer_title_geom(d, order):
    for part in order[1:]:
        xml = d[part].decode("utf-8")
        for m in shapes(xml):
            g = geom(m.group(0)); sz = re.search(r'sz="(\d+)"', m.group(0))
            if g and g[1] < 700000 and sz and int(sz.group(1)) >= 2800:
                c = re.search(r'<a:srgbClr val="(\w+)"', m.group(0))
                return g, sz.group(1), (c.group(1) if c else None)
    return None, None, None

def is_old_divider(xml):
    """An older section divider: a numbered circle, a title and a line under it"""
    return 'prst="ellipse"' in xml and any(text(m.group(0)).strip().isdigit() for m in shapes(xml)) and len([m for m in shapes(xml) if text(m.group(0)).strip()]) <= 4

def newer_divider(d, order):
    for part in order:
        xml = d[part].decode("utf-8")
        if any(re.fullmatch(r"PART \d+", text(m.group(0)).strip()) for m in shapes(xml)): return xml
    return None

def set_text(sp, new):
    """Puts new text in a shape's first run and empties the rest"""
    runs = list(re.finditer(r"<a:t>[^<]*</a:t>", sp))
    if not runs: return sp
    out = sp[:runs[0].start()] + "<a:t>%s</a:t>" % html.escape(new, quote=False)
    last = runs[0].end()
    for r in runs[1:]: out += sp[last:r.start()] + "<a:t></a:t>"; last = r.end()
    return out + sp[last:]

def fix_text(xml, find, repl):
    """Replaces text inside one run, or across the runs of one paragraph"""
    f, r = html.escape(find, quote=False), html.escape(repl, quote=False)
    if f in xml: return xml.replace(f, r), True
    for m in re.finditer(r"(?s)<a:p>.*?</a:p>", xml):
        para = m.group(0); whole = "".join(re.findall(r"<a:t>([^<]*)</a:t>", para))
        if f in whole:
            return xml.replace(para, set_text(para, html.unescape(whole.replace(f, r)))), True
    return xml, False

# ---- restyle: an older slide in another design rebuilt in the newer deck's look (Adam, 2026-09-30: 2010 decks)

def content_template(d, order):
    """A newer content slide with a title, a bullet body and the footer: its background, title, body and footer shapes"""
    for part in order[1:]:
        xml = d[part].decode("utf-8"); sps = [m.group(0) for m in shapes(xml)]
        title = [sp for sp in sps if geom(sp) and geom(sp)[1] < 700000 and re.search(r'sz="(\d+)"', sp) and int(re.search(r'sz="(\d+)"', sp).group(1)) >= 2800]
        body = [sp for sp in sps if "buChar" in sp and geom(sp) and geom(sp)[1] > 1000000]
        foot = [sp for sp in sps if geom(sp) and geom(sp)[1] > 6000000]
        if title and body and foot:
            bg = re.search(r"(?s)<p:bg>.*?</p:bg>", xml)
            para = re.search(r"(?s)<a:p>(?:(?!</a:p>).)*buChar.*?</a:p>", body[0]).group(0)
            return dict(bg=bg.group(0) if bg else "", title=title[0], body=body[0], para=para, foot=foot)
    return None

def old_parts(xml):
    """An older slide's title, paragraphs (with their levels) and pictures, in reading order"""
    title = ""; paras = []; pics = []
    items = []
    for m in re.finditer(r"(?s)<p:sp>.*?</p:sp>|<p:pic>.*?</p:pic>", xml):
        el = m.group(0); g = geom(el) or (0, 0, 0, 0)
        items.append((g[1], g[0], el))
    items.sort(key=lambda x: (x[0] // 300000, x[1]))
    for y, x, el in items:
        if el.startswith("<p:pic>"):
            if "r:embed" in el: pics.append(el)
            continue
        if re.search(r'<p:ph [^>]*type="(sldNum|ftr|dt)"', el): continue
        is_title = re.search(r'<p:ph [^>]*type="(title|ctrTitle)"', el)
        for pm in re.finditer(r"(?s)<a:p>.*?</a:p>|<a:p/>", el):
            t = "".join(html.unescape(t) for t in re.findall(r"<a:t>([^<]*)</a:t>", pm.group(0))).strip()
            if not t: continue
            if is_title and not title: title = t; continue
            lvl = re.search(r'<a:pPr [^>]*lvl="(\d)"', pm.group(0))
            if any(t == q for _, q in paras): continue          # a line the slide repeats is kept once
            paras.append((int(lvl.group(1)) if lvl else 0, t))
    if not title and paras and len(paras[0][1]) <= 70:
        title = paras.pop(0)[1]
    return title, paras, pics

def restyle(xml, tpl, title_override=None):
    title, paras, pics = old_parts(xml)
    if title_override: title = title_override
    ids = iter(range(10, 999))
    def newid(sp): return re.sub(r'<p:cNvPr id="\d+"', '<p:cNvPr id="%d"' % next(ids), sp, count=1)
    t = tpl["title"]; runs = list(re.finditer(r"<a:t>[^<]*</a:t>", t))
    t = t[:runs[0].start()] + "<a:t>%s</a:t>" % html.escape(title_case(title), quote=False) + "".join("" for _ in runs[1:]) + t[runs[0].end():]
    t = re.sub(r"(<a:t>[^<]*</a:t>.*?)<a:t>[^<]*</a:t>", r"\1", t, flags=re.S)
    x0, top, full_w, bottom = 548640, 1417320, 11094415, 6217920
    area_h = bottom - top
    text_w = full_w if not pics else (full_w if not paras else 5852160)
    body = ""
    if paras:
        b = tpl["body"]; g = geom(b)
        b = re.sub(r'<a:off x="-?\d+" y="-?\d+"/><a:ext cx="\d+" cy="\d+"', '<a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"' % (x0, top, text_w, area_h), b, count=1)
        ps = []
        size = 2000 if len(paras) <= 6 else (1800 if len(paras) <= 9 else 1600)
        for lvl, txt in paras:
            p_ = re.sub(r"<a:t>[^<]*</a:t>", "<a:t>%s</a:t>" % html.escape(txt, quote=False), tpl["para"], count=1)
            p_ = re.sub(r'sz="\d+"', 'sz="%d"' % (size - 200 * min(lvl, 2)), p_)
            if lvl: p_ = re.sub(r'marL="(\d+)"', lambda m: 'marL="%d"' % (int(m.group(1)) + 342900 * min(lvl, 2)), p_, count=1)
            ps.append(p_)
        b = re.sub(r"(?s)(<p:txBody>.*?<a:lstStyle/>).*(</p:txBody>)", lambda m: m.group(1) + "".join(ps) + m.group(2), b, count=1)
        if "<a:normAutofit" not in b: b = re.sub(r"<a:bodyPr([^>]*)/>", r"<a:bodyPr\1><a:normAutofit/></a:bodyPr>", b, count=1)
        body = newid(b)
    # pictures in the right half (or the whole area), stacked, each kept in proportion
    pic_x = x0 if not paras else x0 + text_w + 365760
    pic_w = full_w - (pic_x - x0)
    out_pics = ""
    if pics:
        # the pictures keep their arrangement (a diagram of small pictures stays a diagram), scaled as one group
        gs = [geom(el) or (0, 0, 1, 1) for el in pics]
        bx0 = min(g[0] for g in gs); by0 = min(g[1] for g in gs)
        bw = max(g[0] + g[2] for g in gs) - bx0 or 1; bh = max(g[1] + g[3] for g in gs) - by0 or 1
        k = min(pic_w / float(bw), area_h / float(bh))
        ox = pic_x + int((pic_w - bw * k) / 2); oy = top + int((area_h - bh * k) / 2) if not paras else top
        for el, g in zip(pics, gs):
            x = ox + int((g[0] - bx0) * k); y = oy + int((g[1] - by0) * k); w = int(g[2] * k); h = int(g[3] * k)
            el2 = re.sub(r'<a:off x="-?\d+" y="-?\d+"/><a:ext cx="\d+" cy="\d+"', '<a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"' % (x, y, w, h), el, count=1)
            el2 = re.sub(r'<p:nvPr>\s*<p:ph [^>]*/>\s*</p:nvPr>|<p:nvPr><p:ph [^>]*/></p:nvPr>', "<p:nvPr/>", el2)
            out_pics += newid(el2)
    foot = "".join(newid(f) for f in tpl["foot"])
    head = re.search(r"(?s)^.*?<p:cSld[^>]*>", xml).group(0)
    tail = re.search(r"(?s)</p:cSld>.*$", xml).group(0)
    tail = re.sub(r"(?s)<p:transition.*?</p:transition>|<p:timing>.*?</p:timing>|<mc:AlternateContent.*?</mc:AlternateContent>", "", tail)
    tree = ('<p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr/>%s%s%s%s</p:spTree>' % (foot, newid(t), body, out_pics))
    return head + tpl["bg"] + tree + tail

def merge(newer, older, plan, out):
    N = load(newer); O = load(older); p = json.load(open(plan))
    n_order = order_of(N); o_order = order_of(O)
    placed_n = [i for s, i in p["order"] if s == "N"]; placed_o = [i for s, i in p["order"] if s == "O"]
    dropped = [x["slide"] for x in p.get("dropped_old", [])]
    assert placed_n == list(range(1, len(n_order) + 1)), "every newer slide once, in order"
    assert sorted(placed_o + dropped) == list(range(1, len(o_order) + 1)), "every older slide placed or dropped once"
    lab_sp, num_sp = newer_footer(N, n_order); tg, tsz, tcol = newer_title_geom(N, n_order); div_tpl = newer_divider(N, n_order)
    fixes = p.get("text_fixes", []); fixed = []
    tpl = content_template(N, n_order) if p.get("restyle") else None
    n_layout = sorted(k for k in N if re.match(r"ppt/slideLayouts/slideLayout\d+\.xml$", k))[0]
    n_notesmaster = next((k for k in N if re.match(r"ppt/notesMasters/notesMaster\d+\.xml$", k)), None)
    ct = N["[Content_Types].xml"].decode(); oct_ = O["[Content_Types].xml"].decode()
    def ctype(part):
        m = re.search(r'<Override PartName="/%s" ContentType="([^"]+)"' % re.escape(part), oct_); return m.group(1) if m else None
    def nextname(pattern_dir, stem, ext):
        k = 1
        while True:
            n = "%s/%s%d%s" % (pattern_dir, stem, k, ext)
            if n not in N: return n
            k += 1
    copied = {}
    def copy_part(src):
        """Copies an older part (and what it points to) into the newer deck; returns its new name."""
        if src in copied: return copied[src]
        d, b = posixpath.dirname(src), posixpath.basename(src)
        stem, ext = os.path.splitext(b); stem = re.sub(r"\d+$", "", stem)
        if d == "ppt/media": new = "ppt/media/merged-%s" % b
        else: new = nextname(d, stem, ext)
        while new in N: new = new.replace("merged-", "merged-x")
        copied[src] = new; N[new] = O[src]
        c = ctype(src)
        nonlocal ct
        if c: ct = ct.replace("</Types>", '<Override PartName="/%s" ContentType="%s"/></Types>' % (new, c))
        e = os.path.splitext(new)[1].lstrip(".").lower()
        if e and 'Extension="%s"' % e not in ct:
            m = re.search(r'<Default Extension="%s" ContentType="([^"]+)"/>' % re.escape(e), oct_, re.I)
            if m: ct = ct.replace("</Types>", '<Default Extension="%s" ContentType="%s"/></Types>' % (e, m.group(1)))
        rn = rels_name(src)
        if rn in O:
            rels = O[rn].decode()
            def fix(m):
                r = m.group(0)
                if 'TargetMode="External"' in r: return r
                t = re.search(r'Target="([^"]+)"', r).group(1); full = posixpath.normpath(posixpath.join(d, t))
                if "/slideLayout" in r: dest = n_layout
                elif "/notesMaster" in r: dest = n_notesmaster
                elif re.search(r'relationships/slide"', r): dest = None
                else: dest = copy_part(full)
                if dest is None: return r      # notes back link: fixed after the slide's name is known
                return r.replace('Target="%s"' % t, 'Target="%s"' % posixpath.relpath(dest, posixpath.dirname(new)))
            N[rels_name(new)] = re.sub(r"<Relationship [^>]*/>", fix, rels).encode()
        return new
    final = []
    for s, i in p["order"]:
        if s == "N": final.append(n_order[i - 1]); continue
        src = o_order[i - 1]; new = copy_part(src)
        xml = N[new].decode("utf-8")
        if tpl:
            # another design: the slide is rebuilt in the newer look (title, bullets, pictures, notes kept)
            N[new] = restyle(xml, tpl, (p.get("titles") or {}).get(str(i))).encode("utf-8"); final.append(new); continue
        if div_tpl and is_old_divider(xml):
            # the newer deck's divider, carrying the older divider's title and line
            words = [text(m.group(0)).strip() for m in shapes(xml) if text(m.group(0)).strip() and not text(m.group(0)).strip().isdigit()]
            tpl = div_tpl; tsh = [m.group(0) for m in shapes(tpl) if text(m.group(0)).strip() and not re.fullmatch(r"PART \d+", text(m.group(0)).strip())]
            for sp, w in zip(tsh, [title_case(words[0])] + words[1:2] if words else []): tpl = tpl.replace(sp, set_text(sp, w))
            N[new] = tpl.encode("utf-8"); final.append(new); continue
        if is_old_divider(xml):
            # no newer divider to copy: the numbered circle goes, the background takes the newer divider green
            for m in shapes(xml):
                if 'prst="ellipse"' in m.group(0) or text(m.group(0)).strip().isdigit(): xml = xml.replace(m.group(0), "")
            xml = re.sub(r'(<p:bg><p:bgPr><a:solidFill><a:srgbClr val=")\w+"', r'\g<1>275D38"', xml)
            xml = xml.replace('val="BFD3C6"', 'val="E3EEE7"')
            N[new] = xml.encode("utf-8"); final.append(new); continue
        # the newer deck's title position, size and Title Case
        for m in shapes(xml):
            g = geom(m.group(0)); sz = re.search(r'sz="(\d+)"', m.group(0))
            if g and g[1] < 800000 and sz and int(sz.group(1)) >= 2800 and tg:
                sp = m.group(0)
                sp2 = re.sub(r'<a:off x="-?\d+" y="-?\d+"/><a:ext cx="\d+" cy="\d+"', '<a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"' % tg, sp, count=1)
                sp2 = re.sub(r'sz="%s"' % sz.group(1), 'sz="%s"' % tsz, sp2)
                if tcol: sp2 = re.sub(r'(<a:rPr[^>]*>\s*<a:solidFill>\s*<a:srgbClr val=")\w+"', r'\g<1>%s"' % tcol, sp2)
                sp2 = re.sub(r"<a:t>([^<]*)</a:t>", lambda t: "<a:t>%s</a:t>" % html.escape(title_case(html.unescape(t.group(1))), quote=False), sp2)
                xml = xml.replace(sp, sp2); break
        # the newer footer in place of the older one ("Power  |  8")
        for m in shapes(xml):
            g = geom(m.group(0))
            if g and g[1] > 6000000 and re.search(r"\|\s*\d+\s*$", text(m.group(0))) and lab_sp:
                ids = [int(x) for x in re.findall(r'<p:cNvPr id="(\d+)"', xml)]
                a = re.sub(r'<p:cNvPr id="\d+"', '<p:cNvPr id="%d"' % (max(ids) + 1), lab_sp, count=1)
                b = re.sub(r'<p:cNvPr id="\d+"', '<p:cNvPr id="%d"' % (max(ids) + 2), num_sp, count=1)
                xml = xml.replace(m.group(0), a + b); break
        N[new] = xml.encode("utf-8")
        final.append(new)
    # notes back links for every copied notes slide
    back = {v: k for k, v in copied.items()}
    for new in final:
        rn = rels_name(new)
        if rn not in N: continue
        m = re.search(r'Target="\.\./notesSlides/([^"]+)"', N[rn].decode())
        if m:
            nr = rels_name("ppt/notesSlides/" + m.group(1))
            if nr in N: N[nr] = re.sub(r'(relationships/slide" Target=")[^"]+"', r'\g<1>../slides/%s"' % posixpath.basename(new), N[nr].decode()).encode()
    # American spellings on every slide and its notes
    for part in final:
        N[part] = american(N[part].decode("utf-8")).encode("utf-8")
        rn = rels_name(part)
        if rn in N:
            m = re.search(r'Target="\.\./notesSlides/([^"]+)"', N[rn].decode())
            if m: N["ppt/notesSlides/" + m.group(1)] = american(N["ppt/notesSlides/" + m.group(1)].decode("utf-8")).encode("utf-8")
    # PART labels count up in the merged order
    k = 0
    for part in final:
        xml = N[part].decode("utf-8")
        for m in shapes(xml):
            if re.fullmatch(r"PART \d+", text(m.group(0)).strip()):
                k += 1; xml = xml.replace(m.group(0), re.sub(r"<a:t>PART \d+</a:t>", "<a:t>PART %d</a:t>" % k, m.group(0)))
        N[part] = xml.encode("utf-8")
    # text fixes from the plan: {"old"|"new": n, "find": "...", "replace": "..."} on the slide and its notes
    where = {("N", i): n_order[i - 1] for i in range(1, len(n_order) + 1)}
    where.update({("O", i): copied.get(o_order[i - 1]) for i in placed_o})
    for f in fixes:
        # "old": "*" means any placed older slide; "row_contains" limits the fix to one table row
        if f.get("old") == "*": targets = [where[("O", i)] for i in placed_o]
        else: targets = [where.get(("O", f["old"]) if "old" in f else ("N", f["new"]))]
        targets = [t for t in targets if t]
        if not targets: fixed.append(dict(f, done=False, why="slide not in the merged deck")); continue
        done = False
        for part in targets:
            parts = [part]; rn = rels_name(part)
            if rn in N:
                m = re.search(r'Target="\.\./notesSlides/([^"]+)"', N[rn].decode())
                if m: parts.append("ppt/notesSlides/" + m.group(1))
            if f.get("append_notes") and len(parts) > 1:
                nx = N[parts[1]].decode("utf-8")
                body = [m for m in shapes(nx) if 'type="body"' in m.group(0)]
                if body:
                    sp = body[0].group(0); runs = list(re.finditer(r"<a:t>([^<]*)</a:t>", sp))
                    if runs:
                        r = runs[-1]; sp2 = sp[:r.start()] + "<a:t>%s %s</a:t>" % (r.group(1), html.escape(f["append_notes"], quote=False)) + sp[r.end():]
                        N[parts[1]] = nx.replace(sp, sp2).encode("utf-8"); done = True
                continue
            for pt in parts:
                xml = N[pt].decode("utf-8")
                if f.get("row_contains"):
                    for row in re.findall(r"(?s)<a:tr .*?</a:tr>|<a:tr>.*?</a:tr>", xml):
                        if ">%s<" % html.escape(f["row_contains"]) in row:
                            r2, ok = fix_text(row, f["find"], f["replace"])
                            if ok: xml = xml.replace(row, r2); done = True; break
                    N[pt] = xml.encode("utf-8"); continue
                x, ok = fix_text(xml, f["find"], f["replace"])
                if ok: N[pt] = x.encode("utf-8"); done = True
        fixed.append(dict(f, done=done))
    # renumber page numbers in the footer's number box
    for pos, part in enumerate(final, 1):
        xml = N[part].decode("utf-8")
        for m in shapes(xml):
            g = geom(m.group(0))
            if g and g[1] > 6000000 and text(m.group(0)).strip().isdigit():
                xml = xml.replace(m.group(0), re.sub(r"<a:t>\d+</a:t>", "<a:t>%d</a:t>" % pos, m.group(0), count=1))
        N[part] = xml.encode("utf-8")
    # slide list
    prels = N["ppt/_rels/presentation.xml.rels"].decode(); pres = N["ppt/presentation.xml"].decode()
    rid_of = {}
    for r in re.findall(r"<Relationship [^>]*/>", prels):
        if 'relationships/slide"' in r:
            rid_of[posixpath.normpath(posixpath.join("ppt", re.search(r'Target="([^"]+)"', r).group(1)))] = re.search(r'Id="([^"]+)"', r).group(1)
    k = 1
    for part in final:
        if part not in rid_of:
            while "rIdM%d" % k in prels: k += 1
            rid_of[part] = "rIdM%d" % k
            prels = prels.replace("</Relationships>", '<Relationship Id="%s" Type="%s" Target="%s"/></Relationships>' % (rid_of[part], REL_SLIDE, posixpath.relpath(part, "ppt")))
    ids = iter(range(256, 256 + len(final)))
    lst = "".join('<p:sldId id="%d" r:id="%s"/>' % (next(ids), rid_of[x]) for x in final)
    pres = re.sub(r"(?s)<p:sldIdLst>.*?</p:sldIdLst>", "<p:sldIdLst>%s</p:sldIdLst>" % lst, pres)
    N["ppt/_rels/presentation.xml.rels"] = prels.encode(); N["ppt/presentation.xml"] = pres.encode(); N["[Content_Types].xml"] = ct.encode()
    # the app.xml slide count
    if "docProps/app.xml" in N:
        N["docProps/app.xml"] = re.sub(r"<Slides>\d+</Slides>", "<Slides>%d</Slides>" % len(final), N["docProps/app.xml"].decode()).encode()
    if os.path.exists(out): raise SystemExit("exists, not overwritten: " + out)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", N.pop("[Content_Types].xml"))
        for k2 in sorted(N): z.writestr(k2, N[k2])
    open(out, "wb").write(buf.getvalue())
    return dict(out=out, slides=len(final), newer=len(n_order), older_placed=len(placed_o), older_dropped=len(dropped), text_fixes=fixed)

if __name__ == "__main__":
    if len(sys.argv) != 5: print(__doc__); sys.exit(2)
    print(json.dumps(merge(*sys.argv[1:]), indent=1))
