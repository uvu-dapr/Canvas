"""J151 (Adam, 2026-10-07): "build in the Dolby Atmos basic certification into the course for Spatial Audio 1 - DAPR 3340".
Dolby's free self-paced course "Dolby Atmos Music Pro Tools 100" (learning.dolby.com, course 211: Course
Introduction, Core Dolby Atmos Concepts, DAW Setup and Operation, headphone-focused with the Internal Renderer) becomes a
10 point exercise right after The Dolby Atmos Internal Renderer exercise, same layout and rubric as that exercise.
New items arrive unpublished. Usage: python3 dolby_atmos_cert_3340_j151.py <unzipped DAPR 3340 package>"""
import sys, os, re, hashlib
W = sys.argv[1]
AFTER = "gae92a4eaacdd5a06d4a3406514bd107c"            # Exercise - The Dolby Atmos Internal Renderer
TITLE = "Dolby Atmos Renderer: Assignment - Dolby Atmos Music Pro Tools 100 Certificate"
SLUG = "exercise-dolby-atmos-music-pro-tools-100-certificate"
NID = "g" + hashlib.md5(b"3340-j151-dolby-cert").hexdigest()
FILE = "Smith, John - Dolby Atmos Music Pro Tools 100 Certificate.pdf"
src = open(os.path.join(W, "assignments/exercise-the-dolby-atmos-internal-renderer.html")).read()
head, rest = src.split("<h3 ", 1)
grading = "<h3 " + rest[rest.index('margin-top:120px;">Grading</h3>') - len('<h3 style="color:#1b5e20; font-size:1.3em; border-bottom:2px solid #1b5e20; padding-bottom:4px; '):]
H3 = '<h3 style="color:#1b5e20; font-size:1.3em; border-bottom:2px solid #1b5e20; padding-bottom:4px;"><span style="text-decoration: underline;"><strong>%s</strong></span></h3>'
H4 = '<h4 style="font-size:1em; color:#333333; margin-top:16px; margin-bottom:6px"><strong>%s</strong></h4>'
body = (head.replace("Dolby Atmos Renderer: Assignment - The Dolby Atmos Internal Renderer Exercise", TITLE)
        .replace("Renderer_Preferences_Devices_and_Monitoring.png", "Room_View_With_Object_Spheres.png")
        .replace('alt="Renderer preferences showing the Devices and Monitoring sections"', 'alt="The Dolby Atmos Renderer room view with objects shown as spheres around the listener"')
        .replace("Renderer preferences, Devices and Monitoring", "The Renderer room view: objects placed around the listener"))
body += H3 % "Dolby Atmos Music Pro Tools 100" + "\n<hr>\n" + H4 % "Activity" + """
<p>Dolby's own free course, <strong>Dolby Atmos Music Pro Tools 100</strong>, on Dolby's free learning site, teaches the fundamentals of mixing Dolby Atmos for music in Pro Tools with headphones and the Internal Renderer: the same setup you just used in the Internal Renderer exercise. Finishing it gives you Dolby's own record that you completed their basic Dolby Atmos training, which you can show employers and clients.</p>
""" + H4 % "Duration" + """
<p>Plan on 1 to 3 hours, at your own pace. The course is short lessons and a mix-and-bounce walkthrough; this is a 10 point exercise.</p>
""" + H4 % "Goals/Targets" + """
<ul>
<li>Complete all three sections: Course Introduction, Core Dolby Atmos Concepts, and DAW Setup and Operation (mix and bounce a file)</li>
<li>Finish the course's completion survey</li>
<li>Hand in Dolby's completion record and one thing the course taught you</li>
</ul>
""" + H3 % "Steps" + """
<ol>
<li>Go to the <a title="Dolby Atmos Music Pro Tools 100 on Dolby's learning site (opens in a new tab)" href="https://learning.dolby.com/course/info.php?id=211" target="_blank" rel="noopener">Dolby Atmos Music Pro Tools 100 course page</a> on Dolby's learning site.</li>
<li>Click <strong>Log in</strong> and create a free Dolby account with your own email, or sign in if you have one. Then click <strong>Enroll</strong>.</li>
<li>Work through every section in order. Do the mix-and-bounce steps in Pro Tools with the Internal Renderer, as in the Internal Renderer exercise.</li>
<li>Finish the completion survey at the end, so Dolby marks the course complete.</li>
<li>If Dolby offers a certificate, download it. If it does not, take a screenshot of the course page showing every section complete with your name visible (your name appears at the top right when you are signed in).</li>
</ol>
<h3 style="color:#1b5e20; font-size:1.3em; border-bottom:2px solid #1b5e20; padding-bottom:4px; margin-top:120px;">Building Your PDF</h3>
<p>Copy the block below into a new Word document. Replace each placeholder with your own certificate or screenshot and your own words, then export the finished document as a PDF.</p>
<p>Click once anywhere in the gray box, then press Command C to copy.</p>
<hr>
<div style="background-color:#f5f5f5; border-radius:6px; padding:14px 16px; margin:16px 0; user-select:all; -webkit-user-select:all; cursor:pointer">
<p style="font-family:'Courier New', Courier, monospace; font-size:0.95em; margin:0 0 12px 0;">""" + FILE + """</p>
<p style="margin:0 0 12px 0;"><strong>Dolby Atmos Music Pro Tools 100 Certificate - DAPR 3340 - Utah Valley University</strong></p><p style="margin:0 0 4px 0;"><strong>Name:</strong> &nbsp;</p><p style="margin:0 0 20px 0;"><strong>Time this assignment took (hours and minutes):</strong> &nbsp;</p>
<p style="margin:0 0 4px 0;"><strong>1. Dolby's Completion Record</strong></p>
<p style="margin:0 0 4px 0;">Dolby's certificate, or a screenshot of the course page showing every section complete with your name visible.</p>
<p style="margin:0 0 16px 0; color:#616161; font-style:italic;">[ Certificate or screenshot here ]</p>
<p style="margin:0 0 4px 0;"><strong>2. One Thing the Course Taught You</strong></p>
<p style="margin:0 0 4px 0;">In two or three sentences, one thing about mixing in Dolby Atmos that you learned from Dolby's course and how you will use it in your own mix.</p>
<p style="margin:0; color:#616161; font-style:italic;">[ Your answer here ]</p>
</div>
<hr>
"""
g = grading
g = g.replace("each screenshot shows what its item asked for", "the course is complete, shown by Dolby's certificate or a screenshot of every section complete with your name")
g = g.replace("Every numbered item has a screenshot or written response", "Both numbered items are filled in")
g = g.replace("Smith, John - The Dolby Atmos Internal Renderer.pdf", FILE)
g = re.sub(r"<li>Both screenshots present.*?</li>\n<li>Screenshot 1 shows.*?</li>", "<li>Dolby's certificate or the completion screenshot is present, with your name visible.</li>\n<li>Item 2 is in your own words, two or three sentences.</li>", g, flags=re.S)
g = g.replace("10 points, about 30 to 60 minutes. One PDF with two screenshots: the Renderer in Binaural during playback, and the Edit Window with playback running.",
              "10 points, about 1 to 3 hours. One PDF with Dolby's completion record and one thing the course taught you.")
assert FILE in g and "1 to 3 hours" in g and "Item 2 is in your own words" in g, "grading text changed under me"
page = body + g
os.makedirs(os.path.join(W, "assignments"), exist_ok=True)
open(os.path.join(W, "assignments", SLUG + ".html"), "w").write(page)
x = open(os.path.join(W, "assignments/exercise-the-dolby-atmos-internal-renderer.xml")).read()
x = x.replace(AFTER, NID).replace("<title>Exercise - The Dolby Atmos Internal Renderer</title>", "<title>%s</title>" % TITLE)
x = re.sub(r"<due_at>[^<]*</due_at>", "<due_at>2026-11-20T16:00:00Z</due_at>", x)
x = re.sub(r"<workflow_state>[^<]*</workflow_state>", "<workflow_state>unpublished</workflow_state>", x)
x = re.sub(r"<submission_types>[^<]*</submission_types>", "<submission_types>online_upload</submission_types>", x)
x = re.sub(r"<allowed_extensions>[^<]*</allowed_extensions>", "<allowed_extensions>pdf</allowed_extensions>", x)
open(os.path.join(W, "assignments", SLUG + ".xml"), "w").write(x)
man = open(os.path.join(W, "imsmanifest.xml")).read()
assert NID not in man
man = man.replace("</resources>", '    <resource identifier="%s" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="assignments/%s.html">\n      <file href="assignments/%s.html" />\n      <file href="assignments/%s.xml" />\n    </resource>\n  </resources>' % (NID, SLUG, SLUG, SLUG), 1)
open(os.path.join(W, "imsmanifest.xml"), "w").write(man)
mm = open(os.path.join(W, "course_settings/module_meta.xml")).read()
it = re.search(r'<item identifier="[^"]+">(?:(?!</item>).)*<identifierref>%s</identifierref>(?:(?!</item>).)*</item>' % AFTER, mm, re.S).group(0)
new = re.sub(r'<item identifier="[^"]+">', '<item identifier="g%s">' % hashlib.md5(b"3340-j151-item").hexdigest(), it, count=1).replace(AFTER, NID)
new = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % TITLE, new, count=1)
new = re.sub(r"<workflow_state>[^<]*</workflow_state>", "<workflow_state>unpublished</workflow_state>", new, count=1)
mm = mm.replace(it, it + "\n        " + new, 1)
open(os.path.join(W, "course_settings/module_meta.xml"), "w").write(mm)
print("added", TITLE)
