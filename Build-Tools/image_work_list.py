#!/usr/bin/env python3
"""ChatGPT Image Work List for every DAPR class: one Markdown list plus an HTML checklist.

Reads the image briefs, checks every file on disk, and lists only what is still open:
  A  wrong facts in Canvas pictures   (_briefs/ChatGPT Image Prompts - ALL COURSES Priorities.md, Tier 2 items 08 to 29)
  B  outline page topic images        (Schedule_Banner.jpg for 3340, 3255, 3345; prompts below)
  C  placeholders on Canvas pages     (_briefs/ChatGPT Image Prompts - ALL COURSES TO DO.md)
  D  new PowerPoint pictures          (each class's _briefs/ChatGPT Image Creation - DAPR #### Presentations.md)
plus two sections that are not ChatGPT work (Needs Adam captures, live pictures that were only renamed).

Every item carries Standards 20.5b's five details together: Action (REPLACE or ADD NEW), file name,
full save path, the old image (path, thumbnail in the HTML, what is wrong) and what to create.

Canvas Preview's Images to Fix page (Images mode, ⌥⇧⌘I) runs this tool, so the app and these files always agree:
  --extra FILE   what only the app knows, as a JSON list: {"kind": "canvasNote" | "deckNote" | "fixNote", "path", "note",
                 "source"}, {"kind": "temp", "path", "title", "prompt", "width", "height", "made"},
                 {"kind": "keep", "path", "backup"} (made in the app, waiting for Adam's review) and {"kind": "done", "path"}
  --json FILE    writes the list as JSON for the app and nothing else
  --name NAME    file names: "<NAME> - All Classes.md/.html" and "<NAME> - For ChatGPT.md" (Save Fix List for ChatGPT)

Usage:  python3 image_work_list.py [--rev N] [--name NAME] [--extra FILE] [--json FILE]
Writes into UVU Courses/Claude outputs/Notes and Briefs/ (the 2026-09-30 list by default; a re-check bumps --rev).
"""
import os, re, sys, html, json, subprocess, datetime as dt
from urllib.parse import quote

HOME = "/Users/adamwolson/Library/CloudStorage/Dropbox"
CLASSES = HOME + "/apps/GitHub/Canvas/Classes"
COURSES = HOME + "/Miscellaneous/4-Work/UVU/UVU Courses"
NB = COURSES + "/Claude outputs/Notes and Briefs"
def arg(name, default=None): return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default
NAME = arg("--name", "2026-09-30 ChatGPT Image Work List")
OUT_MD = NB + "/" + NAME + " - All Classes.md"
OUT_HTML = NB + "/" + NAME + " - All Classes.html"
REV = arg("--rev", "2")
JSON_OUT = arg("--json")
EXTRA = json.load(open(arg("--extra"))) if arg("--extra") else []
KEEP = {e["path"]: e.get("backup", "") for e in EXTRA if e.get("kind") == "keep"}   # made in the app, waiting for review
DONE = {e["path"] for e in EXTRA if e.get("kind") == "done"}                          # approved in the app

def ts(s): return dt.datetime.strptime(s, "%Y-%m-%d %H:%M").timestamp()
CUT_A = ts("2026-09-25 05:00")   # Tier 2 is done when its file changed after this
CUT_C = ts("2026-09-24 17:00")   # a placeholder is done when its file changed after this
FIXES = CLASSES + "/_briefs/Image Fixes For Later - DAPR All Courses.md"
CUT_E = os.path.getmtime(FIXES)

CLASS_ORDER = ["3340", "2020", "2000", "2255", "3345", "2010", "3255"]   # Adam's class order
CLASS_NAME = {"2000": "DAPR 2000 - Digital Audio Essentials", "2010": "DAPR 2010 - Core Recording",
              "2020": "DAPR 2020 - Core Mixing", "2255": "DAPR 2255 - Audio Hardware I",
              "3255": "DAPR 3255 - Audio Hardware II", "3340": "DAPR 3340 - Spatial Audio I",
              "3345": "DAPR 3345 - Spatial Audio II", "All": "All classes (shared Classes/All)"}
CF = {"2000": "DAPR-2000--Digital_Audio_Essentials", "2010": "DAPR-2010--Core_Recording",
      "2020": "DAPR-2020--Core_Mixing", "2255": "DAPR-2255--Audio_Hardware_I",
      "3255": "DAPR-3255--Audio_Hardware_II", "3340": "DAPR-3340--Spatial_Audio_I",
      "3345": "DAPR-3345--Spatial_Audio_II"}
# The schedule picture each outline page shows now (read from the newest package, 2026-10-01)
B_OLD = {"3340": "Schedule_Module_Timeline.png", "3255": "Term_Schedule_Spring_2027.png", "3345": "Term_Schedule.png"}

# What ChatGPT is told, in the Markdown for ChatGPT and on the HTML page (both are given to the ChatGPT desktop app)
GPT_STEPS = ["1. Read the item's five details: Action, File name, Save path, Old image, What to create.", '2. Open the old image at its path on this Mac and look at it. For a REPLACE, see exactly what is wrong and fix that. For a New PowerPoint picture, make something clearly different from it. An item with no old image has nothing to open.', "3. Generate one image from the item's prompt exactly as written: its pixel size, format and background.", "4. Save it at the item's Save path with the exact File name (same spelling, case and extension). REPLACE: save over the file that is there. ADD NEW: save it as a new file, creating the folder if needed.", '5. Check the saved image against the prompt and the old image. If a fact is wrong, a quoted label is misspelled, or text appears that the prompt did not ask for, make it again and save over it.', '6. Write the item number, the file name and the path you saved to, then stop and wait. Adam says "next" to continue, or an item number to jump to.']
GPT_RULES = ['Every image here is approved to be made. REPLACE items are corrections Adam asked for; do not refuse and do not ask for a photo.', 'Keep every word and number: when an item has an old image, every label, number, address, value, unit and explanation it shows goes into the new image, spelled exactly, beside the part it describes; change only the wording the item calls wrong. This wins over any line in a prompt that says no text or no numbers (Standards 20.5c).', 'A picture with no old image: no text, numbers, letters, logos, brand marks, model numbers, watermarks or readable screens, unless the prompt quotes exact labels; then use only those labels, spelled exactly.', 'Nothing that claims to be a real named product. Equipment is generic and unbranded; screens are dark or out of focus.', 'A New PowerPoint picture must look clearly different from the old Canvas picture it stands beside: a different angle, setting and composition.']

changes = {"alt_trunc": 0, "size_line": 0, "replace_header": 0, "alt_written": 0}
problems = []

def straight(s):
    """Straight quotes, no em or en dashes (All AI Projects 1)."""
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("—", ", "), ("–", " to ")):
        s = s.replace(a, b)
    return s

def mtime(p):
    try: return os.path.getmtime(p)
    except OSError: return None

def fmt_t(t): return dt.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M") if t else "missing"

index = {}
def find_in_class(cls, name, module=""):
    """Path of a picture by name in a class's repo folder, preferring the module's own folder."""
    if cls not in index:
        idx = {}
        for root, dirs, files in os.walk(CLASSES + "/" + CF[cls]):
            dirs[:] = [d for d in dirs if not d.startswith(("_unused", "_duplicates", "_review", "_to_delete", "_briefs"))]
            for f in files: idx.setdefault(f.lower(), []).append(os.path.join(root, f))
        index[cls] = idx
    hits = sorted(index[cls].get(name.lower(), []))
    if not hits: return None
    mod = module.replace(" ", "_").replace(":", "__").lower()
    hits.sort(key=lambda p: (mod not in p.lower() if mod else False, len(p)))
    return hits[0]

def alt_from_prompt(prompt):
    """Alt text written from what the prompt shows, under 120 characters (Standards 2)."""
    body = prompt.split("\n\n", 1)[-1].strip()
    s = re.sub(r"^(Photorealistic, wide landscape image\.|Wide landscape image\.|Photorealistic,? )\s*", "", body)
    s = re.split(r"(?<=[a-z0-9])\. ", s, maxsplit=1)[0].rstrip(".")
    s = re.sub(r"^(an? )?(photorealistic )?(wide )?(banner of |cinematic photograph of |overhead photograph of |photograph of |image of )", "", s, flags=re.I)
    s = s[0].upper() + s[1:]
    if len(s) > 119: s = s[:s.rfind(" ", 0, 119)].rstrip(",;")
    return s

items = []

# ---------------- Part A: wrong facts ----------------
pa = open(CLASSES + "/_briefs/ChatGPT Image Prompts - ALL COURSES Priorities.md").read()
tier2 = pa.split("# Tier 2.")[1].split("# Tier 3.")[0]
a_done = []
for m in re.finditer(r"^## Tier 2, (\d\d)\. (DAPR \d{4}|ALL COURSES): (\S+)\n(.*?)(?=^## Tier 2|\Z)", tier2, re.S | re.M):
    n = int(m.group(1))
    if n < 8: continue
    body = m.group(4)
    why = re.search(r"Wrong now: (.*)", body).group(1).strip()
    code = re.findall(r"```[a-z]*\n(.*?)\n```", body, re.S)[0]
    f = dict(re.findall(r"^(Image|File name|Save to \(overwrite\)|Size|Format|Used on|Fix): (.*)$", code, re.M))
    path = f["Save to (overwrite)"].strip()
    t = mtime(path)
    if t and t > CUT_A and path not in KEEP:
        a_done.append(f["File name"]); continue
    if t is None: problems.append("A %02d %s: the file to replace is missing on disk" % (n, f["File name"]))
    changes["replace_header"] += 1
    items.append(dict(part="A", cls=m.group(2).split()[-1], fname=f["File name"], path=path,
        action="REPLACE" if t else "ADD NEW", old=path if t else "",
        old_desc="This is the picture being replaced. Wrong now: " + why,
        what=f["Image"][:1].upper() + f["Image"][1:],
        size="%s, %s" % (f["Size"], f["Format"]), used=f["Used on"], alt=f["Image"][:1].upper() + f["Image"][1:],
        prompt=("REPLACE AN IMAGE FILE. Adam's decision is already made: make this corrected image so it is "
                "saved over the existing file named below. Do not refuse and do not ask for a photo.\n\n" + code),
        chip="Standards 20.1 rule 3 exception: replacement Adam asked for"))

# ---------------- Part B: outline page topic images ----------------
B_ITEMS = {
 "3340": ("A spatial audio mixing room ready for a planning session",
  "Create a 1600 x 600 pixel JPEG at quality 88.\n\nPhotorealistic, wide landscape photograph. A quiet immersive mixing room in the early morning: a ring of unbranded speakers on stands around a single listening chair, more small speakers mounted high on the walls and ceiling, acoustic panels in deep green (#1B5E20) and charcoal (#212121). On the mixing desk in the foreground lies an open paper week planner, its pages blocked in solid colors of blue (#0D47A1), green and soft gray with no writing at all, beside closed back headphones and a cup of coffee. The computer screens on the desk are dark or softly out of focus. Soft natural light from a high window, shallow depth of field so the speakers behind fall gently soft. Keep the left third of the frame calm.\n\nNo text, no numbers, no letters, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, frames, title bars or caption text, no legible screens or writing anywhere, including on the planner. No real product you could name. No people, no hands.",
  "Immersive mixing room with ceiling speakers and an open color blocked planner on the desk"),
 "3255": ("An audio electronics bench set up for planning the term",
  "Create a 1600 x 600 pixel JPEG at quality 88.\n\nPhotorealistic, wide landscape photograph of a tidy electronics and audio networking workbench in a university lab. Across the bench: a solderless breadboard with a few generic components, a coil of solder, a small soldering station, a bundle of blue (#0D47A1) network patch cables, a generic unbranded network switch with tiny green status lights, and a multimeter with its display turned away from the camera. Behind the bench, a pegboard wall holds rows of solid colored index cards in blue, green (#1B5E20) and orange (#993300), pinned in neat columns like a term plan, with no writing on any card. Warm task lighting from the left, shallow depth of field. Keep the left third of the frame calm.\n\nNo text, no numbers, no letters, no labels, no silkscreen or component markings, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, frames, title bars or caption text, no legible screens or writing anywhere. No real product you could name. No people, no hands.",
  "Electronics bench with breadboard, network cables and a pegboard of color coded planning cards"),
 "3345": ("A game audio studio with a production planning board",
  "Create a 1600 x 600 pixel JPEG at quality 88.\n\nPhotorealistic, wide landscape photograph of a small game audio studio. A desk with two unbranded monitors that are dark or softly out of focus, closed back headphones, a generic game controller and a compact keyboard. On the wall behind the desk, a glass production board holds columns of solid colored sticky notes in blue (#0D47A1), green (#1B5E20), violet (#4A148C) and gray, arranged like a sprint plan, with no writing on any note. Unbranded studio monitors sit on stands at each side of the desk. Cool evening light with a warm desk lamp, shallow depth of field. Keep the left third of the frame calm.\n\nNo text, no numbers, no letters, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, frames, title bars or caption text, no legible screens or writing anywhere, including on the notes. No real product you could name. No people, no hands.",
  "Game audio studio desk with a production board of color coded sticky notes"),
}
b_done = []
for cls in ["3340", "3255", "3345"]:
    what, prompt, alt = B_ITEMS[cls]
    path = "%s/%s/Course_Orientation/Schedule_Banner.jpg" % (CLASSES, CF[cls])
    if os.path.exists(path) and path not in KEEP: b_done.append(cls); continue
    items.append(dict(part="B", cls=cls, fname="Schedule_Banner.jpg", path=path, action="ADD NEW",
        old="%s/%s/Course_Orientation/%s" % (CLASSES, CF[cls], B_OLD[cls]),
        old_desc=("The outline page shows this schedule picture now. The Live Schedule replaces it, which leaves the page "
                  "needing a real topic image (Standards 0b.4, 16b). Make a new banner; the schedule picture is not overwritten."),
        what=what, size="1600 x 600 px, JPEG quality 88",
        used="Orientation: Schedule & Module Outline (top of the page, above the Live Schedule)",
        alt=alt, prompt=prompt, chip="Standards 0b.4 and 16b: every page needs a real image"))

# ---------------- Part C: placeholders ----------------
pc = open(CLASSES + "/_briefs/ChatGPT Image Prompts - ALL COURSES TO DO.md").read()
c_done = []
for sec in re.split(r"^(?=# )", pc, flags=re.M):
    hm = re.match(r"# (Shared|DAPR (\d{4}))", sec)
    if not hm: continue
    course = "All" if hm.group(1) == "Shared" else hm.group(2)
    for m in re.finditer(r"^## (.*?)\n(.*?)(?=^## |\Z)", sec, re.S | re.M):
        title, body = m.group(1), m.group(2)
        if "Save as" not in body: continue
        page = (re.search(r"^Page: (.*)$", body, re.M) or [None, ""])[1]
        status = (re.search(r"^Status: (.*)$", body, re.M) or [None, ""])[1]
        size = (re.search(r"^Final size: (.*)$", body, re.M) or [None, ""])[1]
        save = re.search(r"Save as[^\n]*:\s*\n+```\n(.*?)\n```", body, re.S).group(1).strip()
        pm = re.search(r"Prompt:\s*\n+```\n(.*?)\n```", body, re.S)
        t = mtime(save)
        if t and t > CUT_C and save not in KEEP:
            c_done.append(os.path.basename(save)); continue
        fname = os.path.basename(save); ext = fname.rsplit(".", 1)[1].upper()
        sm = re.search(r"(\d{3,4}) by (\d{3,4})", size)
        w, h = (sm.group(1), sm.group(2)) if sm else ("1600", "900")
        transparent = "transparent" in size.lower()
        if pm:
            p = "Create a %s x %s pixel %s%s.\n\n%s" % (w, h, ext, " with a fully transparent background" if transparent else "", pm.group(1).strip())
            changes["size_line"] += 1
        else:
            # Shared Image 02 has a description only; its words are fixed by the brief.
            p = ("REPLACE AN IMAGE FILE. Adam's decision is already made: make this updated image so it is saved over the existing file named below.\n\n"
                 "Create a %s x %s pixel PNG with a fully transparent background. Attach the current %s as the style reference and keep its look.\n\n"
                 "This is a labeled diagram, the one exception to the no text rule. Use exactly these words and numbers, letter for letter, and no others:\n\n"
                 "Panels, left to right: 1 LECTURE CREDIT (1 blue block, 2 green blocks); 3 LECTURE CREDITS (3 blue blocks over 6 green blocks), then an arrow to 9 HOURS PER WEEK; 1 LAB CREDIT (3 blue blocks, no green), then an arrow to 3 HOURS PER WEEK. Legend: blue IN CLASS OR LAB, green OUTSIDE OF CLASS.\n\n"
                 "Richly rendered dimensional blocks with soft shading, blue #0D47A1 and green #1B5E20, text in charcoal #212121. No logos, no watermark, no signature, no borders, frames, title bars or caption text."
                 % (w, h, fname))
            problems.append("C %s: the brief had no prompt, only a description; the prompt is written from its fixed words" % fname)
        note = (re.search(r"^Note: (.*)$", body, re.M) or [None, ""])[1]
        if status.startswith("Placeholder"):
            od = "A code drawn gray placeholder sits at this exact path. Save the real picture over it; the page already links this name."
        elif status.startswith("Update"):
            od = "The current picture is wrong for the page now: " + status.split(". ", 1)[1]
        else:
            od = "No file yet; the page links this name, so saving it fixes the page."
        if note: od += " " + note
        altm = re.search(r'alt="([^"]+)"', body)
        alt = altm.group(1) if altm else alt_from_prompt(pm.group(1)) if pm else "Bar diagram of weekly hours for lecture and lab credits"
        if not altm: changes["alt_written"] += 1
        items.append(dict(part="C", cls=course, fname=fname, path=save,
            action="REPLACE" if t else "ADD NEW", old=save if t else "", old_desc=od,
            what=re.sub(r"^.*?\d+\. ", "", title),
            size="%s x %s px, %s%s" % (w, h, "PNG" if ext == "PNG" else "JPEG", ", transparent" if transparent else ""),
            used=page, alt=alt[:119], prompt=p, chip="Standards 0b.4 rule 6: placeholder waits on ChatGPT"))

# ---------------- Part C, continued: five-detail briefs (Standards 20.5b), such as Student Essentials ----------------
import glob as _glob
for bf in sorted(_glob.glob(CLASSES + "/*/_briefs/ChatGPT Image Creation - *.md")):
    if bf.endswith("Presentations.md"): continue
    for part in re.split(r"^(?=## Image )", open(bf, encoding="utf-8").read(), flags=re.M)[1:]:
        f = dict((k.strip(), v.strip().strip("`")) for k, v in re.findall(r"^\| \d \| (Action|File name|Full save path|What to create) \| (.*?) \|$", part, re.M))
        alt = (re.search(r"^\| Alt text \| `?(.*?)`? \|$", part, re.M) or [None, ""])[1]
        pm = re.search(r"```text\n(.*?)\n```", part, re.S)
        if "Full save path" not in f or not pm: continue
        path = f["Full save path"]; t = mtime(path)
        # done once a real picture is there: a gray placeholder is small (38 KB at 1600 x 900), a real picture is not
        if t and not ("placeholder" in f.get("Action", "").lower() and os.path.getsize(path) < 80000): continue
        _m = re.search(r"DAPR-(\d{4})--", path)
        items.append(dict(part="C", cls=_m.group(1) if _m else "All", fname=os.path.basename(path), path=path, action="REPLACE" if t else "ADD NEW",
            old=path if t else "", old_desc=("A gray placeholder sits here now; save over it." if t else "No file yet; the page links this name."),
            what=re.sub(r"^## Image \d+ - ", "", part.splitlines()[0]).strip(), size=(re.search(r"(\d+ x \d+ px)", f.get("What to create", "")) or [None, "1600 x 900 px"])[1] + (", JPEG" if path.lower().endswith((".jpg", ".jpeg")) else ", PNG"),
            used=os.path.basename(bf).replace("ChatGPT Image Creation - ", "").replace(".md", ""), alt=alt[:119] or os.path.basename(path), prompt=pm.group(1).strip(),
            chip="Standards 20.5b brief: placeholder waits on ChatGPT"))

# ---------------- Part D: new PowerPoint pictures ----------------
d_counts = {}
# What fills each new deck's picture slot now (Build-Tools/slide_picture_sources.py): a Claude stand-in is the old image;
# a ChatGPT picture already on the slide means the item is done.
SRC_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "slide_picture_sources.json")
IN_SLOT = {}
if os.path.exists(SRC_JSON):
    for sp, sv in json.load(open(SRC_JSON)).items():
        if sv.get("slot"): IN_SLOT[(os.path.dirname(sp), sv["slot"])] = (sp, sv["src"])
for cls in CLASS_ORDER:
    bf = "%s/%s/_briefs/ChatGPT Image Creation - DAPR %s Presentations.md" % (CLASSES, CF[cls], cls)
    txt = open(bf).read()
    module = ""; tot = done = 0
    for part in re.split(r"^(?=#{1,2} )", txt, flags=re.M):
        mm = re.match(r"# (.*)", part)
        if mm and not part.startswith("## "):
            module = mm.group(1).strip(); continue
        im = re.match(r"## Image (\d+) - (.*)", part)
        if not im: continue
        fields = dict((k, v.strip().strip("`")) for k, v in re.findall(r"^\| (Filename|Format|Dimensions|Destination folder|Used on|Alt text) \| (.*?) \|$", part, re.M))
        if "Filename" not in fields: continue
        tot += 1
        path = fields["Destination folder"].rstrip("/") + "/" + fields["Filename"]
        if os.path.exists(path) and path not in KEEP: done += 1; continue
        held = IN_SLOT.get((fields["Destination folder"].rstrip("/"), fields["Filename"]))
        if held and held[1] == "ChatGPT" and path not in KEEP: done += 1; continue
        pm = re.search(r"```text\n(.*?)\n```", part, re.S)
        if not pm: problems.append("D %s %s: no prompt block" % (cls, fields["Filename"]))
        alt = fields.get("Alt text", "")
        if len(alt) >= 118 and not alt.endswith((".", ")")):   # the brief cut it at 120 mid word
            cut = max(alt.rfind("; "), alt.rfind(", "))
            alt = alt[:cut] if cut > 40 else alt[:alt.rfind(" ")]
            changes["alt_trunc"] += 1
        raw_used = (re.search(r"^\| Used on \| (.*?) \|$", part, re.M) or [None, ""])[1]   # backticks kept
        used = raw_used.replace("`", "")
        olds, lost = [], []
        cm = re.search(r"in place of the Canvas pictures? (.*)$", raw_used)
        slot = re.search(r"in the empty picture slot `([^`]+)`", raw_used)
        if cm:
            for cname in re.findall(r"`([^`]+)`", cm.group(1)) or [cm.group(1).strip().rstrip(",.;")]:
                cpath = find_in_class(cls, cname, module)
                if cpath: olds.append(cpath)
                else:
                    lost.append(cname)
                    problems.append("D %s %s: its Canvas picture %s was not found in the repo" % (cls, fields["Filename"], cname))
            od = ("The slide repeats %s now%s. Make a different picture of the same idea: a different angle, setting and composition. "
                  "The Canvas page keeps its picture; only the slide changes." %
                  ("this Canvas picture" if len(olds) + len(lost) == 1 else "these %d Canvas pictures together" % (len(olds) + len(lost)),
                   " (not found in the repo: " + ", ".join(lost) + ")" if lost else ""))
        elif slot and held:
            olds = [held[0]]
            od = ("The slide shows Claude's TEMPORARY stand-in drawing now (Standards 20.1). Make the real picture the slide teaches, "
                  "from its title and the prompt; it does not need to look like the stand-in. Save it under this new name; "
                  "Swap In New Pictures puts it on the slide in place of the stand-in.")
        elif slot:
            od = ("No old picture: the slide has an empty picture slot (%s). Make the picture the slide teaches, "
                  "from its title and the prompt." % slot.group(1))
        else:
            od = "No old picture on this slide."
        items.append(dict(part="D", cls=cls, fname=fields["Filename"], path=path, action="ADD NEW",
            old=olds[0] if olds else "", olds=olds, old_desc=od,
            what="%s: %s" % (module, im.group(2).strip()),
            size="%s, %s" % (fields.get("Dimensions", ""), fields.get("Format", "")), used=used, alt=alt,
            prompt=pm.group(1).strip() if pm else "", chip="Standards 8: new PowerPoint pictures live beside the decks"))
    d_counts[cls] = (tot, done)

# ---------------- Needs Adam (not ChatGPT) ----------------
fx = open(FIXES).read()
na = fx.split("## Needs Adam (photo, screenshot, or a decision)")[1].split("\n## ")[0]
e_items, e_closed = [], []
for row in re.findall(r"^\| (.+?) \| (.+?) \|$", na, re.M):
    if row[0] in ("File", "---"): continue
    pm = re.search(r"`([^`]+\.(?:png|jpg|jpeg))`", row[0])
    full = CLASSES + "/" + pm.group(1) if pm else None
    t = mtime(full) if full else None
    if t and t > CUT_E + 60:
        e_closed.append((pm.group(1), fmt_t(t))); continue
    e_items.append(dict(file=row[0].replace("`", ""), todo=row[1].replace("`", ""), full=full,
        state="missing" if full and t is None else ("no file named" if not full else "unchanged since " + fmt_t(t))))
miss3340 = pc.split("## DAPR 3340: also missing, but not for ChatGPT")[1].split("\n# ")[0]
for page, rel, todo in re.findall(r"^\d+\. Page: (.*?)\. File: `([^`]+)`\. (.*)$", miss3340, re.M):
    full = CLASSES + "/" + rel
    if os.path.exists(full): e_closed.append((rel, "now exists")); continue
    e_items.append(dict(file=rel + " (page: " + page + ")", todo=todo, full=full, state="missing"))

# ---------------- live pictures that were only renamed ----------------
f_rows = []
for cls in CLASS_ORDER:
    p = "%s/%s/Claude outputs/Notes and Briefs/2026-09-30 %s - Live Broken Pictures.md" % (COURSES, CLASS_NAME[cls], CLASS_NAME[cls])
    if not os.path.exists(p): continue
    head = open(p).read()
    m = re.search(r"(\d+) picture links on its pages do not load \((\d+) addresses of (\d+)\)\. (\d+) of them were renamed", head)
    f_rows.append((cls, m.group(1), m.group(2), m.group(3), m.group(4), len(re.findall(r"\| not found in the GitHub folder \|", head)), p))

# ---------------- what only Canvas Preview knows (--extra) ----------------
def pixel_size(path):
    try:
        out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path], capture_output=True, text=True).stdout
        w = int(re.search(r"pixelWidth: (\d+)", out).group(1)); h = int(re.search(r"pixelHeight: (\d+)", out).group(1))
        return w, h
    except Exception: return 1600, 900

def class_of(path):
    m = re.search(r"DAPR-(\d{4})--", path)
    return m.group(1) if m else "All"

def fix_prompt(path, notes):
    """A Fix Canvas Image prompt for a picture Adam wrote notes about (the same shape as Presentation Images' Canvas fix)."""
    w, h = pixel_size(path)
    jpeg = path.lower().endswith((".jpg", ".jpeg"))
    module = os.path.basename(os.path.dirname(path)).replace("__", ": ").replace("_", " ")
    return ("REPLACE AN IMAGE FILE. Adam's decision is already made: make this corrected image so it is saved over the existing file named below. Do not refuse and do not ask for a photo.\n\n"
            "Create a %d x %d pixel %s.\n\n"
            "This is a CORRECTION of a teaching picture on a university audio course page in Canvas (DAPR %s, %s). The old picture is this file: %s. "
            "Open it and look at it: it is wrong in the ways Adam's notes below describe. Make a corrected replacement that does the same teaching job: "
            "keep what is right, fix everything the notes name, and make every technical detail accurate (controls and readings, connector pins, signal flow, values and labels as they really are).\n\n"
            "If the old picture is a photograph, make a realistic photograph of generic equipment showing the correction. If it is a drawing, diagram or chart, "
            "make a clean, richly rendered, slightly dimensional illustration with soft shading, in deep green #1B5E20, blue #0D47A1, red #B71C1C and orange #993300 on neutral greys, %s. "
            "No logos, brand marks or model numbers. No watermark, signature or border.\n\n"
            "Adam's notes on what is wrong and how to fix it (they win over anything above): %s"
            % (w, h, "JPEG" if jpeg else "PNG", class_of(path), module, path, "on a white background" if jpeg else "on a white or fully transparent background", notes))

REPO = os.path.dirname(CLASSES)
def last_change(path):
    """When the picture last changed, and why: its last commit, or this Mac's copy when it has changes not committed."""
    try:
        rel = os.path.relpath(path, REPO)
        if not rel.startswith(".."):
            dirty = subprocess.run(["git", "-C", REPO, "status", "--porcelain", "--", rel], capture_output=True, text=True).stdout.strip()
            if not dirty:
                out = subprocess.run(["git", "-C", REPO, "log", "-1", "--format=%cI|%s", "--", rel], capture_output=True, text=True).stdout.strip()
                if out:
                    d, msg = out.split("|", 1)
                    return dt.datetime.fromisoformat(d).astimezone().replace(tzinfo=None), 'committed "%s"' % msg
    except Exception: pass
    t = mtime(path)
    return (dt.datetime.fromtimestamp(t), "changed on this Mac") if t else (None, "")

def note_time(e):
    try: return dt.datetime.fromisoformat(e["noted"].replace("Z", "+00:00")).astimezone().replace(tzinfo=None) if e.get("noted") else None
    except Exception: return None

by_path = {}
for it in items: by_path.setdefault(it["path"], []).append(it)
def add_note(it, note, who):
    it["old_desc"] += " %s: %s" % (who, note)
    it["prompt"] += "\n\n%s (they win over anything above): %s" % (who, note)
    it["notes"] = (it.get("notes", "") + " " + note).strip()

for e in EXTRA:
    kind, path, note = e.get("kind"), e.get("path", ""), (e.get("note") or "").strip()
    if kind in ("canvasNote", "fixNote", "deckNote") and note:
        hits = by_path.get(path, [])
        who = "Adam's notes" if kind != "deckNote" else "Adam's notes on this slide picture"
        for it in hits:
            add_note(it, note, who)
            if "noted" in it: it["noted"].append(note_time(e))
        if hits or kind != "canvasNote": continue
        if not os.path.exists(path):
            problems.append("Your note on %s: that file is not on this Mac, so it can't be fixed here (%s)" % (os.path.basename(path), e.get("source", "")))
            continue
        w, h = pixel_size(path)
        it = dict(part="E", cls=class_of(path), fname=os.path.basename(path), path=path, action="REPLACE", old=path, olds=[path], noted=[],
                  old_desc="This is the picture being replaced. Adam's notes (%s): %s" % (e.get("source", "Canvas Preview"), note), notes=note,
                  what="Corrected " + os.path.basename(path).rsplit(".", 1)[0].replace("_", " "),
                  size="%d x %d px, %s" % (w, h, "JPEG" if path.lower().endswith((".jpg", ".jpeg")) else "PNG"),
                  used="the Canvas pages that show this picture", alt="Keep the page's current alt text unless the picture's subject changes",
                  prompt=fix_prompt(path, note), chip="Fix Canvas Image: Adam's notes in Canvas Preview")
        it["noted"].append(note_time(e))
        items.append(it); by_path.setdefault(path, []).append(it)
    elif kind == "temp" and os.path.exists(path) and path not in by_path:
        w, h = int(e.get("width") or 1600), int(e.get("height") or 900)
        it = dict(part="F", cls=class_of(path), fname=os.path.basename(path), path=path, action="REPLACE", old=path, olds=[path],
                  old_desc="Claude drew this TEMPORARY stand-in%s while ChatGPT was out of image generations. Make the real image from the prompt and save it over the stand-in." % (" on " + e["made"][:10] if e.get("made") else ""),
                  what=e.get("title") or os.path.basename(path), size="%d x %d px, %s" % (w, h, "JPEG" if path.lower().endswith((".jpg", ".jpeg")) else "PNG"),
                  used="where the stand-in is used now", alt="Keep the current alt text", prompt=e.get("prompt", ""),
                  chip="Standards 20.1: temporary stand-in, replaced by ChatGPT")
        items.append(it); by_path.setdefault(path, []).append(it)
# ---------------- Part G: unique pictures for slides that still show the Canvas picture ----------------
# Adam, 2026-10-02: every deck works now with the Canvas pictures (each slide links its GitHub file through the
# PowerPoint mirror); a link into GitHub means the slide still needs its own picture. Real things stay (keep).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck_pair
d_slides = set()
for it in items:
    if it["part"] == "D":
        m = re.match(r"([^,]+?)\.pptx, slide (\d+)", it["used"])
        if m: d_slides.add((m.group(1), int(m.group(2))))
g_keep = 0
for u in deck_pair.unique(deck_pair.LINKS_ROOT):
    if u["keep"]: g_keep += 1; continue
    if (u["base"], u["slide"]) in d_slides or (os.path.exists(u["new"]) and u["new"] not in KEEP): continue
    jpeg = u["new"].lower().endswith((".jpg", ".jpeg")); title = straight(u["title"] or u["alt"] or "this slide")
    prompt = ("Create a %d x %d pixel %s.\n\nA NEW presentation picture for the slide \"%s\" in %s (a university audio course). "
              "The old image is the picture the Canvas page shows (%s); the slide repeats it now. Make a fresh picture of the same content "
              "for the slide: for a diagram or chart, the same parts, order, values and labels in a new rendered look; for a photograph, the "
              "same kind of subject as a new photograph with a different angle, setting and light. Generic equipment only.\n\n"
              "Slide picture: %s\n\nStyle: clean, richly rendered and slightly dimensional, soft shading, solid color fills in deep green #1B5E20, "
              "blue #0D47A1, red #B71C1C and orange #993300 on neutral greys, %s. No logos, brand marks or model numbers. No watermark, "
              "signature, border or caption text." % (u["width"], u["height"], "JPEG at quality 88" if jpeg else "PNG",
              title, CLASS_NAME[class_of(u["deck"])], u["github"], straight(u["alt"] or title), "on a white background" if jpeg else "on a white or fully transparent background"))
    items.append(dict(part="G", cls=class_of(u["deck"]), fname=os.path.basename(u["new"]), path=u["new"], action="ADD NEW",
        old=u["github"], olds=[u["github"]],
        old_desc=("The slide shows the Canvas picture now, linked from GitHub: %s. Make a unique picture of the same content for the slide; "
                  "the Canvas page keeps its picture. Approving it in Canvas Preview points slide %d of %s-Linked.pptx at the new file "
                  "(the GitHub picture is never written over) and builds the Embedded deck again." % (u["github"], u["slide"], u["base"])),
        what="%s, slide %d: %s" % (u["base"], u["slide"], title), size="%d x %d px, %s" % (u["width"], u["height"], "JPEG" if jpeg else "PNG"),
        used="%s-Linked.pptx, slide %d" % (u["base"], u["slide"]), alt=straight(u["alt"] or title)[:119], prompt=straight(prompt),
        chip="Standards 8: a GitHub link on a slide means it still needs its own picture"))

# Keep every word and number (Adam, 2026-10-02: "it drops all the wording and the numbers ... I need all the explanations
# that are there"). Canvas Preview adds the old picture's exact words; this line goes in every export (Standards 20.5c).
KEEP_TEXT = ("KEEP EVERY WORD AND NUMBER (this wins over any line above that says no text, no numbers, no addresses or only one label): "
             "open the old image at %s. Every label, number, address, value, unit and explanation it shows must be in the new picture, "
             "spelled exactly, beside the part it describes, large and easy to read. Change only the wording this item calls wrong, and "
             "write the corrected wording in its place. Never drop text to make the picture look cleaner.")
for it in items:
    olds = it.get("olds") or ([it["old"]] if it.get("old") else [])
    if olds and "stand-in" not in it["old_desc"]:
        it["prompt"] += "\n\n" + KEEP_TEXT % " and ".join(olds)
# Check first: a picture changed after every note on it (or the notes have no date) may already be fixed. It stays out of
# the ChatGPT list until Adam presses D (done) or writes a new note (Adam, 2026-10-01: Digital_Meter.jpg was fixed on
# 2026-09-24 and its old note made ChatGPT draw it again).
for it in items:
    if it.get("part") != "E" or it["path"] in KEEP: continue
    when, why = last_change(it["path"])
    times = it.pop("noted", [])
    fresh = [n for n in times if n and when and n > when]
    if when and not fresh:
        undated = all(n is None for n in times)
        it["check"] = True
        it["check_info"] = ("Your note has no date (it was written before notes were dated on 2026-10-01). " if undated else "Your note was written before the picture last changed. ") + \
            "The picture %s on %s, so it may already be fixed. Look at it: D if it is done, N if it is still wrong." % (why, when.strftime("%Y-%m-%d %H:%M"))
for it in items:
    it.pop("noted", None)
    it.setdefault("check", False)
    it["state"] = "review" if it["path"] in KEEP else "open"
    it["backup"] = KEEP.get(it["path"], "")
# Twins: the same placeholder saved under the same name in another class (3340 Dolby_Certification repeats 3345's).
# The picture made for one is copied to its twins, so ChatGPT makes it once (2026-10-02).
import hashlib
def _md5(f):
    try: return hashlib.md5(open(f, "rb").read()).hexdigest()
    except Exception: return ""
by_base = {}
for root, dirs, fs in os.walk(CLASSES):
    dirs[:] = [d for d in dirs if d not in ("_unused", "_briefs")]
    for f in fs:
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif")): by_base.setdefault(f, []).append(os.path.join(root, f))
TWINS = set()
for it in items:
    if it["part"] != "C": continue
    twins = [t for t in by_base.get(it["fname"], []) if t != it["path"] and (os.path.getsize(t) < 30000 or _md5(t) == _md5(it["path"]))]
    if twins:
        it["also"] = twins; TWINS.update(twins)
        it["old_desc"] += " The same picture is also used at %s: Canvas Preview copies the new one there too." % ", ".join(twins)
items[:] = [it for it in items if not (it["part"] == "F" and it["path"] in TWINS)]

# A Claude stand-in stays on the list until ChatGPT makes the real picture, even after Adam approves it (Standards 20.1)
TEMPS = {e["path"]: e.get("made", "")[:10] for e in EXTRA if e.get("kind") == "temp"}
for it in items:
    if it["path"] in TEMPS and os.path.exists(it["path"]):
        it["temp"] = True
        it["old_desc"] = ("Claude drew a TEMPORARY stand-in here%s while ChatGPT was out (Standards 20.1): it is the old image now. Make the real picture "
                          "from the prompt and save it over the stand-in. " % (" on " + TEMPS[it["path"]] if TEMPS[it["path"]] else "")) + it["old_desc"]
items[:] = [it for it in items if it["path"] not in DONE or it.get("temp")]

for row in items + e_items:
    for k, v in row.items():
        if isinstance(v, str): row[k] = straight(v)

# ---------------- order and numbers ----------------
items.sort(key=lambda it: ("EFABCDG".index(it["part"]), CLASS_ORDER.index(it["cls"]) if it["part"] in "CD" and it["cls"] in CLASS_ORDER else -1))
groups = [("13", "Your notes: Canvas pictures to fix", [i for i in items if i["part"] == "E"]),
          ("14", "Claude stand-ins to remake", [i for i in items if i["part"] == "F"]),
          ("1", "Part A. Wrong facts in Canvas pictures", [i for i in items if i["part"] == "A"]),
          ("2", "Part B. New topic images for the outline pages", [i for i in items if i["part"] == "B"]),
          ("3", "Part C. Placeholders still on Canvas pages", [i for i in items if i["part"] == "C"])]
for n, cls in enumerate(CLASS_ORDER):
    groups.append((str(4 + n), "Part D. New PowerPoint pictures: " + CLASS_NAME[cls], [i for i in items if i["part"] == "D" and i["cls"] == cls]))
groups.append(("15", "Part G. Unique pictures for slides that still show the Canvas picture", [i for i in items if i["part"] == "G"]))
for g, _, its in groups:
    for k, it in enumerate(its, 1): it["num"] = "%s.%d" % (g, k)
C = {p: sum(1 for i in items if i["part"] == p) for p in "ABCDEFG"}
dper = {c: sum(1 for i in items if i["part"] == "D" and i["cls"] == c) for c in CLASS_ORDER}
cper = {}
for i in items:
    if i["part"] == "C": cper[i["cls"]] = cper.get(i["cls"], 0) + 1
total = sum(C.values())
folder = os.path.dirname
short = lambda cls: "Shared" if cls == "All" else CLASS_NAME[cls].split(" - ")[0]

if JSON_OUT:
    json.dump({"generated": dt.datetime.now().isoformat(timespec="seconds"), "items": items,
               "groups": [{"num": g, "title": title, "count": len(its)} for g, title, its in groups if its],
               "needsAdam": e_items, "problems": problems}, open(JSON_OUT, "w"))
    print("json", JSON_OUT, len(items)); sys.exit(0)

CHECK = [it for it in items if it.get("check")]
items[:] = [it for it in items if not it.get("check")]
for g, title, its in groups: its[:] = [it for it in its if not it.get("check")]
C = {p: sum(1 for i in items if i["part"] == p) for p in "ABCDEFG"}
total = sum(C.values())

# ---------------- Markdown ----------------
md = []; w = md.append
w("All DAPR courses"); w("")
w("# ChatGPT Image Work List: All Classes"); w("")
w("Rev %s, checked against the files on disk on %s. Written from the 2026-09-30 request. A picture already made is not listed. "
  "Every item gives, together: the Action (REPLACE or ADD NEW), the file name, the full save path, the old image (its path and what is wrong with it) "
  "and what to create (Standards 20.5b). The HTML checklist beside this file shows the old image as a picture next to each item:" % (REV, dt.date.today().isoformat()))
w(""); w("```"); w("'" + OUT_HTML + "'"); w("```"); w("")
w("## Count"); w("")
w("| Part | What | Open now | Already made, left out |"); w("|---|---|--:|--:|")
if C["E"]: w("| | Your notes: Canvas pictures to fix (from Canvas Preview) | %d | |" % C["E"])
if C["F"]: w("| | Claude stand-ins to remake | %d | |" % C["F"])
w("| A | Wrong facts in Canvas pictures (Priorities Tier 2, items 08 to 29) | %d | %d |" % (C["A"], len(a_done)))
w("| B | New topic images for the outline pages (3340, 3255, 3345) | %d | %d |" % (C["B"], len(b_done)))
w("| C | Placeholders and missing files on Canvas pages | %d | %d |" % (C["C"], len(c_done)))
w("| D | New PowerPoint pictures | %d | %d |" % (C["D"], sum(v[1] for v in d_counts.values())))
w("| G | Unique pictures for slides that still show the Canvas picture (real things kept: %d) | %d | |" % (g_keep, C["G"]))
w("| | **All ChatGPT work** | **%d** | |" % total); w("")
w("| Action | Items |"); w("|---|--:|")
for a in ("REPLACE", "ADD NEW"): w("| %s | %d |" % (a, sum(1 for i in items if i["action"] == a)))
w("")
w("Part D by class, in your class order:"); w("")
w("| Class | In its brief | Already saved | Open now |"); w("|---|--:|--:|--:|")
for cls in CLASS_ORDER:
    t, d = d_counts[cls]; w("| %s | %d | %d | %d |" % (CLASS_NAME[cls], t, d, dper[cls]))
w("")
w("Part C by class: " + ", ".join("%s %d" % ("shared Classes/All" if c == "All" else short(c), cper[c]) for c in ["All"] + CLASS_ORDER if cper.get(c)) + "."); w("")
w("## How to use"); w("")
w("1. Work top to bottom: A, then B, then C, then D (D runs in class order 3340, 2020, 2000, 2255, 3345, 2010, 3255).")
w("2. Read the item's Action. REPLACE means a file is already at the path: save over it, same name and extension. ADD NEW means nothing is there yet: save the new file at the path (create the folder if needed).")
w("3. Look at the old image (in the HTML checklist it shows beside the item) and what is wrong with it. One image per ChatGPT chat: paste the prompt from the gray box and generate.")
w("4. Save to the full save path. In the Save dialog, press Command Shift G and paste the folder (the HTML checklist has a Folder copy button), then use the file name.")
w("5. Tick it in the HTML checklist, then tell Claude which ones are saved. Claude checks size and weight; for Part D it places each picture on its slide (Canvas Preview, Presentation Images, Use New in Deck) and rebuilds the PDF. Adam commits and pushes the repo pictures (Standards 20.4c).")
w("")
w("## What was changed in the reused prompts, and why"); w("")
w("Prompts are copied word for word from the briefs except:"); w("")
w("- **Part A (%d prompts):** each opens with one REPLACE AN IMAGE FILE line stating your decision is made, so ChatGPT overwrites instead of refusing (your standing rule for replacements, Standards 20.1 rule 3 exception)." % changes["replace_header"])
w("- **Part C (%d prompts):** a first line giving the pixel size and format, because Standards 20.3 says every prompt states its pixel size and these did not." % changes["size_line"])
w("- **Part C, shared Credit_Hour_Rule.png:** the brief had a description but no prompt; this prompt is written from the brief's fixed words, letter for letter.")
w("- **Part C (%d alt texts):** the brief gave none, so the alt text is written from what the prompt shows." % changes["alt_written"])
w("- **Part D (%d alt texts):** the brief cut these off at 120 characters mid word; they end at the last full phrase instead (Standards 2)." % changes["alt_trunc"])
w("- Part A alt text is the brief's own Image line.")
w("")

def md_item(it):
    w("### %s %s: %s" % (it["num"], short(it["cls"]), it["fname"])); w("")
    w("1. **Action:** **%s**. %s" % (it["action"], "A file is at this path now: save the new picture over it, same name and extension." if it["action"] == "REPLACE" else "Nothing is at this path yet: save the new picture here."))
    w("2. **File name:** `%s`" % it["fname"])
    w("3. **Full save path:**"); w(""); w("```"); w("'" + it["path"] + "'"); w("```"); w("")
    olds = it.get("olds") or ([it["old"]] if it["old"] else [])
    if olds:
        w("4. **Old image%s:**" % ("s" if len(olds) > 1 else "")); w("")
        for o in olds: w("```"); w("'" + o + "'"); w("```"); w("")
        w("   " + it["old_desc"])
    else:
        w("4. **Old image:** " + (it["old_desc"] if it["old_desc"].startswith("No old picture") else "none at this path. " + it["old_desc"]))
    w("5. **What to create:** %s. %s, for %s. Class: %s." % (it["what"].rstrip("."), it["size"], it["used"].rstrip("."), CLASS_NAME[it["cls"]]))
    w("   Alt text: " + it["alt"]); w("")
    w("```text"); w(it["prompt"]); w("```"); w("")

for g, title, its in groups:
    if g in ("1", "2", "3", "13", "14", "15"):
        w("# " + title); w("")
    if g == "4":
        w("# Part D. New PowerPoint pictures"); w("")
        w("New PowerPoint Image only: each picture goes on its slide; the Canvas page keeps its picture. Destinations are each module's Presentations/Images folder on this Mac (Standards 8); that folder never uploads."); w("")
    if title.startswith("Part D"):
        w("## %s (%d)" % (CLASS_NAME[CLASS_ORDER[int(g) - 4]], len(its))); w("")
        if not its: w("Nothing open."); w("")
    for it in its: md_item(it)

w("# Not ChatGPT work: pictures that need a real photo or screenshot from Adam"); w("")
w("Still open from the Needs Adam table in Image Fixes For Later (a row whose file changed after that note was written is left out), plus the DAPR 3340 figures the TO DO brief marks as capture or relink. Window captures only, light mode, nothing personal in frame, PNG for anything with text or a screen (Standards 20.6)."); w("")
w("| # | File | What to do | State on disk |"); w("|---|---|---|---|")
for k, e in enumerate(e_items, 1): w("| %d | %s | %s | %s |" % (k, e["file"].replace("|", "/"), e["todo"].replace("|", "/"), e["state"]))
w(""); w("Full paths, in table order:"); w("")
for k, e in enumerate(e_items, 1):
    if e["full"]: w("%d." % k); w(""); w("```"); w("'" + e["full"] + "'"); w("```"); w("")
if e_closed: w("Left out because the file changed since the note: " + ", ".join("%s (%s)" % c for c in e_closed) + "."); w("")
w("# Not ChatGPT work: live pictures that are only renamed"); w("")
w("These live pictures broke because the file was renamed, not because the picture is wrong. Each class's next package relinks them. Counts from each class's 2026-09-30 Live Broken Pictures list:"); w("")
w("| Class | Broken picture links | Different addresses | Addresses on its pages | Renamed (Now at) | Not found under any name |"); w("|---|--:|--:|--:|--:|--:|")
for r in f_rows: w("| %s | %s | %s | %s | %s | %d |" % (CLASS_NAME[r[0]], r[1], r[2], r[3], r[4], r[5]))
w("")
for r in f_rows: w("```"); w("'" + r[6] + "'"); w("```"); w("")
w("DAPR 2010, 3255 and 3345 are not live this term, so they have no such list."); w("")
if CHECK:
    w("# Check first (not given to ChatGPT)"); w("")
    w("These pictures changed after your note on them, so they may already be fixed. In Canvas Preview ▸ Images to Fix: D if done, N if still wrong (a new note puts it back on this list)."); w("")
    for it in CHECK: w("- %s %s: %s" % (it["num"], it["fname"], it["check_info"]))
    w("")
w("# Could not be verified"); w("")
w("- A file that exists is counted as made; outside Parts A and C (where the file date is checked) this cannot tell a finished ChatGPT picture from a Claude stand-in already at that path.")
w("- Part D: where a deck is already a Linked and Embedded pair, the picture still needs Use New in Deck (or the deck's own picture name) to reach the slide.")
w("- The 3340 Presentations brief's intro says 48 images; the brief itself holds 15, and that is what was checked.")
for p in problems: w("- " + p)
gif = [i for i in items if i["fname"].lower().endswith(".gif")]
for i in gif:
    w("- Item %s, %s: the page links a GIF, which Standards 20.2 does not allow. Save ChatGPT's PNG at the path as the brief says; the next %s package should link a .png under the same name." % (i["num"], i["fname"], short(i["cls"])))
w("")
w("# Folders and file names"); w("")
w("Each destination folder, the number of files to save there, and their names in list order (Standards 20.7)."); w("")
seen = []
for it in items:
    if folder(it["path"]) not in seen: seen.append(folder(it["path"]))
for f in seen:
    names = [it["fname"] for it in items if folder(it["path"]) == f]
    w("```"); w(f); w("```"); w(""); w("%d file%s:" % (len(names), "" if len(names) == 1 else "s")); w("")
    w("```"); w("\n".join(names)); w("```"); w("")
md_text = "\n".join(md) + "\n"

# ---------------- HTML (All AI Projects 12) ----------------
E = lambda s: html.escape(s or "", quote=True)
def copy(label, text, pre=False):
    tag = "pre" if pre else "div"
    return '<div class="cb"><span class="cl">%s</span><%s class="copy" title="Click to copy">%s</%s></div>' % (E(label), tag, E(text), tag)
def thumb(path):
    if not path: return '<div class="th none">No old image at this path</div>'
    return ('<div class="th"><img loading="lazy" src="file://%s" alt="Old image" onerror="this.parentNode.classList.add(\'gone\')">'
            '<span class="miss">Not on this Mac</span></div>' % E(quote(path)))
def h_item(it):
    act = "rep" if it["action"] == "REPLACE" else "add"
    olds = it.get("olds") or ([it["old"]] if it["old"] else [])
    thumbs = "".join(thumb(o) for o in olds) if olds else thumb("")
    paths = "".join(copy("Old image path", o) for o in olds)
    return ('<div class="item" data-id="%s"><label class="top"><input type="checkbox"> <span class="num">%s</span> '
            '<span class="act %s">%s</span> <b>%s</b></label> <span class="chip">%s</span>'
            '<div class="row"><div class="ths">%s</div><div class="old"><div class="cl">Old image</div>%s<div class="why">%s</div></div></div>'
            '<div class="what"><b>What to create:</b> %s. %s. Used on: %s. %s.</div>%s%s%s%s%s</div>') % (
        E(it["num"]), E(it["num"]), act, E(it["action"]), E(it["fname"]), E(it["chip"]),
        thumbs, paths, E(it["old_desc"]),
        E(it["what"].rstrip(".")), E(it["size"]), E(it["used"].rstrip(".")), E(CLASS_NAME[it["cls"]]),
        copy("File name", it["fname"]), copy("Full save path", it["path"]), copy("Folder (Command Shift G)", folder(it["path"])),
        copy("ChatGPT prompt", it["prompt"], True), copy("Alt text", it["alt"]))
hg = []
for g, title, its in groups:
    if not its: continue
    hg.append('<section class="grp" data-g="%s"><h2 class="gh" tabindex="0"><span class="arr">&#9656;</span> %s. %s <span class="gc">%d items</span> <span class="gd"></span></h2><div class="gb">%s</div></section>'
              % (g, g, E(title), len(its), "".join(h_item(it) for it in its)))
cap = "".join('<div class="item" data-id="11.%d"><label class="top"><input type="checkbox"> <span class="num">11.%d</span> <b>%s</b></label> <span class="chip">Standards 20.6: captured, never generated</span><div class="row">%s<div class="old"><div class="why"><b>What to do:</b> %s</div><div class="loc">On disk: %s</div></div></div>%s</div>'
              % (k, k, E(e["file"]), thumb(e["full"] if e["state"] != "missing" else ""), E(e["todo"]), E(e["state"]), copy("Full path", e["full"]) if e["full"] else "")
              for k, e in enumerate(e_items, 1))
hg.append('<section class="grp" data-g="11"><h2 class="gh" tabindex="0"><span class="arr">&#9656;</span> 11. Not ChatGPT: real photo or screenshot from Adam <span class="gc">%d items</span> <span class="gd"></span></h2><div class="gb">%s</div></section>' % (len(e_items), cap))
info = "".join('<div class="item info"><b>%s</b>: %s broken picture links, %s renamed (relinked in the next package), %d not found under any name.%s</div>'
               % (E(CLASS_NAME[r[0]]), r[1], r[4], r[5], copy("List", r[6])) for r in f_rows)
hg.append('<section class="grp" data-g="12"><h2 class="gh" tabindex="0"><span class="arr">&#9656;</span> 12. Info only: live pictures that are only renamed <span class="gc">%d classes</span></h2><div class="gb"><p class="note">Not ChatGPT work and nothing to tick. Each class\'s next package relinks these.</p>%s</div></section>' % (len(f_rows), info))

page = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ChatGPT Image Work List</title>
<style>
body{margin:0;background:#EDEAE4;color:#212121;font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;line-height:1.45}
.wrap{max-width:1040px;margin:0 auto;padding:0 16px 60px}
header.mast{padding:22px 0 8px}header.mast h1{margin:0;font-size:1.6em}header.mast p{margin:4px 0 0;color:#5f5a52}
.bar{position:sticky;top:0;z-index:5;background:#EDEAE4;padding:10px 0;border-bottom:1px solid #d6d1c8}
.bar .t{font-weight:600}.track{height:10px;background:#d6d1c8;border-radius:6px;overflow:hidden;margin-top:6px}.fill{height:100%;background:#1B5E20;width:0}
.intro{background:#fff;border-radius:10px;padding:14px 18px;margin:16px 0}
.btns button{font:inherit;padding:6px 12px;margin-right:8px;border-radius:8px;border:1px solid #bdb6aa;background:#fff;cursor:pointer}
.grp{background:#fff;border-radius:10px;margin:14px 0;overflow:hidden}
.gh{margin:0;font-size:1.05em;padding:12px 16px;cursor:pointer;border-left:6px solid #0D47A1;user-select:none}
.grp[data-g="1"] .gh{border-color:#B71C1C}.grp[data-g="2"] .gh{border-color:#993300}.grp[data-g="3"] .gh{border-color:#4A148C}.grp[data-g="11"] .gh{border-color:#5d4037}.grp[data-g="12"] .gh{border-color:#757575}
.arr{display:inline-block;transition:transform .15s}.grp.open .arr{transform:rotate(90deg)}
.gc,.gd{font-weight:400;color:#6d675e;font-size:.85em;margin-left:6px}
.gb{display:none;padding:4px 16px 12px}.grp.open .gb{display:block}
.item{border-top:1px solid #ece8e1;padding:14px 0}.item.done{opacity:.45}
.item .top{cursor:pointer}.num{color:#6d675e;font-variant-numeric:tabular-nums}
.act{font-size:.78em;font-weight:700;border-radius:6px;padding:2px 7px;color:#fff}.act.rep{background:#B71C1C}.act.add{background:#1B5E20}
.chip{display:inline-block;font-size:.75em;background:#f3efe7;border:1px solid #d6d1c8;border-radius:10px;padding:1px 8px}
.row{display:flex;flex-wrap:wrap;gap:14px;margin-top:8px}
.ths{flex:0 0 220px;max-width:100%;display:flex;flex-direction:column;gap:6px}
.th{flex:0 0 auto;max-width:100%;min-height:90px;background:#f7f5f1;border:1px solid #e0dbd2;border-radius:8px;display:flex;align-items:center;justify-content:center;overflow:hidden}
.th img{max-width:100%;max-height:160px;display:block}.th .miss{display:none;color:#6d675e;font-size:.85em}.th.gone img{display:none}.th.gone .miss{display:block}
.th.none{color:#6d675e;font-size:.85em;text-align:center;padding:8px}
.old{flex:1 1 300px;min-width:0}.why,.what{font-size:.92em;margin-top:4px}.what{margin-top:10px}
.loc{font-size:.85em;color:#6d675e;margin-top:4px}
.cb{margin-top:6px}.cl{display:block;font-size:.75em;color:#6d675e;text-transform:uppercase;letter-spacing:.03em}
.copy{background:#f7f5f1;border:1px solid #e0dbd2;border-radius:6px;padding:6px 8px;cursor:pointer;font-family:Menlo,"Courier New",monospace;font-size:.82em;white-space:pre-wrap;word-break:break-word;margin:2px 0 0}
pre.copy{max-height:160px;overflow:auto}.copy.ok{background:#e8f5e9;border-color:#1B5E20}.copy.ok::after{content:"  copied!";color:#1B5E20;font-weight:600}
.item.info{opacity:1}.note{color:#6d675e}footer{color:#6d675e;font-size:.85em;margin-top:30px}
</style></head><body><div class="wrap">
<header class="mast"><h1>ChatGPT Image Work List: All Classes</h1><p>Every DAPR picture still to make in ChatGPT, each with its action, file name, full save path, old image and what to create, checked against the files on disk on """ + dt.date.today().isoformat() + """. rev """ + REV + """.</p></header>
<div class="bar"><div class="t"><span id="done">0</span> / <span id="tot">0</span> fixed</div><div class="track"><div class="fill" id="fill"></div></div></div>
<div class="intro"><b>How to use.</b> Work top to bottom. Each item shows the old image beside what is wrong with it. <b>REPLACE</b> (red) means save over the file already at the path; <b>ADD NEW</b> (green) means nothing is there yet. Click the prompt to copy it into a new ChatGPT chat (one image per chat), then save the result at the full save path: click Folder, press Command Shift G in the Save dialog, and use the File name. Tick the box when it is saved; progress is kept in this browser. Then tell Claude which ones are saved. Groups 11 and 12 are not ChatGPT work.</div>
""" + '<div class="intro"><b>Instructions for ChatGPT.</b> You are making images for Adam Olson\'s Utah Valley University audio courses (DAPR). Work through the items below in order, one image per item.<ol>' + "".join("<li>%s</li>" % E(re.sub(r"^\d+\. ", "", s)) for s in GPT_STEPS) + '</ol>Decisions already made by Adam, for every item:<ul>' + "".join("<li>%s</li>" % E(s) for s in GPT_RULES) + '</ul></div>' + """
<div class="btns"><button id="ex">Expand All</button><button id="co">Collapse All</button></div>
""" + "".join(hg) + """
<footer>Owner: Adam Olson, UVU DAPR. Companion file: 2026-09-30 ChatGPT Image Work List - All Classes.md (Notes and Briefs). Built by Build-Tools/image_work_list.py from the Priorities, TO DO and seven Presentations briefs in the Canvas repo.</footer>
</div>
<script>
(function(){
var K="cgwl-2026-09-30:";
function get(k){try{return localStorage.getItem(K+k)}catch(e){return null}}
function set(k,v){try{if(v)localStorage.setItem(K+k,"1");else localStorage.removeItem(K+k)}catch(e){}}
var boxes=document.querySelectorAll(".item[data-id] input[type=checkbox]");
function tally(){var d=0;boxes.forEach(function(b){if(b.checked)d++});document.getElementById("done").textContent=d;document.getElementById("tot").textContent=boxes.length;document.getElementById("fill").style.width=(boxes.length?100*d/boxes.length:0)+"%";
document.querySelectorAll(".grp").forEach(function(g){var bs=g.querySelectorAll("input[type=checkbox]");if(!bs.length)return;var n=0;bs.forEach(function(b){if(b.checked)n++});var s=g.querySelector(".gd");if(s)s.textContent=n+" / "+bs.length+" done";});}
boxes.forEach(function(b){var it=b.closest(".item"),id=it.getAttribute("data-id");if(get(id)){b.checked=true;it.classList.add("done")}
b.addEventListener("change",function(){it.classList.toggle("done",b.checked);set(id,b.checked);tally()})});
document.querySelectorAll(".grp").forEach(function(g){var bs=g.querySelectorAll("input[type=checkbox]"),all=bs.length>0;bs.forEach(function(b){if(!b.checked)all=false});
if(!all&&g.getAttribute("data-g")!=="12")g.classList.add("open");
var h=g.querySelector(".gh");function t(){g.classList.toggle("open")}h.addEventListener("click",t);h.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();t()}})});
document.getElementById("ex").onclick=function(){document.querySelectorAll(".grp").forEach(function(g){g.classList.add("open")})};
document.getElementById("co").onclick=function(){document.querySelectorAll(".grp").forEach(function(g){g.classList.remove("open")})};
function fb(s){var t=document.createElement("textarea");t.value=s;document.body.appendChild(t);t.select();try{document.execCommand("copy")}catch(e){}document.body.removeChild(t)}
function cp(el){var s=el.textContent;function ok(){el.classList.add("ok");setTimeout(function(){el.classList.remove("ok")},1200)}
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(s).then(ok,function(){fb(s);ok()})}else{fb(s);ok()}}
document.querySelectorAll(".copy").forEach(function(el){el.addEventListener("click",function(){cp(el)})});
tally();
})();
</script></body></html>
"""

# ---------------- one Markdown for ChatGPT to work through ----------------
gp = []; g_ = gp.append
g_("All DAPR courses"); g_("")
g_("# Image work list for ChatGPT: all DAPR classes"); g_("")
g_("Rev %s, %s. %d images. Give this file to the ChatGPT desktop app and say: \"Start at the first item.\"" % (REV, dt.date.today().isoformat(), total)); g_("")
g_("## Instructions for ChatGPT"); g_("")
g_("You are making images for Adam Olson's Utah Valley University audio courses (DAPR). Work through the items below in order, one image per item.")
g_("")
for s in GPT_STEPS: g_(s)
g_("")
g_("Decisions already made by Adam, for every item:")
g_("")
for s in GPT_RULES: g_("- " + s)
g_("")
g_("If this chat gets slow, Adam starts a new chat, gives it this file again and says \"Continue at item N.\"")
g_("")
g_("## Contents"); g_("")
g_("| Group | What | Items |"); g_("|---|---|--:|")
for g, title, its in groups:
    if its: g_("| %s | %s | %d |" % (g, title, len(its)))
g_("")
for g, title, its in groups:
    if not its: continue
    g_("# %s. %s" % (g, title)); g_("")
    for it in its:
        olds = it.get("olds") or ([it["old"]] if it["old"] else [])
        g_("## %s %s (%s)" % (it["num"], it["fname"], CLASS_NAME[it["cls"]])); g_("")
        g_("1. **Action:** **%s**. %s" % (it["action"], "This corrects an existing picture; the new file replaces it." if it["action"] == "REPLACE" else "A new picture; nothing is at this path yet."))
        g_("2. **File name:** `%s`" % it["fname"])
        g_("3. **Save path** (%s):" % ("save over this file" if it["action"] == "REPLACE" else "save the new file here")); g_(""); g_("```"); g_("'" + it["path"] + "'"); g_("```"); g_("")
        if olds:
            g_("4. **Old image%s** (open and look before making the new one):" % ("s" if len(olds) > 1 else "")); g_("")
            for o in olds: g_("```"); g_("'" + o + "'"); g_("```"); g_("")
            g_("   " + it["old_desc"])
        else:
            g_("4. **Old image:** " + (it["old_desc"] if it["old_desc"].startswith("No old picture") else "none. " + it["old_desc"]))
        g_("5. **What to create:** %s. %s. Used on: %s. Alt text: %s" % (it["what"].rstrip("."), it["size"], it["used"].rstrip("."), it["alt"]))
        g_(""); g_("```text"); g_(it["prompt"]); g_("```"); g_("")
gpt_text = "\n".join(gp) + "\n"
OUT_GPT = NB + "/" + NAME + " - For ChatGPT.md"

for name, text in (("md", md_text), ("html", page), ("chatgpt", gpt_text)):
    bad = [c for c in ("—", "–", "‘", "’", "“", "”") if c in text]
    if bad: raise SystemExit("%s has banned characters %r; nothing written" % (name, bad))
    if re.search(r"(?:^|\s)--(?:\s|$)", text, re.M): raise SystemExit(name + " has a free standing double hyphen; nothing written")
missing_core = [i["num"] for i in items if not (i["fname"] and i["path"] and i["prompt"] and i["old_desc"] and i["action"])]
if missing_core: raise SystemExit("items missing one of the five details: %r; nothing written" % missing_core)
open(OUT_MD, "w").write(md_text); open(OUT_HTML, "w").write(page); open(OUT_GPT, "w").write(gpt_text)
print("wrote", OUT_GPT, len(gpt_text), "bytes")
print("open: A %d, B %d, C %d, D %d, total %d" % (C["A"], C["B"], C["C"], C["D"], total))
print("REPLACE %d, ADD NEW %d; old image path given %d of %d" % (sum(1 for i in items if i["action"] == "REPLACE"), sum(1 for i in items if i["action"] == "ADD NEW"), sum(1 for i in items if i["old"]), total))
print("needs Adam %d; renamed lists %d" % (len(e_items), len(f_rows)))
print("problems:", *problems, sep="\n  ")
print("wrote", OUT_MD); print("wrote", OUT_HTML)
