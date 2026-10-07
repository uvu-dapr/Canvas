# J143 (2026-10-07): DAPR 2020 gets "Delivery Recommendations for Recorded Music Projects" (Recording Academy P&E Wing guidebook)
# in Mixing: Master-Buss Processing & Endgame, under Study, after The Master Chain and the Final Check. New page arrives unpublished.
# Usage: python3 delivery_recommendations_j143.py <unzipped working copy>
import sys, os, re, html, hashlib
W = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
TITLE = "Master-Buss Processing and Endgame: Delivery Recommendations for Recorded Music Projects"
SLUG = "master-buss-processing-and-endgame-delivery-recommendations-for-recorded-music-projects-f26"
AFTER = "Master-Buss Processing and Endgame: The Master Chain and the Final Check"
MODULE = "Mixing: Master-Buss Processing & Endgame"
def gid(*p): return "g" + hashlib.md5("|".join(("2020-j143",) + p).encode()).hexdigest()
MM = os.path.join(W, "course_settings/module_meta.xml"); MAN = os.path.join(W, "imsmanifest.xml")
mm = open(MM).read(); man = open(MAN).read()
U = html.unescape
assert TITLE not in U(mm), "page already in this package"
body = open(os.path.join(HERE, "delivery_recommendations_j143_body.html")).read().strip()
rid = gid("page", TITLE)
open(os.path.join(W, "wiki_content/%s.html" % SLUG), "w").write(
    '<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n<title>%s</title>\n<meta name="identifier" content="%s">\n<meta name="editing_roles" content="teachers">\n<meta name="workflow_state" content="unpublished">\n</head>\n<body>\n%s\n</body>\n</html>\n' % (html.escape(TITLE, quote=False), rid, body))
man = man.replace("</resources>", '  <resource identifier="%s" type="webcontent" href="wiki_content/%s.html">\n      <file href="wiki_content/%s.html" />\n    </resource>\n  </resources>' % (rid, SLUG, SLUG), 1)
mod = next(b for b in re.findall(r'<module identifier="[^"]+">.*?</module>', mm, re.S) if U(re.search(r"<title>([^<]*)</title>", b).group(1)) == MODULE)
its = re.findall(r'<item identifier=.*?</item>', mod, re.S)
k = next(i for i, it in enumerate(its) if U(re.search(r"<title>([^<]*)</title>", it).group(1)) == AFTER)
new = ('<item identifier="%s">\n        <content_type>WikiPage</content_type>\n        <workflow_state>unpublished</workflow_state>\n        <title>%s</title>\n'
       '        <identifierref>%s</identifierref>\n        <position>0</position>\n        <new_tab>false</new_tab>\n        <indent>1</indent>\n        <link_settings_json>null</link_settings_json>\n      </item>') % (gid("item", TITLE), html.escape(TITLE, quote=False), rid)
its.insert(k + 1, new)
its = [re.sub(r"<position>\d+</position>", "<position>%d</position>" % n, it, count=1) for n, it in enumerate(its, 1)]
mod2 = mod.split("<items>")[0] + "<items>\n      " + "\n      ".join(its) + "\n    </items>\n  </module>"
mm = mm.replace(mod, mod2)
open(MM, "w").write(mm); open(MAN, "w").write(man)
print("added", TITLE, rid, "at position", k + 2, "of", len(its))
