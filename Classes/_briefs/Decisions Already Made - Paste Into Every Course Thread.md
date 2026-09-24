# Decisions Already Made: Paste Into Every Course Thread

Written 2026-09-23 by Adam. These settle the questions the course threads keep asking. Treat them as final. Take your own recommended option for anything not covered here, and stop to ask only when you are truly blocked.

---

FOR: ALL COURSES (paste into every DAPR course thread)


Read the current standards first: `2026-09-24 DAPR Canvas Standards.md` (older copies are superseded).

## 1. Working rules

0. Start every report or message you write for me with the course number and name on the very first line, for example "DAPR 2010 - Core Recording".

1. Before you move, rename, replace, or delete anything, show me one table (old path to new path, or old image to new image) and wait for my approval.
2. Never commit or push. I review and commit in GitHub Desktop myself.
3. Never replace an image I already have unless you show me the before and after first and I say yes. Keep images I have approved.
4. Ask at most one question at a time, and only when you are truly blocked.
5. No dashes in prose. Full paths in code blocks.

## 2. File layout (GitHub repo and Cloudflare Canvas Links)

1. Every file sits in a module folder: `Classes/<Course_Folder>/<Module_Folder>/<File>` and `Canvas Links/<Course_Folder>/<Module_Folder>/<File>`. No loose files at a course root.
2. Module folder names come from the Canvas module titles. No numbering, no weeks, no `Images/`, `Handouts/`, `Manuals/` or `Presentations/` levels, no filename prefixes or counters. Title_Case with acronyms in capitals.
3. Placement: a file goes in the module whose content page uses it. A resources or link list page never wins placement. Course_Orientation holds only true orientation material.
4. Folders named `Archive` become `_unused`. `_unused` is a holding pen only and is never published to Cloudflare (the sync excludes `**/_unused/**`).
5. Order: fix the layout first, then upload to Cloudflare and rewrite the cartridge once against the new paths. Give me the rclone dry run command; I run it.
6. When the Folder Map or `Canvas Links/README.txt` disagrees with this, this wins. Update them to match.

## 3. Dates (Standards 11d)

1. A module opens Monday of its week. Work is due Friday at 9:00 AM Mountain, never midnight.
2. A 10 or 25 point item is due Friday of the FOLLOWING week (week N+1). Larger items follow the point value window in 11d.
3. A due date that lands in a closure slides to the next open Friday. Nothing but the final exam is due in finals week. Use the Term Spine UTC times (daylight saving handled).
4. Accept the collisions the Term Spine already names (for example Fall Break stacking two modules on one Friday). Flag them in the build notes; do not ask me.
5. Never open new modules in the last days of classes. If a module lands there, move it earlier into the lightest weeks.

## 4. Images

1. Embed only the question body images listed in the kit's `Quiz_Images_To_Embed.md`. Icons and everything else stay as raw GitHub URLs. If the kit lists zero, embed nothing.
2. Real products and real software screens are sourced or captured, never generated. A generated image with a fake software screen can be kept if the screen is defocused so it shows no software.
3. If an image is weak but nothing better is on hand, keep it and add it to `Classes/_briefs/Image Fixes For Later - DAPR All Courses.md`. Do not stop the build for it.
4. Personal information: my own name, account and folder names are fine to show. Blur only other people's names, usernames and student IDs, and Mac serial numbers.
5. Every student visible page carries at least one image for that page's topic, 100 percent of pages. Icons and logos do not count. Order of choice: a real photo, screenshot, diagram or chart; a chart drawn in code where values matter; a useful ChatGPT concept image; at minimum a decorative ChatGPT banner. Decorative is allowed, bare is not. Generated images: no real products, no software screens, no baked in text, numbers, logos or brand marks.
6. For a page waiting on ChatGPT: pick the final filename in the page's module folder, link it now, put a code drawn placeholder PNG at that exact path, and write the prompt in `Classes/_briefs/ChatGPT Image Prompts - DAPR ####.md` (Save as full path, then the prompt). Adam saves the result over the placeholder under the same name. Report two counts every build: finished images, placeholders waiting on ChatGPT.

## 5. Auxiliary Resources (replaces Audio & Sessions)

1. Every course gets a Canvas module named **Auxiliary Resources**. It replaces the old Audio & Sessions module or folder in every course from now on.
2. It holds reference material Adam pulls from while teaching a concept: example sessions, recordings, stems, reference tracks, extra reading. It is not for files that belong to a project or assignment students are already working on; those stay in that assignment's module.
3. The module holds one page, **Auxiliary Resources**, with one row per resource: a short title, one sentence on what it is and when to use it, the file size for anything over 100 MB, and a download link. No due dates, no points, nothing graded.
4. The matching folder is `Auxiliary_Resources` in both places: `Classes/<Course_Folder>/Auxiliary_Resources/` in the repo for images, and `Canvas Links/<Course_Folder>/Auxiliary_Resources/` on Cloudflare for downloads. Link to `https://uvu-files.adamo.workers.dev/<Course_Folder>/Auxiliary_Resources/<File>`.
5. Place the module last in the module list, after the Final, and publish it with the rest of the course (it opens with week 00).
6. Move anything currently in an Audio & Sessions module into Auxiliary Resources, and show Adam the move table first.

## 6. Never in the cartridge

1. No course outline pages of any kind (Course Outline, Course Module Outline, Schedule & Module Outline, Outline, Week by Week, Outline of Classes). Do not use old outline files as a source. Dates come from the Term Spine and 11d; module order from the kit's module_meta.xml.
2. No Student Essentials module.
3. No CS 623a BOAA Lab module and no LC 623a Studio Proficiency Assessment.
4. No Student Rating of Instructor (SRI) bonus. Drop the Bonus group if nothing else is in it.
5. If your current build has any of these, remove them in the next version and tell me what you removed.

## 7. Icons and colors (Adam, 2026-09-24)

1. Icons: link the PNG twin of every shared icon, never the SVG. `Classes/All/DAPR_Canvas_Icon_Reference/<Name>.png`, same size attributes as before (44x44, 66x66 for Submit_Upload).
2. Yellow #fbc02d is a fill and border color only, never text.
3. Orange #e65100 is retired everywhere. Use #BF360C (5.60:1 on white) for every orange: text of any size, table headers, and the module titlebar fill with white text on it. (Adam, 2026-09-24)
4. Live Fall courses are fixed by importing the new cartridge, not by restoring old Images/ paths. Test each import in a sandbox course first.
5. Text in a yellow module (headings, rules, labels) uses amber #856404; yellow #FBC02D stays for fills only. The warning callout left border is #BF360C.

## 8. Where things are

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes
/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links
/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Applications/AI Projects Standards/Work/Utah Valley University
```

Rebuild kit for this course: `<course>/Claude outputs/Notes and Briefs/2026-09-23 <Course_Folder> Rebuild Kit/`
