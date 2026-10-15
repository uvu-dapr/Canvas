#!/usr/bin/env python3
"""Picture weight check for a Canvas package (preflight gate 12u, J309, Adam 2026-10-15).

The 2026-10-15 Canvas Size Audit found a 1.77 MB PNG in the Spring 2000 Template and 7 MB of oversized question bank
pictures copied into every class; no gate looked at picture weight or pixel size. This one does, for every picture
under web_resources/:

  RED     WebP, GIF or SVG file             Standards 20.2: "Never SVG, WebP, GIF" (convert to PNG or JPEG)
  RED     JPEG over 500 KB, PNG over 1 MB   Standards 20.3 weight budget
  YELLOW  page picture, long edge over 1600 px      Standards 20.3 (full width page figure is 1600 px)
  YELLOW  quiz or bank picture, long edge over 1200 px
          (our choice, not a Standards number: the 20.3 overlay size, enough for a question in the quiz column)

A picture is a quiz picture when it sits in assessment_questions/ or only quizzes and banks (.qti, assessment_qti.xml)
name it; otherwise it is a page picture. Pixel sizes are read from the file header (no Pillow on this Mac).

    python3 picture_weight.py <package.imscc | unzipped folder>     # one line per finding, then the counts
"""
import html, os, re, struct, sys, urllib.parse, zipfile

PICS = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.bmp', '.tif', '.tiff')
BANNED = ('.webp', '.gif', '.svg')
JPEG_MAX, PNG_MAX = 500 * 1024, 1024 * 1024
PAGE_PX, QUIZ_PX = 1600, 1200
TEXT = ('.html', '.htm', '.xml', '.qti')


def size_px(b):
    """(width, height) from a PNG, JPEG, GIF or WebP header, or None"""
    try:
        if b[:8] == b'\x89PNG\r\n\x1a\n':
            return struct.unpack('>II', b[16:24])
        if b[:6] in (b'GIF87a', b'GIF89a'):
            return struct.unpack('<HH', b[6:10])
        if b[:4] == b'RIFF' and b[8:12] == b'WEBP':
            k = b[12:16]
            if k == b'VP8X':
                return (int.from_bytes(b[24:27], 'little') + 1, int.from_bytes(b[27:30], 'little') + 1)
            if k == b'VP8L':
                v = int.from_bytes(b[21:25], 'little')
                return ((v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1)
            if k == b'VP8 ':
                w, h = struct.unpack('<HH', b[26:30])
                return (w & 0x3FFF, h & 0x3FFF)
        if b[:2] == b'\xff\xd8':
            i = 2
            while i < len(b) - 9:
                if b[i] != 0xFF:
                    i += 1; continue
                m = b[i + 1]
                if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    h, w = struct.unpack('>HH', b[i + 5:i + 9])
                    return (w, h)
                if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                    i += 2; continue
                i += 2 + struct.unpack('>H', b[i + 2:i + 4])[0]
    except Exception:
        pass
    return None


def _entries(src):
    if os.path.isdir(src):
        out = {}
        for d, _, fs in os.walk(src):
            for f in fs:
                if not f.startswith('.'):
                    p = os.path.join(d, f)
                    out[os.path.relpath(p, src).replace(os.sep, '/')] = (lambda p=p: open(p, 'rb').read())
        return out
    z = zipfile.ZipFile(src)
    return {n: (lambda n=n: z.read(n)) for n in z.namelist() if not n.endswith('/')}


def check(src):
    """[(level, path, why)] with level 'red' or 'yellow', for every picture over a rule"""
    ent = _entries(src)
    pics = [n for n in ent if n.startswith('web_resources/') and n.lower().endswith(PICS)]
    if not pics:
        return []
    page_text, quiz_text = [], []
    for n, rd in ent.items():
        if n == 'imsmanifest.xml' or n.startswith('web_resources/') or not n.lower().endswith(TEXT):
            continue
        t = urllib.parse.unquote(html.unescape(rd().decode('utf-8', 'ignore')))
        (quiz_text if n.endswith('.qti') or n.endswith('assessment_qti.xml') or n.startswith('non_cc_assessments/') else page_text).append(t)
    page_text, quiz_text = '\n'.join(page_text), '\n'.join(quiz_text)
    out = []
    for n in sorted(pics):
        rel = n[len('web_resources/'):]
        ext = os.path.splitext(n)[1].lower()
        b = ent[n]()
        kb = len(b) / 1024
        in_page = ('/' + rel) in page_text
        quiz = rel.startswith('assessment_questions/') or (('/' + rel) in quiz_text and not in_page)
        px = size_px(b)
        if ext in BANNED:
            out.append(('red', rel, '%s is never allowed (Standards 20.2): convert to PNG (diagram, screenshot) or JPEG (photo)' % ext[1:].upper()))
        if ext in ('.jpg', '.jpeg') and len(b) > JPEG_MAX:
            out.append(('red', rel, 'JPEG %.0f KB, over the 500 KB budget (Standards 20.3)' % kb))
        if ext == '.png' and len(b) > PNG_MAX:
            out.append(('red', rel, 'PNG %.2f MB, over the 1 MB budget (Standards 20.3)' % (len(b) / 1048576)))
        if px and ext != '.svg':
            lim = QUIZ_PX if quiz else PAGE_PX
            if max(px) > lim:
                out.append(('yellow', rel, '%s picture %d x %d px, long edge over %d px (%s)' % ('quiz' if quiz else 'page', px[0], px[1], lim,
                            'our quiz size: the 20.3 overlay width' if quiz else 'Standards 20.3')))
    return out


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    r = check(sys.argv[1])
    for lv, p, why in r:
        print('%-6s %s: %s' % (lv.upper(), p, why))
    print('12u picture weight: %d red, %d yellow' % (sum(1 for x in r if x[0] == 'red'), sum(1 for x in r if x[0] == 'yellow')))
    sys.exit(1 if any(x[0] == 'red' for x in r) else 0)
