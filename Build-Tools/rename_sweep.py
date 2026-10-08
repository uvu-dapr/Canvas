#!/usr/bin/env python3
"""rename_sweep.py: every page and cartridge, in every DAPR course, that still points at a GitHub file by a name GitHub
no longer serves (J153, Adam 2026-10-07).

Why: on 2026-09-23 the pictures in Classes/All/DAPR_Introduce_Yourself were renamed from lowercase to Title_Case. GitHub raw
URLs are case sensitive, so every page still using the lowercase names went dead, and the Mac's case-insensitive disk hid
it. The only proof is what GitHub serves: the file list of origin/main (after a fetch), exact case. Never the stale
".../apps/GitHub copy/Canvas".

    python3 rename_sweep.py                       # every course: current packages, next-term templates, live exports
    python3 rename_sweep.py --old Classes/All/DAPR_Introduce_Yourself/preview_adjust_size.png   # one old name (file or
                                                  # folder, any case): every reference to it
    python3 rename_sweep.py --out report.md       # also write the report

For each https://raw.githubusercontent.com/uvu-dapr/Canvas/main/... address it reports one of:
  case       GitHub has the file only under another case: the address that works
  renamed    git recorded a rename: the newest name
  unpushed   the file is in the GitHub folder on this Mac but not on GitHub yet (push it)
  missing    no such file on GitHub or on this Mac
Reads only; changes nothing.
"""
import os, re, sys, glob, html, zipfile, subprocess, urllib.parse, collections

REPO = "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas"
COURSES = "/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses"
RAW = "https://raw.githubusercontent.com/uvu-dapr/Canvas/main/"
URL_RE = re.compile(r"https://raw\.githubusercontent\.com/uvu-dapr/Canvas/main/[^\"'<>\s)]+")


def git(*a):
    return subprocess.run(["git", "-C", REPO] + list(a), capture_output=True, text=True).stdout


def truth():
    subprocess.run(["git", "-C", REPO, "fetch", "-q", "origin"], capture_output=True)
    served = set(git("ls-tree", "-r", "--name-only", "origin/main").splitlines())
    local = set(git("ls-files").splitlines()) | set(git("ls-files", "--others", "--exclude-standard").splitlines())
    step = {}
    for line in reversed(git("log", "--all", "-M", "--diff-filter=R", "--name-status", "--format=%H").splitlines()):
        f = line.split("\t")
        if len(f) == 3 and f[0].startswith("R"):
            step[f[1]] = f[2]
    renames = {}
    for k in step:
        p, seen = k, set()
        while p in step and p not in seen:
            seen.add(p); p = step[p]
        renames[k] = p
    return served, local, renames


def packages():
    """Per class: the newest package of each kind (Full, template, Update), the newest Canvas export, and the Blueprint's"""
    out = []
    for d in sorted(glob.glob(COURSES + "/*/Canvas/Canvas Templates/-Canvas Entire Course")):
        cls = d.split("/")[-4]
        if cls.startswith("Archive") or "/Archive/" in d:
            continue
        files = [f for f in glob.glob(d + "/*.imscc")]
        def ver(f):
            m = re.search(r"-v(\d+)", os.path.basename(f)); return int(m.group(1)) if m else 0
        def newest(fs, key=os.path.getmtime):
            return [max(fs, key=key)] if fs else []
        fulls = [f for f in files if re.search(r"-Full\b|-Template\b", os.path.basename(f))]   # the name, never the "Canvas Templates" folder
        # a Canvas export has no version number; a package built from one ("...export-v13-Full") is a package
        exports = [f for f in files if "export" in os.path.basename(f).lower() and not re.search(r"-v\d+", os.path.basename(f))]
        picks = []
        terms = set(m.group(0) for f in fulls for m in [re.search(r"(Fall|Spring|Summer)-\d{4}", os.path.basename(f))] if m)
        for term in sorted(terms):
            picks += newest([f for f in fulls if term in os.path.basename(f)], key=ver)
        picks += newest([f for f in fulls if not re.search(r"(Fall|Spring|Summer)-\d{4}", os.path.basename(f))], key=ver)
        # the newest export by the date in its name (a later download of an older export must not win)
        picks += newest(exports, key=lambda f: ((re.search(r"\d{4}-\d{2}-\d{2}", os.path.basename(f)) or re.search("", "")).group(0), os.path.getmtime(f)))
        out += [(cls, f) for f in sorted(set(picks))]
    return out


def titled(z, name, text):
    m = re.search(r"<title>(.*?)</title>", text, re.S)
    return html.unescape(m.group(1)).strip() if m else name


def scan(served, local, renames, old=None):
    lower = collections.defaultdict(list)
    for p in served:
        lower[p.lower()].append(p)
    found = []
    oldl = old.lower().strip("/") if old else None
    for cls, pkg in packages():
        try:
            z = zipfile.ZipFile(pkg)
        except Exception:
            continue
        for n in z.namelist():
            if not n.endswith((".html", ".xml", ".qti")) or n.startswith("web_resources/"):
                continue
            t = z.read(n).decode("utf-8", "ignore")
            urls = set(html.unescape(u).split('"')[0] for u in URL_RE.findall(html.unescape(t)))
            for u in sorted(urls):
                rel = urllib.parse.unquote(u[len(RAW):].split("?")[0].split("#")[0])
                if oldl is not None:
                    if not (rel.lower() == oldl or rel.lower().startswith(oldl + "/")):
                        continue
                    if rel in served and rel.lower() != oldl:
                        continue
                if rel in served and oldl is None:
                    continue
                if rel.lower() in lower and rel not in served:
                    kind, fix = "case", lower[rel.lower()][0]
                elif rel in renames and renames[rel] in served:
                    kind, fix = "renamed", renames[rel]
                elif rel in local:
                    kind, fix = "unpushed", rel
                elif rel in served:
                    kind, fix = "ok", rel
                else:
                    kind, fix = "missing", ""
                found.append((cls, os.path.basename(pkg), titled(z, n, t), n, u, kind, fix))
    return found


def report(found, old=None):
    md = ["# Rename sweep%s" % (": " + old if old else ""), "",
          "Every GitHub address in the newest packages, templates and Canvas exports of every DAPR course and the Blueprint, "
          "checked against what GitHub serves (origin/main, exact case). Reads only.", ""]
    by = collections.Counter(f[5] for f in found)
    md.append("Totals: " + (", ".join("%s %d" % (k, v) for k, v in sorted(by.items())) or "nothing found") + ".")
    md.append("")
    last = None
    for cls, pkg, title, n, u, kind, fix in sorted(found):
        if (cls, pkg) != last:
            md += ["", "## %s: %s" % (cls, pkg), ""]
            last = (cls, pkg)
        line = "- **%s** (%s) `%s`" % (kind, title, u[len(RAW):])
        if kind in ("case", "renamed"):
            line += " -> `%s`" % fix
        md.append(line)
    return "\n".join(md) + "\n"


if __name__ == "__main__":
    old = sys.argv[sys.argv.index("--old") + 1] if "--old" in sys.argv else None
    served, local, renames = truth()
    found = scan(served, local, renames, old)
    text = report(found, old)
    if "--out" in sys.argv:
        open(sys.argv[sys.argv.index("--out") + 1], "w").write(text)
    print(text[:6000])
