---
name: canvas
description: Apply this skill for ANY task involving Canvas LMS content at Utah Valley University Audio Program. Use it whenever generating Canvas HTML pages, assignment descriptions, quiz questions, QTI quiz files, or any content that will be pasted into Canvas. Also use for Canvas accessibility fixes, WCAG compliance checks, QTI file structure, New Quizzes conversion, quiz question design, import format decisions, AI prompt templates for Canvas, rubric CSV generation, PDF documentation blocks, assignment point system, GitHub image hosting, file naming conventions, and Canvas module/page naming. Always use this skill before generating any Canvas content, even if the request seems simple.
---

# Canvas HTML, QTI, and New Quizzes Reference Manual
Audio Program | Utah Valley University | Accessibility-First Standards

**REQUIRED:** This manual defines the technical, accessibility, structural, and governance standards for all Canvas LMS content in this program. Compliance with Section 508 and WCAG 2.1 AA is mandatory. Content that does not pass the Canvas Accessibility Checker with zero issues must not be published.

---

## QUICK LOAD GUIDE -- Which Parts to Apply

Read the full file on first load. On subsequent tasks, load by priority:

| Task Type | Parts to Load First |
|---|---|
| Any Canvas HTML page | I, II, III, IV, IX, X, XX |
| Quiz or QTI file | V, VI, VII, IX |
| Rubric CSV | XIV |
| PDF documentation block | XVI, XVII |
| Assignment page with point values | XVII |
| Images on any Canvas page | I (1.9 GitHub Rule), XVIII, XIX (GitHub), XXI |
| Module or page naming | XXII |
| Student file naming | XIX (File Naming) |
| Panorama audit | XIII |

---

## PART I -- Core Canvas HTML Standards

### 1.1 Why Canvas HTML Is Different

Canvas strips or ignores large portions of standard HTML and CSS. No external stylesheets, custom fonts, CSS Grid, CSS Flexbox, CSS variables, or JavaScript. Everything that needs to display must use inline styles or simple supported HTML elements.

**Core Rule:** Write HTML as if you have no stylesheet. Every element that needs visual formatting must carry its own inline style attribute.

### 1.2 What Canvas Strips Out

| Removed / Broken | What Happens |
|---|---|
| `<link rel="...">` (external CSS) | Completely removed |
| `<style>...</style>` blocks | Removed in most contexts |
| display: grid | Layout collapses -- not rendered |
| display: flex | Not rendered in older Canvas builds |
| @font-face | Custom font imports -- ignored |
| font-family (external) | Google Fonts / Adobe Fonts -- blocked |
| `<script>` | All JavaScript removed for security |
| position: absolute / fixed | Stripped or broken |
| CSS variables (--var) | Custom properties -- not supported |
| box-shadow, filter | Advanced CSS properties -- usually stripped |
| class= (custom) | No effect without an inline rule |

### 1.3 What Canvas Supports (Safe to Use)

| Allowed | Notes |
|---|---|
| inline style="" | Direct inline styles -- the only reliable CSS method |
| `<table>` | Side-by-side column layout; use percentage widths |
| `<p>`, `<h2>`--`<h6>` | Paragraph and heading tags with inline styles |
| `<strong>`, `<em>` | Bold and italic -- safe |
| `<ul>`, `<ol>`, `<li>` | Lists -- safe |
| `<a href="...">` | Hyperlinks -- add title and aria-label for accessibility |
| `<img>` | Must include alt attribute (accessibility required) |
| `<hr>` | Horizontal rules -- safe for dividers |
| `<br>` | Line breaks -- safe |
| `<div style="...">` | Block containers with inline styles -- safe |
| `<span style="...">` | Inline text styling -- safe |
| `<blockquote>` | Block quotes -- safe |
| `<pre>`, `<code>` | Code samples -- safe |
| `<iframe>` | Media embeds (YouTube, etc.) -- safe if from trusted source |

### 1.4 Layout Rules

- Multi-column layout: use `<table role="presentation">` with percentage widths.
- Stacked lists: use `<div>` elements instead of tables.
- Never use tables for decorative banners, totals, or visual boxes.

```html
<!-- Two-column layout -->
<table role="presentation" style="width:100%; border-collapse:collapse;">
  <tr>
    <td style="width:50%; padding:12px; vertical-align:top;">
      <p>Left column content here.</p>
    </td>
    <td style="width:50%; padding:12px; vertical-align:top;">
      <p>Right column content here.</p>
    </td>
  </tr>
</table>

<!-- Stacked list layout using divs (zero accessibility warnings) -->
<div style="border:1px solid #cccccc; margin:12px 0;">
  <div style="padding:10px 12px; border-bottom:1px solid #cccccc;">
    <strong>Item 1</strong> - description here
  </div>
  <div style="padding:10px 12px;">
    <strong>Item 2</strong> - description here
  </div>
</div>
```

**WARNING:** Do not rely on the Canvas visual editor to produce clean HTML. Always verify in the raw editor (`</>` button). The visual editor often inserts broken inline styles.

### 1.5 Fonts

Canvas supports only system-safe fonts. Always use one of these:

```css
/* Sans-serif (body text, headings) */
font-family: Arial, Helvetica, sans-serif;

/* Monospace (code samples, terminal output) */
font-family: "Courier New", Courier, monospace;

/* Serif (sparingly, for quotes or callouts) */
font-family: Georgia, "Times New Roman", serif;
```

### 1.6 Color and Contrast -- Accessibility Required

All text must meet WCAG 2.1 AA: 4.5:1 for normal text, 3:1 for large text (18pt+ or 14pt bold). Never use color alone to convey meaning.

| Color Combination | Ratio | Result |
|---|---|---|
| #FFFFFF on #1B5E20 | 8.4:1 | PASS -- heading bars |
| #212121 on #FFFFFF | 16.1:1 | PASS -- body text |
| #0D47A1 on #FFFFFF | 8.6:1 | PASS -- links |
| #993300 on #FFFFFF | 7.4:1 | PASS -- warnings/code (use this, NOT #CC4400) |
| #E65100 on #FFFFFF | 4.6:1 | PASS -- dark orange on white only |
| #CC4400 on #FFFFFF | 4.8:1 | MARGINAL -- Canvas checker flags this |
| #FFFF00 on #FFFFFF | 1.1:1 | FAIL -- never use |
| #AAAAAA on #FFFFFF | 2.3:1 | FAIL for body text |

**WARNING:** Never use #CC4400. Always use #993300 or darker for orange-toned text.

**Panorama false positive note:** Panorama always flags #E65100 (orange position 3 in the color sequence) as a Major contrast failure even though white text on #E65100 is 4.6:1 and technically passes WCAG AA. This is a known false positive. Do not change the orange header color -- it is locked at position 3 in the resistor color sequence.

Contrast checker: webaim.org/resources/contrastchecker

### 1.7 Color Sequence System for Page Headers

This program uses a fixed resistor color code sequence for module page header backgrounds. The sequence is locked permanently. Do not change it or substitute colors. File naming determines color, not the page title. Never embed sequence numbers in visible page title text -- ordering numbers belong in filenames only.

| # | Color Name | Hex Code | Text Color | Notes |
|---|---|---|---|---|
| 1 | Brown | #5D4037 | #FFFFFF | |
| 2 | Red | #B71C1C | #FFFFFF | |
| 3 | Orange | #E65100 | #FFFFFF | Panorama false positive -- do not change |
| 4 | Yellow | #FBC02D | #212121 | Exception -- black text only |
| 5 | Green | #1B5E20 | #FFFFFF | Program default header |
| 6 | Blue | #0D47A1 | #FFFFFF | |
| 7 | Violet | #4A148C | #FFFFFF | |
| 8 | Grey | #424242 | #FFFFFF | |
| 9 | Pink | #C2185B | #FFFFFF | Use bold text |
| 10 | Black | #000000 | #FFFFFF | |

### 1.8 Character Encoding Rule (UTF-8)

All Canvas pages and generated HTML must use UTF-8 encoding. The following tag must appear in the `<head>` of any standalone HTML file:

```html
<meta charset="UTF-8">
```

Without UTF-8, characters like quotation marks and apostrophes display as corrupted text (example: `â€œsyncâ€` instead of `"sync"`). This error commonly appears when copying from Word, Google Docs, or AI tools.

All generated HTML must use straight quotes, not smart quotes. If corrupted characters appear, replace them with standard ASCII characters or HTML entities (`&quot;`).

### 1.9 Image Hosting Rule -- GitHub Required for Everything

**REQUIRED:** Every image and SVG file on a Canvas page must be hosted on GitHub and referenced via a raw.githubusercontent.com URL. There are no exceptions.

| Method | Status | Notes |
|---|---|---|
| GitHub raw URL (`raw.githubusercontent.com/...`) | **Required for everything** | All icons, screenshots, photos, diagrams. Every image on every Canvas page. |
| Inline SVG path data pasted into Canvas HTML | **Prohibited** | Never. Every icon including callout box icons must be an `<img>` tag pointing to GitHub. |
| Base64 data URI (`data:image/png;base64,...`) | **Prohibited** | Bloats HTML, Canvas may silently truncate content, impossible to update. |
| Canvas Files upload | **Prohibited for shared assets** | Never for program icons or reusable content. |
| github.com page URL | **Prohibited** | Returns an HTML preview page, not the file. Canvas shows a broken image. |

**Repository base URL:** `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/`
**Icons folder:** `Classes/All/DAPR_Canvas_Icon_Reference/`
**Course assets:** `Classes/dapr-XXXX/topic-assignment_name/`

**Wikimedia Commons hotlink (for CC-licensed photos only):** Use `<figure>/<figcaption>` with full CC BY-SA attribution. See template below.

**Wikimedia Commons attribution template:**

```html
<figure style="margin:20px 0; text-align:center;">
  <img src="WIKIMEDIA_FILE_URL" alt="DESCRIPTION" title="SHORT TITLE"
       style="max-width:100%; height:auto; border:1px solid #cccccc; border-radius:4px;">
  <figcaption style="font-family:Arial, Helvetica, sans-serif; font-size:0.85em;
              color:#5F5E5A; margin-top:6px;">
    PHOTO TITLE by AUTHOR NAME, via
    <a href="COMMONS_FILE_PAGE_URL" title="Image source on Wikimedia Commons"
       target="_blank" aria-label="Image source on Wikimedia Commons (opens in new tab)"
       style="color:#0D47A1;">Wikimedia Commons</a>.
    Licensed under
    <a href="https://creativecommons.org/licenses/by-sa/3.0/"
       title="Creative Commons Attribution-Share Alike 3.0 license"
       target="_blank"
       aria-label="Creative Commons Attribution-Share Alike 3.0 license (opens in new tab)"
       style="color:#0D47A1;">CC BY-SA 3.0</a>.
  </figcaption>
</figure>
```

---

## PART II -- Accessibility Requirements

UVU is required to comply with Section 508 and WCAG 2.1 Level AA. Every Canvas page, assignment description, and quiz must meet these rules.

### 2.1 Images -- Alt Text Is Required

Every `<img>` tag must have an alt attribute. Decorative images use `alt=""`. Informational images must have a meaningful description under 120 characters (Canvas flags anything longer).

```html
<!-- Informational image -->
<img src="waveform.png"
     alt="Sine wave showing one complete cycle at 440 Hz"
     style="max-width:100%; height:auto;">

<!-- Decorative image -->
<img src="divider-bar.png" alt="" role="presentation">
```

### 2.2 Headings -- Use Proper Hierarchy

Canvas Pages have a built-in H1 title (the page name you typed). Content area must start at H2. Never use H1 inside the Canvas content editor body. Never skip heading levels.

**Critical Rule:** H3 as the first heading on a page is a Severe Panorama error. All section headings must be H2 if there is no H2 parent. Never skip from H2 to H4.

```html
<!-- CORRECT -->
<h2>Objectives</h2>
<h3>Step 1: Room Setup</h3>

<!-- WRONG -- skips levels, uses H1 in body -->
<h1>Assignment</h1>
<h4>Some subpoint</h4>
```

### 2.3 Links -- Descriptive Text and Title Required

Never use "click here" or "read more." All links must carry a title attribute.

```html
<a href="https://www.fmod.com/download"
   title="Download FMOD Studio from fmod.com"
   style="color:#0D47A1;">
  fmod.com/download
</a>

<!-- New tab links -- warn the user -->
<a href="..." target="_blank"
   aria-label="FMOD documentation (opens in new tab)">
  FMOD Documentation
</a>
```

### 2.4 Tables -- Data Tables vs. Layout Tables

| Table Type | Required Treatment |
|---|---|
| Data table (rubrics, specs, comparisons) | Must have `<caption>` (plain text, no style), `<thead>` with `<th scope="col">`, and `<tbody>`. No role attribute. |
| Layout table (side-by-side columns) | Must have `role="presentation"`. No caption, no th tags. |
| Decorative list (items stacked vertically) | Use `<div>` elements. Avoids all table accessibility issues. |

**Caption Note:** Canvas strips position:absolute and clip: styles from captions. Use a plain `<caption>` tag with NO style attribute.

**Key Discovery:** `role="presentation"` does NOT always suppress Canvas checker warnings. The only 100% reliable fix for non-data tables is to not use `<table>` at all -- use divs instead.

**Two-column comparison tables are data tables, not layout tables.** A table with labeled column headers ("Does / Does Not" or "Feature / Description") is a data table regardless of visual appearance. It must use `<thead>` with `<th scope="col">`, a `<caption>`, and `<tbody>`. Do not use `role="presentation"` on any table with meaningful column or row labels.

`<caption>` and `<th scope="col">` are ALWAYS required together on every data table. Missing either one is a separate flagged error.

```html
<!-- DATA table -->
<table style="width:100%; border-collapse:collapse;">
  <caption>Microphone Comparison by Type and Polar Pattern</caption>
  <thead>
    <tr>
      <th scope="col" style="background:#0D47A1; color:#fff; padding:8px;">Mic</th>
      <th scope="col" style="background:#0D47A1; color:#fff; padding:8px;">Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:8px; border:1px solid #ccc;">SM58</td>
      <td style="padding:8px; border:1px solid #ccc;">Dynamic</td>
    </tr>
  </tbody>
</table>

<!-- LAYOUT table (or better: use divs instead) -->
<table role="presentation" style="width:100%;">
  <tr>
    <td style="width:50%; padding:12px;">Column 1</td>
    <td style="width:50%; padding:12px;">Column 2</td>
  </tr>
</table>
```

### 2.5 Video and Audio -- Captions and Transcripts

| Content Type | Accessibility Requirement |
|---|---|
| Video (YouTube) | Review and correct auto-captions in YouTube Studio before posting |
| Video (uploaded) | Add a .srt or .vtt caption file in Canvas Media or use Kaltura |
| Audio (podcast style) | Provide a full written transcript as a linked document |
| Recordings of lectures | Auto-caption in Kaltura, then review for accuracy |
| Demo videos (DAW) | Narrate all on-screen actions; caption the narration |

### 2.6 Color -- Do Not Use Color Alone

Always pair color with a text label or symbol.

```html
<!-- WRONG: color alone -->
<p style="color:red;">This answer is wrong.</p>

<!-- CORRECT: color plus label -->
<p style="color:#B71C1C;"><strong>Incorrect:</strong> This answer is wrong.</p>
```

---

## PART III -- Canvas Accessibility Checker

**PROGRAM STANDARD:** Run the Accessibility Checker on every page before publishing. Zero issues is required.

### 3.1 How to Open

1. Open any Page, Assignment, Discussion, or Quiz in edit mode.
2. Click the accessibility icon (person inside a circle) near the right end of the Rich Content Editor toolbar.
3. A panel slides in from the right showing Issue X/Y.
4. Use Prev and Next to navigate. Click Apply after making a fix.
5. When no issues remain: "No accessibility issues were detected."

### 3.2 Common Issues and Fixes

| Issue | Root Cause | Fastest Fix |
|---|---|---|
| First heading should be H2 | Used H1 inside the page body | Change all H1 tags to H2 in raw HTML |
| Text contrast ratio too low | Common offender: #CC4400 | Replace #CC4400 with #993300 |
| Tables should include a caption | No `<caption>` tag, or caption had style Canvas stripped | Add `<caption>` as plain text -- no style attribute |
| Tables should include at least one header | All cells are `<td>`, no `<th>` defined | For data tables: `<th scope="col">`. For layout tables: replace with `<div>` entirely. |
| Image has no alt text | Missing alt attribute | Add `alt="..."` or `alt=""` for decorative |
| Link has no text | `<a>` wraps only an image with no alt text | Add alt text to image or aria-label to the `<a>` tag |
| This link should have a descriptive title | `<a>` tag missing a title attribute | Add `title="Description of where this link goes"` |
| Heading levels skipped | Jumped from H2 to H4 | Add the missing H3 level |

### 3.3 The Table Problem -- Decision Tree

| Situation | Solution |
|---|---|
| Rubric, comparison chart -- real data in rows/columns | Data table: `<caption>` (no style), `<thead>`, `<th scope="col">`, `<tbody>` |
| Side-by-side two-column layout | Layout table with `role="presentation"`. No caption, no th tags. |
| List of items stacked vertically | `<div>` elements -- not a table. Zero checker warnings. |
| Total/summary banner at bottom of page | Styled `<div>` with two `<span>` elements. Never use a table. |

---

## PART IV -- Canvas Page Template

Copy this into the Canvas raw HTML editor. Replace all placeholder text. Do not remove aria, alt, scope, or title attributes.

```html
<div style="font-family:Arial, Helvetica, sans-serif; max-width:900px;
            margin:0 auto; color:#212121; line-height:1.6;">

  <h2 style="background-color:#1B5E20; color:#ffffff; padding:16px 20px;
             font-size:1.4em; border-radius:4px;">
    Assignment Title Here
  </h2>

  <p style="font-size:1em; margin:16px 0;">Brief description.</p>

  <h2 style="color:#0D47A1; font-size:1.3em;
             border-bottom:2px solid #0D47A1; padding-bottom:4px;">
    Objectives
  </h2>
  <ul>
    <li>Learning objective one.</li>
    <li>Learning objective two.</li>
  </ul>

  <table style="width:100%; border-collapse:collapse;">
    <caption>Grading Rubric</caption>
    <thead>
      <tr>
        <th scope="col" style="background:#0D47A1; color:#fff; padding:8px;">Criteria</th>
        <th scope="col" style="background:#0D47A1; color:#fff; padding:8px;">Points</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:8px; border:1px solid #ccc;">Criterion 1</td>
        <td style="padding:8px; border:1px solid #ccc;">50</td>
      </tr>
    </tbody>
  </table>

  <table role="presentation" style="width:100%; background-color:#E3F2FD; border-left:4px solid #0D47A1;
         border-collapse:collapse; margin:16px 0; border-radius:0 4px 4px 0;">
    <tr>
      <td style="width:38px; padding:12px 8px 12px 14px; vertical-align:top;">
        <img src="https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/Callout_Note.svg"
             alt="" width="22" height="22" style="display:block;">
      </td>
      <td style="padding:12px 14px 12px 4px;">
        <p style="margin:0;"><strong>Note:</strong> Submit your file by Friday at midnight.</p>
      </td>
    </tr>
  </table>

  <p>See the
    <a href="YOUR_URL" title="Grading rubric document"
       style="color:#0D47A1; text-decoration:underline;">
      Grading Rubric
    </a>
    for detailed scoring criteria.
  </p>

</div>
```

---

## PART V -- QTI Quiz File Standards

Canvas most reliably supports QTI 1.2. QTI 2.0 and 2.1 do not unlock additional Canvas features and may be downgraded on import.

**PROGRAM STANDARD:** Use QTI 1.2 for all quiz imports.

### 5.1 QTI File Structure

```
my_quiz.zip
  imsmanifest.xml      <-- required: tells Canvas what is in the package
  quiz_abc123.xml      <-- required: contains the actual questions
```

### 5.2 imsmanifest.xml Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="MANIFEST_001"
  xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1
    http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1.xsd">
  <metadata>
    <schema>IMS Content</schema>
    <schemaversion>1.1.3</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource identifier="ASSESSMENT_001"
             type="imsqti_xmlv1p2"
             href="assessment.xml">
      <file href="assessment.xml"/>
    </resource>
  </resources>
</manifest>
```

### 5.3 Question Types -- QTI XML

**Multiple Choice:**
```xml
<item ident="Q001" title="BANK_CATEGORY_NAME">
  <itemmetadata><qtimetadata>
    <qtimetadatafield>
      <fieldlabel>question_type</fieldlabel>
      <fieldentry>multiple_choice_question</fieldentry>
    </qtimetadatafield>
    <qtimetadatafield>
      <fieldlabel>points_possible</fieldlabel>
      <fieldentry>1</fieldentry>
    </qtimetadatafield>
  </qtimetadata></itemmetadata>
  <presentation>
    <material>
      <mattext texttype="text/html">
        &lt;p&gt;What is the standard tuning frequency for A4?&lt;/p&gt;
      </mattext>
    </material>
    <response_lid ident="response" rcardinality="Single">
      <render_choice>
        <response_label ident="a"><material><mattext>432 Hz</mattext></material></response_label>
        <response_label ident="b"><material><mattext>440 Hz</mattext></material></response_label>
        <response_label ident="c"><material><mattext>444 Hz</mattext></material></response_label>
      </render_choice>
    </response_lid>
  </presentation>
  <resprocessing>
    <outcomes>
      <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
    </outcomes>
    <respcondition continue="No">
      <conditionvar><varequal respident="response">b</varequal></conditionvar>
      <setvar action="Set" varname="SCORE">100</setvar>
    </respcondition>
  </resprocessing>
</item>
```

**True / False:**
```xml
<item ident="Q002" title="BANK_CATEGORY_NAME">
  <itemmetadata><qtimetadata>
    <qtimetadatafield>
      <fieldlabel>question_type</fieldlabel>
      <fieldentry>true_false_question</fieldentry>
    </qtimetadatafield>
  </qtimetadata></itemmetadata>
  <presentation>
    <material>
      <mattext texttype="text/html">&lt;p&gt;The question text here.&lt;/p&gt;</mattext>
    </material>
    <response_lid ident="response" rcardinality="Single">
      <render_choice>
        <response_label ident="true_answer"><material><mattext>True</mattext></material></response_label>
        <response_label ident="false_answer"><material><mattext>False</mattext></material></response_label>
      </render_choice>
    </response_lid>
  </presentation>
  <resprocessing>
    <outcomes>
      <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
    </outcomes>
    <respcondition continue="No">
      <conditionvar><varequal respident="response">true_answer</varequal></conditionvar>
      <setvar action="Set" varname="SCORE">100</setvar>
    </respcondition>
  </resprocessing>
</item>
```

**Short Answer / Fill-in-the-Blank:**
```xml
<item ident="Q003" title="BANK_CATEGORY_NAME">
  <!-- question_type: short_answer_question -->
  <presentation>
    <response_str ident="response" rcardinality="Single">
      <render_fib><response_label ident="answer"/></render_fib>
    </response_str>
  </presentation>
  <resprocessing>
    <respcondition continue="No">
      <conditionvar><varequal respident="response">440</varequal></conditionvar>
      <setvar action="Set" varname="SCORE">100</setvar>
    </respcondition>
    <!-- Add more respcondition blocks for alternate correct answers -->
  </resprocessing>
</item>
```

### 5.4 Importing into Canvas

1. Go to your Course and click Quizzes in the left navigation.
2. Click the three-dot menu at the top right and select Import.
3. From the dropdown, select QTI .zip file.
4. Upload your .zip file and click Import.
5. Canvas imports the questions into a new question bank. Add them to any quiz from there.

### 5.5 QTI Accessibility Guidelines

| Content Type | Accessibility Requirement |
|---|---|
| Images in questions | Use HTML `<img>` with alt text inside the mattext tag. Encode `<` and `>` as `&lt;` and `&gt;` |
| Audio clips in questions | Provide a text transcript |
| Tables in questions | Use `<th scope='col'>` or `<th scope='row'>` inside mattext HTML |
| Math notation | Use MathML or LaTeX (Canvas renders both) |
| Answer labels | Always use descriptive text -- never rely on position alone |

### 5.6 QTI Item Title Rule

Set the title attribute on every `<item>` to the question bank or category name. All questions in the same category share the exact same title string. Do not use the question text as the title. The ident attribute handles unique identification.

**Correct -- all questions share the category name:**
```
title="Network Wiring Standards"
title="Network Wiring Standards"
title="Network Wiring Standards"
```

**Incorrect -- unique question text as title:**
```
title="T568A vs T568B primary difference"
title="T568B pin 1 color"
```

Canvas displays the title value in the Move/Copy Questions dialog and the question bank list. When all questions share the category name, the interface shows which bank each question belongs to immediately.

---

## PART VI -- Self-Grading Policy and Question Design Rules

All quizzes in this program use self-grading question types to scale enrollment.

### 6.1 Permitted Question Types

| Question Type | Notes |
|---|---|
| Multiple Choice -- single correct answer | Standard format. Minimum three options per question. |
| True / False | Use only when answer is unambiguously one or the other. |
| Matching | Supported in New Quizzes. Ensure all pairs are clearly defined. |
| Numeric answer | Specify acceptable range or exact value in the resprocessing block. |
| Short answer -- exact match | Provide alternate correct answers as additional respcondition blocks. |

### 6.2 Prohibited Question Types

| Prohibited Type | Reason |
|---|---|
| Essay / long answer | Requires manual grading. Not scalable. |
| File upload | Requires manual review. Not scalable. |
| Any manually graded response | Use a separate submission assignment if manual grading is required. |

### 6.3 Question Construction Rules -- MANDATORY

**NEVER use "All of the above" or "None of the above" as answer options.** These test test-taking skill, not content knowledge.

- Never use "All of the above" as an answer option.
- Never use "None of the above" as an answer option.
- Each distractor must stand independently and be plausible on its own.
- Avoid trick phrasing. Questions test knowledge, not reading traps.
- Keep distractor length consistent. A notably longer correct answer is a tell.
- Do not rely on answer position patterns. Randomize in Canvas settings.
- State what the question is asking in the stem. Do not make students infer the question.
- Use the same terminology in questions that appears in course materials.

---

## PART VII -- New Quizzes Conversion Standard

The required workflow imports via QTI 1.2 then converts to New Quizzes. Do not build directly in New Quizzes without first validating through QTI import.

### 7.1 Conversion Workflow

1. Build quiz questions and export as QTI 1.2 .zip.
2. Import the QTI .zip into Canvas.
3. Canvas creates a question bank from the imported questions.
4. Open the imported quiz and use the Convert to New Quizzes option.
5. Verify all settings manually after conversion -- they do not always transfer correctly.
6. Test using Student View before deployment.

### 7.2 Post-Conversion Verification Checklist

- Points per question match the intended value.
- Correct answers spot-checked (at least 20% of questions).
- Shuffle answers setting confirmed.
- Attempts allowed confirmed.
- Time limit confirmed.
- Question display settings confirmed (all at once vs. one at a time).
- No essay questions present in converted quiz.
- Tested in Student View before deployment.

**REQUIRED:** Always test in Student View before the quiz goes live.

---

## PART VIII -- Canvas Import Formats

### 8.1 Format Reference

| Format | Use Case | What It Imports |
|---|---|---|
| Canvas Course Export Package | Full course migration | Everything: pages, assignments, quizzes, modules, files, rubrics, outcomes, settings |
| Copy a Canvas Course | Semester rollover within UVU | Same as Export Package but done live inside Canvas |
| QTI .zip file | Quiz/question bank import | Quiz questions only -- does not import quiz settings, time limits, or attempts |
| Common Cartridge 1.x | Publisher content or cross-platform sharing | Pages, discussions, quizzes (via QTI), files; no rubrics |
| Blackboard 6/7/8/9/Ultra .zip | Migration from Blackboard LMS | Content areas, assessments, discussions mapped to Canvas equivalents |
| D2L export .zip | Migration from Brightspace | Content modules, quizzes, discussions; mapping approximate |
| Moodle 1.9/2.x | Migration from Moodle LMS | Courses, quizzes, resources mapped to Canvas. Expect conditional logic rebuilds. |
| Unzip .zip into folder | Raw file upload | Extracts files into Course Files only. Use for audio stems and Pro Tools session files. |

### 8.2 Decision Tree

| Situation | Use This Format |
|---|---|
| Rolling a course forward to a new semester at UVU | Copy a Canvas Course |
| Sharing a complete course with another institution | Canvas Course Export Package (.imscc) |
| Importing only a quiz question bank | QTI .zip file |
| Publisher provided a course cartridge | Common Cartridge 1.x Package |
| Uploading Pro Tools session files or audio stems | Unzip .zip file into folder |

**REQUIRED:** No matter which import format you use, always run the Canvas Accessibility Checker on every imported page and quiz before publishing. Imported content almost always has accessibility issues.

---

## PART IX -- Using AI to Build Canvas Content

### 9.1 Core Problem with AI-Generated HTML

AI defaults to modern web practices: Grid, Flexbox, external fonts, CSS variables, JavaScript. All stripped by Canvas. Without explicit instructions, AI output looks correct in a browser but fails in Canvas.

| What AI Does by Default | What Canvas Needs Instead |
|---|---|
| External `<link>` stylesheet or `<style>` block | All styles as inline `style=""` attributes |
| CSS Grid or Flexbox for layout | HTML tables with `role="presentation"` or stacked divs |
| Google Fonts or @font-face | Arial, Georgia, or Courier New only |
| CSS custom properties | Hardcoded hex values in every inline style |
| JavaScript for interactivity | None -- Canvas removes all JS |
| rgba() color functions | Hex codes only |
| Visually-hidden caption technique | Plain `<caption>` with no style attribute |
| `<h1>` as page title inside content | `<h2>` as first heading -- Canvas owns H1 |
| Navigation links to other HTML files | All content lives inside Canvas pages |

### 9.2 Master Prompt for Canvas HTML Pages

Paste this at the start of every AI session before generating Canvas content:

```
You are generating HTML for Canvas LMS (Instructure). Canvas strips most
modern CSS and all JavaScript. Follow these rules exactly:

HTML RULES:
- All CSS must be inline style="" attributes. No <style> blocks, no external CSS.
- Layout: use HTML tables with role="presentation" for side-by-side columns.
  For vertical lists of items, use stacked <div> elements, not tables.
- Fonts: Arial, Georgia, or Courier New only. No Google Fonts.
- No CSS Grid, no Flexbox, no CSS variables, no JavaScript.
- Use hex color codes. Never use rgba().
- Do not include navigation links to standalone HTML files.
- No em dashes and no double dashes (--) anywhere in visible content.
  Use a hyphen with spaces ( - ) as a separator where a dash is needed.
  Double dashes are permitted only inside HTML comments.
- Do not use manual numbered labels (1. 2. 3.) inside div elements when items
  convey a sequence. Use word-based labels (First, Second, Third) or remove
  the number from the label text.

ACCESSIBILITY RULES (Canvas checker must show 0 issues):
- First heading in content area must be <h2>. Never use <h1>.
- All <img> tags need alt="description" or alt="" for decorative images.
  Alt text must be under 120 characters.
- All <a> links need title="where this goes" attribute.
- Data tables (rubrics, specs): require <caption> (plain text, no style),
  <thead> with <th scope="col">, and <tbody>.
- Layout tables: add role="presentation". Or better: use divs instead.
- Never use a <table> for decorative banners or totals. Use a <div>.
- Text color must pass WCAG 4.5:1 contrast on its background.
  Safe colors on white: #212121, #0D47A1, #1B5E20, #993300, #B71C1C.
  Never use #CC4400 -- Canvas flags it.
- Gold background (#F9A825) requires dark text (#212121), not white.
  White on #F9A825 is only 2.9:1 -- fails WCAG AA.

QUIZ RULES (when generating QTI):
- Never use "All of the above" or "None of the above" as answer options.
- Each distractor must stand independently.
- All assessments must be self-grading. No essay questions.

OUTPUT FORMAT:
- Output only the HTML that goes inside the Canvas content editor body.
- Do not include <!DOCTYPE>, <html>, <head>, or <body> tags.
```

### 9.3 Master Prompt for QTI Quiz Files

```
Generate a Canvas QTI 1.2 quiz package as a .zip file ready for import.

TECHNICAL REQUIREMENTS:
- The zip must contain imsmanifest.xml at the root level.
- Use xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" in the manifest.
- Each question must have a unique ident attribute (use random hex strings).
- question_type values: multiple_choice_question, true_false_question,
  short_answer_question, essay_question
- All HTML in mattext tags must use texttype="text/html" and encode < as &lt;
  and > as &gt;
- For true/false questions use ident="true_answer" and ident="false_answer".
- Essay questions do not include a <resprocessing> block.
- Set points_possible for every question.

ITEM TITLE FORMAT:
- Set the title attribute on every <item> to the question bank or category name.
- All questions in the same category share the exact same title string.
- Do not use the question text as the title. Confirm the bank name first.

QUESTION DESIGN REQUIREMENTS:
- Never use "All of the above" or "None of the above."
- Each distractor must be independently plausible.
- Keep distractor length consistent.
- All questions must be self-grading (no essay or file upload).

QUIZ SETTINGS TO SPECIFY:
  Quiz name:
  Number of questions:
  Points per question:
  Question types (MC, T/F, short answer, matching, mixed):
  Shuffle answers: yes/no

SOURCE QUESTIONS:
  [Paste your questions here]
```

### 9.4 Common AI Mistakes to Watch For

| AI Mistake | What to Tell Claude to Fix It |
|---|---|
| Uses rgba() for colors | "Replace all rgba() color values with equivalent hex codes" |
| Puts H1 as first heading | "Change the first H1 to H2 -- Canvas provides H1 from the page title" |
| Table caption uses visually-hidden CSS | "Remove the style attribute from the `<caption>` tag entirely" |
| Uses a table for a points total banner | "Replace the total banner table with a styled `<div>`" |
| Layout table without role="presentation" | "Add role='presentation' to all layout tables that contain no data" |
| Links without title attribute | "Add title='description of destination' to every `<a>` tag" |
| Includes `<!DOCTYPE>` or `<html>` tags | "Output only the content between the `<body>` tags" |
| Uses #CC4400 for orange text | "Replace #CC4400 with #993300" |
| Includes "All of the above" | "Remove all meta-answers. Rewrite as specific independent distractors." |
| Generates essay questions | "Remove all essay questions. Replace with multiple choice or short answer." |
| Uses em dashes or double dashes in visible text | "Replace all em dashes and double dashes in visible text with a hyphen with spaces ( - )" |

---

## PART X -- AI Voice and Writing Standards

All AI-generated content must sound like it was written directly by the course instructor. Clear, confident, precise, professional. Not a template, not a generic LMS narrator.

### 10.1 Voice and Authority

- Write in the instructor's direct voice.
- Do not refer to "your instructor."
- Do not insert disclaimers or hypothetical scenarios.
- Do not explain that something is required only if requested.
- Default to decisive expectations.

### 10.2 Clarity Over Softening

These phrases are prohibited in AI-generated course content: "if required," "if requested," "if applicable," "depending on course requirements," "you may," "optional unless."

### 10.3 Submission Language Standards

Every assignment or quiz page must state clearly:
- Exactly what to submit.
- The file type.
- The naming convention.
- Whether the submission should be zipped.
- Any required supporting materials.

Never assume the student will infer expectations.

### 10.4 Examples -- Bad and Good

| Prohibited (Bad) | Required (Good) |
|---|---|
| "Only required if your instructor has requested the session file." | "Submit the full session folder as a zipped file. Include all associated audio assets." |
| "You may include screenshots if needed." | "Include two screenshots that clearly show the completed routing configuration." |
| "Depending on your setup, you might want to..." | "Configure your I/O settings as follows before beginning." |

### 10.5 Default Decision Rule

When unsure whether something should be conditional or decisive, choose decisive. If the instructor has not explicitly marked something optional, write it as required. Students should finish reading any page and know exactly what to build, what to submit, how to format it, and how it will be graded. No ambiguity.

---

## PART XI -- Faculty Quick Reference Checklists

### 11.1 HTML Page Checklist

- All styles are inline -- no `<style>` blocks, no external CSS files
- Only system-safe fonts: Arial, Georgia, or Courier New
- First heading in content area is H2 (never H1 -- Canvas provides H1)
- Layout uses HTML tables with `role="presentation"` or stacked `<div>` elements
- All `<img>` tags have meaningful alt text under 120 characters (or `alt=""` for decorative)
- All link text is descriptive -- no "click here" or "read more"
- All `<a>` tags have a title attribute
- Heading tags follow logical hierarchy: H2 > H3 (no skipped levels)
- Data tables have `<caption>` with plain text (no style attribute on caption)
- Data tables use `<th scope="col">` or `<th scope="row">` in the header row
- No `<table>` used for decorative banners or totals -- use `<div>` instead
- All text/background color combinations pass WCAG 4.5:1 contrast ratio
- #CC4400 replaced with #993300 or darker
- Color is not the only indicator of meaning
- Links that open new tabs include aria-label warning the user
- No JavaScript embedded in the page
- No em dashes or double dashes in visible text
- Canvas Accessibility Checker shows 0 issues before publishing

### 11.2 QTI Quiz File Checklist

- imsmanifest.xml is present at the root of the .zip file
- Manifest uses the imsccv1p1 xmlns path
- Each `<item>` has a unique ident attribute
- All questions in the same bank share the same title string (the bank name)
- question_type metadata matches the actual question structure in the XML
- points_possible is set for every question
- Each multiple choice question has at least 3 answer options
- Correct answer is identified in the `<respcondition>` block
- HTML inside `<mattext>` uses `texttype="text/html"` and encodes `<` and `>`
- Images inside question HTML include alt text
- No "All of the above" or "None of the above" used in any question
- No essay questions present in self-grading assessment files

### 11.3 AI Generation Checklist

- HTML output uses inline styles only -- no style blocks, no external CSS
- First heading in AI-generated content is H2
- All colors are hex codes -- no rgba() values
- All `<img>` tags include alt text under 120 characters
- All `<a>` tags include title attribute
- No navigation links to standalone HTML files
- No em dashes or double dashes in visible content
- No "All of the above" or "None of the above" in quiz questions
- No essay questions in self-grading quiz files
- Content reviewed for instructor voice -- no conditional softening language
- Submission instructions state file type, naming convention, and zip requirements
- Canvas Accessibility Checker shows 0 issues after paste

---

## PART XIII -- Panorama Accessibility Checker

Panorama (YuJa Panorama) is the automated accessibility evaluation platform integrated into Canvas LMS. It scans uploaded course files -- including PowerPoint, PDFs, Word documents, and Canvas HTML pages -- and reports accessibility issues based on WCAG 2.1 AA and Section 508. It assigns a score from 0 to 100. A single Severe issue tanks the score significantly.

Panorama is rule-based and standards-based. It is not AI. It checks technical compliance only.

### 13.1 Severity Model

| Severity | Meaning | Score Impact |
|---|---|---|
| Severe | Critical barrier that prevents access entirely | Fails hard -- tanks score even in isolation |
| Major | Significantly breaks usability for users with disabilities | Medium score penalty |
| Minor | Cosmetic or consistency issues -- reduces clarity | Low score penalty |

### 13.2 What Panorama Checks

| Category | What Panorama Checks | Max Severity |
|---|---|---|
| Document Structure | Slide titles (PPT); heading hierarchy; logical reading order | Severe (missing slide title) |
| Images | Missing alt text; decorative vs. informative distinction | Severe (no alt text) |
| Color and Contrast | Text contrast (WCAG 2.1 AA: 4.5:1 normal, 3:1 large text) | Major |
| Tables | Missing header rows; missing captions (HTML/PDF) | Major |
| Links | Broken links; non-descriptive link text | Major |
| OCR / Text Accessibility (PDFs) | Scanned image-only PDFs with no readable text layer | Severe |
| Multimedia | Video captions present; audio accessibility | Major (no captions) |

### 13.3 PowerPoint-Specific Requirements

- Every slide must have a Title placeholder (not a text box). Missing slide title = Severe.
- Slides with no visible title need an off-slide Title placeholder positioned at x="-10000000" y="-10000000" in EMUs (invisible to audience, readable by accessibility tools).
- Every slide title must be unique.
- All images must have alt text or be marked as decorative (right-click, Edit Alt Text).
- Reading order must be verified in the Selection Pane (Home - Arrange - Selection Pane). Objects are read bottom-to-top in the list.
- All text must pass WCAG 4.5:1 contrast.
- Tables must have Header Row checked in the Table Design tab. No merged or split cells.
- Section names must be unique and descriptive -- no "Section 1" defaults.

### 13.4 Panorama vs. Canvas Accessibility Checker

Both tools check WCAG 2.1 AA and Section 508 but they check overlapping, not identical things. Zero issues in both is the required standard. Following this manual consistently produces files that pass Panorama without additional intervention.

---

## PART XIV -- Rubric Import Standards

### 14.1 Enable Enhanced Rubrics (One-Time Per Course)

Course Settings - Feature Options tab - Enhanced Rubrics - set to Enabled. Once enabled, the Rubrics section shows an Import Rubric button. The CSV template is downloadable from that button.

### 14.2 CSV Format

**Required header row (exact text, case-sensitive):**
```
Rubric Name, Criteria Name, Criteria Description, Criteria Enable Range, Rating Name, Rating Description, Rating Points, Rating Name, Rating Description, Rating Points, Rating Name, Rating Description, Rating Points
```

One row per criterion. Three rating levels per criterion (Full Credit, Partial Credit, No Credit) is the program standard.

**Column definitions:**
- Rubric Name: identical on every row for the same rubric
- Criteria Name: the criterion label
- Criteria Description: full text of what is required
- Criteria Enable Range: use false for fixed points
- Rating Name / Rating Description / Rating Points: repeat triplet for each rating level in descending order

### 14.3 Program Standard Rating Scale

Three rating levels per criterion unless explicitly specified otherwise:

| Level | Points | Description |
|---|---|---|
| Full Credit | 100% of criterion points | All criteria for this section are met as described. |
| Partial Credit | 50% of criterion points (round to nearest whole number) | Some criteria met but submission is incomplete or missing required evidence. |
| No Credit | 0 points | Not submitted or does not meet minimum requirements for this section. |

### 14.4 Critical Rule -- No Commas in ANY Field

**This is the single most important technical rule for Canvas rubric CSV import.** Canvas parses rubric CSVs by splitting on commas. A comma inside any field causes silent column misalignment -- Canvas does not report an error, but one or more criteria receive 0 points instead of their intended values.

**The rule:** No field in a Canvas rubric CSV may contain a comma. This includes Rubric Name, Criteria Name, Criteria Description, Rating Name, and all Rating Description fields.

**How to rewrite:** Replace comma-separated lists with "and" or "or" as conjunctions. "Screenshot present but naming is incorrect, or one page is missing" becomes "Screenshot present but naming is incorrect or one page is missing."

### 14.5 Required Generation Method -- Python csv.writer with QUOTE_ALL

All rubric CSV files must be generated using Python's csv.writer module with the QUOTE_ALL quoting option.

```python
import csv

header = ["Rubric Name","Criteria Name","Criteria Description",
    "Criteria Enable Range",
    "Rating Name","Rating Description","Rating Points",
    "Rating Name","Rating Description","Rating Points",
    "Rating Name","Rating Description","Rating Points"]

rows = [header, [criterion_row_1], [criterion_row_2]]

with open('rubric.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(rows)
```

**Verification step:** After generating, parse back with csv.reader and confirm every data row produces exactly 13 columns.

```python
with open('rubric.csv', newline='') as f:
    for i, row in enumerate(csv.reader(f)):
        print(f'Row {i}: {len(row)} cols')  # All data rows must show 13
```

**Pre-import audit:** Before importing any rubric CSV, scan for commas in Rating Description columns:

```python
import csv
with open('your_rubric.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0: continue
        for col in [5, 8, 11]:  # Rating Description columns (0-indexed)
            if col < len(row) and ',' in row[col]:
                print(f'ISSUE: Row {i+1} col {col+1}: {row[col][:60]}')
```

**CSV filename convention:** COURSE_A#_Rubric.csv (example: DAPR3345_A4_Rubric.csv). Deliver alongside the HTML file.

**After importing:** Open the rubric in the Canvas Criteria Builder and confirm every criterion shows a non-zero point value. If any criterion shows 0 pts, there is a column alignment error -- delete the rubric, fix the CSV, and re-import.

---

## PART XVI -- PDF Documentation Page Standards

Many assignments require students to document their work as a PDF submitted alongside a session file. These PDFs are built by copying a numbered list from the Canvas assignment page into Word, adding screenshots, and exporting as PDF.

### 16.1 Purpose and Workflow

Three steps: (1) Canvas assignment page contains a copy-paste block with numbered items, point values, and placeholder lines. (2) Student copies the entire block into a new Word document. (3) Student inserts full-screen screenshots below each numbered item and exports as PDF.

### 16.2 Point Values -- Always Visible

Every numbered item in the copy-paste block must include its point value in parentheses on the same line as the item label.

**Correct:** `1. EQ (15 pts)`

**Incorrect:** `1. EQ`

Point values in the copy-paste block must exactly match the rubric table on the same Canvas page.

### 16.3 Keep Titles With Their Screenshots

The copy-paste block must include a visible instruction line telling students to apply "Keep with next" paragraph formatting to each numbered item line. This prevents orphaned headings.

**Required instruction line at top of every copy-paste block:**
"After pasting this into Word, select each numbered item line and apply Format > Paragraph > Line and Page Breaks > Keep with next. This prevents a section label from appearing alone at the bottom of a page while its screenshot is on the next page."

### 16.4 Required Structure of Every Copy-Paste Block

Every copy-paste block must contain in order:
1. A filename line at the top in monospace: the naming convention for the PDF file.
2. An assignment title line with course and institution.
3. The "Keep with next" instruction line.
4. One numbered item per screenshot requirement: Item Name (X pts) on line 1, a brief description of what the screenshot must show on line 2, and "[ Screenshot here ]" on line 3.

### 16.5 Checklist for PDF Documentation Sections

- Every numbered item includes its point value in parentheses on the same line.
- Point values in the copy-paste block match the rubric table exactly.
- The "Keep with next" instruction appears inside the copy-paste box, before the first numbered item.
- Every numbered item has a "[ Screenshot here ]" placeholder line below the description.
- The filename naming convention appears at the top of the block in monospace.
- The assignment title and course identifier appear below the filename line.
- The block is visually distinct from surrounding Canvas content (gray background box).

---

## PART XVII -- Assignment Classification and Point System

**REQUIRED:** Before generating any assignment page, rubric, or copy-paste PDF block, confirm the assignment tier. Never assume a point value.

### 17.1 The Two-Tier Point System

| Tier | Points | Expected Time | Description |
|---|---|---|---|
| Lab / Short Assignment | 25 pts | 1 to 2 hours | Ear training, session prep, short skill-building exercises, any assignment completed in roughly one sitting. Graded on process completion. |
| Major Mix / Final Project | 100 pts | 4 to 8 hours | Full mix deliverables, end-of-unit and end-of-semester final projects. Graded on mix quality and creative decisions. |

The time rule: 1-2 hours of expected student work = 25 points. 4-8 hours = 100 points. Do not create assignments between these values.

### 17.2 Labs (25 Points) -- Classification Criteria

An assignment is a 25-point lab if it meets one or more of the following:
- Ear training exercise: EQ Lab, Compression Lab, Technical Ear Trainer tasks.
- Session preparation or setup task: Essential Groundwork, Session Setup, file organization.
- Short skill-building exercise completable in one class session.
- Any assignment in a course whose title includes the word Lab (DAPR 2000L, DAPR 2020L, DAPR 2010L).
- The student is practicing a process rather than delivering a polished finished product.

### 17.3 Major Mixes (100 Points) -- Classification Criteria

An assignment is a 100-point major mix if it meets one or more of the following:
- A full mix delivered as a final or near-final product, graded on mix quality.
- An end-of-unit or end-of-semester final project.
- Expected student time investment is 4 to 8 hours.
- Grading evaluates creative and technical decisions, not whether process steps were completed.

### 17.4 Standard Deliverable Weights -- 25-Point Labs

When a 25-point lab requires both a WAV file and a PDF documentation submission:

| Deliverable | Points | What Is Graded |
|---|---|---|
| WAV bounce file | 10 pts | Correct sample rate (44.1 kHz), bit depth (24-bit), interleaved stereo, correct duration, correct file naming. |
| PDF documentation | 15 pts | All required screenshots present, numbered correctly, file naming convention followed, Keep with next applied, exported as PDF. |
| Total | 25 pts | |

If the assignment has no WAV deliverable, all 25 points go to the PDF and process criteria.

### 17.5 Standard Internal Rubric Breakdown -- 25-Point Labs

| Criteria Slot | Points | Typical Content |
|---|---|---|
| Criterion 1 | 6 pts | First major process step or deliverable |
| Criterion 2 | 6 pts | Second major process step or deliverable |
| Criterion 3 | 6 pts | Third major process step or deliverable |
| Criterion 4 - Submission | 7 pts | Correct file type, naming convention, export specs, PDF documentation |
| Total | 25 pts | |

If an assignment has only three natural criteria, split as 8/8/9. If five, split as 5/5/5/5/5. Always sum to 25. Never use a criterion worth fewer than 5 points -- consolidate instead.

### 17.6 Standard Deliverable Weights -- 100-Point Major Mixes

Three separate Canvas submissions: zipped Pro Tools session folder, stereo bounce WAV, and PDF documentation file. The PDF is submitted as a separate Canvas attachment -- not placed inside the zip.

| Deliverable | Points | What Is Graded |
|---|---|---|
| Zipped Pro Tools session | 40 pts | Complete session folder with all audio files. Sample rate, bit depth, track labeling, color coding, routing, gain staging, and processing decisions. |
| Stereo bounce WAV | 20 pts | Exported at 44.1 kHz / 24-bit / Interleaved. Correct duration. Correct file naming convention. |
| PDF documentation | 40 pts | All required screenshots present and numbered. Session view, routing view, processing decisions, and bounce dialog documented. |
| Total | 100 pts | |

**The zip must contain:** the .ptx session file, the Audio Files folder, the Fade Files folder, and any other session-associated folders. Instruct students to use File > Save Copy In with Copy All Audio Files checked before zipping.

### 17.7 Standard Internal Rubric Breakdown -- 100-Point Major Mixes

| Criteria Slot | Points | What It Evaluates |
|---|---|---|
| Technical Foundation | 20 pts | Session setup, sample rate, bit depth, routing, gain staging, export specs |
| Mix Balance and Clarity | 20 pts | Level balance, panning, frequency separation, EQ decisions |
| Dynamics and Processing | 20 pts | Compression, limiting, effects, automation, creative decisions |
| PDF: Session Documentation | 20 pts | Session overview screenshot, track labeling and color coding, markers and arrangement |
| PDF: Processing Documentation | 10 pts | Key plugin settings, routing decisions, and bounce dialog captured |
| PDF: Submission Compliance | 10 pts | Correct file naming, all screenshots numbered, exported as PDF |
| Total | 100 pts | |

### 17.8 Classification Questions -- Ask Before Generating

Before generating any assignment page, rubric, or copy-paste PDF block, confirm:
- What is the assignment name and which course is it for?
- Is this a lab (25 pts) or a major mix (100 pts)?
- What is the expected student time investment?
- Does the student submit a WAV file, a zipped session, or both?
- Does this assignment require a PDF documentation submission?
- How many distinct criteria does the rubric need?
- Are there any custom exceptions to the standard breakdown?

### 17.9 DAPR Course Reference

| Course | Title | Lab Course? |
|---|---|---|
| DAPR 2000 | Digital Audio Essentials | No |
| DAPR 2000L | Digital Audio Essentials Lab | Yes -- all assignments 25 pts |
| DAPR 2010 | Core Recording | No |
| DAPR 2010L | Core Recording Lab | Yes -- all assignments 25 pts |
| DAPR 2020 | Core Mixing | No |
| DAPR 2020L | Core Mixing Lab | Yes -- all assignments 25 pts |
| DAPR 2080 | Podcast and Radio Production | No |
| DAPR 2255 | Audio Hardware I | No |
| DAPR 3010R | Digital Lecture Series | No |
| DAPR 3255 | Audio Hardware II | No |
| DAPR 3340 | Spatial Audio I | No |
| DAPR 3345 | Spatial Audio II | No |

Lab courses: every assignment is 25 pts by definition, using the 6/6/6/7 internal breakdown, unless explicitly designated as an end-of-semester final project at 100 points.

---

## PART XVIII -- GitHub Image Repository Standards

All Canvas page images for the DAPR program are hosted in a single public GitHub repository. Images are referenced in Canvas HTML using raw GitHub URLs. Canvas imposes a 500 KB paste limit on HTML content -- base64-encoded images frequently exceed this and will be rejected. GitHub hosting solves this.

**Repository:** https://github.com/uvu-dapr/Canvas

**Raw URL pattern:**
```
https://raw.githubusercontent.com/uvu-dapr/Canvas/main/FOLDER/SUBFOLDER/FILENAME.jpg
```

Always use raw.githubusercontent.com, never github.com. Verify every new URL in a browser before building the Canvas page -- you should see the image with nothing else around it.

**WARNING:** Never rename or move an existing image file in the repository. Canvas pages contain hardcoded URLs. Renaming a file breaks every page that references it with no warning. To update an image, replace the file in place using the same filename.

### 18.1 Repository Folder Structure

```
Canvas/
    All/                    (images shared across multiple courses)
        ProToolsCleanup/    (legacy -- keep original casing, do not rename)
    dapr-2000/
    dapr-2000l/
    dapr-2010/
    dapr-2010l/
    dapr-2020/
    dapr-2020l/
    dapr-2080/
    dapr-2255/
    dapr-3010r/
    dapr-3255/
    dapr-3340/
    dapr-3345/
```

Use All/ only when the same image appears in pages across two or more different courses.

### 18.2 Folder Naming Convention

Course folders: lowercase with hyphens (dapr-2000, dapr-2000l, dapr-3345). Assignment subfolders: lowercase, with the two-character rule below.

**Two-character rule:**
- Underscores `_` connect words within one concept title
- Hyphens `-` separate distinct segments from each other

| Underscores _ connect words that are one concept | Hyphens - separate distinct segments |
|---|---|
| sound_wave_properties (one concept title) | sound-sound_wave_properties (topic + concept) |
| eq_lab (one concept) | dapr-2000l (dapr and 2000l are two things) |
| pro_tools_cleanup (one concept) | dapr-2000/sound-the_decibel/ |

**Full pattern:** `topic-concept_title`

Examples derived from Canvas page names:

| Canvas Page Name (Option D) | GitHub Folder Name |
|---|---|
| Jobs: Overview | dapr-2000/jobs-overview/ |
| Jobs: Working in the Industry | dapr-2000/jobs-working_in_the_industry/ |
| Sound: The Decibel | dapr-2000/sound-the_decibel/ |
| Sound: Sound Wave Properties | dapr-2000/sound-sound_wave_properties/ |
| Networking: Address Resolution Protocol | dapr-3255/networking-address_resolution_protocol/ |
| Networking: Dynamic Host Configuration Protocol (DHCP) | dapr-3255/networking-dynamic_host_configuration_protocol/ |
| MIDI: Channel Voice Messages | dapr-3255/midi-channel_voice_messages/ |
| EQ: EQ Lab | dapr-2000l/eq-eq_lab/ |

Conversion rule: strip the colon, lowercase everything, replace spaces with underscores within the concept title, put a hyphen between the topic and the concept. Drop parenthetical acronyms in folder names. The week from the module title is never included in any folder name. Folder names are permanent once a URL has been used in a Canvas page.

### 18.3 Image Filename Convention

Lowercase with underscores within concept words and the .jpg extension. Names must be descriptive enough to identify the image without opening it.

**Correct:** `plugin_settings.jpg`, `session_overview.jpg`, `bounce_dialog_settings.jpg`

**Incorrect:** `screenshot1.jpg` (not descriptive), `Screen Shot 2026.jpg` (spaces, mixed case)

### 18.4 Adding Images -- GitHub Desktop Workflow

1. In Finder, navigate to the cloned Canvas repository folder.
2. Create the assignment subfolder if it does not exist.
3. Place all .jpg screenshot files in that subfolder.
4. Open GitHub Desktop. The new files appear in the Changes panel.
5. Type a brief commit summary: "Add EQ Lab images for dapr-2000l"
6. Click Commit to main, then click Push origin.
7. Raw URLs are live immediately after pushing.

After pushing, verify at least one raw URL in a browser before building the Canvas page.

---

## PART XIX -- Student File Naming Standards

Every file a student submits follows a single master naming pattern. Consistent naming makes SpeedGrader usable at scale.

**REQUIRED:** All submitted files must follow the naming conventions in this part exactly. Files named incorrectly will be returned ungraded.

### 19.1 Master Naming Pattern

Three segments separated by space-hyphen-space ( - ):

```
With song name (mix assignments):
LastName, FirstName - Assignment Name - Song Name.ext

Without song name (labs and documentation):
LastName, FirstName - Assignment Name.ext
```

### 19.2 Segment Rules

**Segment 1 - Student Name:** `LastName, FirstName` -- the comma is literal and required. Use the student's preferred name as set in Canvas. Do not abbreviate.

**Segment 2 - Assignment Name:** Use the full Canvas page name with original capitalization and spaces. Replace any colon in the assignment name with space-hyphen-space ( - ). Do not abbreviate.

Example: Canvas page name `Sound: The Decibel` becomes filename segment `Sound - The Decibel`

**Segment 3 - Song Name (mix assignments only):** Use the song title with normal capitalization. Strip apostrophes. Strip all other punctuation including periods, commas, and exclamation marks. Omit this segment entirely for lab assignments and documentation files where no specific song is submitted.

| Song Title | Filename Segment |
|---|---|
| Don't Think Twice, It's All Right | Dont Think Twice Its All Right |
| Knockin' on Heaven's Door | Knockin on Heavens Door |
| Mr. Tambourine Man | Mr Tambourine Man |

### 19.3 File Type Reference

| Extension | Song Name? | Example |
|---|---|---|
| .ptx | Yes | Smith, John - Sound - The Decibel - Dont Think Twice.ptx |
| .zip | Yes | Smith, John - Sound - The Decibel - Dont Think Twice.zip |
| .wav | Yes | Smith, John - Sound - The Decibel - Dont Think Twice.wav |
| .pdf | Yes (mix) / No (lab) | Smith, John - Sound - The Decibel - Dont Think Twice.pdf / Smith, John - EQ - EQ Lab.pdf |

### 19.4 The Zip-Session Matching Rule

The zip file, the .ptx session file inside it, and the WAV bounce must all share the same base name.

```
Correct -- all three names match:
  Smith, John - Sound - The Decibel - Dont Think Twice.zip
  Smith, John - Sound - The Decibel - Dont Think Twice.ptx  (inside the zip)
  Smith, John - Sound - The Decibel - Dont Think Twice.wav

Incorrect -- names do not match:
  Smith, John - Sound - The Decibel - Dont Think Twice.zip
  Untitled.ptx                    (wrong - default name)
  JohnSmithFinalMix.wav           (wrong - wrong format)
```

### 19.5 Prohibited Naming Patterns

| Prohibited | Why It Fails |
|---|---|
| Untitled.ptx | Default Pro Tools session name |
| john smith eq lab.ptx | Name order wrong, comma missing, no separator dashes |
| SmithJohn_EQLab_DontThinkTwice.ptx | Underscores instead of space-hyphen-space separators |
| Smith, John - Sound: The Decibel.ptx | Colon retained -- replace every colon with space-hyphen-space |
| Smith, John - The Decibel.ptx | Topic prefix dropped -- keep the full Canvas page name |

---

## PART XX -- Canvas Icon and Callout Box System

Every Canvas page that uses a callout box must use one of the six approved types. Custom colors and custom icon shapes are not permitted.

**REQUIRED:** Every callout box icon is an `<img>` tag pointing to a raw GitHub URL. No inline SVG. No pasted path data. No exceptions.

### 20.1 Icon Specification

Icons are embedded as `<img>` tags pointing to the raw GitHub URL for that icon type. Size: `width="22" height="22"` inside callout boxes. Use `alt=""` on callout icons -- they are decorative because the bold label text conveys the meaning. The icon files live at:

`https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/`

### 20.2 Six Callout Box Types -- Locked Colors

| Type | GitHub Filename | Border Color | Background Fill | When to Use |
|---|---|---|---|---|
| Required | `Callout_Required.svg` | #1B5E20 | #E8F5E9 | Mandatory rules, program standards, must-follow instructions |
| Note | `Callout_Note.svg` | #0D47A1 | #E3F2FD | Clarifications, reminders, helpful context |
| Warning | `Callout_Warning.svg` | #F57F17 | #FFF8E1 | Common mistakes, known gotchas, proceed with caution |
| Critical | `Callout_Avoid.svg` | #C62828 | #FBE9E7 | Hard rules, enforcement policies, absolute prohibitions |
| Tip | `Callout_Tip.svg` | #4A148C | #F3E5F5 | Helpful suggestions, shortcuts, efficiency notes |
| FAQ | `Callout_FAQ.svg` | #AD1457 | #FCE4EC | Anticipated student questions, Q&A blocks |

### 20.3 Callout Box HTML Template

Use `<table role="presentation">` for the icon + text layout. Never use `display:flex` -- icons inside a flex container often fail to render in Canvas.

```html
<table role="presentation" style="width:100%; background-color:#E8F5E9; border-left:4px solid #1B5E20;
       border-collapse:collapse; margin:16px 0; border-radius:0 4px 4px 0;">
  <tr>
    <td style="width:38px; padding:12px 8px 12px 14px; vertical-align:top;">
      <img
        src="https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/Callout_Required.svg"
        alt=""
        width="22" height="22"
        style="display:block;">
    </td>
    <td style="padding:12px 14px 12px 4px;">
      <p style="margin:0;"><strong>Label:</strong> Content goes here.</p>
    </td>
  </tr>
</table>
```

To switch callout type: change `background-color`, `border-left` color, and the `src` filename. All six filenames and their matching colors are in the table above.

### 20.4 Writing Standards -- Dashes and Separators

**REQUIRED:** No em dashes and no double dashes (--) anywhere in visible Canvas HTML page content. Use a hyphen with spaces ( - ) as a separator where a dash is needed in running text. Double dashes are permitted only inside HTML comments, which Canvas strips before rendering. This rule applies to all AI-generated and manually authored content.

### 20.5 Additional Accessibility Rules

**Do not use manual numbered labels (1. 2. 3.) inside div elements** when items are meant to convey a sequence. Canvas reads digit-period patterns as implied lists and may flag them as an accessibility error. Use word-based labels (First, Second, Third) or remove the number from the label text.

**Gold background (#F9A825) requires dark text (#212121), not white.** White text on #F9A825 produces only 2.9:1 contrast ratio, which fails WCAG AA (minimum 4.5:1). This applies to the Helpful column header in feedback quality comparison tables.

---

## PART XXI -- GitHub Image Workflow for Canvas Pages

Before writing a single img tag, confirm the correct GitHub folder path and confirm the image files have been pushed to the repository. Never construct a raw URL without a confirmed filename.

### 21.1 The Five Pre-Build Questions (Mandatory)

| Question 1 | Is this image shared across multiple courses, or does it belong to one specific course? Shared = All/ One course = dapr-XXXX/ |
|---|---|
| Question 2 | What is the exact course folder name? (dapr-2000, dapr-2000l, dapr-3255, etc.) |
| Question 3 | What is the exact assignment subfolder name? Apply the Option D conversion rule: strip colon, lowercase, underscores within concept, hyphen between topic and concept. |
| Question 4 | What are the exact filenames of all images that have been pushed to the repository? List all of them before any HTML is written. |
| Question 5 | Have these files been committed and pushed in GitHub Desktop? Confirm the push completed before any HTML is written. |

### 21.2 Raw URL Construction

```
https://raw.githubusercontent.com/uvu-dapr/Canvas/main/COURSE/SUBFOLDER/FILENAME.jpg
```

Examples:
```
https://raw.githubusercontent.com/uvu-dapr/Canvas/main/dapr-2000l/eq-eq_lab/plugin_settings.jpg
https://raw.githubusercontent.com/uvu-dapr/Canvas/main/All/ProToolsCleanup/before.jpg
```

### 21.3 Image Placement in HTML

Do not use layout tables (role="presentation") for image placement. Canvas flags these for missing captions and headers regardless of the role attribute. Use stacked divs instead:

```html
<div style="margin:12px 0;">
  <div style="margin-bottom:16px;">
    <p style="font-weight:bold;">Before</p>
    <img src="URL" alt="Description" style="max-width:100%; height:auto;">
  </div>
  <div>
    <p style="font-weight:bold;">After</p>
    <img src="URL" alt="Description" style="max-width:100%; height:auto;">
  </div>
</div>
```

### 21.4 Pre-Publication Checklist for Pages with GitHub Images

- GitHub folder path and complete filename list confirmed before starting HTML generation.
- All image files are pushed to GitHub before the Canvas page is built.
- All img src values use the raw.githubusercontent.com URL pattern.
- At least one raw URL verified in a browser -- image visible with nothing else around it.
- All alt text is present, descriptive, and under 120 characters.
- No layout tables used for image placement -- stacked divs used instead.
- HTML file size is under 500 KB.
- Canvas Accessibility Checker shows zero issues after paste.
- At least two images confirmed visible in Canvas after saving.

---

## PART XXII -- Canvas Module and Page Naming System (Option D)

Option D is the permanent naming system for all Canvas modules and pages across every DAPR course. Apply this system automatically when generating any Canvas content. Do not revert to numbered module prefixes (M01, M02) or part-based page prefixes (M02-P1, M02-P2).

**REQUIRED:** Every Canvas module title and page name across all 12 DAPR courses must follow Option D.

### 22.1 The Three Rules of Option D

**Rule 1 - Module title:** Topic prefix, module number, descriptive title, week in parentheses.

Pattern: `Topic: M# - Descriptive Title (Week ##)`

**Rule 2 - Page name:** Topic prefix and descriptive title only. No module number. No week. No part number.

Pattern: `Topic: Descriptive Page Title`

**Rule 3 - Rollover:** Update only the week parenthetical in module titles if pacing changes. Never rename pages. Pages have no week reference and require zero rollover maintenance.

### 22.2 Module Title Examples

```
Jobs: M1 - Orientation and Recording Studio Jobs (Week 01)
Sound: M2 - Sound and Hearing (Week 02)
Sound: M3 - The Decibel (Week 03)
Networking: M3 - Network Configuration and Control (Week 08)
Networking: M4 - Audio Network Architecture (Week 09)
```

### 22.3 Page Name Examples

```
Jobs: Overview
Jobs: Working in the Industry
Jobs: Read Chapter 1
Sound: Overview
Sound: Read Sound and Hearing
Sound: The Decibel
Sound: Sound Wave Properties
Networking: Address Resolution Protocol
Networking: Dynamic Host Configuration Protocol (DHCP)
MIDI: Channel Voice Messages
EQ: Overview
EQ: EQ Lab
```

### 22.4 Why Pages Have No Module Number or Week Reference

If a page name included a module number or week reference, that page would need renaming every time its module was reordered or rescheduled. Across hundreds of pages and 12 courses over multiple semesters, that maintenance cost is unacceptable. The topic prefix alone sorts and groups pages correctly in every Canvas view.

### 22.5 GitHub Folder Names Under Option D

GitHub folder names are derived from the Canvas page name, not the module title.

Conversion: strip the topic prefix and colon, lowercase everything, replace spaces with underscores within concept words, hyphen between topic and concept. The week parenthetical is never included.

```
Sound: The Decibel  ->  dapr-2000/sound-the_decibel/
Networking: Address Resolution Protocol  ->  dapr-3255/networking-address_resolution_protocol/
Jobs: Working in the Industry  ->  dapr-2000/jobs-working_in_the_industry/
EQ: EQ Lab  ->  dapr-2000l/eq-eq_lab/
```

### 22.6 Semester Rollover Procedure

The only naming maintenance required at rollover is updating the week parenthetical in module titles if pacing changes. Page names require zero updates. This is the minimum possible rollover work while still communicating the weekly schedule to students.

### 22.7 Student File Naming Under Option D

Student submission filenames use the Canvas page name as Segment 2 of the master naming pattern (Part XIX). Because page names follow Option D format (Topic: Descriptive Title), the colon is replaced with space-hyphen-space in the filename.

```
Smith, John - EQ - EQ Lab - Dont Think Twice.wav
Smith, John - Sound - The Decibel.pdf
Smith, John - Networking - Address Resolution Protocol.pdf
```
