import sys, os, re, html, hashlib, datetime, shutil, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pages import PAGES
from questions import P1_NEW, P2_NEW
W = sys.argv[1]
def gid(*p): return "g" + hashlib.md5("|".join(("2000-j133",) + p).encode()).hexdigest()
MM = os.path.join(W, "course_settings/module_meta.xml"); MAN = os.path.join(W, "imsmanifest.xml")
mm = open(MM).read(); man = open(MAN).read()
U = lambda s: html.unescape(s)
def modblock(title):
    return next(b for b in re.findall(r'<module identifier="[^"]+">.*?</module>', mm, re.S) if U(re.search(r"<title>([^<]*)</title>", b).group(1)) == title)
def items(b): return re.findall(r'<item identifier=.*?</item>', b, re.S)
def ititle(it): return U(re.search(r"<title>([^<]*)</title>", it).group(1))
def iref(it): m = re.search(r"<identifierref>([^<]*)</identifierref>", it); return m.group(1) if m else None
def find(b, t): return next(i for i in items(b) if ititle(i) == t)
# ---- date shifting for a module's graded items
def res_files(ref):
    r = re.search(r'<resource identifier="%s"[^>]*>(.*?)</resource>' % re.escape(ref), man, re.S)
    if not r: return []
    fs = re.findall(r'<file href="([^"]+)"', r.group(1))
    for d in re.findall(r'<dependency identifierref="([^"]+)"', r.group(1)): fs += res_files(d)
    return fs
def shift_file(f, days):
    p = os.path.join(W, f)
    if not p.endswith((".xml", ".qti")) or not os.path.exists(p): return 0
    s = open(p).read(); n = [0]
    def sh(m):
        d = datetime.datetime.strptime(m.group(2)[:19], "%Y-%m-%dT%H:%M:%S") + datetime.timedelta(days=days); n[0] += 1
        return m.group(1) + d.strftime("%Y-%m-%dT%H:%M:%S") + m.group(2)[19:] + m.group(3)
    s = re.sub(r"(<(?:due_at|unlock_at|lock_at|todo_date)>)(\d{4}-\d\d-\d\dT[^<]+)(</(?:due_at|unlock_at|lock_at|todo_date)>)", sh, s)
    open(p, "w").write(s); return n[0]
def move_module(title, new_unlock, days):
    global mm
    b = modblock(title)
    b2 = re.sub(r"<unlock_at>[^<]*</unlock_at>", "<unlock_at>%s</unlock_at>" % new_unlock, b, count=1)
    mm = mm.replace(b, b2); n = 0
    for it in items(b2):
        if re.search(r"<content_type>(Assignment|Quizzes::Quiz|DiscussionTopic)</content_type>", it):
            for f in set(res_files(iref(it))): n += shift_file(f, days)
    print("moved", title, "->", new_unlock, "dates shifted:", n)
move_module("Pro Tools: Introduction", "2027-01-11T07:00:00Z", -7)
move_module("Careers: Audio Careers", "2027-01-18T07:00:00Z", 7)
move_module("Monitoring: Psychoacoustics", "2027-02-15T07:00:00Z", 7)
# ---- new pages
newref = {}
for t, (slug, body) in PAGES.items():
    rid = gid("page", t); newref[t] = rid
    open(os.path.join(W, "wiki_content/%s.html" % slug), "w").write(
        '<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n<title>%s</title>\n<meta name="identifier" content="%s"/>\n<meta name="editing_roles" content="teachers"/>\n<meta name="workflow_state" content="unpublished"/>\n<meta name="editor_type" content="rce"/>\n</head>\n<body>\n%s\n</body>\n</html>\n' % (html.escape(t, quote=False), rid, body))
    man = man.replace("</resources>", '  <resource identifier="%s" type="webcontent" href="wiki_content/%s.html">\n      <file href="wiki_content/%s.html" />\n    </resource>\n  </resources>' % (rid, slug, slug), 1)
# ---- quizzes
Q1 = "g0fcd28152278e8efa4b3e494d727d012"
KEEP1 = [6, 8, 17, 18, 19, 22, 24, 25]
KEEP2 = [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 20, 21, 23]
def mc(title, q, ch, right, seed):
    rnd = random.Random(seed); ids = [str(rnd.randint(1000, 9999)) for _ in ch]
    labels = "".join('''
                <response_label ident="%s">
                  <material>
                    <mattext texttype="text/plain">%s</mattext>
                  </material>
                </response_label>''' % (i, html.escape(c, quote=False)) for i, c in zip(ids, ch))
    return '''<item ident="%s" title="%s">
          <itemmetadata>
        <qtimetadata>
          <qtimetadatafield>
            <fieldlabel>question_type</fieldlabel>
            <fieldentry>multiple_choice_question</fieldentry>
          </qtimetadatafield>
          <qtimetadatafield>
            <fieldlabel>points_possible</fieldlabel>
            <fieldentry>1.0</fieldentry>
          </qtimetadatafield>
          <qtimetadatafield>
            <fieldlabel>original_answer_ids</fieldlabel>
            <fieldentry>%s</fieldentry>
          </qtimetadatafield>
        </qtimetadata>
      </itemmetadata>
          <presentation>
            <material>
              <mattext texttype="text/html">%s</mattext>
            </material>
            <response_lid ident="response1" rcardinality="Single">
              <render_choice>%s
              </render_choice>
            </response_lid>
          </presentation>
          <resprocessing>
            <outcomes>
              <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
            </outcomes>
            <respcondition continue="No">
              <conditionvar>
              <varequal respident="response1">%s</varequal>
              </conditionvar>
              <setvar action="Set" varname="SCORE">100</setvar>
            </respcondition>
          </resprocessing>
        </item>''' % (gid("q", title), html.escape(title), ",".join(ids), html.escape("<div><p>%s</p></div>" % html.escape(q, quote=False), quote=False), labels, ids[right])
def rebuild_qti(src, dst, keep, new, old_id, new_id, old_title, new_title):
    s = open(src).read()
    its = re.findall(r'<item ident=.*?</item>', s, re.S)
    head = s[:s.find("<item ident=")]; tail = s[s.rfind("</item>") + len("</item>"):]
    body = "\n".join(its[i - 1] for i in keep) + "\n" + "\n".join(mc(*q, seed=q[0]) for q in new)
    out = (head + body + tail).replace(old_id, new_id).replace('title="%s"' % old_title, 'title="%s"' % html.escape(new_title))
    assert len(re.findall(r'<item ident=', out)) == 25, len(re.findall(r'<item ident=', out))
    open(dst, "w").write(out)
OLD_T = "Sound: Quiz - The Decibel"
T1 = "Sound: Quiz - The Decibel, Acoustics &amp; Level"; T2 = "Sound: Quiz - The Decibel, Power, Voltage &amp; Speakers"
T1u, T2u = U(T1), U(T2)
Q2 = gid("quiz2"); R2 = gid("quiz2meta"); A2 = gid("quiz2assign")
os.makedirs(os.path.join(W, Q2), exist_ok=True)
for name, d in (("%s/assessment_qti.xml", None), ("non_cc_assessments/%s.xml.qti", None)):
    src = os.path.join(W, name % Q1)
    rebuild_qti(src, os.path.join(W, name % Q2), KEEP2, P2_NEW, Q1, Q2, OLD_T, T2u)
    rebuild_qti(src, src, KEEP1, P1_NEW, Q1, Q1, OLD_T, T1u)
meta1 = os.path.join(W, Q1, "assessment_meta.xml"); s = open(meta1).read()
A1 = re.search(r'<assignment identifier="([^"]+)"', s).group(1)
s2 = s.replace(Q1, Q2).replace(A1, A2).replace("<title>%s</title>" % OLD_T, "<title>%s</title>" % T2)
s2 = re.sub(r"<due_at>[^<]*</due_at>", "<due_at>2027-02-19T16:00:00Z</due_at>", s2); s2 = re.sub(r"<unlock_at>[^<]*</unlock_at>", "<unlock_at>2027-02-08T07:00:00Z</unlock_at>", s2)
open(os.path.join(W, Q2, "assessment_meta.xml"), "w").write(s2)
open(meta1, "w").write(s.replace("<title>%s</title>" % OLD_T, "<title>%s</title>" % T1))
man = man.replace("</resources>", '''  <resource identifier="%s" type="imsqti_xmlv1p2/imscc_xmlv1p1/assessment">
      <file href="%s/assessment_qti.xml" />
      <dependency identifierref="%s" />
    </resource>
    <resource identifier="%s" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="%s/assessment_meta.xml">
      <file href="%s/assessment_meta.xml" />
      <file href="non_cc_assessments/%s.xml.qti" />
    </resource>
  </resources>''' % (Q2, Q2, R2, R2, Q2, Q2, Q2), 1)
# ---- modules
def mitem(ct, title, ref=None, url=None, indent=1, state="unpublished", key=None):
    x = '<item identifier="%s">\n        <content_type>%s</content_type>\n        <workflow_state>%s</workflow_state>\n        <title>%s</title>' % (gid("item", key or title, ct), ct, state, title)
    if ref: x += "\n        <identifierref>%s</identifierref>" % ref
    if url: x += "\n        <url>%s</url>" % url
    return x + '\n        <position>0</position>\n        <new_tab>%s</new_tab>\n        <indent>%d</indent>\n        <link_settings_json>null</link_settings_json>\n      </item>' % ("true" if ct == "ExternalUrl" else "false", indent)
def setind(it, n): return re.sub(r"<indent>\d+</indent>", "<indent>%d</indent>" % n, it)
def renum(lst): return "\n      ".join(re.sub(r"<position>\d+</position>", "<position>%d</position>" % k, it, count=1) for k, it in enumerate(lst, 1))
dec = modblock("Sound: The Decibel"); D = {ititle(i): i for i in items(dec)}
hdr = lambda t: next(i for i in items(dec) if ititle(i).lower() == t.lower() and "ContextModuleSubHeader" in i)
def pg(t): return setind(D[t], 1)
def newpg(t): return mitem("WikiPage", html.escape(t, quote=False), ref=newref[t])
quiz1 = setind(D[OLD_T], 1).replace("<title>%s</title>" % OLD_T, "<title>%s</title>" % T1)
part1 = [D["The Decibel: Slides (PDF)"], D["The Decibel: Slides - Inverse Square Law and Decibels (PDF)"], hdr("Study"),
         pg("Sound: Introduction to the Decibel"), newpg("Sound: Sound Pressure Level and the Inverse Square Law"),
         newpg("Sound: Equal-Loudness Contours - Fletcher-Munson to ISO 226"), newpg("Sound: Weighting - dBA, dBC and dBZ, and Safe Listening"),
         pg("Sound: Even More About the dB"), pg("Sound: Glossary of Terms"), hdr("Graded Work"),
         setind(D["Sound: Assignment - The Decibel in the Real World"], 1), quiz1]
P1T = "Sound: The Decibel - Acoustics &amp; Level"; P2T = "Sound: The Decibel - Power, Voltage &amp; Speakers"
dec2 = re.sub(r"<title>Sound: The Decibel</title>", "<title>%s</title>" % P1T, dec.split("<items>")[0], count=1) + "<items>\n      " + renum(part1) + "\n    </items>\n  </module>"
mm = mm.replace(dec, dec2)
mas = "https://uvu-files.adamo.workers.dev/DAPR-2000--Digital_Audio_Essentials/Sound__The_Decibel/Presentations/PDF/Audio_dB_RMS_Headroom_Masterclass.pdf"
part2 = [D["The Decibel: Slides - Decibels Training (PDF)"], D["The Decibel: Slides - Decibels Expanded and Power (PDF)"], D["The Decibel: Slides - Complete Speaker Power Explanation (PDF)"],
         mitem("ExternalUrl", "The Decibel: Slides - Audio dB, RMS and Headroom (PDF)", ref=gid("wl", "masterclass"), url=mas, indent=0),
         mitem("ContextModuleSubHeader", "STUDY", indent=0, key="p2study"), pg("Sound: More About the dB"),
         newpg("Sound: Reference Levels - dBu, dBV, dBm, dBW and dBFS"), newpg("Sound: Speakers, Amplifiers and Sensitivity"), pg("Sound: Watch More dB Videos (if you wish)"),
         mitem("ContextModuleSubHeader", "PRACTICE", indent=0, key="p2practice"), pg("Sound: Real Life Scenario - An Uber Decibel Problem"),
         mitem("ContextModuleSubHeader", "GRADED WORK", indent=0, key="p2graded"), mitem("Quizzes::Quiz", T2, ref=Q2)]
mod2 = '<module identifier="%s">\n    <title>%s</title>\n    <workflow_state>unpublished</workflow_state>\n    <position>99</position>\n    <require_sequential_progress>false</require_sequential_progress>\n    <locked>false</locked><unlock_at>2027-02-08T07:00:00Z</unlock_at>\n    <items>\n      %s\n    </items>\n  </module>' % (gid("mod", "decibel2"), P2T, renum(part2))
mm = mm.replace("</modules>", "  " + mod2 + "\n</modules>")
# weblink for the masterclass deck, same shape as the module's other slide links
wl = gid("wl", "masterclass"); old = re.search(r'<resource identifier="([^"]+)" type="imswl_xmlv1p1" href="(web_links/[^"]+)">', man).group(2)
src = open(os.path.join(W, old)).read()
open(os.path.join(W, "web_links/%s.xml" % wl), "w").write(re.sub(r'(<url href=")[^"]*(")', r"\g<1>%s\2" % mas, re.sub(r"<title>[^<]*</title>", "<title>The Decibel: Slides - Audio dB, RMS and Headroom (PDF)</title>", src)))
man = man.replace("</resources>", '  <resource identifier="%s" type="imswl_xmlv1p1" href="web_links/%s.xml">\n      <file href="web_links/%s.xml" />\n    </resource>\n  </resources>' % (wl, wl, wl), 1)
# "Introducing the DAW" belongs with Pro Tools: Introduction (right-modules rule)
pt = modblock("Pro Tools: Introduction"); its = items(pt)
k = next(i for i, it in enumerate(its) if "ContextModuleSubHeader" in it and ititle(it).upper() == "STUDY")
its.insert(k + 1, setind(D["Sound: Introducing the Digital Audio Workstation (DAW)"], 1))
mm = mm.replace(pt, pt.split("<items>")[0] + "<items>\n      " + renum(its) + "\n    </items>\n  </module>")
open(MM, "w").write(mm); open(MAN, "w").write(man)
print("Q2", Q2, "pages", len(newref))
