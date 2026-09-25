import sys,os,re,json,hashlib; sys.path.insert(0,'/sessions/rcw-01hebs46qpebfpjpevcv8dyi')
from liveinv import *
EP=open('exportpath').read().strip(); R='b40live'
E=inventory(EP); V=inventory(R)
M={}; log={'title_matches':[],'item_remaps':[]}
# 1. title matches (content confirmed)
M['g9794dbd'+[i for i in V['page'] if i.startswith('g9794dbd')][0][8:]]='gc7fb61afd148b137388384fd0da9f2f1'
log['title_matches'].append(['page','macOS: P4: RAM, Storage, and CPUs','RAM, Storage, and CPU','gc7fb61afd148b137388384fd0da9f2f1'])
M['g1ead896269fc0bacc0326f07ea9048a6']='g272d911ba3cb644cac942e316111b87e'
M['b8b96ef18b3fdc31b3ab752e43c5425c']='5117821d205c19efa69675ccf4318c38'
log['title_matches'].append(['quiz','macOS: Quiz - Mac Navigation','Core Mixing Mac Navigation Quiz','g272d911ba3cb644cac942e316111b87e'])
M['g22579e84de216ce0d0a5a687fb15b0cd']='gd9c81dfaf44a4dbbd196ff616f05fc68'
log['title_matches'].append(['module','Effects: Frequency Dynamics & Side-Chains','Module 10: Frequency, Dynamics and Side-chains (was matched to Module 10: Dynamics and Side-chain Lab)','gd9c81dfaf44a4dbbd196ff616f05fc68'])
# 2. module items: live id only when same module and same content
ref=lambda r: M.get(r,r)
eidx={}
for i,x in E['item'].items():
    eidx[(x['module'],x['ref']) if x['ref'] else (x['module'],'SUB:'+x['title'])]=i
used=set()
for i,x in V['item'].items():
    mod=M.get(x['module'],x['module']); key=(mod,ref(x['ref'])) if x['ref'] else (mod,'SUB:'+x['title'])
    if key in eidx and eidx[key] not in used:
        new=eidx[key]
    elif i in E['item']:
        new='g'+hashlib.md5(('dapr2020-v40-live-item-'+i).encode()).hexdigest()
    else: new=i
    used.add(new)
    if new!=i: M[i]=new; log['item_remaps'].append([V['module'][x['module']]['title'],x['title'],i,new,'live' if new in E['item'] else 'fresh'])
# check no new id collides with an unchanged id
allv=set().union(*[set(V[k]) for k in V])
final=[M.get(i,i) for i in allv]
assert len(final)==len(set(final)),'collision'
pat=re.compile('|'.join(map(re.escape,sorted(M,key=len,reverse=True))))
n=0
for r,d,f in os.walk(R):
    for x in f:
        if x.endswith(('.xml','.html','.qti','.txt')):
            p=os.path.join(r,x); s=open(p,encoding='utf-8').read(); t=pat.sub(lambda m:M[m.group(0)],s)
            if t!=s: open(p,'w',encoding='utf-8').write(t); n+=1
# rename paths
for old,new in M.items():
    for a,b in [(f'{R}/{old}',f'{R}/{new}'),(f'{R}/non_cc_assessments/{old}.xml.qti',f'{R}/non_cc_assessments/{new}.xml.qti')]:
        if os.path.exists(a): os.rename(a,b); print('renamed',a,'->',b)
log['files_changed']=n; log['map_size']=len(M)
json.dump(log,open('v40live_log.json','w'),indent=1)
print('files changed',n,'map',len(M),'items remapped',len(log['item_remaps']),'to live',sum(1 for x in log['item_remaps'] if x[4]=='live'),'fresh',sum(1 for x in log['item_remaps'] if x[4]=='fresh'))
