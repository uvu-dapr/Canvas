#!/usr/bin/env python3
"""Fix what Canvas's own accessibility checker flags and a build can fix without judgment (Adam, 2026-09-30).

  python3 canvas_checker_fix.py <unzipped package folder> [--dry-run] [--bold]

1. Header cells without scope ("Tables headers should specify scope"; DAPR Canvas Standards 17): a <th> in <thead>, or in
   a row made only of <th>, gets scope="col"; the first <th> of any other row gets scope="row".
3. A heading longer than 120 characters ("Headings should not contain more than 120 characters"): it is a sentence, not a
   heading, so it becomes a bold paragraph with the same words and inline style.
2. Alt text that is a file name ("Image filenames should not be used as alt text"): the alt becomes the picture's own
   file name read as words (Music_Panner_Network_Address_Menu.png -> "Music Panner Network Address Menu"). File names
   follow Standards 8.0.1 and 20.4, so they already say what the picture shows.

4. With --bold only (Adam decides, question of 2026-09-30): bold set by an inline font-weight, which Canvas removes on
   save, becomes <strong> around the same text, which Canvas keeps; a font-weight that is not bold is just removed.

Only .html files are touched (pages, assignment and discussion bodies). Nothing else changes. Prints what it fixed.
"""
import os, re, sys, html, urllib.parse

IMG_EXT = r"\.(png|jpe?g|gif|webp|svg|tiff?|heic)$"


def alt_is_file_name(a):
    t = a.strip()
    if re.search(IMG_EXT, t, re.I):
        return True
    return " " not in t and "_" in t and len(t) > 3


def words_from_file(src):
    name = os.path.basename(urllib.parse.unquote(html.unescape(src).split("?")[0]))   # Voltage%20Divider.png: words, not %20
    stem = re.sub(IMG_EXT, "", name, flags=re.I)
    stem = stem.replace("__", ": ").replace("_", " ").replace("-", " ")
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem


def fix_scopes(doc):
    n = 0
    def table(m):
        nonlocal n
        t = m.group(0)
        head = re.search(r"(?s)<thead\b.*?</thead>", t)
        def add(tag, scope):
            nonlocal n
            n += 1
            return tag[:-1].rstrip() + ' scope="%s">' % scope if not tag.endswith("/>") else tag
        def row(rm, in_head):
            r = rm.group(0)
            cells = re.findall(r"<t[hd]\b", r)
            all_th = cells and all(c == "<th" for c in cells)
            first = [True]
            def th(tm):
                tag = tm.group(0)
                if re.search(r"\bscope=", tag):
                    first[0] = False
                    return tag
                if in_head or all_th:
                    return add(tag, "col")
                if first[0]:
                    first[0] = False
                    return add(tag, "row")
                return tag
            return re.sub(r"<th\b[^>]*>", th, r)
        if head:
            h = re.sub(r"(?s)<tr\b.*?</tr>", lambda rm: row(rm, True), head.group(0))
            t = t[:head.start()] + h + t[head.end():]
            rest_start = t.find("</thead>") + len("</thead>")
            t = t[:rest_start] + re.sub(r"(?s)<tr\b.*?</tr>", lambda rm: row(rm, False), t[rest_start:])
        else:
            t = re.sub(r"(?s)<tr\b.*?</tr>", lambda rm: row(rm, False), t)
        return t
    doc = re.sub(r"(?s)<table\b.*?</table>", table, doc)
    return doc, n


def fix_alts(doc):
    n = 0
    def img(m):
        nonlocal n
        tag = m.group(0)
        a = re.search(r'\balt="([^"]*)"', tag)
        s = re.search(r'\bsrc="([^"]*)"', tag)
        if not a or not s or not alt_is_file_name(html.unescape(a.group(1))):
            return tag
        new = words_from_file(s.group(1))
        if not new or alt_is_file_name(new):
            return tag
        n += 1
        return tag[:a.start(1)] + html.escape(new, quote=True) + tag[a.end(1):]
    doc = re.sub(r"<img\b[^>]*>", img, doc)
    return doc, n


def fix_long_headings(doc):
    n = 0
    def h(m):
        nonlocal n
        attrs, inner = m.group(2), m.group(3)
        if len(html.unescape(re.sub(r"<[^>]+>", "", inner)).strip()) <= 120:
            return m.group(0)
        n += 1
        return "<p%s><strong>%s</strong></p>" % (attrs, inner)
    doc = re.sub(r"(?s)<h([1-6])(\b[^>]*)>(.*?)</h\1>", h, doc)
    return doc, n


def fix_heading_skips(doc):
    """No heading may skip a level (h3 then h5): a long heading made a paragraph can leave one (2026-10-01, 3340 v71).
    Each heading is at most one level below the one before it; its text and style stay."""
    n = 0
    prev = [1]
    def h(m):
        nonlocal n
        lvl = int(m.group(1))
        new = min(lvl, prev[0] + 1)
        prev[0] = new
        if new == lvl: return m.group(0)
        n += 1
        return "<h%d%s>%s</h%d>" % (new, m.group(2), m.group(3), new)
    doc = re.sub(r"(?s)<h([1-6])(\b[^>]*)>(.*?)</h\1>", h, doc)
    return doc, n


COPY_LINE = "Click once anywhere in the gray box, then press Command C to copy."

def fix_worksheet_blocks(doc):
    """The one-click worksheet block (DAPR Canvas Standards 11b), made to the house format without touching its words:
    no border (it travels into Word), user-select and -webkit-user-select all, cursor pointer, an <hr> directly above
    and below, and the copy instruction above it (2026-10-01: 15 exercises in 3340 v71)."""
    n = 0
    out, pos = [], 0
    for m in re.finditer(r'<(div|section|p)\b([^>]*style="([^"]*user-select\s*:\s*all[^"]*)"[^>]*)>', doc, re.I):
        if m.start() < pos: continue
        tag = m.group(1).lower()
        depth, i, end = 1, m.end(), None
        for t in re.finditer(r"</?%s\b[^>]*>" % tag, doc[m.end():], re.I):
            depth += -1 if t.group(0).startswith("</") else 1
            if depth == 0: end = m.end() + t.end(); break
        if end is None: continue
        style = m.group(3)
        new = re.sub(r"(?:^|;)\s*border\s*:[^;]*", "", style).strip(" ;")
        for want in ("-webkit-user-select:all", "cursor:pointer"):
            if want.split(":")[0] not in new.replace(" ", ""): new += "; " + want
        opentag = m.group(0).replace('style="%s"' % style, 'style="%s"' % new.strip(" ;"))
        before = doc[pos:m.start()]
        changed = opentag != m.group(0)
        tail = before.rstrip()
        if COPY_LINE.lower() not in doc.lower():
            before = tail + "\n<p>%s</p>\n" % COPY_LINE; tail = before.rstrip(); changed = True
        if not re.search(r"<hr\b[^>]*>\s*(?:<p>[^<]*</p>\s*)?$", tail, re.I):
            before = tail + "\n<hr>\n"; changed = True
        block = opentag + doc[m.end():end]
        after_start = end
        if not re.match(r"\s*<hr\b", doc[end:end + 40], re.I):
            block += "\n<hr>"; changed = True
        out.append(before + block); pos = after_start
        if changed: n += 1
    out.append(doc[pos:])
    return "".join(out), n


BOLD = re.compile(r"font-weight\s*:\s*(bold|bolder|[6-9]00)\s*;?", re.I)
ANY_WEIGHT = re.compile(r"font-weight\s*:\s*[^;\"]*;?", re.I)


def fix_bold(doc):
    n = 0
    def el(m):
        nonlocal n
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        style = re.search(r'style="([^"]*)"', attrs)
        if not style or "font-weight" not in style.group(1).lower():
            return m.group(0)
        if re.search(r"<%s\b" % tag, inner, re.I):
            return m.group(0)          # nested same tag: leave it (rare), the Report still lists it
        bold = BOLD.search(style.group(1)) is not None
        new_style = ANY_WEIGHT.sub("", style.group(1)).strip().rstrip(";").strip()
        new_attrs = attrs.replace(style.group(0), 'style="%s"' % new_style if new_style else "").replace("  ", " ").rstrip()
        n += 1
        body = "<strong>%s</strong>" % inner if bold and inner.strip() and not inner.strip().lower().startswith("<strong") else inner
        return "<%s%s>%s</%s>" % (tag, new_attrs, body, tag)
    for tag in ("span", "a", "p", "li", "td", "th", "div", "h2", "h3", "h4", "em", "strong", "caption", "summary"):
        doc = re.sub(r"(?is)<(%s)(\b[^>]*)>(.*?)</\1>" % tag, el, doc)
    return doc, n


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    root, dry, bold = sys.argv[1], "--dry-run" in sys.argv, "--bold" in sys.argv
    bolds = 0
    scopes = alts = files = heads = worksheets = 0
    for d, _, fs in os.walk(root):
        for f in fs:
            if not f.endswith(".html"):
                continue
            p = os.path.join(d, f)
            doc = open(p, encoding="utf-8").read()
            new, a = fix_alts(doc)
            new, s = fix_scopes(new)
            new, hd = fix_long_headings(new)
            new, sk = fix_heading_skips(new); hd += sk
            new, wb = fix_worksheet_blocks(new); worksheets += wb
            if bold:
                new, b = fix_bold(new); bolds += b
            if new != doc:
                files += 1; scopes += s; alts += a; heads += hd
                print("%s: %d scope, %d alt, %d long heading" % (os.path.relpath(p, root), s, a, hd))
                if not dry:
                    open(p, "w", encoding="utf-8").write(new)
    print("RESULT: %d file(s), %d header cell(s) given scope, %d file-name alt text(s) rewritten, %d long heading(s) made bold paragraphs, %d worksheet block(s) made one-click%s%s" % (files, scopes, alts, heads, worksheets, (", %d font-weight(s) made <strong>" % bolds) if bold else "", " (dry run)" if dry else ""))


if __name__ == "__main__":
    main()
