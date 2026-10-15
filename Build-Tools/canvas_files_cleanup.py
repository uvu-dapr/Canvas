#!/usr/bin/env python3
"""canvas_files_cleanup.py: what to delete in Canvas so each class's export is as small as it can be.

Adam, 2026-10-05: "nothing should be more than 100 MB for a canvas export. Give me what I need to clean up online ...
All file use should be put on cloudflare ... [quiz images stay: they cannot be on Cloudflare or GitHub]".

A Canvas export carries every file in the course's Files, used or not. For each class's newest export this sorts every
file into:
  card      the course card picture (course_settings.xml image_identifier_ref, Settings ▸ Course Details ▸ Image):
            ALWAYS stays; deleting it blanks the Dashboard card (J308, 2026-10-15 audit). A small JPEG is offered instead.
  quiz      used by a quiz or a question bank: linked by a quiz; link it from GitHub instead (quiz pictures from GitHub work, 2026-10-15)
  live      used by a page, assignment or discussion students reach (in a module): moves to Cloudflare, the page is
            pasted with the Cloudflare address, then (once a new export shows nothing links it) the Canvas file is deleted
  oldcopy   used only by old pages in no module: delete those pages first; the file is listed once nothing links it
  copy      a "-1"/"-2" byte-identical copy of a question bank picture that no bank, quiz or page uses (the Oct 7 Blueprint
            import made one per picture); listed with the twin question banks
  bankleft  a question bank picture no bank, quiz or page uses (not a "-N" copy)
  unused    used by nothing: delete
Twin question banks (same title, word for word the same questions) are listed per class with which copy to delete: the
later one, Blueprint first, then Sync (J308). Never listed for deletion: anything a page, assignment, quiz or a bank a
quiz draws from links (by path or by file id), assignments, quizzes, discussions (graded work), anything titled Roll Call,
"Unfiled Questions" banks (Canvas makes them for quiz questions) and the course card.
J312 (Adam 2026-10-15): the page is a companion to the TidyUP LTI tool (tool 347769, every course): per class an Open
TidyUP link, the folders to delete (Folders tab), the files TidyUP shows as unused that a question bank uses (TidyUP:
"Question banks cannot be scanned for file usage"), and which copy of a duplicate is safe.
Blueprint pages (modules titled "(Unified Class Content)") are fixed once in the Blueprint and Synced (Adam, 2026-10-05:
"just give me the blueprint course and then I'll push it to everything else").

  python3 canvas_files_cleanup.py <out.html> <export.imscc>=<Course_Folder>=<course id> ... [--copy] [--no-blueprint]

The Blueprint's newest export is added on its own when it is not named (twin banks are deleted there first).
--copy puts the live files into the local Cloudflare Canvas Links folder (Adam uploads with rclone, never this tool).
"""
import zipfile, sys, re, urllib.parse, html, collections, os, json, shutil, datetime

CF = "/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links"
CF_URL = "https://uvu-files.adamo.workers.dev/"
BLUEPRINT_ID = 655823
CANVAS = "https://uvu.instructure.com/courses/%d/"
# J310: the small course card JPEGs and bank pictures made for Adam to swap in by hand
SMALL = "/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses/Claude outputs/Notes and Briefs/2026-10-15 Smaller Canvas Pictures"


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


def plain(s):
    """exact Canvas titles, with any en or em dash shown as a hyphen (All AI Projects 1)"""
    return re.sub(r"\s*[–—]\s*", " - ", s).replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')


def read(exp):
    z = zipfile.ZipFile(exp)
    names = z.namelist()
    infos = {i.filename[len("web_resources/"):]: i for i in z.infolist()
             if i.filename.startswith("web_resources/") and not i.filename.endswith("/")}
    files = {rel: i.file_size for rel, i in infos.items()}
    sig = {rel: (i.file_size, i.CRC) for rel, i in infos.items()}
    mm = z.read("course_settings/module_meta.xml").decode("utf8", "ignore")
    inmod = {}
    for m in re.finditer(r'<module identifier="[^"]+">\s*<title>(.*?)</title>(.*?)</module>', mm, re.S):
        for it in re.finditer(r"<item identifier=\"[^\"]+\">(.*?)</item>", m.group(2), re.S):
            r = re.search(r"<identifierref>(.*?)</identifierref>", it.group(1))
            if r:
                inmod.setdefault(r.group(1), []).append(html.unescape(m.group(1)))
    man = z.read("imsmanifest.xml").decode("utf8", "ignore")
    res_of, file_id = {}, {}
    for m in re.finditer(r'<resource identifier="([^"]+)"[^>]*href="([^"]+)"', man):
        res_of[m.group(2)] = m.group(1)
        if m.group(2).startswith("web_resources/"):
            file_id[m.group(2)[len("web_resources/"):]] = m.group(1)
    # the course card: Settings ▸ Course Details ▸ Image (by file id, or an image_url pointing into Files)
    card = set()
    try:
        cs = z.read("course_settings/course_settings.xml").decode("utf8", "ignore")
    except KeyError:
        cs = ""
    for ref in re.findall(r"<image_identifier_ref>(.*?)</image_identifier_ref>", cs):
        card |= {rel for rel, i in file_id.items() if i == ref.strip()}
    for u in re.findall(r"<image_url>(.*?)</image_url>", cs):
        u = urllib.parse.unquote(html.unescape(u)).split("?")[0]
        if "IMS-CC-FILEBASE$/" in u:
            card.add(u.split("IMS-CC-FILEBASE$/", 1)[1])
    card |= {rel for rel in files if rel.startswith("course_image/")}   # Canvas's own folder for it
    docs, idrefs, drawn = [], set(), set()
    for n in names:
        if n.startswith("web_resources/") or not n.endswith((".html", ".xml", ".qti")):
            continue
        t = z.read(n).decode("utf8", "ignore")
        if n not in ("imsmanifest.xml", "course_settings/files_meta.xml", "course_settings/course_settings.xml"):
            idrefs |= set(re.findall(r"g[0-9a-f]{32}", t))   # a file named by its id, not its path, still counts as used
        drawn |= set(re.findall(r"<sourcebank_ref>(.*?)</sourcebank_ref>", t))   # banks a quiz draws questions from
        if n.startswith("course_settings/") or "IMS-CC-FILEBASE" not in t and "<objectbank" not in t:
            continue
        quiz = n.endswith(".qti") or "assessment" in n
        bank = None
        if "<objectbank" in t:
            b = re.search(r'<objectbank ident="([^"]+)"', t)
            bt = re.search(r"bank_title</fieldlabel>\s*<fieldentry>(.*?)</fieldentry>", t, re.S)
            body = re.sub(r'(ident|identifier)="[^"]*"', "", t)
            body = re.sub(r"bank_context_uuid</fieldlabel>\s*<fieldentry>.*?</fieldentry>", "", body)
            bank = dict(ident=b.group(1) if b else n, title=html.unescape(bt.group(1)).strip() if bt else "(no title)",
                        body=body, items=len(re.findall(r"<item ident=", t)), order=0, size=len(t.encode("utf8")))
        m = re.search(r"<title>(.*?)</title>", t, re.S)
        title = bank["title"] if bank else html.unescape(m.group(1)).strip() if m else n
        rid = res_of.get(n) or n.split("/")[-1].split(".")[0]
        if rid not in inmod and "/" in n and n.split("/")[0] in inmod:
            rid = n.split("/")[0]
        m = re.search(r'name="workflow_state" content="(\w+)"', t) or re.search(r"<workflow_state>(\w+)</workflow_state>", t)
        pub = m.group(1) if m else None
        kind = "bank" if bank else "quiz" if quiz else "page" if n.startswith("wiki_content/") else "assignment" if "assignment" in t[:4000] else "discussion" if "topic" in t[:2000] else "item"
        docs.append(dict(path=n, quiz=quiz, title=title, text=t, mods=inmod.get(rid, []), pub=pub, kind=kind, bank=bank,
                         slug=n[len("wiki_content/"):-5] if n.startswith("wiki_content/") else None))
    order = {m.group(1): i for i, m in enumerate(re.finditer(r'<resource identifier="([^"]+)"', man))}
    for d in docs:
        if d["bank"]:
            d["bank"]["order"] = order.get(d["bank"]["ident"], 10 ** 6)
    return z, files, docs, dict(sig=sig, file_id=file_id, idrefs=idrefs, card=card, drawn=drawn)


def pats(rel):
    enc = urllib.parse.quote(rel, safe="/()'!*,;=&+@:")
    return {rel, enc, enc.replace("%20", "+"), html.escape(rel), urllib.parse.quote(rel, safe="/")}


def copy_of(rel, sig):
    """'A-1-1.png' -> 'A-1.png', 'X-1.svg.png' -> 'X.svg.png': a "-N" name whose original sits beside it, byte for byte"""
    d, base = os.path.split(rel)
    for m in re.finditer(r"-\d+(?=[.-])", base):
        cand = os.path.join(d, base[:m.start()] + base[m.end():]) if d else base[:m.start()] + base[m.end():]
        if cand in sig and sig[cand] == sig[rel]:
            return cand
    return None


def classify(files, docs, ctx):
    rows = []
    for rel, size in files.items():
        p = pats(rel)
        users = [d for d in docs if any(("IMS-CC-FILEBASE$/" + q) in d["text"] for q in p)]
        by_id = ctx["file_id"].get(rel) in ctx["idrefs"]
        placed = [d for d in users if d["mods"]]
        staff = placed and all(all("Instructor Use Only" in m for m in d["mods"]) for d in placed)   # students never see it
        orig = None
        if rel in ctx["card"]:
            k = "card"     # J308: the Dashboard course card picture, never deleted
        elif users and all(u["quiz"] for u in users):
            k = "quiz"     # a quiz or a question bank shows it
        elif users:
            k = "oldcopy" if not placed else "quiz" if all(u["quiz"] for u in placed) else "staff" if staff else "live"
        elif by_id:
            k = "quiz" if rel.startswith("assessment_questions/") else "byid"   # linked by its file id: stays
        else:
            orig = copy_of(rel, ctx["sig"])
            k = "copy" if orig and rel.startswith("assessment_questions/") else "bankleft" if rel.startswith("assessment_questions/") else "unused"
        bp = bool(placed) and all(any("Unified Class Content" in m for m in u["mods"]) for u in placed if not u["quiz"])
        rows.append(dict(file=rel, bytes=size, kind=k, users=users, orig=orig, blueprint=bp and k == "live"))
    rows.sort(key=lambda r: -r["bytes"])
    return rows


def twins(docs, ctx):
    """question banks with the same title and word for word the same questions: [(title, [banks oldest first]), ...]"""
    groups = collections.defaultdict(list)
    for d in docs:
        b = d["bank"]
        if not b or b["title"] == "Unfiled Questions" or "roll call" in b["title"].lower():
            continue
        groups[(b["title"], hash(b["body"]))].append(b)
    out = []
    for (title, _), bs in groups.items():
        if len(bs) < 2 or any(b["ident"] in ctx["drawn"] for b in bs):   # a bank a quiz draws from is never listed
            continue
        out.append((title, sorted(bs, key=lambda b: b["order"])))
    return sorted(out, key=lambda x: x[0].lower())


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
    b = re.sub(r"(\d)\s*[–—]\s*(\d)", r"\1 and \2", b)
    b = re.sub(r"\s+[–—]\s+", ": ", b)
    b = re.sub(r"\s*—\s*", ", ", b).replace("–", "-").replace(" -- ", ": ")
    left = re.findall(r"\$(?:IMS-CC-FILEBASE|CANVAS_[A-Z_]+|WIKI_REFERENCE)\$[^\"'<\s]*", b)
    return b.strip(), left


def mb(n):
    return "%.1f MB" % (n / 1e6) if n >= 1e5 else "%.0f KB" % (n / 1e3)


def esc(s):
    return html.escape(plain(str(s)), quote=True)


TIDYUP = 347769   # the TidyUP LTI tool (account level, the same id in every course)
# Every class in Adam's order (Blueprint first, Fall, Spring last; K109) with its live course number, so a class with no
# export on this Mac still gets its TidyUP link
CLASSES = [("Blueprint", 655823), ("2000", 636866), ("2020", 643734), ("2255", 642395), ("3340", 641145),
           ("2010", 655746), ("3255", 651912), ("3345", 651955)]
SAFE = ("unused", "copy", "bankleft")
KEEP_FOLDERS = ("assessment_questions", "course_image")   # Canvas's own folders: bank pictures and the course card
# Adam's TidyUP routine, 2026-10-15: Scan Course; Files ▸ Show: Unused Files ▸ select all ▸ Delete Selected; Folders ▸
# Show: Empty ▸ select all ▸ Delete Selected; Canvas Content ▸ In Modules: the crossed-out circle ▸ Show: All ▸ select
# all ▸ Delete Selected. This page gives the KEEP list to untick before each Delete Selected.
TIDY_CSV = "/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses/Claude outputs/Notes and Briefs/TidyUP Reports"


def deletable_folders(rows):
    """the topmost folders where every file inside (subfolders too) is safe to delete, biggest first"""
    under = collections.defaultdict(list)
    for r in rows:
        parts = r["file"].split("/")[:-1]
        for i in range(1, len(parts) + 1):
            under["/".join(parts[:i])].append(r)
    ok = {f for f, rs in under.items() if f.split("/")[0] not in KEEP_FOLDERS and all(r["kind"] in SAFE for r in rs)}
    top = [f for f in ok if not any(f.startswith(o + "/") for o in ok)]
    return sorted(((f, under[f]) for f in top), key=lambda x: -sum(r["bytes"] for r in x[1]))


def who(users):
    """'bank "Compression" (2 copies); page "X"': each title once"""
    seen = collections.OrderedDict()
    for u in users:
        k = (u["kind"], plain(u["title"]))
        seen[k] = seen.get(k, 0) + 1
    parts = ["%s \"%s\"%s" % (k, t, " (%d copies)" % n if n > 1 else "") for (k, t), n in seen.items()]
    return "; ".join(parts[:4]) + (" and %d more" % (len(parts) - 4) if len(parts) > 4 else "")


def content(exp):
    """every page, assignment, quiz, discussion and question bank in an export: [dict(kind, title, slug, inmod, linked)]"""
    z = zipfile.ZipFile(exp)
    names = z.namelist()
    rd = lambda n: z.read(n).decode("utf8", "ignore")
    man = rd("imsmanifest.xml")
    mm = rd("course_settings/module_meta.xml")
    inmod = set(re.findall(r"<identifierref>(.*?)</identifierref>", mm))
    res_of = {m.group(2): m.group(1) for m in re.finditer(r'<resource identifier="([^"]+)"[^>]*href="([^"]+)"', man)}
    title = lambda t: html.unescape((re.search(r"<title>(.*?)</title>", t, re.S) or re.search(r"$^", "")).group(1) if re.search(r"<title>(.*?)</title>", t, re.S) else "").strip()
    out, linked = [], set()
    for n in names:
        if n.startswith("web_resources/") or not n.endswith((".html", ".xml", ".qti")) or n == "imsmanifest.xml":
            continue
        t = rd(n)
        linked |= {urllib.parse.unquote(s) for s in re.findall(r"\$WIKI_REFERENCE\$/pages/([^\"'?#<\s]+)", t)}
        linked |= {urllib.parse.unquote(s) for s in re.findall(r"/courses/\d+/pages/([^\"'?#<\s]+)", t)}
        if n.startswith("wiki_content/") and n.endswith(".html"):
            ident = res_of.get(n, "")
            out.append(dict(kind="page", title=title(t), slug=n[len("wiki_content/"):-5], ident=ident, inmod=ident in inmod, src=n))
        elif n.endswith("/assessment_meta.xml"):
            f = n.split("/")[0]
            out.append(dict(kind="quiz", title=title(t), slug=None, ident=f, inmod=f in inmod, src=n))
        elif n.endswith("/assignment_settings.xml") and (n.split("/")[0] + "/assessment_meta.xml") not in names:
            f = n.split("/")[0]
            out.append(dict(kind="assignment", title=title(t), slug=None, ident=f, inmod=f in inmod, src=n))
        elif "imsdt" in t[:600] and "<topic" in t[:600]:
            ident = res_of.get(n, n.split("/")[-1].split(".")[0])
            out.append(dict(kind="discussion", title=title(t), slug=None, ident=ident, inmod=ident in inmod, src=n))
        elif "<objectbank" in t:
            bt = re.search(r"bank_title</fieldlabel>\s*<fieldentry>(.*?)</fieldentry>", t, re.S)
            out.append(dict(kind="question bank", title=html.unescape(bt.group(1)).strip() if bt else "(no title)", slug=None, ident=n, inmod=False, src=n))
    for c in out:
        c["linked"] = c["kind"] == "page" and c["slug"] in linked
    return out


def newest_full(exp):
    """the class's newest Full package beside its export (DAPR-2000-Fall-2026-v133-Full.imscc), or None"""
    d = os.path.dirname(exp)
    best = None
    for f in os.listdir(d):
        m = re.match(r"DAPR-\d{4}-.*-v(\d+)-Full\.imscc$", f)
        if m and (best is None or int(m.group(1)) > best[0]):
            best = (int(m.group(1)), os.path.join(d, f))
    return best[1] if best else None


def keep_reason(c, bp_titles, is_bp, placed=(), built=()):
    """why a not-in-module item must stay, or None when it is safe for TidyUP's Canvas Content delete.
    placed: titles this course has in a module (a loose copy of one is an old duplicate); built: titles in the newest
    Full package (a loose page the build has and no module holds is current work not placed yet, so it stays)"""
    t = c["title"].lower()
    if "roll call" in t or "attendance" in t:
        return "Roll Call: never deleted"
    if c["kind"] in ("assignment", "quiz", "discussion"):
        return "graded work: no gradebook on this Mac proves it has no submissions, so it stays"
    if c["kind"] == "question bank":
        return "question bank: banks are cleaned only in Manage Question Banks (step 5)"
    if any(w in t for w in ("no publish", "not publish", "don't publish", "dont publish", "instructor use only", "instructor notes")):
        return "instructor page (*No Publish, Do Not Publish, Instructor Use Only)"
    if t.startswith("essentials:") or t.startswith("boaa lab:"):
        return "Blueprint content (Essentials, BOAA Lab): fixed in the Blueprint, never in a class"
    if "syllabus" in t or (c["slug"] or "").startswith("syllabus"):
        return "Syllabus page built for review"
    if is_bp:
        return "Blueprint content: Sync carries it to every class"
    if c["linked"]:
        return "another page, assignment or the syllabus links it"
    if c["title"] in bp_titles:
        return "synced from the Blueprint: delete it there, never in a class"
    if "legend" in t or "reference" in t or "front page" in t or "home" == t:
        return "reference page (Course Legend, Reference)"
    if c["title"] in built and c["title"] not in placed:
        return "in the newest Full package but in no module here: current work not placed yet, so it stays until a module holds it"
    return None


def main():
    out = sys.argv[1]
    copy = "--copy" in sys.argv
    specs = [a.split("=") for a in sys.argv[2:] if a.count("=") == 2]
    if "--no-blueprint" not in sys.argv and not any("blu" in os.path.basename(s[0]).lower() for s in specs):
        try:
            specs.append([BLUEPRINT_EXPORT(), "-", str(BLUEPRINT_ID)])   # twin banks go in the Blueprint first
        except Exception:
            pass
    def key_of(exp):
        m = re.search(r"dapr-(\d{4})", os.path.basename(exp).lower())
        return m.group(1) if m else "Blueprint"
    given = {key_of(s[0]): s for s in specs}
    bp_titles = set()
    if "Blueprint" in given:
        bp_titles = {c["title"] for c in content(given["Blueprint"][0]) if c["kind"] != "question bank"}
    bp_rows, bp_docs, sections, nav, totals, summary = {}, {}, [], [], [], []
    bp_twins = set()
    known = [c for c, _ in CLASSES]
    def tick(cls, step, text):
        return "<label class='step' data-id='%s|step|%s'><input type='checkbox'> <b>%s</b></label>" % (cls, step, text)
    def keepbox(cls, step, items, what):
        """items: [(name, reason)] sorted A to Z like TidyUP"""
        if not items:
            return "<p class='ok'>Nothing to untick: %s</p>" % what
        h = ["<div class='keepbox'><b>KEEP: untick these %d before Delete Selected</b> <span class='mut'>(A to Z, as TidyUP sorts by title)</span><ol>" % len(items)]
        for nm, why in sorted(items, key=lambda x: x[0].lower()):
            h.append("<li data-id='%s|keep%s|%s'><label><input type='checkbox'> <b>%s</b></label> <span class='mut'>%s</span></li>" % (cls, step, esc(nm), esc(nm), esc(why)))
        return "".join(h) + "</ol></div>"
    for cls in known + sorted(set(given) - set(known)):
        name = "DAPR " + cls if cls != "Blueprint" else "Blueprint"
        cid = int(given[cls][2]) if cls in given else dict(CLASSES)[cls]
        tidy = CANVAS % cid + "external_tools/%d" % TIDYUP
        term = "Blueprint" if cls == "Blueprint" else "Spring 2027" if cls in ("2010", "3255", "3345") else "Fall 2026"
        if cls not in given:
            sections.append("<section class='cls' id='c%s'><h2>%s <small>%s</small></h2><p><a class='go big' href='%s' target='_blank'>Open TidyUP</a></p>"
                            "<p class='warn'>No export of this live course on this Mac yet, so there is no KEEP list. Do not press Delete Selected here yet.</p>"
                            "<p class='mut'>Export it first (Settings ▸ Export Course Content ▸ Create Export) and save it in the class's -Canvas Entire Course folder; this page then lists what to untick.</p>%s</section>"
                            % (cls, name, term, esc(tidy), tick(cls, "export", "Exported and saved")))
            nav.append("<a href='#c%s'>%s <small>no export</small></a>" % (cls, name))
            continue
        exp = given[cls][0]
        is_bp = cls == "Blueprint"
        z, files, docs, ctx = read(exp)
        rows = classify(files, docs, ctx)
        tw = twins(docs, ctx)
        items = content(exp)
        whole = sum(i.file_size for i in z.infolist())
        if is_bp:
            bp_twins = {t for t, _ in tw}
        by = collections.defaultdict(int)
        for r in rows:
            by[r["kind"]] += r["bytes"]
        tw_bytes = sum(b["size"] for _, bs in tw for b in bs[1:])
        after = whole - sum(by[k] for k in SAFE) - tw_bytes
        totals.append((name, whole, after))
        for r in rows:
            if r["blueprint"] and r["file"] not in bp_rows:
                bp_rows[r["file"]] = (r, z)
                for u in r["users"]:
                    if u["mods"] and not u["quiz"]:
                        bp_docs.setdefault(u["path"], u)
        folders = deletable_folders(rows)
        # step 2 KEEP: what TidyUP calls unused but must stay. TidyUP: "Question banks cannot be scanned for file usage".
        bankonly = [r for r in rows if r["kind"] == "quiz" and (not r["users"] or all(u["kind"] == "bank" for u in r["users"]))]
        odd = [r for r in rows if r["kind"] == "byid"]
        keep2 = [(os.path.basename(r["file"]), "course card picture (Settings ▸ Course Details ▸ Image), %s" % r["file"]) for r in rows if r["kind"] == "card"]
        keep2 += [(os.path.basename(r["file"]), "a question bank uses it: %s" % who(r["users"]) if r["users"] else "a bank names it by file id") for r in bankonly]
        keep2 += [(os.path.basename(r["file"]), "named by its file id in course content") for r in odd]
        gone = [r for r in rows if r["kind"] in SAFE]
        # step 4 KEEP: not in a module, but must stay
        loose = [c for c in items if not c["inmod"]]
        placed = {c["title"] for c in items if c["inmod"]}
        full = None if is_bp else newest_full(exp)
        built = {c["title"] for c in content(full)} if full else set()
        keep4, safe4 = [], []
        bank_seen = collections.Counter(c["title"] for c in loose if c["kind"] == "question bank")
        for c in loose:
            if c["kind"] == "question bank":
                continue
            why = keep_reason(c, bp_titles, is_bp, placed, built)
            (keep4 if why else safe4).append((c["title"], (c["kind"] + ": " + why) if why else c["kind"] + (": an old copy, the module holds another page with this title" if c["title"] in placed else ": in no module, nothing links it, not in the newest Full package")))
        keep4b = sorted(((t, "question bank%s" % (" (%d copies)" % n if n > 1 else "")) for t, n in bank_seen.items()), key=lambda x: x[0].lower())
        summary.append(dict(cls=name, now=whole, after=after, keep_files=len(keep2), files_to_go=len(gone),
                            keep_content=len(keep4), keep_banks=len(keep4b), safe_content=len(safe4), full=os.path.basename(full) if full else None, folders=[f for f, _ in folders],
                            twin_titles=len(tw), twin_extra=sum(len(bs) - 1 for _, bs in tw), card=sorted(ctx["card"])))
        h = ["<section class='cls' id='c%s'><h2>%s <small>%s · %s now, about %s after</small></h2>" % (cls, name, term, mb(whole), mb(after))]
        h.append("<p><a class='go big' href='%s' target='_blank'>Open TidyUP</a> <span class='mut'>for %s. Every Delete Selected is your click; this page only says what to untick first.</span></p>" % (esc(tidy), name))
        h.append("<p class='mut'>From <b>%s</b>, checked against every page, assignment, discussion, quiz and question bank in it, by path and by file id.%s</p>"
                 % (esc(os.path.basename(exp)), "" if is_bp else " Do the Blueprint first and Sync: some of these may already be gone."))
        h.append("<div class='st'>%s<p class='mut'>TidyUP ▸ <b>Scan Course</b>. Wait for it to finish.</p></div>" % tick(cls, "1", "1. Scan Course"))
        h.append("<div class='st'>%s<p class='mut'>Files tab ▸ Show: <b>Unused Files</b> ▸ select all ▸ <b>untick the KEEP list</b> ▸ Delete Selected. "
                 "About %d file(s), %s should go; most are listed under Details below.</p>%s" % (tick(cls, "2", "2. Files: Unused Files"), len(gone), mb(sum(r["bytes"] for r in gone)),
                 keepbox(cls, 2, keep2, "no question bank picture or course card would show as unused.")))
        if gone:
            h.append("<details><summary>Details: what should go in step 2 (%d file(s))</summary>" % len(gone))
            if folders:
                h.append("<p class='mut'>Whole folders, biggest first:</p><ul class='files'>" + "".join("<li><b>%s</b> <span class='mut'>%s, %d file(s)</span></li>" % (esc(f), mb(sum(r["bytes"] for r in rs)), len(rs)) for f, rs in folders) + "</ul>")
            inf = {r["file"] for _, rs in folders for r in rs}
            rest = [r for r in gone if r["file"] not in inf]
            if rest:
                h.append("<p class='mut'>Single files (a \"-N\" copy in assessment_questions is a byte for byte copy of the original, which stays):</p><ul class='files'>"
                         + "".join("<li><code>%s</code> <span class='mut'>%s%s</span></li>" % (esc(r["file"]), mb(r["bytes"]), (" · copy of %s" % esc(os.path.basename(r["orig"]))) if r["orig"] else "") for r in rest) + "</ul>")
            dup = collections.defaultdict(list)
            for r in rows:
                dup[ctx["sig"][r["file"]]].append(r)
            dups = [rs for rs in dup.values() if len(rs) > 1 and any(r["kind"] in SAFE for r in rs) and all(r["kind"] in SAFE for r in rs)]
            if dups:
                h.append("<p class='mut'>Same file twice, every copy safe (TidyUP shows each with its own date; tick both): %s</p>"
                         % esc(", ".join(sorted({os.path.basename(rs[0]["file"]) for rs in dups})[:40])))
            h.append("</details>")
        h.append("<div class='st'>%s<p class='mut'>Folders tab ▸ Show: <b>Empty</b> ▸ select all ▸ Delete Selected. Nothing to untick: an empty folder holds nothing.</p></div>" % tick(cls, "3", "3. Folders: Empty"))
        h.append("<div class='st'>%s<p class='mut'>Canvas Content tab ▸ In Modules: <b>the crossed-out circle</b> (not in a module) ▸ Show: <b>All</b> ▸ select all ▸ <b>untick the KEEP list</b> ▸ Delete Selected.</p>%s"
                 % (tick(cls, "4", "4. Canvas Content: not in a module"), keepbox(cls, 4, keep4, "nothing outside a module must stay.")))
        if keep4b:
            h.append("<details><summary><b>If TidyUP lists question banks here: untick all %d bank titles too</b> (banks are cleaned only in step 5)</summary><ol>%s</ol></details>"
                     % (len(keep4b), "".join("<li data-id='%s|keepb|%s'><label><input type='checkbox'> <b>%s</b></label> <span class='mut'>%s</span></li>" % (cls, esc(t), esc(t), esc(k)) for t, k in keep4b)))
        if is_bp:
            h.append("<p class='warn'>In the Blueprint everything is synced to every class, so the KEEP list is everything: skip this Delete Selected here.</p>")
        if safe4:
            h.append("<details><summary>Details: what should go in step 4 (%d)</summary><ul class='files'>%s</ul></details>"
                     % (len(safe4), "".join("<li>%s <span class='mut'>%s</span></li>" % (esc(t), esc(k)) for t, k in sorted(safe4, key=lambda x: x[0].lower()))))
        h.append("</div>")
        # step 5 twin banks
        if tw:
            extra = sum(len(bs) - 1 for _, bs in tw)
            h.append("<div class='st'>%s" % tick(cls, "5", "5. Twin question banks (Manage Question Banks; TidyUP does not do banks)"))
            if is_bp:
                h.append("<p class='mut'><b>Do this before any class.</b> Each title below is in the Blueprint more than once, word for word the same (the Oct 7 Blueprint import added a copy). "
                         "Open <a class='go' href='%squestion_banks' target='_blank'>Manage Question Banks</a>, open each copy of the title, and delete the "
                         "<b>later copy</b>: the one whose address ends in the <b>higher number</b>. Keep the first. Then <b>Blueprint ▸ Sync</b>, so every class loses its synced copy too. "
                         "No quiz draws from any of these banks.</p>" % (CANVAS % cid))
            else:
                h.append("<p class='mut'>After the Blueprint Sync, open <a class='go' href='%squestion_banks' target='_blank'>Manage Question Banks</a> "
                         "here: for each title below keep <b>one</b> copy (the first, lowest number in its address) and delete the later ones still left. "
                         "No quiz in this class draws from any of these banks.</p>" % (CANVAS % cid))
            h.append("<details><summary>%d bank title(s), %d extra copies</summary><table><tr><th></th><th>Bank title (exact)</th><th>Questions</th><th>Copies now</th><th>Delete</th>%s</tr>" % (len(tw), extra, "" if is_bp else "<th>Also twinned in the Blueprint</th>"))
            for title, bs in tw:
                h.append("<tr data-id='%s|bank|%s'><td><input type='checkbox'></td><td><b>%s</b></td><td>%d</td><td>%d</td><td>%d (the later %s)</td>%s</tr>"
                         % (cls, esc(title), esc(title), bs[0]["items"], len(bs), len(bs) - 1, "one" if len(bs) == 2 else "ones",
                            "" if is_bp else "<td>%s</td>" % ("yes: the Sync removes one" if title in bp_twins else "no: delete here")))
            h.append("</table><p class='mut'>Banks that share a title but differ, and the Unfiled Questions banks Canvas makes for quiz questions, are not listed: they stay.</p></details></div>")
        for c in sorted(ctx["card"]):
            base = os.path.splitext(os.path.basename(c))[0]
            small = next((p for p in (os.path.join(SMALL, name, base + e) for e in (".jpg", ".jpeg")) if os.path.exists(p)), None)
            if small:
                h.append("<div class='st'>%s<p class='mut'>Settings ▸ Course Details ▸ Image ▸ choose <code>%s</code> (%s instead of %s). The old card file then shows as unused in TidyUP the next time; delete it then.</p></div>"
                         % (tick(cls, "card", "6. Smaller course card picture"), esc(small), mb(os.path.getsize(small)), mb(files.get(c, 0))))
        h.append("<div class='st'>%s<p class='mut'>Settings ▸ Export Course Content ▸ Create Export, save it in the class's -Canvas Entire Course folder. Canvas Preview reads it and this page updates.</p></div>" % tick(cls, "x", "Then export again"))
        h.append("<p><button class='nextc'>Next class</button></p></section>")
        sections.append("".join(h))
        nav.append("<a href='#c%s'>%s <small>%s to %s</small></a>" % (cls, name, mb(whole), mb(after)))

    # Blueprint lesson pages whose screenshots are still Canvas files: paste them with Cloudflare addresses, once
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
        bp.append("<section class='cls' id='cBlueprintPages'><h2>Blueprint pages: move their pictures to Cloudflare <small>%d files, %s in every class</small></h2>" % (len(bp_rows), mb(size)))
        bp.append("<p class='mut'>These Blueprint lessons keep pictures in Canvas Files, so every class export carries them. "
                  "They are in the Cloudflare folder <code>All/BOAA_Lab/Images</code> on this Mac%s.</p>" % (" (copied just now)" if copied else ""))
        bp.append("<h3>1. Upload them to Cloudflare</h3><p class='mut'>In Canvas Preview, Cloudflare Changes lists them as new: tick them and press Upload. Or in Terminal: the dry run first, and if it lists only the BOAA_Lab pictures, the second line.</p>")
        for dry in (" --dry-run", ""):
            cmd = 'rclone copy "%s/All/BOAA_Lab" "uvu-r2:uvu-canvas-files/All/BOAA_Lab"%s --exclude ".DS_Store" --exclude "_unused/**" --exclude "**/_unused/**" -v' % (CF, dry)
            bp.append("<pre class='copy' onclick='cp(this)'>%s</pre>" % esc(cmd))
        bp.append("<h3>2. Paste each lesson page in the Blueprint</h3><p class='mut'>Open in Blueprint ▸ Edit ▸ the &lt;/&gt; HTML editor ▸ select all ▸ Copy HTML here ▸ paste ▸ Save. "
                  "The pictures then load from Cloudflare.</p>")
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
                      % (esc(path), esc(u["title"]), esc(link), (" <span class='warn'>still has %d Canvas link(s): %s</span>" % (len(left), esc(", ".join(left[:3])))) if left else "", html.escape(b)))
        bp.append("<h3>3. Export the Blueprint again</h3><p class='mut'>Once the pasted pages are saved, nothing links these files, and the next export lists them under the Blueprint's "
                  "Delete these files step. Delete them there, then Sync.</p></section>")
        nav.insert(1, "<a href='#cBlueprintPages'>Blueprint pages <small>%s</small></a>" % mb(size))
        sections.insert(1, "".join(bp))

    stamp = datetime.datetime.now().strftime("%a %b %-d at %-I:%M %p")
    page = """<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>TidyUP Companion</title><style>
:root{--bg:#EDEAE4;--card:#fff;--ink:#212121;--mut:#5B6770;--acc:#0D47A1;--keep:#FFF3E0;--keepb:#BF360C;--ok:#2E7D32}
@media (prefers-color-scheme:dark){:root{--bg:#1E1E1E;--card:#2A2A2A;--ink:#EEE;--mut:#A9B3BA;--acc:#8CC8F0;--keep:#3A2A1C;--keepb:#FFAB91;--ok:#81C784}}
body{font-family:-apple-system,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);margin:0;padding:16px}.w{max-width:980px;margin:0 auto}
.bar{position:sticky;top:0;background:#1B5E20;color:#fff;padding:8px 14px;border-radius:8px;z-index:2;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.bar a{color:#fff;text-decoration:none;background:rgba(255,255,255,.15);padding:2px 10px;border-radius:12px}.bar a.on{background:#fff;color:#1B5E20}
.bar button{background:#fff;color:#1B5E20;border:0;border-radius:12px;padding:4px 12px;font-weight:700;cursor:pointer}
section{background:var(--card);border-radius:10px;padding:10px 16px;margin:14px 0}h2 small,.mut{color:var(--mut);font-weight:400;font-size:.9em}
ul,ol{padding-left:22px}li{padding:3px 0}.files li{font-size:.92em}.go{color:var(--acc);font-weight:600;margin-left:6px}.go.big{font-size:1.15em;margin-left:0}
.st{border-left:4px solid var(--acc);padding:4px 12px;margin:12px 0}.st.done{opacity:.5}.step{font-size:1.05em}
.keepbox{background:var(--keep);border-left:5px solid var(--keepb);padding:6px 12px;border-radius:6px;margin:8px 0}.keepbox li.done{opacity:.45}.ok{color:var(--ok)}
pre.copy{background:#f2f2f2;color:#222;padding:8px;border-radius:6px;white-space:pre-wrap;word-break:break-all;cursor:pointer;user-select:all;-webkit-user-select:all}
table{border-collapse:collapse;width:100%%;font-size:.92em}td,th{border-bottom:1px solid rgba(128,128,128,.25);padding:4px 6px;text-align:left;vertical-align:top}
code{word-break:break-all}details{margin:8px 0}summary{cursor:pointer}textarea{display:none}.warn{color:#B71C1C;font-weight:600}tr.done,li.done{opacity:.45}
body.one section.cls{display:none}body.one section.cls.cur{display:block}.hl{outline:3px solid #F9A825;outline-offset:4px}
</style></head><body class='one'><div class='w'><div class='bar'><b>TidyUP Companion</b><button id='nx' title='Key: n'>Do the Next Step (n)</button>%s<a href='#' id='all'>Show all</a><span style='margin-left:auto;font-size:.85em'>made %s</span></div>
<section><p><b>A companion to TidyUP</b>, the Canvas tool in every course that lists unused files. One class at a time: Blueprint first, then Fall, then Spring. In each class, before every <b>Delete Selected</b>, untick the orange <b>KEEP</b> list: TidyUP cannot see question banks (it says so) and does not know what is graded, Roll Call, synced or linked. Do the Next Step (or the key n) jumps to the next unticked step. Ticks are kept in this browser.</p>
<p class='mut'>The KEEP lists hold: question bank pictures and the course card (step 2); Roll Call, every assignment, quiz and discussion (no gradebook on this Mac proves one has no submissions, so all stay), *No Publish and Instructor Use Only pages, Syllabus pages, question banks, pages another page links, and Blueprint content (step 4).</p>
<p class='mut'>Sizes: %s.</p></section>%s</div>
<script>
function cp(e){navigator.clipboard.writeText(e.innerText);e.style.background='#C8E6C9'}
function cpt(b){var t=b.parentNode.querySelector('textarea');navigator.clipboard.writeText(t.value);b.textContent='Copied';setTimeout(function(){b.textContent='Copy HTML'},1500)}
var K='cfclean2';var s={};try{s=JSON.parse(localStorage.getItem(K)||'{}')}catch(e){}
function mark(r,on){var p=r.classList.contains('step')?r.closest('.st'):(r.closest('li,tr')||r);if(p)p.classList.toggle('done',on)}
document.querySelectorAll('[data-id]').forEach(function(r){var c=r.matches('input')?r:r.querySelector('input');if(!c)return;var id=r.getAttribute('data-id');
if(s[id]){c.checked=true;mark(r,true)}c.addEventListener('change',function(){s[id]=c.checked;mark(r,c.checked);try{localStorage.setItem(K,JSON.stringify(s))}catch(e){}})});
var secs=[].slice.call(document.querySelectorAll('section.cls'));
function show(sec){secs.forEach(function(x){x.classList.toggle('cur',x===sec)});document.querySelectorAll('.bar a[href^="#c"]').forEach(function(a){a.classList.toggle('on',sec&&a.getAttribute('href')==='#'+sec.id)})}
function next(){var st=[].slice.call(document.querySelectorAll('section.cls label.step input')).filter(function(c){return !c.checked})[0];
document.querySelectorAll('.hl').forEach(function(x){x.classList.remove('hl')});if(!st){alert('Every step is ticked.');return}
var sec=st.closest('section');show(sec);var b=st.closest('.st');b.classList.add('hl');b.scrollIntoView({block:'center'})}
document.getElementById('nx').onclick=next;document.addEventListener('keydown',function(e){if(e.key==='n'&&!e.metaKey&&!e.ctrlKey&&e.target.tagName!=='INPUT')next()});
document.querySelectorAll('.bar a[href^="#c"]').forEach(function(a){a.onclick=function(e){e.preventDefault();document.body.classList.add('one');show(document.querySelector(a.getAttribute('href')));window.scrollTo(0,0)}});
document.getElementById('all').onclick=function(e){e.preventDefault();document.body.classList.toggle('one')};
document.querySelectorAll('.nextc').forEach(function(b){b.onclick=function(){var i=secs.indexOf(b.closest('section'));if(secs[i+1]){show(secs[i+1]);window.scrollTo(0,0)}}});
show(secs[0]);
</script></body></html>""" % ("".join(nav), stamp, ", ".join("%s %s to about %s" % (c, mb(w), mb(a)) for c, w, a in totals), "".join(sections))
    open(out, "w").write(page)
    print(json.dumps(dict(out=out, classes=summary, blueprint_files=len(bp_rows))))


if __name__ == "__main__":
    main()
