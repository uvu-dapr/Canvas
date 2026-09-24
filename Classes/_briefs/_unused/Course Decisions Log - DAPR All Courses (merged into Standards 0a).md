# Course Decisions Log: DAPR All Courses

Adam's decisions for each course, kept here so they do not have to be pasted into every thread. Every thread reads its own section before each build, together with the Standards and the Decisions file. Newest decisions win. Last updated 2026-09-24 evening.

Rules for every course live in the Decisions file and the Standards. The most recent ones: save locally and never import into Canvas (Decisions working rule 6); Course Orientation and Instructor Use Only ship in every cartridge, Unified Class Content never does, and a page with an empty body in the export stays out (Decisions 6); quizzes are practical only with correct keys, and every module quiz has 25 questions and every Final 100, one point each (Decisions 9); an image on every page (Decisions 4). Only the DAPR 2000 thread edits preflight.py; every other thread reports gate problems to Adam instead.

Cartridges are saved in `UVU Courses/<DAPR #### - Course Name>/Canvas/Canvas Templates/-Canvas Entire Course/` and build notes in that course's `Claude outputs/Notes and Briefs/`. Start every report with the course number and name.

## DAPR 2000 - Digital Audio Essentials (live Fall 2026, sandbox course 655820)

1. v68: Orientation: Prerequisites and Orientation: Course Description are empty in the live course, so use the LIVE identifiers and fill them.
2. Syllabus: apply the draft (900 points, no midterm, real grade groups), and also state that the Final has no time limit, is open 1:00 to 2:50 PM on Tue 8 Dec in CS 623, and is a fixed set of 100 questions with answers shuffled. Change nothing else.
3. Approved: Course_Info folder moves, Quarter_Inch_TRS.png in place of the Wikimedia hotlink, Time_Domain re-export, Course_Card re-export.
4. Outline of Classes, Course Development Task List and Instructor Notes are empty in the export; they stay out.
5. Fold every entry of the live regrade list into v68. Adam fixes the live Decibel (Q1, Q2 by hand, Q22 full credit) and Monitoring (Q16 both, Q17 and Q19 full credit) questions himself.
6. Alt 1 quizzes stay held and unpublished. Keep the "is wrong" line in preflight. Regenerate the Image Reference page.
7. Preflight owner, open items (one diff, both copies identical): Lab Template exemption (read workflow_state from the assignment XML; apply the exemption to the 7a and 11b checks); skip hr elements in the 2b contrast check; hard fail an imsqti_xmlv1p2 quiz with no non_cc_assessments copy; treat an empty or self-closing varequal in a scored condition as a broken key and read cc_profile in Canvas export QTI (prove it: the DAPR 2255 live export must report 72); extend the Instructor Use Only exemption to the numbered title and numbered URL gates; accept the assignment total followed by pts or points; point the numbered paragraph message to the 11b worksheet block; hard fail #E65100 and rgb(230, 81, 0) and fix the old comments near lines 998 and 1010. Run against DAPR 2255 v82 and its live export, DAPR 2010 v21, DAPR 2020 v35 and DAPR 2000.
8. Every quiz at full count (25, Final 100).

## DAPR 2010 - Core Recording (not live; template)

1. Approved and applied: the ASP4816 rename. Cloudflare is current (all Auxiliary Resources and the renamed console PDF return 200).
2. Approved: page corrections a to f (show before and after), Mic_Book_Page_Template.docx to `_unused`, classic manual strip drawings that match Studio B (before and after), the Asp4816_Strip_Input re-crop (before and after).
3. Bring all 17 module quizzes from 10 to 25 questions with new practical questions from each module's reading. Report any module that cannot support 25.
4. Adam is running the 14 ChatGPT prompts; rebuild after he says they are saved.
5. Tell Adam which Canvas course the v20 and v21 imports went into.

## DAPR 2020 - Core Mixing (live Fall 2026)

1. v36: leave out Outline of Classes, Course Development Task List and Instructor Notes (empty in the export).
2. The live export has 0 broken quiz keys; no live regrade needed.
3. v35 has 284 questions against 400 in v34: bring every quiz back to full count.
4. Show Adam: the A2 side chain page with its callout table (1 trigger track, 2 key send, 3 side chain input, 4 the compressor on the ducked track, 5 its output pulling the ducked track down), the two new Professional Practice pages, and the quiz audit table.
5. The Syllabus stays as it was. B3 and B12 are ChatGPT prompts; no placeholders over existing images. Brief file name: `ChatGPT Image Prompts - DAPR 2020.md`.
6. The Lab Template gate problem is being fixed in preflight by the DAPR 2000 thread.
7. Before any live import, give Adam the plan for bringing v36 in without duplicate modules, pages or quizzes that already have attempts.

## DAPR 2255 - Audio Hardware I (live Fall 2026)

1. PRIORITY: update `Claude outputs/Notes and Briefs/2026-09-24 DAPR 2255 Live Quiz Regrade List.md` to the 72 broken keys in the live export, past due quizzes first. Adam regrades from it.
2. M06 and M08 instructor pages keep their live titles and URLs (preflight exemption being extended).
3. Pull the course 520146 image on M06 Voltage Regulators into the repo (show the image and path first); if the export lacks it, drop it and log it.
4. v83: the 14 assignment pages (state the 25 point total, printed rubric, one h2, 11b worksheet block).
5. #E65100 and rgb(230, 81, 0) count must be 0.
6. Four MIDI pages keep their 3D renders with the words in HTML beside them; the four _Alt files go to `_unused` (path table first). DMX_Fixture.jpg replaces the PAR photo. Resistors Q4 gets a 1/2 W option as the key.
7. Every trivia question replaced; every quiz at 25.
8. Give Adam the plan for bringing the new quizzes into the live course without duplicating quizzes that have attempts.

## DAPR 3255 - Audio Hardware II (not live; Spring 2027)

1. Do not edit preflight. The last class day rule (Tue 27 Apr) is kept.
2. Software Tools opens Mon 22 Mar (quiz due Fri 2 Apr), Wireless Systems opens Mon 29 Mar (quiz due Fri 9 Apr), both after Network Diagnostics; the final partial week is review only; bonus builds close Tue 27 Apr, 9:00 AM.
3. Rewrite the flagged questions: Livewire+ Q1, Networking Q3 Q24 (CIDR), Electronics Q7 Q19 (THD plus N), IP Addressing Q3 (keep only as a practical addressing choice). Every quiz at 25.
4. Build Course Orientation and Instructor Use Only (shared pages from the DAPR 2000 export).

## DAPR 3340 - Spatial Audio I (live Fall 2026, live course 641145, sandbox 644257)

1. List A approved, with the five held items (Renderer forum, External Renderer exercise, Configuring forum, Mixing in Atmos forum and quiz) moved to list B.
2. Catch up: the Surround Monitoring and Surround Recording exercises, 25 points each, open Mon 5 Oct, due Fri 9 Oct 9:00 AM (2026-10-09T15:00:00Z).
3. Instructor Course Management Notes and the second task list go into Instructor Use Only; drop Course Schedule, How to be a Successful Student and The Book Link.
4. Empty body pages stay out of the live import. Keep the live module titles. The three pages and one module left published in the LIVE import are accepted.
5. The 11 wrong keys are fixed; fix the two reading pages behind Mixing Q10. Adam gives full credit on live Intro Q1 and Q2 himself.
6. v54: bring the nine short quizzes to 25 questions at 1.00 point each. Save both cartridges locally; Adam imports v54-LIVE-Import into sandbox 644257 and then asks for the read-only check (no blank pages, no second Orientation or Instructor module, every list A date including 2026-10-09T15:00:00Z, the Final at 2026-12-10T19:50:00Z).
7. The symphony zip is live (HTTP 200).

## DAPR 3345 - Spatial Audio II (not live)

1. The orchestral assignment links the symphony zip at `https://uvu-files.adamo.workers.dev/DAPR-3340--Spatial_Audio_I/Auxiliary_Resources/2026-02-19_UVU_Symphony_Recording_-_Trimmed.zip` (live).
2. Banners: Implementation_Desk_Banner.jpg for the FMOD overview, Middleware_Desk_Banner.jpg for the Wwise overview.
3. Write ChatGPT prompts for new Workstation banners with the monitors defocused; do not overwrite the current files.
4. Rewrite Final Q26 (what RTPC stands for) as a practical question. Every quiz at 25.
5. Build Course Orientation and Instructor Use Only (shared pages from the DAPR 2000 export).
