#!/usr/bin/env python3
"""
deck_images.py: SUPERSEDED the same day by deck_pair.py (Linked and Embedded decks, Standards 8). Kept for its history; do not run.

deck_images.py: give every slide picture a file of its own and link the deck to it (Adam, 2026-09-30).

"All the PowerPoint should point to the images and reference them, so I can update the images in place and have the
PowerPoint images update." Each picture on a slide is written to its module's Presentations/Images folder (the name of
an identical file already there, or in the module's GitHub images, is reused; otherwise <Deck>-slideNN-k.<ext>), and the
slide's picture gets a link to that file beside its embedded copy (PowerPoint's "Insert and Link"): PowerPoint shows the
file, and falls back to the embedded copy when it can't read it (tested 2026-09-30: with folder access refused, the
export used the embedded picture). PowerPoint is sandboxed, so it asks once for access to the folder: grant it the
Canvas Links folder and every deck's pictures follow their files.

    python3 deck_images.py link <deck.pptx | a Presentations folder | a course's Canvas Links folder> [--github <Classes/<Course_Folder>>] [--dry]

Never: a deck open in PowerPoint (its ~$ lock file is present), decks in Archive, _unused or PDF. The deck before
linking is kept in Presentations/Archive as "<name> (before linked pictures <date>).pptx". Pictures in slide layouts
and masters (backgrounds, logos) stay embedded.
"""
import sys, os, re, zipfile, hashlib, urllib.parse, datetime, json

def sha(b): return hashlib.sha1(b).hexdigest()

def decks(target):
    if target.lower().endswith(".pptx"): return [target]
    out = []
    for root, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if d not in ("Archive", "_unused", "PDF", "Images")]
        if os.path.basename(root) != "Presentations": continue
        out += [os.path.join(root, f) for f in files if f.lower().endswith(".pptx") and not f.startswith("~$")]
    return sorted(out)

def index(folder):
    """sha1 -> file name for the pictures already in a folder."""
    out = {}
    if os.path.isdir(folder):
        for f in os.listdir(folder):
            p = os.path.join(folder, f)
            if os.path.isfile(p) and os.path.splitext(f)[1].lower() in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".tif", ".tiff", ".bmp", ".emf", ".wmf"):
                out.setdefault(sha(open(p, "rb").read()), f)
    return out

def open_in_powerpoint():
    """Names of the decks PowerPoint has open (a deck can be open without a ~$ lock file)."""
    import subprocess
    try:
        r = subprocess.run(["osascript", "-e", 'if application "Microsoft PowerPoint" is running then tell application "Microsoft PowerPoint" to get name of every presentation'],
                           capture_output=True, text=True, timeout=20)
        return {x.strip() for x in r.stdout.split(",") if x.strip()}
    except Exception:
        return set()
OPEN = None

def link_deck(deck, github=None, dry=False):
    global OPEN
    if OPEN is None: OPEN = open_in_powerpoint()
    pres = os.path.dirname(deck); images = os.path.join(pres, "Images"); stem = os.path.splitext(os.path.basename(deck))[0]
    if os.path.exists(os.path.join(pres, "~$" + os.path.basename(deck))) or os.path.basename(deck) in OPEN:
        return dict(deck=deck, skipped="open in PowerPoint (close it, then run again)")
    module = os.path.basename(os.path.dirname(pres))
    have = index(images)
    gh = index(os.path.join(github, module)) if github else {}
    z = zipfile.ZipFile(deck); infos = z.infolist(); data = {i.filename: z.read(i.filename) for i in infos}; z.close()
    linked = written = reused = 0
    for n in sorted(data):
        m = re.match(r"ppt/slides/_rels/slide(\d+)\.xml\.rels$", n)
        if not m: continue
        slide = int(m.group(1)); rels = data[n].decode("utf-8"); sx = "ppt/slides/slide%d.xml" % slide
        if sx not in data: continue
        body = data[sx].decode("utf-8")
        new_rels = []; k = 0
        for r in re.finditer(r'<Relationship Id="([^"]+)" Type="[^"]*/image" Target="([^"]+)"(?![^>]*TargetMode="External")[^>]*/>', rels):
            rid, target = r.group(1), r.group(2)
            if not re.search(r'<a:blip r:embed="%s"(?![^>]*r:link)' % re.escape(rid), body): continue
            media = os.path.normpath(os.path.join("ppt/slides", target)).replace("\\", "/")
            if media not in data: continue
            blob = data[media]; h = sha(blob); ext = os.path.splitext(media)[1].lower()
            k += 1
            if h in have: name = have[h]; reused += 1
            else:
                name = gh.get(h) or "%s-slide%02d-%d%s" % (stem, slide, k, ext)
                base, e2 = os.path.splitext(name); j = 2
                while os.path.exists(os.path.join(images, name)) and sha(open(os.path.join(images, name), "rb").read()) != h:
                    name = "%s-%d%s" % (base, j, e2); j += 1
                if not dry:
                    os.makedirs(images, exist_ok=True)
                    if not os.path.exists(os.path.join(images, name)): open(os.path.join(images, name), "wb").write(blob); written += 1
                else: written += 1
                have[h] = name
            lid = "rIdLink%d" % k
            while lid in rels: lid += "x"
            url = "file://" + urllib.parse.quote(os.path.abspath(os.path.join(images, name)))
            new_rels.append('<Relationship Id="%s" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="%s" TargetMode="External"/>' % (lid, url))
            body = re.sub(r'<a:blip r:embed="%s"(?![^>]*r:link)' % re.escape(rid), '<a:blip r:embed="%s" r:link="%s"' % (rid, lid), body)
            linked += 1
        if new_rels:
            data[n] = rels.replace("</Relationships>", "".join(new_rels) + "</Relationships>").encode("utf-8")
            data[sx] = body.encode("utf-8")
    if dry or not linked:
        return dict(deck=deck, linked=linked, written=written, reused=reused, dry=dry)
    arch = os.path.join(pres, "Archive"); os.makedirs(arch, exist_ok=True)
    keep = os.path.join(arch, "%s (before linked pictures %s).pptx" % (stem, datetime.date.today().isoformat()))
    if not os.path.exists(keep):
        import shutil; shutil.copy2(deck, keep)
    tmp = deck + ".linking"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as o:
        for i in infos: o.writestr(i, data[i.filename])
    os.replace(tmp, deck)
    return dict(deck=deck, linked=linked, written=written, reused=reused, kept=keep)

if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 2 or a[0] != "link": print(__doc__); sys.exit(2)
    gh = a[a.index("--github") + 1] if "--github" in a else None
    res = [link_deck(d, gh, "--dry" in a) for d in decks(a[1])]
    tot = dict(decks=len(res), skipped=sum(1 for r in res if r.get("skipped")), linked=sum(r.get("linked", 0) for r in res), written=sum(r.get("written", 0) for r in res), reused=sum(r.get("reused", 0) for r in res))
    print(json.dumps(dict(total=tot, decks=res), indent=1))
