#!/usr/bin/env python3
"""
powerpoint_access.py: lets PowerPoint on the Mac open the pictures a Linked deck links (Adam, 2026-10-01).

PowerPoint runs in Apple's sandbox, so a Linked deck's pictures in Presentations/Images show as "The picture can't be
displayed" until PowerPoint is granted access. Office's own way to grant more than one file at a time is the VBA
function GrantAccessToMultipleFiles, which shows Office's Grant Access dialog (Adam clicks Grant; never an AI).
This tool builds a tiny macro presentation once (Canvas Preview Access.pptm, in the Canvas Preview cache), opens it
in PowerPoint, runs its one macro with the folders or files to grant, and closes it. Nothing in any deck changes.

    python3 powerpoint_access.py build                      make the macro presentation (done by grant as needed)
    python3 powerpoint_access.py grant <folder|file> [...]  show Office's Grant Access dialog for these paths
    python3 powerpoint_access.py granted [<path> ...]       which of these paths PowerPoint already holds a grant for

The macro presentation carries a hand-written VBA project (MS-OVBA, source only, so PowerPoint compiles it on open)
inside a minimal compound file (MS-CFB). PowerPoint asks once per opening whether to enable its macros.
"""
import sys, os, io, re, struct, zipfile, uuid, random, subprocess, urllib.parse, json, plistlib, math

CACHE = os.path.expanduser("~/Library/Caches/CanvasPreview")
PPTM = os.path.join(CACHE, "Canvas Preview Access.pptm")
BOOKMARKS = os.path.expanduser("~/Library/Containers/com.microsoft.Powerpoint/Data/Library/Preferences/com.microsoft.Powerpoint.securebookmarks.plist")
MODULE = "CanvasPreviewAccess"
MACRO = "GrantPaths"
SOURCE = (
    'Attribute VB_Name = "%s"\r\n'
    "' Canvas Preview: shows Office's Grant Access dialog for the folders or files Canvas Preview passes in\r\n"
    "' (one path per line), so Linked decks can show their pictures.\r\n"
    "Public Sub %s(ByVal pathList As String)\r\n"
    "    Dim parts() As String, files() As Variant, i As Long, n As Long\r\n"
    "    parts = Split(pathList, vbLf)\r\n"
    "    ReDim files(0 To UBound(parts))\r\n"
    "    n = 0\r\n"
    "    For i = 0 To UBound(parts)\r\n"
    "        If Len(Trim(parts(i))) > 0 Then files(n) = parts(i): n = n + 1\r\n"
    "    Next i\r\n"
    "    If n = 0 Then Exit Sub\r\n"
    "    ReDim Preserve files(0 To n - 1)\r\n"
    "    GrantAccessToMultipleFiles files\r\n"
    "End Sub\r\n" % (MODULE, MACRO))

# ---------------------------------------------------------------- MS-OVBA

def compress(data):
    """MS-OVBA 2.4.1: whole 4096-byte chunks stored raw, the last one as literal tokens (valid, just not smaller)"""
    out = bytearray(b"\x01")
    for i in range(0, len(data), 4096):
        chunk = data[i:i + 4096]
        if len(chunk) == 4096:
            out += struct.pack("<H", 0x0FFF | (0b011 << 12)) + chunk
            continue
        body = bytearray()
        for j in range(0, len(chunk), 8):
            body += b"\x00" + chunk[j:j + 8]
        if len(body) + 2 > 4098: raise ValueError("last chunk too long for literal tokens")
        out += struct.pack("<H", (len(body) + 2 - 3) | (0b011 << 12) | (1 << 15)) + body
    return bytes(out)

def pad_source(src):
    """A last chunk over 3640 bytes cannot be written as literals: pad with a comment so it fills 4096 exactly"""
    b = src.encode("cp1252")
    r = len(b) % 4096
    if r > 3640:
        need = 4096 - r
        b += b"'" + b" " * (need - 3) + b"\r\n"
    return b

def rec(rid, payload):
    return struct.pack("<HI", rid, len(payload)) + payload

def dir_stream():
    u = lambda s: s.encode("utf-16-le")
    m = lambda s: s.encode("cp1252")
    d = bytearray()
    d += rec(0x0001, struct.pack("<I", 1))                      # PROJECTSYSKIND: 32-bit
    d += rec(0x0002, struct.pack("<I", 0x409))                  # PROJECTLCID
    d += rec(0x0014, struct.pack("<I", 0x409))                  # PROJECTLCIDINVOKE
    d += rec(0x0003, struct.pack("<H", 1252))                   # PROJECTCODEPAGE
    d += rec(0x0004, m("VBAProject"))                           # PROJECTNAME
    d += rec(0x0005, b"") + rec(0x0040, b"")                    # PROJECTDOCSTRING + unicode
    d += rec(0x0006, b"") + rec(0x003D, b"")                    # PROJECTHELPFILEPATH 1 and 2
    d += rec(0x0007, struct.pack("<I", 0))                      # PROJECTHELPCONTEXT
    d += rec(0x0008, struct.pack("<I", 0))                      # PROJECTLIBFLAGS
    d += struct.pack("<HIIH", 0x0009, 4, 1, 0)                  # PROJECTVERSION (size field is fixed at 4)
    d += rec(0x000C, b"") + rec(0x003C, b"")                    # PROJECTCONSTANTS + unicode
    d += struct.pack("<HIH", 0x000F, 2, 1)                      # PROJECTMODULES: one module
    d += struct.pack("<HIH", 0x0013, 2, 0xFFFF)                 # PROJECTCOOKIE
    d += rec(0x0019, m(MODULE)) + rec(0x0047, u(MODULE))        # MODULENAME + unicode
    d += rec(0x001A, m(MODULE)) + rec(0x0032, u(MODULE))        # MODULESTREAMNAME + unicode
    d += rec(0x001C, b"") + rec(0x0048, b"")                    # MODULEDOCSTRING + unicode
    d += rec(0x0031, struct.pack("<I", 0))                      # MODULEOFFSET: source starts at 0, no p-code
    d += rec(0x001E, struct.pack("<I", 0))                      # MODULEHELPCONTEXT
    d += struct.pack("<HIH", 0x002C, 2, 0xFFFF)                 # MODULECOOKIE
    d += struct.pack("<HI", 0x0021, 0)                          # MODULETYPE: procedural
    d += struct.pack("<HI", 0x002B, 0)                          # module terminator
    d += struct.pack("<HI", 0x0010, 0)                          # dir terminator
    return bytes(d)

def encrypt(data, project_id):
    """MS-OVBA 2.4.3 data encryption, used for the PROJECT stream's CMG, DPB and GC lines"""
    seed = random.randrange(256); version = 2
    proj_key = sum(project_id.encode("cp1252")) & 0xFF
    out = bytearray([seed, seed ^ version, seed ^ proj_key])
    unenc1, enc1, enc2 = proj_key, seed ^ proj_key, seed ^ version     # the scrambled key and version bytes start the chain
    def put(b):
        nonlocal unenc1, enc1, enc2
        e = b ^ ((enc2 + unenc1) & 0xFF)
        out.append(e); enc2 = enc1; enc1 = e; unenc1 = b
    for _ in range((seed & 6) // 2): put(random.randrange(256))
    for b in struct.pack("<I", len(data)): put(b)
    for b in data: put(b)
    return out.hex().upper()

def project_stream(pid):
    lines = ['ID="%s"' % pid, "Module=%s" % MODULE, 'Name="VBAProject"', 'HelpContextID="0"', 'VersionCompatible32="393222000"',
             'CMG="%s"' % encrypt(b"\x00\x00\x00\x00", pid), 'DPB="%s"' % encrypt(b"\x00", pid), 'GC="%s"' % encrypt(b"\xff", pid), "",
             "[Host Extender Info]", "&H00000001={3832D640-CF90-11CF-8E43-00A0C911005A};VBE;&H00000000", "",
             "[Workspace]", "%s=0, 0, 0, 0, C" % MODULE, ""]
    return "\r\n".join(lines).encode("cp1252")

def projectwm_stream():
    return MODULE.encode("cp1252") + b"\x00" + MODULE.encode("utf-16-le") + b"\x00\x00" + b"\x00\x00"

# ---------------------------------------------------------------- MS-CFB (version 3, 512-byte sectors)

FREE, END, FATSECT, NOSTREAM = 0xFFFFFFFF, 0xFFFFFFFE, 0xFFFFFFFD, 0xFFFFFFFF

def cfb(storages):
    """storages: {"": {name: bytes}, "VBA": {name: bytes}}; every stream is under 4096 bytes, so all live in the mini stream"""
    entries = [dict(name="Root Entry", type=5, children=[], data=None)]
    def add(parent, name, typ, data=None):
        entries.append(dict(name=name, type=typ, children=[], data=data)); idx = len(entries) - 1
        entries[parent]["children"].append(idx); return idx
    for name, data in storages[""].items(): add(0, name, 2, data)
    for sname, streams in storages.items():
        if not sname: continue
        s = add(0, sname, 1)
        for name, data in streams.items(): add(s, name, 2, data)
    # mini stream: 64-byte mini sectors
    mini = bytearray(); minifat = []
    for e in entries:
        if e["type"] != 2: continue
        assert len(e["data"]) < 4096, e["name"]
        n = max(1, math.ceil(len(e["data"]) / 64)); e["start"] = len(minifat); e["size"] = len(e["data"])
        minifat += [len(minifat) + k + 1 for k in range(n - 1)] + [END]
        mini += e["data"] + b"\x00" * (n * 64 - len(e["data"]))
    # each storage's children as a balanced tree, ordered by name length then upper-case name
    key = lambda i: (len(entries[i]["name"]), entries[i]["name"].upper())
    def tree(ids):
        if not ids: return NOSTREAM
        ids = sorted(ids, key=key); mid = len(ids) // 2; r = ids[mid]
        entries[r]["left"] = tree(ids[:mid]); entries[r]["right"] = tree(ids[mid + 1:]); return r
    for e in entries:
        e.setdefault("left", NOSTREAM); e.setdefault("right", NOSTREAM)
    for e in entries: e["child"] = tree(e["children"])
    # sector plan: 0 = FAT, then directory, mini FAT, mini stream
    dir_secs = math.ceil(len(entries) * 128 / 512)
    mf_bytes = struct.pack("<%dI" % len(minifat), *minifat); mf_secs = math.ceil(len(mf_bytes) / 512)
    ms_secs = math.ceil(len(mini) / 512)
    first_dir, first_mf, first_ms = 1, 1 + dir_secs, 1 + dir_secs + mf_secs
    total = first_ms + ms_secs; assert total <= 128
    fat = [FATSECT]
    for start, n in ((first_dir, dir_secs), (first_mf, mf_secs), (first_ms, ms_secs)):
        fat += [start + k + 1 for k in range(n - 1)] + [END]
    fat += [FREE] * (128 - len(fat))
    entries[0]["start"] = first_ms; entries[0]["size"] = len(mini)
    d = bytearray()
    for e in entries:
        nm = e["name"].encode("utf-16-le") + b"\x00\x00"
        d += nm + b"\x00" * (64 - len(nm)) + struct.pack("<HBB", len(nm), e["type"], 1)
        d += struct.pack("<III", e["left"], e["right"], e["child"]) + b"\x00" * 16 + b"\x00" * 4 + b"\x00" * 16
        start = e.get("start", END) if e["type"] != 1 else 0; size = e.get("size", 0)
        d += struct.pack("<IQ", start, size)
    d += b"\x00" * (dir_secs * 512 - len(d))
    for k in range(len(entries), dir_secs * 4):                 # unused directory slots
        off = k * 128; d[off:off + 128] = b"\x00" * 64 + struct.pack("<HBB", 0, 0, 0) + struct.pack("<III", NOSTREAM, NOSTREAM, NOSTREAM) + b"\x00" * 48
    hdr = bytearray(b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1" + b"\x00" * 16)
    hdr += struct.pack("<HHHHH", 0x003E, 0x0003, 0xFFFE, 9, 6) + b"\x00" * 6
    hdr += struct.pack("<IIIIIIIII", 0, 1, first_dir, 0, 4096, first_mf if mf_secs else END, mf_secs, END, 0)
    hdr += struct.pack("<I", 0) + struct.pack("<108I", *([FREE] * 108))
    assert len(hdr) == 512
    body = struct.pack("<128I", *fat) + bytes(d) + mf_bytes + b"\xff" * (mf_secs * 512 - len(mf_bytes)) + bytes(mini) + b"\x00" * (ms_secs * 512 - len(mini))
    return bytes(hdr) + body

def vba_project_bin():
    pid = "{%s}" % str(uuid.uuid4()).upper()
    return cfb({"": {"PROJECT": project_stream(pid), "PROJECTwm": projectwm_stream()},
                "VBA": {"_VBA_PROJECT": b"\xCC\x61\xFF\xFF\x00\x00\x00",
                        "dir": compress(dir_stream()),
                        MODULE: compress(pad_source(SOURCE))}})

# ---------------------------------------------------------------- the macro presentation

SLIDE_W, SLIDE_H = 12192000, 6858000
NS_P = 'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"'
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

def theme():
    clr = "".join('<a:%s><a:srgbClr val="%s"/></a:%s>' % (n, v, n) for n, v in (("dk1", "000000"), ("lt1", "FFFFFF"), ("dk2", "1F2A25"), ("lt2", "EEECE1"),
          ("accent1", "275D38"), ("accent2", "BF360C"), ("accent3", "0D47A1"), ("accent4", "856404"), ("accent5", "4A148C"), ("accent6", "424242"), ("hlink", "0D47A1"), ("folHlink", "4A148C")))
    fill = '<a:solidFill><a:schemeClr val="phClr"/></a:solidFill>'
    ln = '<a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln>'
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Canvas Preview">'
            '<a:themeElements><a:clrScheme name="Canvas Preview">%s</a:clrScheme><a:fontScheme name="Canvas Preview"><a:majorFont><a:latin typeface="Arial"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>'
            '<a:minorFont><a:latin typeface="Arial"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont></a:fontScheme><a:fmtScheme name="Canvas Preview"><a:fillStyleLst>%s%s%s</a:fillStyleLst>'
            '<a:lnStyleLst>%s%s%s</a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle><a:effectStyle><a:effectLst/></a:effectStyle><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst>'
            '<a:bgFillStyleLst>%s%s%s</a:bgFillStyleLst></a:fmtScheme></a:themeElements><a:objectDefaults/><a:extraClrSchemeLst/></a:theme>') % (clr, fill, fill, fill, ln, ln, ln, fill, fill, fill)

def pptm_bytes():
    sp_tree = '<p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr/></p:spTree>'
    text = ('<p:sp><p:nvSpPr><p:cNvPr id="2" name="Note"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="609600" y="2743200"/><a:ext cx="10972800" cy="1371600"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr><p:txBody><a:bodyPr wrap="square"/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US" sz="2400"/>'
            '<a:t>Canvas Preview opens this file only to show Office&apos;s Grant Access dialog, then closes it. Nothing here is a course deck.</a:t></a:r></a:p></p:txBody></p:sp>')
    files = {
        "[Content_Types].xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/>'
            '<Default Extension="bin" ContentType="application/vnd.ms-office.vbaProject"/>'
            '<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.ms-powerpoint.presentation.macroEnabled.main+xml"/>'
            '<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>'
            '<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>'
            '<Override PartName="/ppt/slides/slide1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
            '<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/></Types>',
        "_rels/.rels": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="%s/officeDocument" Target="ppt/presentation.xml"/></Relationships>' % R,
        "ppt/presentation.xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:presentation %s><p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>'
            '<p:sldIdLst><p:sldId id="256" r:id="rId2"/></p:sldIdLst><p:sldSz cx="%d" cy="%d"/><p:notesSz cx="6858000" cy="9144000"/></p:presentation>' % (NS_P, SLIDE_W, SLIDE_H),
        "ppt/_rels/presentation.xml.rels": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="%s/slideMaster" Target="slideMasters/slideMaster1.xml"/><Relationship Id="rId2" Type="%s/slide" Target="slides/slide1.xml"/>'
            '<Relationship Id="rId3" Type="%s/theme" Target="theme/theme1.xml"/><Relationship Id="rId4" Type="http://schemas.microsoft.com/office/2006/relationships/vbaProject" Target="vbaProject.bin"/>'
            '</Relationships>' % (R, R, R),
        "ppt/slideMasters/slideMaster1.xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldMaster %s><p:cSld><p:bg><p:bgRef idx="1001"><a:schemeClr val="bg1"/></p:bgRef></p:bg>%s</p:cSld>'
            '<p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>'
            '<p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst></p:sldMaster>' % (NS_P, sp_tree),
        "ppt/slideMasters/_rels/slideMaster1.xml.rels": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="%s/slideLayout" Target="../slideLayouts/slideLayout1.xml"/><Relationship Id="rId2" Type="%s/theme" Target="../theme/theme1.xml"/></Relationships>' % (R, R),
        "ppt/slideLayouts/slideLayout1.xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldLayout %s type="blank"><p:cSld name="Blank">%s</p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sldLayout>' % (NS_P, sp_tree),
        "ppt/slideLayouts/_rels/slideLayout1.xml.rels": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="%s/slideMaster" Target="../slideMasters/slideMaster1.xml"/></Relationships>' % R,
        "ppt/slides/slide1.xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sld %s><p:cSld>%s</p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>' % (NS_P, sp_tree.replace("</p:spTree>", text + "</p:spTree>")),
        "ppt/slides/_rels/slide1.xml.rels": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="%s/slideLayout" Target="../slideLayouts/slideLayout1.xml"/></Relationships>' % R,
        "ppt/theme/theme1.xml": theme(),
    }
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", files.pop("[Content_Types].xml"))
        for n, t in files.items(): z.writestr(n, t)
        z.writestr("ppt/vbaProject.bin", vba_project_bin())
    return buf.getvalue()

def build():
    os.makedirs(CACHE, exist_ok=True)
    tmp = PPTM + ".building"; open(tmp, "wb").write(pptm_bytes()); os.replace(tmp, PPTM)
    return dict(built=PPTM)

# ---------------------------------------------------------------- grant and check

def granted_set():
    try: return {urllib.parse.unquote(k[7:]).rstrip("/") for k in plistlib.load(open(BOOKMARKS, "rb")) if k.startswith("file://")}
    except Exception: return set()

def covered(path, have):
    p = os.path.abspath(path).rstrip("/")
    return any(p == g or p.startswith(g + "/") for g in have)

def osa(script):
    r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True, timeout=600)
    return r.returncode, (r.stdout + r.stderr).strip()

def grant(paths):
    paths = [os.path.abspath(p) for p in paths]
    missing = [p for p in paths if not os.path.exists(p)]
    if missing: return dict(error="not found", missing=missing)
    have = granted_set(); need = [p for p in paths if not covered(p, have)]
    if not need: return dict(already=paths)
    if not os.path.exists(PPTM): build()
    q = lambda s: s.replace("\\", "\\\\").replace('"', '\\"')
    name = os.path.basename(PPTM)
    code, out = osa('tell application "Microsoft PowerPoint"\nactivate\nopen POSIX file "%s"\nend tell' % q(PPTM))
    if code: return dict(error="PowerPoint did not open the access file", detail=out)
    code, out = osa('tell application "Microsoft PowerPoint" to run VB macro macro name "%s" list of parameters {"%s"}' % (MACRO, q("\n".join(need))))
    osa('tell application "Microsoft PowerPoint" to close (every presentation whose name is "%s") saving no' % q(name))
    after = granted_set()
    return dict(asked=need, granted=[p for p in need if covered(p, after)], not_granted=[p for p in need if not covered(p, after)],
                macro_result=out if code == 0 else None, error=out if code else None)

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] not in ("build", "grant", "granted"): print(__doc__); sys.exit(2)
    if a[0] == "build": res = build()
    elif a[0] == "grant": res = grant(a[1:]) if a[1:] else dict(error="name at least one folder or file")
    else:
        have = granted_set(); res = {p: covered(p, have) for p in a[1:]} if a[1:] else sorted(have)
    print(json.dumps(res, indent=1))
