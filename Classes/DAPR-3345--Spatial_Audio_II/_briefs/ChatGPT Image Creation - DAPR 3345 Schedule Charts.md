# DAPR 3345 Image Brief - Schedule Charts (v14, 1,350 point plan)
Generated 2026-09-25. Run each prompt separately in ChatGPT. Save each result
with the exact filename shown, into the exact folder shown. Do not rename.

---

## Why this brief exists

The three charts below were redrawn at 02:40 on 2026-09-25 for the thread's 1,300 point plan.
Adam kept the overnight v14 build (1,350 points), so all three now show the wrong schedule:

| Chart | What is wrong now |
|---|---|
| `Term_Schedule.png` | 9 of 11 rows open or fall due in the wrong week; the Spatial Mix (due Fri 2 Apr) is missing; Final Project shows five due dates instead of four |
| `Final_Project_Milestones.png` | Build the Level is split into two parts; v14 has one 200 point item due Fri 9 Apr. Measure and Mix is shown on 16 Apr; v14 has Fri 23 Apr |
| `Certification_Hours.png` | Content Creation for Games is marked required and Atmos Essentials bonus; v14 is the reverse |

The current files are uncommitted edits in the repo. **Do not push them.** Each prompt
below replaces one of them in place, at the same name, so the pages need no change.

Every date and point value below was read from the v14 package
(`DAPR-3345-Course-Turnkey-v14-Coordinator.imscc`, 620,627 bytes) and matches the cards on
Orientation: Schedule & Module Outline.

## House rules applied

| Rule | Value | Source |
|---|---|---|
| Generator | ChatGPT's image generator. Never drawn in code (no Python, matplotlib, HTML, canvas or SVG) | §20.1 rules 1 and 2 |
| Format | PNG, solid white background (the page is white) | §20.2, §20.4b |
| Size | Same as the file it replaces: 1600 px wide | §20.3 |
| Weight | Under 1 MB | §20.3 |
| Filename | The existing name, overwritten. No counter, no copy | §20.4 |
| Colors | Each section's own header color, as on its Canvas pages | Orientation page cards |
| Commit and push | Adam | §20.4c |

**One rule these charts cannot meet: §20.5's four-string text limit.** A schedule chart is
labels. Every label is quoted exactly below. Check every one against the table in its
section before saving. A misspelled, dropped or doubled label means regenerate, with that
label quoted again. Never hand-patch a label. If ChatGPT cannot get a chart's labels right
in three tries, the §20.5a fallback applies: the page already carries the same facts in its
cards and tables, so the figure can be retired instead.

---

## Image 01 - Term Schedule

| Field | Value |
|---|---|
| Filename | `Term_Schedule.png` (overwrite) |
| Format | PNG, solid white background |
| Dimensions | 1600 x 720 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Course_Orientation/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3345--Spatial_Audio_II/Course_Orientation/Term_Schedule.png` |
| Used on | Canvas page `Orientation: Schedule & Module Outline` |
| Alt text (unchanged) | `A timeline of every section from week 1 to finals, showing when each opens and when each item is due.` |
| Caption (unchanged) | `Figure 1. The whole term on one line per section. A triangle is the Monday a section opens; each dot is a Friday something is due, and bigger dots carry more points. The cards below carry the dates of record.` |

The data, for checking the result (week 1 starts Mon 11 Jan 2027):

| Row | Opens | Due dots (week: points) | Bar spans |
|---|---|---|---|
| Interactive Audio | wk 1 | wk 2: 25, wk 3: 50 | wk 1 to 3 |
| Asset Pipeline | wk 2 | wk 3: 25, wk 4: 50 | wk 2 to 4 |
| FMOD | wk 3 | wk 4: 25, wk 5: 75 (two items) | wk 3 to 5 |
| Wwise | wk 5 | wk 6: 25, wk 8: 100, bonus wk 13: 50, bonus wk 14: 50 | wk 5 to 14 |
| Variation | wk 6 | wk 7: 25, wk 8: 50 | wk 6 to 8 |
| Voice Budget | wk 6 | wk 7: 25 | wk 6 to 7 |
| Implementation | wk 8 | wk 9: 25, wk 11: 50 | wk 8 to 11 |
| Interactive Mix | wk 12 | wk 13: 25 | wk 12 to 13 |
| Spatial Recording | wk 1 | wk 2: 25, wk 4: 75, wk 12: 100 | wk 1 to 12 |
| Dolby Certification | wk 4 | wk 7: 75, bonus wk 15 (all bonus certifications) | wk 4 to 15 |
| Final Project | wk 8 | wk 11: 50, wk 13: 200, wk 15: 150 (two items), final exam star Thu wk 16 | wk 8 to 15 |

**ChatGPT prompt (paste as-is):**

```text
REPLACE AN IMAGE FILE. The job is done only when the new image has been saved over the existing file:
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Course_Orientation/Term_Schedule.png

Adam's decision is already made: generate this chart with ChatGPT's image generator and save it over that file. Do not draw it in code (no Python, matplotlib, HTML, canvas or SVG). Do not stop at a description or a plan.

Create a 1600 x 720 pixel PNG with a solid white background.

A clean, lightly dimensional timeline chart (a Gantt chart) for a 17-week college semester. Bars are softly rounded with a subtle shadow so they sit slightly above the page. Thin light-grey vertical grid lines divide the 17 weeks. Everything is sharp, flat-lit and easy to read.

Columns: 17 equal week columns across the chart, left to right. Under each column, in small dark grey (#212121) type, the labels "Wk 1", "Wk 2", "Wk 3", "Wk 4", "Wk 5", "Wk 6", "Wk 7", "Wk 8", "Wk 9", "Wk 10", "Wk 11", "Wk 12", "Wk 13", "Wk 14", "Wk 15", "Wk 16", "Wk 17".

Shade the whole Wk 10 column pale blue-grey and label it "Spring Break" at the top. Shade the Wk 16 and Wk 17 columns pale pink and label them "Finals" at the top.

Rows: 11 rows, top to bottom, each with its name right-aligned in bold at the left, in the row's color:
1. "Interactive Audio", color #5D4037
2. "Asset Pipeline", color #B71C1C
3. "FMOD", color #BF360C
4. "Wwise", color #8D6E00
5. "Variation", color #1B5E20
6. "Voice Budget", color #0D47A1
7. "Implementation", color #4A148C
8. "Interactive Mix", color #424242
9. "Spatial Recording", color #C2185B
10. "Dolby Certification", color #5D4037
11. "Final Project", color #000000

In each row: a pale tint of the row's color forms a bar. A solid triangle pointing right, in the row's color, sits at the left end of the bar (the Monday the section opens). Solid dots in the row's color sit at the right side of a week column (a Friday something is due). Dot size shows points: small = 25, medium = 50, large = 75 to 100, largest = 150 to 200. A bonus dot is drawn faded, at 40 percent opacity.

1. Interactive Audio: bar from Wk 1 to Wk 3. Triangle at Wk 1. Small dot Wk 2, medium dot Wk 3.
2. Asset Pipeline: bar from Wk 2 to Wk 4. Triangle at Wk 2. Small dot Wk 3, medium dot Wk 4.
3. FMOD: bar from Wk 3 to Wk 5. Triangle at Wk 3. Small dot Wk 4, large dot Wk 5.
4. Wwise: bar from Wk 5 to Wk 14. Triangle at Wk 5. Small dot Wk 6, large dot Wk 8, faded medium dot Wk 13, faded medium dot Wk 14.
5. Variation: bar from Wk 6 to Wk 8. Triangle at Wk 6. Small dot Wk 7, medium dot Wk 8.
6. Voice Budget: bar from Wk 6 to Wk 7. Triangle at Wk 6. Small dot Wk 7.
7. Implementation: bar from Wk 8 to Wk 11, passing through the Spring Break column. Triangle at Wk 8. Small dot Wk 9, medium dot Wk 11.
8. Interactive Mix: bar from Wk 12 to Wk 13. Triangle at Wk 12. Small dot Wk 13.
9. Spatial Recording: bar from Wk 1 to Wk 12. Triangle at Wk 1. Small dot Wk 2, large dot Wk 4, large dot Wk 12.
10. Dolby Certification: bar from Wk 4 to Wk 15. Triangle at Wk 4. Large dot Wk 7, faded large dot Wk 15.
11. Final Project: bar from Wk 8 to Wk 15. Triangle at Wk 8. Medium dot Wk 11, largest dot Wk 13, largest dot Wk 15. A black five-pointed star in the Wk 16 column, on the Thursday (just right of the column's center).

No dot falls in the Wk 10 (Spring Break) column. Reading direction is left to right.

No other text anywhere: no title, no legend, no dates, no point numbers, no caption. No logos, borders, frames, people, watermark or signature.

After generating:
1. Check every label against the lists above, spelled exactly. If any label is misspelled, missing or doubled, regenerate.
2. Save it OVER the file named at the top: same folder, exact same name, PNG. Do not save a copy, a "-v2", or a second file.
3. Report the new pixel size, file size and modified time, and confirm it is no longer the old image.
4. Do not commit or push. Adam does that himself.
5. If you cannot write files, still generate the image, give it to Adam, and say in one line that it could not be saved.
```

---

## Image 02 - Final Project Milestones

| Field | Value |
|---|---|
| Filename | `Final_Project_Milestones.png` (overwrite) |
| Format | PNG, solid white background |
| Dimensions | 1600 x 480 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Final_Project__Interactive_Audio_Implementation_and_Final_Exam/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3345--Spatial_Audio_II/Final_Project__Interactive_Audio_Implementation_and_Final_Exam/Final_Project_Milestones.png` |
| Used on | Canvas page `Final Project: Scope, Milestones, and Deliverables` |
| Alt text (unchanged) | `A timeline from 1 March to 29 April with the proposal, build, measure and mix, walkthrough and final exam marked.` |
| Caption (unchanged) | `Figure 1. Every milestone of the final project in order. The Schedule and Module Outline page carries the dates of record. Bigger dots carry more points; the exam sits at its scheduled finals slot.` |

The data, for checking the result:

| Marker | Date | Points |
|---|---|---|
| Section opens | Mon 1 Mar | |
| Proposal and Scope | Fri 26 Mar | 50 |
| Build the Level | Fri 9 Apr | 200 |
| Measure and Mix | Fri 23 Apr | 100 |
| Walkthrough and Documentation | Fri 23 Apr | 50 |
| Final Exam | Thu 29 Apr | 100 |

Spring Break is Mon 15 Mar to Fri 19 Mar. Nothing is due in it.

**ChatGPT prompt (paste as-is):**

```text
REPLACE AN IMAGE FILE. The job is done only when the new image has been saved over the existing file:
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Final_Project__Interactive_Audio_Implementation_and_Final_Exam/Final_Project_Milestones.png

Adam's decision is already made: generate this chart with ChatGPT's image generator and save it over that file. Do not draw it in code (no Python, matplotlib, HTML, canvas or SVG). Do not stop at a description or a plan.

Create a 1600 x 480 pixel PNG with a solid white background.

A clean, lightly dimensional horizontal timeline. One mid-grey line runs across the middle of the image from left to right, representing 1 March to 29 April 2027 at an even scale (about 26 pixels per day). Markers are solid black (#000000) with a subtle shadow. Labels are dark grey (#212121), centered on their marker, two lines each, alternating above and below the line so none overlap.

A pale blue-grey band crosses the line from 15 March to 19 March, with the words "Spring Break" in small grey type near its bottom. No marker falls inside it.

Markers, left to right, with their exact labels:
1. 1 March, at the far left: a solid triangle pointing right. Label below: "Opens" / "Mon 1 Mar".
2. 26 March: a medium dot. Label above: "Proposal and Scope" / "Fri 26 Mar, 50 pts".
3. 9 April: the largest dot on the chart. Label below: "Build the Level" / "Fri 9 Apr, 200 pts".
4. 23 April: two dots stacked one directly above the other, touching the line: a large dot and a medium dot. Label above: "Measure and Mix" / "Fri 23 Apr, 100 pts". Label below: "Walkthrough and Documentation" / "Fri 23 Apr, 50 pts".
5. 29 April, at the far right: a black five-pointed star. Label above: "Final Exam" / "Thu 29 Apr, 100 pts".

There is no "Part 1" or "Part 2" anywhere, and nothing on 2 April or 16 April.

No other text anywhere: no title, no legend, no caption. No logos, borders, frames, people, watermark or signature. Reading direction is left to right.

After generating:
1. Check every label against the list above, spelled exactly. If any label is misspelled, missing or doubled, regenerate.
2. Save it OVER the file named at the top: same folder, exact same name, PNG. Do not save a copy, a "-v2", or a second file.
3. Report the new pixel size, file size and modified time, and confirm it is no longer the old image.
4. Do not commit or push. Adam does that himself.
5. If you cannot write files, still generate the image, give it to Adam, and say in one line that it could not be saved.
```

---

## Image 03 - Certification Hours

| Field | Value |
|---|---|
| Filename | `Certification_Hours.png` (overwrite) |
| Format | PNG, solid white background |
| Dimensions | 1600 x 640 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Dolby_Certification__Dolby_Learning_Portal_Certification_Track/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3345--Spatial_Audio_II/Dolby_Certification__Dolby_Learning_Portal_Certification_Track/Certification_Hours.png` |
| Used on | Canvas page `Dolby Certification: Planning Your Certification Time` |
| Alt text (unchanged) | `Estimated hours for each Dolby certification, from 3 to 7 hours each.` |
| Caption (unchanged) | `Figure 1. Planning numbers, not promises. Dolby publishes no completion times, so these ranges come from the activity count and the writing each assignment asks for.` |

The data, in the order of the page's table: Atmos Essentials is the one required
certification (75 points); every other one is bonus.

| Row | Status | Hours |
|---|---|---|
| Atmos Essentials | Required | 4.5 to 7 |
| Content Creation for Games | Bonus | 4 to 6 |
| Music Pro Tools 100 | Bonus | 3 to 5 |
| Music for Pro Tools 200 | Bonus, no portal entry yet | 4 to 6 |
| Mix Room Design and DARDT | Bonus | 3 to 5 |
| Music Logic Pro 100 | Bonus | 3 to 5 |
| Music Logic Pro 200 | Bonus | 3 to 5 |
| Music Logic Pro 300 | Bonus | 4 to 6 |
| Music for Pro Tools 300 | Bonus, no portal entry yet | 4 to 6 |

**ChatGPT prompt (paste as-is):**

```text
REPLACE AN IMAGE FILE. The job is done only when the new image has been saved over the existing file:
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Dolby_Certification__Dolby_Learning_Portal_Certification_Track/Certification_Hours.png

Adam's decision is already made: generate this chart with ChatGPT's image generator and save it over that file. Do not draw it in code (no Python, matplotlib, HTML, canvas or SVG). Do not stop at a description or a plan.

Create a 1600 x 640 pixel PNG with a solid white background.

A clean, lightly dimensional horizontal range-bar chart. Each bar is softly rounded with a subtle shadow, floating slightly above the page. A horizontal axis along the bottom runs from 0 to 8 hours at an even scale, with small dark grey (#212121) tick labels "0", "1", "2", "3", "4", "5", "6", "7", "8" and, centered under them, the axis title "hours of portal time, estimated". Faint vertical grid lines at each whole hour.

Nine rows, top to bottom. Each row name is right-aligned at the left in dark grey (#212121) type. Each bar starts and ends at the hours given, and the range is written just right of the bar in grey type.

1. "Atmos Essentials (required)": bar from 4.5 to 7, solid deep brown #5D4037. Range text "4.5 to 7 h". This is the only dark bar; make its row name bold.
2. "Content Creation for Games (bonus)": bar from 4 to 6, light brown #A1887F. Range text "4 to 6 h".
3. "Music Pro Tools 100 (bonus)": bar from 3 to 5, #A1887F. Range text "3 to 5 h".
4. "Music for Pro Tools 200 (bonus, no portal entry yet)": bar from 4 to 6, #A1887F. Range text "4 to 6 h".
5. "Mix Room Design and DARDT (bonus)": bar from 3 to 5, #A1887F. Range text "3 to 5 h".
6. "Music Logic Pro 100 (bonus)": bar from 3 to 5, #A1887F. Range text "3 to 5 h".
7. "Music Logic Pro 200 (bonus)": bar from 3 to 5, #A1887F. Range text "3 to 5 h".
8. "Music Logic Pro 300 (bonus)": bar from 4 to 6, #A1887F. Range text "4 to 6 h".
9. "Music for Pro Tools 300 (bonus, no portal entry yet)": bar from 4 to 6, #A1887F. Range text "4 to 6 h".

Atmos Essentials is required and Content Creation for Games is bonus. Do not swap them.

No other text anywhere: no title, no legend, no caption. No Dolby logo or any other logo, no borders, frames, people, watermark or signature. Reading direction is top to bottom.

After generating:
1. Check every label and every bar's start and end against the list above, spelled exactly. If any label is misspelled, missing or doubled, or any bar is at the wrong hours, regenerate.
2. Save it OVER the file named at the top: same folder, exact same name, PNG. Do not save a copy, a "-v2", or a second file.
3. Report the new pixel size, file size and modified time, and confirm it is no longer the old image.
4. Do not commit or push. Adam does that himself.
5. If you cannot write files, still generate the image, give it to Adam, and say in one line that it could not be saved.
```

---

## After all three

1. Look at each one on white at full size. Check the labels against the tables above.
2. In the repo, the three files show as modified. Commit and push them yourself (§20.4c).
3. Open each raw URL once in a browser to confirm the new image is live.

## Found while checking (not part of the images)

`Dolby Certification: Planning Your Certification Time` says the certifications "open in the
first week and stay open". In v14 the Dolby section opens Mon 1 Feb, week 4. The page text
needs one line changed in the 3345 thread; the chart above already shows week 4.
