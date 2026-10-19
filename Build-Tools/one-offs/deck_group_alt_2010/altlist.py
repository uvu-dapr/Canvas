"""[slide index over all slides, group name, alt] for every top-level group in a deck that has descr and is not decorative"""
import sys, re, json, zipfile, posixpath, html
def altlist(deck):
    z = zipfile.ZipFile(deck)
    pres = z.read("ppt/presentation.xml").decode(); rels = z.read("ppt/_rels/presentation.xml.rels").decode()
    tmap = {re.search(r'Id="([^"]+)"', r).group(1): re.search(r'Target="([^"]+)"', r).group(1) for r in re.findall(r"<Relationship\b[^>]*/?>", rels)}
    out = []
    for si, rid in enumerate(re.findall(r'<p:sldId\b[^>]*\br:id="([^"]+)"', pres)):
        t = tmap[rid]; sx = t.lstrip("/") if t.startswith("/") else posixpath.normpath(posixpath.join("ppt", t))
        x = z.read(sx).decode()
        for m in re.finditer(r'<p:nvGrpSpPr>\s*<p:cNvPr\b([^>]*?)(/?)>', x):
            a = m.group(1); d = re.search(r'\bdescr="([^"]*)"', a); n = re.search(r'\bname="([^"]*)"', a)
            if not d or not d.group(1).strip(): continue
            tail = x[m.end():m.end() + 1500].split("</p:cNvPr>")[0] if not m.group(2) else ""
            if re.search(r'decorative[^>]*val="1"', tail): continue
            out.append([si, html.unescape(n.group(1)), html.unescape(d.group(1))])
    return out
if __name__ == "__main__":
    json.dump(altlist(sys.argv[1]), open(sys.argv[2], "w"), indent=0); print(len(altlist(sys.argv[1])))
