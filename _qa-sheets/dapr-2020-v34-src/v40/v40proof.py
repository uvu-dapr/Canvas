import sys,json; sys.path.insert(0,'/sessions/rcw-01hebs46qpebfpjpevcv8dyi')
from liveinv import *
EP=open('exportpath').read().strip()
E=inventory(EP); L=inventory('v40livecheck')
out={}
for k in ['module','page','assignment','quiz','discussion','weblink','group','item']:
    e=E.get(k,{}); l=L.get(k,{})
    carry=[i for i in l if i in e]
    if k=='item':
        ok=[i for i in carry if e[i]['module']==l[i]['module'] and e[i]['ref']==l[i]['ref']]
        wrong=[i for i in carry if i not in ok]
    else: ok=carry; wrong=[]
    out[k]=dict(live_total=len(e),cart_total=len(l),carry=len(ok),wrong=len(wrong),
        rows=[[l[i]['title'],e[i]['title'],i] for i in ok] if k!='item' else [],
        new=[[l[i]['title'],i] for i in l if i not in e],
        gone=[[e[i]['title'],i]+([E['module'][e[i]['module']]['title'],e[i]['type']] if k=='item' else []) for i in e if i not in l])
    print(k,'live',len(e),'cart',len(l),'carry live id',len(ok),'id reused wrongly',len(wrong),'new',len(out[k]['new']),'live-only',len(out[k]['gone']))
# quiz assignment ids
for i,q in L['quiz'].items():
    if i in E['quiz']: print('  quiz assign id', q['title'][:35], 'same' if q['assign']==E['quiz'][i]['assign'] else 'DIFF %s vs %s'%(q['assign'],E['quiz'][i]['assign']))
json.dump(out,open('v40proof.json','w'),indent=1)
