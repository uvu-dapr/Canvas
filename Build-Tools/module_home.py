#!/usr/bin/env python3
"""Everything lives in a module (J397, Adam 2026-10-15).

TidyUP's "not in a module, delete all" took 78 items out of live DAPR 2000 on 2026-10-15 because each was in no module.
A package never leaves an item unplaced: every page, assignment, quiz and discussion it carries is in one of its modules
(or, for a partial LIVE package, already in a live module). Syllabus pages and instructor items (*No Publish, Instructor
Use Only, [Do Not Publish]) go into the class's "<Class> - DAPR NNNN - Instructor Use Only - [Do Not Publish]" module.
The front page needs no module (it is the course's Home). Files and web links are left to unused_files.py.

  python3 module_home.py check <package folder or .imscc> [--live <the class's current export .imscc>]
  python3 module_home.py fix <in.imscc> <out.imscc>     a package that carries its Instructor Use Only module (Full,
                                                         Template): each unplaced item goes to the end of that module,
                                                         unpublished. Never overwrites.

preflight.py gate 12w imports find() and carries_modules(). A package that carries no modules (a pages-only Update) is not
fixed here: it cannot carry the live Instructor Use Only module safely (export ids are not import match ids), so after its
import Fix Everything step 11 (Put Everything in Its Module) places the item live; 12w only warns for it.
"""
import hashlib, html, os, re, sys, urllib.parse, zipfile


class Reader:
    """A package as an unpacked folder or a zip, read in place (an export is never copied, Standards 16c)"""
    def __init__(self, path):
        if not os.path.exists(path): raise FileNotFoundError(path)
        self.path = path
        self.zip = zipfile.ZipFile(path) if os.path.isfile(path) else None

    def names(self):
        if self.zip: return self.zip.namelist()
        out = []
        for dp, dn, fn in os.walk(self.path):
            for f in fn: out.append(os.path.relpath(os.path.join(dp, f), self.path))
        return out

    def read(self, name):
        try:
            if self.zip: return self.zip.read(name).decode('utf-8', 'ignore')
            with open(os.path.join(self.path, name), encoding='utf-8', errors='ignore') as f: return f.read()
        except (KeyError, OSError):
            return ''


def _strip_ns(t, root):
    ns = re.findall(r'<(\w+):%s[\s>]' % root, t)
    return re.sub(r'</?%s:' % re.escape(ns[0]), lambda m: m.group(0).replace(ns[0] + ':', ''), t) if ns else t


def title_key(s):
    return re.sub(r'[^a-z0-9]+', '', html.unescape(s or '').lower())


def is_instructor(title):
    t = (title or '').strip()
    return t.startswith('*No Publish') or 'instructor use only' in t.lower() or '[do not publish]' in t.lower()


def is_syllabus_page(item):
    return item['kind'] == 'page' and 'syllabus' in title_key(item['title'])


def _tag(t, name):
    m = re.search(r'<%s\b[^>]*>(.*?)</%s>' % (name, name), t, re.S)
    return html.unescape(m.group(1).strip()) if m else ''


def items(rd):
    """Every page, assignment, quiz and discussion the package carries: kind, ident, title, slug, front"""
    man = _strip_ns(rd.read('imsmanifest.xml'), 'manifest')
    names = set(rd.names())
    res = {}
    for m in re.finditer(r'<resource\b([^>]*?)(?:/>|>(.*?)</resource>)', man, re.S):
        at, body = m.group(1), m.group(2) or ''
        i = re.search(r'identifier="([^"]+)"', at)
        if not i: continue
        t = re.search(r'type="([^"]+)"', at); h = re.search(r'href="([^"]+)"', at)
        res[i.group(1)] = {'type': t.group(1) if t else '', 'href': urllib.parse.unquote(h.group(1)) if h else '',
                           'files': [urllib.parse.unquote(x) for x in re.findall(r'<file href="([^"]+)"', body)],
                           'deps': re.findall(r'<dependency identifierref="([^"]+)"', body)}
    out = []
    for ident, r in res.items():
        ty, href = r['type'], r['href']
        if ty == 'webcontent' and href.startswith('wiki_content/') and href.endswith('.html'):
            t = rd.read(href)
            out.append({'kind': 'page', 'ident': ident, 'title': _tag(t, 'title'), 'slug': href[len('wiki_content/'):-5],
                        'front': bool(re.search(r'<meta name="front_page" content="true"', t))})
        elif 'imsqti' in ty:
            meta = '%s/assessment_meta.xml' % ident
            t = rd.read(meta) if meta in names else ''
            out.append({'kind': 'quiz', 'ident': ident, 'title': _tag(re.sub(r'<assignment\b.*?</assignment>', '', t, flags=re.S), 'title'), 'slug': '', 'front': False})
        elif ty.startswith('imsdt'):
            t = rd.read(href or (r['files'] or [''])[0])
            deps = ''.join(rd.read(res.get(d, {}).get('href', '')) for d in r['deps'])
            if re.search(r'<type>announcement</type>', deps): continue
            out.append({'kind': 'discussion', 'ident': ident, 'title': _tag(t, 'title'), 'slug': '', 'front': False})
        elif '%s/assignment_settings.xml' % ident in names:
            t = rd.read('%s/assignment_settings.xml' % ident)
            if not re.sub(r'<\?xml[^>]*\?>\s*', '', t, count=1).lstrip().startswith('<assignment'): continue
            out.append({'kind': 'assignment', 'ident': ident, 'title': _tag(t, 'title'), 'slug': '', 'front': False})
    return out


def placed(rd):
    """What the package's modules list: identifierrefs, page addresses, (kind, title key); and the Instructor Use Only
    module's identifier"""
    mm = _strip_ns(rd.read('course_settings/module_meta.xml'), 'modules')
    refs = set(re.findall(r'<identifierref>([^<]+)</identifierref>', mm))
    kinds = {'WikiPage': 'page', 'Assignment': 'assignment', 'Quizzes::Quiz': 'quiz', 'DiscussionTopic': 'discussion'}
    titles = set()
    for b in re.findall(r'<item identifier="[^"]+">(.*?)</item>', mm, re.S):
        k = kinds.get(_tag(b, 'content_type'))
        if k: titles.add((k, title_key(_tag(b, 'title'))))
    by = {i['ident']: i for i in items(rd)}
    slugs = {by[r]['slug'] for r in refs if r in by and by[r]['slug']}
    iuo = None
    for mid, mb in re.findall(r'<module identifier="([^"]+)">(.*?)(?=<module identifier=|</modules>)', mm, re.S):
        if 'instructor use only' in _tag(re.sub(r'<items>.*?</items>', '', mb, flags=re.S), 'title').lower(): iuo = mid; break
    return refs, slugs, titles, iuo


def carries_modules(path='.'):
    """True when the package carries modules of its own (Full, Template, a LIVE package with modules)"""
    return bool(re.search(r'<module identifier=', _strip_ns(Reader(path).read('course_settings/module_meta.xml'), 'modules')))


def find(path='.', live=None):
    """Items the package carries in none of its modules (and, with live, in no live module either): list of
    (item, why the Instructor Use Only module is its place, or the week module it should be in)"""
    rd = Reader(path)
    refs, slugs, titles, _ = placed(rd)
    lrefs = lslugs = ltitles = set()
    if live:
        lrefs, lslugs, ltitles, _ = placed(Reader(live))
    out = []
    for it in items(rd):
        if it['front'] or it['ident'] in refs: continue
        if live and (it['ident'] in lrefs or (it['slug'] and it['slug'] in lslugs) or (it['kind'], title_key(it['title'])) in ltitles): continue
        where = 'Instructor Use Only (a Syllabus page)' if is_syllabus_page(it) else 'Instructor Use Only (an instructor item)' if is_instructor(it['title']) else 'its week module, or Instructor Use Only'
        out.append((it, where))
    return out


def fix(src, dst):
    """Full packages: every unplaced item at the end of the Instructor Use Only module, unpublished"""
    if os.path.exists(dst): sys.exit('refused: %s exists (never overwrite a package; save as the next free version)' % dst)
    rd = Reader(src)
    loose = find(src)
    mm = rd.read('course_settings/module_meta.xml')
    _, _, _, iuo = placed(rd)
    if not loose: print('nothing to fix: every item is in a module'); return
    if not iuo: sys.exit('refused: the package carries no "<Class> - DAPR NNNN - Instructor Use Only - [Do Not Publish]" module '
                         '(a partial package): after its import, Fix Everything step 11 (Put Everything in Its Module) places the items live')
    ctype = {'page': 'WikiPage', 'assignment': 'Assignment', 'quiz': 'Quizzes::Quiz', 'discussion': 'DiscussionTopic'}
    m = re.search(r'(<module identifier="%s">.*?)(</items>)' % re.escape(iuo), mm, re.S)
    if not m: sys.exit('refused: the Instructor Use Only module has no <items> list to add to')
    pos = max([int(x) for x in re.findall(r'<position>(\d+)</position>', re.search(r'<items>.*', m.group(1), re.S).group(0))] or [0])
    add = ''
    for it, _ in loose:
        pos += 1
        iid = 'g' + hashlib.md5(('module_home ' + it['ident']).encode()).hexdigest()
        add += ('      <item identifier="%s">\n        <content_type>%s</content_type>\n        <workflow_state>unpublished</workflow_state>\n'
                '        <title>%s</title>\n        <identifierref>%s</identifierref>\n        <position>%d</position>\n'
                '        <new_tab>false</new_tab>\n        <indent>0</indent>\n        <link_settings_json>null</link_settings_json>\n      </item>\n') % (
            iid, ctype[it['kind']], html.escape(it['title'], quote=False), it['ident'], pos)
    new_mm = mm[:m.start(2)] + add + '    ' + mm[m.start(2):]
    zin = zipfile.ZipFile(src)
    with zipfile.ZipFile(dst + '.part', 'w', zipfile.ZIP_DEFLATED) as zout:
        for zi in zin.infolist():
            data = new_mm.encode('utf-8') if zi.filename == 'course_settings/module_meta.xml' else zin.read(zi.filename)
            zout.writestr(zi, data)
    os.replace(dst + '.part', dst)
    for it, _ in loose: print('placed in Instructor Use Only: %s "%s"' % (it['kind'], it['title']))


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == 'check':
        live = a[a.index('--live') + 1] if '--live' in a else None
        r = find(a[1], live)
        print('items in no module (must be 0): %d' % len(r))
        for it, where in r: print('    %s "%s" (%s): goes to %s' % (it['kind'], it['title'], it['slug'] or it['ident'], where))
        sys.exit(1 if r else 0)
    if len(a) == 3 and a[0] == 'fix': fix(a[1], a[2]); sys.exit(0)
    sys.exit(__doc__)
