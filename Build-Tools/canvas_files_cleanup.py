#!/usr/bin/env python3
"""canvas_files_cleanup.py: what to delete in Canvas so each class's export is as small as it can be.

Adam, 2026-10-05: "nothing should be more than 100 MB for a canvas export. Give me what I need to clean up online ...
All file use should be put on cloudflare ... [quiz images stay: they cannot be on Cloudflare or GitHub]".

A Canvas export carries every file in the course's Files, used or not. For each class's newest export this sorts every
file into:
  card      the course card picture (course_settings.xml image_identifier_ref, Settings ▸ Course Details ▸ Image):
            ALWAYS stays; deleting it blanks the Dashboard card (J308, 2026-10-15 audit). A small JPEG is offered instead.
  quiz      used by a quiz or a question bank: stays in Canvas Files (quizzes block outside images, Standards 8.1)
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


TIDYUP = 347769   # the TidyUP LTI tool (account level, the same id in every course): Files ▸ Unused Files, Folders tab
# Every class in Adam's order (Blueprint first, Fall, Spring last; K109) with its live course number, so a class with no
# export on this Mac still gets its TidyUP link
CLASSES = [("Blueprint", 655823), ("2000", 636866), ("2020", 643734), ("2255", 642395), ("3340", 641145),
           ("2010", 655746), ("3255", 651912), ("3345", 651955)]
SAFE = ("unused", "copy", "bankleft")
KEEP_FOLDERS = ("assessment_questions", "course_image")   # Canvas's own folders: bank pictures and the course card


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
    bp_rows, bp_docs, sections, nav, totals, summary = {}, {}, [], [], [], []
    bp_twins = set()
    known = [c for c, _ in CLASSES]
    for cls in known + sorted(set(given) - set(known)):
        name = "DAPR " + cls if cls != "Blueprint" else "Blueprint"
        cid = int(given[cls][2]) if cls in given else dict(CLASSES)[cls]
        tidy = CANVAS % cid + "external_tools/%d" % TIDYUP
        if cls not in given:
            sections.append("<section id='c%s'><h2>%s</h2><p><a class='go' href='%s' target='_blank'>Open TidyUP</a></p>"
                            "<p class='mut'>No export of this live course on this Mac yet, so nothing is listed. Before you tick anything in TidyUP, export it (Settings ▸ Export Course Content), save it in the class's "
                            "-Canvas Entire Course folder, and this page lists which files a question bank uses (TidyUP cannot see that).</p></section>" % (cls, name, esc(tidy)))
            nav.append("<a href='#c%s'>%s <small>no export</small></a>" % (cls, name))
            continue
        exp = given[cls][0]
        is_bp = cls == "Blueprint"
        z, files, docs, ctx = read(exp)
        rows = classify(files, docs, ctx)
        tw = twins(docs, ctx)
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
        in_folder = {r["file"] for _, rs in folders for r in rs}
        loose = [r for r in rows if r["kind"] in SAFE and r["file"] not in in_folder]
        # the gap TidyUP warns about: "Question banks cannot be scanned for file usage"
        bankonly = [r for r in rows if r["kind"] == "quiz" and (not r["users"] or all(u["kind"] == "bank" for u in r["users"]))]
        # the same picture in more than one place: which copy is safe
        dup = collections.defaultdict(list)
        for r in rows:
            dup[ctx["sig"][r["file"]]].append(r)
        dups = sorted([rs for rs in dup.values() if len(rs) > 1 and any(r["kind"] in SAFE for r in rs)], key=lambda rs: -rs[0]["bytes"] * len(rs))
        summary.append(dict(cls=name, now=whole, after=after, folders=[(f, len(rs), sum(r["bytes"] for r in rs)) for f, rs in folders],
                            loose=len(loose), bank_only=len(bankonly), dup_groups=len(dups), twin_titles=len(tw),
                            twin_extra=sum(len(bs) - 1 for _, bs in tw), card=sorted(ctx["card"])))
        h = ["<section id='c%s'><h2>%s <small>%s now, about %s after</small></h2>" % (cls, name, mb(whole), mb(after))]
        h.append("<p><a class='go big' href='%s' target='_blank'>Open TidyUP</a> <span class='mut'>for %s. Deleting is your click in TidyUP or Files; this page only says what is safe.</span></p>" % (esc(tidy), name))
        h.append("<p class='mut'>From <b>%s</b>. Every file below was checked against every page, assignment, discussion, quiz and question bank in that export, by path and by file id.%s</p>"
                 % (esc(os.path.basename(exp)), "" if is_bp else " Do the Blueprint first: after its Sync, some of these may already be gone."))
        for c in sorted(ctx["card"]):
            small = os.path.join(SMALL, name, os.path.splitext(os.path.basename(c))[0] + ".jpg")
            h.append("<p class='keep'><b>Keep</b> <code>%s</code> (%s): the <b>course card picture</b> on the Dashboard (Settings ▸ Course Details ▸ Image). "
                     "TidyUP may list it as unused: do not tick it.%s</p>" % (esc(c), mb(files.get(c, 0)),
                     (" A small JPEG of it is ready to swap in there: <code>%s</code>." % esc(small)) if os.path.exists(small) else ""))
        # (c) first, so it is read before any ticking
        h.append("<h3 class='stop'>Do NOT delete: TidyUP shows these as unused, but a question bank uses them (%d)</h3>" % len(bankonly))
        if bankonly:
            h.append("<p class='mut'>TidyUP says \"Question banks cannot be scanned for file usage\", so it lists these as unused. Leave them unticked: deleting one breaks a bank question.</p><ul class='files'>"
                     + "".join("<li><code>%s</code> <span class='mut'>%s · %s</span></li>" % (esc(r["file"]), mb(r["bytes"]), esc(who(r["users"])) if r["users"] else "named by its file id") for r in bankonly) + "</ul>")
        else:
            h.append("<p class='mut'>None in this export.</p>")
        # (b) folders
        h.append("<h3>Delete these folders <span class='mut'>(TidyUP ▸ Folders tab, biggest first)</span></h3>")
        if folders:
            h.append("<p class='mut'>Every file in each folder (subfolders too) is in no module and linked by nothing.</p><ul>")
            for f, rs in folders:
                h.append("<li data-id='%s|folder|%s'><label><input type='checkbox'> <b>%s</b></label> <span class='mut'>%s, %d file(s)</span></li>" % (cls, esc(f), esc(f), mb(sum(r["bytes"] for r in rs)), len(rs)))
            h.append("</ul>")
        else:
            h.append("<p class='mut'>No whole folder can go.</p>")
        # (d) single files
        h.append("<h3>Safe to delete: single files TidyUP shows <span class='mut'>(outside those folders)</span></h3>")
        if loose:
            h.append("<p class='mut'>Linked by nothing. A \"-N\" name in assessment_questions is a byte for byte copy of the original named beside it (made by the Oct 7 Blueprint import); the original stays.</p><ul class='files'>")
            for r in loose:
                h.append("<li data-id='%s|file|%s'><label><input type='checkbox'> <code>%s</code></label> <span class='mut'>%s%s</span></li>"
                         % (cls, esc(r["file"]), esc(r["file"]), mb(r["bytes"]), (" · copy of %s, which stays" % esc(os.path.basename(r["orig"]))) if r["orig"] else ""))
            h.append("</ul>")
        else:
            h.append("<p class='mut'>None.</p>")
        if dups:
            h.append("<details><summary><b>Same file in more than one place (%d)</b>: TidyUP shows each copy with its own date; this says which copy is safe</summary><table><tr><th>File</th><th>Copies</th></tr>" % len(dups))
            for rs in dups:
                cells = []
                for r in sorted(rs, key=lambda r: r["file"]):
                    if r["kind"] in SAFE:
                        verdict = "<b>safe</b>" + (" (whole folder goes)" if r["file"] in in_folder else "")
                    elif r["kind"] == "card":
                        verdict = "<b class='warn'>keep: course card</b>"
                    else:
                        verdict = "<b class='warn'>keep</b>: " + (esc(who(r["users"])) if r["users"] else "named by its file id")
                    cells.append("<code>%s</code>: %s" % (esc(os.path.dirname(r["file"]) or "(top)"), verdict))
                h.append("<tr><td>%s <span class='mut'>%s each</span></td><td>%s</td></tr>" % (esc(os.path.basename(rs[0]["file"])), mb(rs[0]["bytes"]), "<br>".join(cells)))
            h.append("</table>%s</details>" % ("<p class='mut'>Every copy safe: tick both in TidyUP.</p>" if all(all(r["kind"] in SAFE for r in rs) for rs in dups) else ""))
        # twin banks
        if tw:
            extra = sum(len(bs) - 1 for _, bs in tw)
            h.append("<h3>Twin question banks <span class='mut'>(Quizzes ▸ ⋮ ▸ Manage Question Banks; TidyUP does not do banks)</span></h3>")
            if is_bp:
                h.append("<p class='mut'><b>Do this first.</b> Each title below is in the Blueprint more than once, word for word the same (the Oct 7 Blueprint import added a copy). "
                         "Open <a class='go' href='%squestion_banks' target='_blank'>Manage Question Banks</a>, open each copy of the title, and delete the "
                         "<b>later copy</b>: the one whose address ends in the <b>higher number</b>. Keep the first. Then <b>Blueprint ▸ Sync</b>, so every class loses its synced copy too. "
                         "No quiz draws from any of these banks.</p>" % (CANVAS % cid))
            else:
                h.append("<p class='mut'>After the Blueprint Sync, open <a class='go' href='%squestion_banks' target='_blank'>Manage Question Banks</a> "
                         "here: for each title below keep <b>one</b> copy (the first, lowest number in its address) and delete the later ones that are still left. "
                         "No quiz in this class draws from any of these banks.</p>" % (CANVAS % cid))
            h.append("<table><tr><th></th><th>Bank title (exact)</th><th>Questions</th><th>Copies now</th><th>Delete</th>%s</tr>" % ("" if is_bp else "<th>Also twinned in the Blueprint</th>"))
            for title, bs in tw:
                h.append("<tr data-id='%s|bank|%s'><td><input type='checkbox'></td><td><b>%s</b></td><td>%d</td><td>%d</td><td>%d (the later %s)</td>%s</tr>"
                         % (cls, esc(title), esc(title), bs[0]["items"], len(bs), len(bs) - 1, "one" if len(bs) == 2 else "ones",
                            "" if is_bp else "<td>%s</td>" % ("yes: the Sync removes one" if title in bp_twins else "no: delete here")))
            h.append("</table><p class='mut'>%d bank title(s), %d extra copies. Banks that share a title but differ, and the Unfiled Questions banks Canvas makes for quiz questions, are not listed: they stay.</p>" % (len(tw), extra))
        # old pages and live files (rare now)
        old = collections.OrderedDict()
        for r in rows:
            if r["kind"] == "oldcopy":
                for u in r["users"]:
                    if u["kind"] == "page" and "roll call" not in u["title"].lower():
                        o = old.setdefault(u["path"], dict(u=u, bytes=0, n=0)); o["bytes"] += r["bytes"]; o["n"] += 1
        if old:
            h.append("<h3>Old pages holding files</h3><p class='mut'>Pages in no module. Delete the page first (&#8942; ▸ Delete); its files show up above after the next export.</p><ul>")
            for o in sorted(old.values(), key=lambda o: -o["bytes"]):
                u = o["u"]
                h.append("<li data-id='%s|old|%s'><label><input type='checkbox'> <b>%s</b></label> <span class='mut'>%d file(s), %s</span> <a class='go' href='%s' target='_blank'>Open in Canvas</a></li>"
                         % (cls, esc(u["path"]), esc(u["title"]), o["n"], mb(o["bytes"]), esc(CANVAS % cid + "pages/" + u["slug"])))
            h.append("</ul>")
        left = [r for r in rows if r["kind"] == "live" and not r["blueprint"]]
        if left:
            h.append("<h3>Move to Cloudflare</h3><ul>" + "".join("<li>%s <span class='mut'>%s, on %s</span></li>" % (esc(r["file"]), mb(r["bytes"]), esc(", ".join(u["title"] for u in r["users"][:2]))) for r in left[:30]) + "</ul>")
        h.append("<h3>Then export again</h3><p class='mut'>Settings ▸ Export Course Content ▸ Create Export, save it in the class's -Canvas Entire Course folder. Canvas Preview reads it and this page updates.</p></section>")
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
        bp.append("<section id='cBlueprintPages'><h2>Blueprint pages: move their pictures to Cloudflare <small>%d files, %s in every class</small></h2>" % (len(bp_rows), mb(size)))
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
    page = """<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Canvas Files Cleanup</title><style>
:root{--bg:#EDEAE4;--card:#fff;--ink:#212121;--mut:#5B6770;--acc:#0D47A1;--keep:#E8F5E9}
@media (prefers-color-scheme:dark){:root{--bg:#1E1E1E;--card:#2A2A2A;--ink:#EEE;--mut:#A9B3BA;--acc:#8CC8F0;--keep:#1F3324}}
body{font-family:-apple-system,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);margin:0;padding:16px}.w{max-width:980px;margin:0 auto}
.bar{position:sticky;top:0;background:#1B5E20;color:#fff;padding:8px 14px;border-radius:8px;z-index:2;display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.bar a{color:#fff;text-decoration:none;background:rgba(255,255,255,.15);padding:2px 10px;border-radius:12px}
section{background:var(--card);border-radius:10px;padding:10px 16px;margin:14px 0}h2 small,.mut{color:var(--mut);font-weight:400;font-size:.9em}
ul{list-style:none;padding-left:6px}li{padding:3px 0}.files li{font-size:.92em}.fold{margin:6px 0}.go{color:var(--acc);font-weight:600;margin-left:6px}
pre.copy{background:#f2f2f2;color:#222;padding:8px;border-radius:6px;white-space:pre-wrap;word-break:break-all;cursor:pointer;user-select:all;-webkit-user-select:all}
table{border-collapse:collapse;width:100%%;font-size:.92em}td,th{border-bottom:1px solid rgba(128,128,128,.25);padding:4px 6px;text-align:left;vertical-align:top}
.keep{background:var(--keep);padding:8px 10px;border-radius:6px;border-left:5px solid #2E7D32}code{word-break:break-all}
h3.stop{color:#B71C1C}.go.big{font-size:1.1em;margin-left:0}details{margin:8px 0}summary{cursor:pointer}
textarea{display:none}.warn{color:#B71C1C;font-weight:600}.done{opacity:.45}button{margin-left:6px}
</style></head><body><div class='w'><div class='bar'><b>Canvas Files Cleanup</b>%s<span style='margin-left:auto;font-size:.85em'>made %s</span></div>
<section><p><b>A companion to TidyUP</b> (the Canvas tool in every course that lists unused files). Every Canvas export carries all of the course's Files, used or not, so these steps take each class from its size now to about the size shown. Blueprint first (it fixes every class at once), then Fall, then Spring. TidyUP cannot see question banks, so each class first lists the files it shows as unused that a bank uses: never tick those. Ticks here are kept in this browser.</p>
<p class='mut'><b>Never listed here:</b> the course card picture, graded work (assignments, quizzes, discussions), Roll Call, and any file a page, assignment, quiz or a bank a quiz draws from links.</p>
<p class='mut'>Sizes: %s.</p></section>%s</div>
<script>
function cp(e){navigator.clipboard.writeText(e.innerText);e.style.background='#C8E6C9'}
function cpt(b){var t=b.parentNode.querySelector('textarea');navigator.clipboard.writeText(t.value);b.textContent='Copied';setTimeout(function(){b.textContent='Copy HTML'},1500)}
var K='cfclean';var s={};try{s=JSON.parse(localStorage.getItem(K)||'{}')}catch(e){}
document.querySelectorAll('[data-id]').forEach(function(r){var c=r.matches('input')?r:r.querySelector('input');if(!c)return;var id=r.getAttribute('data-id');
if(s[id]){c.checked=true;r.classList.add('done')}c.addEventListener('change',function(){s[id]=c.checked;(r.closest('li,div,tr')||r).classList.toggle('done',c.checked);try{localStorage.setItem(K,JSON.stringify(s))}catch(e){}})});
</script></body></html>""" % ("".join(nav), stamp, ", ".join("%s %s to about %s" % (c, mb(w), mb(a)) for c, w, a in totals), "".join(sections))
    open(out, "w").write(page)
    print(json.dumps(dict(out=out, classes=summary, blueprint_files=len(bp_rows))))


if __name__ == "__main__":
    main()
