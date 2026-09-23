# DAPR-3345--Spatial_Audio_II — Rename Handoff

**Date:** 2026-09-22  
**Course folder:** `DAPR-3345--Spatial_Audio_II`  
**Scope:** every GitHub image path and every Cloudflare download path in this course that changed.

## 1. What this file is for

Every image and download in this course was renamed to one universal standard. The old paths are gone. Any Canvas page, cartridge, quiz or capture sheet that still points at an old path is broken.

Use the tables below to rewrite this course's cartridge. Match on the old path, write the new path. Do not invent names, do not shorten them, do not re-case them. The new path column is the name on disk, byte for byte.

## 2. The naming rule, in full

Write the real title. Substitute three characters. Nothing else.

| In the real title | In the filename |
|---|---|
| space | `_` |
| colon | `__` |
| slash | `-` |

Commas simply disappear. Apostrophes simply disappear (`Ohm's Law` becomes `Ohms_Law`).

**Case.** Title Case, normal English rules. `a`, `an`, `the`, `is`, `and`, `or`, `to`, `of`, `in`, `for` stay lowercase unless one of them starts the name. Acronyms are fully uppercase: `AWG`, `SPL`, `EQ`, `DAW`, `LUFS`, `AES`, `LED`, `MIDI`, `IP`, `FMOD`, `BOAA`. A plural acronym takes a lowercase s: `LEDs`. Brand styling wins where a company sets it: `macOS`, not `MacOS`.

**Spelling.** American only, never British.

**Banned with no exceptions:** spaces, apostrophes, ampersands (write the word `and`), numbering of any kind, revision counters (`-01`, `-02`), version numbers (`v2`), course codes inside a filename, dates, uppercase extensions.

Numbering is the one worth restating. Modules get reordered every semester by design, and modules get dropped when the course learning outcomes are already covered elsewhere. A filename must never assume a position.

**Case is load bearing.** Both `raw.githubusercontent.com` and `uvu-files.adamo.workers.dev` are case sensitive and neither folds case. `Patch_Bays.pdf` and `patch_bays.pdf` are two different objects and one of them 404s. macOS being case insensitive by default is exactly why this goes wrong quietly.

## 3. The structure

```
Classes/<Course_Folder>/<Module_Name>/<Filename>.<ext>          GitHub, images
Canvas Links/<Course_Folder>/<Module_Name>/<Filename>.<ext>     Cloudflare, downloads
```

There is no `Images/` level. There is no module prefix on the filename. The parent folder IS the module name, and the two hosts use the same module folder names so they line up side by side.

Course folders keep their existing form in both places: `DAPR-<number><L if lab>--<Title_With_Underscores>`. The double hyphen there is deliberate and is the only place it appears.

PowerPoint decks, handouts, worksheets and session archives all live in the module folder they belong to, under the same rule. There is no separate `Presentations/`, `Handouts/`, `Audio/` or `Sessions/` folder, so a glance at a module folder shows whether that module has a deck.

## 4. GitHub image renames

**22 files.** Base URL: `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/`

| Old path | New path |
|---|---|
| `DAPR-3345--Spatial_Audio_II/Images/asset-pipeline/asset-pipeline-team-room-banner.jpg` | `DAPR-3345--Spatial_Audio_II/Asset_Pipeline/Team_Room_Banner.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/dolby-certification/dolby-certification-atmos-room-banner-01.jpg` | `DAPR-3345--Spatial_Audio_II/Dolby_Certification/Atmos_Room_Banner.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/final-project/final-project-playable-build-banner-01.jpg` | `DAPR-3345--Spatial_Audio_II/Final_Project/Player_at_Monitor_in_Dark_Room.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/final-project/final-project-playable-build-banner-02.jpg` | `DAPR-3345--Spatial_Audio_II/Final_Project/Player_at_Monitor_in_Lamplit_Room.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/final-project/final-project-study-guide-banner.jpg` | `DAPR-3345--Spatial_Audio_II/Final_Project/Study_Guide_Banner.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/fmod/fmod-implementation-desk-banner.jpg` | `DAPR-3345--Spatial_Audio_II/FMOD/Implementation_Desk_Banner.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/implementation/implementation-emitter-trigger-zone.jpg` | `DAPR-3345--Spatial_Audio_II/Implementation/Emitter_Trigger_Zone.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/implementation/implementation-listener-placement.jpg` | `DAPR-3345--Spatial_Audio_II/Implementation/Listener_Placement.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/interactive-audio/interactive-audio-cone-of-confusion.jpg` | `DAPR-3345--Spatial_Audio_II/Interactive_Audio/Cone_of_Confusion.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/interactive-audio/interactive-audio-distance-minimum-and-maximum.jpg` | `DAPR-3345--Spatial_Audio_II/Interactive_Audio/Distance_Minimum_and_Maximum.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/interactive-audio/interactive-audio-linear-versus-branching.jpg` | `DAPR-3345--Spatial_Audio_II/Interactive_Audio/Linear_versus_Branching.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/interactive-audio/interactive-audio-obstruction-versus-occlusion.jpg` | `DAPR-3345--Spatial_Audio_II/Interactive_Audio/Obstruction_versus_Occlusion.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/interactive-audio/interactive-audio-rooms-and-portals.jpg` | `DAPR-3345--Spatial_Audio_II/Interactive_Audio/Rooms_and_Portals.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/interactive-audio/interactive-audio-signal-chain-handoff.jpg` | `DAPR-3345--Spatial_Audio_II/Interactive_Audio/Signal_Chain_Handoff.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/interactive-audio/interactive-audio-workstation-banner.jpg` | `DAPR-3345--Spatial_Audio_II/Interactive_Audio/Workstation_Banner.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/interactive-mix/interactive-mix-controller-position-banner.jpg` | `DAPR-3345--Spatial_Audio_II/Interactive_Mix/Controller_Position_Banner.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/spatial-recording/spatial-recording-concert-hall-rig-banner-01.jpg` | `DAPR-3345--Spatial_Audio_II/Spatial_Recording/Frontal_Stage_View_with_Microphone_Tree.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/spatial-recording/spatial-recording-concert-hall-rig-banner-02.jpg` | `DAPR-3345--Spatial_Audio_II/Spatial_Recording/Angled_Stage_View_with_Boom_Array.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/variation/variation-layered-recombination.jpg` | `DAPR-3345--Spatial_Audio_II/Variation/Layered_Recombination.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/variation/variation-randomization-dimensions-banner-01.jpg` | `DAPR-3345--Spatial_Audio_II/Variation/Randomization_Dimensions_Banner.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/voice-budget/voice-budget-crowded-scene-banner.jpg` | `DAPR-3345--Spatial_Audio_II/Voice_Budget/Crowded_Scene_Banner.jpg` |
| `DAPR-3345--Spatial_Audio_II/Images/voice-budget/voice-budget-virtual-voices.jpg` | `DAPR-3345--Spatial_Audio_II/Voice_Budget/Virtual_Voices.jpg` |

## 5. Cloudflare download renames

**0 files.** Base URL: `https://uvu-files.adamo.workers.dev/`

None.

## 6. Unresolved

None for this course.

## 7. Reference rewrite status

Every reference inside the `Classes/` tree of this repo has been rewritten to the new paths. What has **not** been rewritten:

- The Canvas cartridge for this course. That is the job this file exists for.
- Live Canvas pages. They only change when the rebuilt cartridge is imported.
- Files under `_briefs/` and `_superseded/`. Those are historical working notes and were left alone on purpose.
- `DAPR-3345--Spatial_Audio_II--Image-Reference.html` at the course root, if one exists. It is a generated sheet and should be regenerated rather than patched.

## 8. Importing into Canvas

Canvas import **does not replace, it duplicates**. Canvas never deletes on import and no packaging trick avoids this.

| Object | On re-import into a course that already has content |
|---|---|
| Pages | May duplicate, object type dependent |
| Page publish state | Never changes on an existing page. Only the first import into a shell controls it |
| Quizzes | A new quiz copy is created. The existing quiz is not modified |
| Student attempts and grades | Stay attached to the OLD quiz. The new copy starts empty, so you get two gradebook columns |
| Clearing a bad import | One delete box per item, by hand, no bulk option |

Before importing into any live course:

1. Export the gradebook to CSV first. That is the only safety net.
2. On the import screen choose **Select specific content**, not All content, so Canvas shows what it found before committing.
3. Choose **Don't Import Policy** for the Automatic Missing Policy, or Canvas can post automatic zeroes for imported assignments whose due dates are already past.
4. After the import, check the destination course settings. An import can overwrite grade posting policy and license settings.

After importing, delete the superseded duplicates by hand. Never delete a quiz that carries student attempts. Where an old quiz holds real student work and a new copy exists, keep the old one, delete the new copy, and move the corrected content into the old quiz by editing it directly.
