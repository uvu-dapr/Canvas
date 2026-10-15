#!/usr/bin/env python3
"""
a11y_files.py: files a class links but Canvas does not store follow the same accessibility rules as Canvas pages
(Adam, 2026-10-15, J381: "just because they're not in Canvas they still follow Panorama rules"). Standards §2a.

What it reads (read only, unless `fixmeta` is asked for):
  PDFs      every PDF in the Cloudflare Canvas Links folder (Archive and _unused skipped): tagged (/MarkInfo /Marked
            true and a /StructTreeRoot), /Lang, a document title (/Info /Title or XMP dc:title) shown in the title bar
            (/ViewerPreferences /DisplayDocTitle true), Figure tags with /Alt or /ActualText, headings, table headers,
            a text layer (pages with fonts; none at all = a scanned, image only PDF, Panorama Severe), bookmarks
            for a PDF of 20 pages or more, encryption.
  Decks     every -Linked deck (and any single deck) beside them: slides with no title, pictures with no alt text
            (decorative pictures marked the PowerPoint way count as done), alt text that is a file name, a
            document title in docProps/core.xml.
  Pictures  every GitHub picture a class page links: the page's alt text (missing, empty, a file name, a
            placeholder word, over 120 characters), and pictures no page links at all.
  Pages     each class's current export (the fixed-name "Canvas Export (latest).imscc"), or for a class with no
            live course its newest Template package, read in place with zipfile. Links to Cloudflare files are
            matched to the files above, so the report says which flagged files students can reach.

    python3 a11y_files.py scan [--class 2000] [--out <folder>]    report per class (.md + .json) and a summary line
    python3 a11y_files.py pdf <file.pdf> [...]                      one PDF's facts, as JSON
    python3 a11y_files.py deck <deck.pptx> [...]                    one deck's facts, as JSON
    python3 a11y_files.py fixmeta <file.pdf|folder> [--dry] [--lang en-US] [--title "..."] [--like <final.pdf>]
                     metadata only: adds /Title, /Lang and DisplayDocTitle as an incremental update (PDF
                     7.5.6): the original bytes stay untouched at the front of the file, a new catalog and info
                     dictionary are appended, and the file is re-read before it replaces the old one. Tags, pages,
                     pictures and text are never changed. An untagged PDF stays untagged: export it again tagged.
    python3 a11y_files.py titles <deck.pptx> [--dry] [--out <copy.pptx>]
                     slides with no title placeholder: the heading text box becomes the title (same look: position,
                     fonts and left alignment written out) and the deckstyle bars are marked decorative. In place it
                     keeps a copy in Archive first; the Embedded deck and PDF must then be built again (deck_pair.py embed).
    python3 a11y_files.py summary [--out <folder>]                  the last scan's counts, one line per class (for the app)

Standard library only (zlib, zipfile, re); no pikepdf or pypdf on this Mac. The PDF reader follows cross-reference
tables and streams (with /Prev chains and PNG predictors) and object streams, and falls back to scanning for
"n g obj" when the cross-reference is broken.
"""
import sys, os, re, io, json, zlib, zipfile, html, glob, mmap, datetime, shutil, tempfile, posixpath, urllib.parse

CF = "/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links"
GH = "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes"
COURSES = "/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses"
OUT = os.path.expanduser("~/Library/Application Support/Canvas Preview/Linked Files Accessibility")   # where Check the App reads it
CF_HOSTS = ("pub-", "r2.dev", "files.dawhelp.com", "cloudflare")
GH_RAW = "raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/"
SKIP_DIRS = {"Archive", "_unused", "_archive", "Claude outputs", "_qa-sheets", "_briefs"}
PIC_EXT = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"}
PLACEHOLDER_ALT = {"image", "picture", "photo", "graphic", "placeholder", "untitled", "icon", "img", "screenshot", "figure"}
LONG_PDF_PAGES = 20

# ================================================================ PDF reading

WS = b" \t\r\n\f\x00"
DELIM = b"()<>[]{}/%"

class Ref:
    __slots__ = ("num", "gen")
    def __init__(self, num, gen): self.num, self.gen = num, gen
    def __eq__(self, o): return isinstance(o, Ref) and o.num == self.num and o.gen == self.gen
    def __hash__(self): return hash((self.num, self.gen))
    def __repr__(self): return "%d %d R" % (self.num, self.gen)

class Name(str):
    pass

class Str(bytes):
    """A PDF string: kept as bytes, written back as hex"""

class Num:
    """A number kept with its exact spelling, so a rewritten dictionary keeps every value byte for byte"""
    __slots__ = ("raw",)
    def __init__(self, raw): self.raw = raw
    def value(self):
        try: return int(self.raw)
        except ValueError: return float(self.raw)
    def __int__(self): return int(float(self.raw))

class Stream:
    __slots__ = ("d", "start", "length")
    def __init__(self, d, start, length): self.d, self.start, self.length = d, start, length

class Keyword(str):
    pass

class PDFError(Exception):
    pass

def _skip(b, i):
    n = len(b)
    while i < n:
        c = b[i]
        if c in WS: i += 1
        elif c == 0x25:                                  # % comment to end of line
            while i < n and b[i] not in b"\r\n": i += 1
        else: break
    return i

def _token_end(b, i):
    n = len(b)
    while i < n and b[i] not in WS and b[i] not in DELIM: i += 1
    return i

def parse(b, i, doc=None):
    """One PDF object at b[i:]: (object, index after it). A dictionary followed by `stream` becomes a Stream."""
    i = _skip(b, i)
    if i >= len(b): raise PDFError("end of data")
    c = b[i]
    if c == 0x3C and b[i + 1:i + 2] == b"<":            # << dict >>
        i += 2; d = {}
        while True:
            i = _skip(b, i)
            if b[i:i + 2] == b">>": i += 2; break
            k, i = parse(b, i, doc)
            if not isinstance(k, Name): raise PDFError("dictionary key is not a name at %d" % i)
            v, i = parse(b, i, doc)
            d[k] = v
        j = _skip(b, i)
        if b[j:j + 6] == b"stream":
            j += 6
            if b[j:j + 2] == b"\r\n": j += 2
            elif b[j:j + 1] in (b"\n", b"\r"): j += 1
            ln = d.get("Length")
            if isinstance(ln, Ref) and doc is not None:
                try: ln = doc.get(ln)
                except Exception: ln = None
            L = int(ln) if isinstance(ln, Num) else None
            if L is None or b[j + L:j + L + 20].find(b"endstream") < 0:
                e = b.find(b"endstream", j)
                if e < 0: raise PDFError("stream without endstream")
                L = e - j
                while L > 0 and b[j + L - 1] in b"\r\n": L -= 1
            k = b.find(b"endstream", j + L)
            return Stream(d, j, L), (k + 9 if k >= 0 else j + L)
        return d, i
    if c == 0x3C:                                        # <hex>
        e = b.find(b">", i)
        h = re.sub(rb"[^0-9A-Fa-f]", b"", bytes(b[i + 1:e]))
        if len(h) % 2: h += b"0"
        return Str(bytes.fromhex(h.decode())), e + 1
    if c == 0x28:                                        # (literal)
        i += 1; out = bytearray(); depth = 1; n = len(b)
        while i < n:
            ch = b[i]
            if ch == 0x5C:
                i += 1; e = b[i]
                m = {0x6E: 10, 0x72: 13, 0x74: 9, 0x62: 8, 0x66: 12, 0x28: 0x28, 0x29: 0x29, 0x5C: 0x5C}
                if e in m: out.append(m[e]); i += 1
                elif 0x30 <= e <= 0x37:
                    k = i
                    while k < i + 3 and k < n and 0x30 <= b[k] <= 0x37: k += 1
                    out.append(int(bytes(b[i:k]), 8) & 255); i = k
                elif e == 0x0D:
                    i += 2 if b[i + 1:i + 2] == b"\n" else 1
                elif e == 0x0A: i += 1
                else: out.append(e); i += 1
                continue
            if ch == 0x28: depth += 1
            elif ch == 0x29:
                depth -= 1
                if depth == 0: return Str(bytes(out)), i + 1
            out.append(ch); i += 1
        raise PDFError("unterminated string")
    if c == 0x5B:                                        # [ array ]
        i += 1; a = []
        while True:
            i = _skip(b, i)
            if b[i:i + 1] == b"]": return a, i + 1
            v, i = parse(b, i, doc); a.append(v)
    if c == 0x2F:                                        # /Name
        e = _token_end(b, i + 1)
        raw = bytes(b[i + 1:e])
        if b"#" in raw: raw = re.sub(rb"#([0-9A-Fa-f]{2})", lambda m: bytes([int(m.group(1), 16)]), raw)
        return Name(raw.decode("latin-1")), e
    e = _token_end(b, i)
    tok = bytes(b[i:e])
    if not tok: raise PDFError("unexpected byte %r at %d" % (bytes(b[i:i + 1]), i))
    if re.fullmatch(rb"[+-]?(\d+\.?\d*|\.\d+)", tok):
        if re.fullmatch(rb"\d+", tok):                    # maybe "n g R"
            m = re.match(rb"\s+(\d+)\s+R(?=[\s/<>\[\]()%]|$)", bytes(b[e:e + 24]))
            if m: return Ref(int(tok), int(m.group(1))), e + m.end()
        return Num(tok.decode()), e
    if tok == b"true": return True, e
    if tok == b"false": return False, e
    if tok == b"null": return None, e
    return Keyword(tok.decode("latin-1")), e

def _png_unpredict(data, columns):
    out = bytearray(); prev = bytearray(columns); i = 0; row = columns + 1
    while i + row <= len(data):
        f = data[i]; cur = bytearray(data[i + 1:i + row])
        for k in range(columns):
            a = cur[k - 1] if k else 0; up = prev[k]; c = prev[k - 1] if k else 0
            if f == 1: cur[k] = (cur[k] + a) & 255
            elif f == 2: cur[k] = (cur[k] + up) & 255
            elif f == 3: cur[k] = (cur[k] + ((a + up) >> 1)) & 255
            elif f == 4:
                p = a + up - c; pa, pb, pc = abs(p - a), abs(p - up), abs(p - c)
                cur[k] = (cur[k] + (a if pa <= pb and pa <= pc else up if pb <= pc else c)) & 255
        out += cur; prev = cur; i += row
    return bytes(out)

class PDF:
    def __init__(self, path):
        self.path = path
        self.f = open(path, "rb")
        try: self.b = mmap.mmap(self.f.fileno(), 0, access=mmap.ACCESS_READ)
        except ValueError: self.b = self.f.read()     # an empty file
        self.xref = {}          # num -> ("n", offset, gen) | ("c", stream num, index)
        self.trailer = {}
        self.cache = {}
        self.last_xref_is_stream = False
        self.startxref = None
        self.broken_xref = False
        self._read_xref()

    def close(self):
        try:
            if isinstance(self.b, mmap.mmap): self.b.close()
        finally: self.f.close()

    # ---------------------------------------------------------------- cross-reference
    def _read_xref(self):
        b = self.b
        k = b.rfind(b"startxref")
        try:
            if k < 0: raise PDFError("no startxref")
            m = re.match(rb"startxref\s+(\d+)", bytes(b[k:k + 40]))
            off = int(m.group(1)); self.startxref = off
            seen = set(); first = True
            while off is not None and off not in seen:
                seen.add(off)
                prev, is_stream = self._xref_section(off)
                if first: self.last_xref_is_stream = is_stream; first = False
                off = prev
            if "Root" not in self.trailer: raise PDFError("no Root in trailer")
        except Exception:
            self.broken_xref = True
            self._scan_objects()

    def _xref_section(self, off):
        b = self.b
        i = _skip(b, off)
        if b[i:i + 4] == b"xref":
            i += 4
            while True:
                i = _skip(b, i)
                if b[i:i + 7] == b"trailer": break
                m = re.match(rb"(\d+)\s+(\d+)", bytes(b[i:i + 40]))
                if not m: raise PDFError("bad xref subsection")
                start, count = int(m.group(1)), int(m.group(2)); i += m.end()
                for n in range(count):
                    i = _skip(b, i)
                    e = re.match(rb"(\d{1,10})\s+(\d{1,5})\s+([nf])", bytes(b[i:i + 24]))
                    if not e: raise PDFError("bad xref entry")
                    i += e.end()
                    num = start + n
                    if num not in self.xref and e.group(3) == b"n":
                        self.xref[num] = ("n", int(e.group(1)), int(e.group(2)))
                    elif num not in self.xref: self.xref[num] = ("f", 0, 0)
            t, _ = parse(b, i + 7, None)
            for k, v in t.items(): self.trailer.setdefault(k, v)
            if isinstance(t.get("XRefStm"), Num):
                try: self._xref_section(int(t["XRefStm"]))
                except Exception: pass
            return (int(t["Prev"]) if isinstance(t.get("Prev"), Num) else None), False
        m = re.match(rb"(\d+)\s+(\d+)\s+obj", bytes(b[i:i + 40]))
        if not m: raise PDFError("startxref points at nothing")
        s, _ = parse(b, i + m.end(), self)
        if not isinstance(s, Stream) or s.d.get("Type") != "XRef": raise PDFError("not an xref stream")
        data = self.stream_data(s)
        W = [int(x) for x in s.d["W"]]
        size = int(s.d["Size"])
        idx = [int(x) for x in s.d.get("Index", [Num("0"), Num(str(size))])]
        p = 0; rowlen = sum(W)
        for a in range(0, len(idx), 2):
            start, count = idx[a], idx[a + 1]
            for n in range(count):
                row = data[p:p + rowlen]; p += rowlen
                if len(row) < rowlen: break
                f = []; q = 0
                for w in W:
                    f.append(int.from_bytes(row[q:q + w], "big") if w else None); q += w
                typ = f[0] if W[0] else 1
                num = start + n
                if num in self.xref: continue
                if typ == 1: self.xref[num] = ("n", f[1], f[2] or 0)
                elif typ == 2: self.xref[num] = ("c", f[1], f[2])
                else: self.xref[num] = ("f", 0, 0)
        for k, v in s.d.items():
            if k not in ("Type", "W", "Index", "Length", "Filter", "DecodeParms", "Prev"): self.trailer.setdefault(k, v)
        return (int(s.d["Prev"]) if isinstance(s.d.get("Prev"), Num) else None), True

    def _scan_objects(self):
        """A broken cross-reference: find every "n g obj" in the file (later copies win, as an update would)"""
        b = bytes(self.b)
        self.xref = {}
        for m in re.finditer(rb"(?<![0-9])(\d{1,10})\s+(\d{1,5})\s+obj\b", b):
            self.xref[int(m.group(1))] = ("n", m.start(), int(m.group(2)))
        for m in re.finditer(rb"trailer\s*<<", b):
            try:
                t, _ = parse(b, m.start() + 7, None)
                self.trailer.update(t)
            except Exception: pass
        if "Root" not in self.trailer:
            for num, (_, off, gen) in list(self.xref.items()):
                try:
                    o = self.get(Ref(num, gen))
                    d = o.d if isinstance(o, Stream) else o
                    if isinstance(d, dict) and d.get("Type") == "Catalog": self.trailer["Root"] = Ref(num, gen)
                    if isinstance(d, dict) and d.get("Type") == "XRef":
                        for k in ("Info", "ID", "Encrypt"):
                            if k in d: self.trailer.setdefault(k, d[k])
                except Exception: continue

    # ---------------------------------------------------------------- objects
    def get(self, r):
        """The object a Ref points at (anything else is returned as is)"""
        if not isinstance(r, Ref): return r
        if r.num in self.cache: return self.cache[r.num]
        e = self.xref.get(r.num)
        if not e or e[0] == "f": return None
        self.cache[r.num] = None                          # a reference loop resolves to null
        if e[0] == "n":
            m = re.match(rb"\s*(\d+)\s+(\d+)\s+obj", bytes(self.b[e[1]:e[1] + 40]))
            if not m: return None
            o, _ = parse(self.b, e[1] + m.end(), self)
        else:
            o = self._from_objstm(e[1], e[2], r.num)
        self.cache[r.num] = o
        return o

    def _from_objstm(self, snum, index, num):
        s = self.get(Ref(snum, 0))
        if not isinstance(s, Stream): return None
        key = ("objstm", snum)
        if key not in self.cache:
            data = self.stream_data(s)
            n = int(s.d["N"]); first = int(s.d["First"])
            nums = re.findall(rb"(\d+)\s+(\d+)", data[:first])[:n]
            self.cache[key] = (data, first, [(int(a), int(o)) for a, o in nums])
        data, first, nums = self.cache[key]
        for a, o in nums:
            if a == num:
                v, _ = parse(data, first + o, self)
                return v
        if index < len(nums):
            v, _ = parse(data, first + nums[index][1], self)
            return v
        return None

    def stream_data(self, s, limit=None):
        raw = bytes(self.b[s.start:s.start + s.length])
        f = self.get(s.d.get("Filter"))
        filters = [f] if isinstance(f, Name) else (f or [])
        parms = self.get(s.d.get("DecodeParms"))
        parms = [parms] if isinstance(parms, dict) or parms is None else parms
        data = raw
        for k, flt in enumerate(filters):
            p = self.get(parms[k]) if k < len(parms) else None
            if flt in ("FlateDecode", "Fl"):
                try: data = zlib.decompress(data)
                except zlib.error:
                    d = zlib.decompressobj(); data = d.decompress(data)
                if isinstance(p, dict) and int(p.get("Predictor", Num("1"))) >= 10:
                    data = _png_unpredict(data, int(p.get("Columns", Num("1"))) * int(p.get("Colors", Num("1"))) * int(p.get("BitsPerComponent", Num("8"))) // 8)
            else:
                raise PDFError("filter %s not read" % flt)
        return data

    # ---------------------------------------------------------------- facts
    @property
    def catalog(self): return self.get(self.trailer.get("Root")) or {}

    @property
    def info(self):
        i = self.get(self.trailer.get("Info"))
        return i if isinstance(i, dict) else {}

    def pages(self):
        out = []; seen = set()
        def walk(node, inherited):
            node_d = self.get(node)
            if not isinstance(node_d, dict) or id(node_d) in seen or len(out) > 5000: return
            seen.add(id(node_d))
            res = node_d.get("Resources", inherited)
            if node_d.get("Type") == "Pages" or "Kids" in node_d:
                for k in self.get(node_d.get("Kids")) or []: walk(k, res)
            else: out.append((node_d, res))
        walk(self.catalog.get("Pages"), None)
        return out

def text_of(s):
    """A PDF text string as Python text (UTF-16 with a byte order mark, UTF-8 with one, else PDFDocEncoding)"""
    if not isinstance(s, (bytes, Str)): return ""
    b = bytes(s)
    if b[:2] == b"\xfe\xff": return b[2:].decode("utf-16-be", "replace")
    if b[:2] == b"\xff\xfe": return b[2:].decode("utf-16-le", "replace")
    if b[:3] == b"\xef\xbb\xbf": return b[3:].decode("utf-8", "replace")
    return b.decode("latin-1")

def pdf_facts(path):
    """Everything Panorama and PDF/UA look at in one PDF, read only"""
    r = {"file": path, "name": os.path.basename(path), "size": os.path.getsize(path)}
    try: p = PDF(path)
    except Exception as e:
        r["error"] = "could not open: %s" % e; return r
    try:
        if p.trailer.get("Encrypt") is not None:
            r["encrypted"] = True
        cat = p.catalog
        if not isinstance(cat, dict): raise PDFError("no catalog")
        mi = p.get(cat.get("MarkInfo"))
        r["marked"] = bool(isinstance(mi, dict) and p.get(mi.get("Marked")) is True)
        r["struct_tree"] = cat.get("StructTreeRoot") is not None
        r["tagged"] = r["marked"] and r["struct_tree"]
        lang = p.get(cat.get("Lang"))
        r["lang"] = text_of(lang) if not r.get("encrypted") else ("(encrypted)" if lang is not None else "")
        vp = p.get(cat.get("ViewerPreferences"))
        r["display_doc_title"] = bool(isinstance(vp, dict) and p.get(vp.get("DisplayDocTitle")) is True)
        r["title"] = text_of(p.get(p.info.get("Title"))).strip() if not r.get("encrypted") else ""
        r["producer"] = text_of(p.get(p.info.get("Producer"))).strip()[:80]
        r["creator"] = text_of(p.get(p.info.get("Creator"))).strip()[:80]
        xmp_title = ""
        md = p.get(cat.get("Metadata"))
        if isinstance(md, Stream):
            try:
                x = p.stream_data(md).decode("utf-8", "replace")
                m = re.search(r"(?s)<dc:title>.*?<rdf:li[^>]*>(.*?)</rdf:li>", x)
                if m: xmp_title = html.unescape(m.group(1)).strip()
            except Exception: pass
        r["xmp_title"] = xmp_title
        pages = p.pages()
        r["pages"] = len(pages)
        text_pages = 0; annot_pages = 0; annot_no_tabs = 0
        for d, res in pages:
            res = p.get(res)
            fonts = p.get(res.get("Font")) if isinstance(res, dict) else None
            if isinstance(fonts, dict) and fonts: text_pages += 1
            if p.get(d.get("Annots")):
                annot_pages += 1
                if d.get("Tabs") != "S": annot_no_tabs += 1
        r["text_pages"] = text_pages
        r["no_text_layer"] = len(pages) > 0 and text_pages == 0
        r["annot_pages_no_tab_order"] = annot_no_tabs
        ol = p.get(cat.get("Outlines"))
        r["bookmarks"] = bool(isinstance(ol, dict) and ol.get("First") is not None)
        # the structure tree: figures with alt, headings, tables
        figs = figs_alt = heads = tables = th = 0; types = {}
        if r["struct_tree"]:
            root = p.get(cat.get("StructTreeRoot"))
            rm = p.get(root.get("RoleMap")) if isinstance(root, dict) else None
            rm = rm if isinstance(rm, dict) else {}
            stack = [root.get("K")] if isinstance(root, dict) else []
            seen = set(); count = 0
            while stack and count < 200000:
                k = stack.pop()
                if isinstance(k, Ref):
                    if k.num in seen: continue
                    seen.add(k.num); k = p.get(k)
                if isinstance(k, list): stack.extend(reversed(k)); continue
                if not isinstance(k, dict): continue
                s = k.get("S")
                if s is None: continue                    # a marked-content or object reference
                count += 1
                t = str(s); hop = 0
                while t in rm and isinstance(rm.get(t), Name) and hop < 5 and rm[t] != t: t = str(rm[t]); hop += 1
                types[t] = types.get(t, 0) + 1
                if t == "Figure":
                    figs += 1
                    if text_of(p.get(k.get("Alt"))).strip() or text_of(p.get(k.get("ActualText"))).strip(): figs_alt += 1
                elif re.fullmatch(r"H[1-6]?", t): heads += 1
                elif t == "Table": tables += 1
                elif t == "TH": th += 1
                kk = k.get("K")
                if kk is not None: stack.append(kk)
        r.update(figures=figs, figures_with_alt=figs_alt, headings=heads, tables=tables, table_headers=th,
                 struct_types=dict(sorted(types.items(), key=lambda x: -x[1])[:12]))
        r["broken_xref"] = p.broken_xref
    except Exception as e:
        r["error"] = "%s: %s" % (type(e).__name__, e)
    finally:
        p.close()
    r["issues"] = pdf_issues(r)
    return r

def pdf_issues(r):
    """(severity, text, fix) per problem. fix: "meta" (fixmeta does it), "export" (export the deck again tagged),
    "source" (fix the source document and save it again as a tagged PDF)"""
    out = []
    if r.get("error"): return [("Severe", "could not be read (%s)" % r["error"], "source")]
    if r.get("encrypted"): out.append(("Severe", "encrypted (Panorama cannot check it)", "source"))
    if r.get("no_text_layer"): out.append(("Severe", "no text layer: a scanned or image only PDF", "source"))
    if not r.get("tagged"): out.append(("Major", "untagged (no structure tree)" if not r.get("struct_tree") else "structure tree but not marked as tagged", "export" if r.get("deck") else "source"))
    if not (r.get("title") or r.get("xmp_title")) or looks_like_filename(r.get("title") or r.get("xmp_title"), r["name"]): out.append(("Major", "no document title", "meta"))
    if not r.get("display_doc_title"): out.append(("Minor", "title bar shows the file name (DisplayDocTitle off)", "meta"))
    if not r.get("lang"): out.append(("Minor", "no document language", "meta"))
    if r.get("tagged") and r.get("figures", 0) > r.get("figures_with_alt", 0):
        out.append(("Major", "%d of %d figure tags without alt text" % (r["figures"] - r["figures_with_alt"], r["figures"]), "export" if r.get("deck") else "source"))
    if r.get("tagged") and not r.get("headings") and r.get("pages", 0) > 1:
        out.append(("Major", "no headings in the structure", "export" if r.get("deck") else "source"))
    if r.get("tagged") and r.get("tables", 0) and not r.get("table_headers"):
        out.append(("Major", "%d table(s) without header cells" % r["tables"], "export" if r.get("deck") else "source"))
    if r.get("pages", 0) >= LONG_PDF_PAGES and not r.get("bookmarks"):
        out.append(("Minor", "%d pages and no bookmarks" % r["pages"], "export" if r.get("deck") else "source"))
    if r.get("annot_pages_no_tab_order"):
        out.append(("Minor", "%d page(s) with links and no tab order" % r["annot_pages_no_tab_order"], "export" if r.get("deck") else "source"))
    return out

def looks_like_filename(t, fname):
    t = (t or "").strip()
    if not t: return True
    base = os.path.splitext(fname)[0]
    if t.lower() in ("untitled", "powerpoint presentation", "presentation", "microsoft word - document1", "slide 1"): return True
    if re.search(r"\.(pptx?|docx?|pdf|key|pages|xlsx?)$", t, re.I): return True
    if t == base and ("_" in base or "-" in base): return True
    if re.match(r"(?i)render_\d+", t): return True
    return False

def title_from_name(fname):
    """Ambisonics_vs_Binaural.pdf -> Ambisonics vs Binaural; Op_Amps__Bench_Day.pdf -> Op Amps: Bench Day"""
    base = os.path.splitext(os.path.basename(fname))[0]
    base = re.sub(r"-(Linked|Embedded)$", "", base)
    t = base.replace("__", ": ").replace("_", " ")
    joins = re.findall(r"(?<=[A-Za-z0-9]{2})-(?=[A-Z][A-Za-z0-9])", t)
    if len(joins) == 1 and ": " not in t:                  # Spatial_Recording-Orchestral -> Spatial Recording: Orchestral
        t = re.sub(r"(?<=[A-Za-z0-9]{2})-(?=[A-Z][A-Za-z0-9])", ": ", t)
    return re.sub(r"\s+", " ", t).strip()

def deck_title_for(pdf):
    """A slide PDF's deck title (docProps/core.xml) when it is a real title: Presentations/PDF/<Base>.pdf"""
    if os.path.basename(os.path.dirname(pdf)) != "PDF": return None
    base = os.path.splitext(os.path.basename(pdf))[0]; pres = os.path.dirname(os.path.dirname(pdf))
    for cand in ("%s-Embedded.pptx" % base, "%s-Linked.pptx" % base, "%s.pptx" % base):
        f = os.path.join(pres, cand)
        if not os.path.exists(f): continue
        try:
            with zipfile.ZipFile(f) as z: core = z.read("docProps/core.xml").decode("utf-8", "replace")
        except Exception: return None
        m = re.search(r"(?s)<dc:title>(.*?)</dc:title>", core)
        t = html.unescape(m.group(1)).strip() if m else ""
        return t if t and not looks_like_filename(t, cand) and len(t) <= 200 and title_matches(t, base) else None
    return None

def _words(t): return set(w for w in re.findall(r"[a-z0-9]+", t.lower().replace("&", " and ")) if w not in ("and", "the", "of", "a", "to", "in", "linked", "embedded"))

def title_matches(title, fname):
    """A deck title copied from another deck (3255 decks titled "Networking: IP Addressing") does not match its file"""
    a, b = _words(title), _words(os.path.splitext(os.path.basename(fname))[0].replace("_", " ").replace("-", " "))
    return bool(a and b) and len(a & b) / max(1, min(len(a), len(b))) >= 0.6

# ================================================================ PDF metadata fix (incremental update)

def ser(o):
    """A Python PDF object back to PDF bytes"""
    if isinstance(o, Ref): return b"%d %d R" % (o.num, o.gen)
    if isinstance(o, Name):
        out = bytearray(b"/")
        for ch in o.encode("latin-1"):
            out += bytes([ch]) if 0x21 <= ch <= 0x7E and ch not in b"()<>[]{}/%#" else b"#%02X" % ch
        return bytes(out)
    if isinstance(o, Str) or isinstance(o, bytes): return b"<" + bytes(o).hex().upper().encode() + b">"
    if isinstance(o, Num): return o.raw.encode()
    if o is True: return b"true"
    if o is False: return b"false"
    if o is None: return b"null"
    if isinstance(o, int): return str(o).encode()
    if isinstance(o, list): return b"[" + b" ".join(ser(x) for x in o) + b"]"
    if isinstance(o, dict): return b"<<" + b"".join(ser(Name(k)) + b" " + ser(v) for k, v in o.items()) + b">>"
    if isinstance(o, Keyword): return o.encode("latin-1")
    raise PDFError("cannot write %r" % type(o))

def pdf_text(s):
    """Python text as a PDF text string: PDFDocEncoding when plain ASCII, else UTF-16BE with a byte order mark"""
    try:
        s.encode("ascii"); return Str(s.encode("ascii"))
    except UnicodeEncodeError:
        return Str(b"\xfe\xff" + s.encode("utf-16-be"))

def fix_meta(path, lang="en-US", title=None, dry=False, like=None):
    """Adds what is missing of /Title, /Lang and DisplayDocTitle as an incremental update. Returns (changed, notes)."""
    p = PDF(path)
    try:
        if p.trailer.get("Encrypt") is not None: return False, ["encrypted: left alone"]
        if p.broken_xref: return False, ["cross-reference damaged: left alone (save it again from its source)"]
        root_ref = p.trailer.get("Root")
        if not isinstance(root_ref, Ref): return False, ["no catalog reference"]
        cat = p.get(root_ref)
        if not isinstance(cat, dict): return False, ["no catalog"]
        cat = dict(cat); notes = []; new_objs = {}; cat_changed = info_changed = False
        info_ref = p.trailer.get("Info"); info = p.get(info_ref) if info_ref is not None else None
        info = dict(info) if isinstance(info, dict) else {}
        old_title = text_of(p.get(info.get("Title"))).strip()
        # like: the PDF's final place, when this one is a fresh export in a temporary folder (Canvas Preview's Export)
        fname = os.path.basename(like or path)
        want_title = title or (old_title if not looks_like_filename(old_title, fname) and not looks_like_filename(old_title, os.path.basename(path)) else (deck_title_for(like or path) or title_from_name(fname)))
        if want_title != old_title:
            info["Title"] = pdf_text(want_title); notes.append("title %r" % want_title); info_changed = True
        if not text_of(p.get(cat.get("Lang"))).strip():
            cat["Lang"] = pdf_text(lang); notes.append("language %s" % lang); cat_changed = True
        vp_ref = cat.get("ViewerPreferences"); vp = p.get(vp_ref)
        vp = dict(vp) if isinstance(vp, dict) else {}
        if p.get(vp.get("DisplayDocTitle")) is not True:
            vp["DisplayDocTitle"] = True; notes.append("title bar shows the title")
            if isinstance(vp_ref, Ref): new_objs[vp_ref.num] = (vp_ref.gen, vp)
            else: cat["ViewerPreferences"] = vp; cat_changed = True
        if not notes: return False, ["nothing missing"]
        size = int(p.trailer.get("Size", Num("1")))
        size = max(size, (max(p.xref) + 1) if p.xref else 1)
        if cat_changed: new_objs[root_ref.num] = (root_ref.gen, cat)
        if info_changed:
            if isinstance(info_ref, Ref): new_objs[info_ref.num] = (info_ref.gen, info)
            else:
                info_ref = Ref(size, 0); size += 1; new_objs[info_ref.num] = (0, info)
        if dry: return True, notes
        b = p.b
        tail = bytes(b[-1:]) if len(b) else b"\n"
        buf = bytearray(b"" if tail in (b"\n", b"\r") else b"\n")
        base = len(b)
        offsets = {}
        for num in sorted(new_objs):
            gen, obj = new_objs[num]
            offsets[num] = (base + len(buf), gen)
            buf += b"%d %d obj\n" % (num, gen) + ser(obj) + b"\nendobj\n"
        trailer = {"Size": None, "Root": root_ref}
        if isinstance(info_ref, Ref): trailer["Info"] = info_ref
        if p.trailer.get("ID") is not None: trailer["ID"] = p.trailer["ID"]
        trailer["Prev"] = Num(str(p.startxref))
        if p.last_xref_is_stream:
            xnum = size; size += 1
            offsets[xnum] = (base + len(buf), 0)
            rows = bytearray(); index = []
            for num in sorted(offsets):
                off, gen = offsets[num]
                rows += bytes([1]) + off.to_bytes(4, "big") + min(gen, 65535).to_bytes(2, "big")
                index += [Num(str(num)), Num("1")]
            trailer["Size"] = Num(str(size))
            d = {"Type": Name("XRef"), "W": [Num("1"), Num("4"), Num("2")], "Index": index, "Length": Num(str(len(rows)))}
            d.update({k: v for k, v in trailer.items()})
            xoff = offsets[xnum][0]
            buf += b"%d 0 obj\n" % xnum + ser(d) + b"\nstream\n" + bytes(rows) + b"\nendstream\nendobj\n"
        else:
            trailer["Size"] = Num(str(size))
            xoff = base + len(buf)
            buf += b"xref\n"
            for num in sorted(offsets):
                off, gen = offsets[num]
                buf += b"%d 1\n%010d %05d n\r\n" % (num, off, gen)
            buf += b"trailer\n" + ser(trailer) + b"\n"
        buf += b"startxref\n%d\n%%%%EOF\n" % xoff
        if base + len(buf) > 2 ** 32 - 1: return False, ["file too large for this writer"]
        original = bytes(b)
    finally:
        p.close()
    # write beside, re-read, then replace (same folder so the move is atomic; times and Finder tags kept by copystat)
    d = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(prefix=".a11y-", suffix=".pdf", dir=d); os.close(fd)
    try:
        with open(tmp, "wb") as f: f.write(original); f.write(bytes(buf))
        chk = pdf_facts(tmp)
        if chk.get("error") or chk.get("pages") != pdf_facts_pages(original_path=path): raise PDFError("re-read failed: %s" % chk.get("error", "page count changed"))
        if chk.get("title") != want_title: raise PDFError("title did not read back")
        if not chk.get("lang") or not chk.get("display_doc_title"): raise PDFError("language or title bar did not read back")
        try: subprocess_xattr_copy(path, tmp)
        except Exception: pass
        st = os.stat(path); os.chmod(tmp, st.st_mode & 0o7777)       # mkstemp makes 0600; keep the file's own mode
        os.utime(tmp, ns=(st.st_atime_ns, time_now_ns()))
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp): os.remove(tmp)
        raise
    return True, notes

def time_now_ns():
    import time
    return time.time_ns()

_pages_cache = {}
def pdf_facts_pages(original_path):
    if original_path not in _pages_cache: _pages_cache[original_path] = pdf_facts(original_path).get("pages")
    return _pages_cache[original_path]

def subprocess_xattr_copy(src, dst):
    """Finder tags and other extended attributes go with the file (Adam's colour tags)"""
    import subprocess
    out = subprocess.run(["/usr/bin/xattr", src], capture_output=True, text=True).stdout.split()
    for a in out:
        if a in ("com.apple.quarantine",): continue
        v = subprocess.run(["/usr/bin/xattr", "-px", a, src], capture_output=True, text=True).stdout
        subprocess.run(["/usr/bin/xattr", "-wx", a, v.replace("\n", " ").strip(), dst], capture_output=True)

# ================================================================ decks

A_NS_DECOR = re.compile(r'<adec:decorative\b[^>]*\bval="1"|<[a-z0-9]+:decorative\b[^>]*\bval="1"')

def deck_facts(path):
    r = {"file": path, "name": os.path.basename(path)}
    try: z = zipfile.ZipFile(path)
    except Exception as e:
        r["error"] = "could not open: %s" % e; r["issues"] = [("Severe", r["error"], "deck")]; return r
    try:
        names = set(z.namelist())
        def rd(n):
            try: return z.read(n).decode("utf-8", "replace")
            except KeyError: return ""
        pres = rd("ppt/presentation.xml"); rels = rd("ppt/_rels/presentation.xml.rels")
        order = re.findall(r'<p:sldId\b[^>]*\br:id="([^"]+)"', re.search(r"(?s)<p:sldIdLst>(.*?)</p:sldIdLst>", pres).group(1) if "<p:sldIdLst>" in pres else "")
        tmap = {}
        for rel in re.findall(r"<Relationship\b[^>]*/?>", rels):
            i = re.search(r'Id="([^"]+)"', rel); t = re.search(r'Target="([^"]+)"', rel)
            if i and t: tmap[i.group(1)] = t.group(1)
        core = rd("docProps/core.xml")
        m = re.search(r"(?s)<dc:title>(.*?)</dc:title>", core)
        r["title"] = html.unescape(m.group(1)).strip() if m else ""
        lm = re.search(r'<a:defRPr\b[^>]*\blang="([^"]+)"', pres) or re.search(r'\blang="([^"]+)"', pres)
        r["lang"] = lm.group(1) if lm else ""
        slides = []; no_title = []; no_alt = []; bad_alt = []; pics = 0; decorative = 0; hidden = 0
        # a layout's title placeholder counts only when the slide fills it; text in a title placeholder is the title
        for pos, rid in enumerate(order, 1):
            tgt = tmap.get(rid)
            if not tgt: continue
            sx = posixpath.normpath(posixpath.join("ppt", tgt)) if not tgt.startswith("/") else tgt.lstrip("/")
            x = rd(sx)
            if not x: continue
            if re.search(r'<p:sld\b[^>]*\bshow="0"', x): hidden += 1; continue
            title = ""
            for sp in re.findall(r"(?s)<p:sp>.*?</p:sp>|<p:sp\b[^>]*>.*?</p:sp>", x):
                if re.search(r'<p:ph\b[^>]*\btype="(title|ctrTitle)"', sp):
                    t = " ".join(html.unescape(t) for t in re.findall(r"<a:t(?: [^>]*)?>([^<]*)</a:t>", sp)).strip()
                    if t: title = t; break
            if not title: no_title.append(pos)
            for pic in re.findall(r"(?s)<p:pic>.*?</p:pic>|<p:pic\b[^>]*>.*?</p:pic>", x):
                pics += 1
                c = re.search(r"<p:cNvPr\b[^>]*>", pic)
                cnv = c.group(0) if c else ""
                d = re.search(r'\bdescr="([^"]*)"', cnv)
                alt = html.unescape(d.group(1)).strip() if d else ""
                if A_NS_DECOR.search(pic): decorative += 1; continue
                if not alt: no_alt.append(pos)
                elif re.search(r"\.(png|jpe?g|gif|svg|webp|tiff?|bmp|emf|wmf)\b", alt, re.I) or "/" in alt and " " not in alt or alt.lower() in PLACEHOLDER_ALT or re.fullmatch(r"(?i)(picture|image|graphic)\s*\d+", alt):
                    bad_alt.append(pos)
                elif re.search(r"(?i)description automatically generated", alt): bad_alt.append(pos)
            slides.append(pos)
        r.update(slides=len(order), shown=len(slides), hidden=hidden, pictures=pics, decorative=decorative,
                 slides_no_title=no_title, pictures_no_alt=no_alt, pictures_bad_alt=bad_alt)
    except Exception as e:
        r["error"] = "%s: %s" % (type(e).__name__, e)
    finally:
        z.close()
    out = []
    if r.get("error"): out.append(("Severe", "could not be read (%s)" % r["error"], "deck"))
    else:
        if r["slides_no_title"]: out.append(("Major", "%d slide(s) without a title: %s" % (len(r["slides_no_title"]), short_list(r["slides_no_title"])), "deck"))
        if r["pictures_no_alt"]: out.append(("Major", "%d picture(s) without alt text on slide(s) %s" % (len(r["pictures_no_alt"]), short_list(sorted(set(r["pictures_no_alt"])))), "alt"))
        if r["pictures_bad_alt"]: out.append(("Major", "%d picture(s) whose alt text is a file name or placeholder on slide(s) %s" % (len(r["pictures_bad_alt"]), short_list(sorted(set(r["pictures_bad_alt"])))), "alt"))
        if not r["title"] or looks_like_filename(r["title"], r["name"]): out.append(("Major", "no document title (File > Properties)", "deck"))
        elif not title_matches(r["title"], r["name"]): out.append(("Minor", "document title %r looks copied from another deck" % r["title"], "deck"))
    r["issues"] = out
    return r

def short_list(xs, n=12):
    xs = list(xs)
    return ", ".join(str(x) for x in xs[:n]) + (" and %d more" % (len(xs) - n) if len(xs) > n else "")

DECOR_EXT = ('<a:extLst><a:ext uri="{C183D7F6-B498-43B3-948B-1728B52AA6E4}"><adec:decorative '
             'xmlns:adec="http://schemas.microsoft.com/office/drawing/2017/decorative" val="1"/></a:ext></a:extLst>')

def _title_style_safe(data):
    """A title placeholder takes the master's title style wherever the slide does not say otherwise. The change is
    only made when that style adds nothing the text box did not already have: no line spacing, no space before
    other than 0 (generated decks: pptxgenjs masters)."""
    for n, b in data.items():
        if not re.match(r"ppt/slideMasters/slideMaster\d+\.xml$", n): continue
        x = b.decode("utf-8", "replace")
        m = re.search(r"(?s)<p:titleStyle>.*?</a:lvl1pPr>", x)
        if not m: continue
        t = m.group(0)
        if "<a:lnSpc>" in t: return False
        sb = re.search(r'(?s)<a:spcBef>.*?val="(\d+)".*?</a:spcBef>', t)
        if sb and sb.group(1) != "0": return False
    return True

def make_title(sp):
    """A heading text box as the slide's title placeholder, looking the same: left alignment written out (the title
    style centres), the box's own position, insets and fonts kept. None when the box leans on inherited formatting."""
    body = re.search(r"<a:bodyPr\b[^>]*>", sp)
    if not body or not all(re.search(r'\b%s="' % k, body.group(0)) for k in ("anchor", "lIns", "tIns", "rIns", "bIns")): return None
    for rp in re.findall(r"(?s)<a:rPr\b[^>]*?(?:/>|>.*?</a:rPr>)", sp):
        if "<a:solidFill>" not in rp or "<a:latin " not in rp or ' sz="' not in rp: return None
    if not re.search(r"<a:rPr\b", sp): return None
    out = re.sub(r'<p:cNvSpPr txBox="1"\s*/>', '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>', sp, count=1)
    if re.search(r"<p:nvPr\s*/>", out): out = re.sub(r"<p:nvPr\s*/>", '<p:nvPr><p:ph type="title"/></p:nvPr>', out, count=1)
    elif re.search(r"<p:nvPr>\s*</p:nvPr>", out): out = re.sub(r"<p:nvPr>\s*</p:nvPr>", '<p:nvPr><p:ph type="title"/></p:nvPr>', out, count=1)
    else: return None
    out = re.sub(r"<a:pPr\b(?![^>]*\balgn=)", '<a:pPr algn="l"', out)
    out = re.sub(r"<a:p>(?!<a:pPr)", '<a:p><a:pPr algn="l"/>', out)
    return out

def deck_titles(path, out=None, dry=False):
    """Slides with no title placeholder get their heading text box made the title (what Panorama and PowerPoint's
    Accessibility Checker read as the slide title, and what a tagged PDF export can mark as a heading); the
    deckstyle bars (design shapes, no text) are marked decorative. Returns (slides titled, bars marked, skipped)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import deck_pair as dp
    from merge_decks import shapes, geom
    infos, data = dp.read(path)
    if not _title_style_safe(data): return 0, 0, ["master title style has its own spacing: left alone"]
    titled = bars = 0; skipped = []
    for k, (rid, sx) in enumerate(dp.slide_order(data), 1):
        if sx not in data: continue
        x = data[sx].decode("utf-8")
        if re.search(r'<p:sld\b[^>]*\bshow="0"', x): continue
        y = x
        for m in shapes(y):
            sp = m.group(0)
            # design shapes with no words and no picture fill: the deckstyle bars, card backgrounds, divider lines
            if "<a:t>" not in sp and "decorative" not in sp and "<a:blip" not in sp and "<p:ph" not in sp and (
                    re.search(r'<p:cNvPr [^>]*name="(deckstyle|Shape) \d+"', sp)):
                c = re.search(r"<p:cNvPr\b[^>]*?(/>|>)", sp)
                rep = c.group(0)[:-2] + ">" + DECOR_EXT + "</p:cNvPr>" if c.group(1) == "/>" else c.group(0) + DECOR_EXT
                y = y.replace(sp, sp.replace(c.group(0), rep, 1), 1); bars += 1
        has = any(re.search(r'<p:ph\b[^>]*\btype="(title|ctrTitle)"', m.group(0)) and "<a:t>" in m.group(0) for m in shapes(y))
        if not has:
            best = None
            for m in shapes(y):
                sp = m.group(0); g = geom(sp); sz = re.search(r'sz="(\d+)"', sp)
                t = " ".join(re.findall(r"<a:t>([^<]*)</a:t>", sp)).strip()
                if "<p:ph" in sp or not (g and sz and t): continue
                near_top = g[1] < 1300000 and int(sz.group(1)) >= 2400
                big = int(sz.group(1)) >= 3200                # a title slide: the big words anywhere
                if not (near_top or big): continue
                key = (1 if near_top else 0, int(sz.group(1)))
                if best is None or key > best[0]: best = (key, sp)
            if best:
                new = make_title(best[1])
                if new: y = y.replace(best[1], new, 1); titled += 1
                else: skipped.append("slide %d: heading box uses inherited formatting" % k)
            else: skipped.append("slide %d: no heading text near the top" % k)
        if y != x: data[sx] = y.encode("utf-8")
    if not dry and (titled or bars):
        target = out or path
        if not out:
            arch = os.path.join(os.path.dirname(path), "Archive"); os.makedirs(arch, exist_ok=True)
            shutil.copy2(path, os.path.join(arch, "%s (before slide titles %s).pptx" % (os.path.splitext(os.path.basename(path))[0], datetime.datetime.now().strftime("%Y-%m-%d %H%M"))))
        dp.write(target, infos, data)
    return titled, bars, skipped

# ================================================================ pages and pictures

def class_of(path):
    m = re.search(r"DAPR[- ](\d{4}[A-Z]?)", path)
    return m.group(1) if m else ("All" if "/All/" in path else "?")

def current_package(code):
    """The class's current export, else (no live course) its newest Template package; (path, label)"""
    for d in glob.glob(os.path.join(COURSES, "DAPR %s - *" % code)):
        ent = os.path.join(d, "Canvas", "Canvas Templates", "-Canvas Entire Course")
        exp = [f for f in glob.glob(os.path.join(ent, "*Canvas Export (latest).imscc"))]
        if exp: return exp[0], "current export"
        best = None
        for f in glob.glob(os.path.join(ent, "**", "*.imscc"), recursive=True):
            if "_superseded" in f or "/Archive/" in f or f.endswith(".noimport"): continue
            m = re.search(r"-v(\d+)-(Template|Full)", os.path.basename(f))
            if m and (best is None or int(m.group(1)) > best[0]): best = (int(m.group(1)), f)
        if best: return best[1], "newest package v%d" % best[0]
    return None, ""

IMG_RE = re.compile(r"(?is)<img\b[^>]*>")
A_RE = re.compile(r'(?is)<a\b[^>]*\bhref="([^"]+)"[^>]*>(.*?)</a>')

def attr(tag, name):
    m = re.search(r'(?is)\b%s\s*=\s*"([^"]*)"' % name, tag) or re.search(r"(?is)\b%s\s*=\s*'([^']*)'" % name, tag)
    return html.unescape(m.group(1)) if m else None

def alt_problem(alt, src):
    if alt is None: return "no alt attribute"
    a = alt.strip()
    if not a: return "empty alt"
    if len(a) > 120: return "alt over 120 characters"
    if a.lower() in PLACEHOLDER_ALT: return "placeholder alt %r" % a
    fn = os.path.basename(urllib.parse.unquote(src.split("?")[0]))
    if a == fn or re.search(r"\.(png|jpe?g|gif|svg|webp)$", a, re.I): return "file name as alt"
    return None

def read_pages(pkg):
    """Every HTML page in a package (read in place): [(entry name, page title, html)]"""
    out = []
    try: z = zipfile.ZipFile(pkg)
    except Exception: return out
    with z:
        for n in z.namelist():
            if n == "course_settings/module_meta.xml":
                # module items that are links (External URL): the slide PDFs students open from a module
                t = z.read(n).decode("utf-8", "replace")
                for item in re.findall(r"(?s)<item\b.*?</item>", t):
                    u = re.search(r"<url>(.*?)</url>", item); ti = re.search(r"<title>(.*?)</title>", item)
                    if u: out.append((n, "module item: " + html.unescape(ti.group(1) if ti else ""), '<a href="%s">x</a>' % html.unescape(u.group(1))))
                continue
            if not n.lower().endswith((".html", ".htm", ".xml")) or n.startswith("course_settings/") or n == "imsmanifest.xml": continue
            try: t = z.read(n).decode("utf-8", "replace")
            except Exception: continue
            if n.lower().endswith(".xml"):
                # assignment and quiz bodies carry their HTML escaped inside XML
                if "&lt;img" not in t and "&lt;a " not in t: continue
                t = html.unescape(t)
            m = re.search(r"(?is)<title>(.*?)</title>", t)
            out.append((n, html.unescape(m.group(1)).strip() if m else n, t))
    return out

def gh_rel(src):
    s = urllib.parse.unquote(src)
    i = s.find(GH_RAW)
    return s[i + len(GH_RAW):].split("?")[0] if i >= 0 else None

def cf_rel(href):
    """A Cloudflare Canvas Links URL as a path inside the Canvas Links folder"""
    s = urllib.parse.unquote(href).split("?")[0]
    m = re.search(r"https?://[^/]+/((?:DAPR-\d{4}[A-Z]?--[^/]+|All)/.+)$", s)
    if not m: return None
    if not any(h in s for h in CF_HOSTS) and "githubusercontent" in s: return None
    return m.group(1)

# ================================================================ scan

def walk_files(root, exts):
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS and not x.startswith(".")]
        for f in files:
            if f.startswith(("~$", ".")) or "conflicted copy" in f: continue
            if os.path.splitext(f)[1].lower() in exts: yield os.path.join(d, f)

def scan(only=None, out_dir=OUT):
    os.makedirs(out_dir, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %-I:%M %p")
    classes = {}
    def C(code): return classes.setdefault(code, {"class": code, "pdfs": [], "decks": [], "pictures": [], "package": "", "package_label": ""})
    # PDFs and decks in Cloudflare
    decks_by_dir = {}
    for f in walk_files(CF, {".pdf", ".pptx"}):
        code = class_of(f)
        if only and code != only: continue
        if f.lower().endswith(".pptx"):
            if f.endswith("-Embedded.pptx") and os.path.exists(f.replace("-Embedded.pptx", "-Linked.pptx")): continue
            d = deck_facts(f); d["rel"] = os.path.relpath(f, CF); C(code)["decks"].append(d)
            decks_by_dir.setdefault(os.path.dirname(f), []).append(f)
        else:
            r = pdf_facts(f); r["rel"] = os.path.relpath(f, CF)
            # a slide PDF: Presentations/PDF/<Base>.pdf beside <Base>-Linked.pptx
            if os.path.basename(os.path.dirname(f)) == "PDF":
                base = os.path.splitext(os.path.basename(f))[0]
                pres = os.path.dirname(os.path.dirname(f))
                for cand in ("%s-Embedded.pptx" % base, "%s-Linked.pptx" % base, "%s.pptx" % base):
                    if os.path.exists(os.path.join(pres, cand)): r["deck"] = os.path.relpath(os.path.join(pres, cand), CF); break
            r["issues"] = pdf_issues(r)
            C(code)["pdfs"].append(r)
    # pages: which files and pictures students reach
    codes = sorted(set(list(classes) + [c for c in ("2000", "2010", "2020", "2255", "3255", "3340", "3345") if not only or c == only]))
    for code in codes:
        if code in ("All", "?"): continue
        c = C(code)
        pkg, label = current_package(code)
        c["package"], c["package_label"] = pkg or "", label
        linked_cf = {}; pics = {}
        for n, title, t in (read_pages(pkg) if pkg else []):
            for tag in IMG_RE.findall(t):
                src = attr(tag, "src") or ""
                rel = gh_rel(src)
                if not rel:
                    cr = cf_rel(src)                      # a picture on Cloudflare (All/BOAA_Lab/Images)
                    if not cr or os.path.splitext(cr)[1].lower() not in PIC_EXT: continue
                    rel = "Cloudflare: " + cr
                prob = alt_problem(attr(tag, "alt"), src)
                e = pics.setdefault(rel, {"rel": rel, "pages": [], "problems": []})
                if title not in e["pages"]: e["pages"].append(title)
                if prob and (prob, title) not in [tuple(x) for x in e["problems"]]: e["problems"].append((prob, title))
            for href, text in A_RE.findall(t):
                rel = cf_rel(href)
                if rel: linked_cf.setdefault(rel, []).append(title)
        for r in c["pdfs"]: r["linked_from"] = sorted(set(linked_cf.get(r["rel"], [])))[:6]
        c["linked_files"] = len(linked_cf)
        c["missing_links"] = sorted(r for r in linked_cf if r.lower().endswith(".pdf") and not os.path.exists(os.path.join(CF, r)))[:50]
        for rel, e in sorted(pics.items()):
            p = os.path.join(CF, rel[len("Cloudflare: "):]) if rel.startswith("Cloudflare: ") else os.path.join(GH, rel)
            e["exists"] = os.path.exists(p)
            c["pictures"].append(e)
        # GitHub pictures in this class's folder that no page links (reported, not flagged red)
        gdirs = glob.glob(os.path.join(GH, "DAPR-%s--*" % code))
        unlinked = 0
        for g in gdirs:
            for f in walk_files(g, PIC_EXT):
                if os.path.relpath(f, GH) not in pics: unlinked += 1
        c["pictures_unlinked"] = unlinked
    # report
    summary = []
    for code in sorted(classes):
        c = classes[code]
        pdf_untagged = sum(1 for r in c["pdfs"] if not r.get("tagged"))
        pdf_meta = sum(1 for r in c["pdfs"] if any(i[2] == "meta" for i in r["issues"]))
        pdf_severe = sum(1 for r in c["pdfs"] if any(i[0] == "Severe" for i in r["issues"]))
        fig_noalt = sum(max(0, r.get("figures", 0) - r.get("figures_with_alt", 0)) for r in c["pdfs"] if r.get("tagged"))
        deck_noalt = sum(len(d.get("pictures_no_alt", [])) + len(d.get("pictures_bad_alt", [])) for d in c["decks"])
        deck_notitle = sum(len(d.get("slides_no_title", [])) for d in c["decks"])
        pic_bad = sum(1 for p in c["pictures"] if p["problems"])
        pic_missing = sum(1 for p in c["pictures"] if not p.get("exists"))
        c["counts"] = dict(pdfs=len(c["pdfs"]), pdf_untagged=pdf_untagged, pdf_meta=pdf_meta, pdf_severe=pdf_severe,
                           pdf_figures_no_alt=fig_noalt, decks=len(c["decks"]), deck_pictures_no_alt=deck_noalt,
                           deck_slides_no_title=deck_notitle, pictures=len(c["pictures"]), pictures_bad_alt=pic_bad,
                           pictures_missing=pic_missing, pictures_unlinked=c.get("pictures_unlinked", 0),
                           red=pdf_untagged + pdf_severe + deck_noalt + pic_bad + pic_missing,
                           yellow=pdf_meta + deck_notitle + fig_noalt)
        write_class_report(c, out_dir, stamp)
        summary.append(c["counts"] | {"class": code})
    with open(os.path.join(out_dir, "summary.json"), "w") as f:
        json.dump({"made": stamp, "classes": summary}, f, indent=1)
    return summary

def write_class_report(c, out_dir, stamp):
    code = c["class"]; k = c["counts"]
    name = "All Classes" if code == "All" else "DAPR %s" % code
    L = ["# Linked Files Accessibility: %s" % name, "",
         "Made %s by Build-Tools/a11y_files.py (read only). Standards §2a: files a class links follow the same rules as Canvas pages." % stamp, ""]
    if c.get("package"): L += ["Pages read from: %s (%s)." % (os.path.basename(c["package"]), c["package_label"]), ""]
    L += ["| What | Count |", "|---|---|",
          "| PDFs | %d |" % k["pdfs"], "| PDFs untagged | %d |" % k["pdf_untagged"],
          "| PDFs missing title, language or title bar (fixmeta fixes) | %d |" % k["pdf_meta"],
          "| PDFs scanned, encrypted or unreadable | %d |" % k["pdf_severe"],
          "| Figure tags without alt in tagged PDFs | %d |" % k["pdf_figures_no_alt"],
          "| Decks | %d |" % k["decks"], "| Deck pictures without real alt text | %d |" % k["deck_pictures_no_alt"],
          "| Deck slides without a title | %d |" % k["deck_slides_no_title"],
          "| Pictures on pages (GitHub and Cloudflare) | %d |" % k["pictures"], "| Pictures with missing or bad alt on a page | %d |" % k["pictures_bad_alt"],
          "| Pictures a page links that are not on the Mac (GitHub repo or Canvas Links) | %d |" % k["pictures_missing"],
          "| GitHub pictures no page links | %d |" % k["pictures_unlinked"], ""]
    bad = [r for r in c["pdfs"] if r["issues"]]
    if bad:
        L += ["## PDFs", ""]
        for r in sorted(bad, key=lambda r: r["rel"]):
            how = sorted(set(i[2] for i in r["issues"]))
            L.append("- `%s`%s: %s. Fix: %s." % (r["rel"], " (linked from %s)" % ", ".join(r["linked_from"][:3]) if r.get("linked_from") else "",
                     "; ".join("%s %s" % (i[0], i[1]) for i in r["issues"]),
                     ", ".join({"meta": "fixmeta (metadata only)", "export": "export the deck again as a tagged PDF", "source": "save the source again as a tagged PDF"}[h] for h in how)))
        L.append("")
    badd = [d for d in c["decks"] if d["issues"]]
    if badd:
        L += ["## Decks", ""]
        for d in sorted(badd, key=lambda d: d["rel"]):
            L.append("- `%s`: %s." % (d["rel"], "; ".join("%s %s" % (i[0], i[1]) for i in d["issues"])))
        L.append("")
    badp = [p for p in c["pictures"] if p["problems"] or not p.get("exists")]
    if badp:
        L += ["## Pictures on pages", ""]
        for p in badp[:400]:
            probs = "; ".join("%s (%s)" % (a, b) for a, b in p["problems"][:4])
            L.append("- `%s`: %s%s" % (p["rel"], "" if p.get("exists") else "NOT ON THE MAC; ", probs or "linked"))
        L.append("")
    if c.get("missing_links"):
        L += ["## Cloudflare links with no file on the Mac", ""] + ["- `%s`" % r for r in c["missing_links"]] + [""]
    base = "a11y-files-%s" % code
    with open(os.path.join(out_dir, base + ".md"), "w") as f: f.write("\n".join(L))
    slim = {k2: v for k2, v in c.items()}
    with open(os.path.join(out_dir, base + ".json"), "w") as f: json.dump(slim, f, indent=1, default=str)

# ================================================================ main

def main(argv):
    if not argv or argv[0] in ("-h", "--help"): print(__doc__); return 0
    cmd, rest = argv[0], argv[1:]
    def opt(name, default=None):
        if name in rest:
            i = rest.index(name); v = rest[i + 1]; del rest[i:i + 2]; return v
        return default
    if cmd == "scan":
        only = opt("--class"); out = opt("--out", OUT)
        s = scan(only, out)
        for c in s:
            print("%-5s PDFs %3d (untagged %3d, metadata %3d, severe %d) decks %3d (pictures no alt %3d, slides no title %3d) page pictures %4d (bad alt %3d, missing %d) red %d" % (
                c["class"], c["pdfs"], c["pdf_untagged"], c["pdf_meta"], c["pdf_severe"], c["decks"], c["deck_pictures_no_alt"],
                c["deck_slides_no_title"], c["pictures"], c["pictures_bad_alt"], c["pictures_missing"], c["red"]))
        print("report: %s" % out)
        return 0
    if cmd == "summary":
        out = opt("--out", OUT)
        try: print(open(os.path.join(out, "summary.json")).read())
        except OSError: print("{}"); return 1
        return 0
    if cmd == "pdf":
        for f in rest: print(json.dumps(pdf_facts(f), indent=1, default=str))
        return 0
    if cmd == "deck":
        for f in rest: print(json.dumps(deck_facts(f), indent=1, default=str))
        return 0
    if cmd == "titles":
        dry = "--dry" in rest
        if dry: rest.remove("--dry")
        out = opt("--out")
        for a in rest:
            t, b, sk = deck_titles(a, out=out, dry=dry)
            print("%s %s: %d slide titles, %d design bars marked decorative%s" % ("WOULD CHANGE" if dry else "CHANGED" if (t or b) else "same", a, t, b, ("; skipped " + "; ".join(sk[:6])) if sk else ""))
        return 0
    if cmd == "fixmeta":
        dry = "--dry" in rest
        if dry: rest.remove("--dry")
        lang = opt("--lang", "en-US"); title = opt("--title"); like = opt("--like")
        files = []
        for a in rest:
            files += sorted(walk_files(a, {".pdf"})) if os.path.isdir(a) else [a]
        changed = 0
        for f in files:
            try:
                ok, notes = fix_meta(f, lang=lang, title=title if len(files) == 1 else None, dry=dry, like=like if len(files) == 1 else None)
            except Exception as e:
                ok, notes = False, ["FAILED: %s" % e]
            if ok: changed += 1
            print("%s %s: %s" % ("WOULD FIX" if ok and dry else "FIXED" if ok else "same", f, "; ".join(notes)))
        print("%d of %d %s" % (changed, len(files), "would change" if dry else "changed"))
        return 0
    print(__doc__); return 2

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
