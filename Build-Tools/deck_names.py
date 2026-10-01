#!/usr/bin/env python3
"""
deck_names.py: the Standards 8.0.1 name for a deck, and for the pictures a deck uses (Adam, 2026-09-30).

One naming rule for everything in Canvas Links: a colon becomes __, a slash becomes -, spaces become _, Title Case with
a, an, the, is, and, or, to, of, in, for lowercase unless first, acronyms in capitals, American spellings; never module
numbers (M1), lesson, part or week numbers, years, course codes or counters (_2). Deck names otherwise stay as Adam
wrote them.
"""
import re, html

SMALL = {"a", "an", "the", "is", "and", "or", "to", "of", "in", "for", "vs"}

def title_case(words):
    out = []
    for i, w in enumerate(words):
        if i and w.lower() in SMALL: out.append(w.lower())
        elif w.isupper() or any(c.isupper() for c in w[1:]) or w[:1].isdigit(): out.append(w)
        else: out.append(w[:1].upper() + w[1:])
    return out

def split_camel(tok):
    """VoltageDropResistors -> Voltage_Drop_Resistors; OpAmp -> Op_Amp; leaves macOS, MIDI, LM741, dBu alone"""
    return "_".join(re.findall(r"[A-Z][a-z]+", tok)) if re.fullmatch(r"(?:[A-Z][a-z]+){2,}s?", tok) else tok

def key(s): return re.sub(r"[^a-z0-9]", "", s.lower().replace("&", "and"))

# decks whose rule name comes from their title slide rather than their file name
BY_TITLE = {"Acoustics_2025_Lecture": "Acoustics_Review", "Gain_Staging_2025_Lecture": "Mixers_vs_Recorders"}

def deck_base(stem, module_folder=None):
    """Today's name, minus what the rules ban: Adam keeps his deck names (2026-09-30), so only module numbers, lesson,
    part or week numbers, years, course codes, counters and run-together words change."""
    s = re.sub(r"-(Linked|Embedded)$", "", stem)
    if s in BY_TITLE: return BY_TITLE[s]
    s = re.sub(r"^DAPR_?\d{4}[-_]", "", s)                                   # course codes
    s = re.sub(r"(^|[_-])M\d{1,2}(?=[_-]|$)", r"\1", s)                    # module numbers
    s = re.sub(r"(^|[_-])(Lesson|Part|Week|Module|Unit|Day)_\d+(?=[_-]|$)", r"\1", s, flags=re.I)
    s = re.sub(r"[_-]20\d\d(?=[_-]|$)", "", s)                              # years
    s = re.sub(r"_Lecture$", "", s)
    s = re.sub(r"(?<!Layer)(?<!Layers)(?<!Mix)_\d{1,2}$", "", s)             # counters (not OSI Layer 1 or Mix 2; a model
                                                                                # number like 1176 is 3+ digits and stays)
    s = re.sub(r"__+", "__", s).strip("_-")
    parts = re.split(r"(__|-)", s)
    out = []
    for p in parts:
        if p in ("__", "-"): out.append(p); continue
        out.append("_".join(w for x in p.split("_") for w in split_camel(x).split("_") if w))
    return "".join(out)

# Picture names: <Base>-<Subject>.<ext>, the subject from the alt text, else the slide title; never numbered.
DESIGN = {"icon", "checkmark", "check mark", "warning", "logo", "bullet", "arrow", "divider", "decorative", "graphic"}

def clean_alt(t):
    t = html.unescape(t or "").replace("\r", "\n")
    t = re.sub(r"(?is)\s*description automatically generated.*$", "", t)
    t = re.sub(r"(?i)^(a picture containing|a close up of( a)?|an? (image|photo|picture) of)\s*", "", t)
    t = re.split(r"\s[|｜]\s?|\s[-:]\s(?=[A-Z0-9][\w.]*$)", t)[0]      # "Name | Sweetwater", "Buy Mac Studio - Apple"
    t = t.split("\n")[0].strip()
    m = re.fullmatch(r"(?i)(?:[\w.\- ]*/)*([\w.\- ]+)\.(png|jpe?g|gif|tiff?|svg|emf|wmf|bmp|webp)", t)
    if m and "/" in t or m and "_" in m.group(1):          # alt text that is a file path or file name: its stem says what it is
        t = m.group(1).replace("_", " ").replace("-", " ")
    if re.fullmatch(r"(?i)[\w\-. ]+\.(png|jpe?g|gif|tiff?|svg|emf|wmf|bmp)|(picture|image|graphic|figure|slide|content placeholder|screenshot|screen shot|preencoded)\s*\d*|\d+", t): return ""
    return t

def words(t):
    t = (t or "").replace("&", " and ").replace("'", "").replace("’", "")
    return re.findall(r"[A-Za-z0-9]+", t)

def is_design(alt, decorative=False):
    return decorative or html.unescape(alt or "").strip().lower() in DESIGN

def place(g, slide_w=12192000, slide_h=6858000):
    """a position word for a picture: Top_Left, Right, Bottom, Center"""
    if not g: return []
    x, y, w, h = g; cx, cy = (x + w / 2) / slide_w, (y + h / 2) / slide_h
    v = "Top" if cy < 0.36 else ("Bottom" if cy > 0.64 else "")
    hz = "Left" if cx < 0.36 else ("Right" if cx > 0.64 else "")
    return [p for p in (v, hz) if p] or ["Center"]

def subject_candidates(alt, title, g):
    """Names to try in order until one is free in this deck"""
    def short(w, n):
        w = w[:n]
        while len(w) > 2 and w[-1].lower() in SMALL | {"with", "on", "at", "by", "from", "showing", "shows", "that", "its"}: w = w[:-1]
        return w
    a = words(clean_alt(alt)); t = words(clean_alt(title)); base = short(a, 6) or short(t, 6) or ["Picture"]
    out = [base, short(a, 9) or base, base + place(g)]
    if t and short(t, 5) != base[:5]: out.append(base + ["on"] + short(t, 5) + place(g))
    return ["_".join(title_case(c)) for c in out]
