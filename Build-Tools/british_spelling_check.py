# -*- coding: utf-8 -*-
import re,sys,os,html
PAIRS=[
 # (british regex, american replacement shown for reporting)
 (r'\bcentre(s|d)?\b','center'),(r'\bmetre(s)?\b','meter'),(r'\blitre(s)?\b','liter'),
 (r'\bfibre(s)?\b','fiber'),(r'\btheatre(s)?\b','theater'),(r'\bcalibre\b','caliber'),
 (r'\bsombre\b','somber'),(r'\bspectre\b','specter'),
 (r'\bcolour','color'),
 (r'\bbehaviour','behavior'),(r'\bfavour','favor'),(r'\bflavour','flavor'),
 (r'\bhonour','honor'),(r'\blabour','labor'),(r'\bneighbour','neighbor'),
 (r'\bharbour','harbor'),(r'\brumour','rumor'),(r'\bendeavour','endeavor'),
 (r'\bsaviour','savior'),(r'\bvapour','vapor'),(r'\bodour','odor'),(r'\barmour','armor'),
 (r'\bhumour','humor'),(r'\bparlour','parlor'),(r'\bsplendour','splendor'),
 (r'\borganis(e|ed|es|ing|ation)','organiz'),(r'\brecognis(e|ed|es|ing)','recogniz'),
 (r'\bapologis(e|ed|es|ing)','apologiz'),(r'\banalys(e|ed|es|ing)\b','analyz'),
 (r'\bcategoris(e|ed|es|ing)','categoriz'),(r'\bcharacteris(e|ed|es|ing)','characteriz'),
 (r'\bcustomis(e|ed|es|ing)','customiz'),(r'\bemphasis(e|ed|es|ing)\b','emphasiz'),
 (r'\bequalis(e|ed|es|ing|ation|er)','equaliz'),(r'\bharmonis(e|ed|es|ing)','harmoniz'),
 (r'\bmaximis(e|ed|es|ing|ation|er)','maximiz'),(r'\bminimis(e|ed|es|ing)','minimiz'),
 (r'\bnormalis(e|ed|es|ing|ation)','normaliz'),(r'\boptimis(e|ed|es|ing|ation)','optimiz'),
 (r'\bprioritis(e|ed|es|ing)','prioritiz'),(r'\brealis(e|ed|es|ing)','realiz'),
 (r'\bstandardis(e|ed|es|ing|ation)','standardiz'),(r'\bsummaris(e|ed|es|ing)','summariz'),
 (r'\bsynthesis(e|ed|es|ing|er)\b','synthesiz'),(r'\butilis(e|ed|es|ing)','utiliz'),
 (r'\bvisualis(e|ed|es|ing|ation)','visualiz'),(r'\bspecialis(e|ed|es|ing)\b','specializ'),
 (r'\bstabilis(e|ed|es|ing)','stabiliz'),(r'\bdigitis(e|ed|es|ing)','digitiz'),
 (r'\bdefence','defense'),(r'\boffence','offense'),(r'\bpretence','pretense'),
 (r'\blicence','license'),(r'\bpractis(e|ed|es|ing)','practice'),
 (r'\bcancell(ed|ing)','cancel'),(r'\btravell(ed|ing|er)','travel'),
 (r'\bmodell(ed|ing)','model'),(r'\blabell(ed|ing)','label'),(r'\bsignall(ed|ing)','signal'),
 (r'\bfuelled\b','fueled'),(r'\bmarvellous\b','marvelous'),(r'\bskilful\b','skillful'),
 (r'\benrol\b','enroll'),(r'\bfulfil\b','fulfill'),(r'\binstalment','installment'),
 (r'\bprogramme(s|d)?\b','program'),(r'\bcatalogue(s|d)?\b','catalog'),(r'\bdialogue box','dialog box'),
 (r'\banalogue(s)?\b','analog'),(r'\bmonologue\b','monolog'),
 (r'\bgrey\b','gray'),(r'\bgreyscale\b','grayscale'),(r'\bstorey(s)?\b','story'),
 (r'\bplough','plow'),(r'\bmoustache','mustache'),(r'\baeroplane','airplane'),
 (r'\baluminium','aluminum'),(r'\bsulphur','sulfur'),
 (r'\bjudgement','judgment'),(r'\backnowledgement','acknowledgment'),
 (r'\bwhilst\b','while'),(r'\bamongst\b','among'),(r'\btowards the\b','toward the'),
 (r'\bspeciality','specialty'),(r'\bmanoeuvre','maneuver'),(r'\bdefences','defenses'),
 (r'\bencyclopaedia','encyclopedia'),(r'\bmediaeval','medieval'),
 (r'\bcheque\b','check'),(r'\btyre(s)?\b','tire'),(r'\bkerb\b','curb'),
 (r'\bbuss(es|ed|ing)?\b','bus'),
]
# Words that are correct where they appear: exact titles of published works cited in
# APA references. Add only with the citation that justifies it.
ALLOW=['Sulphur-rich volcanic eruptions and stratospheric aerosols',
       # Audient document titles, DAPR 2010 resources page. Audient plc, ASP4816-HE
       # documentation set, filenames as published: 'Connector Panel Visualisation.pdf'
       # and 'ASP4816-HE Visualisation.pdf'.
       'Connector Panel Visualisation',
       'ASP4816-HE Visualisation']

def scan(paths):
    hits=[]
    for p in paths:
        try: x=open(p,encoding='utf-8',errors='ignore').read()
        except Exception: continue
        # ignore url/attribute values and hex colors
        t=re.sub(r'(src|href)="[^"]*"','',x)
        for a in ALLOW: t=t.replace(a,'')
        for rx,amer in PAIRS:
            for m in re.finditer(rx,t,re.I):
                ctx=re.sub(r'\s+',' ',t[max(0,m.start()-70):m.end()+70])
                hits.append((p,m.group(0),amer,ctx))
    return hits
if __name__=='__main__':
    import glob
    roots=sys.argv[1:]
    paths=[]
    for r in roots:
        if os.path.isfile(r): paths.append(r)
        else:
            for dp,dn,fn in os.walk(r):
                for f in fn:
                    if f.lower().endswith(('.html','.xml','.md','.txt','.csv')):
                        paths.append(os.path.join(dp,f))
    hits=scan(paths)
    print('scanned %d files, %d hits'%(len(paths),len(hits)))
    for p,w,a,c in hits:
        print('\n%-70s  %-16s -> %s\n    ...%s...'%(p[-70:],w,a,c))
