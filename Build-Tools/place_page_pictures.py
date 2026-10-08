#!/usr/bin/env python3
"""place_page_pictures.py: put checked page pictures under their headings in a class's next package (J159, 2026-10-08).

The picture session stages pictures with a manifest (Claude outputs/Page Pictures <date>/manifest.json): file, class,
page (wiki_content file name, without the term suffix), after_heading, alt, batch. For one class this:
  1. copies each picture into the GitHub folder the page's other pictures already use (Classes/<repo>/<module>/),
  2. inserts it right after the named heading (h2 to h4), the same markup as the first 14 (K98, 2026-10-07),
  3. keeps alt text under 120 characters (Standards: first sentence, else cut at a word),
  4. records it in Build-Tools/page_picture_sources.json,
and writes a new package. Fails closed: a page or heading it can't find stops the build and names it (nothing written).

    python3 place_page_pictures.py <manifest.json> <class 2255> <package.imscc> <out.imscc> [--batch "2026-10-07 2 PM"]
"""
import sys, os, re, json, html, shutil, zipfile, collections

REPO = "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas"
RAW = "https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/"


def short_alt(a):
    a = " ".join(a.split())
    if len(a) < 120:
        return a
    first = re.split(r"(?<=[.!?])\s", a)[0]
    if len(first) < 120:
        return first.rstrip(".") + "."
    cut = a[:118].rsplit(" ", 1)[0].rstrip(",;: ")
    return cut


def main():
    man, cls, pkg, out = sys.argv[1:5]
    batch = sys.argv[sys.argv.index("--batch") + 1] if "--batch" in sys.argv else None
    assert not os.path.exists(out), "never overwrite " + out
    items = [i for i in json.load(open(man)) if str(i.get("class")) == cls and (batch is None or i.get("batch", "").startswith(batch))]
    if not items:
        sys.exit("no pictures for class %s%s" % (cls, " in batch " + batch if batch else ""))
    w = out + ".work"
    shutil.rmtree(w, ignore_errors=True)
    zipfile.ZipFile(pkg).extractall(w)
    pages = {f: os.path.join(w, "wiki_content", f) for f in os.listdir(os.path.join(w, "wiki_content"))}
    problems, done = [], []
    by_page = collections.defaultdict(list)
    for it in items:
        base = it["page"][:-5] if it["page"].endswith(".html") else it["page"]
        hit = [f for f in pages if f == base + ".html" or re.fullmatch(re.escape(base) + r"(-[a-z]\d\d)?(-\d+)?\.html", f)]
        if len(hit) != 1:
            problems.append("%s: page %s found %d times" % (it["file"], it["page"], len(hit)))
            continue
        by_page[hit[0]].append(it)
    for page, its in by_page.items():
        p = pages[page]
        t = open(p, encoding="utf8").read()
        # the GitHub folder this page's pictures already use
        folders = collections.Counter(re.findall(re.escape(RAW) + r"([^\"']+)/[^/\"']+\.(?:png|jpe?g|svg|gif)", t))
        folders = {k: v for k, v in folders.items() if "/All/" not in "/" + k + "/" and "DAPR_Canvas_Icon" not in k}
        if not folders:
            problems.append("%s: no picture folder on the page to follow" % page)
            continue
        folder = max(folders, key=folders.get)
        for it in its:
            src = os.path.join(os.path.dirname(man), it["file"])
            if not os.path.exists(src):
                problems.append("%s: file missing beside the manifest" % it["file"])
                continue
            if it["file"] in t:
                done.append("%s already on %s" % (it["file"], page))
                continue
            # the heading's words, allowing inline tags around them (<h3><strong>7.1 Surround Sound</strong></h3>)
            def heading(s):
                return re.compile(r"(<h[2-4][^>]*>\s*(?:<[^>]+>\s*)*%s\s*(?:</[^>]+>\s*)*</h[2-4]>)" % re.escape(s).replace("\\ ", r"\s+"), re.I)
            m = heading(html.escape(it["after_heading"], quote=False)).search(t) or heading(it["after_heading"]).search(t)
            if not m:
                problems.append("%s: heading \"%s\" not on %s" % (it["file"], it["after_heading"], page))
                continue
            alt = html.escape(short_alt(it["alt"]), quote=True)
            img = '\n<p style="margin: 16px 0;"><img style="max-width: 100%%; height: auto;" src="%s%s/%s" alt="%s" loading="lazy"></p>\n' % (RAW, folder, it["file"], alt)
            t = t[:m.end()] + img + t[m.end():]
            dest = os.path.join(REPO, "Classes", folder, it["file"])
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            if not os.path.exists(dest):
                shutil.copy2(src, dest)
            done.append("%s under \"%s\" on %s (%s)" % (it["file"], it["after_heading"], page, folder))
        open(p, "w", encoding="utf8").write(t)
    if problems:
        shutil.rmtree(w, ignore_errors=True)
        sys.exit("STOPPED, nothing written:\n  " + "\n  ".join(problems))
    cwd = os.getcwd(); os.chdir(w)
    os.system('zip -q -r -D -X "%s" . -x "*.DS_Store" "__MACOSX/*"' % (out + ".partial"))
    os.chdir(cwd); os.rename(out + ".partial", out); shutil.rmtree(w, ignore_errors=True)
    src_p = os.path.join(REPO, "Build-Tools/page_picture_sources.json")
    srcs = json.load(open(src_p))
    for it in items:
        srcs.setdefault(it["file"], {"src": "ChatGPT", "made": (it.get("batch") or "")[:10] or "2026-10-07", "class": cls, "page": it["page"], "checked_by": "picture session (accuracy)"})
    json.dump(srcs, open(src_p, "w"), indent=1)
    print("\n".join(done))
    print("%d placed, written %s" % (len(done), out))


if __name__ == "__main__":
    main()
