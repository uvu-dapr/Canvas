#!/usr/bin/env python3
"""blueprint_copies.py: find and take out class copies of Blueprint content (Standards 0b.6, Adam 2026-10-05).

Adam: "you've got a bug where all the orientation stuff for course orientation gets thrown into from the blueprint
course, which is wrong". The Blueprint (Unified Class Content) already gives every class its Essentials pages and
quizzes; a class package that carries its own copies, renamed ("Orientation: Course Legend" for "Essentials: 3E) Course
Legend"), shows students everything twice. Titles alone miss a renamed copy, so this compares words.

Reference: every page and quiz in a "(Unified Class Content)" module of the class's live export, plus the Blueprint's own
newest export. Empty Blueprint placeholders (the per-class "Orientation: Prerequisites" and "Course Description") are
not references: each class writes its own.

    python3 blueprint_copies.py plan  <package.imscc> <live export.imscc> [--json out.json]
    python3 blueprint_copies.py apply <package.imscc> <live export.imscc> <out.imscc>

apply never overwrites. It removes each copy (resource, files, module items) and points links to it at the Blueprint
page it copies, by that page's address in the live course.
"""
import sys, os, re, html, json, zipfile, glob, shutil, tempfile

BLUEPRINT = "/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses/Universal Class Content/Canvas/Canvas Templates/-Canvas Entire Course"
PAGE_MATCH = 0.6     # share of words (Jaccard) that makes a page a copy; real class pages score under 0.4
QUIZ_MATCH = 0.5


def words(t):
    t = re.sub(r"(?s)<head.*?</head>", "", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", html.unescape(t))).lower()
    return set(re.findall(r"[a-z][a-z']{3,}", t))


def U(s):
    return " ".join(html.unescape(s or "").split())


def read_items(path):
    """title -> dict(kind, file, slug, words, rid) for pages and quizzes, and the module each identifier sits in"""
    z = zipfile.ZipFile(path)
    names = z.namelist()
    man = z.read("imsmanifest.xml").decode("utf8", "ignore")
    rid_of = {m.group(2): m.group(1) for m in re.finditer(r'<resource identifier="([^"]+)"[^>]*href="([^"]+)"', man)}
    mm = z.read("course_settings/module_meta.xml").decode("utf8", "ignore") if "course_settings/module_meta.xml" in names else ""
    mod_of = {}
    for m in re.finditer(r'<module identifier="[^"]+">\s*<title>([^<]*)</title>(.*?)</module>', mm, re.S):
        for r in re.findall(r"<identifierref>([^<]+)</identifierref>", m.group(2)):
            mod_of[r] = U(m.group(1))
    out = {}
    for n in names:
        if n.startswith("wiki_content/") and n.endswith(".html"):
            t = z.read(n).decode("utf8", "ignore")
            m = re.search(r"<title>([^<]*)", t)
            if not m:
                continue
            rid = rid_of.get(n, "")
            out.setdefault(("page", U(m.group(1))), dict(kind="page", title=U(m.group(1)), file=n, slug=n[13:-5], words=words(t), rid=rid, module=mod_of.get(rid, "")))
        elif n.endswith(".qti") or n.endswith("/assessment_qti.xml"):
            t = z.read(n).decode("utf8", "ignore")
            m = re.search(r'<assessment[^>]*title="([^"]*)"', t)
            if not m:
                continue
            rid = n.split("/")[-1].split(".")[0] if n.endswith(".qti") else n.split("/")[0]
            out.setdefault(("quiz", U(m.group(1))), dict(kind="quiz", title=U(m.group(1)), file=n, slug=None, words=words(t), rid=rid, module=mod_of.get(rid, "")))
    return out


def references(export):
    ref = {}
    for k, v in read_items(export).items():
        if "Unified Class Content" in v["module"] and len(v["words"]) >= 20:
            ref[k] = v
    full = [f for f in glob.glob(os.path.join(BLUEPRINT, "*.imscc")) if "blu" in f.lower() and "LIVE" not in f and os.path.getsize(f) > 50e6]
    if full:
        for k, v in read_items(max(full, key=os.path.getmtime)).items():
            if len(v["words"]) >= 20 and k not in ref:
                v = dict(v, slug=None)   # its address in the class is unknown; links fall back to the title
                ref[k] = v
    return ref


def plan(pkg, export):
    ref = references(export)
    copies = []
    for k, v in read_items(pkg).items():
        if "Unified Class Content" in v["module"] or "Instructor Use Only" in v["module"]:
            continue
        if len(v["words"]) < 20:
            continue
        best, bt = 0.0, None
        for rk, rv in ref.items():
            if rk[0] != v["kind"]:
                continue
            j = len(v["words"] & rv["words"]) / max(1, len(v["words"] | rv["words"]))
            if j > best:
                best, bt = j, rv
        if bt is not None and best >= (PAGE_MATCH if v["kind"] == "page" else QUIZ_MATCH):
            copies.append(dict(kind=v["kind"], title=v["title"], file=v["file"], slug=v["slug"], rid=v["rid"], module=v["module"],
                               copies=bt["title"], copies_slug=bt["slug"], share=round(best, 2)))
    # a quiz on Blueprint pages: almost all its words are in Blueprint pages and almost none only in the class's own pages
    # (2020 v84: the two Orientation quizzes 0.87 and 0.90 Blueprint, 0.04 and 0.06 own; every module quiz 0.20 or more own)
    items = read_items(pkg)
    gone = {c["title"] for c in copies}
    bpw = set().union(*[rv["words"] for rk, rv in ref.items() if rk[0] == "page"] or [set()])
    own = set().union(*[v["words"] for k, v in items.items() if k[0] == "page" and v["title"] not in gone] or [set()])
    for k, v in items.items():
        if k[0] != "quiz" or "Unified Class Content" in v["module"] or len(v["words"]) < 20:
            continue
        w = v["words"]
        inbp, only = len(w & bpw) / len(w), len((w & own) - bpw) / len(w)
        if inbp >= 0.8 and only < 0.1:
            copies.append(dict(kind="quiz", title=v["title"], file=v["file"], slug=None, rid=v["rid"], module=v["module"],
                               copies="the Essentials quizzes (its questions are on Blueprint pages)", copies_slug=None, share=round(inbp, 2)))
    return sorted(copies, key=lambda c: c["title"])


def apply(pkg, export, out, copies):
    assert not os.path.exists(out), "never overwrite: " + out
    w = tempfile.mkdtemp(prefix="bpcopies-")
    zipfile.ZipFile(pkg).extractall(w)
    shutil.rmtree(os.path.join(w, "__MACOSX"), ignore_errors=True)
    rp = lambda p: os.path.join(w, p)
    man = open(rp("imsmanifest.xml"), encoding="utf8").read()
    mm = open(rp("course_settings/module_meta.xml"), encoding="utf8").read()
    for c in copies:
        rid = c["rid"]
        m = re.search(r'<resource\b[^>]*identifier="%s"[^>]*>.*?</resource>' % re.escape(rid), man, re.S) if rid else None
        files = re.findall(r'<file href="([^"]+)"', m.group(0)) if m else [c["file"]]
        deps = re.findall(r'<dependency identifierref="([^"]+)"', m.group(0)) if m else []
        for x in [rid] + deps:
            if not x:
                continue
            dm = re.search(r'<resource\b[^>]*identifier="%s"[^>]*>.*?</resource>' % re.escape(x), man, re.S)
            if dm:
                files += re.findall(r'<file href="([^"]+)"', dm.group(0))
            man = re.sub(r'\s*<resource\b[^>]*identifier="%s"[^>]*>.*?</resource>' % re.escape(x), "", man, flags=re.S)
            man = re.sub(r'\s*<item identifier="[^"]+" identifierref="%s">\s*<title>[^<]*</title>\s*</item>' % re.escape(x), "", man)
            mm = re.sub(r'\s*<item identifier="[^"]+">(?:(?!</item>).)*?<identifierref>%s</identifierref>.*?</item>' % re.escape(x), "", mm, flags=re.S)
            shutil.rmtree(rp(x), ignore_errors=True)
            for f in ("non_cc_assessments/%s.xml.qti" % x,):
                if os.path.exists(rp(f)):
                    os.remove(rp(f))
        for f in set(files + [c["file"]]):
            if f and os.path.isfile(rp(f)) and not f.startswith("web_resources/"):
                os.remove(rp(f))
    open(rp("imsmanifest.xml"), "w", encoding="utf8").write(man)
    open(rp("course_settings/module_meta.xml"), "w", encoding="utf8").write(mm)
    # links to a removed page go to the Blueprint page it copied (its address in this class), else lose the link
    relinked = []
    for root, _, fs in os.walk(w):
        for f in fs:
            if not f.endswith((".html", ".xml", ".qti")):
                continue
            p = os.path.join(root, f)
            t = open(p, encoding="utf8", errors="ignore").read()
            t0 = t
            for c in copies:
                if c["kind"] != "page" or not c["slug"]:
                    continue
                new = c["copies_slug"]
                pat = re.compile(r"\$WIKI_REFERENCE\$/pages/%s(?=[\"'#?])" % re.escape(c["slug"]))
                if new:
                    t = pat.sub("$WIKI_REFERENCE$/pages/" + new, t)
                else:
                    t = re.sub(r"<a\b[^>]*href=\"\$WIKI_REFERENCE\$/pages/%s[^\"]*\"[^>]*>(.*?)</a>" % re.escape(c["slug"]), r"\1", t, flags=re.S)
            if t != t0:
                open(p, "w", encoding="utf8").write(t)
                relinked.append(os.path.relpath(p, w))
    tmp = out + ".partial"
    cwd = os.getcwd()
    os.chdir(w)
    os.system('zip -q -r -D -X "%s" . -x "*.DS_Store" "__MACOSX/*"' % tmp)
    os.chdir(cwd)
    os.rename(tmp, out)
    shutil.rmtree(w, ignore_errors=True)
    return relinked


if __name__ == "__main__":
    cmd, pkg, export = sys.argv[1], sys.argv[2], sys.argv[3]
    cs = plan(pkg, export)
    if cmd == "plan":
        for c in cs:
            print("%-5s %.2f  %-60s copies  %s" % (c["kind"], c["share"], c["title"][:60], c["copies"]))
        print("%d Blueprint copies" % len(cs))
        if "--json" in sys.argv:
            json.dump(cs, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1)
    elif cmd == "apply":
        rl = apply(pkg, export, sys.argv[4], cs)
        print(json.dumps(dict(out=sys.argv[4], removed=[c["title"] for c in cs], relinked=rl), indent=1))
