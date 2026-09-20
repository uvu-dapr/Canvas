# -*- coding: utf-8 -*-
"""Spring 2027 term spine for UVU DAPR courses.
Every date is computed from the UVU academic calendar, never typed twice.
Calendar verified 2026-09-20 against https://www.uvu.edu/schedule/spring/ ."""
import datetime as dt

FIRST_DAY = dt.date(2027,1,11)          # Mon, classes begin
TERM_END  = dt.date(2027,5,5)           # Wed, finals end, commencement, term ends
# DST 2027: second Sunday in March to first Sunday in November
DST_START = dt.date(2027,3,14)
DST_END   = dt.date(2027,11,7)

CLOSURES = {
 dt.date(2027,1,18): 'Martin Luther King Jr. Day, campus closed',
 dt.date(2027,2,15): 'Presidents Day, campus closed',
}
SPRING_BREAK = (dt.date(2027,3,15), dt.date(2027,3,21))
BLOCK_SWITCH = (dt.date(2027,3,2), dt.date(2027,3,3))     # first block ends, second begins
LAST_CLASS   = dt.date(2027,4,27)                          # Tue
INTERIM_DAY  = dt.date(2027,4,28)                          # Wed, no classes
FINALS       = (dt.date(2027,4,29), dt.date(2027,5,5))
CONVOCATIONS = (dt.date(2027,5,6), dt.date(2027,5,7))

def offset(d):
    """Hours to ADD to Mountain local time to get UTC. MST is 7, MDT is 6."""
    return 6 if DST_START <= d < DST_END else 7

def zulu(d,hh,mm=0):
    return (dt.datetime(d.year,d.month,d.day,hh,mm)+dt.timedelta(hours=offset(d))).strftime('%Y-%m-%dT%H:%M:%SZ')

def weeks():
    out=[];mon=FIRST_DAY;n=1
    while mon<=TERM_END:
        fri=mon+dt.timedelta(days=4)
        closed=SPRING_BREAK[0]<=mon<=SPRING_BREAK[1]
        note=[]
        for d,txt in sorted(CLOSURES.items()):
            if mon<=d<=fri: note.append(txt)
        if closed: note.append('Spring Break, campus closed all week')
        if mon<=BLOCK_SWITCH[0]<=fri: note.append('First block ends Tue 2 Mar, second block begins Wed 3 Mar')
        if mon<=LAST_CLASS<=fri:
            note.append('Classes end Tue 27 Apr. Interim Day Wed 28 Apr, no classes. Final exams begin Thu 29 Apr')
        if mon<=FINALS[1]<=fri and not (mon<=LAST_CLASS<=fri):
            note.append('Finals run Mon to Wed. Term ends and Commencement is Wed 5 May. Convocations Thu and Fri 6 to 7 May')
        span='%s to %s'%(mon.strftime('%b %-d'),fri.strftime('%b %-d') if fri.month==mon.month else fri.strftime('%b %-d'))
        out.append(dict(n=n,mon=mon,fri=fri,span=span,closed=closed,note='. '.join(note)))
        mon+=dt.timedelta(days=7);n+=1
    return out

W=weeks()

def due_fridays():
    """Fridays a graded item may be due: not week 1, not a closed week, not finals week."""
    ok=[]
    for w in W:
        if w['n']==1: continue                      # four days after classes begin
        if w['closed']: continue
        if w['fri']>LAST_CLASS: continue            # finals week owns the end
        ok.append(w)
    return ok
