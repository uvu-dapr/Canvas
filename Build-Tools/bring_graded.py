#!/usr/bin/env python3
"""Bring the graded work into a pages-only LIVE package, so moving a module can move its due dates (Adam, 2026-10-01).

    python3 bring_graded.py <working folder> <full package .imscc or folder> [--live <Canvas export.imscc>] [--dry-run]

A pages-only package (Standards 16b) carries pages and modules but no quizzes or assignments, so Canvas Preview's
Week Planner could only list the due dates to change by hand. This copies every quiz, assignment and graded
discussion from the class's full package (the one already imported, whose identifiers are the ones Canvas matches,
Standards 16a) into the working folder, and links each one into the module of the same title, after the item it
followed in the full package:

- Items the full package carries (files and manifest resource): copied with the same identifier, so the import
  updates the live item in place. A due date moved in the Week Planner then moves in Canvas.
- Items the full package only links (taken work it left out on purpose): linked the same way, by the same id.
- With --live, any item whose id Canvas knows only as an export label (an id an import cannot match) is left out,
  copied or linked: importing it would add a second copy, or drop the link. It stays where it is in the live course
  and its date is changed in Canvas. Without --live nothing can be checked, so always pass it.
- Their assignment group and rubric references are dropped when the working folder has no assignment_groups.xml or
  rubrics.xml: Canvas then keeps each item's live group and rubric (a reference to a group the package does not
  carry would put the item in a new default group).
- Each module item gets a new identifier (the item lands in the new module; the old module keeps its own link until
  it is deleted).

- Modules are matched by title; when the live course still uses its older names ("Module 08: Dynamic Effects" for
  "Effects: Dynamic Effects", 2020 on 2026-10-01), by topic: numbers and "Module NN:" or "Week NN:" dropped, the words
  compared (best overlap wins), and a lab that matches nothing follows its numbered topic ("Module 08: Compression Lab"
  with "Module 08: Dynamic Effects"). Shared modules (Unified Class Content, Bonus, Instructor Use Only) are never
  matched. Every topic match is printed ("mapped: ... -> ...") so Adam can check it before the real run.
Never overwrites an item already in the working folder. Prints what it added, then RESULT.
"""
import os, re, sys, shutil, zipfile, tempfile, hashlib, html

def read(p): return open(p, encoding="utf-8").read()
def write(p, s): open(p, "w", encoding="utf-8").write(s)
def U(s): return " ".join(html.unescape(s).split())

def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    work, full = sys.argv[1], sys.argv[2]
    dry = "--dry-run" in sys.argv
    labels = set()
    if "--live" in sys.argv:
        z = zipfile.ZipFile(sys.argv[sys.argv.index("--live") + 1])
        labels = set(re.findall(r'identifier="([^"]+)"', z.read("imsmanifest.xml").decode("utf-8", "ignore")))
        if "course_settings/module_meta.xml" in z.namelist():
            labels |= set(re.findall(r'identifier="([^"]+)"', z.read("course_settings/module_meta.xml").decode("utf-8", "ignore")))
        # an id an earlier import stored is one Canvas matches even when the export also shows it (Adam, 2026-10-01:
        # "this file can contain the whole semester"; 3340's taken Introduction quiz could be placed after all)
        try:
            import subprocess, json
            out = subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "match_ids.py"), "stored",
                                  sys.argv[sys.argv.index("--live") + 1]], capture_output=True, text=True).stdout
            labels -= set(json.loads(out or "[]"))
        except Exception:
            pass
    tmp = None
    if os.path.isfile(full):
        tmp = tempfile.mkdtemp(prefix="bring_graded_")
        zipfile.ZipFile(full).extractall(tmp)
        src = tmp
    else:
        src = full
    try:
        run(work, src, dry, labels)
    finally:
        if tmp: shutil.rmtree(tmp, ignore_errors=True)

STOP = {"and", "the", "of", "with", "a", "an", "for", "in", "to", "on", "lab", "module", "week"}
SHARED = ("unified class content", "bonus", "instructor use only", "do not publish")

def words(t):
    """A title's topic words: numbers, "Module NN:" and small words dropped."""
    t = html.unescape(t).lower().replace("&", " and ")
    t = re.sub(r"^\\s*(module|week)\\s*\\d+\\s*[:\\-]?\\s*", "", t)
    return {w for w in re.findall(r"[a-z0-9]+", t) if w not in STOP and not w.isdigit()}

def same_word(x, y):
    """Mix and Mixing, Balance and Balancing, Arranging and Arrangement: one starts the other, or 5 letters agree."""
    return x.startswith(y) or y.startswith(x) or (len(x) >= 5 and len(y) >= 5 and x[:5] == y[:5])

def topic_match(title, wmods):
    """The package module an older live module name means, or None: at least 60% of the live title's words found,
    ties going to the module with the fewest other words ("Dynamic Effects" over "Frequency Dynamics & Side-Chains")."""
    if any(k in title.lower() for k in SHARED): return None
    a = words(title)
    if not a: return None
    scored = []
    for t in wmods:
        b = words(t)
        if not b: continue
        hit = sum(1 for x in a if any(same_word(x, y) for y in b))
        scored.append((hit / len(a), hit / len(b), t))
    scored.sort(reverse=True)
    if not scored or scored[0][0] < 0.6 or (len(scored) > 1 and scored[1][:2] == scored[0][:2]): return None
    return scored[0][2]

def run(work, src, dry, labels=set()):
    sman, wman = read(os.path.join(src, "imsmanifest.xml")), read(os.path.join(work, "imsmanifest.xml"))
    smm, wmm_path = read(os.path.join(src, "course_settings/module_meta.xml")), os.path.join(work, "course_settings/module_meta.xml")
    wmm = read(wmm_path)
    keep_groups = os.path.exists(os.path.join(work, "course_settings/assignment_groups.xml"))
    keep_rubrics = os.path.exists(os.path.join(work, "course_settings/rubrics.xml"))
    wres = set(re.findall(r'<resource identifier="([^"]+)"', wman))
    sres = {m.group(1): m.group(0) for m in re.finditer(r'(?s)<resource identifier="([^"]+)"[^>]*>.*?</resource>|<resource identifier="([^"]+)"[^>]*/>', sman) if m.group(1)}
    wmods = {U(m.group(2)): m.group(1) for m in re.finditer(r'(?s)<module identifier="([^"]+)">\s*<title>([^<]*)</title>', wmm)}
    graded = ("Assignment", "Quizzes::Quiz", "DiscussionTopic")
    added, linked, skipped, new_res = [], [], [], []
    copied = set()

    def copy_resource(rid):
        """The resource, its files and its dependencies (a quiz's _meta, a discussion's topicMeta)."""
        if rid in wres or rid in copied or rid not in sres: return
        block = sres[rid]
        copied.add(rid)
        for href in re.findall(r'<file href="([^"]+)"', block):
            a, b = os.path.join(src, href), os.path.join(work, href)
            if not os.path.exists(a): continue
            if os.path.exists(b): continue
            if not dry:
                os.makedirs(os.path.dirname(b), exist_ok=True)
                shutil.copy2(a, b)
                if b.endswith((".xml",)) and (not keep_groups or not keep_rubrics):
                    x = read(b); y = x
                    if not keep_groups: y = re.sub(r"\s*<assignment_group_identifierref>[^<]*</assignment_group_identifierref>", "", y)
                    if not keep_rubrics:
                        y = re.sub(r"\s*<rubric_identifierref>[^<]*</rubric_identifierref>", "", y)
                        y = re.sub(r"\s*<rubric_external_identifier>[^<]*</rubric_external_identifier>", "", y)
                    if y != x: write(b, y)
        new_res.append(block)
        for dep in re.findall(r'<dependency identifierref="([^"]+)"', block): copy_resource(dep)
        # the other half of a quiz or discussion: a resource whose files sit in this one's folder
        for other, ob in sres.items():
            if other != rid and other not in copied and re.search(r'<file href="%s/' % re.escape(rid), ob): copy_resource(other)

    # older live names: by topic, and a lab that matches nothing follows the module with its number
    smods = [U(m.group(2)) for m in re.finditer(r'(?s)<module identifier="([^"]+)">\s*<title>([^<]*)</title>', smm)]
    def num(t): n = re.match(r"\s*(?:module|week)\s*(\d+)", t, re.I); return int(n.group(1)) if n else None
    by_title = {}
    for t in smods:
        if t in wmods or any(k in t.lower() for k in SHARED): continue
        hit = topic_match(t, wmods)
        if hit: by_title[t] = hit
    for t in smods:
        if t in wmods or t in by_title or any(k in t.lower() for k in SHARED) or num(t) is None: continue
        same = [by_title[o] for o in smods if o in by_title and num(o) == num(t)]
        if same and all(x == same[0] for x in same): by_title[t] = same[0]
    for t, w in by_title.items(): print("mapped: %s -> %s" % (t, w))
    out = wmm
    for m in re.finditer(r'(?s)<module identifier="([^"]+)">\s*<title>([^<]*)</title>(.*?)</module>', smm):
        title = U(m.group(2)); target = wmods.get(title) or wmods.get(by_title.get(title, ""))
        items = list(re.finditer(r'(?s)<item identifier="([^"]+)">(.*?)</item>', m.group(3)))
        prev_title = None
        for it in items:
            body = it.group(2)
            ct = (re.search(r"<content_type>([^<]*)", body) or [None, ""])[1]
            ititle = U((re.search(r"<title>([^<]*)", body) or [None, ""])[1])
            ref = (re.search(r"<identifierref>([^<]*)", body) or [None, ""])[1]
            if ct not in graded or not ref:
                prev_title = ititle; continue
            if target is None:
                skipped.append("%s (no module named %s in this package)" % (ititle, title)); continue
            wmod = re.search(r'(?s)(<module identifier="%s">.*?)(</items>|</module>)' % re.escape(target), out)
            if re.search(r"<identifierref>%s</identifierref>" % re.escape(ref), wmod.group(1)):
                prev_title = ititle; continue          # already linked here
            # an id Canvas knows only as an export label can't be matched by an import: copying the item would add a
            # second copy beside the live one (2026-10-01: none of 2020's 55 graded ids were stored, so bringing them
            # in from the export would have added 48 copies). Checked before copying, not only for linked work.
            if ref in labels:
                skipped.append("%s (made in Canvas, so an import would add a copy: change its date in Canvas)" % ititle); prev_title = ititle; continue
            if ref in sres: copy_resource(ref); added.append(ititle)
            else: linked.append(ititle)
            iid = "i" + hashlib.md5((target + ref).encode()).hexdigest()[:12]
            item = '<item identifier="%s">%s</item>' % (iid, body)
            # after the item it followed in the full package, else at the end of the module's items
            mod = wmod.group(1)
            spot = None
            if prev_title:
                for pm in re.finditer(r'(?s)<item identifier="[^"]+">.*?<title>([^<]*)</title>.*?</item>', mod):
                    if U(pm.group(1)) == prev_title: spot = wmod.start(1) + pm.end()
            if spot is None:
                spot = wmod.end(1)                      # just before </items> (or </module> when it has none)
                if wmod.group(2) == "</module>":
                    item = "<items>" + item + "</items>"
            out = out[:spot] + "\n      " + item + out[spot:]
            prev_title = ititle
    # renumber positions inside each module
    def renumber(mm):
        def mod(mx):
            n = [0]
            def pos(px): n[0] += 1; return "<position>%d</position>" % n[0]
            return re.sub(r"<position>\d+</position>", pos, mx.group(0))
        return re.sub(r'(?s)<module identifier="[^"]+">.*?</module>', mod, mm)
    out = renumber(out)
    if not dry:
        write(wmm_path, out)
        if new_res:
            wman2 = wman.replace("</resources>", "\n    " + "\n    ".join(new_res) + "\n  </resources>", 1)
            write(os.path.join(work, "imsmanifest.xml"), wman2)
    for t in added: print("added: " + t)
    for t in linked: print("linked (taken work, by its id): " + t)
    for t in skipped: print("skipped: " + t)
    print("RESULT: %d graded item(s) added, %d linked by id, %d skipped%s%s" % (len(added), len(linked), len(skipped),
          "" if keep_groups else "; their live assignment groups and rubrics are kept", " (dry run)" if dry else ""))

if __name__ == "__main__":
    main()
