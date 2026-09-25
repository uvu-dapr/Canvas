import re,os,html,glob
def T(s): return html.unescape(html.unescape(s)).strip()
def inventory(root):
    man=open(root+'/imsmanifest.xml').read()
    o={}
    def add(kind,i,title,extra=None): o.setdefault(kind,{})[i]=dict(title=title,**(extra or {}))
    for m in re.finditer(r'<resource identifier="([^"]+)" type="([^"]+)"(?: href="([^"]*)")?[^>]*>(.*?)</resource>',man,re.S):
        rid,typ,href,body=m.groups(); href=href or ''
        files=re.findall(r'<file href="([^"]+)"',body)
        p=lambda f: os.path.join(root,f)
        if typ=='webcontent' and href.startswith('wiki_content/') and href.endswith('.html') and os.path.exists(p(href)):
            s=open(p(href),errors='ignore').read(); t=re.search(r'<title>([^<]*)',s); add('page',rid,T(t.group(1)) if t else '')
        elif typ=='associatedcontent/imscc_xmlv1p1/learning-application-resource':
            sf=[f for f in files if f.endswith('assignment_settings.xml') or (f.startswith('assignments/') and f.endswith('.xml'))]
            if sf and os.path.exists(p(sf[0])):
                s=open(p(sf[0])).read(); add('assignment',rid,T(re.search(r'<title>([^<]*)',s).group(1)))
        elif typ=='imsqti_xmlv1p2/imscc_xmlv1p1/assessment':
            d=[f for f in files][0].split('/')[0]; mf=p(d+'/assessment_meta.xml')
            if os.path.exists(mf):
                s=open(mf).read(); a=re.search(r'<assignment identifier="([^"]+)"',s)
                add('quiz',rid,T(re.search(r'<title>([^<]*)',s).group(1)),dict(assign=a.group(1) if a else None))
        elif typ=='imsdt_xmlv1p1':
            f=p(files[0]) if files else p(href)
            s=open(f).read(); add('discussion',rid,T(re.search(r'<title>([^<]*)',s).group(1)))
        elif typ=='imswl_xmlv1p1':
            f=p(files[0]) if files else p(href)
            s=open(f).read(); u=re.search(r'href="([^"]+)"',s); add('weblink',rid,T(re.search(r'<title>([^<]*)',s).group(1)),dict(url=u.group(1) if u else ''))
    mm=open(root+'/course_settings/module_meta.xml').read()
    for b in re.split(r'(?=<module identifier=)',mm)[1:]:
        mid=re.search(r'identifier="([^"]+)"',b).group(1); add('module',mid,T(re.search(r'<title>([^<]*)',b).group(1)))
        for iid,body in re.findall(r'<item identifier="([^"]+)">(.*?)</item>',b,re.S):
            ref=re.search(r'<identifierref>([^<]*)<',body)
            add('item',iid,T(re.search(r'<title>([^<]*)',body).group(1)),dict(module=mid,ref=ref.group(1) if ref else None,type=re.search(r'<content_type>([^<]*)',body).group(1)))
    ag=open(root+'/course_settings/assignment_groups.xml').read()
    for gid,t in re.findall(r'<assignmentGroup identifier="([^"]+)">\s*<title>([^<]*)',ag): add('group',gid,T(t))
    if os.path.exists(root+'/course_settings/rubrics.xml'):
        rb=open(root+'/course_settings/rubrics.xml').read()
        for rid,t in re.findall(r'<rubric identifier="([^"]+)">\s*<title>([^<]*)',rb): add('rubric',rid,T(t))
    return o
def norm(t):
    t=t.lower().replace('&','and')
    t=re.sub(r'^(module|week|m)\s*_?\d+\s*[:_\-]\s*','',t)
    t=re.sub(r'^quiz\s*_?\d+\s*[:_\-]\s*','quiz ',t)
    t=re.sub(r'\(classic\)','',t)
    return re.sub(r'[^a-z0-9]+',' ',t).strip()
