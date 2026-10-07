"""nametime.py <pkg folder>...: J141 (Adam, 2026-10-07): every assignment asks for the student's name and the time the
work took, at the top of the hand-in. A note at the top of What to Submit (or under the title when a page has none) on
every assignment students hand in, and Name and Time lines under the title of every one-click worksheet."""
import sys, os, re, glob
ICON = "https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/Callout_Note.png"
NOTE = ('<div style="background-color:#e3f2fd; border-left:4px solid #0d47a1; margin:16px 0; padding:12px 14px;">'
        '<img src="%s" alt="Note" width="44" height="44" style="vertical-align:middle; margin-right:10px;">'
        '<strong style="vertical-align:middle;">Name and time at the top</strong>'
        '<div style="margin-left:54px; margin-top:4px;">At the top of what you hand in, put your name and how long this assignment '
        'took you, start to finish, in hours and minutes. For an audio or video hand-in, type both in the submission comment box. '
        'The time is not graded; it tells me how long the work really takes.</div></div>') % ICON
LINES = ('<p style="margin:0 0 4px 0;"><strong>Name:</strong> &nbsp;</p>'
         '<p style="margin:0 0 20px 0;"><strong>Time this assignment took (hours and minutes):</strong> &nbsp;</p>')
SKIP = ("none", "not_graded", "on_paper", "external_tool", "")
for pkg in sys.argv[1:]:
    man = open(os.path.join(pkg, "imsmanifest.xml"), encoding="utf-8").read()
    pages = set()
    for res in re.findall(r"<resource\b.*?</resource>", man, re.S):
        files = re.findall(r'<file href="([^"]+)"', res)
        # assignment settings: assignment_settings.xml, or an assignments/<name>.xml whose root is <assignment> (DAPR 3340)
        st = [f for f in files if f.endswith(".xml") and os.path.exists(os.path.join(pkg, f))
              and re.sub(r"<\?xml[^>]*\?>\s*", "", open(os.path.join(pkg, f), encoding="utf-8").read(400), count=1).lstrip().startswith("<assignment")]
        if not st or not os.path.exists(os.path.join(pkg, st[0])): continue
        x = open(os.path.join(pkg, st[0]), encoding="utf-8").read()
        sub = (re.search(r"<submission_types>([^<]*)", x) or [0, ""])[1]
        if (re.search(r"<workflow_state>deleted", x)) or all(t in SKIP for t in sub.split(",")): continue
        pages |= {f for f in files if f.endswith(".html")}
    notes = lines = 0
    for f in glob.glob(os.path.join(pkg, "**/*.html"), recursive=True):
        rel = os.path.relpath(f, pkg); s = o = open(f, encoding="utf-8").read()
        # worksheet: Name and Time right under the worksheet's title, inside the one-click box
        def ws(m):
            body = m.group(0)
            if "Time this assignment took" in body: return body
            # under the worksheet's title (a paragraph that is only a bold title, within the first two), else at the top
            ps = list(re.finditer(r"<p[^>]*>.*?</p>", body, re.S))[:2]
            t = next((m for m in ps if re.fullmatch(r"<p[^>]*><strong>[^<]*</strong></p>", m.group(0))), None)
            at = t.end() if t else body.find(">") + 1
            return body[:at] + LINES + body[at:]
        s = re.sub(r'<div style="[^"]*user-select:\s*all[^"]*">.*?</div>', ws, s, flags=re.S)
        if rel in pages and "Name and time at the top" not in s:
            m = re.search(r"<strong[^>]*>What to Submit</strong></div>", s)
            if m: s = s[:m.end()] + "\n" + NOTE + s[m.end():]
            else:
                m = re.search(r"</h2>", s)
                if m: s = s[:m.end()] + "\n" + NOTE + s[m.end():]
                else: print("NO PLACE", rel); continue
        if s != o:
            notes += ("Name and time at the top" in s) and ("Name and time at the top" not in o)
            lines += s.count("Time this assignment took") - o.count("Time this assignment took")
            open(f, "w", encoding="utf-8").write(s)
    print(pkg, "assignment pages", len(pages), "notes added", notes, "worksheets", lines)
