"""J132 Fall: DAPR 2000 Fall gets the Spring v107 EQ / Dynamics split before Processing: Compression opens (Mon 12 Oct 2026).
dynamics_into_fall_2000_j132.py <Fall work folder (v105 unzipped)> <Spring v107 unzipped>"""
import sys, os, re, html, shutil
W, SP = sys.argv[1], sys.argv[2]
U = html.unescape
MM = os.path.join(W, "course_settings/module_meta.xml"); MAN = os.path.join(W, "imsmanifest.xml")
mm = open(MM).read(); man = open(MAN).read(); smm = open(os.path.join(SP, "course_settings/module_meta.xml")).read(); sman = open(os.path.join(SP, "imsmanifest.xml")).read()
def mods(s): return re.findall(r'<module identifier="[^"]+">.*?</module>', s, re.S)
def modblock(s, t): return next(b for b in mods(s) if U(re.search(r"<title>([^<]*)</title>", b).group(1)) == t)
def items(b): return re.findall(r'<item identifier=.*?</item>', b, re.S)
def ititle(it): return U(re.search(r"<title>([^<]*)</title>", it).group(1))
def iref(it): m = re.search(r"<identifierref>([^<]*)</identifierref>", it); return m.group(1) if m else None
def renum(lst): return "\n      ".join(re.sub(r"<position>\d+</position>", "<position>%d</position>" % k, it, count=1) for k, it in enumerate(lst, 1))
def settitle(x, old, new): return x.replace("<title>%s</title>" % html.escape(old, quote=False), "<title>%s</title>" % html.escape(new, quote=False))
def unpub(it): return re.sub(r"<workflow_state>[^<]*</workflow_state>", "<workflow_state>unpublished</workflow_state>", it, count=1)
def copy_res(ref):
    global man
    if 'identifier="%s"' % ref in man: return
    r = re.search(r'<resource identifier="%s"[^>]*>.*?</resource>' % re.escape(ref), sman, re.S).group(0)
    for f in re.findall(r'<file href="([^"]+)"', r):
        os.makedirs(os.path.dirname(os.path.join(W, f)), exist_ok=True); shutil.copy2(os.path.join(SP, f), os.path.join(W, f))
    man = man.replace("</resources>", "  " + r + "\n  </resources>", 1)
    for d in re.findall(r'<dependency identifierref="([^"]+)"', r): copy_res(d)
EQ_T, DYN_T, QUIZ_T = "Dynamics: EQ", "Dynamics: Compressors/Limiters & Expanders/Gates", "Dynamics: Quiz - Compressors, Limiters, Expanders & Gates"
seq, sdyn = modblock(smm, EQ_T), modblock(smm, DYN_T); SE = {ititle(i): i for i in items(seq)}; SD = {ititle(i): i for i in items(sdyn)}
eq, comp = modblock(mm, "DAW: EQ & Dynamics"), modblock(mm, "Processing: Compression")
E = {ititle(i): i for i in items(eq)}; Cm = {ititle(i): i for i in items(comp)}
EQPG, OV = "DAW: Read - Filter Slopes, Shelves and Bells", "Processing: Overview - Dynamics"
GATES = ["Processing: Read - How a Gate Works", "Processing: Read - Expanders & Downward Expansion", "Processing: Read - Key Input & Side-Chain Filters"]
GA = "Processing: Assignment - Gate the Toms, Expand the Vocal"
for it in [SE[EQPG], SD[OV], SD[GA]] + [SD[g] for g in GATES]: copy_res(iref(it))
ga = iref(SD[GA]); comp_as = iref(Cm["Processing: Assignment - Three Sources, Three Settings"])
grp = re.search(r"<assignment_group_identifierref>([^<]*)<", open(os.path.join(W, comp_as, "assignment_settings.xml")).read()).group(1)
for f in os.listdir(os.path.join(W, ga)):
    if f.endswith(".xml"):
        p = os.path.join(W, ga, f); t = open(p).read()
        t = re.sub(r"<due_at>[^<]*</due_at>", "<due_at>2026-10-30T15:00:00Z</due_at>", t); t = re.sub(r"<unlock_at>[^<]*</unlock_at>", "<unlock_at>2026-10-12T06:00:00Z</unlock_at>", t)
        t = re.sub(r"<assignment_group_identifierref>[^<]*<", "<assignment_group_identifierref>%s<" % grp, t); t = re.sub(r"<workflow_state>[^<]*</workflow_state>", "<workflow_state>unpublished</workflow_state>", t)
        open(p, "w").write(t)
def href(m, ref): return re.search(r'<resource identifier="%s"[^>]*href="([^"]+)"' % ref, m).group(1)
fov = os.path.join(W, href(man, iref(E["DAW: Overview - EQ & Dynamics"]))); sov = os.path.join(SP, href(sman, iref(SE["DAW: Overview - EQ"])))
s = open(fov).read(); b = open(sov).read(); s = s[:s.index("<body>")] + b[b.index("<body>"):]
s = re.sub(r"<title>[^<]*</title>", "<title>DAW: Overview - EQ</title>", s, count=1); open(fov, "w").write(s)
div = lambda D, t: next(i for i in items(eq if D is E else comp) if ititle(i).lower() == t.lower() and "ContextModuleSubHeader" in i)
eq_items = [E["EQ & Dynamics: Slides (PDF)"], div(E, "Study"), settitle(E["DAW: Overview - EQ & Dynamics"], "DAW: Overview - EQ & Dynamics", "DAW: Overview - EQ"), E["DAW: Exploring The DAW"], E["DAW: EQ"],
            unpub(SE[EQPG]), div(E, "Graded Work"), E["DAW: Assignment - Four EQ Moves, Four Reasons"], E["DAW: Quiz - Filters & EQ"]]
mm = mm.replace(eq, settitle(eq.split("<items>")[0], "DAW: EQ & Dynamics", EQ_T) + "<items>\n      " + renum(eq_items) + "\n    </items>\n  </module>")
dyn_items = [Cm["Compression: Slides (PDF)"], div(Cm, "Study"), unpub(SD[OV]), E["DAW: Dynamic Based Processing"]] \
    + [Cm[t] for t in ["Processing: Understanding the How & Why of Compression", "Processing: Read - Attack and Release", "Processing: Read - Reading Gain Reduction", "Processing: Read - Four Compressors and Why They Sound Different", "Processing: Read - Parallel Compression", "Processing: Watch More Compression Videos"]] \
    + [unpub(SD[g]) for g in GATES] + [div(Cm, "Graded Work"), Cm["Processing: Assignment - Three Sources, Three Settings"], unpub(SD[GA]), settitle(Cm["Processing: Quiz - Compression"], "Processing: Quiz - Compression", QUIZ_T)]
mm = mm.replace(comp, settitle(comp.split("<items>")[0], "Processing: Compression", DYN_T) + "<items>\n      " + renum(dyn_items) + "\n    </items>\n  </module>")
QC = "g59e6b19ad897ef16359d7a21018f6efa"
for n in ("%s/assessment_qti.xml", "non_cc_assessments/%s.xml.qti"): shutil.copy2(os.path.join(SP, n % QC), os.path.join(W, n % QC))
m = os.path.join(W, QC, "assessment_meta.xml"); t = open(m).read()
t = t.replace("<title>Processing: Quiz - Compression</title>", "<title>%s</title>" % html.escape(QUIZ_T, quote=False)); t = re.sub(r"<due_at>[^<]*</due_at>", "<due_at>2026-10-30T15:00:00Z</due_at>", t)
open(m, "w").write(t)
# pages that name the old modules and quiz
DYNh, Qh = html.escape(DYN_T, quote=False), html.escape(QUIZ_T, quote=False)
for f in os.listdir(os.path.join(W, "wiki_content")):
    p = os.path.join(W, "wiki_content", f); s = open(p).read(); o = s
    s = s.replace("DAW: EQ &amp; Dynamics", "Dynamics: EQ").replace("Processing: Quiz - Compression", Qh).replace("Processing: Compression", DYNh)
    s = s.replace("Quiz - Compression, 25 pts, due Fri Oct 23", "Gate the Toms, Expand the Vocal, 25 pts, due Fri Oct 30 Quiz - Compressors, Limiters, Expanders &amp; Gates, 25 pts, due Fri Oct 30")
    if s != o: open(p, "w").write(s); print("renamed in", f)
open(MM, "w").write(mm); open(MAN, "w").write(man); print("ok")

# The Fall package is partial (no course_settings), so the gate assignment goes without its rubric link; the rubric stays in Spring v107.
