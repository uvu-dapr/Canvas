#!/usr/bin/env python3
"""Where every slide picture came from: ChatGPT, a Claude stand-in, a Canvas picture, or the old decks.

Fingerprints every picture in each module's Presentations/Images folder (CloudFlare/Canvas Links) and matches it against
ChatGPT's own output (~/.codex/generated_images and Canvas Preview's work-* folders), Claude's stand-in drawings
(Canvas Preview/Images/temp-*.png) and the Canvas repo's pictures. A picture in a new deck's picture slot
(placeholder-<slide>-1.png in a Presentations brief) is a Claude stand-in unless it matches ChatGPT: those slots were
only ever filled by the two, and some stand-in drawings are no longer on disk to match.

Writes:
  Build-Tools/slide_picture_sources.json   {path: {"src", "slot"}}; image_work_list.py reads it for Part D
  Notes and Briefs/<date> Slide Picture Sources - All Classes.md
Adam, 2026-10-01: "are all the images to each of the PowerPoints made with ChatGPT?"
"""
import os, re, glob, json, subprocess, collections, datetime as dt

HOME = "/Users/adamwolson/Library/CloudStorage/Dropbox"
REPO = HOME + "/apps/GitHub/Canvas"
CLASSES = REPO + "/Classes"
LINKS = HOME + "/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links"
NB = HOME + "/Miscellaneous/4-Work/UVU/UVU Courses/Claude outputs/Notes and Briefs"
APP = os.path.expanduser("~/Library/Application Support/Canvas Preview/Images")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_JSON = HERE + "/slide_picture_sources.json"
PICS = (".png", ".jpg", ".jpeg", ".webp")
CLASS_ORDER = ["3340", "2020", "2000", "2255", "3345", "2010", "3255"]   # Adam's class order
CLASS_NAME = {"3340": "Spatial Audio I", "2020": "Core Mixing", "2000": "Digital Audio Essentials", "2255": "Audio Hardware I",
              "3345": "Spatial Audio II", "2010": "Core Recording", "3255": "Audio Hardware II"}

def tool():
    """Builds picture_fingerprint.swift once (again when the source is newer)."""
    src = HERE + "/picture_fingerprint.swift"
    out = os.path.expanduser("~/Library/Caches/canvas-build-tools/picture_fingerprint")
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        subprocess.run(["swiftc", "-O", src, "-o", out], check=True)
    return out

def files(*roots, where=lambda p: True):
    out = []
    for r in roots:
        for d, _, fs in os.walk(r):
            out += [os.path.join(d, f) for f in fs if f.lower().endswith(PICS) and where(os.path.join(d, f))]
    return sorted(set(out))

def prints(paths):
    """{path: 64-bit difference hash} for each picture that opens."""
    if not paths: return {}
    r = subprocess.run([tool()], input="\n".join(paths) + "\n", capture_output=True, text=True)
    return {p: int(h, 16) for h, _, _, p in (l.split("\t", 3) for l in r.stdout.splitlines() if l.count("\t") >= 3)}

def nearest(h, pool, limit=5):
    if h in pool: return pool[h]
    best = None
    for ph, p in pool.items():
        d = bin(h ^ ph).count("1")
        if d <= limit and (best is None or d < best[0]): best = (d, p)
    return best[1] if best else None

def norm(s): return re.sub(r"[^a-z0-9]+", " ", s.lower().replace("'", "").replace("’", "")).split()

slides = prints(files(LINKS, where=lambda p: "/Presentations/Images/" in p))
gpt = {h: p for p, h in prints(files(os.path.expanduser("~/.codex/generated_images")) + files(APP, where=lambda p: "/work-" in p)).items()}
claude = {h: p for p, h in prints(glob.glob(APP + "/temp-*.png")).items()}
canvas_prints = prints(files(CLASSES))
canvas = {h: p for p, h in canvas_prints.items()}

def canvas_source(p, h):
    """The Canvas picture a slide picture copies: the closest fingerprint (3 of 64 bits or fewer), same module first, then
    same class; None when two different files tie, so a doubtful match is never relinked."""
    cls_dir = re.search(r"Canvas Links/(DAPR-[^/]+)/([^/]+)/", p)
    hits = [(bin(h ^ ph).count("1"), cp) for cp, ph in canvas_prints.items() if bin(h ^ ph).count("1") <= 3]
    if not hits: return None
    def rank(x):
        d, cp = x
        return (d, 0 if cls_dir and "/%s/%s/" % cls_dir.groups() in cp else 1 if cls_dir and "/%s/" % cls_dir.group(1) in cp else 2)
    hits.sort(key=rank)
    if len(hits) > 1 and rank(hits[0]) == rank(hits[1]) and open(hits[0][1], "rb").read() != open(hits[1][1], "rb").read(): return None
    return hits[0][1]

src = {}
for p, h in slides.items():
    kind = "ChatGPT" if nearest(h, gpt) else "Claude stand-in" if nearest(h, claude) else "Canvas picture" if nearest(h, canvas) else "Old deck picture"
    src[p] = {"src": kind, "slot": "", "canvas": (canvas_source(p, h) or "") if kind == "Canvas picture" else ""}

# New decks' picture slots: the deck's picture is "<deck>-<first words of the alt text>"
for bf in glob.glob(CLASSES + "/*/_briefs/ChatGPT Image Creation - DAPR * Presentations.md"):
    for part in re.split(r"^(?=## Image )", open(bf).read(), flags=re.M):
        f = dict((k, v.strip().strip("`")) for k, v in re.findall(r"^\| (Filename|Destination folder|Used on|Alt text) \| (.*?) \|$", part, re.M))
        if "empty picture slot" not in f.get("Used on", ""): continue
        deck = re.search(r"([^`/]+)\.pptx", f["Used on"]).group(1)
        alt, best = norm(f.get("Alt text", "")), None
        for p in glob.glob(glob.escape(f["Destination folder"].rstrip("/")) + "/" + glob.escape(deck) + "-*"):
            words = norm(os.path.basename(p)[len(deck) + 1:].rsplit(".", 1)[0])
            if words and alt[:len(words)] == words and (best is None or len(words) > best[0]): best = (len(words), p)
        if best and best[1] in src:
            s = src[best[1]]
            s["slot"] = f["Filename"]
            if s["src"] != "ChatGPT": s["src"] = "Claude stand-in"

json.dump(src, open(OUT_JSON, "w"), indent=1, sort_keys=True)

# ---------------- report ----------------
def cls(p): return re.search(r"Canvas Links/DAPR-(\d{4})", p).group(1)
cols = ["ChatGPT", "Claude stand-in", "Canvas picture", "Old deck picture"]
t = collections.Counter((cls(p), s["src"]) for p, s in src.items())
today = dt.date.today().isoformat()
L = ["# Slide Picture Sources - All Classes", "",
     "%s. Every picture in each module's `Presentations/Images` folder under CloudFlare/Canvas Links (%s files), matched by fingerprint "
     "against ChatGPT's own output, Claude's stand-in drawings and the Canvas repo's pictures. Built by Build-Tools/slide_picture_sources.py." % (today, format(len(src), ",")), "",
     "- **ChatGPT:** matches an image ChatGPT generated.",
     "- **Claude stand-in:** a temporary drawing by Claude (Standards 20.1 exception). Each one still needs a ChatGPT image; the ChatGPT Image Work List (Part D) names it as the old image.",
     "- **Canvas picture:** a copy of a picture on the Canvas pages (photos, paid images, diagrams, screenshots). Some were made earlier in the ChatGPT app, which leaves no record to match.",
     "- **Old deck picture:** matches nothing: pictures from the original decks (web photos, product shots, screenshots).", "",
     "| Class | " + " | ".join(cols) + " | Total |", "|---|" + "---:|" * (len(cols) + 1)]
for c in CLASS_ORDER:
    L.append("| DAPR %s %s | " % (c, CLASS_NAME[c]) + " | ".join(str(t[(c, k)]) for k in cols) + " | %d |" % sum(t[(c, k)] for k in cols))
L.append("| **All** | " + " | ".join("**%d**" % sum(t[(c, k)] for c in CLASS_ORDER) for k in cols) + " | **%d** |" % len(src))
stand = sorted((p for p, s in src.items() if s["src"] == "Claude stand-in"), key=lambda p: (CLASS_ORDER.index(cls(p)), p))
L += ["", "## Claude stand-ins in the decks now (%d)" % len(stand), ""]
mod = None
for p in stand:
    m = re.search(r"Canvas Links/[^/]+/([^/]+)/", p).group(1)
    if m != mod: L += ["", "### DAPR %s: %s" % (cls(p), m.replace("__", ": ").replace("_", " ")), ""]; mod = m
    L.append("- `%s`%s" % (p, " (ChatGPT saves `%s`)" % src[p]["slot"] if src[p]["slot"] else ""))
open("%s/%s Slide Picture Sources - All Classes.md" % (NB, today), "w").write("\n".join(L) + "\n")
print("%d slide pictures: %s" % (len(src), ", ".join("%s %d" % (k, sum(t[(c, k)] for c in CLASS_ORDER)) for k in cols)))
