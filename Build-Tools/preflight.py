#!/usr/bin/env python3
"""DAPR Canvas cartridge preflight. Run from inside an unzipped .imscc folder."""
import html as html_mod
html=html_mod
import re,os,glob,sys,urllib.parse
import xml.etree.ElementTree as ET

fails=[]; warns=[]; L=print

# 1 XML parses
bad=0; tot=0
for p in glob.glob('**/*',recursive=True):
    if not os.path.isfile(p) or not p.endswith(('.xml','.qti')): continue
    tot+=1
    try: ET.parse(p)
    except Exception as e: bad+=1; fails.append('XML parse %s: %s'%(p,e))
L('XML/QTI parsed: %d  failures: %d'%(tot,bad))

man=open('imsmanifest.xml',encoding='utf-8').read()
# Canvas writes imsmanifest.xml with every element namespaced (<ims:resource>, <ims:file>).
# Every manifest check below matches BARE tags, so without this normalization the declared-file
# check, the webcontent-ownership check (21.1b) and the quiz href resolution all silently saw
# zero elements and reported clean. This is the same false-negative that module_meta.xml was
# already normalized for further down; it was never applied here. A gate that finds nothing
# reports nothing, and nothing ever tells you. Strip the prefix once, here.
_mns=re.findall(r'<(\w+):manifest[\s>]',man)
if _mns:
    _mp=_mns[0]
    man=re.sub(r'</?%s:'%re.escape(_mp), lambda m: m.group(0).replace(_mp+':',''), man)
    print('    note: imsmanifest.xml is namespaced (%s:), prefixes stripped for matching'%_mp)
ids=set(re.findall(r'identifier="([^"]+)"',man))
pages={os.path.basename(p)[:-5] for p in glob.glob('wiki_content/*.html')}

# 1b QUIZ INVENTORY, RESOLVED FROM THE MANIFEST, NEVER FROM A FOLDER GLOB.
#   Canvas writes two different layouts for the same kind of object:
#     one folder per quiz   <id>/assessment_qti.xml   + <id>/assessment_meta.xml
#     a flat directory      quizzes/quiz_<slug>.xml   + quizzes/quiz_<slug>_meta.xml
#   Every quiz check below used to glob '*/assessment_meta.xml'. Against a flat-layout
#   package that glob returns nothing, so this script printed "quizzes: 0" and the
#   empty-quiz, point-total, non-ASCII, named-entity and external-image checks all
#   passed without reading a single question. DAPR 2255 is flat and shipped that way.
#   Platform Reference 30: never count, always resolve, and when the shape of the data
#   changes confirm the checker still sees it. A check that passes quietly may not be
#   looking.
#   Attribute order in a manifest is not fixed (21.3), so nothing here assumes it.
RES={}
for _m in re.finditer(r'<resource\b([^>]*)>(.*?)</resource>',man,re.S):
    _at,_body=_m.group(1),_m.group(2)
    _i=re.search(r'identifier="([^"]+)"',_at)
    if not _i: continue
    _t=re.search(r'type="([^"]+)"',_at); _h=re.search(r'href="([^"]+)"',_at)
    RES[_i.group(1)]={'type':_t.group(1) if _t else '',
                      'href':urllib.parse.unquote(_h.group(1)) if _h else None,
                      'deps':re.findall(r'<dependency identifierref="([^"]+)"',_body),
                      'files':[urllib.parse.unquote(x) for x in re.findall(r'<file href="([^"]+)"',_body)]}
QUIZ=[]   # (identifier, qti_path, meta_path or None)
for _i,_r in RES.items():
    if 'imsqti' not in _r['type']: continue
    # Canvas's own export writes a quiz resource with NO href on the <resource>
    # element; the qti file is named only by its <file> child. Requiring href
    # here skipped every Canvas-native quiz, so all the quiz checks below ran on
    # an empty list and reported clean. Verified against an untouched export:
    # 31 quiz resources, none with href. Fall back to the <file> entry.
    _qti=_r['href']
    if not _qti:
        _qti=next((c for c in _r['files'] if c.endswith(('.xml','.qti'))
                   and not c.endswith('_meta.xml')), None)
    if not _qti: continue
    _meta=None
    for _d in _r['deps']:                      # the meta rides in a dependency resource
        _dr=RES.get(_d)
        if not _dr: continue
        for _c in ([_dr['href']] if _dr['href'] else [])+_dr['files']:
            if _c and _c.endswith('_meta.xml') or _c=='%s/assessment_meta.xml'%_i:
                _meta=_c; break
        if _meta: break
    if _meta is None:                          # conventional siblings, both layouts
        for _c in (os.path.join(os.path.dirname(_qti),'assessment_meta.xml'),
                   _qti[:-4]+'_meta.xml'):
            if os.path.exists(_c): _meta=_c; break
    QUIZ.append((_i,_qti,_meta))
QTI_FILES=sorted({q for _,q,_m in QUIZ if os.path.exists(q)})
_nometa=[q for _,q,m in QUIZ if m is None]
L('quiz resources in the manifest: %d   qti files on disk: %d   metas resolved: %d'
  %(len(QUIZ),len(QTI_FILES),sum(1 for _,_q,m in QUIZ if m)))
if not QUIZ: warns.append('the manifest declares no quiz resources at all')
if _nometa: fails.append('quiz resources with no resolvable meta: %s'%[os.path.basename(x) for x in _nometa][:5])

# 2 canvas_export.txt declared  (else Assignments import as Pages)
ok='course_settings/canvas_export.txt' in man
L('canvas_export.txt declared: %s'%ok)
if not ok: fails.append('canvas_export.txt not declared as a resource')

# 3 declared files exist
# Manifest hrefs are XML escaped; zip entry names are not (Platform Reference 21.3).
# 'web_resources/01 Media/Audio &amp; Sessions/x.txt' is 'Audio & Sessions' in the zip.
# Unquoting alone left every declared path containing an ampersand looking missing,
# which reported two files that were present as a hard fail on DAPR 3255 v4.
def declared_path(h):
    return urllib.parse.unquote(html_mod.unescape(h))
miss=[h for h in re.findall(r'<file href="([^"]+)"',man) if not os.path.exists(declared_path(h))]
L('declared files missing on disk: %d'%len(miss))
if miss: fails.append('missing declared files: %s'%miss[:5])

# 4 EVERY placeholder token must resolve, AND its target must be the href of its OWN
#   webcontent resource. Canvas imports ONE file per resource, taken from that
#   resource's href. Extra <file> children of a resource are not imported. A package
#   that lumps N images into a single resource imports exactly one of them and every
#   other reference becomes "Missing links found in imported content". Being present
#   on disk is not enough, and being listed as a <file> child is not enough.
#   DAPR 2000 v30 shipped this way: 34 images under one resource, 30 import issues.
OWNED=set()
for _m in re.finditer(r'<resource identifier="[^"]+" type="webcontent" href="([^"]+)">(.*?)</resource>',man,re.S):
    OWNED.add(urllib.parse.unquote(_m.group(1)))
    _kids=re.findall(r'<file href="([^"]+)"\s*/>',_m.group(2))
    if len(_kids)>1:
        fails.append('resource %s bundles %d files; Canvas imports only its href'%(_m.group(1)[:60],len(_kids)))
probs=[]
for p in glob.glob('**/*',recursive=True):
    if not os.path.isfile(p): continue
    try: s=open(p,encoding='utf-8',errors='replace').read()
    except: continue
    for m in re.finditer(r'\$[A-Z_]+(?:-[A-Z]+)*\$[^"\'\s<)]*',s):
        t=m.group(0)
        if t.startswith('$IMS-CC-FILEBASE$/'):
            # FILEBASE resolves to web_resources/  (NOT the package root)
            f=os.path.join('web_resources',urllib.parse.unquote(t.split('$',2)[2][1:]))
            if not os.path.exists(f): probs.append((p,t[:90],'file missing'))
            elif f not in OWNED: probs.append((p,t[:90],'file is not the href of its own webcontent resource, so Canvas never imports it'))
        elif t.startswith('$WIKI_REFERENCE$/pages/'):
            if t.split('/pages/',1)[1].split('?')[0] not in pages: probs.append((p,t[:90],'page missing'))
        elif t.startswith('$CANVAS_OBJECT_REFERENCE$/'):
            if t.rsplit('/',1)[1] not in ids: probs.append((p,t[:90],'object missing'))
        elif t.startswith('$CANVAS_COURSE_REFERENCE$'):
            probs.append((p,t[:90],'bare course reference, resolves to the Files index'))
L('unresolvable placeholders: %d'%len(probs))
for x in probs[:10]: L('   %s | %s | %s'%x)
if probs: fails.append('%d unresolvable placeholders'%len(probs))

# 4b Canvas media attributes and Canvas-host URLs inside CONTENT BODIES.
#   data-media-id="m-..." names a Canvas media object in the SOURCE course. On import
#   Canvas tries to resolve it in the destination, fails, logs "Missing links found in
#   imported content", and rewrites the element into
#   /courses/<id>/file_contents/course files/<the original url>, which renders the
#   Canvas dashboard inside the player instead of the media. Strip the attribute and
#   let a plain HTML5 <audio controls>/<video controls> carry the external URL.
#   A link to a Canvas course, file or API on the Canvas host is the same defect: it
#   points at the course this content came FROM, not the one it is going TO.
#   Scoped to page/assignment bodies and quiz question text. XML namespace URIs on
#   canvas.instructure.com and LTI launch URLs are metadata and are not content.
def _bodies():
    # glob 'wiki_content/*.html' and glob '*/*.html' both match a wiki page, so
    # this yielded every page twice and doubled every count below it. Two real
    # links were reported as four defects on 2026-09-20.
    _seen=set()
    for f in glob.glob('wiki_content/*.html')+glob.glob('*/*.html'):
        _k=os.path.normpath(f)
        if _k in _seen: continue
        _seen.add(_k)
        yield f, open(f,encoding='utf-8',errors='replace').read()
    for f in QTI_FILES+glob.glob('non_cc_assessments/*.qti'):
        t=open(f,encoding='utf-8',errors='replace').read()
        yield f, html_mod.unescape(' '.join(re.findall(r'<mattext[^>]*>(.*?)</mattext>',t,re.S)))
media=[]
for f,body in _bodies():
    n=body.count('data-media-id')
    if n: media.append((f,'%d data-media-id attribute(s): Canvas cannot resolve these'%n))
    if '/file_contents/' in body: media.append((f,'Canvas file_contents URL'))
    # Narrowed 2026-09-20 to what the comment above says it means: a link back
    # into the course this content came FROM, which is a /courses/, /files/,
    # /api/, /users/ or /assignments/ path. An institution's Canvas login root
    # is where a student is supposed to be sent and survives import intact, and
    # Instructure's own documentation pages are ordinary external links.
    for m in set(re.findall(r'https?://(?!canvas\.instructure\.com/xsd)[a-z0-9.-]*instructure\.com/(?:api/|files/|courses/|users/|assignments/)[^"\'<> ]*',body)):
        media.append((f,'link into a Canvas course: '+m[:78]))
    for e in re.findall(r'<(?:audio|video)\b[^>]*>',body):
        if ' controls' not in e: media.append((f,'media element with no controls attribute'))
L('canvas media/link defects in content bodies: %d'%len(media))
for x in media[:10]: L('   %s | %s'%x)
if media: fails.append('%d canvas media/link defects'%len(media))

# 5 pages: head present, identifier matches, unpublished
nohead=idmm=pub=0
for p in glob.glob('wiki_content/*.html'):
    s=open(p,encoding='utf-8').read()
    if '<head>' not in s: nohead+=1
    i=re.search(r'<meta name="identifier" content="([^"]+)"',s)
    if not i or i.group(1) not in ids: idmm+=1
    w=re.search(r'<meta name="workflow_state" content="([^"]+)"',s)
    if not w or w.group(1)!='unpublished': pub+=1
L('pages: %d  no head: %d  identifier mismatch: %d  not unpublished: %d'%(len(pages),nohead,idmm,pub))
for n,v in (('pages with no head',nohead),('identifier mismatch',idmm),('pages not unpublished',pub)):
    if v: fails.append('%s: %d'%(n,v))

# 6 org items all resolve
org=re.findall(r'identifierref="([^"]+)"',man)
dang=[o for o in org if o not in ids]
L('organizations items: %d  dangling: %d'%(len(org),len(dang)))
if dang: fails.append('dangling org items: %s'%dang[:5])

# 7 publish states
# Assignment settings files come in two layouts in this program:
#   DAPR 2000:  g<hash>/assignment_settings.xml
#   DAPR 2020:  assignments/<slug>.xml, declared as a <file> of the assignment's resource
# Globbing one shape silently found zero in the other and reported every publish-state and
# rubric check clean. Resolve from the manifest; fall back to the glob only if that finds none.
def _resolve_assignments():
    out=[]
    for _m in re.finditer(r'<resource[^>]*type="associatedcontent/imscc_xmlv1p1/learning-application-resource"[^>]*>(.*?)</resource>',man,re.S):
        for _f in re.findall(r'<file href="([^"]+)"',_m.group(1)):
            _f=urllib.parse.unquote(_f)
            if _f.endswith('.xml') and os.path.exists(_f) and not _f.startswith('course_settings/'):
                try: _t=open(_f,encoding='utf-8',errors='ignore').read(4000)
                except Exception: continue
                # must be an assignment DOCUMENT, not merely a file that mentions points.
                # course_settings/assignment_groups.xml and rubrics.xml both carry
                # <points_possible> and are not assignments; counting them reported two
                # phantom "published assignments" that do not exist.
                # A graded quiz's meta carries a NESTED <assignment> block, which is what
                # creates its gradebook column (20.4). That makes it match both tests above
                # while not being an assignment at all, and an ungraded practice quiz's meta
                # has no <workflow_state> to find, so it reported as a published assignment.
                # DAPR 2255's MIDI diagnostic survey did exactly that. Require the file to be
                # an assignment DOCUMENT: <assignment> as its root element, not nested inside.
                if _f.endswith('_meta.xml'): continue
                _root=re.sub(r'<\?xml[^>]*\?>\s*','',_t,count=1).lstrip()
                if not _root.startswith('<assignment'): continue
                out.append(_f)
    return sorted(set(out))
a=_resolve_assignments() or [p for p in glob.glob('*/assignment_settings.xml')]
ap=sum(1 for p in a if '<workflow_state>unpublished</workflow_state>' not in open(p,encoding='utf-8').read())
L('assignments: %d  not unpublished: %d'%(len(a),ap))
if ap: fails.append('assignments not unpublished: %d'%ap)
mm=open('course_settings/module_meta.xml',encoding='utf-8').read()
# Some Canvas exports namespace every tag (<ns0:module>, <ns0:title>) and some do not.
# DAPR 3255 is namespaced. Every module check below matches bare tags, so without this
# normalization the whole module half of this script silently saw zero modules and
# reported clean. A false negative in a gate is worse than a false positive, because
# nothing ever tells you. Strip the prefix once, here, and match bare tags everywhere.
_ns=re.findall(r'<(\w+):modules[\s>]',mm)
if _ns:
    _p=_ns[0]
    mm=re.sub(r'</?%s:'%re.escape(_p), lambda m: m.group(0).replace(_p+':',''), mm)
    print('    note: module_meta.xml is namespaced (%s:), prefixes stripped for matching'%_p)
# Added 2026-09-24. The Instructor Use Only - [Do Not Publish] module now ships in every
# cartridge (Standards 0), carrying the live course's *No Publish pages VERBATIM: Adam's rule
# is copy them and change only dates and links. Those pages are never student visible, so
# the student page gates below (image on every page, content drift, headings, tables,
# contrast) do not score them. Resolved from module_meta, never matched by a phrase. Each
# page must still be unpublished, or it is scored like any other page.
_INSTR=set()
for _blk in re.findall(r'<module identifier="[^"]+">(.*?)</module>',mm,re.S):
    _tt=re.search(r'<title>([^<]*)</title>',_blk)
    if _tt and 'Instructor Use Only' in _tt.group(1):
        for _r in re.findall(r'<identifierref>([^<]+)</identifierref>',_blk):
            _h=RES.get(_r,{}).get('href')
            if _h and os.path.exists(_h) and 'content="unpublished"' in open(_h,encoding='utf-8',errors='ignore').read():
                _INSTR.add(_h)
L('instructor only pages carried verbatim, not scored as student pages: %d'%len(_INSTR))
# module-level state only. Module ITEMS legitimately stay 'active' (standards 22.6).
mods=re.findall(r'<module identifier="[^"]+">(.*?)(?=<module identifier=|</modules>)',mm,re.S)
mp=0
for b in mods:
    b=re.sub(r'<items>.*?</items>','',b,flags=re.S)
    w=re.search(r'<workflow_state>([^<]+)</workflow_state>',b)
    if not w or w.group(1)!='unpublished': mp+=1
L('modules: %d  not unpublished: %d'%(len(mods),mp))
if mp: fails.append('modules not unpublished: %d'%mp)
q=[m for _i,_q,m in QUIZ if m and os.path.exists(m)]
qa=sum(1 for p in q if '<available>true</available>' in open(p,encoding='utf-8').read())
L('quizzes: %d  available=true: %d'%(len(q),qa))
if qa: fails.append('quizzes available: %d'%qa)

# 9b every quiz has questions IN THE FILE THE MANIFEST POINTS AT, and they sum to the
# declared total. A quiz whose real questions live only in non_cc_assessments imports
# with zero questions and its full point value. Resolve the href, never the folder.
empty=[];mismatch=[]
for qid,qp,mp_ in QUIZ:
    if not mp_ or not os.path.exists(mp_):
        empty.append((qid,'no meta on disk')); continue
    s=open(mp_,encoding='utf-8').read()
    title=re.search(r'<title>(.*?)</title>',s,re.S)
    title=title.group(1) if title else qid
    dec=re.search(r'<points_possible>([\d.]+)</points_possible>',s)
    dec=float(dec.group(1)) if dec else 0.0
    if not os.path.exists(qp):
        empty.append((title,'manifest href missing on disk: '+qp)); continue
    body=open(qp,encoding='utf-8').read()
    _qns=re.findall(r'<(\w+):questestinterop[\s>]',body)
    if _qns:
        _qp=_qns[0]
        body=re.sub(r'</?%s:'%re.escape(_qp), lambda mo: mo.group(0).replace(_qp+':',''), body)
    n=len(re.findall(r'<item ident',body))
    tot=sum(float(v) for v in re.findall(r'<fieldlabel>points_possible</fieldlabel>\s*<fieldentry>([\d.]+)</fieldentry>',body))
    if n==0: empty.append((title,'0 questions in '+qp))
    elif abs(tot-dec)>0.01: mismatch.append((title,'questions sum to %g, declared %g'%(tot,dec)))
# 9b-1 Quiz shape: the true/false cap and the question count.
#   Standards 9.1c is LOCKED: no quiz, alternate or final carries more than five
#   true/false questions, because a coin flip measures nothing. Standards 11a sets a
#   module quiz at 25 questions, one point each. Neither was checked here before, and
#   DAPR 2255 shipped a module quiz that was 12 true/false out of 14. Counted from the
#   file the MANIFEST points at, the same file Canvas imports, never from a folder.
#   Whitespace between qtimetadata tags varies by generator, so nothing here assumes it.
#   9.1b also requires shuffled answers on every quiz. This is load bearing: a question
#   whose options were authored with the correct answer first is only fair because Canvas
#   shuffles them at delivery. If shuffling is ever switched off, position A becomes the
#   answer key for the whole exam.
#   20.4: a graded quiz carries its dates twice, once on the quiz and once inside the
#   nested <assignment> block that creates the gradebook column. They must agree. The
#   date check below skips the Final Exam by title, so a stale nested block on that one
#   object sailed through every build until v67, still reading the wrong finals day.
_split=[]
for _i,_q,_m in QUIZ:
    if not _m or not os.path.exists(_m): continue
    _s=open(_m,encoding='utf-8').read()
    _j=_s.find('<assignment identifier=')
    if _j<0: continue
    def _g(_t,_k):
        _x=re.search(r'<%s>([^<]*)</%s>'%(_k,_k),_t)
        return _x.group(1) if _x else ''
    # 8.0.1 / Canvas layout: the quiz level dates sit AFTER </assignment>, never before it.
    # Reading only _s[:_j] finds no date tags at all in a Canvas produced assessment_meta.xml,
    # so the check fired on every quiz that had a date and passed only when none did.
    _e=_s.find('</assignment>')
    _o=_s[:_j]+(_s[_e+len('</assignment>'):] if _e>0 else '')
    _n=_s[_j:_e] if _e>0 else _s[_j:]
    if (_g(_o,'due_at'),_g(_o,'unlock_at'))!=(_g(_n,'due_at'),_g(_n,'unlock_at')):
        _ti=re.search(r'<title>([^<]*)</title>',_o)
        _split.append((html.unescape(_ti.group(1)) if _ti else _m,
                       'quiz due %s unlock %s, gradebook column due %s unlock %s'%(_g(_o,'due_at'),_g(_o,'unlock_at') or '(none)',_g(_n,'due_at'),_g(_n,'unlock_at') or '(none)')))
        # Printing only due_at made a missing quiz-level unlock_at look like a gate bug:
        # both sides showed the same due date. Found on DAPR 2000 v62, 2026-09-24.
L('graded quizzes whose gradebook column disagrees with the quiz (must be 0): %d'%len(_split))
for _t,_w in _split[:8]: L('    %s | %s'%(_t,_w))
if _split: fails.append('quiz and gradebook column dates disagree: %d'%len(_split))

_noshuf=[m for _i,_q,m in QUIZ if m and os.path.exists(m)
         and '<shuffle_answers>true</shuffle_answers>' not in open(m,encoding='utf-8').read()]
L('quizzes with answer shuffling off (must be 0): %d'%len(_noshuf))
if _noshuf: fails.append('quizzes not shuffling answers: %s'%[os.path.basename(x) for x in _noshuf][:5])

_QT=re.compile(r'<fieldlabel>\s*question_type\s*</fieldlabel>\s*<fieldentry>\s*([^<]+?)\s*</fieldentry>',re.S)
_tfbad=[];_countbad=[]
for _qid,_qp,_mp in QUIZ:
    if not os.path.exists(_qp): continue
    _s=open(_qp,encoding='utf-8',errors='replace').read()
    _t=_QT.findall(_s)
    _ti=None
    if _mp and os.path.exists(_mp):
        _m=re.search(r'<title>(.*?)</title>',open(_mp,encoding='utf-8').read(),re.S)
        _ti=html.unescape(_m.group(1)) if _m else None
    _ti=_ti or os.path.basename(_qp)
    _tf=sum(1 for x in _t if x=='true_false_question')
    if _tf>5: _tfbad.append((_ti,'%d true/false questions, cap is 5'%_tf))
    _qns2=re.findall(r'<(\w+):questestinterop[\s>]',_s)
    if _qns2:
        _qp2=_qns2[0]
        _s=re.sub(r'</?%s:'%re.escape(_qp2), lambda mo: mo.group(0).replace(_qp2+':',''), _s)
    _n=len(re.findall(r'<item ident',_s))
    _graded=bool(_mp and '<assignment identifier=' in open(_mp,encoding='utf-8').read())
    # Set by Adam 2026-09-20: the rule binds a 25-point quiz to 25 questions and
    # the final to 100. It says nothing about smaller quizzes, and it never meant
    # to: requiring 25 questions on a 10-point quiz makes each question worth 0.4
    # points. A quiz at any other point value is not checked here.
    _pp=None
    if _mp:
        _mm=re.search(r'<points_possible>([\d.]+)',open(_mp,encoding='utf-8').read())
        if _mm: _pp=float(_mm.group(1))
    _target=None
    if 'Final Exam' in _ti: _target=100
    elif _pp is not None and abs(_pp-25.0)<0.01: _target=25
    if _graded and _target and _n!=_target:
        _countbad.append((_ti,'%d questions, the standard is %d'%(_n,_target)))
    for _x in re.findall(r'<mattext[^>]*>(.*?)</mattext>',_s,re.S):
        if 'of the above' in html.unescape(_x).lower():
            _tfbad.append((_ti,'an answer reads "of the above" and answers are shuffled (9.1c)')); break
L('quizzes over the true/false cap: %d   quizzes off the standard question count: %d'
  %(len(_tfbad),len(_countbad)))
for _t,_w in _tfbad[:10]: L('    %s | %s'%(_t,_w))
for _t,_w in _countbad[:12]: L('    %s | %s'%(_t,_w))
if _tfbad: fails.append('quizzes over the true/false cap: %d'%len(_tfbad))
if _countbad: warns.append('quizzes off the 25 question standard: %d'%len(_countbad))

# 9b-2 Rubrics (Standards 11b-1 LOCKED, Platform Reference 36).
#   A rubric that does not resolve, does not sum, or does not drive the grade looks
#   identical in Canvas to one that does, right up until grades are due.
_rub={}
if os.path.exists('course_settings/rubrics.xml'):
    _rs=open('course_settings/rubrics.xml',encoding='utf-8').read()
    if 'course_settings/rubrics.xml' not in man:
        fails.append('rubrics.xml is on disk but not declared in the manifest')
    for _m in re.finditer(r'<rubric identifier="([^"]+)">(.*?)</rubric>',_rs,re.S):
        _i,_b=_m.group(1),_m.group(2)
        _pp=re.search(r'<points_possible>([\d.]+)</points_possible>',_b)
        _crit=[float(x) for x in re.findall(r'<criterion_id>[^<]*</criterion_id>\s*<points>([\d.]+)</points>',_b)]
        _rats=[float(x) for x in re.findall(r'<rating>\s*<description>[^<]*</description>\s*<points>([\d.]+)</points>',_b)]
        _rub[_i]={'pts':float(_pp.group(1)) if _pp else None,'crit':_crit,
                  'title':(re.search(r'<title>([^<]*)</title>',_b) or [None,''])[1] if False else
                          (re.search(r'<title>([^<]*)</title>',_b).group(1) if re.search(r'<title>([^<]*)</title>',_b) else _i),
                  'maxrat':max(_rats) if _rats else 0.0}
        if _pp and abs(sum(_crit)-float(_pp.group(1)))>0.01:
            fails.append('rubric %s: criteria sum to %g, declares %s'%(_i[:12],sum(_crit),_pp.group(1)))
        if _rats and _crit and max(_rats)>max(_crit)+0.01:
            fails.append('rubric %s: a rating exceeds its criterion points'%_i[:12])
_withref=0
# 8.0.1 / Canvas layout: a course export writes assignments/<slug>.xml, not
# assignments/<slug>/assignment_settings.xml. Globbing only the folder form matched
# nothing, so every rubric check below was skipped and the block could only report
# "0 of n" - which read as a warning about the cartridge instead of about this glob.
# Use the same resolved list the rest of the file uses.
for _p in a:
    if not os.path.isfile(_p): continue
    _lbl=os.path.dirname(_p) if os.path.basename(_p)=='assignment_settings.xml' else os.path.basename(_p)
    _t=open(_p,encoding='utf-8').read()
    _r=re.search(r'<rubric_identifierref>([^<]+)</rubric_identifierref>',_t)
    if not _r: continue
    _withref+=1
    if _r.group(1) not in _rub:
        fails.append('%s: rubric_identifierref resolves to nothing'%_lbl)
        continue
    _ap=re.search(r'<points_possible>([\d.]+)</points_possible>',_t)
    if _ap and _rub[_r.group(1)]['pts'] is not None and abs(_rub[_r.group(1)]['pts']-float(_ap.group(1)))>0.01:
        fails.append('%s: rubric is %g points, assignment is %s'%(_lbl,_rub[_r.group(1)]['pts'],_ap.group(1)))
    if '<rubric_use_for_grading>true</rubric_use_for_grading>' not in _t:
        fails.append('%s: rubric_use_for_grading is not true, so the rubric displays but does not score'%_lbl)
L('rubrics defined: %d   assignments declaring one: %d of %d'%(len(_rub),_withref,len(a)))
if _rub and _withref==0: warns.append('rubrics are defined but no assignment references one')

L('quizzes with no questions in the imported file: %d   point mismatches: %d'%(len(empty),len(mismatch)))
for t,r in (empty+mismatch)[:10]: L('   %s | %s'%(t,r))
if empty: fails.append('quizzes with no questions: %d'%len(empty))
if mismatch: fails.append('quiz point mismatches: %d'%len(mismatch))

# 9c LTI hygiene, see Platform Reference 38.3a.
# Roll Call is supplied by UVU at the account level, so a portable copy of its
# configuration must never ride along. No credential may ever be packaged. And
# every external_tool_identifierref has to resolve, so removing a tool config
# cannot leave an assignment pointing at nothing.
lti=[p_ for p_ in glob.glob('*.xml')+glob.glob('*/*.xml') if 'basiclti' in open(p_,encoding='utf-8',errors='ignore').read()[:4000]]
rollcall=[]
for p_ in lti:
    s=open(p_,encoding='utf-8',errors='ignore').read()
    t=re.search(r'<blti:title>(.*?)</blti:title>',s,re.S)
    tid=re.search(r'name="tool_id">([^<]*)<',s)
    if (t and 'roll call' in t.group(1).lower()) or (tid and tid.group(1).strip().lower()=='rollcall'):
        rollcall.append(p_)
creds=[]
for p_ in lti:
    s=open(p_,encoding='utf-8',errors='ignore').read()
    for k in ('consumer_key','shared_secret','oauth_consumer_key','access_token','private_key'):
        if k in s: creds.append('%s | %s'%(p_,k))
etrefs=[]
for p_ in a:
    s=open(p_,encoding='utf-8',errors='ignore').read()
    for m_ in re.finditer(r'<external_tool_identifierref>\s*([^<\s]+)\s*</external_tool_identifierref>',s):
        if m_.group(1) not in ids: etrefs.append('%s -> %s'%(p_,m_.group(1)))
L('LTI files: %d   Roll Call configs: %d   credentials: %d   dangling external_tool refs: %d'
  %(len(lti),len(rollcall),len(creds),len(etrefs)))
for v in (rollcall+creds+etrefs)[:8]: L('   %s'%v)
# 9d every Cloudflare worker link a student can click must actually return 200.
# A cartridge can pass every structural check and still ship a dead download, because
# the file lives outside the package. Set DAPR_PREFLIGHT_NO_NET=1 to skip when offline.
if not os.environ.get('DAPR_PREFLIGHT_NO_NET'):
    import urllib.request,urllib.error
    wurls=set()
    for p_ in glob.glob('wiki_content/*.html')+glob.glob('*/*.html')+glob.glob('*/*.xml'):
        try: s=open(p_,encoding='utf-8',errors='ignore').read()
        except Exception: continue
        for m_ in re.finditer(r'https://uvu-files\.adamo\.workers\.dev/[^"\'\s<>)\]]+',s):
            wurls.add(m_.group(0).replace('&amp;','&'))
    dead=[]
    for u in sorted(wurls):
        try:
            # the worker does not answer HEAD; ask for one byte instead
            # Cloudflare 403s the default Python user agent, so present a browser one
            rq=urllib.request.Request(u,headers={'Range':'bytes=0-0',
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/140.0 Safari/537.36'})
            with urllib.request.urlopen(rq,timeout=25) as r:
                if r.status not in (200,206): dead.append((u,r.status))
        except urllib.error.HTTPError as e: dead.append((u,e.code))
        except Exception as e: dead.append((u,'unreachable: %s'%type(e).__name__))
    L('Cloudflare student downloads checked live: %d   dead: %d'%(len(wurls),len(dead)))
    for u,c in dead[:8]: L('   %s  %s'%(c,u.split('/')[-1]))
    if dead: fails.append('dead Cloudflare download links: %d'%len(dead))
else:
    L('Cloudflare link check SKIPPED (DAPR_PREFLIGHT_NO_NET set)')

if rollcall: fails.append('Roll Call LTI config present (38.3a): %s'%rollcall[:3])
if creds:    fails.append('LTI credential packaged (38.3a rule 3): %s'%creds[:3])
if etrefs:   fails.append('dangling external_tool_identifierref (38.3a rule 7): %s'%etrefs[:3])

# 8 QTI hygiene
ne=na=0
for p in sorted(set(glob.glob('**/*.qti',recursive=True))|set(QTI_FILES)):
    s=open(p,encoding='utf-8',errors='replace').read()
    if any(ord(c)>127 for c in s): na+=1
    if re.search(r'&(?!amp;|lt;|gt;|quot;|apos;|#)\w+;',s): ne+=1
L('quiz files with non-ASCII: %d   with named entities: %d'%(na,ne))
if na: fails.append('non-ASCII in quiz XML: %d files'%na)
if ne: fails.append('HTML named entities in quiz XML: %d files'%ne)

# 9 question groups resolve
banks=set()
for p in glob.glob('**/*',recursive=True):
    if not os.path.isfile(p): continue
    try: s=open(p,encoding='utf-8',errors='replace').read()
    except: continue
    banks.update(re.findall(r'<(?:objectbank|section)[^>]*ident="([^"]+)"',s))
refs=[]
for p in glob.glob('**/*',recursive=True):
    if not os.path.isfile(p): continue
    try: s=open(p,encoding='utf-8',errors='replace').read()
    except: continue
    refs+= re.findall(r'sourcebank_ref"?\s*>?\s*([0-9a-zA-Z_]{8,})',s)
ur=sorted({r for r in refs if r not in banks})
L('question group refs: %d  unresolved: %d'%(len(refs),len(ur)))
if ur: fails.append('unresolved question groups: %s'%ur[:5])

# 10 quiz images must be internal (Canvas quiz iframe is default-src none)
ext=0
for p in sorted(set(glob.glob('**/*.qti',recursive=True))|set(QTI_FILES)):
    ext+=len(re.findall(r'src=(?:&quot;|")https?://',open(p,encoding='utf-8',errors='replace').read()))
L('quiz images on an external host (must be 0): %d'%ext)
if ext: fails.append('external quiz image refs: %d'%ext)

# 11 alt text and inline svg
noalt=svg=0
for p in glob.glob('wiki_content/*.html'):
    s=open(p,encoding='utf-8').read()
    svg+= s.count('<svg')
    for m in re.finditer(r'<img[^>]*>',s):
        if 'alt=' not in m.group(0): noalt+=1
L('images with no alt attribute: %d   inline <svg>: %d'%(noalt,svg))
if noalt: fails.append('images with no alt: %d'%noalt)
if svg: warns.append('inline svg present: %d'%svg)

# 12 week suffixes must not appear in module titles
wk=len(re.findall(r'\(Week\s*\d+\)',mm))
if wk: fails.append('module titles with week suffix: %d'%wk)

# --- 6.8 every student-visible module carries at least four pages ------------------
_mm68=open('course_settings/module_meta.xml',encoding='utf-8').read()
_p68=re.findall(r'<(\w+):modules[\s>]',_mm68)
if _p68: _mm68=re.sub(r'</?%s:'%re.escape(_p68[0]),lambda m:m.group(0).replace(_p68[0]+':',''),_mm68)
_thin=[]
for _blk in re.findall(r'<module identifier="[^"]+">(.*?)(?=<module identifier=|</modules>)',_mm68,re.S):
    _t=re.search(r'<title>([^<]*)</title>',_blk)
    if not _t: continue
    _name=_t.group(1)
    # a hidden instructor-only module is exempt
    if ('Instructor Resources' in _name or 'Instructor Notes' in _name
            or '(Hidden)' in _name): continue
    # A final exam module is not a thin module. The comment below already says
    # so; the zero-page test underneath only exempted one that carries no study
    # guide at all, which penalised the better-built version. 6.8 is about
    # reading too slight to support a quiz, and a final exam is not that.
    if 'Final Exam' in _name: continue
    _pg=len(re.findall(r'<content_type>WikiPage</content_type>',_blk))
    # A module that deliberately holds no pages, such as one containing only the final exam,
    # is not a thin module. 6.8 is about reading too slight to support a quiz, not about a
    # module that was never meant to carry reading.
    if _pg==0: continue
    # Nor is a module that carries no graded object at all. 6.8 measures reading
    # against the quiz it has to support, so with no quiz and no assignment there
    # is nothing to measure. Added 2026-09-22 for Course Orientation, which is
    # three pages because the shared Student Essentials module in Canvas carries
    # the rest. Stated by Adam the same day: none of those pages belong in the
    # cartridge. This is deliberately a shape test, not a name test, so the next
    # orientation-shaped module needs no further patch.
    _graded68=re.findall(r'<content_type>(Quizzes::Quiz|Assignment|DiscussionTopic)</content_type>',_blk)
    if not _graded68: continue
    if _pg<4: _thin.append('%s (%d)'%(_name,_pg))
L('modules with fewer than four pages (must be 0): %d'%len(_thin))
for _x in _thin[:12]: L('    %s'%_x)
if _thin: fails.append('modules under four pages: %d'%len(_thin))

# --- 21.1g module items must resolve to a payload -------------------------------
_mmraw=open('course_settings/module_meta.xml',encoding='utf-8').read()
_p=re.findall(r'<(\w+):modules[\s>]',_mmraw)
if _p: _mmraw=re.sub(r'</?%s:'%re.escape(_p[0]),lambda m:m.group(0).replace(_p[0]+':',''),_mmraw)
_dead=[]
for _it in re.finditer(r'<item identifier="[^"]+">(.*?)</item>',_mmraw,re.S):
    _b=_it.group(1)
    _ct=re.search(r'<content_type>([^<]*)</content_type>',_b)
    if not _ct or _ct.group(1) not in ('Attachment',): continue
    _t=re.search(r'<title>([^<]*)</title>',_b)
    _r=re.search(r'<identifierref>([^<]*)</identifierref>',_b)
    _has=False
    if _r:
        _m2=re.search(r'<resource identifier="%s"[^>]*>(.*?)</resource>'%re.escape(_r.group(1)),man,re.S)
        if _m2:
            for _f in re.findall(r'<file href="([^"]+)"',_m2.group(1)):
                if os.path.exists(urllib.parse.unquote(_f)): _has=True
            if re.search(r'href="https?://',_m2.group(0)): _has=True
    if not _has: _dead.append(_t.group(1) if _t else '?')
L('attachment module items with no file and no URL (must be 0): %d'%len(_dead))
for _d in _dead[:10]: L('    %s'%_d)
if _dead: fails.append('dead attachment items: %d'%len(_dead))

L('module titles carrying a (Week NN) suffix (must be 0): %d'%wk)
if wk: fails.append('module titles with week suffix: %d'%wk)

# 12b a page's filename IS its Canvas URL. A module or week number in a page URL is a
#     promise about teaching order that a course taught in any order cannot keep.
slugs=[f[:-5] for f in os.listdir('wiki_content') if f.endswith('.html')] if os.path.isdir('wiki_content') else []
numbered=sorted(x for x in slugs if re.match(r'm\d|wk\d|week[-_]?\d|module[-_]?\d',x))
L('page URLs carrying a module or week number (must be 0): %d'%len(numbered))
if numbered:
    for x in numbered[:8]: L('    %s'%x)
    fails.append('numbered page URLs: %d'%len(numbered))

# 12c every $WIKI_REFERENCE$ cross-link must name a page that exists
sset=set(slugs); dead=[]; xtot=0
for dp,dn,fn in os.walk('.'):
    for f in fn:
        if not f.endswith(('.html','.xml')): continue
        try: t=open(os.path.join(dp,f),encoding='utf-8').read()
        except Exception: continue
        for m in re.findall(r'\$WIKI_REFERENCE\$/pages/([A-Za-z0-9._-]+)',t):
            xtot+=1
            if m not in sset: dead.append((os.path.relpath(os.path.join(dp,f),'.'),m))
L('page cross-links: %d   pointing at a page that does not exist: %d'%(xtot,len(dead)))
if dead:
    for d in dead[:8]: L('    %s -> %s'%d)
    fails.append('dead page cross-links: %d'%len(dead))

# 12d content drift: no page may describe a graded object the package does not contain,
#     and no page may name a module that is not in module_meta. Instructor pages drift
#     silently because nothing renders them against the cartridge.
graded=set(re.findall(r'<title>([^<]*)</title>',mm))
modtitles={html.unescape(t).strip() for t in re.findall(r'<module identifier[^>]*>\s*<title>([^<]*)</title>',mm)}
allmm=' '.join(graded).lower()
GHOSTS=[('midterm','a midterm exam'),('practice quiz','a practice quiz'),
        ('lc623a','an LC623a item'),('boaa','a BOAA item')]
drift=[]
for dp,dn,fn in os.walk('wiki_content'):
    for f in sorted(fn):
        if not f.endswith('.html'): continue
        if os.path.join(dp,f) in _INSTR: continue
        body=open(os.path.join(dp,f),encoding='utf-8').read()
        txt=html.unescape(re.sub(r'<[^>]+>',' ',body)).lower()
        for needle,label in GHOSTS:
            if needle in txt and needle not in allmm:
                # a page may say the thing is gone; it may not schedule or assign it
                VERBS=r'\b(due|opens|covers|worth|run the|assign|assigned|set it|scheduled for)\b'
                CLEARED=('no '+needle,'not in this course','was deleted','does not exist',
                         'gone','is not','are not','used to','no longer','never built')
                for _v in [0]:
                    for m in re.finditer(re.escape(needle),txt):
                        near=txt[max(0,m.start()-90):m.start()+90]
                        if re.search(VERBS,near) and not any(c in near for c in CLEARED):
                            drift.append((f,label,' '.join(near.split())[:90])); break
L('pages describing a graded object the package does not contain (must be 0): %d'%len(drift))
if drift:
    for d in drift[:6]: L('    %s: %s :: ...%s...'%d)
    fails.append('content drift: %d'%len(drift))

# 12e Standards 6.2: no sequence numbering in ANY visible title. Module titles, module
#     item titles, assignment and quiz titles, and rubric titles all counted. The old
#     week-suffix check caught only "(Week NN)" and only in module titles, which let
#     "DAW: M7 - Your First Mix" and "Electronics: 03 AC & DC" through untouched.
NUMBERED=re.compile(r'(?:^|[:\s(])(?:M-?\d{1,2}\b|Q\d{1,2}\b|Module\s*\d|Week\s*\d|Wk\s*\d|\d{1,2}\.\d\b)'
                    r'|^\s*\d{1,2}[)\.]\s|:\s*\d{1,2}\s+[A-Z]', re.I)
# proper names and real course codes are names, not sequence: Wwise 101, DAPR 3345, CLO 3
EXEMPT=re.compile(r'\b(?:DAPR|MUSC|THEA)\s*\d{3,4}\b|\bWwise\s*\d{3}\b|\bCLO\s*\d\b|\b\d{3,4}\s*Hz\b'
                  r'|\bMix\s*\d[AB]?\b|\bLayer\s*\d\b|\d+(?:\.\d+)?\s*%|\d+(?:\.\d+)?\s*(?:pts?|points)\b', re.I)
titles=set()
for m in re.finditer(r'<title>([^<]*)</title>',mm): titles.add(('module_meta',html.unescape(m.group(1))))
# 12e-2 [2026-09-24]: the manifest organizations block carries its own copy of every
#   module item title. Canvas imports module structure from module_meta.xml, so drift
#   here is invisible in Canvas and visible to every other reader of the cartridge, and
#   it is where retired titles survive a rename ("M07: ... (classic)", "Quiz 03 - ...").
_orgt={}
for m in re.finditer(r'<item identifier="[^"]+" identifierref="([^"]+)"><title>([^<]*)</title>',man):
    _orgt[m.group(1)]=html.unescape(m.group(2))
    titles.add(('manifest',html.unescape(m.group(2))))
_metat={}
for m in re.finditer(r'<item identifier="[^"]+">(.*?)</item>',mm,re.S):
    _b=m.group(1)
    _t=re.search(r'<title>([^<]*)</title>',_b); _r=re.search(r'<identifierref>([^<]*)</identifierref>',_b)
    if _t and _r: _metat[_r.group(1)]=html.unescape(_t.group(1))
_drift=sorted(k for k in _orgt if k in _metat and _orgt[k]!=_metat[k])
L('manifest item titles disagreeing with module_meta (must be 0): %d'%len(_drift))
for k in _drift[:10]: L('   %s | manifest %r | module_meta %r'%(k[:10],_orgt[k][:46],_metat[k][:46]))
if _drift: fails.append('manifest and module_meta item titles disagree: %d'%len(_drift))
# 12e-3 [2026-09-24]: a cartridge export writes assignments/<slug>.xml and
#   quizzes/<id>_meta.xml. Only the course-copy names were listed, so no assignment or
#   quiz title was ever checked for sequence numbering on a real export.
for _p in glob.glob('assignments/*.xml')+glob.glob('quizzes/*_meta.xml'):
    _t=open(_p,encoding='utf-8').read()
    for m in re.finditer(r'<title>([^<]*)</title>',_t): titles.add((os.path.basename(_p),html.unescape(m.group(1))))
for dp,dn,fn in os.walk('.'):
    for f in fn:
        if f not in ('assessment_meta.xml','assignment_settings.xml'): continue
        t=open(os.path.join(dp,f),encoding='utf-8').read()
        for m in re.finditer(r'<title>([^<]*)</title>',t): titles.add((f,html.unescape(m.group(1))))
for dp,dn,fn in os.walk('.'):
    for f in fn:
        if not f.endswith('.xml'): continue
        t=open(os.path.join(dp,f),encoding='utf-8').read()
        if '<rubric ' not in t and 'rubricCriterion' not in t: continue
        for m in re.finditer(r'<title>([^<]*)</title>',t): titles.add(('rubric',html.unescape(m.group(1))))
numbered=sorted({(w,t) for w,t in titles if NUMBERED.search(EXEMPT.sub('',t))})
L('titles carrying a sequence number (must be 0): %d'%len(numbered))
piped=sorted({(w,t) for w,t in titles if '|' in t})
L('titles carrying a pipe character (must be 0): %d'%len(piped))
if piped:
    for w,t in piped[:8]: L('    [%s] %s'%(w,t))
    fails.append('piped titles: %d'%len(piped))
if numbered:
    for w,t in numbered[:10]: L('    [%s] %s'%(w,t))
    fails.append('numbered titles: %d'%len(numbered))


# 12h Standards 8.1, which was already written and was ignored twice on 2026-09-20:
#     "every module's folder holds what that module uses and no page has to reach into
#     another module's folder", and "every image filename begins with the slug of the topic
#     folder it sits in". Both were violated: a module referenced another COURSE's images,
#     and then a set of non-topic folders was invented to hold them. Neither produced any
#     error, because the URLs resolved. Now it fails the build.
#     Set DAPR_COURSE_FOLDER to this course's repo folder name, e.g.
#     DAPR-2000--Digital_Audio_Essentials.
_cf=os.environ.get('DAPR_COURSE_FOLDER')
if _cf:
    _foreign=[]; _misnamed=[]
    _seen=set()
    for dp,dn,fn in os.walk('wiki_content'):
        for f in sorted(fn):
            if not f.endswith('.html'): continue
            t=open(os.path.join(dp,f),encoding='utf-8',errors='replace').read()
            for m in re.finditer(r'src="[^"]*?/Classes/([^/"]+)/Images/([^/"]+)/([^/"]+)"',t):
                course,topic,fname=m.group(1),m.group(2),m.group(3)
                key=(course,topic,fname)
                if key in _seen: continue
                _seen.add(key)
                if course!=_cf: _foreign.append((f,course,topic,fname)); continue
                if not fname.startswith(topic+'-'): _misnamed.append((topic,fname))
    L('images referenced from another course (must be 0): %d'%len(_foreign))
    if _foreign:
        for x in _foreign[:6]: L('    %s -> Classes/%s/Images/%s/%s'%x)
        fails.append('cross-course image refs: %d'%len(_foreign))
    L('image filenames not prefixed by their topic folder (must be 0): %d'%len(_misnamed))
    if _misnamed:
        for tp,fn2 in _misnamed[:8]: L('    Images/%s/%s'%(tp,fn2))
        fails.append('image filename prefix mismatches: %d'%len(_misnamed))

# 12e-1 Sections that are not permitted on a student facing page (Standards 6.8, 17).
#     A module overview carries Learning Objectives, Before Class and a Conclusion.
#     "During Class" and "Looking Ahead" are instructor notes and are prohibited on
#     every overview page in every DAPR course, as are bring-to-class supply lists.
#     DAPR 2255 v65 carried all of one page with both, and nothing was looking.
BANNED=[('Looking Ahead','a Looking Ahead section'),
        ('During Class','a During Class section'),
        ('Bring to class','a bring-to-class list'),
        ('Bring to Class','a bring-to-class list')]
_bansec=[]
for _p in glob.glob('wiki_content/*.html')+glob.glob('*/*.html'):
    _t=open(_p,encoding='utf-8',errors='replace').read()
    for _needle,_why in BANNED:
        if re.search(r'<h[1-4][^>]*>\s*%s\s*</h[1-4]>'%re.escape(_needle),_t):
            _bansec.append((_p,_why))
L('student pages carrying an instructor-only section (must be 0): %d'%len(_bansec))
for _p,_w in _bansec[:10]: L('    %s | %s'%(_p,_w))
if _bansec: fails.append('instructor-only sections on student pages: %d'%len(_bansec))

# 12f Dates. Found 2026-09-20 on DAPR 2010: every graded object shipped with an empty
#     <due_at/>, and Canvas imports that silently as "no due date" with no warning.
#     The second half of the same trap is the daylight saving offset. Mountain time is
#     UTC-7 in standard time and UTC-6 in daylight time, so a single hardcoded offset
#     puts half a term's due dates an hour wrong and nothing ever complains. This check
#     converts each Zulu stamp back to Mountain local and asserts the house rule:
#     due Friday 9:00 AM, opens Monday midnight, and open before due.
import datetime as _dt

def _nth_sun(y, month, n):
    d = _dt.date(y, month, 1)
    d += _dt.timedelta(days=(6 - d.weekday()) % 7)
    return d + _dt.timedelta(days=7 * (n - 1))

def _mountain(z):
    """Zulu string -> naive Mountain local datetime, US DST rules."""
    u = _dt.datetime.strptime(z, '%Y-%m-%dT%H:%M:%SZ')
    start = _dt.datetime.combine(_nth_sun(u.year, 3, 2), _dt.time(9))    # 2 AM MST = 09Z
    end = _dt.datetime.combine(_nth_sun(u.year, 11, 1), _dt.time(8))     # 2 AM MDT = 08Z
    return u - _dt.timedelta(hours=6 if start <= u < end else 7)

_dated, _undated, _dbad = [], [], []
# Amended 2026-09-24 (DAPR 3255 v11). The last day of classes is not always a Friday.
# Spring 2027 ends on Tue Apr 27, and Adam set the last Electronics quizzes, the Talkback
# Box and the bonus builds to close there at 9:00 AM. That is the one date allowed to break
# the Friday rule. It is read from the term spine files beside this script, never typed.
_LAST_CLASS_DAYS = set()
for _spine in ('spring_2027_spine.py', 'fall_2026_spine.py'):
    _sp = os.path.join(os.path.dirname(os.path.abspath(__file__)), _spine)
    if os.path.exists(_sp):
        try:
            import runpy as _rp
            _lc = _rp.run_path(_sp).get('LAST_CLASS')
            if _lc: _LAST_CLASS_DAYS.add(_lc)
        except Exception:
            pass
#     Amended again 2026-09-20. This loop used to walk for files literally named
#     assessment_meta.xml. A flat-layout package names them quizzes/quiz_<slug>_meta.xml,
#     so on DAPR 2255 it saw 14 of 36 graded objects and called the other 22 clean.
#     Resolve the objects from the manifest inventory instead of matching filenames,
#     and take each object's owning identifier from the resource, not from its folder.
_targets = [(os.path.basename(os.path.dirname(_p)), _p)
            for _p in a]
_targets += [(_qid, _mp) for _qid, _qp, _mp in QUIZ if _mp and os.path.exists(_mp)]
for _own, p in _targets:
        f = os.path.basename(p)
        t = open(p, encoding='utf-8').read()
        if f.endswith('_meta.xml') and '<assignment identifier=' not in t:
            continue                                   # ungraded quiz, no gradebook column
        # Amended 2026-09-20. Three deliberate cases were failing this check on DAPR 2000:
        #   - held alternate quizzes, kept in the package but removed from every module
        #   - Roll Call Attendance, which is ongoing and has no single due date
        #   - the Final Exam, scheduled by the university's finals period, not by a Friday
        # An object that no module references has no module schedule to honor, so skip it.
        if _own and _own not in mm:
            continue
        _ti0 = re.search(r'<title>([^<]*)</title>', t)
        if _ti0 and ('Final Exam' in _ti0.group(1) or 'Roll Call' in _ti0.group(1)):
            continue
        ti = re.search(r'<title>([^<]*)</title>', t)
        ti = html.unescape(ti.group(1)) if ti else p
        du = re.search(r'<due_at>([^<]+)</due_at>', t)
        un = re.search(r'<unlock_at>([^<]+)</unlock_at>', t)
        if not du:
            _undated.append(ti)
            continue
        _dated.append(ti)
        try:
            d = _mountain(du.group(1))
        except Exception:
            _dbad.append((ti, 'due_at is not a Zulu timestamp: %s' % du.group(1)))
            continue
        _end_of_term_ok = d.date() in _LAST_CLASS_DAYS and (d.hour, d.minute) == (9, 0)
        if not _end_of_term_ok and (d.weekday() != 4 or (d.hour, d.minute) != (9, 0)):
            _dbad.append((ti, 'due %s Mountain, house rule is Friday 9:00 AM' %
                          d.strftime('%a %Y-%m-%d %H:%M')))
        if un:
            try:
                o = _mountain(un.group(1))
            except Exception:
                _dbad.append((ti, 'unlock_at is not a Zulu timestamp: %s' % un.group(1)))
                continue
            if o.weekday() != 0 or (o.hour, o.minute) != (0, 0):
                _dbad.append((ti, 'opens %s Mountain, house rule is Monday midnight' %
                              o.strftime('%a %Y-%m-%d %H:%M')))
            if o >= d:
                _dbad.append((ti, 'opens %s, due %s' % (o, d)))
L('graded objects with a due date: %d   without: %d   date defects: %d'
  % (len(_dated), len(_undated), len(_dbad)))
if _dated and _undated:
    for t in _undated[:8]:
        L('    no due date: %s' % t)
    fails.append('graded objects with no due date: %d' % len(_undated))
elif _undated:
    warns.append('no due dates set on any graded object: %d' % len(_undated))
if _dbad:
    for t, why in _dbad[:10]:
        L('    %s :: %s' % (t, why))
    fails.append('date defects: %d' % len(_dbad))

# 12g orphaned image folders. An image committed to the repo and referenced by nothing is
#     invisible: it costs repo size, it looks like work that was done, and nobody notices.
#     106 connector images sat unused by all seven courses until 2026-09-20, added for a
#     module that was never built. A WARNING, not a hard fail: a spare image is a judgement
#     call and a build should not block on one. Point DAPR_REPO_IMAGES at the course's own
#     Images folder, not another course's.
_repo=os.environ.get('DAPR_REPO_IMAGES')
if _repo and os.path.isdir(_repo):
    _used=set()
    for dp,dn,fn in os.walk('.'):
        for f in fn:
            if not f.endswith(('.html','.xml','.qti')): continue
            try: t=open(os.path.join(dp,f),encoding='utf-8',errors='replace').read()
            except Exception: continue
            for m in re.finditer(r'/([A-Za-z0-9._-]+\.(?:png|jpe?g|svg|webp))',t): _used.add(m.group(1))
    _by={}
    for dp,dn,fn in os.walk(_repo):
        for f in fn:
            if not f.lower().endswith(('.png','.jpg','.jpeg','.svg','.webp')): continue
            k=os.path.basename(dp); _by.setdefault(k,[0,0]); _by[k][0]+=1
            if f in _used: _by[k][1]+=1
    _dead=sorted(k for k,(tot,u) in _by.items() if tot and u==0)
    _tot=sum(t for t,_ in _by.values()); _u=sum(u for _,u in _by.values())
    L('repo images referenced by this course: %d of %d   folders referenced by nothing: %d'%(_u,_tot,len(_dead)))
    for d in _dead[:8]: L('    unused folder: %s (%d images)'%(d,_by[d][0]))
    if _dead: warns.append('image folders referenced by nothing: %d'%len(_dead))

# ---------------------------------------------------------------- 7a / 11b page conformance
# Added 2026-09-20. v19 passed every other gate while 27 of 33 assignment pages were
# broken, because nothing here looked at an assignment body. 18a.4: a gate that cannot
# fail on the thing that matters is not a gate.
ICONREF = 'DAPR_Canvas_Icon_Reference'
_noicon=[]; _nosubmit=[]; _nopoints=[]; _norubric=[]; _offpage=[]
_multi_h2=[]; _heading_skip=[]; _noheading=[]; _emptyalt=[]; _numbered_p=[]; _lowcontrast=[]

def _lum(h):
    h=h.lstrip('#')
    if len(h)==3: h=''.join(c*2 for c in h)
    if len(h)!=6: return None
    try: r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    except ValueError: return None
    f=lambda c: c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)

def _ratio(a,b):
    la,lb=_lum(a),_lum(b)
    if la is None or lb is None: return None
    hi,lo=max(la,lb),min(la,lb)
    return (hi+0.05)/(lo+0.05)

# Amended 2026-09-24 [Adam approved]. This block globbed assignments/*.html only. DAPR 2000
# writes each assignment body as g<hash>/<slug>.html beside its assignment_settings.xml, so the
# conformance block reported "0 assignment pages" on a package holding 15 and checked none of
# them, and the accessibility checks below never saw an assignment body either. Resolve the
# body pages from the assignment documents already resolved from the manifest (list a, rule 7).
_assign_pages=set(glob.glob('assignments/*.html'))
for _af in a:
    _d=os.path.dirname(_af)
    if _d and _d!='assignments':
        _assign_pages.update(glob.glob(os.path.join(_d,'*.html')))
    elif _d=='assignments':
        _h=_af[:-4]+'.html'
        if os.path.exists(_h): _assign_pages.add(_h)
_pages = sorted(_assign_pages) + sorted(p for p in glob.glob('wiki_content/*.html') if p not in _INSTR)
for _p in _pages:
    _t = open(_p,encoding='utf-8',errors='ignore').read()
    _txt = html.unescape(re.sub(r'<[^>]+>',' ',_t))
    _is_assign = _p in _assign_pages

    # --- accessibility, all pages
    # Headings. WCAG asks that levels are never SKIPPED on the way down. Returning
    # from h3 back up to h2 starts a new sibling section and is correct, not a defect.
    # An earlier version of this gate flagged the return, which was wrong, and it
    # condemned 12 pages that were fine. Corrected 2026-09-21.
    _hs=[int(m.group(1)) for m in re.finditer(r'<h([1-6])\b',_t)]
    if not _hs:
        _noheading.append(_p)
    else:
        if _hs[0] != 2:
            _heading_skip.append('%s starts at h%d, Canvas supplies the h1'%(_p,_hs[0]))
        else:
            for _i in range(1,len(_hs)):
                if _hs[_i] > _hs[_i-1]+1:
                    _heading_skip.append('%s skips h%d to h%d'%(_p,_hs[_i-1],_hs[_i])); break
    # 7a assignment pages carry exactly one h2, the green banner, and h3 below it.
    # Content pages may carry as many h2 sections as they need.
    if _is_assign and _hs.count(2) > 1: _multi_h2.append(_p)
    # A bare alt="" is Severe (Standards 2). Canvas's Ally plugin writes its own
    # data-ally-user-updated-alt="" alongside a perfectly good alt, and the first
    # version of this check matched that substring and accused the syllabus, whose
    # logo alt text is correct. Anchor on the attribute boundary. Fixed 2026-09-21.
    if re.search(r'(?<![-\w])alt=""',_t): _emptyalt.append(_p)
    # 11b worksheet blocks are manually numbered ON PURPOSE: an <ol> renumbers itself
    # when it is pasted into Word, which breaks the question numbers the rubric refers
    # to. So blank out every user-select:all block before looking for numbered runs.
    _outside = re.sub(r'<div[^>]*user-select\s*:\s*all.*?</div>', ' ', _t, flags=re.S|re.I)
    _ps=re.findall(r'<p[^>]*>\s*(?:<strong>)?\s*(\d)\.',_outside)
    _run=0
    for _a,_b in zip(_ps,_ps[1:]):
        _run = _run+1 if int(_b)==int(_a)+1 else 0
        if _run>=2: _numbered_p.append(_p); break
    for _m in re.finditer(r'style="([^"]*)"',_t):
        _st=_m.group(1)
        # Must not match border-color, outline-color, border-top-color and friends.
        # The first version used a (?<!background-) lookbehind only, so 'border-color:
        # #bdbdbd' was scored as body text and raised a false failure. Fixed 2026-09-21.
        _fg=re.search(r'(?:^|;)\s*color:\s*(#[0-9a-fA-F]{3,6})',_st)
        _bg=re.search(r'background-color:\s*(#[0-9a-fA-F]{3,6})',_st)
        if _fg and _bg:
            # WCAG AA is 4.5:1 for body text and 3:1 for large text, which is 18.66px
            # bold or 24px plain. A module banner is font-size:1.4em bold, so white on
            # the orange #E65100 header scores 3.79:1 and PASSES as large text. Standards
            # 3 records that colour as a Panorama false positive and says keep it; before
            # this correction the gate condemned it on four pages. Fixed 2026-09-21.
            _fs=re.search(r'font-size:\s*([\d.]+)\s*(em|px|rem)',_st)
            _px=None
            if _fs:
                _v=float(_fs.group(1))
                _px=_v*16 if _fs.group(2) in ('em','rem') else _v
            # Bold does NOT count. Canvas's editor strips font-weight out of an inline
            # style when the page is saved, so a pair that passed only because the text
            # was 18.66px BOLD fails the moment Adam edits the page in Canvas. Verified
            # 2026-09-21: four Major findings on the outline page, all of them white on
            # #E65100 at 1.25em, where the build had written font-weight:bold and the
            # saved page no longer had it. Large text here means 24px or more, full stop.
            _large=bool(_px and _px>=24)
            _need=3.0 if _large else 4.5
            _r=_ratio(_fg.group(1),_bg.group(1))
            if _r and _r<_need:
                _lowcontrast.append('%s %s on %s %.2f:1 (needs %.1f:1)'
                                    %(_p,_fg.group(1),_bg.group(1),_r,_need)); break

    if not _is_assign: continue
    if 'roll-call' in _p: continue          # the Roll Call stub is not a normal assignment
    # --- 7a / 11b, assignment pages only
    if ICONREF not in _t: _noicon.append(_p)
    if 'What to Submit' not in _t: _nosubmit.append(_p)
    if not re.search(r'\b\d+\s*points?\b',_txt,re.I): _nopoints.append(_p)
    if not re.search(r'Criterion|What earns full credit',_t): _norubric.append(_p)
    if re.search(r'Content and Resources|download .{0,40}Template|found in the module',_txt,re.I):
        _offpage.append(_p)

L('')
L('7a / 11b assignment page conformance, %d assignment pages'%len(_assign_pages))
if a and not _assign_pages: fails.append('7a: %d assignments resolved but no assignment body page found; the conformance checks saw nothing'%len(a))
for _lab,_lst in [('no DAPR icon reference',_noicon),('no What to Submit section',_nosubmit),
                  ('point value never stated',_nopoints),('no printed rubric table',_norubric),
                  ('sends the student off the page',_offpage)]:
    L('   %-34s %d'%(_lab,len(_lst)))
    for _x in _lst[:4]: L('      %s'%_x)
L('accessibility, all %d pages'%len(_pages))
for _lab,_lst in [('assignment page with 2+ <h2>',_multi_h2),('heading level skipped',_heading_skip),
                  ('page with no heading at all',_noheading),
                  ('bare alt=""',_emptyalt),('manually numbered <p> run',_numbered_p),
                  ('contrast under 4.5:1',_lowcontrast)]:
    L('   %-34s %d'%(_lab,len(_lst)))
    for _x in _lst[:4]: L('      %s'%_x)

if _noicon:      fails.append('assignments with no icons (7a): %d'%len(_noicon))
if _nosubmit:    fails.append('assignments with no What to Submit (7a): %d'%len(_nosubmit))
if _nopoints:    fails.append('assignments not stating points (11): %d'%len(_nopoints))
if _norubric:    fails.append('assignments with no printed rubric (11b-1): %d'%len(_norubric))
if _offpage:     fails.append('assignments sending the student off the page (11b): %d'%len(_offpage))
if _heading_skip: fails.append('heading level skipped (2): %d'%len(_heading_skip))
if _noheading:   fails.append('pages with no heading at all (2): %d'%len(_noheading))
if _emptyalt:    fails.append('bare alt="" (2): %d'%len(_emptyalt))
if _numbered_p:  fails.append('manually numbered paragraphs (2): %d'%len(_numbered_p))
if _lowcontrast: fails.append('contrast under 4.5:1 (2): %d'%len(_lowcontrast))
if _multi_h2:    fails.append('assignment pages with more than one h2 (7a): %d'%len(_multi_h2))


# ---------------------------------------------------------------- 11a quiz point tiers
# Adam 2026-09-20: a module quiz is 25 points. The Final is 100 (9.1a). macOS is
# larger by design and is allowed 50. Anything else is a retier, not a judgement call.
_QUIZ_EXEMPT = {'Final Exam': 100, 'Mac Navigation': 50}
_tier=[]
for _qm in sorted(glob.glob('quizzes/*_meta.xml')) or sorted(glob.glob('*/assessment_meta.xml')):
    _s2=open(_qm,encoding='utf-8',errors='ignore').read()
    _t2=re.search(r'<title>(.*?)</title>',_s2,re.S)
    _p2=re.search(r'<points_possible>([\d.]+)</points_possible>',_s2)
    if not _p2: continue
    _name=html.unescape(_t2.group(1)) if _t2 else os.path.basename(_qm)
    # Adam 2026-09-21: a Canvas practice quiz is ungraded by definition, so the 25 point
    # tier does not apply to it. It is still held to a rule: a practice quiz carries zero.
    # DAPR 2255's M0 Diagnostic Prior Knowledge Survey is the case that exposed this.
    if re.search(r'<quiz_type>\s*practice_quiz\s*</quiz_type>',_s2):
        if abs(float(_p2.group(1)))>0.01:
            _tier.append('%s: practice quiz carrying %g points, 11a wants 0'
                         %(_name[:52],float(_p2.group(1))))
        continue
    _want=25
    for _k,_v in _QUIZ_EXEMPT.items():
        if _k in _name: _want=_v
    if abs(float(_p2.group(1))-_want)>0.01:
        _tier.append('%s: %g points, 11a wants %d'%(_name[:52],float(_p2.group(1)),_want))
L('quizzes off the 11a point tier (must be 0): %d'%len(_tier))
for _x in _tier[:12]: L('    %s'%_x)
if _tier: fails.append('quizzes off the 11a point tier: %d'%len(_tier))


# ---------------------------------------------------------------- 12i tables (Standards 2, 11b-1)
# Adam, 2026-09-21: he imported the cartridge and Canvas's Accessibility Report filled the
# sidebar with the same two findings repeated down the whole page.
#     "Table does not have a header."   Severe
#     "Table does not have a caption."  Minor
# Standards 2 had already ruled on this and the build ignored it 64 times: layout tables are
# deprecated, role="presentation" does not exempt one, and icon-and-text rows, callouts,
# banners, totals and picture grids are divs. Standards 11b-1 adds that a caption is plain
# text with no style attribute. Nothing in the build was checking any of it, and 176 of the
# package's 217 tables had no caption at all. Six rules, each one proved by breaking it.
_t_noth=[]; _t_nocap=[]; _t_noscope=[]; _t_capstyle=[]; _t_pres=[]; _t_emul=[]
for _p in sorted(set(glob.glob('wiki_content/*.html')+glob.glob('*/*.html')+glob.glob('*.html'))-_INSTR):
    _t=open(_p,encoding='utf-8',errors='replace').read()
    if re.search(r'display:\s*table',_t): _t_emul.append(_p)
    for _tb in re.findall(r'<table\b.*?</table>',_t,re.S|re.I):
        _ths=re.findall(r'<th(?:\s[^>]*)?>',_tb,re.I)
        if not _ths: _t_noth.append(_p)
        elif any('scope=' not in _h for _h in _ths): _t_noscope.append(_p)
        if not re.search(r'<caption[^>]*>\s*\S',_tb,re.I): _t_nocap.append(_p)
        if re.search(r'<caption[^>]*\sstyle=',_tb,re.I): _t_capstyle.append(_p)
        if 'role="presentation"' in _tb.split('>',1)[0]: _t_pres.append(_p)
for _label,_hits,_why in [
        ('tables with no header cell',_t_noth,'tables with no header cell (12i)'),
        ('tables with no caption text',_t_nocap,'tables with no caption (12i)'),
        ('header cells with no scope',_t_noscope,'header cells with no scope (12i)'),
        ('captions carrying a style attribute',_t_capstyle,'styled captions (12i)'),
        ('layout tables, role="presentation"',_t_pres,'layout tables (12i)'),
        ('files emulating a table with display:table',_t_emul,'display:table emulation (12i)')]:
    L('%s (must be 0): %d'%(_label,len(_hits)))
    for _x in sorted(set(_hits))[:6]: L('    %s'%_x)
    if _hits: fails.append('%s: %d'%(_why,len(_hits)))


# ---------------------------------------------------------------- 2b inherited-background contrast
# Adam 2026-09-21: the 12i contrast check only compared a colour to a background declared
# in the SAME style attribute. 58 section headings styled color:#fbc02d with no background
# of their own, sitting on the wrapper's white, shipped at 1.66:1 and nothing saw them.
# 193 pairs failed in v71; the old check reported 29. This carries the nearest ancestor
# background down the tree, which is what a browser and a screen reader both do.
from html.parser import HTMLParser as _HP

def _lum(h):
    h=h.lstrip('#')
    if len(h)==3: h="".join(c*2 for c in h)
    f=lambda v:(lambda x: x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4)(int(v,16)/255.0)
    return 0.2126*f(h[0:2])+0.7152*f(h[2:4])+0.0722*f(h[4:6])

def _ratio(a,b):
    la,lb=_lum(a),_lum(b); hi,lo=max(la,lb),min(la,lb); return (hi+0.05)/(lo+0.05)

_BGRE=re.compile(r'(?<!-)background(?:-color)?:\s*(#[0-9a-fA-F]{3,8})')
_FGRE=re.compile(r'(?<![a-z-])color:\s*(#[0-9a-fA-F]{3,8})')
_VOID={'img','br','hr','input','meta','link','source'}

class _InkScan(_HP):
    def __init__(self):
        _HP.__init__(self, convert_charrefs=True)
        self.stack=['#ffffff']; self.bad=[]
    def handle_starttag(self, tag, attrs):
        st=dict(attrs).get('style','') or ''
        _b=_BGRE.search(st); _f=_FGRE.search(st)
        here=_b.group(1).lower() if _b else self.stack[-1]
        if _f and len(_f.group(1))==7:
            _ink=_f.group(1).lower()
            _r=_ratio(_ink,here)
            if _r<4.5: self.bad.append((_ink,here,round(_r,2)))
        if tag not in _VOID: self.stack.append(here)
    def handle_endtag(self, tag):
        if tag not in _VOID and len(self.stack)>1: self.stack.pop()

_ink_bad=[]
for _p in sorted(set(glob.glob('wiki_content/*.html')+glob.glob('*/*.html')+glob.glob('*.html'))-_INSTR):
    _sc=_InkScan()
    try: _sc.feed(open(_p,encoding='utf-8',errors='replace').read())
    except Exception: continue
    for _ink,_bg,_r in _sc.bad: _ink_bad.append((_p,_ink,_bg,_r))
L('text on its INHERITED background under 4.5:1 (2b, must be 0): %d'%len(_ink_bad))
_seen={}
for _p,_ink,_bg,_r in _ink_bad: _seen.setdefault((_ink,_bg,_r),[]).append(_p)
for (_ink,_bg,_r),_fs in sorted(_seen.items(), key=lambda x:-len(x[1]))[:8]:
    L('    %s on %s  %.2f:1  x%d   e.g. %s'%(_ink,_bg,_r,len(_fs),os.path.basename(_fs[0])))
if _ink_bad: fails.append('inherited-background contrast under 4.5:1 (2b): %d'%len(_ink_bad))

# 6b every module item resolves to a resource the manifest declares
# Added 2026-09-22. Rule 6 above checks the manifest's own organizations tree.
# Nothing checked module_meta, which is what Canvas actually builds the modules
# from. A module item whose identifierref names nothing imports as a missing
# item and its content disappears from the module without a word. A 25 point
# assignment shipped that way in v6, v7 and v8. Subheaders and external items
# carry no resource of their own and are exempt.
_mitems=re.findall(r'<item identifier="[^"]*">(.*?)</item>',mm,re.S)
_mdang=[]
for _b in _mitems:
    _r=re.search(r'<identifierref>\s*([^<\s]+)\s*</identifierref>',_b)
    if not _r: continue
    _c=re.search(r'<content_type>([^<]*)</content_type>',_b)
    _ct=_c.group(1) if _c else ''
    if _ct in ('ContextModuleSubHeader','ExternalUrl','ExternalTool'): continue
    _t=re.search(r'<title>([^<]*)</title>',_b)
    if _r.group(1) not in ids:
        _mdang.append(((_t.group(1) if _t else '(untitled)'),_r.group(1)))
L('module items: %d  pointing at an undeclared resource: %d'%(len(_mitems),len(_mdang)))
for _t,_r in _mdang[:8]: L('    %s -> %s'%(_t,_r))
if _mdang: fails.append('module items point at undeclared resources: %s'%[t for t,_ in _mdang][:5])

# 11b figure captions on a page run 1..n
# Added 2026-09-22. Captions were written from a global image brief, so a figure
# that was seventh in the brief was captioned "Figure 7." on a page holding one
# picture. Twenty one pages were wrong at once. The number a student reads has
# to match the page they are reading, not the order I generated things in.
_fignum=[]
for _p in sorted(set(glob.glob('wiki_content/*.html'))|set(glob.glob('*/*.html'))):
    try: _s=open(_p,encoding='utf-8',errors='replace').read()
    except Exception: continue
    _n=[int(_x) for _x in re.findall(r'Figure (\d+)\.',_s)]
    if _n and _n!=list(range(1,len(_n)+1)):
        _fignum.append((os.path.basename(_p),_n))
L('pages whose figure captions do not run 1..n (must be 0): %d'%len(_fignum))
for _n2,_v in _fignum[:8]: L('    %s %s'%(_n2,_v))
if _fignum: fails.append('figure captions out of sequence on %d pages'%len(_fignum))

# 11c alt text stays inside the Standards 2 cap of 120 characters
# Added 2026-09-22. Rule 11 already counted images with no alt at all. Nothing
# counted alt text that runs long, and eight tags were over at once, the worst
# at 235 characters. A screen reader reads the whole string before the caption.
_altlong=[]
for _p in sorted(set(glob.glob('wiki_content/*.html'))|set(glob.glob('*/*.html'))):
    try: _s=open(_p,encoding='utf-8',errors='replace').read()
    except Exception: continue
    for _a in re.findall(r'<img [^>]*alt="([^"]*)"',_s):
        if len(_a)>120: _altlong.append((os.path.basename(_p),len(_a)))
L('alt attributes over the 120 character cap (must be 0): %d'%len(_altlong))
for _n,_c in _altlong[:8]: L('    %s (%d chars)'%(_n,_c))
if _altlong: fails.append('alt text over the 120 character cap: %d'%len(_altlong))

# 0 an image on every page (Adam, 2026-09-24): every student visible page carries at
# least one real image. Icons, callout icons and logos do not count.
# Amended 2026-09-24 [Adam approved]. The logo filter matched only a path containing '/logo',
# so Instructor_Use_Only_(Hidden)/Uvu_Digital_Media_Logo.png counted as a real image and a
# syllabus carrying nothing but the department logo passed as illustrated. Test the FILE NAME:
# any name whose words include logo (Logo.png, Uvu_Digital_Media_Logo.png, logo-01.png).
# Also 2026-09-24: the Instructor Use Only - [Do Not Publish] module now ships in every
# cartridge (Standards 0). Its *No Publish pages are never student visible, so they are
# resolved from module_meta and exempted, rather than matched by a phrase in the body.
_islogo=lambda u: bool(re.search(r'(?:^|[_\-. ])logo(?:[_\-. ]|$)',os.path.basename(urllib.parse.unquote(u)).lower()))
_bare=[]
for _p in sorted(set(glob.glob('wiki_content/*.html'))|set(glob.glob('assignments/*.html'))|set(glob.glob('*/*.html'))):
    if '/' not in _p: continue
    try: _s=open(_p,encoding='utf-8',errors='replace').read()
    except Exception: continue
    if 'Do Not Publish' in _s or 'Instructor_Use_Only' in _p or _p in _INSTR: continue
    _imgs=[m for m in re.findall(r'<img [^>]*src="([^"]+)"',_s)
           if 'DAPR_Canvas_Icon_Reference' not in m and not _islogo(m)]
    if not _imgs: _bare.append(os.path.basename(_p))
L('pages with no real image (Standards 0, must be 0): %d'%len(_bare))
for _n in _bare[:12]: L('    %s'%_n)
if _bare: fails.append('pages with no real image: %d'%len(_bare))

# 20.5d a figure must not lose its labels to a newer generation
# Added 2026-09-22 after v9 moved 32 pages from -01 to -02 and 28 of them lost
# the labels that were the teaching content: axis names, OSI layer names,
# protocol names, the decisions in a decision tree. Standards 20.5 says ask for
# no text at all, which is right for a figure whose subject is a shape and wrong
# for one whose subject is its labels. Until 20.5 carries that distinction, the
# gate carries it.
_census=os.path.join('..','census.tsv')
_repo=os.environ.get('DAPR_REPO_IMAGES')
if _repo: _census=os.path.join(_repo,'_briefs','_review','ocr-label-census.tsv')
_chars={}
if os.path.exists(_census):
    for _ln in open(_census,encoding='utf-8',errors='replace'):
        _pt=_ln.rstrip('\n').split('\t')
        if len(_pt)==2 and _pt[1].strip().isdigit():
            _chars[os.path.basename(_pt[0])]=int(_pt[1].strip())
_used=set()
for _p in sorted(set(glob.glob('wiki_content/*.html'))|set(glob.glob('*/*.html'))):
    try: _s=open(_p,encoding='utf-8',errors='replace').read()
    except Exception: continue
    for _m in re.finditer(r'/Images/[a-z-]+/([A-Za-z0-9._-]+\.(?:png|jpe?g))',_s):
        _used.add(_m.group(1))
_lostlab=[]; _nocensus=[]
_FLOOR=10
for _f in sorted(_used):
    if _f not in _chars:
        if _f.endswith('.png'): _nocensus.append(_f)
        continue
    _mine=_chars[_f]
    if _mine>_FLOOR: continue
    _mm=re.match(r'^(.*)-(\d\d)\.(png|jpe?g)$',_f)
    if not _mm: continue
    _stem,_gen,_ext=_mm.group(1),int(_mm.group(2)),_mm.group(3)
    for _g in range(1,_gen):
        _sib='%s-%02d.%s'%(_stem,_g,_ext)
        _sc=_chars.get(_sib)
        if _sc is not None and _sc>_FLOOR:
            _lostlab.append((_f,_mine,_sib,_sc)); break
L('figures in use that lost labels to an older generation (must be 0): %d'%len(_lostlab))
for _a,_b,_c,_d in _lostlab[:8]:
    L('    %s (%d chars) replaced %s (%d chars)'%(_a,_b,_c,_d))
if _lostlab: fails.append('figures placed that lost their labels: %d'%len(_lostlab))
if not os.path.exists(_census):
    L('    note: no OCR label census found, rule 20.5d could not run')
    warns.append('no OCR label census; rule 20.5d did not run')
elif _nocensus:
    L('    note: %d figures in use are missing from the census'%len(_nocensus))
    warns.append('figures missing from the OCR label census: %d'%len(_nocensus))

L('')
# 9.3a-1 every scored key resolves (Adam, 2026-09-24; Standards 9.3a, Decisions 9)
#   A DAPR 2255 student chose the right answers on the Resistors quiz three times and was
#   marked wrong, because 8 of its 25 keys pointed at no answer (77 broken keys across 11
#   quizzes in the v58 export). Every scored multiple choice, multiple answers and
#   true/false item must key a response_label ident that exists IN THAT ITEM, and must
#   carry a 100 point condition. Checked in every QTI file the manifest resolves AND in
#   every non_cc_assessments copy, because the two copies drift independently.
_keyfails=[]
_qfiles=set(QTI_FILES)|set(glob.glob('non_cc_assessments/*.qti'))|set(glob.glob('non_cc_assessments/*.xml'))
_SCORED=('multiple_choice_question','multiple_answers_question','true_false_question')
for _qf in sorted(_qfiles):
    try: _qt=open(_qf,encoding='utf-8',errors='replace').read()
    except Exception: continue
    for _im in re.finditer(r'<item\b[^>]*\bident="([^"]+)"[^>]*>(.*?)</item>',_qt,re.S):
        _ib=_im.group(2)
        _ty=re.search(r'question_type</fieldlabel>\s*<fieldentry>([^<]+)',_ib)
        if not _ty or _ty.group(1).strip() not in _SCORED: continue
        _labels=set(re.findall(r'<response_label\b[^>]*\bident="([^"]+)"',_ib))
        _full=False
        for _rc in re.findall(r'<respcondition\b.*?</respcondition>',_ib,re.S):
            _sv=re.search(r'<setvar\b[^>]*>\s*([-\d.]+)\s*</setvar>',_rc)
            if not _sv or float(_sv.group(1))<=0: continue
            if float(_sv.group(1))>=100: _full=True
            for _k in re.findall(r'<varequal\b[^>]*>([^<]*)</varequal>',_rc):
                if _k.strip() not in _labels:
                    _keyfails.append('%s %s key %s is not an answer in that item'%(_qf,_im.group(1),_k.strip()))
        if not _full: _keyfails.append('%s %s has no 100 point key'%(_qf,_im.group(1)))
L('scored quiz items whose key does not resolve (9.3a, must be 0): %d'%len(_keyfails))
for _x in _keyfails[:8]: L('    %s'%_x)
if _keyfails: fails.append('quiz keys that do not resolve to an answer (9.3a): %d'%len(_keyfails))

# 9.3a-2 no history or naming questions (Adam, 2026-09-24). A stem that asks who, when,
#   which company, what something is named after or what an acronym stands for fails the
#   build. A year is 1800 to 2029 NOT followed by a unit, so "2000 Hz" and "1130 ft" pass.
#   STEM_OVERRIDES holds stems Adam has approved; add the stem text (any unique substring),
#   with his name and the date in a comment, and that one question passes.
STEM_OVERRIDES=[
]
_HIST=re.compile(r"\binvent(?:s|ed|ion|or|ing)?\b|\bnamed (?:after|for)\b|\bname is the origin\b|\borigin of the name\b"
                 r"|\bwho (?:invented|is credited|was credited|developed|created|founded|designed|coined)\b|\bcredited with\b"
                 r"|\b(?:in )?(?:what|which) year\b|\bwhich compan(?:y|ies)\b|\bwhich organi[sz]ation\b|\bstands? for\b|\bacronym\b"
                 r"|\b(?:18\d\d|19\d\d|20[0-2]\d)\b(?!\s*(?:k?Hz|Hertz|ms|seconds?|s\b|ohms?|Ω|&#937;|[kKmM]?W\b|watts?|V\b|volts?|dB|samples?|points?|pts|feet|foot|ft|inch|in\b|m\b|meters?|%|x\b|times|bits?|MB|GB|kbps|BPM|RPM|cycles?|degrees|°|&#176;)|[,.]\d)", re.I)
_histfails=[]
for _qf in sorted(_qfiles):
    try: _qt=open(_qf,encoding='utf-8',errors='replace').read()
    except Exception: continue
    for _im in re.finditer(r'<item\b[^>]*\bident="([^"]+)"[^>]*>(.*?)</item>',_qt,re.S):
        _st=re.search(r'<presentation>\s*<material>\s*<mattext[^>]*>(.*?)</mattext>',_im.group(2),re.S)
        if not _st: continue
        _stem=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',html.unescape(_st.group(1))))).strip()
        _hm=_HIST.search(_stem)
        if _hm and not any(_o in _stem for _o in STEM_OVERRIDES):
            _histfails.append('%s %s "%s" in: %s'%(_qf,_im.group(1),_hm.group(0),_stem[:90]))
L('question stems asking history or naming (9.3a, must be 0): %d'%len(_histfails))
for _x in _histfails[:8]: L('    %s'%_x)
if _histfails: fails.append('history or naming question stems (9.3a): %d'%len(_histfails))
L('RESULT: %s | hard fails: %s | warnings: %s'%('PASS' if not fails else 'FAIL',fails,warns))
sys.exit(1 if fails else 0)
