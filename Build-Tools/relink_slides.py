#!/usr/bin/env python3
"""
relink_slides.py: a package's slide PDF links brought up to the decks in Canvas Links (Adam, 2026-09-30).

After decks become Linked and Embedded pairs, lose banned parts of their names, or merge with a twin, a package still
links the old PDFs. This reads the course's Presentations folders and, in a copy of the package:
  renamed   a link to X.pdf, where X became <Base> (Presentations/Archive holds "X (before Linked and Embedded ...)"),
            points at <Base>.pdf; the item and page link titles follow
  merged    a link to the older deck of a merged pair ("X (before merge ...)" in Archive, and no current X deck) is
            removed: the module item, its web link, its manifest entries and any page download link
  added     a current deck whose PDF no package item links gets an item "<Topic>: Slides - <Title> (PDF)" beside the
            module's other Slides items (Standards 8), UNPUBLISHED: Adam publishes new items himself (2026-09-30)
Nothing else changes. Items keep their identifiers, so a LIVE-Import updates them in place; a removed item stays in the
live course until deleted by hand (the step page lists it).

    python3 relink_slides.py <package.imscc> <out.imscc> [--live <live export>] [--dry] [--keep-unlinked=Base,...]

With --live, every module or item the live course does not already have is set unpublished; without it (a template),
every link, tool and file item is. Preflight gate 12m checks it.
"""
import sys, os, re, zipfile, hashlib, json, html, glob, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_names import deck_base

CL = "/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links"
BASE_URL = "https://uvu-files.adamo.workers.dev/"

def readable(base):
    return base.replace("__", ": ").replace("-", " - ").replace("_", " ").replace("  ", " ")

def course_folder(pkg):
    code = re.search(r"(?i)dapr[- _]?(\d{4})", os.path.basename(pkg)).group(1)
    return [d for d in os.listdir(CL) if d.startswith("DAPR-%s" % code)][0]

def state(cf):
    """current pair bases by module folder, and what each archived name became"""
    cur = {}; renamed = {}; merged = set()
    for L in glob.glob("%s/%s/*/Presentations/*-Linked.pptx" % (CL, cf)):
        mod = L.split("/")[-3]; cur.setdefault(mod, set()).add(os.path.basename(L)[:-12])
    for A in glob.glob("%s/%s/*/Presentations/Archive/*.pptx" % (CL, cf)):
        mod = A.split("/")[-4]; n = os.path.basename(A)[:-5]
        m = re.match(r"(.+) \(before (Linked and Embedded|merge) \d{4}-\d\d-\d\d\)$", n)
        if not m: continue
        x, why = m.group(1), m.group(2)
        if x in cur.get(mod, set()): continue
        if why == "merge": merged.add((mod, x))
        elif deck_base(x) in cur.get(mod, set()): renamed[(mod, x)] = deck_base(x)
    return cur, renamed, merged

def live_ids(export):
    """Everything the live course already has: the export's identifiers and the ids Canvas stored (match_ids.py)"""
    z = zipfile.ZipFile(export)
    ids = set(re.findall(r'identifier="([^"]+)"', z.read("imsmanifest.xml").decode("utf-8", "ignore")))
    try:
        import match_ids
        _, lv, _ = match_ids.lineage(export, [match_ids.class_folder(export)])
        ids |= {v["stored"] for v in lv.values() if v.get("stored")}
    except Exception:
        pass
    return ids

def unpublish_new(meta, live):
    """New modules and module items arrive unpublished (Adam, 2026-09-30: "they should all be inactive so I can make them
    live myself"). With a live export: whatever Canvas does not already have. Without one (a template): every link,
    tool and file item. Returns the new module_meta and what changed."""
    changed = []
    def item(m):
        iid, body = m.group(1), m.group(2)
        ct = (re.search(r"<content_type>([^<]*)</content_type>", body) or [0, ""])[1]
        new = (iid not in live) if live is not None else ct in ("ExternalUrl", "ExternalTool", "Attachment")
        if new and "<workflow_state>active</workflow_state>" in body:
            changed.append(html.unescape((re.search(r"<title>([^<]*)</title>", body) or [0, iid])[1]))
            body = body.replace("<workflow_state>active</workflow_state>", "<workflow_state>unpublished</workflow_state>", 1)
        return '<item identifier="%s">%s</item>' % (iid, body)
    meta = re.sub(r'(?s)<item identifier="([^"]+)">(.*?)</item>', item, meta)
    if live is not None:
        def module(m):
            mid, body = m.group(1), m.group(2)
            head, sep, rest = body.partition("<items>")
            if mid not in live and "<workflow_state>active</workflow_state>" in head:
                changed.append("module " + html.unescape((re.search(r"<title>([^<]*)</title>", head) or [0, mid])[1]))
                head = head.replace("<workflow_state>active</workflow_state>", "<workflow_state>unpublished</workflow_state>", 1)
            return '<module identifier="%s">%s%s%s' % (mid, head, sep, rest)
        meta = re.sub(r'(?s)<module identifier="([^"]+)">(.*?)(?=<module identifier=|</modules>)', lambda m: module(m), meta)
    return meta, changed

def relink(pkg, out, dry=False, keep_unlinked=(), live_export=None):
    cf = course_folder(pkg); cur, renamed, merged = state(cf)
    z = zipfile.ZipFile(pkg); infos = z.infolist(); data = {i.filename: z.read(i.filename) for i in infos}
    meta = data["course_settings/module_meta.xml"].decode("utf-8"); man = data["imsmanifest.xml"].decode("utf-8")
    pdf_re = re.compile(re.escape(BASE_URL + cf) + r"/([^/\"<>]+)/Presentations/PDF/([^\"<>/]+)\.pdf")
    report = dict(package=os.path.basename(pkg), renamed=[], removed=[], added=[], unresolved=[])
    # 1. renames and removals, item by item
    for item in re.findall(r"(?s)<item identifier=\"[^\"]+\">(?:(?!</item>).)*?<content_type>ExternalUrl</content_type>.*?</item>", meta):
        u = re.search(r"<url>([^<]+)</url>", item)
        m = pdf_re.search(html.unescape(u.group(1))) if u else None
        if not m: continue
        mod, x = m.group(1), urllib.parse.unquote(m.group(2))
        if x in cur.get(mod, set()): continue
        ref = re.search(r"<identifierref>([^<]+)</identifierref>", item).group(1)
        title = html.unescape(re.search(r"<title>([^<]*)</title>", item).group(1))
        if (mod, x) in renamed:
            new = renamed[(mod, x)]
            new_title = title.replace(readable(x), readable(new)) if readable(x) in title else re.sub(r"Slides( - [^(]+)? \(PDF\)$", "Slides - %s (PDF)" % readable(new), title)
            old_url = BASE_URL + "%s/%s/Presentations/PDF/%s.pdf" % (cf, mod, x); new_url = BASE_URL + "%s/%s/Presentations/PDF/%s.pdf" % (cf, mod, new)
            for n in list(data):
                if n.endswith((".xml", ".html")):
                    t = data[n].decode("utf-8")
                    t2 = t.replace(old_url, new_url).replace(html.escape(title, quote=False), html.escape(new_title, quote=False)).replace("Download: %s (PDF" % readable(x), "Download: %s (PDF" % readable(new))
                    if t2 != t: data[n] = t2.encode("utf-8")
            report["renamed"].append(dict(item=title, to=new_title, pdf="%s.pdf -> %s.pdf" % (x, new)))
        elif (mod, x) in merged:
            meta2 = data["course_settings/module_meta.xml"].decode("utf-8")
            data["course_settings/module_meta.xml"] = meta2.replace(item, "").encode("utf-8")
            man2 = data["imsmanifest.xml"].decode("utf-8")
            man2 = re.sub(r"(?s)<item identifier=\"[^\"]+\" identifierref=\"%s\">.*?</item>\s*" % re.escape(ref), "", man2)
            man2 = re.sub(r"(?s)<resource identifier=\"%s\"[^>]*>.*?</resource>\s*|<resource identifier=\"%s\"[^>]*/>\s*" % (re.escape(ref), re.escape(ref)), "", man2)
            data["imsmanifest.xml"] = man2.encode("utf-8")
            data.pop("web_links/%s.xml" % ref, None)
            old_url = BASE_URL + "%s/%s/Presentations/PDF/%s.pdf" % (cf, mod, x)
            for n in list(data):
                if n.endswith(".html"):
                    t = data[n].decode("utf-8")
                    t2 = re.sub(r"(?s)<p>(?:(?!</p>).)*?%s.*?</p>\s*" % re.escape(old_url), "", t)
                    if t2 != t: data[n] = t2.encode("utf-8")
            report["removed"].append(dict(item=title, pdf=x + ".pdf", identifier=re.search(r'identifier="([^"]+)"', item).group(1)))
        else:
            report["unresolved"].append(dict(item=title, pdf=x + ".pdf"))
    # 2. current decks nothing links: a new item beside the module's Slides items
    meta = data["course_settings/module_meta.xml"].decode("utf-8")
    linked = set(urllib.parse.unquote(m.group(1)) + "/" + urllib.parse.unquote(m.group(2)) for m in pdf_re.finditer(html.unescape(meta)))
    modules = re.findall(r"(?s)<module identifier=\"([^\"]+)\">(.*?)</module>", meta)
    def folder(title):
        t = re.sub(r"^\s*(M\d+[a-z]?\s*[:\-_]|Week\s*\d+\s*-)\s*", "", title, flags=re.I)
        t = re.sub(r"\s*\((Weeks?[^)]*|Finals Week|[^)]*%[^)]*|\d+\s*pts?)\)\s*$", "", t, flags=re.I)
        t = t.replace("%", "").replace("&", "and").replace(",", "").replace("'", "").replace("’", "")
        t = t.replace(":", "__").replace("/", "-").replace(" ", "_")
        return re.sub(r"_{3,}", "__", t)
    for mod, bases in sorted(cur.items()):
        for b in sorted(bases):
            if "%s/%s" % (mod, b) in linked or b in keep_unlinked: continue
            hit = [(mid, body) for mid, body in modules if folder(html.unescape(re.search(r"<title>([^<]*)</title>", body).group(1))) == mod]
            if not hit: report["unresolved"].append(dict(item="(no module for %s)" % mod, pdf=b + ".pdf")); continue
            mid, body = hit[0]
            mtitle = html.unescape(re.search(r"<title>([^<]*)</title>", body).group(1))
            topic = mtitle.split(":")[0].strip()
            title = "%s: Slides - %s (PDF)" % (topic, readable(b))
            url = BASE_URL + "%s/%s/Presentations/PDF/%s.pdf" % (cf, mod, urllib.parse.quote(b))
            ident = "g" + hashlib.md5(("slides " + url).encode()).hexdigest(); ref = "g" + hashlib.md5(("weblink " + url).encode()).hexdigest()
            items = list(re.finditer(r"(?s)<item identifier=\"[^\"]+\">.*?</item>", body))
            slides = [m for m in items if "Slides" in m.group(0) and "ExternalUrl" in m.group(0)]
            after = (slides or items or [None])[-1]
            pos = int(re.search(r"<position>(\d+)</position>", after.group(0)).group(1)) + 1 if after else 1
            new_item = ('<item identifier="%s">\n        <content_type>ExternalUrl</content_type>\n        <workflow_state>unpublished</workflow_state>\n        <title>%s</title>\n'
                        '        <identifierref>%s</identifierref>\n        <url>%s</url>\n        <position>%d</position>\n        <new_tab>true</new_tab>\n        <indent>0</indent>\n        <link_settings_json>null</link_settings_json>\n      </item>') % (ident, html.escape(title, quote=False), ref, url, pos)
            # later items move down one
            body2 = re.sub(r"<position>(\d+)</position>", lambda m: "<position>%d</position>" % (int(m.group(1)) + (1 if int(m.group(1)) >= pos else 0)), body)
            if after:
                a2 = re.sub(r"<position>(\d+)</position>", lambda m: "<position>%d</position>" % (int(m.group(1)) + (1 if int(m.group(1)) >= pos else 0)), after.group(0))
                body2 = body2.replace(a2, a2 + "\n      " + new_item, 1)
            else:
                body2 = re.sub(r"<items>\s*</items>|<items/>", "<items>\n      %s\n    </items>" % new_item, body2, count=1)
            meta = meta.replace(body, body2, 1); modules = [(i2, body2 if i2 == mid else bb) for i2, bb in modules]
            data["web_links/%s.xml" % ref] = ('<?xml version="1.0" encoding="UTF-8"?>\n<webLink xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imswl_v1p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
                'xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imswl_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imswl_v1p1.xsd">\n  <title>%s</title>\n  <url href="%s"/>\n</webLink>\n' % (html.escape(title, quote=False), url)).encode("utf-8")
            man = data["imsmanifest.xml"].decode("utf-8")
            man = man.replace("</resources>", '  <resource identifier="%s" type="imswl_xmlv1p1" href="web_links/%s.xml">\n      <file href="web_links/%s.xml"/>\n    </resource>\n  </resources>' % (ref, ref, ref), 1)
            # the organization tree: the new item goes into its module's entry
            mm = re.search(r'(<item identifier="%s">\s*<title>[^<]*</title>)' % re.escape(mid), man)
            if mm: man = man.replace(mm.group(1), mm.group(1) + '\n        <item identifier="%s" identifierref="%s">\n          <title>%s</title>\n        </item>' % (ident, ref, html.escape(title, quote=False)), 1)
            data["imsmanifest.xml"] = man.encode("utf-8")
            report["added"].append(dict(item=title, module=mtitle, position=pos))
    meta, report["unpublished"] = unpublish_new(meta, live_ids(live_export) if live_export else None)
    data["course_settings/module_meta.xml"] = meta.encode("utf-8")
    if not dry:
        if os.path.exists(out): raise SystemExit("exists, not overwritten: " + out)
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as o:
            done = set()
            for i in infos:
                if i.filename in data: o.writestr(i, data[i.filename]); done.add(i.filename)
            for n in data:
                if n not in done: o.writestr(n, data[n])
    return report

if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 2: print(__doc__); sys.exit(2)
    keep = next((x.split("=", 1)[1].split(",") for x in a if x.startswith("--keep-unlinked=")), [])
    live = a[a.index("--live") + 1] if "--live" in a else None
    print(json.dumps(relink(a[0], a[1], "--dry" in a, keep, live), indent=1))
