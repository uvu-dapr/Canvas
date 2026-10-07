# J144 (2026-10-07): Blueprint (BLU_Olson_Course Resources) gets two reference modules with three NEW pages.
# Only new items: every live Blueprint item was made in Canvas (match_ids: 72 original), so an existing
# page in this package would arrive as a second copy and Sync would push it to every class.
# Existing pages are moved and renamed by hand (step page in Universal Class Content Notes and Briefs).
# Usage: python3 blueprint_reference_modules_j144.py <empty output folder>
import sys, os, html, hashlib
OUT = sys.argv[1]; HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blueprint_j144")
def gid(*p): return "g" + hashlib.md5("|".join(("blu-j144",) + p).encode()).hexdigest()
MODULES = [
    ("Protocols and Standards - (Unified Class Content)", [
        ("Protocols: Delivery and File Naming Standards", "protocols-delivery-and-file-naming-standards"),
        ("Protocols: Delivery Recommendations for Recorded Music Projects", "protocols-delivery-recommendations-for-recorded-music-projects")]),
    ("General Reference - (Unified Class Content)", [
        ("Reference: PreSonus FaderPort Quick Start for Pro Tools", "reference-presonus-faderport-quick-start-for-pro-tools")]),
]
os.makedirs(os.path.join(OUT, "wiki_content")); os.makedirs(os.path.join(OUT, "course_settings"))
res = []; mods = []
for mpos, (mtitle, pages) in enumerate(MODULES, 1):
    items = []
    for ipos, (title, slug) in enumerate(pages, 1):
        rid = gid("page", title)
        body = open(os.path.join(HERE, slug + ".body.html")).read().strip()
        open(os.path.join(OUT, "wiki_content", slug + ".html"), "w").write(
            '<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n<title>%s</title>\n<meta name="identifier" content="%s"/>\n<meta name="editing_roles" content="teachers"/>\n<meta name="workflow_state" content="unpublished"/>\n</head>\n<body>\n%s\n</body>\n</html>\n' % (html.escape(title, quote=False), rid, body))
        res.append('    <resource identifier="%s" type="webcontent" href="wiki_content/%s.html">\n      <file href="wiki_content/%s.html"/>\n    </resource>' % (rid, slug, slug))
        items.append('      <item identifier="%s">\n        <content_type>WikiPage</content_type>\n        <workflow_state>unpublished</workflow_state>\n        <title>%s</title>\n        <identifierref>%s</identifierref>\n        <position>%d</position>\n        <new_tab>false</new_tab>\n        <indent>0</indent>\n        <link_settings_json>null</link_settings_json>\n      </item>' % (gid("item", title), html.escape(title, quote=False), rid, ipos))
    mods.append('  <module identifier="%s">\n    <title>%s</title>\n    <workflow_state>unpublished</workflow_state>\n    <position>%d</position>\n    <require_sequential_progress>false</require_sequential_progress>\n    <locked>false</locked>\n    <items>\n%s\n    </items>\n  </module>' % (gid("module", mtitle), html.escape(mtitle, quote=False), mpos, "\n".join(items)))
open(os.path.join(OUT, "course_settings/module_meta.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<modules xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">\n%s\n</modules>\n' % "\n".join(mods))
open(os.path.join(OUT, "course_settings/canvas_export.txt"), "w").write("Q: What did the panda say when he was forced out of his natural habitat?\nA: This is un-BEAR-able\n")
open(os.path.join(OUT, "imsmanifest.xml"), "w").write('''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="%s" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lomresource_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lommanifest_v1p0.xsd">
  <metadata>
    <schema>IMS Common Cartridge</schema>
    <schemaversion>1.1.0</schemaversion>
    <lomimscc:lom>
      <lomimscc:general>
        <lomimscc:title>
          <lomimscc:string>BLU_Olson_Course Resources</lomimscc:string>
        </lomimscc:title>
      </lomimscc:general>
      <lomimscc:lifeCycle>
        <lomimscc:contribute>
          <lomimscc:date>
            <lomimscc:dateTime>2026-10-07</lomimscc:dateTime>
          </lomimscc:date>
        </lomimscc:contribute>
      </lomimscc:lifeCycle>
      <lomimscc:rights>
        <lomimscc:copyrightAndOtherRestrictions>
          <lomimscc:value>yes</lomimscc:value>
        </lomimscc:copyrightAndOtherRestrictions>
        <lomimscc:description>
          <lomimscc:string>Private (Copyrighted) - http://en.wikipedia.org/wiki/Copyright</lomimscc:string>
        </lomimscc:description>
      </lomimscc:rights>
    </lomimscc:lom>
  </metadata>
  <organizations>
    <organization identifier="org_1" structure="rooted-hierarchy">
      <item identifier="LearningModules"/>
    </organization>
  </organizations>
  <resources>
%s
    <resource identifier="%s" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="course_settings/canvas_export.txt">
      <file href="course_settings/module_meta.xml"/>
      <file href="course_settings/canvas_export.txt"/>
    </resource>
  </resources>
</manifest>
''' % (gid("manifest"), "\n".join(res), gid("settings")))
print("built", sum(len(p) for _, p in MODULES), "pages in", len(MODULES), "modules")
