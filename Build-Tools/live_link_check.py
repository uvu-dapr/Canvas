#!/usr/bin/env python3
"""Broken GitHub picture links on a live course, and where each picture went (Adam, 2026-10-02).

    python3 live_link_check.py <Canvas export .imscc> [--md OUT.md]

Reads every page, assignment, discussion and quiz in a Canvas export, finds each raw.githubusercontent.com picture link
whose file is no longer in the repo (a rename or move after the page was built, such as the 2026-09-23 renaming that
retired Images/<topic>/<slug>-01.jpg), and finds the file's new path from git's rename history. Prints one line per
broken link, grouped by page, with the new raw URL to paste. Pages-only Full packages never update assignments, so an
assignment's links are fixed by pasting the corrected HTML (or bringing the graded work in, Standards 16b).
"""
import os, re, sys, zipfile, subprocess, urllib.parse, collections, html

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = "https://raw.githubusercontent.com/uvu-dapr/Canvas/main/"


def renames():
    """{old path: newest path} from every rename git recorded, followed to the end of the chain."""
    out = subprocess.run(["git", "-C", REPO, "log", "--all", "-M", "--diff-filter=R", "--name-status", "--format=%H"],
                         capture_output=True, text=True).stdout
    step = {}
    for line in reversed(out.splitlines()):              # oldest first, so a later rename wins
        parts = line.split("\t")
        if len(parts) == 3 and parts[0].startswith("R"): step[parts[1]] = parts[2]
    def last(p, seen=()):
        return last(step[p], seen + (p,)) if p in step and p not in seen else p
    return {p: last(p) for p in step}


def title_of(text, name):
    m = re.search(r"<title>(.*?)</title>", text, re.S)
    return html.unescape(m.group(1)).strip() if m else os.path.basename(name)


def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    z = zipfile.ZipFile(sys.argv[1]); moved = renames()
    pages = collections.OrderedDict(); total = set()
    for n in sorted(z.namelist()):
        if not n.endswith((".html", ".xml")) or n.startswith("course_settings/"): continue
        t = z.read(n).decode("utf-8", "ignore")
        for u in sorted(set(re.findall(r'https://raw\.githubusercontent\.com/uvu-dapr/Canvas/main/[^"\'\s)<>]+', t))):
            rel = urllib.parse.unquote(html.unescape(u)[len(RAW):])
            total.add(u)
            if os.path.exists(os.path.join(REPO, rel)): continue
            new = moved.get(rel)
            ok = new and os.path.exists(os.path.join(REPO, new))
            pages.setdefault((n, title_of(t, n)), []).append((u, RAW + urllib.parse.quote(new) if ok else ""))
    broken = sum(len(v) for v in pages.values()); found = sum(1 for v in pages.values() for _, nu in v if nu)
    lines = ["# Broken GitHub picture links: %s" % os.path.basename(sys.argv[1]), "",
             "%d picture links, %d broken on %d page(s); %d have a new path in git, %d were removed." % (len(total), broken, len(pages), found, broken - found), ""]
    for (n, title), rows in pages.items():
        lines += ["## %s" % title, "", "`%s`" % n, ""]
        for old, new in rows:
            lines.append("- old: %s" % old)
            lines.append("  new: %s" % (new or "(no longer in the repo: pick a replacement)"))
        lines.append("")
    text = "\n".join(lines) + "\n"
    if "--md" in sys.argv: open(sys.argv[sys.argv.index("--md") + 1], "w").write(text)
    print(lines[2])
    if "--md" not in sys.argv: print(text)


if __name__ == "__main__":
    main()
