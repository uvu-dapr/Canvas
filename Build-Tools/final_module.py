#!/usr/bin/env python3
"""final_module.py: the final exam in a module of its own, and Instructor Use Only names (DAPR Canvas Standards
2026-10-06 v01, §6.9 item 6, §11d, §0 Instructor Use Only names).

Adam, 2026-10-06: "Final exam should never be in with the final project so that can be its own module. It can be the
week before final exam start in every single class and I can have the study guide that's in there." And: "I start
things off with the Asterix no publish and Colon" (Instructor Use Only pages are "*No Publish: <Title>").

    python3 final_module.py <unzipped package folder> --opens 2026-11-30 [--week 15] [--dry]

  * The module holding the final exam quiz: when it also holds other work (a final mix, a final project), the exam
    pieces move to a new module "Final Exam" (the quiz, a study guide, pages and slides titled "Final Exam: ..."), with
    the class's own divider words; the old module loses "& Final Exam" / "and Final Exam" from its title.
  * The Final Exam module opens the Monday given (--opens, 7:00 AM UTC is midnight Mountain standard time, the
    week before finals); with --week and module labels in use ("Week NN: ..."), its title says that week.
  * Pages in the Instructor Use Only module are named "*No Publish: <Title>" (module item, page <title>).
Edits module_meta.xml and page heads as text (never through an XML library, Platform Reference 22a). Fails closed: if
the quiz is not found exactly once, nothing is written.
"""
import sys, re, os, hashlib, argparse, html

def gid(*parts): return "g" + hashlib.md5("|".join(parts).encode()).hexdigest()

def field(item, tag):
    m = re.search(r"<%s>([^<]*)</%s>" % (tag, tag), item)
    return html.unescape(m.group(1)) if m else ""

def set_field(block, tag, value):
    v = html.escape(value, quote=False)
    if re.search(r"<%s>[^<]*</%s>" % (tag, tag), block):
        return re.sub(r"<%s>[^<]*</%s>" % (tag, tag), lambda m: "<%s>%s</%s>" % (tag, v, tag), block, count=1)
    return block.replace("</title>", "</title><%s>%s</%s>" % (tag, v, tag), 1)

def no_publish(t):
    """'Instructor: Course Schedule Notes [Do Not Publish]' -> '*No Publish: Course Schedule Notes'"""
    if t.startswith("*No Publish:"): return t
    s = re.sub(r"\s*-?\s*\[\s*do not publish\s*\]\s*", " ", t, flags=re.I).strip()
    # place labels go (an M06, an Orientation or Instructor prefix); the rest of the title stays as written
    s = re.sub(r"^(instructor|m\d+|module \d+|orientation)\s*:\s*", "", s, flags=re.I)
    s = re.sub(r"^(instructor|m\d+)\s*:\s*", "", s, flags=re.I)
    s = re.sub(r"\s*-\s*instructor$", " (Instructor)", s, flags=re.I).strip(" -")
    return "*No Publish: " + s

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir"); ap.add_argument("--opens", required=True); ap.add_argument("--week", type=int); ap.add_argument("--utc-hour", type=int, default=7)   # 7 = midnight MST, 6 = midnight MDT
    ap.add_argument("--dry", action="store_true"); ap.add_argument("--rename-graded", action="store_true")   # templates only: never rename live work students took (16a)
    a = ap.parse_args()
    mm_path = os.path.join(a.dir, "course_settings", "module_meta.xml")
    s = open(mm_path, encoding="utf-8").read()
    mods = list(re.finditer(r'<module identifier="([^"]+)">[\s\S]*?</module>', s))
    report = []
    # 1. the final exam's module
    def is_exam(it):
        return field(it, "content_type") == "Quizzes::Quiz" and re.search(r"final exam", field(it, "title"), re.I) and not re.search(r"alt \d|study", field(it, "title"), re.I)
    hits = [(m, it) for m in mods for it in re.findall(r'<item identifier="[^"]+">[\s\S]*?</item>', m.group(0)) if is_exam(it)]
    if len(hits) != 1: sys.exit("FAIL: found %d final exam quizzes in module_meta.xml; nothing written" % len(hits))
    mod, quiz = hits[0]
    block = mod.group(0)
    items = re.findall(r'<item identifier="[^"]+">[\s\S]*?</item>', block)
    def exam_piece(it):
        t, ct = field(it, "title"), field(it, "content_type")
        if it == quiz: return True
        if ct == "Quizzes::Quiz" and re.search(r"final exam", t, re.I): return True   # its Alt 1, Alt 2 go with it (Standards 9.1b)
        if ct == "WikiPage" and re.search(r"study guide|^final exam\b|^final:\s*final exam\b", t, re.I) and not re.search(r"mix|project", t, re.I): return True
        if ct == "ExternalUrl" and re.search(r"^final exam\b", t, re.I): return True
        return False
    # the study guide of a combined module ("Final Mix and Final Exam: Study Guide") is the exam's
    exam = [it for it in items if exam_piece(it) or (field(it, "content_type") == "WikiPage" and re.search(r"study guide", field(it, "title"), re.I))]
    divs = [it for it in items if field(it, "content_type") == "ContextModuleSubHeader"]
    other = [it for it in items if it not in exam and it not in divs and not re.search(r"overview", field(it, "title"), re.I)]
    title = field(block, "title")
    label = re.match(r"^(Week \d+:\s*)", title)
    words = [field(d, "title") for d in divs]
    study = next((w for w in words if w.lower() == "study"), "STUDY" if any(w.isupper() for w in words) else "Study")
    graded = next((w for w in words if w.lower() == "graded work"), "GRADED WORK" if study.isupper() else "Graded Work")
    new_title = ("Week %02d: " % a.week if (label and a.week) else "") + "Final Exam"
    opens = None if a.opens == "none" else "%sT%02d:00:00Z" % (a.opens, a.utc_hour)   # "none": a template with no dates yet
    if not other:
        # already its own module: its title and opening only
        nb = set_field(block, "title", new_title)
        if opens: nb = set_field(nb, "unlock_at", opens)
        s = s.replace(block, nb, 1)
        report.append("Final Exam module already separate: now '%s', opens %s" % (new_title, a.opens))
    else:
        mid = gid(mod.group(1), "final-exam-module")
        pos = int(field(block, "position") or "0")
        def item(ct, t, indent, ref=None, keep=None):
            if keep:   # an existing item moved over: same identifier (Canvas matches it), new indent
                return re.sub(r"<indent>[^<]*</indent>", "<indent>%d</indent>" % indent, keep)
            return ('<item identifier="%s">\n<content_type>%s</content_type>\n<workflow_state>unpublished</workflow_state>\n<title>%s</title>\n<new_tab/>\n<position>0</position>\n<indent>%d</indent>\n<link_settings_json>null</link_settings_json>\n</item>'
                    % (gid(mid, t), ct, html.escape(t, quote=False), indent))
        pages = [it for it in exam if field(it, "content_type") != "Quizzes::Quiz"]
        new_items = ([item("ContextModuleSubHeader", study, 0)] + [item(None, None, 1, keep=p) for p in pages] if pages else []) \
            + [item("ContextModuleSubHeader", graded, 0), item(None, None, 1, keep=quiz)]
        new_items = [re.sub(r"<position>\d+</position>", "<position>%d</position>" % (i + 1), x) for i, x in enumerate(new_items)]
        nm = ('<module identifier="%s">\n    <title>%s</title>%s\n    <workflow_state>unpublished</workflow_state>\n    <position>%d</position>\n    <require_sequential_progress>false</require_sequential_progress>\n    <locked>false</locked>\n    <items>\n      %s\n    </items>\n  </module>'
              % (mid, html.escape(new_title, quote=False), "<unlock_at>%s</unlock_at>" % opens if opens else "", pos + 1, "\n      ".join(new_items)))
        ob = block
        for it in exam: ob = ob.replace(it, "", 1)
        old_title = re.sub(r"\s*(&|and)\s*Final Exam\b", "", title)
        old_title = re.sub(r"\bFinal Project and Final Exam\b", "Final Project", old_title)
        ob = set_field(ob, "title", old_title)
        s = s.replace(block, ob + "\n  " + nm, 1)
        # later modules move down one place
        report.append("split '%s' into '%s' (%d item(s) left) and '%s' (%s), opens %s"
                      % (title, old_title, len(other), new_title, ", ".join(field(x, "title") for x in exam), a.opens))
    # 1b. what stays in the project module drops "and Final Exam" from its name: pages and slide links always, graded
    # work only in a template (--rename-graded); a live package's taken work is renamed by hand in Canvas (Standards 16a)
    strip = lambda t: re.sub(r"\s*(&|and)\s*Final Exam(?=:)", "", re.sub(r"^Final:\s*(?=Final Mix)", "", t))
    by_hand = []
    for m in re.finditer(r'<module identifier="[^"]+">[\s\S]*?</module>', s):
        if re.search(r"final exam$", field(m.group(0), "title"), re.I): continue
        b = m.group(0); nb = b
        for it in re.findall(r'<item identifier="[^"]+">[\s\S]*?</item>', b):
            t, ct = field(it, "title"), field(it, "content_type")
            n = strip(t)
            if n == t: continue
            if ct in ("Assignment", "Quizzes::Quiz", "DiscussionTopic") and not a.rename_graded: by_hand.append((t, n)); continue
            nb = nb.replace(it, set_field(it, "title", n), 1)
            ref = field(it, "identifierref")
            for root, _, files in os.walk(a.dir):
                for f in files:
                    if not f.endswith((".html", ".xml")) or f in ("module_meta.xml", "imsmanifest.xml"): continue
                    pth = os.path.join(root, f); h = open(pth, encoding="utf-8").read()
                    if ref and ref in h[:4000] and html.escape(t, quote=False) in h:
                        h2 = h.replace("<title>%s</title>" % html.escape(t, quote=False), "<title>%s</title>" % html.escape(n, quote=False))
                        if h2 != h and not a.dry: open(pth, "w", encoding="utf-8").write(h2)
            report.append("renamed '%s' -> '%s'" % (t, n))
        s = s.replace(b, nb, 1)
    for t, n in by_hand: report.append("rename by hand in Canvas (work students took): '%s' -> '%s'" % (t, n))
    # 2. Instructor Use Only page names
    pages_changed = []
    for m in re.finditer(r'<module identifier="[^"]+">[\s\S]*?</module>', s):
        if "Instructor Use Only" not in field(m.group(0), "title"): continue
        b = m.group(0); nb = b
        for it in re.findall(r'<item identifier="[^"]+">[\s\S]*?</item>', b):
            if field(it, "content_type") != "WikiPage": continue
            t = field(it, "title"); n = no_publish(t)
            if n != t:
                nb = nb.replace(it, set_field(it, "title", n), 1)
                pages_changed.append((field(it, "identifierref"), t, n))
        s = s.replace(b, nb, 1)
    # page heads carry the title too
    for ref, t, n in pages_changed:
        for f in os.listdir(os.path.join(a.dir, "wiki_content")):
            p = os.path.join(a.dir, "wiki_content", f)
            h = open(p, encoding="utf-8").read()
            if 'content="%s"' % ref not in h[:3000]: continue
            h2 = re.sub(r"<title>[^<]*</title>", lambda _: "<title>%s</title>" % html.escape(n, quote=False), h, count=1)
            if not a.dry: open(p, "w", encoding="utf-8").write(h2)
        report.append("renamed '%s' -> '%s'" % (t, n))
    # an older package also names items in the manifest's organizations tree: the same titles there (preflight compares them)
    if pages_changed:
        mp = os.path.join(a.dir, "imsmanifest.xml"); man = open(mp, encoding="utf-8").read(); m2 = man
        for ref, t, n in pages_changed:
            m2 = re.sub(r'(identifierref="%s"[^>]*>\s*<title>)[^<]*(</title>)' % re.escape(ref), lambda m: m.group(1) + html.escape(n, quote=False) + m.group(2), m2)
        if m2 != man and not a.dry: open(mp, "w", encoding="utf-8").write(m2)
    # positions 1..n in file order
    k = [0]
    def renum(m):
        k[0] += 1
        return re.sub(r"(<position>)\d+(</position>)", r"\g<1>%d\g<2>" % k[0], m.group(0), count=1)
    s = re.sub(r'<module identifier="[^"]+">\s*<title>[\s\S]*?<position>\d+</position>', renum, s)
    if not a.dry: open(mm_path, "w", encoding="utf-8").write(s)
    print("\n".join(report) or "nothing to change")

if __name__ == "__main__":
    main()
