import sys, os, re, html, shutil, random, hashlib
W = sys.argv[1]
MM = os.path.join(W, "course_settings/module_meta.xml"); MAN = os.path.join(W, "imsmanifest.xml")
mm = open(MM).read(); man = open(MAN).read()
U = html.unescape
def gid(*p): return "g" + hashlib.md5("|".join(("2000-j132",) + p).encode()).hexdigest()
def modblock(t): return next(b for b in re.findall(r'<module identifier="[^"]+">.*?</module>', mm, re.S) if U(re.search(r"<title>([^<]*)</title>", b).group(1)) == t)
def items(b): return re.findall(r'<item identifier=.*?</item>', b, re.S)
def ititle(it): return U(re.search(r"<title>([^<]*)</title>", it).group(1))
def renum(lst): return "\n      ".join(re.sub(r"<position>\d+</position>", "<position>%d</position>" % k, it, count=1) for k, it in enumerate(lst, 1))
def settitle(x, old, new): return x.replace("<title>%s</title>" % html.escape(old, quote=False), "<title>%s</title>" % html.escape(new, quote=False))
EQ_T, DYN_T = "Dynamics: EQ", "Dynamics: Compressors/Limiters & Expanders/Gates"
QUIZ_T = "Dynamics: Quiz - Compressors, Limiters, Expanders & Gates"
eq = modblock("DAW: EQ & Dynamics"); comp = modblock("Processing: Compression"); gates = modblock("Processing: Gates & Expanders")
E = {ititle(i): i for i in items(eq)}; Cm = {ititle(i): i for i in items(comp)}; G = {ititle(i): i for i in items(gates)}
# EQ module: EQ only
NEWPG = "DAW: Read - Filter Slopes, Shelves and Bells"; NEWREF = gid("page", NEWPG)
newitem = re.sub(r'<item identifier="[^"]+">', '<item identifier="%s">' % gid("item", NEWPG), E["DAW: EQ"], count=1)
newitem = re.sub(r"<identifierref>[^<]*</identifierref>", "<identifierref>%s</identifierref>" % NEWREF, settitle(newitem, "DAW: EQ", NEWPG))
newitem = re.sub(r"<workflow_state>[^<]*</workflow_state>", "<workflow_state>unpublished</workflow_state>", newitem, count=1)
eq_items = [E["EQ & Dynamics: Slides (PDF)"], E["STUDY"], settitle(E["DAW: Overview - EQ & Dynamics"], "DAW: Overview - EQ & Dynamics", "DAW: Overview - EQ"),
            E["DAW: Exploring The DAW"], E["DAW: EQ"], newitem, E["GRADED WORK"], E["DAW: Assignment - Four EQ Moves, Four Reasons"], E["DAW: Quiz - Filters & EQ"]]
eq2 = settitle(eq.split("<items>")[0], "DAW: EQ & Dynamics", EQ_T) + "<items>\n      " + renum(eq_items) + "\n    </items>\n  </module>"
mm = mm.replace(eq, eq2)
# Dynamics module: compression + gates + dynamic based processing, one quiz
dyn_items = [Cm["Compression: Slides (PDF)"], Cm["STUDY"], settitle(G["Processing: Overview - Gates & Expanders"], "Processing: Overview - Gates & Expanders", "Processing: Overview - Dynamics"),
             E["DAW: Dynamic Based Processing"]] + [Cm[t] for t in ["Processing: Understanding the How & Why of Compression", "Processing: Read - Attack and Release", "Processing: Read - Reading Gain Reduction",
             "Processing: Read - Four Compressors and Why They Sound Different", "Processing: Read - Parallel Compression", "Processing: Watch More Compression Videos"]] \
           + [G[t] for t in ["Processing: Read - How a Gate Works", "Processing: Read - Expanders & Downward Expansion", "Processing: Read - Key Input & Side-Chain Filters"]] \
           + [Cm["GRADED WORK"], Cm["Processing: Assignment - Three Sources, Three Settings"], G["Processing: Assignment - Gate the Toms, Expand the Vocal"],
              settitle(Cm["Processing: Quiz - Compression"], "Processing: Quiz - Compression", QUIZ_T)]
comp2 = settitle(comp.split("<items>")[0], "Processing: Compression", DYN_T) + "<items>\n      " + renum(dyn_items) + "\n    </items>\n  </module>"
mm = mm.replace(comp, comp2).replace(gates, "")
mm = re.sub(r"\n\s*\n(\s*<module)", r"\n\1", mm)
# merged quiz: compression quiz + the gates quiz's questions, 50 points, due Fri 12 Mar
QC, QG = "g59e6b19ad897ef16359d7a21018f6efa", "g0dd6868ffb3331c28fc1d5bbe4f52f35"
for name in ("%s/assessment_qti.xml", "non_cc_assessments/%s.xml.qti"):
    c = open(os.path.join(W, name % QC)).read(); g = open(os.path.join(W, name % QG)).read()
    gi = re.findall(r'<item ident=.*?</item>', g, re.S); ci = re.findall(r'<item ident=.*?</item>', c, re.S)
    keep_c = [1, 2, 5, 7, 8, 9, 10, 11, 15, 17, 21, 23, 25]; keep_g = [1, 3, 4, 8, 10, 12, 13, 16, 17, 18, 19, 23]
    first = c.find("<item ident="); last = c.rfind("</item>") + len("</item>")
    c = c[:first] + "\n".join([ci[k - 1] for k in keep_c] + [gi[k - 1] for k in keep_g]) + c[last:]
    c = c.replace('title="Processing: Quiz - Compression"', 'title="%s"' % html.escape(QUIZ_T))
    assert len(re.findall(r'<item ident=', c)) == 25
    open(os.path.join(W, name % QC), "w").write(c)
m = os.path.join(W, QC, "assessment_meta.xml"); s = open(m).read()
s = s.replace("<title>Processing: Quiz - Compression</title>", "<title>%s</title>" % html.escape(QUIZ_T, quote=False))
s = re.sub(r"<due_at>[^<]*</due_at>", "<due_at>2027-03-12T16:00:00Z</due_at>", s); open(m, "w").write(s)
# gates assignment opens with the module and is due Fri 12 Mar
ga = re.search(r"<identifierref>([^<]*)</identifierref>", G["Processing: Assignment - Gate the Toms, Expand the Vocal"]).group(1)
for f in os.listdir(os.path.join(W, ga)):
    if f.endswith(".xml"):
        p = os.path.join(W, ga, f); t = open(p).read()
        t = re.sub(r"<due_at>[^<]*</due_at>", "<due_at>2027-03-12T16:00:00Z</due_at>", t); t = re.sub(r"<unlock_at>[^<]*</unlock_at>", "<unlock_at>2027-02-22T07:00:00Z</unlock_at>", t)
        open(p, "w").write(t)
# drop the gates quiz from the package
r = re.search(r'\s*<resource identifier="%s"[^>]*>.*?</resource>' % QG, man, re.S); dep = re.search(r'<dependency identifierref="([^"]+)"', r.group(0)).group(1)
man = man.replace(r.group(0), ""); man = man.replace(re.search(r'\s*<resource identifier="%s"[^>]*>.*?</resource>' % dep, man, re.S).group(0), "")
shutil.rmtree(os.path.join(W, QG)); os.remove(os.path.join(W, "non_cc_assessments/%s.xml.qti" % QG))
# EQ quiz: question 25 (a compressor question) becomes an EQ one
QE = "geb6519539e3e793608a162cbe37bf56c"
for name in ("%s/assessment_qti.xml", "non_cc_assessments/%s.xml.qti"):
    p = os.path.join(W, name % QE); t = open(p).read(); its = re.findall(r'<item ident=.*?</item>', t, re.S); old = its[24]
    assert "compressor" in U(U(old)).lower()
    rnd = random.Random("eq25"); ids = [str(rnd.randint(1000, 9999)) for _ in range(4)]
    ch = ["Everything below about 100 Hz, raised by up to 3 dB", "Only 100 Hz itself, in a narrow band", "Everything above 100 Hz", "Nothing until the signal passes a threshold"]
    new = re.sub(r'<item ident="[^"]+" title="[^"]*"', '<item ident="%s" title="Low shelf"' % gid("eq25"), old, count=1)
    new = re.sub(r"(<mattext texttype=\"text/html\">).*?(</mattext>)", lambda x: x.group(1) + html.escape("<div><p>You set a low shelf at 100 Hz and boost it 3 dB. Which frequencies change?</p></div>", quote=False) + x.group(2), new, count=1, flags=re.S)
    labels = re.findall(r'<response_label ident="[^"]+">.*?</response_label>', new, re.S)
    new = new.replace("".join([]), "")
    rc = re.search(r"<render_choice>.*?</render_choice>", new, re.S).group(0)
    nl = "<render_choice>" + "".join('\n                <response_label ident="%s">\n                  <material>\n                    <mattext texttype="text/plain">%s</mattext>\n                  </material>\n                </response_label>' % (i, c) for i, c in zip(ids, ch)) + "\n              </render_choice>"
    new = new.replace(rc, nl)
    new = re.sub(r"(<fieldlabel>original_answer_ids</fieldlabel>\s*<fieldentry>)[^<]*", r"\g<1>" + ",".join(ids), new)
    new = re.sub(r'(<varequal respident="response1">)[^<]*', r"\g<1>" + ids[0], new)
    new = re.sub(r'<respcondition continue="No">\s*<conditionvar>\s*<varequal[^>]*>[^<]*</varequal>\s*</conditionvar>\s*<setvar[^>]*>100</setvar>\s*</respcondition>', '<respcondition continue="No">\n              <conditionvar>\n              <varequal respident="response1">%s</varequal>\n              </conditionvar>\n              <setvar action="Set" varname="SCORE">100</setvar>\n            </respcondition>' % ids[0], new, count=1)
    open(p, "w").write(t.replace(old, new))
GH = "https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/"
K = "#1b5e20"
def h3(t): return '<h3 style="color:%s; font-size:1.2em; border-bottom:2px solid %s; padding-bottom:4px; margin-top:32px;">%s</h3>\n' % (K, K, t)
def fig(f, alt, cap): return '<div style="margin:20px 0;">\n  <img src="%s%s" alt="%s" style="max-width:100%%; height:auto; border:1px solid #cccccc; border-radius:6px;" loading="lazy">\n  <p style="font-size:0.9em; color:#616161; margin:8px 0 0 0;">%s</p>\n</div>\n' % (GH, f, alt, cap)
body = ('<div style="font-family:Arial, Helvetica, sans-serif; max-width:900px; margin:0 auto; color:#212121; line-height:1.6; background-color:#ffffff; padding:0 12px;">\n'
 '<h2 style="background-color:%s; color:#ffffff; padding:16px 20px; font-size:1.4em; border-radius:4px; margin-top:0;">%s</h2>\n' % (K, NEWPG)
 + "<p>Every EQ move is one of three shapes: a <strong>filter</strong> that removes everything past a point, a <strong>shelf</strong> that lifts or lowers everything past a point by a set amount, or a <strong>bell</strong> that lifts or lowers a band around a center. Knowing which shape a problem needs is most of the job.</p>\n"
 + h3("Filters and Their Slopes")
 + "<p>A <strong>high pass filter</strong> (also called a low cut) lets the highs pass and removes the lows; a <strong>low pass filter</strong> (a high cut) does the opposite. The <strong>cutoff</strong> frequency is where the filter is already <strong>3 dB down</strong>, so a 100 Hz high pass still lets some 80 Hz through. How fast it removes what is past the cutoff is the <strong>slope</strong>, in dB per octave.</p>\n"
 + fig("EQ_High_Pass_Slopes.jpg", "High pass filters at 100 Hz with 6, 12, 18 and 24 dB per octave slopes, each 3 dB down at the cutoff", "The same 100 Hz high pass at four slopes. One octave below the cutoff (50 Hz) a 6 dB slope has removed about 6 dB more; a 24 dB slope about 24 dB more.")
 + "<table style=\"width:100%; border-collapse:collapse; margin:12px 0 16px 0;\"><caption>Filter slopes and when to use them</caption><thead><tr>"
 + "".join('<th style="background-color:%s; color:#ffffff; padding:8px 10px; text-align:left;" scope="col">%s</th>' % (K, x) for x in ["Slope", "Sounds", "Good for"]) + "</tr></thead><tbody>\n"
 + "".join("<tr>" + "".join('<td style="padding:8px 10px; border-bottom:1px solid #e0e0e0;">%s</td>' % c for c in r) + "</tr>\n" for r in [["6 dB per octave", "Gentle and natural", "Softening a lot of low or high end without an obvious edge"], ["12 dB per octave", "The everyday choice", "Clearing rumble and mud from most tracks"], ["18 and 24 dB per octave", "Steep, surgical", "Removing subsonic rumble or bleed while keeping everything just above the cutoff"]])
 + "</tbody></table>\n"
 + h3("Shelves and Bells")
 + fig("EQ_Shelf_vs_Bell.jpg", "Low and high shelves lifting everything past a point, and narrow and wide bells around 1 kHz", "A shelf lifts or lowers everything beyond its point by the same amount; a bell changes a band, narrow or wide depending on Q.")
 + "<ul>\n<li><strong>Shelf:</strong> a low shelf changes everything below its frequency, a high shelf everything above it, by the gain you set. Use a high shelf to add air to a vocal or a low shelf to tame a boomy guitar without touching the mids.</li>\n"
 + "<li><strong>Bell:</strong> lifts or lowers a band around its center frequency. <strong>Q</strong> sets the width: a high Q is narrow (one ringing note on a snare), a low Q is wide (a broad, gentle tone change).</li>\n"
 + "<li><strong>Cut before you boost.</strong> Cutting the problem is usually cleaner than boosting around it, and every 6 dB of boost asks the amplifier and the mix bus for four times the power at those frequencies.</li>\n</ul>\n"
 + h3("Which Shape for Which Problem")
 + "<ul>\n<li>Rumble, stand thumps or handling noise below the instrument: <strong>high pass</strong>.</li>\n<li>Hiss or harsh fizz above the instrument: <strong>low pass</strong>.</li>\n<li>Too much or too little low end or top overall: <strong>shelf</strong>.</li>\n<li>One ringing note, a boxy band or a nasal spot: <strong>bell</strong>, narrow for a ring, wider for a tone.</li>\n</ul>\n</div>")
open(os.path.join(W, "wiki_content/daw-read-filter-slopes-shelves-and-bells.html"), "w").write('<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n<title>%s</title>\n<meta name="identifier" content="%s"/>\n<meta name="editing_roles" content="teachers"/>\n<meta name="workflow_state" content="unpublished"/>\n<meta name="editor_type" content="rce"/>\n</head>\n<body>\n%s\n</body>\n</html>\n' % (NEWPG, NEWREF, body))
man = man.replace("</resources>", '  <resource identifier="%s" type="webcontent" href="wiki_content/daw-read-filter-slopes-shelves-and-bells.html">\n      <file href="wiki_content/daw-read-filter-slopes-shelves-and-bells.html" />\n    </resource>\n  </resources>' % NEWREF, 1)
open(MM, "w").write(mm); open(MAN, "w").write(man)
# overview pages
C = "#0d47a1"
def ov(title, objectives, before, conclusion, img_html):
    h2 = lambda t: '<h2 style="color:%s; font-size:1.3em; border-bottom:2px solid %s; padding-bottom:4px; margin-top:32px;">%s</h2>' % (C, C, t)
    return ('<div style="font-family:Arial, Helvetica, sans-serif; max-width:900px; margin:0 auto; color:#212121; line-height:1.6; background-color:#ffffff; padding:0 12px;">\n\n'
            '<h2 style="background-color:%s; color:#ffffff; padding:16px 20px; font-size:1.4em; border-radius:4px;">%s</h2>%s\n\n' % (C, html.escape(title, quote=False), img_html)
            + h2("Learning Objectives") + "\n<p>Upon completing this module, you will be able to:</p>\n<ul>\n" + "".join("<li>%s</li>\n" % o for o in objectives) + "</ul>\n\n"
            + h2("Before Class") + "\n<p>Review the following before the class session:</p>\n<ul>\n" + "".join("<li>%s</li>\n" % b for b in before) + "</ul>\n\n"
            + h2("Module Conclusion") + "\n<p>Complete the following to finish this module:</p>\n<ul>\n" + "".join("<li>%s</li>\n" % c for c in conclusion) + "</ul>\n</div>")
def rewrite(fname, title, body):
    p = os.path.join(W, "wiki_content", fname); s = open(p).read()
    img = re.search(r'<div style="margin:0 0 24px 0;"><img[^>]*></div>|<img[^>]*>', s.split("<body>")[1]).group(0)
    s = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % html.escape(title, quote=False), s, count=1)
    s = s.split("<body>")[0] + "<body>\n" + body.replace("%IMG%", img) + "\n</body>\n</html>\n"
    open(p, "w").write(s)
rewrite("daw-overview-eq-dynamics.html", "DAW: Overview - EQ", ov("DAW: Overview - EQ",
    ["Explain what an equalizer does and read an EQ graph: frequency, gain and Q.", "Choose between high pass and low pass filters, shelves and bells for a given problem.", "Tell a parametric EQ from a graphic EQ and know when each is used.", "Apply EQ to individual tracks with a named reason for every cut and boost."],
    ["DAW: Exploring The DAW", "DAW: EQ", "DAW: Read - Filter Slopes, Shelves and Bells"], ["DAW: Assignment - Four EQ Moves, Four Reasons", "DAW: Quiz - Filters &amp; EQ (25 pts)"], "%IMG%"))
rewrite("processing-overview-gates-and-expanders.html", "Processing: Overview - Dynamics", ov("Processing: Overview - Dynamics",
    ["Explain what a compressor does with threshold, ratio, attack, release and makeup gain, and how a limiter differs.", "Read a gain reduction meter and choose a compressor type for a source.", "Explain how a gate and an expander work, including range, hold and hysteresis.", "Use key input and side-chain filters to control what opens a gate.", "Choose compression, limiting, expansion or gating for a given problem."],
    ["DAW: Dynamic Based Processing", "Processing: Understanding the How &amp; Why of Compression and the four compression readings", "Processing: Read - How a Gate Works, Expanders &amp; Downward Expansion, and Key Input &amp; Side-Chain Filters"],
    ["Processing: Assignment - Three Sources, Three Settings", "Processing: Assignment - Gate the Toms, Expand the Vocal", "Dynamics: Quiz - Compressors, Limiters, Expanders &amp; Gates (25 pts)"], "%IMG%"))
print("ok")
