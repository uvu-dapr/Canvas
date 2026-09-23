# DAPR-2010--Core_Recording — Rename Handoff

**Date:** 2026-09-22  
**Course folder:** `DAPR-2010--Core_Recording`  
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

**68 files.** Base URL: `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/`

| Old path | New path |
|---|---|
| `DAPR-2010--Core_Recording/Images/acoustics/acoustics-early-reflections-01.png` | `DAPR-2010--Core_Recording/Acoustics/Room_Plan_with_Reflection_Points_Marked.png` |
| `DAPR-2010--Core_Recording/Images/acoustics/acoustics-early-reflections-02.png` | `DAPR-2010--Core_Recording/Acoustics/Room_Paths_with_Arrival_Time_Graph.png` |
| `DAPR-2010--Core_Recording/Images/acoustics/acoustics-reflection-absorption-diffusion-01.png` | `DAPR-2010--Core_Recording/Acoustics/Blue_Arrow_Panels_on_Flat_Surfaces.png` |
| `DAPR-2010--Core_Recording/Images/acoustics/acoustics-reflection-absorption-diffusion-02.png` | `DAPR-2010--Core_Recording/Acoustics/Blue_Arrow_Panels_with_Angle_Arc.png` |
| `DAPR-2010--Core_Recording/Images/acoustics/acoustics-standing-waves-modes-01.png` | `DAPR-2010--Core_Recording/Acoustics/Standing_Waves_Modes.png` |
| `DAPR-2010--Core_Recording/Images/console-operation/console-operation-asp4816-block-diagram-full-01.png` | `DAPR-2010--Core_Recording/Console_Operation/Asp4816_Block_Diagram_Full.png` |
| `DAPR-2010--Core_Recording/Images/console-operation/console-operation-asp4816-connector-panel-01.png` | `DAPR-2010--Core_Recording/Console_Operation/Asp4816_Connector_Panel.png` |
| `DAPR-2010--Core_Recording/Images/console-operation/console-operation-asp4816-typical-configuration-01.png` | `DAPR-2010--Core_Recording/Console_Operation/Asp4816_Typical_Configuration.png` |
| `DAPR-2010--Core_Recording/Images/console-operation/console-operation-headphone-mix-flow-02.png` | `DAPR-2010--Core_Recording/Console_Operation/Headphone_Mix_Flow.png` |
| `DAPR-2010--Core_Recording/Images/console-operation/console-operation-troubleshooting-order-02.png` | `DAPR-2010--Core_Recording/Console_Operation/Troubleshooting_Order.png` |
| `DAPR-2010--Core_Recording/Images/console-signal-flow/console-signal-flow-asp4816-block-diagram-01.png` | `DAPR-2010--Core_Recording/Console_Signal_Flow/Asp4816_Block_Diagram.png` |
| `DAPR-2010--Core_Recording/Images/console-signal-flow/console-signal-flow-asp4816-full-panel-01.png` | `DAPR-2010--Core_Recording/Console_Signal_Flow/Asp4816_Full_Panel.png` |
| `DAPR-2010--Core_Recording/Images/console-signal-flow/console-signal-flow-asp4816-strip-auxiliaries-02.png` | `DAPR-2010--Core_Recording/Console_Signal_Flow/Asp4816_Strip_Auxiliaries.png` |
| `DAPR-2010--Core_Recording/Images/console-signal-flow/console-signal-flow-asp4816-strip-equalizers-02.png` | `DAPR-2010--Core_Recording/Console_Signal_Flow/Asp4816_Strip_Equalizers.png` |
| `DAPR-2010--Core_Recording/Images/console-signal-flow/console-signal-flow-asp4816-strip-input-01.png` | `DAPR-2010--Core_Recording/Console_Signal_Flow/Asp4816_Strip_Input.png` |
| `DAPR-2010--Core_Recording/Images/console-signal-flow/console-signal-flow-asp4816-strip-long-fader-02.png` | `DAPR-2010--Core_Recording/Console_Signal_Flow/Asp4816_Strip_Long_Fader.png` |
| `DAPR-2010--Core_Recording/Images/console-signal-flow/console-signal-flow-asp4816-strip-routing-02.png` | `DAPR-2010--Core_Recording/Console_Signal_Flow/Asp4816_Strip_Routing.png` |
| `DAPR-2010--Core_Recording/Images/console-signal-flow/console-signal-flow-asp4816-strip-short-fader-02.png` | `DAPR-2010--Core_Recording/Console_Signal_Flow/Asp4816_Strip_Short_Fader.png` |
| `DAPR-2010--Core_Recording/Images/course-orientation/course-orientation-course-card-01.png` | `DAPR-2010--Core_Recording/Course_Orientation/Course_Card.png` |
| `DAPR-2010--Core_Recording/Images/digital-recording/digital-recording-air-to-file-02.png` | `DAPR-2010--Core_Recording/Digital_Recording/Air_to_File.png` |
| `DAPR-2010--Core_Recording/Images/digital-recording/digital-recording-pro-tools-playback-engine-01.png` | `DAPR-2010--Core_Recording/Digital_Recording/Pro_Tools_Playback_Engine.png` |
| `DAPR-2010--Core_Recording/Images/digital-recording/digital-recording-sample-rate-bit-depth-02.png` | `DAPR-2010--Core_Recording/Digital_Recording/Sample_Rate_Bit_Depth.png` |
| `DAPR-2010--Core_Recording/Images/digital-recording/digital-recording-session-folder-02.png` | `DAPR-2010--Core_Recording/Digital_Recording/Session_Folder.png` |
| `DAPR-2010--Core_Recording/Images/drums/drums-kit-preparation-02.png` | `DAPR-2010--Core_Recording/Drums/Kit_Preparation.png` |
| `DAPR-2010--Core_Recording/Images/drums/drums-microphone-placement-01.png` | `DAPR-2010--Core_Recording/Drums/Overhead_Kit_Plan_with_Red_Markers.png` |
| `DAPR-2010--Core_Recording/Images/drums/drums-microphone-placement-02.png` | `DAPR-2010--Core_Recording/Drums/Perspective_Kit_with_Numbered_Blue_Markers.png` |
| `DAPR-2010--Core_Recording/Images/drums/drums-overhead-techniques-01.png` | `DAPR-2010--Core_Recording/Drums/Spaced_Pair_versus_Coincident_Line_Drawing.png` |
| `DAPR-2010--Core_Recording/Images/drums/drums-overhead-techniques-02.png` | `DAPR-2010--Core_Recording/Drums/Drum_Kit_Panels_with_Overhead_Options.png` |
| `DAPR-2010--Core_Recording/Images/drums/drums-tuning-and-prep-01.png` | `DAPR-2010--Core_Recording/Drums/Tuning_and_Prep.png` |
| `DAPR-2010--Core_Recording/Images/gain-staging/gain-staging-decibel-scales-02.png` | `DAPR-2010--Core_Recording/Gain_Staging/Decibel_Scales_with_Headroom_Bracket.png` |
| `DAPR-2010--Core_Recording/Images/gain-staging/gain-staging-decibel-scales-03.png` | `DAPR-2010--Core_Recording/Gain_Staging/Decibel_Scales_Aligned_at_Nominal.png` |
| `DAPR-2010--Core_Recording/Images/gain-staging/gain-staging-headroom-noise-floor-02.png` | `DAPR-2010--Core_Recording/Gain_Staging/Headroom_Noise_Floor.png` |
| `DAPR-2010--Core_Recording/Images/guitar-bass/guitar-bass-di-and-amp-blend-01.png` | `DAPR-2010--Core_Recording/Guitar_and_Bass/Instrument_Split_to_DI_and_Amp.png` |
| `DAPR-2010--Core_Recording/Images/guitar-bass/guitar-bass-di-and-amp-blend-02.png` | `DAPR-2010--Core_Recording/Guitar_and_Bass/Detailed_Signal_Chain_with_Orange_Note.png` |
| `DAPR-2010--Core_Recording/Images/guitar-bass/guitar-bass-speaker-cone-positions-01.png` | `DAPR-2010--Core_Recording/Guitar_and_Bass/Speaker_Cone_Face_with_Red_Markers.png` |
| `DAPR-2010--Core_Recording/Images/guitar-bass/guitar-bass-speaker-cone-positions-02.png` | `DAPR-2010--Core_Recording/Guitar_and_Bass/Speaker_Cone_with_Numbered_Blue_Callouts.png` |
| `DAPR-2010--Core_Recording/Images/impedance/impedance-bridging-versus-matching-02.png` | `DAPR-2010--Core_Recording/Impedance/Bridging_versus_Matching.png` |
| `DAPR-2010--Core_Recording/Images/impedance/impedance-five-connection-cases-01.png` | `DAPR-2010--Core_Recording/Impedance/Five_Connection_Cases.png` |
| `DAPR-2010--Core_Recording/Images/impedance/impedance-voltage-divider-02.png` | `DAPR-2010--Core_Recording/Impedance/Source_and_Load_Circuit_with_Table.png` |
| `DAPR-2010--Core_Recording/Images/impedance/impedance-voltage-divider-03.png` | `DAPR-2010--Core_Recording/Impedance/Resistor_Divider_with_Blue_Header_Table.png` |
| `DAPR-2010--Core_Recording/Images/microphones/microphones-polar-patterns-02.png` | `DAPR-2010--Core_Recording/Microphones/Polar_Plots_with_Ring_Scale_Legend.png` |
| `DAPR-2010--Core_Recording/Images/microphones/microphones-polar-patterns-03.png` | `DAPR-2010--Core_Recording/Microphones/Dark_Green_Polar_Pattern_Row.png` |
| `DAPR-2010--Core_Recording/Images/microphones/microphones-pressure-vs-gradient-01.png` | `DAPR-2010--Core_Recording/Microphones/Pressure_vs_Gradient.png` |
| `DAPR-2010--Core_Recording/Images/microphones/microphones-proximity-effect-02.png` | `DAPR-2010--Core_Recording/Microphones/Proximity_Effect.png` |
| `DAPR-2010--Core_Recording/Images/microphones/microphones-spec-sheet-anatomy-02.png` | `DAPR-2010--Core_Recording/Microphones/Spec_Sheet_Anatomy.png` |
| `DAPR-2010--Core_Recording/Images/microphones/microphones-transducer-types-02.png` | `DAPR-2010--Core_Recording/Microphones/Transducer_Types.png` |
| `DAPR-2010--Core_Recording/Images/miking-techniques/miking-techniques-coincident-arrays-02.png` | `DAPR-2010--Core_Recording/Miking_Techniques/Coincident_Arrays.png` |
| `DAPR-2010--Core_Recording/Images/miking-techniques/miking-techniques-phase-versus-polarity-02.png` | `DAPR-2010--Core_Recording/Miking_Techniques/Phase_versus_Polarity.png` |
| `DAPR-2010--Core_Recording/Images/miking-techniques/miking-techniques-spaced-arrays-01.png` | `DAPR-2010--Core_Recording/Miking_Techniques/ORTF_versus_Spaced_Pair_Panels.png` |
| `DAPR-2010--Core_Recording/Images/miking-techniques/miking-techniques-spaced-arrays-02.png` | `DAPR-2010--Core_Recording/Miking_Techniques/Array_Panels_with_Drawn_Microphones.png` |
| `DAPR-2010--Core_Recording/Images/miking-techniques/miking-techniques-three-to-one-rule-02.png` | `DAPR-2010--Core_Recording/Miking_Techniques/Titled_Leakage_Path_Spacing_Diagram.png` |
| `DAPR-2010--Core_Recording/Images/miking-techniques/miking-techniques-three-to-one-rule-03.png` | `DAPR-2010--Core_Recording/Miking_Techniques/Untitled_Leakage_Path_Spacing_Diagram.png` |
| `DAPR-2010--Core_Recording/Images/patch-bays/patch-bays-normalling-types-02.png` | `DAPR-2010--Core_Recording/Patch_Bays/Normalling_Columns_with_Plain_Jack_Boxes.png` |
| `DAPR-2010--Core_Recording/Images/patch-bays/patch-bays-normalling-types-03.png` | `DAPR-2010--Core_Recording/Patch_Bays/Normalling_Grid_with_Blue_Patch_Cables.png` |
| `DAPR-2010--Core_Recording/Images/patch-bays/patch-bays-studio-b-bay-map-01.png` | `DAPR-2010--Core_Recording/Patch_Bays/Studio_B_Bay_Map.png` |
| `DAPR-2010--Core_Recording/Images/studio-business/studio-business-cost-breakdown-01.png` | `DAPR-2010--Core_Recording/Studio_Business/Cost_Breakdown.png` |
| `DAPR-2010--Core_Recording/Images/studio-business/studio-business-rate-structures-01.png` | `DAPR-2010--Core_Recording/Studio_Business/Rate_Structures.png` |
| `DAPR-2010--Core_Recording/Images/studio-care/studio-care-fragile-gear-02.png` | `DAPR-2010--Core_Recording/Studio_Care/Fragile_Gear.png` |
| `DAPR-2010--Core_Recording/Images/studio-care/studio-care-power-up-sequence-02.png` | `DAPR-2010--Core_Recording/Studio_Care/Power_Up_Sequence.png` |
| `DAPR-2010--Core_Recording/Images/studio-care/studio-care-studio-floor-plan-01.png` | `DAPR-2010--Core_Recording/Studio_Care/Studio_Floor_Plan.png` |
| `DAPR-2010--Core_Recording/Images/studio-etiquette/studio-etiquette-assistant-timeline-01.png` | `DAPR-2010--Core_Recording/Studio_Etiquette/Assistant_Timeline.png` |
| `DAPR-2010--Core_Recording/Images/studio-etiquette/studio-etiquette-session-roles-02.png` | `DAPR-2010--Core_Recording/Studio_Etiquette/Session_Roles.png` |
| `DAPR-2010--Core_Recording/Images/tracking/tracking-pro-tools-edit-window-01.png` | `DAPR-2010--Core_Recording/Tracking/Pro_Tools_Edit_Window.png` |
| `DAPR-2010--Core_Recording/Images/tracking/tracking-pro-tools-mix-window-01.png` | `DAPR-2010--Core_Recording/Tracking/Pro_Tools_Mix_Window.png` |
| `DAPR-2010--Core_Recording/Images/tracking/tracking-pro-tools-record-arm-controls-01.png` | `DAPR-2010--Core_Recording/Tracking/Pro_Tools_Record_Arm_Controls.png` |
| `DAPR-2010--Core_Recording/Images/tracking/tracking-punch-and-playlists-02.png` | `DAPR-2010--Core_Recording/Tracking/Punch_and_Playlists.png` |
| `DAPR-2010--Core_Recording/Images/vocals/vocals-comping-playlists-01.png` | `DAPR-2010--Core_Recording/Vocals/Comping_Playlists.png` |
| `DAPR-2010--Core_Recording/Images/vocals/vocals-recording-chain-01.png` | `DAPR-2010--Core_Recording/Vocals/Recording_Chain.png` |

## 5. Cloudflare download renames

**38 files.** Base URL: `https://uvu-files.adamo.workers.dev/`

| Old path | New path | Module |
|---|---|---|
| `DAPR-2010--Core_Recording/Handouts/01-Basic_Studio_Etiquette.pdf` | `DAPR-2010--Core_Recording/Studio_Etiquette/Basic_Studio_Etiquette.pdf` | Studio Etiquette |
| `DAPR-2010--Core_Recording/Handouts/01-assistant_engineering.pdf` | `DAPR-2010--Core_Recording/Studio_Etiquette/Assistant_Engineering.pdf` | Studio Etiquette |
| `DAPR-2010--Core_Recording/Handouts/02-Studio_Checklist.docx` | `DAPR-2010--Core_Recording/Studio_Use_and_Care/Studio_Checklist.docx` | Studio Use & Care |
| `DAPR-2010--Core_Recording/Handouts/02-Studio_Rules.pdf` | `DAPR-2010--Core_Recording/Studio_Use_and_Care/Studio_Rules.pdf` | Studio Use & Care |
| `DAPR-2010--Core_Recording/Handouts/03-Mic_Book_Condensed.xlsx` | `DAPR-2010--Core_Recording/Microphones/Mic_Book_Condensed.xlsx` | Microphones |
| `DAPR-2010--Core_Recording/Handouts/03-Mic_Book_Page_Template.docx` | `DAPR-2010--Core_Recording/Microphones/Mic_Book_Page_Template.docx` | Microphones |
| `DAPR-2010--Core_Recording/Handouts/06-Impedance_Matching-Core_Recording.pdf` | `DAPR-2010--Core_Recording/Impedance_and_Voltage/Impedance_Matching.pdf` | Impedance and Voltage |
| `DAPR-2010--Core_Recording/Handouts/07-DAPR_Studio_Reservation_Agreement.docx` | `DAPR-2010--Core_Recording/Course_Orientation/DAPR_Studio_Reservation_Agreement.docx` | Course Orientation |
| `DAPR-2010--Core_Recording/Handouts/07-Equipment_and_Checkout_Criteria.docx` | `DAPR-2010--Core_Recording/Course_Orientation/Equipment_and_Checkout_Criteria.docx` | Course Orientation |
| `DAPR-2010--Core_Recording/Handouts/07-Reservable_Studio_Equipment.docx` | `DAPR-2010--Core_Recording/Course_Orientation/Reservable_Studio_Equipment.docx` | Course Orientation |
| `DAPR-2010--Core_Recording/Handouts/10-Drum_Setup_List.docx` | `DAPR-2010--Core_Recording/Drum_Recording/Drum_Setup_List.docx` | Drum Recording |
| `DAPR-2010--Core_Recording/Handouts/A_Horse_Is_Not_A_Home-Chord_Changes.pdf` | `DAPR-2010--Core_Recording/Final_Project/A_Horse_is_Not_a_Home_Chord_Changes.pdf` | Final Project |
| `DAPR-2010--Core_Recording/Handouts/A_Horse_is_Not_a_Home-Lyrics.pdf` | `DAPR-2010--Core_Recording/Final_Project/A_Horse_is_Not_a_Home_Lyrics.pdf` | Final Project |
| `DAPR-2010--Core_Recording/Handouts/Audient_ASP4816_Setup_Sheet.pdf` | `DAPR-2010--Core_Recording/Console_Signal_Flow/Audient_ASP4816_Setup_Sheet.pdf` | Console Signal Flow |
| `DAPR-2010--Core_Recording/Handouts/How_to_Create_Headphone_Mix_Audient.pdf` | `DAPR-2010--Core_Recording/Console_Operation/How_to_Create_Headphone_Mix_Audient.pdf` | Console Operation |
| `DAPR-2010--Core_Recording/Handouts/How_to_plug_in_a_mic_and_set_levels_Audient.pdf` | `DAPR-2010--Core_Recording/Console_Operation/How_to_Plug_in_a_Mic_and_Set_Levels_Audient.pdf` | Console Operation |
| `DAPR-2010--Core_Recording/Handouts/Studio_B_Patch_Bay.pdf` | `DAPR-2010--Core_Recording/Patch_Bays/Studio_B_Patch_Bay.pdf` | Patch Bays |
| `DAPR-2010--Core_Recording/Handouts/Studio_Map.pdf` | `DAPR-2010--Core_Recording/Final_Project/Studio_Map.pdf` | Final Project; Pro Tools for Tracking |
| `DAPR-2010--Core_Recording/Handouts/Track_List.xlsx` | `DAPR-2010--Core_Recording/Final_Project/Track_List.xlsx` | Final Project; Pro Tools for Tracking |
| `DAPR-2010--Core_Recording/Manuals/ASP4816-HE_Visualisation.pdf` | `DAPR-2010--Core_Recording/Course_Orientation/ASP4816_HE_Visualization.pdf` | Course Orientation |
| `DAPR-2010--Core_Recording/Manuals/Audient_ASP-4816_Console.pdf` | `DAPR-2010--Core_Recording/Console_Signal_Flow/Audient_ASP_4816_Console.pdf` | Console Signal Flow |
| `DAPR-2010--Core_Recording/Manuals/Connector_Panel_Visualisation.pdf` | `DAPR-2010--Core_Recording/Course_Orientation/Connector_Panel_Visualization.pdf` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/01-Behringer.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Behringer.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/01-Studio_Etiquette.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Studio_Etiquette.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/03-Microphones.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Microphones.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/03-Patch_Bay.pptx` | `DAPR-2010--Core_Recording/Patch_Bay.pptx` | NO MODULE REFERENCE |
| `DAPR-2010--Core_Recording/Presentations/04-Audient_ASP4816.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Audient_ASP4816.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/05-Console_Review.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Console_Review.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/05-Patch_Bay.pptx` | `DAPR-2010--Core_Recording/Archive/Patch_Bay_Duplicate.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/06-Audient_ASP4816.pptx` | `DAPR-2010--Core_Recording/Archive/Audient_ASP4816_Duplicate.pptx` | NO MODULE REFERENCE |
| `DAPR-2010--Core_Recording/Presentations/06-Gain_Staging.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Gain_Staging.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/06-Impedance_and_dB.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Impedance_and_dB.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/07-Tracking_Techniques.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Tracking_Techniques.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/08-Multi_Mic_Setups.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Multi_Mic_Setups.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/08-Sonic_Reality_in_a_Virtual_World.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Sonic_Reality_in_a_Virtual_World.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/09-Acoustics.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Acoustics.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/12-Digital_Audio_Workstations.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Digital_Audio_Workstations.pptx` | Course Orientation |
| `DAPR-2010--Core_Recording/Presentations/Mid_Side_Miking_Presentation.pptx` | `DAPR-2010--Core_Recording/Course_Orientation/Mid_Side_Miking_Presentation.pptx` | Course Orientation |

## 6. Unresolved

None for this course.

## 7. Reference rewrite status

Every reference inside the `Classes/` tree of this repo has been rewritten to the new paths. What has **not** been rewritten:

- The Canvas cartridge for this course. That is the job this file exists for.
- Live Canvas pages. They only change when the rebuilt cartridge is imported.
- Files under `_briefs/` and `_superseded/`. Those are historical working notes and were left alone on purpose.
- `DAPR-2010--Core_Recording--Image-Reference.html` at the course root, if one exists. It is a generated sheet and should be regenerated rather than patched.

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
