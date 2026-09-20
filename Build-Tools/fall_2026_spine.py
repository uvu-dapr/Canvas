# -*- coding: utf-8 -*-
"""Fall 2026 term spine for UVU DAPR courses.
Every date is computed from the UVU academic calendar, never typed twice.
Calendar verified 2026-09-20 against https://www.uvu.edu/schedule/fall/ , which
matched the WEEKS table already in use in the DAPR 2000 build on every date.

Fall runs the opposite way to Spring: it starts in daylight time and ends in
standard time, so the offset comparison flips. Spring needs DST_START, Fall needs
DST_END. A script that hardcodes one offset puts every due date after 1 November
an hour wrong and nothing in Canvas warns you."""
import datetime as dt

FIRST_MONDAY = dt.date(2026,8,17)       # Mon, week 00 anchor
FIRST_CLASS  = dt.date(2026,8,19)       # Wed, classes begin
LAST_CLASS   = dt.date(2026,12,4)       # Fri, last day of classes
FINALS       = (dt.date(2026,12,7), dt.date(2026,12,11))
TERM_END     = dt.date(2026,12,12)      # Sat, official term end
# DST 2026: ends first Sunday in November
DST_END      = dt.date(2026,11,1)

CLOSURES = {
 dt.date(2026,9,7): 'Labor Day, campus closed',
}
FALL_BREAK    = (dt.date(2026,10,15), dt.date(2026,10,18))   # Thu to Sun
THANKSGIVING  = (dt.date(2026,11,23), dt.date(2026,11,29))   # Mon to Sun

def offset(d):
    """Hours to ADD to Mountain local time to get UTC. MDT is 6, MST is 7."""
    return 6 if d < DST_END else 7

def zulu(d,hh,mm=0):
    return (dt.datetime(d.year,d.month,d.day,hh,mm)+dt.timedelta(hours=offset(d))).strftime('%Y-%m-%dT%H:%M:%SZ')

def _overlap(a,b,lo,hi):
    return not (b < lo or a > hi)

def weeks():
    out=[];mon=FIRST_MONDAY;n=0
    while mon <= FINALS[1]:
        fri=mon+dt.timedelta(days=4)
        tg = _overlap(mon,fri,*THANKSGIVING)
        note=[]
        if mon <= FIRST_CLASS <= fri: note.append('Classes begin Wednesday 19 August')
        for d,txt in sorted(CLOSURES.items()):
            if mon <= d <= fri: note.append(txt)
        if _overlap(mon,fri,*FALL_BREAK): note.append('Fall Break Thursday 15 to Sunday 18 October, campus closed')
        if tg: note.append('Thanksgiving Break, campus closed all week')
        if mon <= LAST_CLASS <= fri: note.append('Last day of classes Friday 4 December')
        if mon <= FINALS[0] <= fri: note.append('Finals week. Term ends Saturday 12 December')
        span='%s to %s'%(mon.strftime('%b %-d'), fri.strftime('%b %-d'))
        out.append(dict(n=n,mon=mon,fri=fri,span=span,closed=tg,note='. '.join(note)))
        mon+=dt.timedelta(days=7);n+=1
    return out

W=weeks()

def due_fridays():
    """Fridays a graded item may be due. Excluded: week 00, because classes begin
    on the Wednesday; any week closed all week; any Friday inside Fall Break; and
    anything after the last day of classes, because finals week owns the end."""
    ok=[]
    for w in W:
        if w['n']==0: continue
        if w['closed']: continue
        if FALL_BREAK[0] <= w['fri'] <= FALL_BREAK[1]: continue
        if w['fri'] > LAST_CLASS: continue
        ok.append(w)
    return ok
