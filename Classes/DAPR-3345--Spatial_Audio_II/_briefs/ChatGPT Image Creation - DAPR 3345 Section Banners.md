# DAPR 3345 Image Brief - Section Banners
Revision 3, 2026-09-23. Rewritten against `2026-09-23 DAPR File Locations and Change Log.md`
and `DAPR-3345--Spatial_Audio_II__Rename_Handoff.md`.

**There is nothing left to generate.** All four generatable banners are done and in place.
What remains is four screen captures, two retirements, and one recompression.

---

## What revision 2 got wrong

Revision 2 was written against `DAPR Canvas Standards §20.4`, which was superseded the same
day by the Universal File Naming Standard. Three things in it are now wrong:

| Revision 2 said | The standard says |
|---|---|
| `dolby-certification-atmos-room-banner-01.jpg` | `Atmos_Room_Banner.jpg`. Title Case, underscores, **no module prefix** |
| Add the two-digit counter `-01` | **Revision counters are banned with no exceptions.** A replacement keeps the same filename |
| Save into `Images/<topic-slug>/` | There is **no `Images/` level**. The module folder sits directly under the course folder |

I corrected you toward `-01` on 22 September after reading §20.4. That section was already
superseded when I read it. The counter was my error twice over: absent the first time,
insisted on the second.

Filenames below are the names on disk, byte for byte, taken from the repo as it stands
this morning.

---

## Every image in the course, checked

22 files across 10 module folders.

### Ship as they are

| Module folder | File | Note |
|---|---|---|
| `Asset_Pipeline` | `Team_Room_Banner.jpg` | Team desks, kanban board, concept art |
| `Dolby_Certification` | `Atmos_Room_Banner.jpg` | Three fronts, two sides, four ceiling speakers. The overhead layer is unmistakable |
| `Implementation` | `Emitter_Trigger_Zone.jpg` | Point emitter, two box volumes at different scales |
| `Implementation` | `Listener_Placement.jpg` | Adequate. Listener marker on the head, camera behind |
| `Interactive_Audio` | `Cone_of_Confusion.jpg` | Two sources on one cone surface, apex at the ear. Textbook |
| `Interactive_Audio` | `Distance_Minimum_and_Maximum.jpg` | Corrected 22 September. Spheres centered on the emitter, two source sizes |
| `Interactive_Audio` | `Linear_versus_Branching.jpg` | One timeline, branch point, four outcomes |
| `Interactive_Audio` | `Obstruction_versus_Occlusion.jpg` | Thin panel bends sound, thick wall stops it, listener between |
| `Interactive_Audio` | `Rooms_and_Portals.jpg` | Four rooms, sound through the doorway only |
| `Interactive_Audio` | `Signal_Chain_Handoff.jpg` | Decorative rather than instructive, but nothing false |
| `Interactive_Mix` | `Controller_Position_Banner.jpg` | Mix room, surround monitors, controller at the sweet spot |
| `Variation` | `Layered_Recombination.jpg` | Four stacks, same layers, different permutations. One of the best |
| `Variation` | `Randomization_Dimensions_Banner.jpg` | Eight identical cubes, eight different forms. Reads instantly |
| `Voice_Budget` | `Crowded_Scene_Banner.jpg` | Cutaway of a busy facility, dozens of sources |
| `Voice_Budget` | `Virtual_Voices.jpg` | Warm spheres audible, pale spheres virtualized |

### The two you regenerated overnight, both improved

| File | Verdict |
|---|---|
| `Spatial_Recording/Angled_Stage_View_with_Boom_Array.jpg` | **Ship it.** The three-quarter angle fixed the problem. The centre microphone now hangs forward and below the bar with the two outers swept back, so the tree reads as a triangle rather than a straight line. Ambisonic spheres, outriggers, spots, harp and timpani all present. |
| `Final_Project/Player_at_Monitor_in_Lamplit_Room.jpg` | **Ship it.** The lamp carries detail across all three thirds. Controller and hands read clearly, the screen still holds untextured grey geometry with the warm light at the end, and no heads-up display crept in. |

### Retire these two, superseded by the pair above

| File | Reason |
|---|---|
| `Spatial_Recording/Frontal_Stage_View_with_Microphone_Tree.jpg` | Microphone tree reads as a straight line, not a triangle |
| `Final_Project/Player_at_Monitor_in_Dark_Room.jpg` | Outer thirds near black. On a white page it reads as a bar with a bright window |

Nothing references either one yet, so both can go to `_superseded/` whenever you like.

### Two that violate §20.1 rule 3 and need capturing

| File | Problem |
|---|---|
| `FMOD/Implementation_Desk_Banner.jpg` | Fabricated DAW timeline on the monitor. Also opens **both** the FMOD and the Wwise sections |
| `Interactive_Audio/Workstation_Banner.jpg` | Fabricated DAW timeline **and** a fabricated engine viewport. I passed this in the 22 September audit and should not have |

§20.1 rule 3 names DAW windows explicitly. A generator invents controls and fabricates
model numbers, and a photorealistic fake is more convincing and exactly as wrong.

---

## The four captures

Screenshot or screen-recording still from the real application. Crop to **1600 x 667**,
save **JPEG quality 88**, keep under 500 KB.

| # | Save to | Capture |
|---|---|---|
| 01 | `FMOD/Authoring_Session_Banner.jpg` | A real FMOD Studio session, wide crop. Event editor open, timeline legible, a 3D panner or spatializer visible on an event. It must be recognisably FMOD |
| 02 | `Wwise/Authoring_Hierarchy_Banner.jpg` | A real Wwise Authoring session, Project Explorer tree expanded down the left so the hierarchy is the subject. Voice Profiler or attenuation editor in frame is a bonus. **Create the folder `Wwise/`** |
| 03 | `Implementation/Engine_Editor_Banner.jpg` | A real engine editor, level open with audio emitters placed, and a code editor in the same frame showing a script that posts an event or sets a parameter |
| 04 | `Interactive_Audio/Workstation_Banner.jpg` | A real DAW session and a real engine viewport side by side, the same comparison the current file fakes. **Same filename**, so the URL does not change |

Full destination for all four:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/
```

Raw URL pattern after push:

```
https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3345--Spatial_Audio_II/<Module_Folder>/<Filename>.jpg
```

Captures 01 and 02 exist so FMOD and Wwise stop opening with the same borrowed photograph.

**Note on `Wwise/`:** the change log says folder names must come from the Canvas module list
rather than from what is on disk, and that 66 of 106 folders do not yet match. The 3345
module is `Wwise: Implementation and Certification in Wwise`, and every sibling folder here
uses the part before the colon, so `Wwise/` is consistent with `FMOD/`, `Variation/` and the
rest. If the Module Folder Plan lands on something different, this one moves with them.

---

## Two housekeeping items

**One file is over the weight cap.** §20.3 caps a JPEG at 500 KB.

| File | Size |
|---|---|
| `Final_Project/Study_Guide_Banner.jpg` | 532,822 bytes, 520 KB |

Everything else is inside. One command fixes it and I can run it on your say-so.

**Width.** §20.3 sets a full-width Canvas figure at 1600 px. The two new images came back at
1600 x 667, correct. The other twenty did not move in the restructure and are still at their
original sizes:

| Shape | Count | Width |
|---|---|---|
| New, from revision 2 prompts | 2 | **1600** |
| Banners | 9 | 1942 |
| Concept figures | 9 | 1536 |

Nothing is broken, because the pages carry `max-width:100%`. It is a standards gap, and now
that two files are correct the set is inconsistent in a way it was not before. Down-sampling
all twenty to 1600 wide is one pass, no regeneration, no filename changes, and no reference
rewrites, since only the pixels change. Say the word.

---

## What I do next

1. Rewrite every `<img>` in the cartridge from the old `Images/<slug>/<prefixed-name>` paths
   to the new flat module paths, using the Rename Handoff table rather than guessing.
2. Add the banner block to the section overviews that have none.
3. Point the Wwise overview at its own banner instead of FMOD's.
4. Regenerate the Image Reference page against the new structure.
5. HTTP check every raw URL and report any that does not return 200.

Then push, or GitHub keeps serving nothing at the new paths:

```
cd ~/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II && git add -A && git status
```
