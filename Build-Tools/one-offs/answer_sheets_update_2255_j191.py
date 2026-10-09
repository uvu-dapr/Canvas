#!/usr/bin/env python3
"""J191: DAPR 2255 Update package with the 13 instructor Answer Sheet pages (12 from v130, Resistors new).
Usage: build_answer_update.py <v130 unzipped dir> <answers.json for Resistors> <out dir>"""
import sys, os, json, html, shutil, re
v130, rj, out = sys.argv[1:4]
esc = lambda s: html.escape(s, quote=False).encode("ascii", "xmlcharrefreplace").decode()
H3 = "color:#1b5e20; font-size:1.2em; border-bottom:2px solid #1b5e20; padding-bottom:4px;"
def page(j, ident):
    t = "Answer Sheet: " + j["title"]
    b = ('<div style="font-family:Arial, Helvetica, sans-serif; max-width:900px; margin:0 auto; color:#212121; line-height:1.6; background-color:#ffffff; padding:0 12px;">'
         '<h2 style="background-color:#424242; color:#ffffff; padding:16px 20px; font-size:1.4em; border-radius:4px; margin-top:0;">%s</h2>' % esc(t)
         + "<p><strong>Instructor only. Keep this page unpublished.</strong> Rows follow the rubric. This term students have the original numbers (the page was already open when personal numbers came in).</p>")
    for n, it in enumerate(j["items"], 1):
        o = it.get("original", it)
        b += '<h3 style="%s">%d. %s (%s pts)</h3>' % (H3, n, esc(it["criterion"]), it["points"])
        b += "<p>%s</p>" % esc(o["worksheet_text"].replace("\n", " "))
        b += '<p style="font-size:1.15em;"><strong>Answer:</strong> %s</p>' % esc(o["answer"])
        b += "<ol>" + "".join("<li>%s</li>" % esc(w) for w in o["work"]) + "</ol>"
        b += "<p><strong>Full:</strong> %s<br><strong>Partial:</strong> %s<br><strong>None:</strong> %s</p>" % (esc(o["full"]), esc(it["partial"]), esc(o["none"]))
        b += "<p><em>Watch for:</em> %s</p>" % esc(o["watch"])
    b += "</div>"
    return ('<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n<title>*No Publish: %s</title>\n'
            '<meta name="identifier" content="%s"/>\n<meta name="editing_roles" content="teachers"/>\n<meta name="workflow_state" content="unpublished"/>\n</head>\n<body>\n%s\n</body>\n</html>\n') % (esc(t), ident, b)

if os.path.exists(out): shutil.rmtree(out)
os.makedirs(out + "/wiki_content"); os.makedirs(out + "/course_settings")
pages = []   # (ident, file, title)
for f in sorted(os.listdir(v130 + "/wiki_content")):
    if not f.startswith("answer-sheet-"): continue
    x = open(v130 + "/wiki_content/" + f, encoding="utf-8").read()
    ident = re.search(r'name="identifier" content="([^"]+)"', x).group(1)
    title = html.unescape(re.search(r"<title>([^<]*)</title>", x).group(1))
    assert 'content="unpublished"' in x, f
    shutil.copy(v130 + "/wiki_content/" + f, out + "/wiki_content/" + f)
    pages.append((ident, f, title))
j = json.load(open(rj, encoding="utf-8"))
ident = "dapr-answers-resistors-assignment-color-codes-power-a"
f = "answer-sheet-resistors-assignment-color-codes-power-audio-applic.html"
open(out + "/wiki_content/" + f, "w", encoding="utf-8").write(page(j, ident))
pages.append((ident, f, "*No Publish: Answer Sheet: " + j["title"]))
pages.sort(key=lambda p: p[2].lower())
assert len(pages) == 13, len(pages)

res = "".join('<resource identifier="%s" type="webcontent" href="wiki_content/%s">\n      <file href="wiki_content/%s"/>\n    </resource>\n' % (i, f, f) for i, f, _ in pages)
open(out + "/imsmanifest.xml", "w", encoding="utf-8").write(
    "<?xml version='1.0' encoding='UTF-8'?>\n"
    '<manifest xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" identifier="dapr2255-answer-sheets-v146" '
    'xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1     http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p1.xsd">\n'
    "  <metadata>\n    <schema>IMS Common Cartridge</schema>\n    <schemaversion>1.1.0</schemaversion>\n  </metadata>\n  <organizations/>\n  <resources>\n"
    '<resource identifier="module_meta_res" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="course_settings/canvas_export.txt"><file href="course_settings/module_meta.xml"/><file href="course_settings/canvas_export.txt"/></resource>\n'
    + res + "  </resources>\n</manifest>\n")
items = "".join(
    "      <item identifier=\"%s-item\">\n        <content_type>WikiPage</content_type>\n        <workflow_state>unpublished</workflow_state>\n"
    "        <title>%s</title>\n        <identifierref>%s</identifierref>\n        <position>%d</position>\n        <new_tab/>\n        <indent>0</indent>\n      </item>\n"
    % (i, esc(t), i, n) for n, (i, f, t) in enumerate(pages, 1))
open(out + "/course_settings/module_meta.xml", "w", encoding="utf-8").write(
    "<?xml version='1.0' encoding='UTF-8'?>\n"
    '<modules xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0     https://canvas.instructure.com/xsd/cccv1p0.xsd">\n'
    '  <module identifier="dapr2255-answer-sheets-module">\n    <title>Audio Hardware 1 - DAPR 2255 - Answer Sheets - Instructor Use Only - [Do Not Publish]</title>\n'
    "    <position>1</position>\n    <workflow_state>unpublished</workflow_state>\n    <items>\n" + items + "    </items>\n  </module>\n</modules>\n")
shutil.copy(v130 + "/course_settings/canvas_export.txt", out + "/course_settings/canvas_export.txt")
print("built", out, len(pages), "pages")
for i, f, t in pages: print("  ", t)
