#!/usr/bin/env python3
"""canvas_files_cleanup.py: what to delete in Canvas so each class's export is as small as it can be.

Adam, 2026-10-05: "nothing should be more than 100 MB for a canvas export. Give me what I need to clean up online ...
All file use should be put on cloudflare ... [quiz images stay: they cannot be on Cloudflare or GitHub]".

A Canvas export carries every file in the course's Files, used or not. For each class's newest export this sorts every
file into:
  quiz      used by a quiz question: stays in Canvas Files (quizzes block outside images, Standards 8.1)
  live      used by a page, assignment or discussion students reach (in a module): moves to Cloudflare, the page is
            pasted with the Cloudflare address, then the Canvas file is deleted
  oldcopy   used only by old copies (pages in no module, unpublished leftovers): delete those pages, then the file
  unused    used by nothing: delete
Blueprint pages (modules titled "(Unified Class Content)") are fixed once in the Blueprint and Synced (Adam, 2026-10-05:
"just give me the blueprint course and then I'll push it to everything else").

  python3 canvas_files_cleanup.py <out.html> <export.imscc>=<Course_Folder>=<course id> ... [--copy]

--copy puts the live files into the local Cloudflare Canvas Links folder (Adam uploads with rclone, never this tool).
"""
import zipfile, sys, re, urllib.parse, html, collections, os, json, shutil, datetime

CF = "/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links"
CF_URL = "https://uvu-files.adamo.workers.dev/"
BLUEPRINT_ID = 655823
CANVAS = "https://uvu.instructure.com/courses/%d/"


def BLUEPRINT_EXPORT():
    """the Blueprint's newest full export (Universal Class Content), for its own page addresses"""
    d = "/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses/Universal Class Content/Canvas/Canvas Templates/-Canvas Entire Course"
    fs = [os.path.join(d, f) for f in os.listdir(d) if f.endswith(".imscc") and "blu" in f.lower() and "LIVE" not in f]
    full = [f for f in fs if os.path.getsize(f) > 50e6] or fs   # a full export, not a small LIVE-Add package
    return max(full, key=os.path.getmtime)


def cf_name(base):
    """Standards 8.0.1 file names: spaces to underscores, ' - ' to '-', & to and"""
    n = base.replace(" - ", "-").replace("&", "and").replace(" ", "_")
    return re.sub(r"_+", "_", n).replace("_.", ".")


def read(exp):
    z = zipfile.ZipFile(exp)
    names = z.namelist()
    files = {i.filename[len("web_resources/"):]: i.file_size for i in z.infolist()
             if i.filename.startswith("web_resources/") and not i.filename.endswith("/")}
    mm = z.read("course_settings/module_meta.xml").decode("utf8", "ignore")
    inmod = {}
    for m in re.finditer(r'<module identifier="[^"]+">\s*<title>(.*?)</title>(.*?)</module>', mm, re.S):
        for it in re.finditer(r"<item identifier=\"[^\"]+\">(.*?)</item>", m.group(2), re.S):
            r = re.search(r"<identifierref>(.*?)</identifierref>", it.group(1))
            if r:
                inmod.setdefault(r.group(1), []).append(html.unescape(m.group(1)))
    man = z.read("imsmanifest.xml").decode("utf8", "ignore")
    res_of = {}
    for m in re.finditer(r'<resource identifier="([^"]+)"[^>]*href="([^"]+)"', man):
        res_of[m.group(2)] = m.group(1)
    docs = []
    for n in names:
        if n.startswith(("web_resources/", "course_settings/")) or not n.endswith((".html", ".xml", ".qti")):
            continue
        t = z.read(n).decode("utf8", "ignore")
        if "IMS-CC-FILEBASE" not in t:
            continue
        quiz = n.endswith(".qti") or "assessment" in n
        m = re.search(r"<title>(.*?)</title>", t, re.S)
        title = html.unescape(m.group(1)).strip() if m else n
        rid = res_of.get(n) or n.split("/")[-1].split(".")[0]
        if rid not in inmod and "/" in n and n.split("/")[0] in inmod:
            rid = n.split("/")[0]
        m = re.search(r'name="workflow_state" content="(\w+)"', t) or re.search(r"<workflow_state>(\w+)</workflow_state>", t)
        pub = m.group(1) if m else None
        kind = "quiz" if quiz else "page" if n.startswith("wiki_content/") else "assignment" if "assignment" in t[:4000] else "discussion" if "topic" in t[:2000] else "item"
        docs.append(dict(path=n, quiz=quiz, title=title, text=t, mods=inmod.get(rid, []), pub=pub, kind=kind,
                         slug=n[len("wiki_content/"):-5] if n.startswith("wiki_content/") else None))
    return z, files, docs


def pats(rel):
    enc = urllib.parse.quote(rel, safe="/()'!*,;=&+@:")
    return {rel, enc, enc.replace("%20", "+"), html.escape(rel), urllib.parse.quote(rel, safe="/")}


def classify(files, docs):
    rows = []
    for rel, size in files.items():
        p = pats(rel)
        users = [d for d in docs if any(("IMS-CC-FILEBASE$/" + q) in d["text"] for q in p)]
        placed = [d for d in users if d["mods"]]
        staff = placed and all(all("Instructor Use Only" in m for m in d["mods"]) for d in placed)   # students never see it
        # Canvas keeps quiz question pictures in assessment_questions (and a quiz may name them by id, not path)
        if rel.startswith("assessment_questions/") or (users and all(u["quiz"] for u in users)):
            k = "quiz"
        elif not users:
            k = "unused"
        elif not placed:
            k = "oldcopy"
        elif all(u["quiz"] for u in placed):
            k = "quiz"
        elif staff:
            k = "staff"
        else:
            k = "live"
        bp = bool(placed) and all(any("Unified Class Content" in m for m in u["mods"]) for u in placed if not u["quiz"])
        rows.append(dict(file=rel, bytes=size, kind=k, users=users, blueprint=bp and k == "live"))
    rows.sort(key=lambda r: -r["bytes"])
    return rows


def fixed_html(doc, mapping):
    """the page body with every moved file pointed at Cloudflare, or None when other Canvas file links remain"""
    t = doc["text"]
    body = re.search(r"<body[^>]*>(.*)</body>", t, re.S)
    b = body.group(1) if body else t
    for rel, url in mapping.items():
        for q in sorted(pats(rel), key=len, reverse=True):
            b = re.sub(re.escape("$IMS-CC-FILEBASE$/" + q) + r'(\?[^"\']*)?', url, b)
    # course links work in the Blueprint and Sync rewrites them for each class
    b = re.sub(r"\$WIKI_REFERENCE\$/pages/", "/courses/%d/pages/" % BLUEPRINT_ID, b)
    # no en or em dashes in pasted HTML (All AI Projects 1): ranges read "1 and 2", a spaced dash a colon, an em dash a comma
    b = re.sub(r"(\d)\s*[\u2013\u2014]\s*(\d)", r"\1 and \2", b)
    b = re.sub(r"\s+[\u2013\u2014]\s+", ": ", b)
    b = re.sub(r"\s*\u2014\s*", ", ", b).replace("\u2013", "-").replace(" -- ", ": ")
    left = re.findall(r"\$(?:IMS-CC-FILEBASE|CANVAS_[A-Z_]+|WIKI_REFERENCE)\$[^\"'<\s]*", b)
    return b.strip(), left


def mb(n):
    return "%.1f MB" % (n / 1e6) if n >= 1e5 else "%.0f KB" % (n / 1e3)


def esc(s):
    return html.escape(str(s), quote=True)


def main():
    out = sys.argv[1]
    copy = "--copy" in sys.argv
    specs = [a.split("=") for a in sys.argv[2:] if a.count("=") == 2]
    bp_rows, bp_docs, sections, nav, totals = {}, {}, [], [], []
    for exp, course_folder, cid in specs:
        cid = int(cid)
        z, files, docs = read(exp)
        rows = classify(files, docs)
        whole = sum(i.file_size for i in z.infolist())
        cls = re.search(r"dapr-(\d{4})", os.path.basename(exp)).group(1)
        by = collections.defaultdict(int)
        for r in rows:
            by[r["kind"]] += r["bytes"]
        after = whole - by["unused"] - by["oldcopy"] - by["live"]
        totals.append((cls, whole, after))
        # Blueprint files: gathered once, from the first class that has them
        for r in rows:
            if r["blueprint"] and r["file"] not in bp_rows:
                bp_rows[r["file"]] = (r, z)
                for u in r["users"]:
                    if u["mods"] and not u["quiz"]:
                        bp_docs.setdefault(u["path"], u)
        # old pages: in no module, holding files nothing else uses
        old = collections.OrderedDict()
        for r in rows:
            if r["kind"] != "oldcopy":
                continue
            for u in r["users"]:
                o = old.setdefault(u["path"], dict(u=u, bytes=0, n=0))
                o["bytes"] += r["bytes"]; o["n"] += 1
        old = sorted(old.values(), key=lambda o: -o["bytes"])
        # files to delete, by folder: a folder whose every file goes is deleted whole
        gone = [r for r in rows if r["kind"] in ("unused", "oldcopy") or (r["kind"] == "live" and r["blueprint"])]
        allin = collections.defaultdict(list)
        for r in rows:
            allin[os.path.dirname(r["file"]) or "(top)"].append(r)
        folders = collections.defaultdict(list)
        for r in gone:
            folders[os.path.dirname(r["file"]) or "(top)"].append(r)
        h = ["<section id='c%s'><h2>DAPR %s <small>%s now, about %s after</small></h2>" % (cls, cls, mb(whole), mb(after))]
        h.append("<p class='mut'>From <b>%s</b>. Quiz pictures stay (%s): quizzes cannot show pictures from Cloudflare or GitHub (Standards 8.1).</p>"
                 % (esc(os.path.basename(exp)), mb(by["quiz"])))
        # step 1: old pages
        if old:
            step = 1
            h.append("<h3>1. Delete these old pages (%d)</h3><p class='mut'>They are in no module: old copies from earlier imports. Students can still find the published ones from Pages. "
                     "Open each one, then <b>&#8942; (Options) ▸ Delete</b>. The files only they use go in step 2.</p><ul>" % len(old))
            for o in old:
                u = o["u"]
                link = CANVAS % cid + ("pages/" + u["slug"] if u["slug"] else "assignments" if u["kind"] == "assignment" else "discussion_topics" if u["kind"] == "discussion" else "pages")
                h.append("<li class='row' data-id='%s|old|%s'><label><input type='checkbox'> <b>%s</b></label> <span class='mut'>%s · %s · %d file(s), %s</span> "
                         "<a class='go' href='%s' target='_blank'>Open in Canvas</a></li>"
                         % (cls, esc(u["path"]), esc(u["title"]), esc(u["kind"]), "published" if u["pub"] in ("active", "published") else "unpublished", o["n"], mb(o["bytes"]), esc(link)))
            h.append("</ul>")
        # step 2: files
        n = 2 if old else 1
        h.append("<h3>%d. Delete these files in Files</h3>" % n + "<p class='mut'>Open <a class='go' href='%sfiles' target='_blank'>Files in Canvas</a>, open each folder, tick the files (or the whole folder where it says so), then the trash can. "
                 "Do the Blueprint section first for the BOAA screenshots: after you Sync, check they are gone here too.</p>" % (CANVAS % cid))
        if not folders:
            h.append("<p><b>Nothing to delete:</b> every file here is used by a quiz or by live work.</p>")
        for f, rs in sorted(folders.items(), key=lambda x: -sum(r["bytes"] for r in x[1])):
            whole_folder = len(rs) == len(allin[f])
            size = sum(r["bytes"] for r in rs)
            h.append("<div class='fold'><label><input type='checkbox' data-id='%s|f|%s'> <b>%s</b></label> <span class='mut'>%s, %d file(s)%s</span>"
                     % (cls, esc(f), esc(f), mb(size), len(rs), " · <b>delete the whole folder</b>" if whole_folder else ""))
            if not whole_folder:
                h.append("<ul class='files'>" + "".join("<li>%s <span class='mut'>%s · %s</span></li>" % (esc(os.path.basename(r["file"])), mb(r["bytes"]),
                         "Blueprint, moved to Cloudflare" if r["blueprint"] else "no page uses it" if r["kind"] == "unused" else "only old pages use it") for r in rs) + "</ul>")
            h.append("</div>")
        left = [r for r in rows if r["kind"] == "live" and not r["blueprint"]]
        if left:
            n += 1
            h.append("<h3>%d. Move to Cloudflare</h3><ul>" % n + "".join("<li>%s <span class='mut'>%s, on %s</span></li>" % (esc(r["file"]), mb(r["bytes"]), esc(", ".join(u["title"] for u in r["users"][:2]))) for r in left[:30]) + "</ul>")
        h.append("<h3>%d. Then export again</h3><p>Settings ▸ Export Course Content ▸ Create Export, save it in the class's -Canvas Entire Course folder. Canvas Preview reads it and this page updates.</p></section>" % (n + 1))
        sections.append("".join(h))
        nav.append("<a href='#c%s'>DAPR %s <small>%s to %s</small></a>" % (cls, cls, mb(whole), mb(after)))

    # Blueprint first: the BOAA Lab screenshots, fixed once
    bp = []
    if bp_rows:
        mapping, copied = {}, 0
        for rel, (r, z) in bp_rows.items():
            dest_rel = "All/BOAA_Lab/Images/" + cf_name(os.path.basename(rel))
            mapping[rel] = CF_URL + dest_rel
            dest = os.path.join(CF, dest_rel)
            if copy and not os.path.exists(dest):
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with z.open("web_resources/" + rel) as src, open(dest, "wb") as dst:
                    shutil.copyfileobj(src, dst)
                copied += 1
        size = sum(r["bytes"] for r, _ in bp_rows.values())
        bp.append("<section id='cBlueprint'><h2>Blueprint: fix once, then Sync <small>%d screenshots, %s in every class</small></h2>" % (len(bp_rows), mb(size)))
        bp.append("<p class='mut'>The BOAA Lab lessons (CS 623a BOAA Lab, Unified Class Content) keep their screenshots in Canvas Files, so every class export carries them. "
                  "They are in the Cloudflare folder <code>All/BOAA_Lab/Images</code> on this Mac%s.</p>" % (" (copied just now)" if copied else ""))
        bp.append("<h3>1. Upload them to Cloudflare</h3><p class='mut'>In Canvas Preview, Cloudflare Changes lists them as new: tick them and press Upload. Or in Terminal: the dry run first, and if it lists only the BOAA_Lab pictures, the second line.</p>")
        for dry in (" --dry-run", ""):
            cmd = 'rclone copy "%s/All/BOAA_Lab" "uvu-r2:uvu-canvas-files/All/BOAA_Lab"%s --exclude ".DS_Store" --exclude "_unused/**" --exclude "**/_unused/**" -v' % (CF, dry)
            bp.append("<pre class='copy' onclick='cp(this)'>%s</pre>" % esc(cmd))
        bp.append("<h3>2. Paste each lesson page in the Blueprint</h3><p class='mut'>Open in Blueprint ▸ Edit ▸ the &lt;/&gt; HTML editor ▸ select all ▸ Copy HTML here ▸ paste ▸ Save. "
                  "The pictures then load from Cloudflare.</p>")
        # one per lesson, at the Blueprint's own address (a class's synced copy can be "...-2" when an old class page had the name)
        bslug = {}
        try:
            bz = zipfile.ZipFile(BLUEPRINT_EXPORT())
            for n in bz.namelist():
                if n.startswith("wiki_content/") and n.endswith(".html"):
                    m = re.search(r"<title>(.*?)</title>", bz.read(n).decode("utf8", "ignore"), re.S)
                    if m: bslug[html.unescape(m.group(1)).strip()] = n[len("wiki_content/"):-5]
        except Exception:
            pass
        one = {}
        for path, u in sorted(bp_docs.items()):
            one.setdefault(u["title"], u)
        for u in one.values():
            u["slug"] = bslug.get(u["title"], re.sub(r"-\d+$", "", u["slug"] or "")) or None
        for path, u in sorted(((u["path"], u) for u in one.values()), key=lambda x: x[1]["title"]):
            b, left = fixed_html(u, mapping)
            link = CANVAS % BLUEPRINT_ID + ("pages/%s/edit" % u["slug"] if u["slug"] else "pages")
            bp.append("<div class='row' data-id='bp|%s'><label><input type='checkbox'> <b>%s</b></label> <a class='go' href='%s' target='_blank'>Open in Blueprint</a> "
                      "<button onclick='cpt(this)'>Copy HTML</button>%s<textarea readonly>%s</textarea></div>"
                      % (esc(path), esc(u["title"]), esc(link), (" <span class='warn'>still has %d Canvas link(s): %s</span>" % (len(left), esc(", ".join(left[:3])))) if left else "", esc(b)))
        folders = sorted(set(os.path.dirname(r) for r in bp_rows))
        bp.append("<h3>3. Delete the screenshots from the Blueprint's Files, then Sync</h3><p class='mut'>In <a class='go' href='%sfiles' target='_blank'>Blueprint Files</a>: %s. "
                  "Then Blueprint ▸ Sync. The classes' copies go with the Sync; step 2 in each class lists any that stay.</p><ul class='files'>%s</ul></section>"
                  % (CANVAS % BLUEPRINT_ID, " and ".join("<b>%s</b>" % esc(f) for f in folders),
                     "".join("<li>%s <span class='mut'>%s</span></li>" % (esc(rel), mb(r["bytes"])) for rel, (r, _) in sorted(bp_rows.items()))))
        nav.insert(0, "<a href='#cBlueprint'>Blueprint <small>%s</small></a>" % mb(size))

    stamp = datetime.datetime.now().strftime("%a %b %-d at %-I:%M %p")
    page = """<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Canvas Files Cleanup</title><style>
:root{--bg:#EDEAE4;--card:#fff;--ink:#212121;--mut:#5B6770;--acc:#0D47A1}
@media (prefers-color-scheme:dark){:root{--bg:#1E1E1E;--card:#2A2A2A;--ink:#EEE;--mut:#A9B3BA;--acc:#8CC8F0}}
body{font-family:-apple-system,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);margin:0;padding:16px}.w{max-width:980px;margin:0 auto}
.bar{position:sticky;top:0;background:#1B5E20;color:#fff;padding:8px 14px;border-radius:8px;z-index:2;display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.bar a{color:#fff;text-decoration:none;background:rgba(255,255,255,.15);padding:2px 10px;border-radius:12px}
section{background:var(--card);border-radius:10px;padding:10px 16px;margin:14px 0}h2 small,.mut{color:var(--mut);font-weight:400;font-size:.9em}
ul{list-style:none;padding-left:6px}li{padding:3px 0}.files li{font-size:.92em}.fold{margin:6px 0}.go{color:var(--acc);font-weight:600;margin-left:6px}
pre.copy{background:#f2f2f2;color:#222;padding:8px;border-radius:6px;white-space:pre-wrap;word-break:break-all;cursor:pointer;user-select:all;-webkit-user-select:all}
textarea{display:none}.warn{color:#B71C1C;font-weight:600}.done{opacity:.45}button{margin-left:6px}
</style></head><body><div class='w'><div class='bar'><b>Canvas Files Cleanup</b>%s<span style='margin-left:auto;font-size:.85em'>made %s</span></div>
<section><p>Every Canvas export carries all of the course's Files, used or not, so these steps take each class from its size now to about the size shown. Blueprint first (it fixes every class at once), then each class. Ticks are kept in this browser.</p>
<p class='mut'>Sizes: %s.</p></section>%s%s</div>
<script>
function cp(e){navigator.clipboard.writeText(e.innerText);e.style.background='#C8E6C9'}
function cpt(b){var t=b.parentNode.querySelector('textarea');navigator.clipboard.writeText(t.value);b.textContent='Copied';setTimeout(function(){b.textContent='Copy HTML'},1500)}
var K='cfclean';var s={};try{s=JSON.parse(localStorage.getItem(K)||'{}')}catch(e){}
document.querySelectorAll('[data-id]').forEach(function(r){var c=r.matches('input')?r:r.querySelector('input');if(!c)return;var id=r.getAttribute('data-id');
if(s[id]){c.checked=true;r.classList.add('done')}c.addEventListener('change',function(){s[id]=c.checked;(r.closest('li,div')||r).classList.toggle('done',c.checked);try{localStorage.setItem(K,JSON.stringify(s))}catch(e){}})});
</script></body></html>""" % ("".join(nav), stamp, ", ".join("DAPR %s %s to about %s" % (c, mb(w), mb(a)) for c, w, a in totals), "".join(bp), "".join(sections))
    open(out, "w").write(page)
    print(json.dumps(dict(out=out, classes=[dict(cls=c, now=w, after=a) for c, w, a in totals], blueprint_files=len(bp_rows))))


if __name__ == "__main__":
    main()
