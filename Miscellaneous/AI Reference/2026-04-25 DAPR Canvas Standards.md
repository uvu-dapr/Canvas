# DAPR Canvas Standards (AI Reference)

UVU Digital Audio Production. Apply to all Canvas content. Section 508 + WCAG 2.1 AA mandatory. Canvas Accessibility Checker must show 0 issues before publish.

## 1. Canvas HTML Hard Rules

- All CSS inline via `style=""`. No `<style>`, no external CSS, no `<link>`.
- No JavaScript. `<script>` is stripped.
- No `<h1>` in body. Canvas provides H1 from page title. Start at H2.
- Fonts only: `Arial, Helvetica, sans-serif` | `Georgia, "Times New Roman", serif` | `"Courier New", Courier, monospace`
- Hex codes only. No rgba(), CSS vars, @font-face, Google Fonts.
- No `display:flex` for icon+text. Use `<table role="presentation">`.
- No em dashes or `--` in visible text. Use ` - ` (space-hyphen-space).
- UTF-8 only. Straight quotes.
- Output: only body content. No `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`.

## 2. Accessibility

- Every `<img>`: `alt="..."` (<120 chars) or `alt=""` for decorative.
- Every `<a>`: `title="..."` required. Never "click here"/"read more". Tabs that open new windows must say so.
- Headings: H2 first, no skipped levels (no H2→H4).
- **Data tables** (rubrics, specs, comparisons): require `<caption>` (plain text, NO style attribute), `<thead>` with `<th scope="col">`, `<tbody>`. Two-column comparison with labeled headers IS a data table.
- **Layout tables** (side-by-side icon+text): `role="presentation"`, no caption, no `<th>`.
- **Decorative banners/totals**: use `<div>`, never `<table>`.

## 3. Color Palette (WCAG AA verified on white unless noted)

- Body text: `#212121` (16.1:1)
- Links/blue: `#0D47A1` (8.6:1)
- Green/required: `#1B5E20` (8.4:1)
- Red: `#B71C1C` / `#C62828`
- Orange text: `#993300` ✅. **NEVER `#CC4400`** (Canvas flags it)
- Orange header bg: `#E65100` (Panorama false positive — keep, do not change)
- Gold bg `#F9A825`: requires DARK text `#212121` (white = 2.9:1, fails)

### Module Header Color Sequence (resistor code, locked)

1. Brown #5D4037 / white
2. Red #B71C1C / white
3. Orange #E65100 / white
4. Yellow #FBC02D / **black #212121**
5. Green #1B5E20 / white (default)
6. Blue #0D47A1 / white
7. Violet #4A148C / white
8. Grey #424242 / white
9. Pink #C2185B / white bold
10. Black #000000 / white

## 4. Callout Boxes — Six Approved Types

Every callout uses the SAME template. Swap three things per type: filename, border-left hex, background hex.

| Type | Filename | Border | Background | When |
|---|---|---|---|---|
| Required | Callout_Required.svg | #1B5E20 | #E8F5E9 | Mandatory rules, program standards |
| Note | Callout_Note.svg | #0D47A1 | #E3F2FD | Clarifications, reminders, context |
| Warning | Callout_Warning.svg | #F57F17 | #FFF8E1 | Common mistakes, gotchas |
| Critical | **Callout_Avoid.svg** | #C62828 | #FBE9E7 | Hard rules, prohibitions |
| Tip | Callout_Tip.svg | #4A148C | #F3E5F5 | Shortcuts, optional improvements |
| FAQ | Callout_FAQ.svg | #AD1457 | #FCE4EC | Anticipated student Q&A |

**Critical type uses Callout_Avoid.svg** (filename never renamed per never-rename rule).

### Canonical Callout Template

```html
<table role="presentation" style="width:100%; background-color:#E3F2FD; border-left:4px solid #0D47A1; border-collapse:collapse; margin:16px 0; border-radius:0 4px 4px 0;">
  <tr>
    <td style="width:38px; padding:12px 8px 12px 14px; vertical-align:top;">
      <img src="https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/Callout_Note.svg" alt="Note" width="22" height="22">
    </td>
    <td style="padding:12px 14px 12px 4px;">
      <p style="margin:0;"><strong>Note:</strong> Content here.</p>
    </td>
  </tr>
</table>
```

Tip vs FAQ: Tip = unprompted instructor advice. FAQ = phrased as Q&A.

## 5. Icon Library

**ALL icons are `<img>` tags from GitHub. Never inline SVG. Never upload to Canvas. Never `github.com/blob/...` URLs (returns HTML page, breaks image).**

Base URL: `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/`

Sizing: 22×22 in callouts | 36×36 standalone email/contact | 20×20 inline next to text (add `style="vertical-align:middle;"`)

### All Filenames

**Callout (6):** Callout_Required, Callout_Note, Callout_Warning, Callout_Avoid (=Critical), Callout_Tip, Callout_FAQ

**Feedback Quality (6):**
- Feedback_Not_Helpful.svg — red stroke #B71C1C, light red rows
- Feedback_Not_Helpful_white.svg — white stroke, dark red header #B71C1C only
- Feedback_Helpful.svg — gold stroke #F9A825, light gold rows
- Feedback_Helpful_dark.svg — dark stroke #212121, gold header #F9A825 only (white on gold fails contrast)
- Feedback_Best.svg — green stroke #1B5E20, light green rows
- Feedback_Best_white.svg — white stroke, dark green header #1B5E20 only

**Submission (8):**
- Submit_Upload — generic file upload
- Submit_Download — instructor-provided download
- Submit_Audio — WAV/MP3/AIFF
- Submit_PDF — PDF/DOCX/TXT
- Submit_PTX — .ptx file only (no zip)
- Submit_Session — full PT session zipped (.ptx + Audio Files + Fade Files)
- Submit_ZIP — non-session zip (stems, bundles)
- Submit_Video — MP4/MOV

**Action (5):** Action_Checklist, Action_Deadline, Action_Email, Action_External_Link, Action_Peer

### Feedback Quality Table — full color spec

Three-column comparison table for teaching actionable peer-review feedback. Use the `_white` icon for Not Helpful and Best (white on dark header). Use `_dark` icon for Helpful (dark on gold header — white fails 4.5:1 contrast).

| Level | Header bg | Header text | Row bg | Row text | Icon stroke |
|---|---|---|---|---|---|
| Not Helpful | #B71C1C | #FFFFFF | #FFEBEE | #B71C1C | #FFFFFF (use _white file) |
| Helpful | #F9A825 | #212121 | #FFFDE7 | #212121 | #212121 (use _dark file) |
| Best | #1B5E20 | #FFFFFF | #E8F5E9 | #212121 | #FFFFFF (use _white file) |

Examples by level:
- Not Helpful: vague, emotional, unactionable ("sounded weird")
- Helpful: specific enough to identify the issue ("the low end felt muddy")
- Best: specific + constructive + immediately actionable ("the kick at 2:14 is clipping the master bus — pull it down 2 dB and re-bounce")

### Inline Icon Pattern

```html
<img src="https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/Action_Checklist.svg" alt="Checklist" width="24" height="24" style="vertical-align:middle; margin-right:6px;">
```

## 6. Standard Page Skeleton

```html
<div style="font-family:Arial, Helvetica, sans-serif; max-width:900px; margin:0 auto; color:#212121; line-height:1.6;">

  <!-- Title bar — color from module sequence (green default) -->
  <h2 style="background-color:#1B5E20; color:#ffffff; padding:16px 20px; font-size:1.4em; border-radius:4px;">Assignment Title</h2>

  <p style="font-size:1em; margin:16px 0;">Brief description.</p>

  <!-- Section heading -->
  <h2 style="color:#0D47A1; font-size:1.3em; border-bottom:2px solid #0D47A1; padding-bottom:4px;">Objectives</h2>
  <ul><li>Objective.</li></ul>

  <!-- Data table -->
  <table style="width:100%; border-collapse:collapse;">
    <caption>Grading Rubric</caption>
    <thead><tr>
      <th scope="col" style="background:#0D47A1; color:#fff; padding:8px;">Criteria</th>
      <th scope="col" style="background:#0D47A1; color:#fff; padding:8px;">Points</th>
    </tr></thead>
    <tbody><tr>
      <td style="padding:8px; border:1px solid #ccc;">Criterion 1</td>
      <td style="padding:8px; border:1px solid #ccc;">50</td>
    </tr></tbody>
  </table>

</div>
```

## 7. Module & Page Naming (Option D)

**Module:** `Topic: M# - Descriptive Title (Week ##)` — e.g., `Sound: M3 - The Decibel (Week 03)`. At rollover update only the week parenthetical.

**Page:** `Topic: Descriptive Title` (no module #, no week, no part #) — e.g., `Sound: The Decibel`, `Networking: Address Resolution Protocol`, `EQ: EQ Lab`. Pages are never renamed.

## 8. Student File Naming

Pattern with song: `LastName, FirstName - Assignment Name - Song Name.ext`
Without song: `LastName, FirstName - Assignment Name.ext`

- Comma after LastName is literal
- Separator: space-hyphen-space ` - `
- Replace colons in page name with ` - ` for filename
- Strip apostrophes, commas, all other punctuation from song names
- Zip + .ptx + WAV must share base name (Canvas only shows zip in SpeedGrader)

Examples:
- `Smith, John - EQ - EQ Lab - Dont Think Twice Its All Right.wav`
- `Smith, John - Sound - The Decibel.pdf`

Prohibited: `Untitled.ptx`, `SmithJohn_EQLab_X.ptx` (underscores), retained colons, dropped topic prefix.

## 9. GitHub Image Repository

Repo: `https://github.com/uvu-dapr/Canvas` | Always `raw.githubusercontent.com`, never `github.com/blob/...` in Canvas.

**Only image files** (SVG, JPG, PNG, GIF). No CSS, JS, HTML, PDFs, audio, video, sessions, zips.

**Folder naming:** underscores join words within concept, hyphens separate segments.
- `dapr-2000/sound-the_decibel/`
- `dapr-3255/networking-address_resolution_protocol/`
- `dapr-2000l/eq-eq_lab/`

**Page → folder:** strip colon, lowercase, spaces → `_`, prefix topic with hyphen.
- "Sound: The Decibel" → `sound-the_decibel/`
- "EQ: EQ Lab" → `eq-eq_lab/`

**NEVER rename or move existing files.** Replace in place using same filename.

### Vertical image stacks: use divs, not tables

```html
<div style="margin:12px 0;">
  <div style="margin-bottom:16px;">
    <p style="font-weight:bold;">Before</p>
    <img src="..." alt="..." style="max-width:100%; height:auto;">
  </div>
  <div>
    <p style="font-weight:bold;">After</p>
    <img src="..." alt="..." style="max-width:100%; height:auto;">
  </div>
</div>
```

### Pre-build 5 questions
1. Shared (`All/`) or course-specific (`dapr-XXXX/`)?
2. Exact course folder?
3. Exact subfolder (Option D conversion)?
4. Exact filenames pushed?
5. Committed AND pushed in GitHub Desktop?

## 10. QTI Quiz Standards

- QTI 1.2 only. 2.0/2.1 may be downgraded.
- Zip: `imsmanifest.xml` at root + quiz XML.
- Manifest xmlns: `http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1`
- Resource type: `imsqti_xmlv1p2`
- Each `<item>` needs unique `ident` (random hex).
- HTML in `mattext`: `texttype="text/html"`, encode `<` as `&lt;` etc.
- True/False: `ident="true_answer"` and `ident="false_answer"`.
- `points_possible` set on every question.
- **Every `<item>`'s `title` = question bank/category name** (all questions in same bank share one title string).

### Question Design

- ❌ Never "All of the above" / "None of the above"
- ❌ No essay, file upload, manual grading
- ✅ MC (single correct), T/F (unambiguous), Matching, Numeric, Short answer (exact match)
- Each distractor must stand independently and be plausible alone
- Min 3 options for MC

### New Quizzes
Always import via QTI 1.2 first, then convert. Verify post-conversion: points, ≥20% spot check, shuffle, attempts, time limit, display, no essays, Student View tested.

## 11. Rubric CSV

**No commas in ANY field.** Canvas splits on commas → silent column misalignment → 0 points awarded with no error message. Replace with "and"/"or".

Header (exact, case-sensitive):
```
Rubric Name, Criteria Name, Criteria Description, Criteria Enable Range, Rating Name, Rating Description, Rating Points, Rating Name, Rating Description, Rating Points, Rating Name, Rating Description, Rating Points
```

Generate with Python `csv.writer` + `QUOTE_ALL`. Verify every row = exactly 13 columns.

Filename: `COURSE_A#_Rubric.csv` (e.g., `DAPR3345_A4_Rubric.csv`).

### Standard 3-Level Scale

- Full Credit: 100% of criterion points — all criteria met
- Partial Credit: 50% (round to whole) — incomplete or missing evidence
- No Credit: 0 — not submitted or fails minimum

## 12. Assignment Points

**Lab / Short (25 pts)** — 1-2 hrs. All assignments in `*L` courses. Rubric: 4 criteria summing to 25 (e.g., 6+6+6+7) OR WAV 10 + PDF 15.

**Major Mix / Final (100 pts)** — 4-8 hrs.
- Zipped PT session: 40
- Stereo bounce WAV: 20
- PDF docs: 40

Zip contains: `.ptx`, `Audio Files/`, `Fade Files/`. Use File > Save Copy In with "Copy All Audio Files" before zipping.

## 13. PDF Documentation Block

For assignments requiring PDF + session. Copy-paste block structure:

1. Filename line in monospace at top (PDF naming convention)
2. Assignment title with course + institution
3. "Keep with next" instruction line (verbatim below)
4. Numbered items: `**Item Name (X pts)**` line 1, description line 2, `[ Screenshot here ]` line 3

Required instruction line (verbatim):
> After pasting this into Word, select each numbered item line and apply Format > Paragraph > Line and Page Breaks > Keep with next. This prevents a section label from appearing alone at the bottom of a page while its screenshot is on the next page.

**Point values in copy-paste block must match rubric exactly.** Format: `1. EQ (15 pts)` — not `1. EQ`.

## 14. AI Voice Rules

Sound like the instructor wrote it. Decisive, not conditional.

- ❌ "if required", "if requested", "if applicable", "depending on", "you may", "optional unless", "might want to"
- ✅ "Submit X.", "Configure as follows.", "Include two screenshots that show..."

When unsure whether to be conditional or decisive, choose decisive.

## 15. DAPR Course List

| Course | Title | Lab? |
|---|---|---|
| DAPR 2000 | Digital Audio Essentials | No |
| DAPR 2000L | Digital Audio Essentials Lab | Yes (25 pt) |
| DAPR 2010 | Core Recording | No |
| DAPR 2010L | Core Recording Lab | Yes (25 pt) |
| DAPR 2020 | Core Mixing | No |
| DAPR 2020L | Core Mixing Lab | Yes (25 pt) |
| DAPR 2080 | Podcast and Radio Production | No |
| DAPR 2255 | Audio Hardware I | No |
| DAPR 3010R | Digital Lecture Series | No |
| DAPR 3255 | Audio Hardware II | No |
| DAPR 3340 | Spatial Audio I | No |
| DAPR 3345 | Spatial Audio II | No |

## 16. Panorama (PowerPoint scans)

Severity: Severe (tanks score) | Major (medium penalty) | Minor (cosmetic).

PowerPoint requirements:
- Every slide has a Title placeholder (not text box). Off-slide placeholder at x=-10000000 y=-10000000 EMU if no visible title.
- Unique slide titles.
- Alt text on all images or marked decorative (right-click > Edit Alt Text).
- Reading order verified in Selection Pane (read bottom-to-top in list).
- Tables: Header Row checked, no merged or split cells.
- Section names unique and descriptive.

## 17. Canvas Imports

| Situation | Format |
|---|---|
| Roll forward at UVU | Copy a Canvas Course |
| Share complete course externally | Canvas Export Package (.imscc) |
| Quiz bank only | QTI .zip |
| Publisher cartridge | Common Cartridge 1.x |
| Pro Tools sessions/stems | Unzip into folder |

Don't import Automatic Missing Policy during rollovers — use "Don't Import Policy" until due dates updated.

## 18. Common AI Mistakes (Quick Fixes)

- Inline `<svg>` for icons → replace with `<img>` from GitHub raw URL
- `github.com/blob/...` URL → change to `raw.githubusercontent.com`
- Invented icon filenames or callout colors → use only the approved set above
- `display:flex` for icon+text → use 2-cell `<table role="presentation">`
- `rgba()` colors → hex codes
- H1 in body → H2
- Caption with style attribute → plain `<caption>` text only
- Table for totals/banner → `<div>`
- Link without title → add `title="..."`
- `<!DOCTYPE>`/`<html>` in output → strip
- `#CC4400` → `#993300`
- "All/None of the above" → independent distractors
- Em dash or `--` → ` - `
