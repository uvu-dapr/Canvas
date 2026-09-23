# DAPR Restructure: Session Handoff

**Date:** 2026-09-23
**Purpose:** everything a new session needs to pick this up without redoing work or undoing it.
**Read first:** `2026-09-22 DAPR Canvas Standards.md` §8.0.1. It is the single authority on filenames, module folder names, and where every file lives. Everything below is state, not rules.

---

## 1. What this was

Every folder under `Classes/` and `Canvas Links/` was renamed so that **one folder equals one Canvas module**, with the module name read from that course's current cartridge. Roughly 1,300 files moved. Both hosts now match each other.

Before: folders were named after page-level topics, in a mix of lowercase-hyphen and Title Case, with an `Images/` level and a topic prefix on every filename.
After: `Classes/<Course_Folder>/<Module_Name>/<Filename>.<ext>`, no `Images/`, no prefix.

---

## 2. Current state, measured

| Course | GitHub module folders | GitHub `_unused` | Cloudflare module folders | Cloudflare `_unused` |
|---|---|---|---|---|
| DAPR-2000--Digital_Audio_Essentials | 17 | 96 | 1 | 3 |
| DAPR-2010--Core_Recording | 17 | 126 | 12 | 17 |
| DAPR-2020--Core_Mixing | 16 | 98 | 14 | 0 |
| DAPR-2255--Audio_Hardware_I | 20 | 40 | 0 | 0 |
| DAPR-3255--Audio_Hardware_II | 8 | 59 | 0 | 0 |
| DAPR-3340--Spatial_Audio_I | 12 | 96 | 3 | 0 |
| DAPR-3345--Spatial_Audio_II | 9 | 7 | 0 | 0 |

GitHub: 2,059 files. Cloudflare: 82 files.

**Zero folders on either host carry a number, a week, a `%`, or a `- (Unified Class Content)` marker.**

---

## 3. Decisions Adam made today. Do not relitigate these.

| Decision | What it means |
|---|---|
| Folder names come from `course_settings/module_meta.xml`, never from folders already on disk | Transliterating existing folder names is what produced 66 wrong folders on 2026-09-22 |
| A folder is a module. Page-level topics get no folder | |
| Strip `M##:`, `(Week N)`, `(Finals Week)`, `(5% Total)`, `%`, `- (Unified Class Content)` before the substitutions, **without asking** | §6.2 is unconditional |
| DAPR 2020 keeps the colon prefix `module_meta` carries | `Mixing__Comping_and_Arrangement`, not `Comping_and_Arrangement` |
| Place files by cartridge evidence, never by name resemblance | |
| When a file is referenced from several modules, the **most specific** module wins | The module referencing the fewest files. A resources page that links everything never wins |
| Unreferenced files go to `_unused/<folder it came from>/` | Never parked in a real module folder |
| **Course Orientation holds images only** | No deck, no handout, no session archive, ever |
| Byte-identical duplicates are deleted, unique unreferenced files are kept | 40 deleted, 528 kept |
| Blueprint module names decide folder names; sync state decides only where files sit | Both `All/X` and `<Course>/X` can exist and both be correct |
| R2 gets a destructive mirror (`rclone sync`), old keys deleted | Adam's explicit choice, made knowing live cartridges break until re-imported |

---

## 4. What is DONE

- **GitHub restructure.** Committed and pushed. Two commits: `b8bd650` (restructure) and `92ec1d9` (restore, dedupe, inventories). `origin/main` is at `92ec1d9`. Working tree clean.
- **1,282 references rewritten** across 36 files in the repo to the new paths. Every remaining unresolved link is in `_briefs`, an archived icon page, or a generated `--Image-Reference.html` sheet. No live module content has a dead link.
- **Blueprint modules moved to `All/`:** `CS_623a_BOAA_Lab` (68 files, merged from the old `CS623A_Lab` and `BOAA_Lab` which were two halves of one module), `Bonus__Assignments`, `Student_Essentials`.
- **196 files restored** from `_unused` to their module, where the folder they came from was an exact module name.
- **40 byte-identical duplicates deleted.**
- **Per-course unused inventories written** to `Classes/<Course>/<Course>__Unused_Inventory.md`.
- **Standards consolidated.** Naming and locations folded into Canvas Standards §8.0.1. The separate Universal File Naming Standard and File Locations files are archived with a note explaining why.

---

## 5. What is IN FLIGHT

**The R2 sync is running or just finished.** Adam started it at roughly 10:31 Mountain on 2026-09-23. It is 18.16 GiB of uploads and 155 deletes freeing 32.11 GiB.

As of the last live check, old keys still returned 200 and new paths still returned 404, so it had not completed.

**A second sync pass is required.** After the first finishes, run the same command again:

```
rclone sync "/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links" uvu-r2:uvu-canvas-files --exclude ".DS_Store" --exclude "**/_unused/**" --progress
```

Why: 14 PowerPoints and handouts were wrongly sitting in `DAPR-2010--Core_Recording/Course_Orientation/` when the first run started. They have since been moved to `_unused/Course_Orientation/`. The second pass removes them from R2 if the first uploaded them.

**Verify after it finishes.** These should return 200:

```
https://uvu-files.adamo.workers.dev/DAPR-2020--Core_Mixing/Monitoring__Calibration_and_Monitoring/Calibration.pptx
https://uvu-files.adamo.workers.dev/DAPR-2010--Core_Recording/Acoustics/Acoustics.pptx
https://uvu-files.adamo.workers.dev/DAPR-3340--Spatial_Audio_I/The_Dolby_Atmos_Renderer/Natures_Fury_Dolby_Demo.zip
```

These should return 404:

```
https://uvu-files.adamo.workers.dev/DAPR-2020--Core_Mixing/Presentations/calibration.pptx
https://uvu-files.adamo.workers.dev/DAPR-2010--Core_Recording/Course_Orientation/Multi_Mic_Setups.pptx
```

---

## 6. What is NOT done

### 6.1 Every live cartridge is now broken against Cloudflare

Once the sync completes, every `uvu-files` URL in every live course 404s until that course's cartridge is rebuilt with the new paths and re-imported. This is expected and was Adam's choice. **The seven cartridges have not been rebuilt.**

Use `Classes/2026-09-23 DAPR Cloudflare Download Index.md` for the correct URLs and `Classes/2026-09-23 DAPR Module Folder Rename Map.md` for every old-to-new path.

### 6.2 810 external quiz image references

Quiz images must be embedded in the cartridge and referenced with `$IMS-CC-FILEBASE$/Uploaded%20Media/<filename>`. Canvas renders quizzes in a sandboxed iframe with `default-src none`, so an external URL is a broken image with no workaround.

Measured across the seven current cartridges: **810 external against 133 correctly embedded.** Five of seven courses have none embedded.

| Course | External | Embedded |
|---|---|---|
| DAPR 2000 | 98 | 122 |
| DAPR 2010 | 103 | 0 |
| DAPR 2020 | 85 | 0 |
| DAPR 2255 | 127 | 0 |
| DAPR 3255 | 181 | 11 |
| DAPR 3340 | 111 | 0 |
| DAPR 3345 | 105 | 0 |

The images those quizzes reference are already correctly placed in module folders. The job is: copy each into `web_resources/Uploaded Media/`, declare it in `imsmanifest.xml`, rewrite the quiz XML. Do it during the cartridge rebuild, not as a separate pass.

### 6.3 528 unique unreferenced files

Sitting in `_unused/` across the seven courses. No page, quiz, or module item in any current cartridge references them. Almost certainly artwork from earlier builds that later cartridge versions dropped. Each course has an inventory listing filename, source folder, size and pixel dimensions. **Do not delete without Adam.**

### 6.4 Two cartridges unreadable

Adam downloaded fresh Canvas exports today. These are cloud-only in Dropbox and cannot be opened without hydrating them:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses/DAPR 2255 - Audio Hardware I/Canvas/Canvas Templates/-Canvas Entire Course/dapr-2255-001-_-2026-fall-full-term-export.imscc copy
```
(135 MB, and the DAPR 3340 equivalent.) They hold the current live Course Essentials layout. Adam said they are **not** the target state, only a reference for how Canvas looks today.

### 6.5 Still owed to Adam

He asked for these and they were not delivered before the model switch:

1. **A zip per course** containing that course's markdown so the per-course thread can start updating.
2. **A brand new `.imscc` per course** pointing at the new GitHub and Cloudflare locations, including the PowerPoints, following the course outline and due dates.
3. **A paste-ready prompt block per course** to drop into each Claude project.

Source material for 2 and 3: `UVU Courses/DAPR-Course-Build-Specs/` has a Build Spec per course with term and date rules. Fall house rule: a module opens **Monday** of its week and never closes; everything is due **Friday 9:00 AM Mountain**, never midnight; point value sets the window. Fall 2026 DST boundary is 1 November 2026, so 9:00 AM Mountain is `15:00:00Z` before and `16:00:00Z` after.

---

## 7. Where things live

```
Classes/<Course_Folder>/<Module_Name>/<Filename>.<ext>                GitHub images
Canvas Links/<Course_Folder>/<Module_Name>/<Filename>.<ext>           Cloudflare downloads
<Course Folder>/Canvas/Canvas Templates/-Canvas Entire Course/*.imscc  cartridges, all of them
<Course Folder>/Claude outputs/{Notes and Briefs,Previews,Builds,Media}/  AI working output
```

Standards folder, rules only:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Applications/AI Projects Standards/Work/Utah Valley University/
    2026-09-22 DAPR Canvas Standards.md                    367 KB, the authority
    2026-09-22 Canvas Platform and IMSCC Reference.md      170 KB
    2026-09-22 UVU DAPR All Courses - Folder Map & CLOs.md  91 KB
    2026-09-20 UVU Fall 2026 Term Spine.md
    2026-09-20 UVU Spring 2027 Term Spine.md
    Archive/2026-09-23 Why these are archived.md
```

Mirrored to Google Drive `AI Project Standards/`. Lookups live in the repo, not here.

---

## 8. Working habits Adam expects

- **Full absolute paths, always, in a code block.** He hovers a path and runs a Keyboard Maestro shortcut that opens it in Finder. A relative or truncated path is useless.
- **No dashes of any kind** in prose. No em dashes, en dashes, or double hyphens.
- **Ask one question at a time with a recommendation**, using the multiple-choice tool, not prose questions.
- **Never guess a file's module from its name.** Read the cartridge.
- **Do not ask about things his standards already settle.** §6.2 bans numbering unconditionally, so strip it and move on.
- He corrects errors explicitly and expects the correction acknowledged, not defended.

---

## 9. Access notes for the next session

- `rclone` is **not** available in the device VM. Cloudflare sync commands have to be run by Adam in Terminal on his Mac.
- Git works from `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas` but **push fails**, no credentials in the VM. Commit here, Adam pushes.
- Delete permission was granted this session for the UVU folder, the Canvas repo, and the Reference Files UVU folder. A new session starts without it and must request it again.
- The Canvas repo root is a granted folder, not a default connected one. A new session may only see `Classes/` and will need to request the parent to run git.
