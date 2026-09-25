#!/usr/bin/env python3
"""Standards §11e / §11e-1 credit hour budget for a DAPR cartridge. This is gate 12j.

Run it from inside an unzipped .imscc, or pass the folder:

    python3 budget_check.py .
    DAPR_POINT_MODEL=A python3 budget_check.py .      # only for a course not in the §11e-1 table

preflight.py imports this file and runs the same check as gate 12j, so the two can never
disagree. Rewritten 2026-09-24. The version before this read only assignments/*.xml and
quizzes/*_meta.xml, so on a Canvas export (one folder per object: g<id>/assignment_settings.xml,
g<id>/assessment_meta.xml) it found nothing, reported a 0 point course and failed it as thin.
Platform Reference 30: never count, always resolve. Graded objects are now resolved from the
files the manifest declares, whatever folder they sit in.

What it has to know, and where it learns it (course facts are never typed into this file
twice; the built-in table is only a fallback when the documents cannot be found):

    credits, and whether a lab is part of the course   Folder Map & CLOs §2b (§3.13 for courses §2b leaves out)
    which model (A or B), budget, ceiling, range       DAPR Canvas Standards §11e-1
"""
import os, re, sys, glob, datetime as dt
import xml.etree.ElementTree as ET

STANDARDS_DIR = os.environ.get('DAPR_STANDARDS_DIR',
    '/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Applications/AI Projects Standards/Work/Utah Valley University')

MODELS = {
    'A': dict(label='A, 3 credit lecture', hours=90, ceiling=1500, low=1350, thin=1200, weekly=100,
              basis='3 credit lecture: 6 outside hours a week x 15 weeks = 90 h'),
    'B': dict(label='B, 3 credit lecture plus 1 credit lab', hours=135, ceiling=2250, low=2025, thin=1800, weekly=150,
              basis='3 credit lecture: 6 outside hours a week x 15 weeks = 90 h, plus 1 credit lab: about 3 scheduled lab hours a week and 0 outside hours x 15 weeks = 45 h, the time students use to finish the lecture practical work (Standards 11e-0), total 135 h'),
}
# Fallback only. The live values come from the Standards and Folder Map files above.
FALLBACK = {
    'DAPR 2000': ('Digital Audio Essentials', 3, None, 0, 'A'),   # no lab beginning Fall 2026 (Standards 11e-0)
    'DAPR 2010': ('Core Recording', 3, 'DAPR 2010L', 1, 'B'),
    'DAPR 2020': ('Core Mixing', 3, 'DAPR 2020L', 1, 'B'),
    'DAPR 2080': ('Podcast and Radio Production', 3, None, 0, 'A'),
    'DAPR 2255': ('Audio Hardware I', 3, None, 0, 'A'),
    'DAPR 3255': ('Audio Hardware II', 3, None, 0, 'A'),
    'DAPR 3340': ('Spatial Audio I', 3, None, 0, 'A'),
    'DAPR 3345': ('Spatial Audio II', 3, None, 0, 'A'),
}
TIERS = {10, 25, 50, 75, 100, 150, 200}
HOURS_PER_POINT = {'fastest': 0.04, 'median': 0.06, 'slowest': 0.08}   # 25 pts = 1 h, 90 min, 2 h
TERM_WEEKS = 15


def _txt(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()


def _newest(suffix):
    try:
        names = [n for n in os.listdir(STANDARDS_DIR) if n.endswith(suffix)]
    except OSError:
        return None
    return os.path.join(STANDARDS_DIR, sorted(names)[-1]) if names else None


def spine_for(items):
    """The Term Spine whose week 00 is the latest one on or before the first date in the course."""
    dates = [d for i in items for d in (i['unlock'], i['due']) if d]
    try:
        names = [n for n in os.listdir(STANDARDS_DIR) if n.endswith('Term Spine.md')]
    except OSError:
        return None
    best = None
    for n in names:
        m = re.search(r'\|\s*00\s*\|\s*`(\d{4}-\d{2}-\d{2})`', _txt(os.path.join(STANDARDS_DIR, n)))
        if not m: continue
        start = dt.datetime.strptime(m.group(1), '%Y-%m-%d')
        if dates and start <= min(dates) + dt.timedelta(days=7) and (best is None or start > best[0]):
            best = (start, os.path.join(STANDARDS_DIR, n))
    return best[1] if best else None


def _num(s):
    s = re.sub(r'[^\d.]', '', s or '')
    return float(s) if s else None


# ---------------------------------------------------------------- course facts
def course_facts(code):
    """Everything §11e needs to know about one course: credits, lab, model and budget, with sources."""
    facts = dict(code=code, name='', credits=None, lab=None, lab_credits=0, model=None, sources=[])
    std = _newest('DAPR Canvas Standards.md')
    fmap = _newest('Folder Map & CLOs.md')
    # Standards §11e-1 table: | DAPR 2010 Core Recording | lecture + DAPR 2010L, one cartridge | **B** | 135 h | 2,250 | 2,025 to 2,250 | 1,800 | 150 pts |
    # (DAPR 2000 has no lab from Fall 2026 and is Model A, §11e-0 and §11e-1.)
    if std:
        for line in _txt(std).splitlines():
            if not line.startswith('| ' + code + ' '):
                continue
            cols = [c.strip() for c in line.strip('|').split('|')]
            m = re.search(r'\*\*([AB])\*\*', line)
            if len(cols) >= 8 and m:
                facts['name'] = cols[0][len(code):].strip()
                facts['model'] = m.group(1)
                lab = re.search(r'(DAPR \d{4}L)', cols[1])
                if lab:
                    facts['lab'] = lab.group(1)
                rng = re.findall(r'[\d,]+', cols[5])
                facts['table'] = dict(hours=_num(cols[3]), ceiling=_num(cols[4]),
                                      low=_num(rng[0]) if rng else None, thin=_num(cols[6]), weekly=_num(cols[7]))
                facts['sources'].append('model and budget: %s §11e-1' % os.path.basename(std))
                break
    # Credits: Folder Map §2b is authoritative ("| Course | Title | Credits | Type | ..."). §2b leaves out
    # DAPR 2080 and 3010R on purpose and points to §3.13 ("| Course | Credits | Term | ..."), so fall back to it.
    if fmap:
        def table(header, credit_col):
            rows, in_table = {}, False
            for line in _txt(fmap).splitlines():
                if re.match(header, line):
                    in_table = True
                    continue
                if in_table:
                    if not line.startswith('|'):
                        if rows: break
                        continue
                    cols = [c.strip() for c in line.strip().strip('|').split('|')]
                    if len(cols) > credit_col and re.match(r'DAPR \d{4}[A-Z]?$', cols[0]):
                        n = re.match(r'(\d+)', cols[credit_col])
                        if n: rows[cols[0]] = int(n.group(1))
            return rows
        for section, header, col in (('§2b', r'\|\s*Course\s*\|\s*Title\s*\|\s*Credits\s*\|', 2),
                                     ('§3.13', r'\|\s*Course\s*\|\s*Credits\s*\|', 1)):
            rows = table(header, col)
            if code in rows:
                facts['credits'] = rows[code]
                if facts['lab'] is None and (code + 'L') in rows:
                    facts['lab'] = code + 'L'
                if facts['lab']:
                    facts['lab_credits'] = rows.get(facts['lab'], 1)
                facts['credits_section'] = section
                facts['sources'].append('credits: %s %s' % (os.path.basename(fmap), section))
                break
    fb = FALLBACK.get(code)
    if fb:
        if not facts['name']: facts['name'] = fb[0]
        if facts['credits'] is None: facts['credits'] = fb[1]
        if facts['lab'] is None and fb[2]: facts['lab'], facts['lab_credits'] = fb[2], fb[3]
        if facts['model'] is None: facts['model'] = fb[4]
        if len(facts['sources']) < 2:
            facts['sources'].append('built-in fallback table in budget_check.py (a standards file could not be read)')
    return facts


def identify_course(root):
    """Course code from the package itself: course_settings.xml, then the manifest title, then the folder name."""
    hay = []
    cs = os.path.join(root, 'course_settings', 'course_settings.xml')
    if os.path.exists(cs):
        t = _txt(cs)
        for tag in ('course_code', 'title'):
            m = re.search(r'<%s>(.*?)</%s>' % (tag, tag), t, re.S)
            if m: hay.append(m.group(1))
    mp = os.path.join(root, 'imsmanifest.xml')
    if os.path.exists(mp):
        m = re.search(r'<(?:\w+:)?title>\s*(?:<[^>]+>)*([^<]+)', _txt(mp))
        if m: hay.append(m.group(1))
    hay.append(os.path.basename(os.path.abspath(root)))
    for h in hay:
        m = re.search(r'DAPR[\s_-]*(\d{4})(L?)\b', h, re.I)
        if m:
            return 'DAPR %s' % m.group(1), bool(m.group(2)), h.strip()
    return None, False, (hay[0].strip() if hay else '')


# ---------------------------------------------------------------- graded objects, resolved from the manifest
def _local(tag):
    return tag.split('}')[-1]


def _child(el, name):
    for c in el:
        if _local(c.tag) == name:
            return (c.text or '').strip()
    return ''


def _date(s):
    if not s:
        return None
    try:
        return dt.datetime.strptime(s[:19], '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return None


def graded_objects(root):
    mp = os.path.join(root, 'imsmanifest.xml')
    man = _txt(mp)
    declared = set()
    for h in re.findall(r'<(?:\w+:)?(?:file|resource)\b[^>]*\bhref="([^"]+)"', man):
        declared.add(h.replace('&amp;', '&'))
    try:
        from urllib.parse import unquote
        declared = {unquote(h) for h in declared}
    except Exception:
        pass
    out, seen = [], set()
    for rel in sorted(declared):
        if not rel.endswith('.xml') or rel in seen:
            continue
        seen.add(rel)
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            continue
        try:
            el = ET.parse(p).getroot()
        except ET.ParseError:
            continue
        kind, src = _local(el.tag), el
        if kind == 'assignment':
            if _child(el, 'grading_type') == 'not_graded':
                continue
        elif kind == 'quiz':
            if _child(el, 'quiz_type') not in ('assignment', 'graded_survey'):
                continue
        elif kind == 'topicMeta':
            src = next((c for c in el if _local(c.tag) == 'assignment'), None)   # graded discussion
            if src is None:
                continue
            kind = 'discussion'
        else:
            continue
        title = _child(el, 'title')
        pts = _num(_child(src, 'points_possible'))
        if pts is None:
            continue
        low = title.lower()
        out.append(dict(file=rel, kind=kind, title=title, pts=pts,
                        due=_date(_child(src, 'due_at') or _child(el, 'due_at')),
                        unlock=_date(_child(src, 'unlock_at') or _child(el, 'unlock_at')),
                        alt=bool(re.search(r'-\s*Alt\s*\d', title)),
                        attendance='roll call' in low or 'attendance' in low,
                        bonus=_child(src, 'omit_from_final_grade') == 'true' or '(Bonus)' in title or title.startswith('Bonus:'),
                        final=kind == 'quiz' and 'final' in low))
    return out


# ---------------------------------------------------------------- the check
# ---------------------------------------------------------------- accepted decisions
# Added 2026-09-25 [Adam]. A collision Adam has looked at and accepted (DAPR 2020's Fri 4 Dec,
# three items above 75 points) should not keep failing every build, and a term Adam has
# decided to run under the floor (DAPR 2000 Fall 2026, decided mid-term) should not either.
# Each decision is one line in accepted-decisions.md, kept beside the cartridges in the
# course's -Canvas Entire Course folder, never inside a cartridge:
#   collision: 2026-12-04 | Final Mix: "A Horse Is Not a Home"; Final Mix - Jeff Hirata; Mixing Topic Presentation | Adam, 2026-09-24
#   budget: Fall 2026 | work total under the floor, live course mid-term | Adam, 2026-09-25
# A collision line matches only when its date falls in the colliding week AND every item in
# that collision is named (a title or any unique part of one). A budget line matches only the
# term the package's own due dates fall in. Anything not listed still fails.
def _accepted_file(root, code):
    if os.environ.get('DAPR_ACCEPTED'):
        return os.environ['DAPR_ACCEPTED']
    d = os.path.abspath(root)
    for _ in range(3):
        p = os.path.join(d, 'accepted-decisions.md')
        if os.path.exists(p): return p
        d = os.path.dirname(d)
    if not code: return None
    here = os.path.dirname(os.path.abspath(__file__))
    roots, d = [], here
    for _ in range(10):
        roots.append(os.path.join(d, 'Miscellaneous', '4-Work', 'UVU', 'UVU Courses'))
        roots.append(os.path.join(d, 'UVU Courses'))
        up = os.path.dirname(d)
        if up == d: break
        d = up
    roots += ['/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses',
              os.path.expanduser('~/mnt/UVU Courses'),
              os.path.expanduser('~/mnt/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses')]
    for r in roots:
        for p in sorted(glob.glob(os.path.join(r, code + ' - *', 'Canvas', 'Canvas Templates',
                                               '-Canvas Entire Course', 'accepted-decisions.md'))):
            return p
    return None

def _term_of(items):
    ds = sorted(i['due'] for i in items if i.get('due'))
    if not ds: return None
    d = ds[len(ds) // 2]
    return ('Spring' if d.month <= 5 else 'Summer' if d.month <= 7 else 'Fall') + ' %d' % d.year

def accepted_decisions(root, code):
    p = _accepted_file(root, code)
    out = dict(path=p, collision=[], budget=[])
    if not p or not os.path.exists(p): return out
    for line in _txt(p).splitlines():
        m = re.match(r'\s*[-*]?\s*(collision|budget)\s*:\s*(.+)$', line, re.I)
        if not m: continue
        parts = [x.strip() for x in m.group(2).split('|')]
        if m.group(1).lower() == 'collision' and len(parts) >= 2:
            try:
                day = dt.datetime.strptime(parts[0], '%Y-%m-%d').date()
            except ValueError:
                continue
            out['collision'].append(dict(day=day, titles=[t.strip().strip('"').lower() for t in parts[1].split(';') if t.strip()],
                                         who=parts[2] if len(parts) > 2 else 'accepted'))
        elif m.group(1).lower() == 'budget':
            out['budget'].append(dict(term=parts[0].lower(), why=parts[1] if len(parts) > 1 else '',
                                      who=parts[2] if len(parts) > 2 else 'accepted'))
    return out


def run(root='.', exclude=None):
    """Returns (fails, warns, report_lines, ai_block). Never exits, never changes directory.
    exclude: package paths of Instructor Use Only items (preflight passes its exemption list);
    they are not student work and are left out of every 12j count."""
    fails, warns, L = [], [], []
    code, is_lab_code, where = identify_course(root)
    forced = os.environ.get('DAPR_POINT_MODEL', '').strip().upper()
    facts = course_facts(code) if code else dict(code=None, name='', credits=None, lab=None, lab_credits=0, model=None, sources=[])
    key = forced or facts.get('model')

    L.append('COURSE')
    L.append('  Package course code:  %s' % (where or 'not found'))
    if code:
        L.append('  Course:               %s %s, %s credits, lecture' % (code, facts['name'], facts['credits'] if facts['credits'] is not None else '?'))
        if facts['lab']:
            L.append('  Lab:                  %s, %d credit, part of this course and built into this one cartridge (§11e-1)' % (facts['lab'], facts['lab_credits']))
        else:
            L.append('  Lab:                  none, lecture only')
        total_credits = (facts['credits'] or 0) + (facts['lab_credits'] or 0)
        L.append('  Total credits:        %d' % total_credits)
    if is_lab_code:
        fails.append('this package is a lab cartridge (%sL); §11e-1 says a lecture and its lab ship as ONE cartridge named for the lecture' % code)
    if not key:
        fails.append('the course is not in the §11e-1 table and no model was named; re-run with DAPR_POINT_MODEL=A or B')
        L.append('  Model:                UNKNOWN')
        return fails, warns, L, ''
    if code and facts['credits'] not in (None, 3):
        warns.append('%s is %s credits; §11e only defines budgets for 3 credit lectures, with or without a 1 credit lab' % (code, facts['credits']))
    if code and facts['model'] and facts['lab'] and facts['model'] != 'B':
        warns.append('%s has a lab (%s) but §11e-1 lists it as Model %s' % (code, facts['lab'], facts['model']))
    M = dict(MODELS[key])
    if facts.get('table') and not forced:
        for k in ('hours', 'ceiling', 'low', 'thin', 'weekly'):
            if facts['table'].get(k): M[k] = facts['table'][k]
    L.append('  Model:                %s%s' % (M['label'], ' (forced by DAPR_POINT_MODEL)' if forced else ''))
    L.append('  Why that many hours:  %s' % M['basis'])
    L.append('  Budget:               %d h, ceiling %s, build range %s to %s, thin below %s, %d points a week'
             % (M['hours'], format(int(M['ceiling']), ','), format(int(M['low']), ','), format(int(M['ceiling']), ','), format(int(M['thin']), ','), M['weekly']))
    for s in facts.get('sources', []):
        L.append('  Source:               %s' % s)

    items = graded_objects(root)
    # Added 2026-09-25 [Adam, DAPR 2020 v39]: the unpublished Lab Template in Instructor Use Only
    # failed the tier check at 30 points. Instructor Use Only items are not student work.
    _ex = {os.path.normpath(x) for x in (exclude or ())}
    instr = [i for i in items if os.path.normpath(i['file']) in _ex]
    items = [i for i in items if os.path.normpath(i['file']) not in _ex]
    live = [i for i in items if not i['alt']]
    held = [i for i in items if i['alt']]
    published = sum(i['pts'] for i in live)
    excluded = sum(i['pts'] for i in live if i['bonus'] or i['attendance'])
    work = published - excluded
    hours = {k: work * v for k, v in HOURS_PER_POINT.items()}
    pct = hours['median'] / M['hours'] * 100

    # 1-2 ceiling, floor, range
    if work > M['ceiling']:
        fails.append('work time total %d is over the Model %s ceiling of %d by %d points (%.0f median hours)'
                     % (work, key, M['ceiling'], work - M['ceiling'], (work - M['ceiling']) * HOURS_PER_POINT['median']))
    elif work < M['thin']:
        fails.append('work time total %d is under the Model %s thin floor of %d (the build range is %d to %d)'
                     % (work, key, M['thin'], M['low'], M['ceiling']))
    elif work < M['low']:
        warns.append('work time total %d is above the thin floor but under the build range of %d to %d' % (work, M['low'], M['ceiling']))

    # 3 tier scale
    for i in live:
        if i['attendance'] or i['bonus']: continue
        if i['pts'] not in TIERS:
            fails.append('off tier: %s is %g points (tiers: 10, 25, 50, 75, 100, 150, 200)' % (i['title'][:60], i['pts']))

    # 4-5 weekly spread load and open window; the final is budgeted 33 a week over its last three weeks
    def monday(x): return (x - dt.timedelta(days=x.weekday())).date()
    weekload = {}
    for i in live:
        if i['bonus'] or i['attendance'] or not i['due']: continue
        due, unl = i['due'], i['unlock']
        if i['final']:
            weeks, start = 3, monday(due) - dt.timedelta(weeks=2)
        else:
            weeks = max(1, int(round((due - unl).days / 7.0))) if unl and unl < due else 1
            start = monday(unl) if unl and unl < due else monday(due)
            need = max(1, -(-int(i['pts']) // 50))
            if weeks < need:
                fails.append('open window: %s is %g points but open %d week(s); needs %d (one week per 50 points)' % (i['title'][:52], i['pts'], weeks, need))
        for k in range(weeks):
            w = start + dt.timedelta(weeks=k)
            weekload[w] = weekload.get(w, 0) + i['pts'] / float(weeks)
    over = sorted((w, v) for w, v in weekload.items() if v > M['weekly'] + 0.01)
    for w, v in over:
        fails.append('week of %s carries %.0f points of spread load; Model %s capacity is %d' % (w, v, key, M['weekly']))

    # 6 two items above 75 points due the same week
    byweek = {}
    for i in live:
        if i['bonus'] or i['attendance'] or not i['due'] or i['pts'] <= 75: continue
        byweek.setdefault(monday(i['due']), []).append(i)
    collisions = [(w, l) for w, l in sorted(byweek.items()) if len(l) > 1]
    for w, lst in collisions:
        fails.append('collision: week of %s has %d items above 75 points due: %s' % (w, len(lst), '; '.join('%s (%g)' % (x['title'][:40], x['pts']) for x in lst)))

    if not items:
        fails.append('no graded objects were found in the files the manifest declares; the gate is not seeing the package')

    # ------------------------------------------------------------ report, in the §11e-1 shape
    L.append('')
    L.append('11e POINT BUDGET')
    L.append('Published course total:   %s' % format(int(published), ','))
    L.append('Attendance and bonus:     %s' % format(int(excluded), ','))
    L.append('Work time total:          %s' % format(int(work), ','))
    L.append('Median student hours:     %.1f of %d h  (%.0f percent of budget, %.1f h per week)' % (hours['median'], M['hours'], pct, hours['median'] / TERM_WEEKS))
    L.append('Student range:            fastest %.0f h, median %.0f h, slowest %.0f h  (25 pts = 1 h, 90 min, 2 h)' % (hours['fastest'], hours['median'], hours['slowest']))
    L.append('Model:                    %s' % M['label'])
    L.append('Weeks over capacity:      %d of %d' % (len(over), len(weekload)))
    L.append('Items above 75 pts sharing a due week: %d' % sum(len(l) for _, l in collisions))
    L.append('Graded objects resolved:  %d (%d held alternates left out: %s)' % (len(items), len(held), ', '.join(i['title'] for i in held) or 'none'))
    if instr:
        L.append('Instructor Use Only:      %d left out: %s' % (len(instr), ', '.join(i['title'] for i in instr)))
    # accepted decisions turn their one matching fail into a warning that names the decision
    acc = accepted_decisions(root, code)
    term = _term_of(live)
    if acc['path']:
        L.append('Accepted decisions:       %s (%d collision, %d budget)' % (acc['path'], len(acc['collision']), len(acc['budget'])))
    def _monday(x): return x - dt.timedelta(days=x.weekday())
    for w, lst in collisions:
        msg = [f for f in fails if f.startswith('collision: week of %s ' % w)]
        if not msg: continue
        hit = next((a for a in acc['collision'] if _monday(a['day']) == w and
                    all(any(t in x['title'].lower() for t in a['titles']) for x in lst)), None)
        if hit:
            fails.remove(msg[0])
            warns.append('accepted collision (%s): %s' % (hit['who'], msg[0][len('collision: '):]))
    floor = [f for f in fails if 'thin floor' in f or 'over the Model' in f]
    for f in floor:
        hit = next((a for a in acc['budget'] if term and a['term'] == term.lower()), None)
        if hit:
            fails.remove(f)
            warns.append('accepted budget exception for %s (%s, %s): %s' % (term, hit['why'], hit['who'], f))
    for k, v in enumerate(L):
        if v.startswith('Result: '):
            L[k] = 'Result: FAIL' if fails else ('Result: inside the thin floor, below the build range' if warns else 'Result: inside the build range')
    if fails:
        L.append('Result: FAIL')
    elif warns:
        L.append('Result: inside the thin floor, below the build range')
    else:
        L.append('Result: inside the build range')

    return fails, warns, L, ai_block(root, code, facts, M, key, live, published, excluded, work, hours, pct, fails, warns, weekload)


def ai_block(root, code, facts, M, key, live, published, excluded, work, hours, pct, fails, warns, weekload):
    std = _newest('DAPR Canvas Standards.md')
    fmap = _newest('Folder Map & CLOs.md')
    spine = spine_for(live)
    lo, hi = M['low'], M['ceiling']
    B = []
    B.append('===== COPY FROM HERE TO GIVE TO AI =====')
    B.append('Update this Canvas cartridge so its student workload meets the credit hour standard.')
    B.append('')
    B.append('Package (unzipped): %s' % os.path.abspath(root))
    if code:
        lab = (' plus %s lab, %d credit, built into the same cartridge' % (facts['lab'], facts['lab_credits'])) if facts['lab'] else ', no lab'
        B.append('Course: %s %s, %s credit lecture%s. Model %s.' % (code, facts['name'], facts['credits'], lab, key))
    B.append('Budget: %d median student hours (%s). Build range %s to %s work time points, thin below %s, at most %d points of spread load in any week.'
             % (M['hours'], M['basis'], format(int(lo), ','), format(int(hi), ','), format(int(M['thin']), ','), M['weekly']))
    B.append('Read first: %s sections 11, 11a, 11d, 11e and 11e-1%s%s.' % (std or 'DAPR Canvas Standards', ('; credits: %s section %s' % (fmap, facts.get('credits_section', '§2b').lstrip('§'))) if fmap else '', ('; dates: %s' % spine) if spine else ''))
    B.append('')
    B.append('Where it stands now:')
    B.append('- Published total %s, attendance and bonus %s, work time %s.' % (format(int(published), ','), format(int(excluded), ','), format(int(work), ',')))
    B.append('- Median student %.0f h of %d h (%.0f%%); fastest %.0f h, slowest %.0f h.' % (hours['median'], M['hours'], pct, hours['fastest'], hours['slowest']))
    if work < lo:
        B.append('- Short of the build range by %s to %s points (%.0f to %.0f median hours).'
                 % (format(int(lo - work), ','), format(int(hi - work), ','), (lo - work) * 0.06, (hi - work) * 0.06))
    elif work > hi:
        B.append('- Over the ceiling by %s points; something must come out.' % format(int(work - hi), ','))
    busiest = max(weekload.values()) if weekload else 0
    B.append('- Busiest week carries %.0f of %d points.' % (busiest, M['weekly']))
    for f in fails: B.append('- FAIL: %s' % f)
    for w in warns: B.append('- warn: %s' % w)
    B.append('')
    B.append('Graded items now (points, opens, due, file):')
    for i in sorted(live, key=lambda x: (x['due'] or dt.datetime.max, x['title'])):
        tag = ' [attendance, not counted]' if i['attendance'] else (' [bonus, not counted]' if i['bonus'] else '')
        B.append('- %s: %g pts, opens %s, due %s, %s%s' % (i['title'], i['pts'],
                 i['unlock'].strftime('%Y-%m-%d') if i['unlock'] else '-', i['due'].strftime('%Y-%m-%d') if i['due'] else '-', i['file'], tag))
    B.append('')
    B.append('How to fix it (from the Standards):')
    B.append('- Add or rescope graded work; never raise the points on an existing item just to hit the number (section 11a, Course total).')
    B.append('- Small modules follow Pattern A: one 25 point assignment and one 25 point quiz, 50 per module; reading-only modules get a quiz only (11a).')
    B.append('- Integrative work follows Pattern B: projects at 75, 100, 150 or 200 points, opened one week per 50 points (11a, 11e).')
    B.append('- Every item sits on the tier scale 10, 25, 50, 75, 100, 150, 200 (11). Open Monday, due Friday 9:00 AM Mountain, never in a closure (11d).')
    B.append('- Never two items above 75 points due the same week; no week over %d points of spread load (11e).' % M['weekly'])
    B.append('- The final stays 100 questions and 100 points (9.1a); there is no midterm (9.1).')
    B.append('')
    B.append('Before editing any file, show me the plan: a table of every item to add, rescope or remove, with module, points, open week and due week, and the new budget math. Ask me to choose using Standards 0.5 (multiple choice with your recommendation). After I approve, build it, re-run preflight.py on a fresh unzip, and report gate 12j.')
    B.append('===== END =====')
    return '\n'.join(B)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    if not os.path.exists(os.path.join(root, 'imsmanifest.xml')):
        print('FAIL  no imsmanifest.xml in %s; run this inside an unzipped .imscc' % os.path.abspath(root))
        sys.exit(2)
    fails, warns, lines, block = run(root)
    for l in lines: print(l)
    for f in fails: print('  FAIL  %s' % f)
    for w in warns: print('  warn  %s' % w)
    if block:
        print('')
        print(block)
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
