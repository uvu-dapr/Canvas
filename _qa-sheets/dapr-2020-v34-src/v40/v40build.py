import re,os,html,json,hashlib,glob
B=os.path.expanduser('~/b40'); os.chdir(B)
S=os.path.expanduser('~/mnt/_qa-sheets/dapr-2020-v34-src')
def rd(p): return open(p,encoding='utf-8').read()
def wr(p,s): open(p,'w',encoding='utf-8').write(s)
H=lambda s: hashlib.md5(s.encode()).hexdigest()
man=rd('imsmanifest.xml'); mm=rd('course_settings/module_meta.xml'); log={'weblinks':[],'assign':[],'pages':[],'quizzes':[],'overview':[]}
esc=lambda t: html.escape(t,quote=False)
def modblock(title):
    for b in re.split(r'(?=  <module identifier=)',mm):
        m=re.search(r'<title>([^<]*)</title>',b)
        if b.strip().startswith('<module') and m and html.unescape(m.group(1))==title: return b
    raise KeyError(title)
def items_of(b): return re.findall(r'[ \t]*<item identifier="[^"]+">.*?</item>\n?',b,re.S)
def renumber(b):
    n=[0]
    def rp(m): n[0]+=1; return '<position>%d</position>'%n[0]
    i=b.find('<items>'); return b[:i]+re.sub(r'<position>\d+</position>',rp,b[i:])
def mkitem(iid,ctype,title,ref):
    return '''      <item identifier="%s">
        <content_type>%s</content_type>
        <workflow_state>active</workflow_state>
        <title>%s</title>
        <identifierref>%s</identifierref>
        <position>0</position>
        <new_tab>false</new_tab>
        <indent>0</indent>
        <link_settings_json>null</link_settings_json>
      </item>
'''%(iid,ctype,esc(title),ref)
def add_res(res):
    global man
    i=man.find('</resources>'); ls=man.rfind('\n',0,i)+1; man=man[:ls]+res+man[ls:]
def org_insert_after(ref_after_itemid,newid,newref,title,anchor_ref=None):
    global man
    p=man.find('<item identifier="%s"'%ref_after_itemid)
    if p<0 and anchor_ref: p=man.find('identifierref="%s"'%anchor_ref); p=man.rfind('<item ',0,p)
    assert p>0,ref_after_itemid
    e=man.find('</item>',p)+len('</item>')
    man=man[:e]+'<item identifier="%s" identifierref="%s"><title>%s</title></item>'%(newid,newref,esc(title))+man[e:]
# ---------- A. §12a: remove chapter web links
for f in sorted(glob.glob('web_links/*.xml')):
    s=rd(f)
    if 'cambridge-mt.com/ms/ch' not in s: continue
    rid=os.path.basename(f)[:-4]; url=re.search(r'<url>([^<]*)</url>',s) or re.search(r'href="([^"]+)"',s)
    it=re.search(r'[ \t]*<item identifier="([^"]+)">\s*<content_type>ExternalUrl</content_type>\s*<workflow_state>[^<]*</workflow_state>\s*<title>([^<]*)</title>\s*<identifierref>%s</identifierref>.*?</item>\n?'%rid,mm,re.S)
    modt=None
    for b in re.split(r'(?=  <module identifier=)',mm):
        if it and it.group(0) in b: modt=html.unescape(re.search(r'<title>([^<]*)</title>',b).group(1))
    if it: mm=mm.replace(it.group(0),'',1)
    blk=re.search(r'\n?[ \t]*<resource identifier="%s"[^>]*>.*?</resource>'%rid,man,re.S); man=man.replace(blk.group(0),'',1)
    oi=re.search(r'<item identifier="[^"]+" identifierref="%s">\s*<title>[^<]*</title>\s*</item>'%rid,man)
    if oi: man=man.replace(oi.group(0),'',1)
    os.remove(f)
    log['weblinks'].append(dict(module=modt,link_text=html.unescape(html.unescape(it.group(2))) if it else '',url=url.group(1) if url else '',replaced_by='nothing (module item removed); the module reading pages are already in the module'))
# ---------- B. new pages
FOLDER={'tuning':('Mixing: Tuning','Mixing__Tuning'),'fds':('Effects: Frequency Dynamics & Side-Chains','Effects__Frequency_Dynamics_and_Side-Chains'),'masterbuss':('Mixing: Master-Buss Processing & Endgame','Mixing__Master-Buss_Processing_and_Endgame')}
OUT={k:json.load(open(f'{S}/v40/out_{k}.json')) for k in FOLDER}
newpages={}
for k,(modt,folder) in FOLDER.items():
    b=modblock(modt); its=items_of(b)
    wiki=[x for x in its if '<content_type>WikiPage</content_type>' in x and 'Module Overview' not in x and 'Distortion:' not in x]
    anchor=wiki[-1]; nb=b; after_org=re.search(r'<item identifier="([^"]+)"',anchor).group(1); aref=re.search(r'<identifierref>([^<]+)<',anchor).group(1)
    ins=''
    for p in OUT[k]['pages']:
        pid='g'+H('dapr2020-v40-page-'+p['slug']); iid='g'+H('dapr2020-v40-item-'+p['slug'])
        fn=f"wiki_content/{p['slug']}.html"; assert not os.path.exists(fn),fn
        wr(fn,'<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n<title>%s</title>\n<meta name="identifier" content="%s">\n<meta name="editing_roles" content="teachers">\n<meta name="workflow_state" content="unpublished">\n</head>\n<body>\n%s\n</body>\n</html>\n'%(esc(p['title']),pid,p['body_html'].strip()))
        add_res('    <resource identifier="%s" type="webcontent" href="%s">\n      <file href="%s"/>\n    </resource>\n'%(pid,fn,fn))
        ins+=mkitem(iid,'WikiPage',p['title'],pid)
        org_insert_after(after_org,iid,pid,p['title'],aref); after_org=iid; aref=pid
        newpages.setdefault(k,[]).append((p['title'],p['slug'],pid))
        log['pages'].append(dict(module=modt,title=p['title'],file=fn,figures=p['figures']))
    a=anchor if anchor.endswith('\n') else anchor+'\n'
    nb=b.replace(anchor,a+ins,1); nb=renumber(nb); mm=mm.replace(b,nb,1)
# ---------- C. new quizzes (clone of the Calibration quiz shell)
SRC='gcbd71ca2a6134135adc0099a4ecff8c6'; SRCT='Monitoring: Quiz - Calibration &amp; Monitoring'
QZ={'tuning':('Mixing: Quiz - Tuning','2026-10-05T06:00:00Z','2026-10-23T15:00:00Z'),
    'fds':('Effects: Quiz - Frequency Dynamics &amp; Side-Chains','2026-10-26T06:00:00Z','2026-11-06T16:00:00Z'),
    'masterbuss':('Mixing: Quiz - Master-Buss Processing &amp; Endgame','2026-11-16T07:00:00Z','2026-12-04T16:00:00Z')}
srcmeta=rd(f'{SRC}/assessment_meta.xml'); srcaid=re.search(r'<assignment identifier="([^"]+)"',srcmeta).group(1)
def qitem(q,cc,tag):
    ident=tag+H(q['stem'])[:22]
    ids=[str(10000+int(H(q['stem']+o)[:6],16)%89999) for o in q['options']]; assert len(set(ids))==len(ids)
    typ=q['type']; card='Multiple' if typ=='multiple_answers_question' else 'Single'
    lab='<fieldlabel>cc_profile</fieldlabel>\n              <fieldentry>cc.multiple_choice.v0p1</fieldentry>' if cc else '<fieldlabel>question_type</fieldlabel>\n              <fieldentry>%s</fieldentry>'%typ
    labels=''.join('\n              <response_label ident="%s">\n                <material>\n                  <mattext texttype="text/plain">%s</mattext>\n                </material>\n              </response_label>'%(a,esc(o)) for a,o in zip(ids,q['options']))
    keyids=[a for a,o in zip(ids,q['options']) if o in q['key']]; assert keyids
    if typ=='multiple_answers_question':
        cond='<and>\n'+''.join('                <varequal respident="response1">%s</varequal>\n'%a for a in keyids)+''.join('                <not>\n                  <varequal respident="response1">%s</varequal>\n                </not>\n'%a for a in ids if a not in keyids)+'              </and>'
    else: cond='<varequal respident="response1">%s</varequal>'%keyids[0]
    return '''<item ident="%s" title="Question">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              %s
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1</fieldentry>
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
          <response_lid ident="response1" rcardinality="%s">
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
              %s
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>
'''%(ident,lab,','.join(ids),esc('<p>%s</p>'%esc(q['stem'])),card,labels,cond)
newquiz={}
for k,(QT,unl,due) in QZ.items():
    qs=OUT[k]['quiz']['questions']; assert len(qs)==25,(k,len(qs))
    qid='g'+H('dapr2020-v40-quiz-'+k); aid=H('dapr2020-v40-quiz-assign-'+k); mid='i'+H('dapr2020-v40-quiz-meta-'+k)
    os.makedirs(qid)
    meta=srcmeta.replace(SRC,qid).replace(SRCT,QT).replace(srcaid,aid)
    meta=meta.replace('2026-09-28T06:00:00Z',unl).replace('2026-10-09T15:00:00Z',due)
    assert meta.count(unl)==2 and meta.count(due)==2,k
    wr(f'{qid}/assessment_meta.xml',meta)
    for cc in (True,False):
        t=rd(f'{SRC}/assessment_qti.xml' if cc else f'non_cc_assessments/{SRC}.xml.qti')
        head=t[:t.find('<section ident="root_section">')+len('<section ident="root_section">')].replace(SRC,qid).replace(SRCT,QT)
        body=head+'\n'+''.join(qitem(q,cc,'v40'+k[:3]) for q in qs)+'      </section>\n  </assessment>\n</questestinterop>\n'
        wr(f'{qid}/assessment_qti.xml' if cc else f'non_cc_assessments/{qid}.xml.qti',body)
    add_res('''    <resource identifier="%s" type="imsqti_xmlv1p2/imscc_xmlv1p1/assessment">
      <file href="%s/assessment_qti.xml"/>
      <dependency identifierref="%s"/>
    </resource>
    <resource identifier="%s" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="%s/assessment_meta.xml">
      <file href="%s/assessment_meta.xml"/>
      <file href="non_cc_assessments/%s.xml.qti"/>
    </resource>
'''%(qid,qid,mid,mid,qid,qid,qid))
    modt=FOLDER[k][0]; b=modblock(modt); its=items_of(b)
    asg=[x for x in its if '<content_type>Assignment</content_type>' in x or 'Quizzes::Quiz' in x]
    anchor=asg[-1]; iid='g'+H('dapr2020-v40-quiz-item-'+k)
    nb=b.replace(anchor,(anchor if anchor.endswith('\n') else anchor+'\n')+mkitem(iid,'Quizzes::Quiz',html.unescape(QT),qid),1)
    mm=mm.replace(b,renumber(nb),1)
    org_insert_after(re.search(r'<item identifier="([^"]+)"',anchor).group(1),iid,qid,html.unescape(QT),re.search(r'<identifierref>([^<]+)<',anchor).group(1))
    newquiz[k]=(html.unescape(QT),qid); log['quizzes'].append(dict(quiz=html.unescape(QT),id=qid,opens=unl,due=due,questions=25))
newquiz['monitoring']=('Monitoring: Quiz - Calibration & Monitoring',SRC)
# ---------- D. overview pages: new reading pages into Before Class, new quizzes into Conclusion
OV={'tuning':'mixing-tuning-overview.html','fds':'effects-frequency-dynamics-side-chains-overview.html','masterbuss':'mixing-master-buss-processing-endgame-overview.html','monitoring':'monitoring-calibration-monitoring-overview.html'}
for k,f in OV.items():
    p='wiki_content/'+f; s=rd(p)
    bc=s.find('>Before Class</h2>'); ul_end=s.find('</ul>',bc)
    add=''.join('<li><a title="%s" href="$WIKI_REFERENCE$/pages/%s">%s</a></li>\n'%(html.escape(t),sl,esc(t)) for t,sl,_ in newpages.get(k,[]))
    s=s[:ul_end]+add+s[ul_end:]
    cc=s.find('>Conclusion</h2>'); ul_end=s.find('</ul>',cc)
    t,q=newquiz[k]
    s=s[:ul_end]+'<li><a title="%s" href="$CANVAS_OBJECT_REFERENCE$/quizzes/%s">%s</a></li>\n'%(html.escape(t),q,esc(t))+s[ul_end:]
    wr(p,s); log['overview'].append(dict(page=f,added_reading=[t for t,_,_ in newpages.get(k,[])],added_quiz=t))
# ---------- E. assignments: chapter references to the module's own pages
def module_of_ref(ref):
    for b in re.split(r'(?=  <module identifier=)',mm):
        if '<identifierref>%s</identifierref>'%ref in b: return b
def reading_titles(b):
    r=[]
    for ct,t in re.findall(r'<content_type>([^<]*)</content_type>\s*<workflow_state>[^<]*</workflow_state>\s*<title>([^<]*)</title>',b):
        t=html.unescape(html.unescape(t))
        if ct=='WikiPage' and 'Module Overview' not in t: r.append(t)
    return r
NOTE='<img src="https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/Callout_Note.png" alt="Note" width="44" height="44" style="vertical-align:middle; margin-right:10px;">'
for f in sorted(glob.glob('*/assignment_settings.xml')):
    d=os.path.dirname(f); h=[x for x in glob.glob(d+'/*.html')][0]; s=rd(h); o=s
    if 'cambridge-mt.com/ms/ch' not in s: continue
    b=module_of_ref(d); rt=reading_titles(b); pg=[t for t in rt if 'Procedure' in t] or rt[:1]
    ch=[]
    def cb(m):
        blk=m.group(0)
        if 'ms/ch' not in blk: return blk
        titles=re.findall(r'>(Chapter [^<]+|the reading for this module[^<]*)</a>',blk)
        ch.append(dict(where='readings callout',before=[html.unescape(x) for x in titles],after=rt))
        newlist='<ul style="margin:0; padding-left:20px;">\n'+''.join('<li style="margin-bottom:6px;">%s</li>\n'%esc(t) for t in rt)+'</ul>'
        blk2=re.sub(r'<img[^>]*Action_External_Link[^>]*>',NOTE,blk)
        blk2=re.sub(r'<strong style="vertical-align:middle;">[^<]*</strong>','<strong style="vertical-align:middle;">Read these pages in this module first</strong>',blk2,1)
        inner_start=blk2.find('<div style="margin-left:54px; margin-top:4px;">')+len('<div style="margin-left:54px; margin-top:4px;">')
        inner_end=blk2.rfind('</div>',0,blk2.rfind('</div>'))
        return blk2[:inner_start]+'\n'+newlist+'\n'+blk2[inner_end:]
    s=re.sub(r'<div style="background-color:#e3f2fd;[^"]*"><img[^>]*Action_External_Link[^>]*>.*?</div>\s*</div>',cb,s,flags=re.S)
    def wt(m):
        ch.append(dict(where='step',before=html.unescape(re.sub(r'<[^>]+>','',m.group(0))),after='Work through %s ...'%pg[0]))
        return 'Work through %s with the session open'%esc(pg[0])
    s=re.sub(r'Work through <a[^>]*ms/ch[^>]*>[^<]*</a>(?: and <a[^>]*ms/ch[^>]*>[^<]*</a>)? with the session open',wt,s)
    for a,bb in [('Apply all of the techniques demonstrated to your own mix.','Apply the techniques from this module&#39;s reading pages to your own mix.'),
                 ('Work out why he uses that setting','Work out why the reading calls for that setting'),
                 ('the way the one in the videos does','the way some compressors do'),
                 ('>The required video<','>The required reading<'),
                 ('Work through the required video and apply the techniques it demonstrates to your mix. Match every track and plugin adjustment to the settings shown in the tutorial.','Work through the required reading and apply its techniques to your mix. Make every track and plugin adjustment for a reason you can name from the reading.')]:
        if a in s: s=s.replace(a,bb); ch.append(dict(where='text',before=html.unescape(a.strip('<>')),after=html.unescape(bb.strip('<>'))))
    assert 'cambridge-mt.com/ms/ch' not in s,(h,re.findall(r'.{80}ms/ch.{40}',s))
    wr(h,s); log['assign'].append(dict(assignment=html.unescape(re.search(r'<title>([^<]*)',rd(f)).group(1)),file=h,changes=ch))
wr('imsmanifest.xml',man); wr('course_settings/module_meta.xml',mm)
json.dump(log,open(os.path.expanduser('~/v40_log.json'),'w'),indent=1)
print(json.dumps({k:len(v) for k,v in log.items()}))
