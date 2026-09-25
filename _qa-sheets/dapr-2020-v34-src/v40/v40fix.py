import re,json,os
os.chdir(os.path.expanduser('~/b40/wiki_content'))
chg=[]
def rep(f,old,new):
    s=open(f).read(); assert s.count(old)==1,(f,old[:60],s.count(old)); open(f,'w').write(s.replace(old,new)); chg.append(dict(page=f,before=old,after=new))
rep('calibration-and-monitoring-ms-mid-side-matrix.html',
 'Sum MS L and MS R together (both soloed). If the Side signal is correctly inverted, the Side components cancel and you are left with only the Mid signal, the same as MS C alone.',
 'Mute MS L and MS R. You should hear only the Mid signal, the same as MS C alone. Then solo MS L and MS R together. You hear only the Side information, wide and diffuse, and it cancels to silence when the mix is folded to mono. If it does not cancel, the polarity invert is missing from MS R.')
rep('master-buss-processing-and-endgame-knowing-when-to-stop.html',
 'Master buss processing is for the last few percent, after the mix already works.',
 'Gentle master buss compression can go on early and be mixed into. Everything else on the master buss comes last, for the last few percent, after the mix already works.')
s=open('master-buss-processing-and-endgame-knowing-when-to-stop.html').read()
m=re.search(r'Leave the peaks under 0 dBFS\.\s*What you deliver is not what a streaming service will play back\.',s); assert m
rep('master-buss-processing-and-endgame-knowing-when-to-stop.html',m.group(0),
 'Leave about 6 dB of peak headroom: peaks near -6 dBFS when the mix goes to mastering. The finished master&#39;s ceiling sits below 0 dBFS, at about -1 dBTP.')
for old,new in [('Mix buss processing added at the end','Mix buss compression added at the end'),('Put it on early and mix into it, or leave it off.','Put gentle buss compression on early and mix into it, or leave it off. Everything else on the master buss comes last.')]:
    rep('master-buss-processing-endgame-common-mistakes-and-how-to-hear-them.html',old,new)
rep('master-buss-processing-and-endgame-procedure-guide.html',
 'Insert master-bus processing in a deliberate order and make small, level-matched changes. Leave headroom for the final bounce.',
 'Put gentle master-bus compression on early and mix into it. Add everything else on the master bus last, with small, level-matched changes. Leave about 6 dB of peak headroom, with peaks near -6 dBFS, in the mix that goes to mastering.')
json.dump(chg,open(os.path.expanduser('~/v40_pagefixes.json'),'w'),indent=1)
print(len(chg),'edits')
