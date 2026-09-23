# DAPR File Locations and Change Log

**Version:** 2026-09-23
**Applies to:** every DAPR course, every AI session, every Claude and ChatGPT project
**Companion to:** `2026-09-22 DAPR Universal File Naming Standard.md` (what files are named), `DAPR Canvas Standards.md` (how Canvas content is built), `UVU DAPR All Courses - Folder Map & CLOs.md` (which course, which outcomes)
**Maintained by:** adamo@uvu.edu

---

## 0. Read this first

On 2026-09-22 and 2026-09-23 the whole DAPR file layout changed. Thousands of files were renamed and moved, on GitHub, on Cloudflare, and across the Dropbox working folders.

If you are an AI session picking up work in any DAPR course, **the old paths are gone**. Do not recreate them. Do not "restore" a file to where you remember it being. Section 2 is the current map. Section 3 is what moved. Section 4 is the rules that keep it from drifting again.

---

## 1. The naming rule, in one line

Write the real title, then substitute three characters: **space becomes `_`, colon becomes `__`, slash becomes `-`.**

Commas and apostrophes disappear. `&` becomes the word `and` in anything that becomes a URL. Title Case, normal English rules. Acronyms fully uppercase (`DAW`, `EQ`, `MIDI`, `SPL`, `AES`, `LED`, `IP`, `FMOD`, `BOAA`), plurals take a lowercase s (`LEDs`). Brand styling wins where a company sets it (`macOS`). American spellings only.

**Banned everywhere:** spaces, apostrophes, ampersands, numbering of any kind, revision counters (`-01`), version numbers (`v2`), course codes inside a filename, dates, uppercase extensions.

Numbering is the one worth restating. Modules get reordered every semester by design and dropped when the learning outcomes are covered elsewhere. A filename must never assume a position.

**Case is load bearing.** `raw.githubusercontent.com` and `uvu-files.adamo.workers.dev` are both case sensitive. macOS is not. That is how this breaks quietly.

Full detail lives in `2026-09-22 DAPR Universal File Naming Standard.md`.

---

## 2. Where everything lives now

### 2.1 GitHub, images only

```
Classes/<Course_Folder>/<Module_Name>/<Filename>.<ext>
```

Served from `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/...`

There is **no `Images/` level**. There is **no module prefix on the filename**. The parent folder is the module name. That is the whole structure.

```
Classes/
└── DAPR-2255--Audio_Hardware_I/
    └── Batteries/
        ├── Assignment_Bench.jpg
        ├── Car_Battery.jpg
        └── Coin_Cell.jpg
```

Utility folders keep a leading underscore and are not modules: `_briefs`, `_duplicates`, `_review`, `_superseded`, `_unplaced`, `_to_delete`.

### 2.2 Cloudflare, downloads only

```
Canvas Links/<Course_Folder>/<Module_Name>/<Filename>.<ext>
```

Served from `https://uvu-files.adamo.workers.dev/...`

Same module folder names as GitHub, so the two trees read side by side. There is no `Handouts/`, `Sessions/`, `Audio/` or `Presentations/` level. A PowerPoint deck for a module sits in that module's folder, which is how you can see at a glance whether a module has a deck.

Local staging folder:
`/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Miscellaneous/4-Work/UVU/CloudFlare/Canvas Links/`

### 2.3 Canvas cartridges

```
<Course Folder>/Canvas/Canvas Templates/-Canvas Entire Course/*.imscc
```

**Every `.imscc` goes here. No exceptions.** Not in `Claude outputs`, not at the course root, not on the Desktop. This is the only place a session should look for the current cartridge, and the newest file by modified date is the current one.

`.imscc` files are exempt from the naming rule. They never appear in a URL and no student sees them. Canvas native exports keep the name Canvas gave them (`dapr-2000-002-_-2026-fall-full-term-export.imscc`), because that shape is the useful signal that it came out of Canvas rather than out of a build.

### 2.4 AI working output

```
<Course Folder>/Claude outputs/
    Notes and Briefs/    .md build notes, image briefs, audits, change logs
    Previews/            .html previews, capture sheets, schedule pastes
    Builds/              unpacked cartridge trees, build scripts, QTI, XML
    Media/               images, audio, session zips not yet filed
```

**Four buckets, no more.** Nothing goes loose at the root of `Claude outputs`. One `Claude outputs` folder per course, at the course root, never a second one under `Canvas/`.

Three shared ones exist outside the courses and follow the same four buckets:
`UVU Courses/Claude outputs/`, `Reference Files/.../UVU/Claude outputs/`, `Utah Valley University/Claude outputs/`

### 2.5 Standards documents

```
/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Applications/AI Projects Standards/Work/Utah Valley University/
```
mirrored to
```
/Users/adamwolson/Library/CloudStorage/GoogleDrive-adamo@uvu.edu/My Drive/AI Project Standards/
```

Standards files are exempt from the naming rule. They carry a date prefix and use spaces, because they are read by people and found by date.

### 2.6 Course working folders

Each course keeps five folders and no more:

```
<Course Folder>/
    Canvas/
    Claude outputs/
    Instructor Stuff/
    Miscellaneous/
    Presentations/
```

---

## 3. What changed

### 3.1 GitHub repository `Classes/`

| Change | Scale |
|---|---|
| Images renamed to the standard | 1,262 files |
| `Images/` level removed, files lifted to the course folder | 1,803 files moved |
| `<Module>__` filename prefix stripped | every renamed file |
| Topic folders renamed to Title Case with the three substitutions | 107 folders |
| Empty `Images/` shells removed | 4 folders |
| References rewritten to the flat paths | 1,802 substitutions across 62 files |
| Dropbox conflict folder removed after SHA-256 confirmed it was byte identical | 1 folder |
| `Tuning/` images recovered from `Timing/` | 4 files |
| Per-course rename handoff written into each course folder | 7 files |

Current repo: **2,074 files**.

Five `.wav` files in DAPR 2000 were found to be M4A files with the wrong extension, which is why Canvas showed "Your browser cannot play this file." Extensions corrected. Two of the five were byte identical and are now one file.

### 3.2 Cloudflare staging folder

Files moved into module folders and the `<Module>__` filename prefix stripped, 62 files. Twenty files whose meaningful hyphens had been destroyed by a bad transform were restored from backup.

**Not yet uploaded.** R2 still serves the old keys, which means every download in every live course still works and nothing is broken for students. The cartridges still point at those old keys. The upload and the cartridge rewrite have to happen as one unit.

### 3.3 Cartridges consolidated

| Course | Cartridges now in `-Canvas Entire Course` |
|---|---|
| DAPR 2000 Digital Audio Essentials | 5 |
| DAPR 2010 Core Recording | 20 |
| DAPR 2020 Core Mixing | 22 |
| DAPR 2255 Audio Hardware I | 17 |
| DAPR 3255 Audio Hardware II | 7 |
| DAPR 3340 Spatial Audio I | 9 |
| DAPR 3345 Spatial Audio II | 8 |

DAPR 2255 v72 through v76 and eight DAPR 2010 cartridges were sitting in `Claude outputs` and were moved back.

### 3.4 `Claude outputs` sorted

Eleven scattered folders holding 3,823 files and 3.08 GB became nine folders with four buckets each. 175 top-level items moved, none failed, nothing deleted. The duplicate `Canvas/Claude outputs` folders in DAPR 2000, 2020 and 3340 were merged into the course-root folder and removed.

Full move list: `UVU Courses/2026-09-23 Claude Outputs Sort Manifest.md`

### 3.5 Standards updated

`2026-09-22 DAPR Universal File Naming Standard.md` moved to version **2026-09-22b**. Section 4 rewritten. The `Images/` level and the filename prefix it used to describe are both gone.

---

## 4. Rules that keep this from drifting

1. **Folder names come from the Canvas module list, never from the folder names already on disk.** Open the newest cartridge in `-Canvas Entire Course`, read the module titles out of `imsmanifest.xml`, apply the three substitutions. Renaming what is already there just launders an old mistake into a new one. This rule exists because that is exactly what happened: 66 of 106 folders ended up named after page-level topics rather than modules.

2. **A folder is a module. Nothing else gets a folder.** If it is not in the module list, it is not a folder. Page-level topics do not get folders.

3. **Place a file by evidence, not by resemblance.** Which module's page references the file, read from the cartridge. Never fuzzy name matching. Anything nothing references goes to `_unplaced/` and waits for Adam.

4. **Never rename a Cloudflare key without saying so first.** GitHub references all live in the repo and can be rewritten in one pass. Cloudflare keys are referenced by cartridges. Both are findable and greppable, so both can be done, but the Cloudflare upload and the cartridge rewrite must ship together or a live download dies.

5. **Give full absolute paths, always, in a code block.** Adam hovers a path and runs a Keyboard Maestro shortcut that opens it in the Finder. A truncated or relative path is useless to him.

6. **Never put a file at the root of `Claude outputs`.** One of the four buckets, or the right permanent home.

7. **`.imscc` always goes to `-Canvas Entire Course`.**

8. **Do not restore old paths.** If a path in an old brief or an old chat does not exist, it was renamed on purpose. Look it up in the course's `__Rename_Handoff.md`.

---

## 5. Still open

- Folder names do not yet match module titles. 66 of 106 folders are named after page-level topics. The full plan is in `2026-09-23 DAPR Module Folder Plan.html`.
- 654 files are referenced by no page in any current cartridge and need placing by hand.
- Cloudflare is not synced to R2 and GitHub is not pushed, so both live hosts still serve the old paths.
- Cloudflare folder names do not match GitHub in 13 places.
- `DAPR-3345--Spatial_Audio_II/2026-02-19_UVU_Symphony_Recording_-_Trimmed.zip` is linked from the Spatial Audio II cartridge and is 404 on R2. Students clicking it get nothing.
- One audio file, `essentails-piano-01.wav`, is live on R2 but missing from the staging folder and has no name yet.

---

## 6. Reference files

```
/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Applications/AI Projects Standards/Work/Utah Valley University/2026-09-22 DAPR Universal File Naming Standard.md
/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Applications/AI Projects Standards/Work/Utah Valley University/2026-09-23 DAPR Module Folder Plan.html
/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses/2026-09-23 Claude Outputs Sort Manifest.md
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/DAPR-2000--Digital_Audio_Essentials__Rename_Handoff.md
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/DAPR-2010--Core_Recording__Rename_Handoff.md
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/DAPR-2020--Core_Mixing__Rename_Handoff.md
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/DAPR-2255--Audio_Hardware_I__Rename_Handoff.md
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/DAPR-3255--Audio_Hardware_II__Rename_Handoff.md
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/DAPR-3340--Spatial_Audio_I__Rename_Handoff.md
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/DAPR-3345--Spatial_Audio_II__Rename_Handoff.md
```
