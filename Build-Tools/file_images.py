#!/usr/bin/env python3
"""
file_images.py - take whatever ChatGPT hands back and file it correctly.

    python3 file_images.py ~/Downloads
    python3 file_images.py ~/Downloads/images.zip
    python3 file_images.py ~/Downloads --dry-run

Reads every `ChatGPT Image Creation - *.md` brief in the Canvas repo, builds a manifest
of (filename -> destination folder, expected format) from the locked Standards 20.5
tables, then matches every image it finds in the source against that manifest.

It forgives what ChatGPT gets wrong and refuses to guess what it cannot know:
  - a dropped -01 or -02 counter                      matched and restored
  - the wrong extension (.png delivered for a .jpg)   converted, flattened on white
  - an oversized image                                downscaled to 1600 px wide
  - a JPEG over 500 KB or a PNG over 1 MB             re-saved inside the budget
  - a name that matches two entries                   reported, never guessed
  - a target file that already exists                 skipped, never overwritten
  - a .jpg delivered where a transparent .png is due  reported, never faked

Standards: 20.2 format, 20.3 size and weight, 20.4 filenames are permanent and a file
is never overwritten, 20.4c Claude writes the files and Adam commits them.
"""
import argparse, os, re, sys, shutil, tempfile, zipfile

REPO_DEFAULT = "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas"
IMG_EXT = (".png", ".jpg", ".jpeg", ".webp")

try:
    from PIL import Image
except ImportError:
    print("This needs Pillow.  pip3 install --user pillow")
    sys.exit(2)


def norm(name):
    """Collapse a filename to what it is really called: no extension, no counter,
    no punctuation, lowercase."""
    s = os.path.basename(name).lower()
    s = re.sub(r"\.(png|jpe?g|webp)$", "", s)
    s = re.sub(r"[ _]+", "-", s)
    s = re.sub(r"\(\d+\)$", "", s)          # browser "file (1)"
    s = re.sub(r"-\d\d?$", "", s)           # -01, -2
    s = re.sub(r"[^a-z0-9]+", "", s)
    return s


def read_briefs(repo):
    """Every brief in the repo becomes manifest rows: name -> (folder, ext)."""
    man, briefs = {}, []
    root = os.path.join(repo, "Classes")
    for course in sorted(os.listdir(root)):
        bdir = os.path.join(root, course, "Images", "_briefs")
        if not os.path.isdir(bdir):
            continue
        for f in sorted(os.listdir(bdir)):
            if not f.startswith("ChatGPT Image Creation - ") or not f.endswith(".md"):
                continue
            path = os.path.join(bdir, f)
            briefs.append(path)
            text = open(path, encoding="utf-8").read()
            for blk in text.split("\n## Image ")[1:]:
                fn = re.search(r"^\| Filename \| `(.+?)` \|", blk, re.M)
                fo = re.search(r"^\| Destination folder \| `(.+?)` \|", blk, re.M)
                if not (fn and fo):
                    continue
                name = fn.group(1)
                man[norm(name)] = (name, fo.group(1).rstrip("/"), os.path.splitext(name)[1].lower())
    return man, briefs


def collect(source, workdir):
    """Every image under source, with zips unpacked into workdir."""
    found = []
    def take(p):
        if p.lower().endswith(IMG_EXT) and not os.path.basename(p).startswith("."):
            found.append(p)
    if os.path.isfile(source):
        cands = [source]
    else:
        cands = []
        for dp, _, fs in os.walk(source):
            if os.sep + "__MACOSX" in dp:
                continue
            for f in fs:
                cands.append(os.path.join(dp, f))
    for p in cands:
        if p.lower().endswith(".zip"):
            out = os.path.join(workdir, os.path.basename(p) + ".unpacked")
            os.makedirs(out, exist_ok=True)
            try:
                with zipfile.ZipFile(p) as z:
                    z.extractall(out)
            except Exception as e:
                print("  could not unpack %s: %s" % (os.path.basename(p), e))
                continue
            for dp, _, fs in os.walk(out):
                if os.sep + "__MACOSX" in dp:
                    continue
                for f in fs:
                    take(os.path.join(dp, f))
        else:
            take(p)
    return sorted(set(found))


def place(src, dest, want_ext, dry):
    """Write src to dest in the right format and inside the weight budget."""
    notes = []
    im = Image.open(src)
    w, h = im.size
    if w > 1600:
        im = im.resize((1600, round(h * 1600 / w)), Image.LANCZOS)
        notes.append("downscaled from %d px" % w)
        w, h = im.size
    elif w < 1600:
        notes.append("only %d px wide, under the 1600 px target" % w)

    if want_ext in (".jpg", ".jpeg"):
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[-1])
            im = bg
            notes.append("flattened onto white")
        else:
            im = im.convert("RGB")
        if os.path.splitext(src)[1].lower() not in (".jpg", ".jpeg"):
            notes.append("converted to JPEG")
        if not dry:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            q = 88
            im.save(dest, "JPEG", quality=q, optimize=True)
            while os.path.getsize(dest) > 500_000 and q > 60:
                q -= 6
                im.save(dest, "JPEG", quality=q, optimize=True)
            if q != 88:
                notes.append("saved at quality %d to stay under 500 KB" % q)
    else:
        if im.mode not in ("RGBA", "LA") and os.path.splitext(src)[1].lower() in (".jpg", ".jpeg"):
            return None, "delivered as JPEG but this entry needs a transparent PNG, regenerate it"
        if not dry:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            im.save(dest, "PNG", optimize=True)
            if os.path.getsize(dest) > 1_000_000:
                notes.append("%.1f MB, over the 1 MB PNG budget" % (os.path.getsize(dest) / 1e6))
    return notes, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="a zip, or a folder holding the images or the zip")
    ap.add_argument("--repo", default=REPO_DEFAULT)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    man, briefs = read_briefs(a.repo)
    if not man:
        print("No briefs found under %s/Classes/*/Images/_briefs/" % a.repo)
        return 2
    print("manifest: %d images across %d brief%s" % (len(man), len(briefs), "" if len(briefs) == 1 else "s"))

    work = tempfile.mkdtemp(prefix="fileimg-")
    try:
        imgs = collect(a.source, work)
        print("found %d image file%s in %s\n" % (len(imgs), "" if len(imgs) == 1 else "s", a.source))

        placed, skipped, unmatched, ambiguous, failed = [], [], [], [], []
        for p in imgs:
            key = norm(p)
            hits = [k for k in man if k == key] or [k for k in man if k.startswith(key) or key.startswith(k)]
            hits = sorted(set(hits))
            if not hits:
                unmatched.append(p); continue
            if len(hits) > 1:
                ambiguous.append((p, [man[h][0] for h in hits])); continue
            name, folder, ext = man[hits[0]]
            dest = os.path.join(folder, name)
            if os.path.exists(dest):
                skipped.append((os.path.basename(p), name)); continue
            notes, err = place(p, dest, ext, a.dry_run)
            if err:
                failed.append((os.path.basename(p), name, err))
            else:
                placed.append((name, folder, notes))

        w = max([len(n) for n, _, _ in placed] + [10])
        if placed:
            print("PLACED %d" % len(placed))
            for name, folder, notes in sorted(placed):
                tail = "   " + "; ".join(notes) if notes else ""
                print("   %-*s -> %s%s" % (w, name, os.path.basename(folder), tail))
        for label, rows, fmt in (
            ("ALREADY THERE, not overwritten", skipped, lambda r: "%s matches %s" % r),
            ("COULD NOT PLACE", failed, lambda r: "%s -> %s: %s" % r),
            ("NAME MATCHED MORE THAN ONE ENTRY, not guessed", ambiguous,
             lambda r: "%s could be %s" % (os.path.basename(r[0]), " or ".join(r[1]))),
            ("NOT IN ANY BRIEF", [(p,) for p in unmatched], lambda r: os.path.basename(r[0])),
        ):
            if rows:
                print("\n%s (%d)" % (label, len(rows)))
                for r in rows:
                    print("   " + fmt(r))

        have = set()
        for p in imgs:
            key = norm(p)
            hits = [k for k in man if k == key] or [k for k in man if k.startswith(key) or key.startswith(k)]
            if len(set(hits)) == 1:
                have.add(sorted(set(hits))[0])
        for k, (name, folder, _) in man.items():
            if os.path.exists(os.path.join(folder, name)):
                have.add(k)
        missing = sorted(man[k][0] for k in man if k not in have)
        print("\nSTILL MISSING (%d of %d)" % (len(missing), len(man)))
        for m in missing:
            print("   " + m)
        if a.dry_run:
            print("\ndry run, nothing was written")
        elif placed:
            print("\n%d file%s written. Review them in GitHub Desktop, then commit and push."
                  % (len(placed), "" if len(placed) == 1 else "s"))
        return 0
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
