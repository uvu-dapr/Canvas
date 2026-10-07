"""J105 (Adam's decisions, 2026-10-06): DAPR 2000 Spring 2027 mixes get a Class Ratings column. Mix 1A 100 = 75 instructor +
25 class; Mix 2 75 = 50 + 25. Students upload the WAV to "<Mix>: Class Ratings", Canvas peer review hands it to every
classmate anonymously with the Class Ratings rubric (Balance, Tone, Dynamics, Space, Overall; a comment on every row), and
the grade is the class average (Canvas Preview computes it; the Gradebook import is Adam's click).
    class_ratings_2000_spring_j105.py <unzipped template>"""
import sys, os, re, html, hashlib, datetime
W = sys.argv[1]
def gid(*p): return "g" + hashlib.md5("|".join(("2000-j105",) + p).encode()).hexdigest()
RUB = os.path.join(W, "course_settings/rubrics.xml"); rub = open(RUB).read()
MAN = os.path.join(W, "imsmanifest.xml"); man = open(MAN).read()
MM = os.path.join(W, "course_settings/module_meta.xml"); mm = open(MM).read()
MIXES = [  # assignment id, old total, new total, {row number: new points, or None to remove}
    ("g0ff4e66f20bf7a56b836d0acdfd8cedd", 100, 75, {1: 10, 2: 10, 3: 15, 6: None}, "Mix 1A - Six of One"),
    ("ga7c31f9e0b4d82615ce7048dbb9f3a12", 75, 50, {1: 10, 2: 5, 3: 5, 6: 5}, "Mix 2 - Six of One Revision")]
def fmt(x): return ("%g" % x)
for aid, old, new, rows, short in MIXES:
    sp = os.path.join(W, aid, "assignment_settings.xml"); st = open(sp).read()
    rid = re.search(r"<rubric_identifierref>([^<]+)", st).group(1)
    st = st.replace("<points_possible>%s.0</points_possible>" % old, "<points_possible>%s.0</points_possible>" % new); open(sp, "w").write(st)
    blk = re.search(r'<rubric identifier="%s">.*?</rubric>' % rid, rub, re.S).group(0); nb = blk
    nb = nb.replace("(%d pts)" % old, "(%d pts)" % new).replace("<points_possible>%d.0</points_possible>" % old, "<points_possible>%d.0</points_possible>" % new, 1)
    for c in re.findall(r"<criterion>.*?</criterion>", blk, re.S):
        n = int(re.search(r"<description>(\d+)\.", c).group(1))
        if n not in rows: continue
        if rows[n] is None: nb = nb.replace(c, ""); continue
        p = rows[n]; cid = re.search(r"<criterion_id>([^<]+)", c).group(1)
        rs = re.findall(r"<rating>.*?</rating>", c, re.S)
        # full credit, then half when the row keeps a middle rating and the half is a whole number, then none
        keep = [rs[0]] + ([rs[1]] if len(rs) == 3 and p % 2 == 0 and p >= 10 else []) + [rs[-1]]
        pts = [p] + ([p // 2] if len(keep) == 3 else []) + [0]
        nr = "".join(re.sub(r"<points>[^<]*</points>", "<points>%s.0</points>" % q, r, count=1) for r, q in zip(keep, pts))
        nr = re.sub(r"<id>[^<]*_(\d)</id>", lambda m: m.group(0), nr)
        c2 = re.sub(r"<points>[^<]*</points>", "<points>%s.0</points>" % p, c, count=1)
        c2 = re.sub(r"<ratings>.*</ratings>", "<ratings>\n          " + nr + "\n        </ratings>", c2, count=1, flags=re.S)
        nb = nb.replace(c, c2)
    tot = sum(float(x) for x in re.findall(r"<criterion>\s*<criterion_id>[^<]+</criterion_id>\s*<points>([^<]+)</points>", nb))
    assert tot == new, (short, tot)
    rub = rub.replace(blk, nb)
    # the page: "worth N points", the table caption, the rows
    hp = [os.path.join(W, aid, f) for f in os.listdir(os.path.join(W, aid)) if f.endswith(".html")][0]; h = open(hp).read()
    h = h.replace("worth %d points" % old, "worth %d points, plus %d points in %s: Class Ratings" % (new, old - new, short.split(" - ")[0]))
    h = re.sub(r"(<caption><strong>[^<]*?, )%d( points</strong></caption>)" % old, r"\g<1>%d\g<2>" % new, h)
    for tr in re.findall(r"<tr><td[^>]*>(\d+)\. .*?</tr>", h, re.S): pass
    for m in list(re.finditer(r"<tr><td[^>]*>(\d+)\. (?:(?!</tr>).)*</tr>", h, re.S)):
        n = int(m.group(1))
        if n not in rows: continue
        row = m.group(0)
        if rows[n] is None: h = h.replace(row, ""); continue
        row2 = re.sub(r'(text-align:right;">)\d+(</td></tr>)$', lambda x: x.group(1) + str(rows[n]) + x.group(2), row)
        h = h.replace(row, row2)
    open(hp, "w").write(h)
open(RUB, "w").write(rub)
ROWS = [("Balance", "Every part can be heard; nothing buries the lead or the groove."), ("Tone", "Each instrument sounds clear and natural, with no harsh, muddy or thin spots."), ("Dynamics", "The mix moves with the song: controlled peaks, nothing flattened or jumping out."), ("Space", "Width, depth and reverb place the parts so the mix sounds open, not cluttered."), ("Overall", "You would play this for a friend: it feels finished and serves the song.")]
# the Class Ratings rubric: five rows, 5 points each, full or none
CR = gid("rubric")
crit = ""
for i, (name, what) in enumerate([("Balance", "Every part can be heard; nothing buries the lead or the groove."), ("Tone", "Each instrument sounds clear and natural, with no harsh, muddy or thin spots."), ("Dynamics", "The mix moves with the song: controlled peaks, nothing flattened or jumping out."), ("Space", "Width, depth and reverb place the parts so the mix sounds open, not cluttered."), ("Overall", "You would play this for a friend: it feels finished and serves the song.")], 1):
    cid = "_cr%d" % i
    crit += """      <criterion>
        <criterion_id>%s</criterion_id>
        <points>5.0</points>
        <description>%d. %s</description>
        <long_description>%s Write one sentence about what you heard.</long_description>
        <ratings>
          <rating>
            <description>Yes</description>
            <long_description>Fully true for this mix.</long_description>
            <points>5.0</points>
            <criterion_id>%s</criterion_id>
            <id>%s_0</id>
          </rating>
          <rating>
            <description>Not yet</description>
            <long_description>Not true yet; your comment says what would fix it.</long_description>
            <points>0.0</points>
            <criterion_id>%s</criterion_id>
            <id>%s_1</id>
          </rating>
        </ratings>
      </criterion>
""" % (cid, i, name, what, cid, cid, cid, cid)
rub = open(RUB).read().replace("</rubrics>", """  <rubric identifier="%s">
    <read_only>false</read_only>
    <title>Class Ratings (25 pts)</title>
    <reusable>false</reusable>
    <public>false</public>
    <points_possible>25.0</points_possible>
    <hide_score_total>false</hide_score_total>
    <free_form_criterion_comments>false</free_form_criterion_comments>
    <rating_order>descending</rating_order>
    <criteria>
%s    </criteria>
  </rubric>
</rubrics>""" % (CR, crit), 1)
open(RUB, "w").write(rub)
# the Class Ratings assignments, right after each mix
def page(title, mix):
    C = "#1b5e20"
    return ('<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n<title>%s</title>\n</head>\n<body>\n'
     '<div style="font-family:Arial, Helvetica, sans-serif; max-width:900px; margin:0 auto; color:#212121; line-height:1.6; background-color:#ffffff; padding:0 12px;">\n'
     '<h2 style="background-color:%s; color:#ffffff; padding:16px 20px; font-size:1.4em; border-radius:4px; margin-top:0;">%s</h2>\n'
     '<p style="margin:0 0 16px 0;"><img style="max-width: 100%%; height: auto;" src="https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/Student_Essentials/Feedback_Loop.png" alt="A loop from making a mix, to listening, to feedback, to the next mix" loading="lazy"></p>\n'
     '<p><strong>25 points.</strong> About 1 hour: 10 minutes to upload, then a few minutes per classmate\'s mix.</p>\n'
     '<p>Your mix gets two grades. %s is my grade, against my rubric. This assignment is the class\'s grade: every classmate listens to your mix and rates it, and your score here is the average of their ratings. You will see every comment; you will not see who wrote it.</p>\n'
     '<h3 style="color:%s; font-size:1.2em; border-bottom:2px solid %s; padding-bottom:4px; margin-top:32px;">Do this</h3>\n<ol>\n'
     '<li>Upload the same stereo WAV you submitted to %s here (a WAV or an MP3 so it plays in the browser).</li>\n'
     '<li>After the due date, Canvas gives you your classmates\' mixes to review. Open each one from your To Do list, listen all the way through on headphones or the studio monitors, and fill in the rubric.</li>\n'
     '<li>Every row needs a rating and one sentence about what you heard. Be specific and kind: name the part and the moment, and say what would make it better.</li>\n</ol>\n'
     '<h3 style="color:%s; font-size:1.2em; border-bottom:2px solid %s; padding-bottom:4px; margin-top:32px;">The rating rows</h3>\n'
     '<div style="background-color:#e3f2fd; border-left:4px solid #0d47a1; margin:16px 0; padding:12px 14px;"><img style="vertical-align:middle; margin-right:10px;" src="https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/Callout_Note.png" alt="Note" width="44" height="44"> <strong style="vertical-align:middle;">Your score is the class average.</strong><div style="margin-left:54px; margin-top:6px;">Each classmate\'s rubric is a score out of 25; this assignment\'s grade is the average of them, entered after the reviews close. A rating with no comment does not count, and I can drop a review that is not fair.</div></div>\n'
     '<table style="border-collapse:collapse; width:100%%; margin:12px 0 16px 0;" border="1"><caption><strong>Class Ratings, 25 points</strong></caption><thead><tr><th scope="col" style="padding:8px 12px; background-color:#eceff1; text-align:left;"><strong>Criterion</strong></th><th scope="col" style="padding:8px 12px; background-color:#eceff1; text-align:left;"><strong>What earns full credit</strong></th><th scope="col" style="padding:8px 12px; background-color:#eceff1; text-align:left;"><strong>Points</strong></th></tr></thead><tbody>'
     + "".join('<tr><td style="padding:8px 12px; border:1px solid #e0e0e0;">%d. %s</td><td style="padding:8px 12px; border:1px solid #e0e0e0;">%s</td><td style="padding:8px 12px; border:1px solid #e0e0e0; text-align:right;">5</td></tr>' % (i, n, w) for i, (n, w) in enumerate(ROWS, 1))
     + '</tbody></table>\n'
     '<h3 style="color:%s; font-size:1.2em; border-bottom:2px solid %s; padding-bottom:4px; margin-top:32px;">What to Submit</h3>\n'
     '<p>One stereo WAV or MP3 of your mix, the same mix you submitted to %s. Then complete every review Canvas assigns you by the review due date.</p>\n'
     '</div>\n</body>\n</html>\n') % (html.escape(title, quote=False), C, html.escape(title, quote=False), mix, C, C, mix, C, C, C, C, mix)
for aid, old, new, rows, short in MIXES:
    st = open(os.path.join(W, aid, "assignment_settings.xml")).read()
    mixtitle = html.unescape(re.search(r"<title>([^<]*)", st).group(1)); topic = mixtitle.split(":")[0]
    title = "%s: Assignment - %s: Class Ratings" % (topic, short.split(" - ")[0])
    nid = gid("assign", short); os.makedirs(os.path.join(W, nid), exist_ok=True)
    due = datetime.datetime.strptime(re.search(r"<due_at>([^<]+)", st).group(1), "%Y-%m-%dT%H:%M:%SZ")
    reviews = (due + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")
    s2 = st.replace(aid, nid).replace("<title>%s</title>" % html.escape(mixtitle, quote=False), "<title>%s</title>" % html.escape(title, quote=False))
    s2 = re.sub(r"<rubric_identifierref>[^<]+", "<rubric_identifierref>" + CR, s2); 
    s2 = re.sub(r"<points_possible>[^<]+", "<points_possible>25.0", s2); s2 = re.sub(r"<allowed_extensions>[^<]*</allowed_extensions>|<allowed_extensions/>", "<allowed_extensions>wav,mp3</allowed_extensions>", s2)
    s2 = re.sub(r"<workflow_state>[^<]+", "<workflow_state>unpublished", s2)
    for k, v in [("peer_reviews", "true"), ("automatic_peer_reviews", "true"), ("anonymous_peer_reviews", "true"), ("peer_review_count", "19")]:
        s2 = re.sub(r"<%s>[^<]*</%s>" % (k, k), "<%s>%s</%s>" % (k, v, k), s2)
    s2 = s2.replace("<peer_reviews>true</peer_reviews>", "<peer_reviews>true</peer_reviews>\n  <peer_reviews_due_at>%s</peer_reviews_due_at>" % reviews)
    fname = "class-ratings-%s.html" % re.sub(r"[^a-z0-9]+", "-", short.lower()).strip("-")
    open(os.path.join(W, nid, "assignment_settings.xml"), "w").write(s2)
    open(os.path.join(W, nid, fname), "w").write(page(title, "the " + short.split(" - ")[0] + " assignment"))
    man = man.replace("</resources>", '  <resource identifier="%s" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="%s/%s">\n      <file href="%s/%s" />\n      <file href="%s/assignment_settings.xml" />\n    </resource>\n  </resources>' % (nid, nid, fname, nid, fname, nid), 1)
    it = re.search(r'<item identifier="[^"]+">\s*<content_type>Assignment</content_type>(?:(?!</item>).)*<identifierref>%s</identifierref>.*?</item>' % aid, mm, re.S).group(0)
    new_it = re.sub(r'<item identifier="[^"]+">', '<item identifier="%s">' % gid("item", short), it, count=1).replace(aid, nid)
    new_it = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % html.escape(title, quote=False), new_it, count=1)
    new_it = re.sub(r"<workflow_state>[^<]+", "<workflow_state>unpublished", new_it, count=1)
    mm = mm.replace(it, it + "\n      " + new_it)
    print(title, "| reviews due", reviews[:10])
open(MAN, "w").write(man); open(MM, "w").write(mm); print("ok")
