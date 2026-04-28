# DAPR Canvas Standards (AI Reference)

UVU Digital Audio Production. Apply to all Canvas content. Section 508 + WCAG 2.1 AA mandatory. Canvas Accessibility Checker must show 0 issues before publish.

## 1. Canvas HTML Hard Rules

- All CSS inline via `style=""`. No `<style>`, no external CSS, no `<link>`.
- No JavaScript. `<script>` is stripped.
- No `<h1>` in body. Canvas provides H1 from page title. Start at H2.
- Fonts only: `Arial, Helvetica, sans-serif` | `Georgia, "Times New Roman", serif` | `"Courier New", Courier, monospace`
- Hex codes only. No rgba(), CSS vars, @font-face, Google Fonts.
- **No `<table>` tags anywhere unless it is a true data table.** Canvas Panorama flags every `<table>` for missing header/caption regardless of `role="presentation"`. Use `<div>` with inline `<img alt="..." style="vertical-align:middle">` for icon+text layouts.
- No `display:flex`, `display:table`, or `display:table-cell` on `<div>`. Canvas treats CSS-table divs as tables and flags them too. Use `position:relative` + `position:absolute` or simple inline-block patterns instead.
- No em dashes or `--` in visible text. Use ` - ` (space-hyphen-space).
- UTF-8 only. Straight quotes.
- Output: only body content. No `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`.
- **Empty divs used as visual separators get stripped by Canvas.** Replace `<div style="border-top:3px solid ...">` with `<hr style="border:none; border-top:3px solid ...; margin:0;">`. The `<hr>` is a void element and survives Canvas paste.

## 2. Accessibility

- Every `<img>`: `alt="..."` (<120 chars) or `alt=""` for decorative.
- Every `<a>`: `title="..."` required. Never "click here"/"read more". Tabs that open new windows must say so.
- Headings: H2 first, no skipped levels (no H2→H4).
- **Data tables** (rubrics, specs, comparisons) are the ONLY place `<table>` is allowed. Require `<caption>` (plain text, NO style attribute), `<thead>` with `<th scope="col">`, `<tbody>`. Two-column comparison with labeled headers IS a data table.
- **Layout tables are deprecated.** Even `<table role="presentation">` triggers Canvas Panorama "Table does not have a header" / "Table does not have a caption" errors. Replace ALL layout tables with `<div>` + inline `<img>` patterns.
- **Icon+text rows, callouts, banners, totals, checklists**: use `<div>` only. Never `<table>`. Never `display:table`.
- **Gray placeholder text fails contrast.** `#555555` on white fails WCAG AA at small font sizes. Use `#616161` minimum (5.9:1) for italic placeholder text like `[ Screenshot here ]` or `[ Write your answer here ]`. For real body content, use `#212121`.

### How Canvas Panorama scans for table errors

Canvas Panorama (the accessibility scanner) flags `<table>` AND CSS-table-emulating divs (`display:table`, `display:table-cell`). Workarounds that DO work:
- Plain `<div>` with `<img style="vertical-align:middle">` immediately followed by text
- `<div>` with `position:relative` parent and `position:absolute` child for offset elements (number badges, icons in fixed slots)
- Padding-left + absolutely positioned number/icon badge for indented numbered lists

If Canvas Panorama still shows table errors after you've replaced all `<table>` tags, search for `display:table` and replace those too.

## 3. Color Palette (WCAG AA verified on white unless noted)

- Body text: `#212121` (16.1:1)
- Placeholder/muted text: `#616161` (5.9:1) - minimum for any visible italic placeholder text. Never use `#555555` or lighter on white.
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

**Common AI mistake on borders:** Warning border is `#F57F17`, NOT `#E65100` (that's the orange header bg only). Critical border is `#C62828`, NOT `#B71C1C`. Note bg is `#E3F2FD`, NOT `#E8EAF6`. Use the table above as the only source of truth.

### Canonical Callout Template (div-only, Panorama-safe)

```html
<div style="background-color:#E3F2FD; border-left:4px solid #0D47A1; margin:16px 0; padding:12px 14px;">
  <img src="https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/Callout_Note.svg" alt="Note" width="44" height="44" style="vertical-align:middle; margin-right:10px;">
  <strong style="vertical-align:middle;">Note:</strong> <span style="vertical-align:middle;">Content here.</span>
</div>
```

For multi-line callout content, indent continuation lines with `margin-left:54px` (44px icon + 10px gap) so wrapped text aligns under the heading rather than wrapping under the icon.

Tip vs FAQ: Tip = unprompted instructor advice. FAQ = phrased as Q&A.

## 5. Icon Library

**ALL icons are `<img>` tags from GitHub. Never inline SVG. Never upload to Canvas. Never `github.com/blob/...` URLs (returns HTML page, breaks image).**

Base URL: `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/`

### Sizing (current standard)

- **44×44** - default size for ALL callouts, section headers, checklist row icons, submit-item icons. This is the program-standard size for visible icons.
- **20×20** - tiny inline icons mid-paragraph only (next to a single word). Add `style="vertical-align:middle;"`.
- Always set width AND height attributes explicitly. Never rely on CSS-only sizing.
- Icons inside a section header or callout: place inline as the first child with `vertical-align:middle; margin-right:10px;` on the `<img>` element.

### Icon-and-text consistency rule

When a section has many checklist rows, do NOT repeat the same icon on every row - meaning is lost. Use this pattern instead:

1. One large (44×44) icon in the section header alongside the section title
2. Numbered rows below with no per-row icons
3. Per-row icons ONLY when each row represents a distinct file type or distinct action (e.g., the What to Submit section uses Submit_Session for the zip and Submit_Audio for the WAV).

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
- Submit_Audio — WAV/MP3/AIFF (also used for media-recording bounce uploads)
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
- Best: specific + constructive + immediately actionable ("the kick at 2:14 is clipping the master bus - pull it down 2 dB and re-bounce")

### Inline Icon Pattern (section header / callout)

```html
<div style="margin:16px 0 6px 0;">
  <img src="https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/Action_Checklist.svg" alt="Checklist" width="44" height="44" style="vertical-align:middle; margin-right:10px;">
  <strong style="font-size:1.1em; vertical-align:middle;">Section Title</strong>
</div>
```

## 6. Standard Page Skeleton

```html
<div style="font-family:Arial, Helvetica, sans-serif; max-width:900px; margin:0 auto; color:#212121; line-height:1.6;">

  <!-- Title bar — color from module sequence (green default) -->
  <h2 style="background-color:#1B5E20; color:#ffffff; padding:16px 20px; font-size:1.4em; border-radius:4px;">Assignment Title</h2>

  <p>Brief description.</p>

  <!-- Section heading -->
  <h2 style="color:#1B5E20; font-size:1.3em; border-bottom:2px solid #1B5E20; padding-bottom:4px;">Goals</h2>
  <ul><li>Goal.</li></ul>

  <!-- Body sections (PDF copy-paste block, rubric tables, etc.) go here -->

  <!-- Before You Submit section: prep callouts (naming convention, bounce prep, checklist refs) -->
  <h2 style="color:#1B5E20; font-size:1.3em; border-bottom:2px solid #1B5E20; padding-bottom:4px;">Before You Submit</h2>
  <!-- callouts here -->

  <!-- What to Submit section: ALWAYS LAST, separated by 3px green hr -->
  <hr style="border:none; border-top:3px solid #1B5E20; margin:0;">
  <div style="margin:16px 0 12px 0;">
    <img src="https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/Action_Deadline.svg" alt="Deadline" width="44" height="44" style="vertical-align:middle; margin-right:10px;">
    <strong style="font-size:1.3em; color:#1B5E20; vertical-align:middle;">What to Submit</strong>
  </div>
  <!-- Upload items here, one div per file with appropriate Submit_* icon -->

</div>
```

### Page Section Order (locked)

1. Title bar (h2, colored background per module sequence)
2. Intro paragraph
3. Goals / Objectives
4. Body sections (How to Build the PDF + copy-paste block, rubric tables, etc.)
5. Peer Feedback (if applicable)
6. **Before You Submit** - prep section containing the file naming convention callout, bounce/zip preparation callouts, and any reference callouts (e.g., link to the module checklist slide)
7. **What to Submit - ALWAYS LAST**, preceded by a 3px green `<hr>` rule for visual separation. This section contains ONLY the upload action items - one div per file the student is uploading, with the appropriate Submit_* icon. No prep instructions, no naming-convention reminders, no "test your zip" notes mixed in here.

This separation is non-negotiable. Students should be able to scroll to the bottom of any assignment page and see exactly which files to upload, with no preparation steps mixed into the action list. All preparation belongs in "Before You Submit" above the green rule.

### Cross-document number-matching (mandatory)

For any assignment with a numbered PDF documentation block + rubric:

- The numbered items in the **PDF copy-paste block** (e.g., `1. EQ (15 pts)`, `2. Compression (15 pts)`)
- The criterion cells in the **rubric table on the assignment page** (e.g., `1. EQ`, `2. Compression`)
- The `Criteria Name` field in the **rubric CSV** (e.g., `1. EQ`, `2. Compression`)

must all use the SAME prefix numbers and identical criterion names. A student should be able to read "criterion 5" in the gradebook and find item 5 in the rubric, in the assignment page, and in the PDF instructions. Mismatch is the most common cause of confusion in SpeedGrader.

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
- When the same WAV is submitted both inside the zip AND as a separate media recording upload, both copies share the same filename - the WAV inside the zip and the standalone WAV are byte-identical files in two locations.

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

**No commas in ANY field.** Canvas splits on commas → silent column misalignment → 0 points awarded with no error message. Replace with "and" or "or" throughout every field.

Header (exact, case-sensitive):
```
Rubric Name, Criteria Name, Criteria Description, Criteria Enable Range, Rating Name, Rating Description, Rating Points, Rating Name, Rating Description, Rating Points, Rating Name, Rating Description, Rating Points
```

Generate with Python `csv.writer` + `QUOTE_ALL`. Verify every row = exactly 13 columns.

Filename: `COURSE_A#_Rubric.csv` (e.g., `DAPR3345_A4_Rubric.csv`).

### Standard 3-Level Scale

- Full Credit: 100% of criterion points - all criteria met
- Partial Credit: 50% rounded to nearest multiple of 5 (round half up). For 5-point criteria, omit Partial Credit and use 2-level scale (Full / No Credit only).
- No Credit: 0 - not submitted or fails minimum

### All point values must be multiples of 5 (program-wide rule)

Every Rating Points value in every rubric CSV must be a multiple of 5. This applies to Full Credit, Partial Credit, and No Credit. Standard mappings:

| Full Credit | Partial Credit | No Credit |
|---|---|---|
| 25 | 15 | 0 |
| 20 | 10 | 0 |
| 15 | 10 | 0 |
| 10 | 5 | 0 |
| 5 | (omit Partial - use Full + No only) | 0 |

Why: keeps the gradebook display clean, prevents fractional grades, and makes total point math obvious to students. Never use values like 7, 8, 12, or 13.

### Criteria Name format (mandatory)

Every `Criteria Name` field begins with the same number used in the assignment page rubric table and the PDF copy-paste block. Format: `N. Item Name` (e.g., `1. EQ`, `2. Compression`, `13. Overall`). The number, period, and space are required. This makes SpeedGrader, the rubric, the assignment page, and the PDF mutually navigable.

## 12. Assignment Points

All point totals and per-criterion values across the program are **multiples of 5**. No exceptions.

**Lab / Short (25 pts)** — 1-2 hrs. All assignments in `*L` courses. Rubric: 4 criteria summing to 25 (e.g., 5+5+5+10) OR WAV 10 + PDF 15. Use whichever per-criterion split is cleanest, but every value must be a multiple of 5.

**Major Mix / Final (100 pts)** — 4-8 hrs.
- Zipped PT session: 40
- Stereo bounce WAV: 20
- PDF docs: 40

**Extended Major Mix (150 pts)** — 6-10 hrs, used when a final mix has 13+ documented elements (full mix with routing, automation, mix buss, cross-fades, etc.). All criteria are multiples of 5.

Zip contains: `.ptx`, `Audio Files/`, `Fade Files/`. Use File > Save Copy In with "Copy All Audio Files" before zipping.

When the assignment also requires a stereo bounce uploaded as a media recording, that WAV file appears in two places: once inside the zip's Bounced Files folder, and once as a standalone media-recording upload. Both copies are byte-identical and share the same filename.

## 13. PDF Documentation Block

For assignments requiring PDF + session. Copy-paste block structure:

1. Filename line in monospace at top (PDF naming convention)
2. Assignment title with course + institution
3. "Keep with next" instruction line (verbatim below)
4. Numbered items: `**N. Item Name (X pts)**` line 1, description line 2, `[ Screenshot here ]` line 3

Required instruction line (verbatim):
> After pasting this into Word, select each numbered item line and apply Format > Paragraph > Line and Page Breaks > Keep with next. This prevents a section label from appearing alone at the bottom of a page while its screenshot is on the next page.

**Point values in copy-paste block must match rubric exactly.** Format: `1. EQ (15 pts)` - not `1. EQ`.

**Item numbers in the PDF block must match the criterion numbers in the rubric CSV and the rubric table on the assignment page.** See §6 cross-document number-matching rule.

Italic placeholder text inside the copy-paste block (`[ Screenshot here ]`, `[ Write your answer here ]`) must use color `#616161` minimum. `#555555` fails Canvas Accessibility Checker contrast at small font sizes.

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
- `display:flex` for icon+text → use `<div>` + inline `<img style="vertical-align:middle">`
- `display:table` / `display:table-cell` on divs → Canvas Panorama flags these as tables. Use `position:relative` + `position:absolute` instead.
- `<table role="presentation">` for layout → Canvas Panorama still flags. Convert to `<div>` layout.
- `rgba()` colors → hex codes
- H1 in body → H2
- Caption with style attribute → plain `<caption>` text only
- Table for totals/banner → `<div>`
- Link without title → add `title="..."`
- `<!DOCTYPE>`/`<html>` in output → strip
- `#CC4400` → `#993300`
- `#555555` for placeholder text → `#616161` (fails contrast at small font sizes otherwise)
- Empty `<div>` used as a separator → Canvas strips it. Use `<hr>` instead.
- Wrong callout border colors (Warning bg `#E65100`, Critical bg `#B71C1C`) → use the §4 table - Warning border `#F57F17`, Critical border `#C62828`.
- "All/None of the above" → independent distractors
- Em dash or `--` → ` - `
- Icons too small (20×20) → use 44×44 for headers and checklist rows
- Same icon repeated on every checklist row → use one icon in the section header instead
- Naming convention or "test your zip" callouts mixed throughout the page → put them in the "Before You Submit" prep section, NOT inside "What to Submit"
- "What to Submit" contains naming-convention or bounce-prep callouts → these belong in "Before You Submit". "What to Submit" is upload action items only.
- "What to Submit" section in middle of page → must be LAST, separated by 3px green `<hr>`
- Rubric criterion cells without numbers (`EQ` instead of `1. EQ`) → numbers are mandatory and must match the PDF copy-paste block and rubric CSV exactly
- Rubric Partial Credit values like 7, 8, 12, 13 → all rubric point values must be multiples of 5. See §11 mapping table.
- Rubric Total includes a non-multiple-of-5 number (e.g., 47, 23) → recheck per-criterion math; every assignment total in the program is a multiple of 5
- 26 Canvas Panorama errors after publish → search file for `<table` and `display:table`. Both must be replaced with pure divs.
