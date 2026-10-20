#!/usr/bin/env python3
"""K178 2026-10-19: drop startAt="1" from numbered paragraphs that continue a list (not the first of it). Words untouched."""
import sys, os, re, zipfile, json, glob

P_RE = re.compile(r'<a:p>.*?</a:p>|<a:p/>', re.S)
TX_RE = re.compile(r'<(p|a):txBody>.*?</\1:txBody>', re.S)

def para_info(p):
    m = re.search(r'<a:pPr\b([^>]*?)(/>|>(.*?)</a:pPr>)', p, re.S)
    attrs = m.group(1) if m else ""; inner = (m.group(3) or "") if m else ""
    lv = re.search(r'\blvl="(\d+)"', attrs); lvl = int(lv.group(1)) if lv else 0
    num = re.search(r'<a:buAutoNum\b[^>]*/>', inner)
    typ = re.search(r'type="([^"]+)"', num.group(0)).group(1) if num else None
    text = "".join(re.findall(r'<a:t>([^<]*)</a:t>', p))
    return dict(lvl=lvl, num=num.group(0) if num else None, typ=typ, none=bool(re.search(r'<a:buNone', inner)), text=text)

def fix_body(body, stats):
    paras = list(P_RE.finditer(body)); out = []; last = 0
    stack = []   # recent paragraphs (info) to find the previous one at the same or lower level
    for m in paras:
        p = m.group(0); i = para_info(p); newp = p
        if i["num"] and 'startAt="1"' in i["num"]:
            prev = None
            for q in reversed(stack):
                if q["lvl"] <= i["lvl"]: prev = q; break
            if prev and prev["lvl"] == i["lvl"] and prev["typ"] == i["typ"]:
                newnum = i["num"].replace(' startAt="1"', "")
                newp = p.replace(i["num"], newnum, 1); stats["changed"] += 1
            else: stats["first"] += 1
            if prev is None and stack: stats["after_other"] += 1
        if i["text"].strip() == "" and not i["num"]: stats["empty_seen"] += 1
        stack.append(i)
        out.append(body[last:m.start()]); out.append(newp); last = m.end()
    out.append(body[last:]); return "".join(out)

def fix_xml(x, stats):
    return TX_RE.sub(lambda m: fix_body(m.group(0), stats), x)

def fix_deck(src, dst=None, dry=False):
    z = zipfile.ZipFile(src); infos = z.infolist(); stats = dict(changed=0, first=0, empty_seen=0, after_other=0, slides=[])
    new = {}
    for inf in infos:
        if re.match(r'ppt/slides/slide\d+\.xml$', inf.filename):
            x = z.read(inf).decode("utf-8"); c0 = stats["changed"]; y = fix_xml(x, stats)
            if y != x:
                # words check: the same text runs in the same order
                assert re.findall(r'<a:t>([^<]*)</a:t>', x) == re.findall(r'<a:t>([^<]*)</a:t>', y)
                assert x.replace(' startAt="1"', "") == y.replace(' startAt="1"', "")
                new[inf.filename] = y.encode("utf-8"); stats["slides"].append(int(re.search(r'(\d+)', inf.filename).group(1)))
    if dry or not new: z.close(); return stats
    dst = dst or src; tmp = dst + ".numfix"
    with zipfile.ZipFile(tmp, "w") as o:
        for inf in infos:
            b = new.get(inf.filename) or z.read(inf)
            ni = zipfile.ZipInfo(inf.filename, inf.date_time); ni.compress_type = inf.compress_type; ni.external_attr = inf.external_attr
            o.writestr(ni, b)
    z.close(); os.replace(tmp, dst); stats["slides"].sort(); return stats

if __name__ == "__main__":
    dry = "--dry" in sys.argv; args = [a for a in sys.argv[1:] if a != "--dry"]
    if args and args[0] == "--to":
        print(json.dumps(fix_deck(args[1], args[2]))); sys.exit(0)
    for f in args: print(json.dumps(dict(deck=f, **fix_deck(f, dry=dry))))
