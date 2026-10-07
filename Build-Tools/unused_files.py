#!/usr/bin/env python3
"""Files a Canvas package carries that nothing uses (Standards 12s, Adam 2026-10-07).

Adam: "I don't want extra stuff in packages that don't need to be used that goes for every single canvas package."
A Canvas export carries everything in the course's Files, used or not: the Blueprint's 10-07 export was 123 MB, 108 MB
of it BOAA screenshots no page used any more (the lessons load them from Cloudflare), plus folder READ ME notes, old
course-card images and the -1/-2/-3 copies Canvas makes of quiz pictures. Every package ships only files something uses.

A file under web_resources/ is USED when any other file in the package (pages, assignments, quizzes, discussions,
course settings, module_meta, another web_resources page or stylesheet) names it by its path (as written, URL-encoded
or HTML-escaped) or by its manifest resource identifier. imsmanifest.xml itself does not count: it lists every file.

    python3 unused_files.py list  <package.imscc | unzipped folder>     # one line per unused file, then a total
    python3 unused_files.py strip <in.imscc> <out.imscc>                # same package without them (manifest too)
    python3 unused_files.py dupes <package.imscc | unzipped folder>     # identical images used by the same module or quiz
    python3 unused_files.py fix   <in.imscc> <out.imscc>                # repoint those duplicates to one copy, then strip

Duplicate images (Adam 2026-10-07: "There should never ever be a duplicate image in a canvas package unless it has
to be for a different quiz or something"): two image files with the same bytes are allowed only when each copy is used
by a different module or quiz. Otherwise every reference points at one copy and the others go (fix does both).

strip copies every other entry byte for byte under its original name (zip/unzip mangle names such as a U+202F
narrow space in a macOS screenshot name), and removes each unused file's <resource> from imsmanifest.xml.
preflight.py runs find() as hard fail 12s; Canvas Preview's Report shows it.
"""
import html, os, re, sys, urllib.parse, zipfile

TEXT = ('.html', '.htm', '.xml', '.qti', '.txt', '.json', '.css', '.js')


def _norm(s):
    return urllib.parse.unquote(html.unescape(s))


def _uses(text, rel):
    """True when text names rel as a path (after a / or a quote), not just as the tail of a longer name."""
    return ('/' + rel) in text or ('"' + rel) in text or ("'" + rel) in text


def _entries(src):
    """{name: bytes-reader} for a .imscc or an unzipped folder."""
    if os.path.isdir(src):
        out = {}
        for d, _, fs in os.walk(src):
            for f in fs:
                if f.startswith('.'):
                    continue
                p = os.path.join(d, f)
                out[os.path.relpath(p, src).replace(os.sep, '/')] = (lambda p=p: open(p, 'rb').read())
        return out
    z = zipfile.ZipFile(src)
    return {n: (lambda n=n: z.read(n)) for n in z.namelist() if not n.endswith('/')}


def find(src):
    """[(name, size)] of web_resources files nothing in the package uses."""
    ent = _entries(src)
    man = ent['imsmanifest.xml']().decode('utf-8', 'ignore') if 'imsmanifest.xml' in ent else ''
    rid = {}
    for m in re.finditer(r'<(?:\w+:)?resource\b([^>]*)>(.*?)</(?:\w+:)?resource>', man, re.S):
        i = re.search(r'identifier="([^"]+)"', m.group(1))
        for h in re.findall(r'<(?:\w+:)?file\s+href="([^"]+)"', m.group(2)):
            if i:
                rid[_norm(h)] = i.group(1)
    files = [n for n in ent if n.startswith('web_resources/')]
    texts = {n: _norm(ent[n]().decode('utf-8', 'ignore')) for n in ent
             if n != 'imsmanifest.xml' and n.lower().endswith(TEXT)}
    unused = []
    for n in files:
        rel = n[len('web_resources/'):]
        i = rid.get(_norm(n), '')
        used = any((_uses(t, rel) or (i and i in t)) for k, t in texts.items() if k != n)
        if not used:
            size = len(ent[n]())
            unused.append((n, size))
    return sorted(unused)


def strip(src, out):
    drop = {n for n, _ in find(src)}
    z = zipfile.ZipFile(src)
    man = z.read('imsmanifest.xml').decode('utf-8')
    for n in drop:
        h = html.escape(n, quote=False)
        man, k = re.subn(r'\s*<(\w+:)?resource\b[^>]*>\s*<(?:\w+:)?file\s+href="%s"\s*/>\s*</(?:\w+:)?resource>' % re.escape(h), '', man)
        if k > 1:
            raise SystemExit('more than one manifest entry for %s' % n)
        # k == 0: Canvas exports ship some files (quiz picture copies) without declaring them; nothing to remove
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as w:
        for n in sorted(z.namelist(), key=lambda n: (n != 'imsmanifest.xml', n)):
            if n in drop:
                continue
            w.writestr(n, man.encode('utf-8') if n == 'imsmanifest.xml' else z.read(n))
    return drop


IMG = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.bmp', '.tif', '.tiff')


def _owners(ent):
    """{text file: owner} where owner is the quiz or module that shows it (or the file itself when in no module)."""
    mm = ent['course_settings/module_meta.xml']().decode('utf-8', 'ignore') if 'course_settings/module_meta.xml' in ent else ''
    man = ent['imsmanifest.xml']().decode('utf-8', 'ignore') if 'imsmanifest.xml' in ent else ''
    ref_mod = {}
    for mid, body in re.findall(r'<module identifier="([^"]+)">(.*?)</module>', mm, re.S):
        for r in re.findall(r'<identifierref>([^<]+)</identifierref>', body):
            ref_mod.setdefault(r, 'module ' + mid)
    file_ref = {}
    for m in re.finditer(r'<(?:\w+:)?resource\b([^>]*)>(.*?)</(?:\w+:)?resource>', man, re.S):
        i = re.search(r'identifier="([^"]+)"', m.group(1))
        for h in re.findall(r'<(?:\w+:)?file\s+href="([^"]+)"', m.group(2)):
            if i: file_ref[_norm(h)] = i.group(1)
    out = {}
    for n in ent:
        top = n.split('/')[0]
        if n.startswith('non_cc_assessments/'):
            q = os.path.basename(n).split('.')[0]; out[n] = ref_mod.get(q, 'quiz ' + q)
        elif re.fullmatch(r'g[0-9a-f]{32}', top):
            out[n] = ref_mod.get(top, 'item ' + top)          # quiz, assignment or discussion folder
        else:
            r = file_ref.get(_norm(n)); out[n] = ref_mod.get(r, n) if r else n
    return out


def dupes(src):
    """[(owner, [copies], [files])] where one module or quiz uses two or more identical images.
    Copies used by DIFFERENT modules or quizzes are allowed (Adam: "unless it has to be for a different quiz")."""
    import hashlib, collections
    ent = _entries(src); own = _owners(ent)
    texts = {n: _norm(ent[n]().decode('utf-8', 'ignore')) for n in ent
             if n != 'imsmanifest.xml' and n.lower().endswith(TEXT)}
    groups = collections.defaultdict(list)
    for n in ent:
        if n.startswith('web_resources/') and n.lower().endswith(IMG):
            groups[hashlib.sha1(ent[n]()).hexdigest()].append(n)
    bad = []
    for names in groups.values():
        if len(names) < 2: continue
        by_owner = collections.defaultdict(lambda: (set(), set()))   # owner -> (copies it uses, its files)
        for n in names:
            for k, t in texts.items():
                if _uses(t, n[len('web_resources/'):]):
                    o = own.get(k, k); by_owner[o][0].add(n); by_owner[o][1].add(k)
        for o, (copies, files) in by_owner.items():
            if len(copies) > 1: bad.append((o, sorted(copies), sorted(files)))
    return bad


def fix(src, out):
    """In each module or quiz that uses two identical images, point its files at one copy; then strip what is unused."""
    bad = dupes(src); z = zipfile.ZipFile(src); swaps = {}   # file -> {old rel: kept rel}
    for _, copies, files in bad:
        keep = min(copies, key=lambda c: (len(c), c))[len('web_resources/'):]   # the plain name, not the -1 copy
        for f in files:
            for c in copies:
                if c[len('web_resources/'):] != keep: swaps.setdefault(f, {})[c[len('web_resources/'):]] = keep
    tmp = out + '.dedupe-tmp'   # never the caller's own temp name
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as w:
        for n in z.namelist():
            data = z.read(n)
            if n in swaps:
                t = data.decode('utf-8')
                for a, b in swaps[n].items():
                    for fa, fb in ((a, b), (urllib.parse.quote(a), urllib.parse.quote(b)), (html.escape(a, quote=False), html.escape(b, quote=False))):
                        t = re.sub(r'(?<=[/"\'])' + re.escape(fa) + r'(?=["\'?#\s)<]|$)', lambda m: fb, t)
                data = t.encode('utf-8')
            w.writestr(n, data)
    d = strip(tmp, out); os.remove(tmp)
    return bad, d


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'list':
        u = find(sys.argv[2])
        for n, s in u:
            print('%8.0f KB  %s' % (s / 1e3, n))
        print('%d unused file(s), %.1f MB' % (len(u), sum(s for _, s in u) / 1e6))
    elif len(sys.argv) >= 4 and sys.argv[1] == 'strip':
        d = strip(sys.argv[2], sys.argv[3])
        print('left out %d unused file(s) -> %s' % (len(d), sys.argv[3]))
    elif len(sys.argv) >= 3 and sys.argv[1] == 'dupes':
        b = dupes(sys.argv[2])
        for o, c, _ in b: print('%s uses the same picture %d times: %s' % (o, len(c), ' = '.join(c)))
        print('%d duplicate group(s)' % len(b))
    elif len(sys.argv) >= 4 and sys.argv[1] == 'fix':
        b, d = fix(sys.argv[2], sys.argv[3])
        print('repointed %d duplicate group(s), left out %d unused file(s) -> %s' % (len(b), len(d), sys.argv[3]))
    else:
        print(__doc__)
