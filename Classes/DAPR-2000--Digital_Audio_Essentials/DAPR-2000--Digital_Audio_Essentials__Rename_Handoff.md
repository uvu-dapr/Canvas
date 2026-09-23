# DAPR-2000--Digital_Audio_Essentials — Rename Handoff

**Date:** 2026-09-22  
**Course folder:** `DAPR-2000--Digital_Audio_Essentials`  
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

**250 files.** Base URL: `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/`

| Old path | New path |
|---|---|
| `DAPR-2000--Digital_Audio_Essentials/Images/careers/careers-game-audio-pipeline-01.png` | `DAPR-2000--Digital_Audio_Essentials/Careers/Game_Audio_Pipeline.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/careers/careers-live-sound-roles-01.png` | `DAPR-2000--Digital_Audio_Essentials/Careers/Live_Sound_Roles.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/careers/careers-music-production-roles-01.png` | `DAPR-2000--Digital_Audio_Essentials/Careers/Music_Production_Roles.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/careers/careers-pathway-map-01.png` | `DAPR-2000--Digital_Audio_Essentials/Careers/Pathway_Map.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/careers/careers-post-production-roles-01.png` | `DAPR-2000--Digital_Audio_Essentials/Careers/Post_Production_Roles.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/course-info/course-info-mac-disk-utility-erase-button-01.png` | `DAPR-2000--Digital_Audio_Essentials/Course_Info/MAC_Disk_Utility_Erase_Button.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/course-info/course-info-mac-disk-utility-erase-menu-01.png` | `DAPR-2000--Digital_Audio_Essentials/Course_Info/MAC_Disk_Utility_Erase_Menu.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/course-info/course-info-mac-disk-utility-show-all-devices-01.png` | `DAPR-2000--Digital_Audio_Essentials/Course_Info/MAC_Disk_Utility_Show_All_Devices.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/course-info/course-info-mac-erase-exfat-01.png` | `DAPR-2000--Digital_Audio_Essentials/Course_Info/MAC_Erase_Exfat.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/course-orientation/course-orientation-uvu-digital-media-logo-01.png` | `DAPR-2000--Digital_Audio_Essentials/Course_Orientation/Uvu_Digital_Media_Logo.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-api-560-graphic-eq-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Api_560_Graphic_EQ.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-bell-eq-or-parametric-eq-gain-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Bell_EQ_or_Parametric_EQ_Gain.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-bell-eq-or-parametric-eq-plus-gain-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Bell_EQ_or_Parametric_EQ_Plus_Gain.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-edit-tools-tool-quiz-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Three_Tool_Group_Highlighted.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-edit-tools-tool-quiz-02.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Magnifier_Zoom_Icon_Highlighted.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-edit-tools-tool-quiz-03.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Trim_Arrows_Icon_Highlighted.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-edit-tools-tool-quiz-04.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Waveform_Select_Icon_Highlighted.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-edit-tools-tool-quiz-05.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Open_Hand_Icon_Highlighted.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-edit-tools-tool-quiz-06.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Speaker_Scrub_Icon_Highlighted.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-edit-tools-tool-quiz-07.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pencil_Icon_Highlighted.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-eq-filter-slopes-01.svg` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/EQ_Filter_Slopes.svg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-frequency-chart-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Frequency_Chart.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-gml-8200-parametric-eq-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Gml_8200_Parametric_EQ.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-high-pass-filter-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/High_Pass_Filter.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-high-shelving-eq-gain-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/High_Shelving_EQ_Gain.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-high-shelving-eq-plus-gain-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/High_Shelving_EQ_Plus_Gain.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-low-pass-filter-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Low_Pass_Filter.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-low-shelving-eq-gain-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Low_Shelving_EQ_Gain.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-low-shelving-eq-plus-gain-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Low_Shelving_EQ_Plus_Gain.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-maag-eq4-air-band-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Maag_Eq4_Air_Band.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-module-banner-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Module_Banner.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-blank-edit-window-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Blank_Edit_Window.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-blank-mix-window-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Blank_Mix_Window.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-dashboard-key-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Dashboard_Key.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-fader-and-meters-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Fader_and_Meters.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-i-o-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_I-O.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-inserts-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Inserts.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-panner-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Panner.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-splash-screen-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Splash_Screen.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-track-with-clip-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Track_with_Clip.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-track-with-clip-labeled-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Track_with_Clip_Labeled.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-pro-tools-transport-controls-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Transport_Controls.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-eq-dynamics/daw-eq-dynamics-the-anatomy-of-a-compressor-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/The_Anatomy_of_a_Compressor.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-first-mix/daw-first-mix-drum-routing-example-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__First_Mix/Drum_Routing_Example.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-first-mix/daw-first-mix-pro-tools-blank-mix-window-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__First_Mix/Pro_Tools_Blank_Mix_Window.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-first-mix/daw-first-mix-pro-tools-hard-panned-channel-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__First_Mix/Pro_Tools_Hard_Panned_Channel.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-first-mix/daw-first-mix-sends-aux-and-effects-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__First_Mix/Sends_Aux_and_Effects.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/daw-first-mix/daw-first-mix-three-checks-01.png` | `DAPR-2000--Digital_Audio_Essentials/DAW__First_Mix/Three_Checks.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/digital-domain/digital-domain-bit-depth-ladder-01.png` | `DAPR-2000--Digital_Audio_Essentials/Digital_Domain/Bit_Depth_Ladder.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/digital-domain/digital-domain-module-banner-01.png` | `DAPR-2000--Digital_Audio_Essentials/Digital_Domain/Module_Banner.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/digital-domain/digital-domain-sampling-quantization-01.png` | `DAPR-2000--Digital_Audio_Essentials/Digital_Domain/Sampling_Quantization.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/exams/exams-final-topic-map-01.png` | `DAPR-2000--Digital_Audio_Essentials/Exams/Final_Topic_Map.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/microphones-characteristics/microphones-characteristics-mic-pattern-polar-chart-cardioid-labeled-01.png` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics/Mic_Pattern_Polar_Chart_Cardioid_Labeled.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/microphones-characteristics/microphones-characteristics-module-banner-01.png` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics/Module_Banner.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/microphones-characteristics/microphones-characteristics-polar-chart-supercardioid-labeled-01.png` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics/Polar_Chart_Supercardioid_Labeled.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/microphones-characteristics/microphones-characteristics-polarpatterncomparison-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics/Polarpatterncomparison.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/microphones-stereo-techniques/microphones-stereo-techniques-pro-tools-hard-panned-channel-01.png` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Stereo_Techniques/Channel_Strip_with_Centered_Pan_Knobs.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/microphones-stereo-techniques/microphones-stereo-techniques-pro-tools-hard-panned-channel-02.png` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Stereo_Techniques/Channel_Strip_with_Hard_Panned_Knobs.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/microphones-stereo-techniques/microphones-stereo-techniques-stereo-mic-techniques-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Stereo_Techniques/Stereo_Mic_Techniques.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/microphones-stereo-techniques/microphones-stereo-techniques-stereo-recording-techniques-graphic4-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Stereo_Techniques/Stereo_Recording_Techniques_Graphic4.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/microphones-stereo-techniques/microphones-stereo-techniques-xy-coincident-pair-01.jpeg` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Stereo_Techniques/Xy_Coincident_Pair.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/mixing-mastering/mixing-mastering-automation-timeline-01.png` | `DAPR-2000--Digital_Audio_Essentials/Mixing_and_Mastering/Automation_Timeline.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/mixing-mastering/mixing-mastering-loudness-ceiling-01.png` | `DAPR-2000--Digital_Audio_Essentials/Mixing_and_Mastering/Loudness_Ceiling.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/mixing-mastering/mixing-mastering-mastering-chain-01.png` | `DAPR-2000--Digital_Audio_Essentials/Mixing_and_Mastering/Mastering_Chain.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/mixing-mastering/mixing-mastering-mix-arc-01.png` | `DAPR-2000--Digital_Audio_Essentials/Mixing_and_Mastering/Mix_Arc.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/mixing-mastering/mixing-mastering-module-banner-01.png` | `DAPR-2000--Digital_Audio_Essentials/Mixing_and_Mastering/Module_Banner.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/mixing-mastering/mixing-mastering-sample-vs-true-peak-01.png` | `DAPR-2000--Digital_Audio_Essentials/Mixing_and_Mastering/Sample_vs_True_Peak.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/monitoring-psychoacoustics/monitoring-psychoacoustics-equal-loudness-01.png` | `DAPR-2000--Digital_Audio_Essentials/Monitoring_and_Psychoacoustics/Equal_Loudness.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/monitoring-psychoacoustics/monitoring-psychoacoustics-module-banner-01.png` | `DAPR-2000--Digital_Audio_Essentials/Monitoring_and_Psychoacoustics/Module_Banner.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/monitoring-psychoacoustics/monitoring-psychoacoustics-monitor-triangle-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Monitoring_and_Psychoacoustics/Monitor_Triangle.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/monitoring-psychoacoustics/monitoring-psychoacoustics-sound-field-speaker-placement-01.png` | `DAPR-2000--Digital_Audio_Essentials/Monitoring_and_Psychoacoustics/Sound_Field_Speaker_Placement.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-01-new-tracks-dialog-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_01_New_Tracks_Dialog.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-02-mix-window-sends-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_02_Mix_Window_Sends.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-02-mix-window-track-types-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_02_Mix_Window_Track_Types.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-03-edit-window-track-types-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_03_Edit_Window_Track_Types.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-04-io-setup-output-page-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_04_IO_Setup_Output_Page.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-05-io-setup-input-page-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_05_IO_Setup_Input_Page.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-06-io-setup-bus-page-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_06_IO_Setup_Bus_Page.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-07-window-menu-edit-and-mix-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_07_Window_Menu_Edit_and_Mix.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-08-edit-window-view-selector-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_08_Edit_Window_View_Selector.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-09-edit-modes-shuffle-slip-spot-grid-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_09_Edit_Modes_Shuffle_Slip_Spot_Grid.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-10-edit-toolbar-expanded-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_10_Edit_Toolbar_Expanded.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-11-edit-toolbar-standard-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_11_Edit_Toolbar_Standard.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-12-transport-window-controls-01.png` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_12_Transport_Window_Controls.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-13-record-enabled-audio-track-01.png` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_13_Record_Enabled_Audio_Track.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-dapr2000-protools-15-input-monitoring-playback-example-01.png` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Dapr2000_Protools_15_Input_Monitoring_Playback_Example.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/pro-tools-introduction/pro-tools-introduction-pro-tools-dashboard-1-01.png` | `DAPR-2000--Digital_Audio_Essentials/Pro_Tools_Introduction/Pro_Tools_Dashboard_1.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-compression/processing-compression-attack-release-envelope-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Compression/Attack_Release_Envelope.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-compression/processing-compression-bf-2a-plugin-window-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Compression/Bf_2a_Plugin_Window.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-compression/processing-compression-bf-76-peak-limiter-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Compression/Bf_76_Peak_Limiter.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-compression/processing-compression-compressor-limiter-iii-plugin-window-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Compression/Compressor_Limiter_Iii_Plugin_Window.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-compression/processing-compression-la-2a-leveling-amplifier-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Compression/La_2a_Leveling_Amplifier.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-compression/processing-compression-parallel-routing-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Compression/Parallel_Routing.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-compression/processing-compression-the-anatomy-of-a-compressor-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Compression/The_Anatomy_of_a_Compressor.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-time-based/processing-time-based-d-verb-plugin-window-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Time_Based/D_Verb_Plugin_Window.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-time-based/processing-time-based-mod-delay-iii-plugin-window-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Time_Based/Mod_Delay_Iii_Plugin_Window.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-time-based/processing-time-based-module-banner-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Time_Based/Module_Banner.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-time-based/processing-time-based-pre-delay-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Time_Based/Pre_Delay.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/processing-time-based/processing-time-based-send-vs-insert-01.png` | `DAPR-2000--Digital_Audio_Essentials/Processing__Time_Based/Send_vs_Insert.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/quiz-questions/quiz-questions-pro-tools-pan-and-track-state-quiz-01.png` | `DAPR-2000--Digital_Audio_Essentials/Quiz_Questions/Pro_Tools_Pan_and_Track_State_Quiz.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-adam-audio-monitors-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Adam_Audio_Monitors.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-aes50-network-cable-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Aes50_Network_Cable.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-aes67-network-cable-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Aes67_Network_Cable.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-avb-network-cable-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/AVB_Network_Cable.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-balanced-audio-01.webp` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Balanced_Audio.webp` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-banana-plug-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Banana_Plug.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bedroom-studio-01.webp` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bedroom_Studio.webp` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-binding-post-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Binding_Post.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-50-ohm-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_50_Ohm.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-75-ohm-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_75_Ohm.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-75-ohm-terminator-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_75_Ohm_Terminator.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-aes3id-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_Aes3id.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-barrel-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_Barrel.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-female-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_Female.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-madi-coax-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_Madi_Coax.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-male-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_Male.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-male-male-adapter-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_Male_Male_Adapter.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-tee-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_Tee.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-bnc-word-clock-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Bnc_Word_Clock.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-cat6-cable-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Cat6_Cable.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-connector-size-comparison-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Connector_Size_Comparison.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-dante-network-cable-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Dante_Network_Cable.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-db25-aes-digital-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Db25_AES_Digital.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-db25-analog-vs-aes-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Db25_Analog_vs_AES.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-db25-audio-breakout-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Db25_Audio_Breakout.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-db25-female-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Db25_Female.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-db25-male-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Db25_Male.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-dc-barrel-size-comparison-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/DC_Barrel_Size_Comparison.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-edac-516-male-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Edac_516_Male.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-edac-516-mating-pair-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Edac_516_Mating_Pair.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-eighth-inch-to-quarter-inch-adapter-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Eighth_Inch_to_Quarter_Inch_Adapter.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-eighth-inch-trrs-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Eighth_Inch_Trrs.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-eighth-inch-trs-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Eighth_Inch_Trs.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-eighth-inch-ts-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Eighth_Inch_Ts.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-ethercon-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Ethercon.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-firewire-400-4-pin-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Firewire_400_4_Pin.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-firewire-400-6-pin-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Firewire_400_6_Pin.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-firewire-800-9-pin-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Firewire_800_9_Pin.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-focusrite-scarlett-01.webp` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Focusrite_Scarlett.webp` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-headphones-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Headphones.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-hirose-4-pin-dc-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Hirose_4_Pin_DC.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-home-studio-signal-flow-01.jpeg` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Home_Studio_Signal_Flow.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-iec-c13-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Iec_C13.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-iec-c14-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Iec_C14.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-instrument-vs-speaker-cable-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Instrument_vs_Speaker_Cable.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-laptop-01.webp` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Laptop.webp` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-latching-iec-inlet-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Latching_Iec_Inlet.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-locking-twist-connector-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Locking_Twist_Connector.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-midi-5-pin-din-female-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/MIDI_5_Pin_Din_Female.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-midi-5-pin-din-male-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/MIDI_5_Pin_Din_Male.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-mini-toslink-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Mini_Toslink.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-phone-plug-size-comparison-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Phone_Plug_Size_Comparison.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-quarter-inch-speaker-cable-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Quarter_Inch_Speaker_Cable.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-quarter-inch-to-eighth-inch-adapter-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Quarter_Inch_to_Eighth_Inch_Adapter.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-quarter-inch-trs-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Quarter_Inch_Trs.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-quarter-inch-ts-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Quarter_Inch_Ts.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-quarter-inch-ts-vs-trs-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Quarter_Inch_Ts_vs_Trs.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-rca-analog-audio-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Rca_Analog_Audio.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-rca-analog-vs-spdif-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Rca_Analog_vs_Spdif.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-rca-female-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Rca_Female.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-rca-male-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Rca_Male.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-rca-spdif-75-ohm-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Rca_Spdif_75_Ohm.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-rj45-8p8c-jack-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Rj45_8p8c_Jack.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-rj45-8p8c-plug-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Rj45_8p8c_Plug.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-rj45-vs-ethercon-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Rj45_vs_Ethercon.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-same-connector-different-impedance-bnc-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Same_Connector_Different_Impedance_Bnc.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-same-connector-different-protocol-usbc-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Same_Connector_Different_Protocol_Usbc.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-same-connector-different-signal-rca-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Same_Connector_Different_Signal_Rca.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-same-connector-different-signal-xlr-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Same_Connector_Different_Signal_Xlr.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-speakon-2-pole-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Speakon_2_Pole.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-speakon-4-pole-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Speakon_4_Pole.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-ta3-mini-xlr-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Ta3_Mini_Xlr.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-ta5-mini-xlr-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Ta5_Mini_Xlr.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-tfunk-mic-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Tfunk_Mic.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-thunderbolt-usb-c-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Thunderbolt_USB_C.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-toslink-optical-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Toslink_Optical.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-toslink-vs-mini-toslink-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Toslink_vs_Mini_Toslink.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-tt-bantam-patch-cable-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Tt_Bantam_Patch_Cable.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-tt-bantam-plug-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Tt_Bantam_Plug.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-tt-vs-eighth-inch-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Tt_vs_Eighth_Inch.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-a-male-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_a_Male.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-a-to-usb-c-adapter-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_a_to_USB_C_Adapter.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-a-vs-b-vs-c-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_a_vs_B_vs_C.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-b-male-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_B_Male.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-c-plug-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_C_Plug.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-c-to-hdmi-adapter-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_C_to_Hdmi_Adapter.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-c-to-usb-a-adapter-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_C_to_USB_a_Adapter.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-c-to-usb-b-interface-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_C_to_USB_B_Interface.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-c-vs-thunderbolt-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_C_vs_Thunderbolt.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-micro-b-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_Micro_B.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-mini-b-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_Mini_B.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-usb-vs-firewire-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/USB_vs_Firewire.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-xlr-3-pin-female-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Xlr_3_Pin_Female.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-xlr-3-pin-male-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Xlr_3_Pin_Male.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-xlr-4-pin-male-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Xlr_4_Pin_Male.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-xlr-5-pin-female-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Xlr_5_Pin_Female.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-xlr-5-pin-male-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Xlr_5_Pin_Male.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-xlr-aes3-110-ohm-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Xlr_Aes3_110_Ohm.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-xlr-analog-balanced-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Xlr_Analog_Balanced.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-xlr-analog-vs-aes3-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Xlr_Analog_vs_Aes3.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/signal-flow-cables/signal-flow-cables-xlr-trs-combo-jack-01.png` | `DAPR-2000--Digital_Audio_Essentials/Signal_Flow_and_Cables/Xlr_Trs_Combo_Jack.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-adsr-envelope-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Adsr_Envelope.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-amplitude-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Sine_Wave_with_Wavelength_and_Amplitude.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-amplitude-02.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/High_and_Low_Frequency_Wave_Comparison.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-amplitude-change-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Amplitude_Change.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-audible-range-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Audible_Range.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-chorus-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Chorus.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-clipping-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Clipping.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-clipping-distortion-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Clipping_Distortion.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-fletcher-munson-curve-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Fletcher_Munson_Curve.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-frequency-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Frequency.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-module-banner-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Module_Banner.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-phase-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Phase.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-phase-shift-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Phase_Shift.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-reflection-absorption-diffusion-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Reflection_Absorption_and_Diffusion_Arrow_Panels.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-reflection-absorption-diffusion-02.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Threshold_Labeled_Loudness_Contour_Curves.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-hearing-frequency/sound-hearing-frequency-waveform-basics-01.jpeg` | `DAPR-2000--Digital_Audio_Essentials/Sound__Hearing_Frequency/Waveform_Basics.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-decibel/sound-the-decibel-krakatoa-header-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Decibel/Krakatoa_Header.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-decibel/sound-the-decibel-reference-ladder-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Decibel/Reference_Ladder.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-decibel/sound-the-decibel-series-parallel-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Decibel/Series_Parallel.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-decibel/sound-the-decibel-the-decibel-01.jpeg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Decibel/The_Decibel.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-decibel/sound-the-decibel-the-uberschall-dream-meets-real-world-math-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Decibel/The_Uberschall_Dream_Meets_Real_World_Math.png` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-adiabatic-vs-isothermal-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Adiabatic_vs_Isothermal.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-altitude-speed-constant-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Altitude_Speed_Constant.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-collision-relay-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Collision_Relay.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-delay-tower-drift-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Delay_Tower_Drift.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-gamma-degrees-of-freedom-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Gamma_Degrees_of_Freedom.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-gamma-piston-vs-box-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Gamma_Piston_vs_Box.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-impedance-coupling-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Impedance_Coupling.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-kelvin-ladder-phases-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Kelvin_Ladder_Phases.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-nondispersive-arrival-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Nondispersive_Arrival.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-sofar-channel-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Sofar_Channel.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-sofar-channel-01.svg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Sofar_Channel.svg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-speed-across-media-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Speed_Across_Media.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-speed-across-media-01.svg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Speed_Across_Media.svg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-speed-vs-temperature-curve-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Speed_vs_Temperature_Curve.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-stiffness-vs-density-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Stiffness_vs_Density.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-temperature-molecular-speed-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Temperature_Molecular_Speed.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-temperature-refraction-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Temperature_Refraction.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-wavelength-ruler-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Wavelength_Ruler.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-diagram-wind-refraction-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Diagram_Wind_Refraction.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-photo-cold-winter-load-in-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Photo_Cold_Winter_Load_in.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-photo-dead-sea-shore-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Photo_Dead_Sea_Shore.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-photo-delay-tower-field-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Photo_Delay_Tower_Field.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-photo-hero-utah-valley-dawn-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Photo_Hero_Utah_Valley_Dawn.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-photo-high-altitude-summit-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Photo_High_Altitude_Summit.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-photo-outdoor-stage-dusk-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Photo_Outdoor_Stage_Dusk.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-photo-steel-structure-detail-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Photo_Steel_Structure_Detail.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-the-speed-of-sound/sound-the-speed-of-sound-photo-underwater-light-shafts-01.jpg` | `DAPR-2000--Digital_Audio_Essentials/Sound__The_Speed_of_Sound/Photo_Underwater_Light_Shafts.jpg` |
| `DAPR-2000--Digital_Audio_Essentials/Images/sound-wave-properties/sound-wave-properties-anatomy-01.png` | `DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties/Anatomy.png` |

## 5. Cloudflare download renames

**5 files.** Base URL: `https://uvu-files.adamo.workers.dev/`

| Old path | New path | Module |
|---|---|---|
| `DAPR-2000--Digital_Audio_Essentials/daw-first-mix/six-of-one-assets.zip` | `DAPR-2000--Digital_Audio_Essentials/Project__Mix_1A-Six_of_One/Six_of_One_Assets.zip` | Project: Mix 1A - Six of One; Sound: The Decibel |
| `DAPR-2000--Digital_Audio_Essentials/microphones-characteristics/essentails-piano-02.wav` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics/Piano-Coincident_Pair.m4a` | Microphones: Characteristics |
| `DAPR-2000--Digital_Audio_Essentials/microphones-characteristics/essentails-piano-plusgtr-01.wav` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics/Guitar_Not_Mono_Compatible.m4a` | Microphones: Characteristics |
| `DAPR-2000--Digital_Audio_Essentials/microphones-characteristics/essentails-piano-plusgtr-02.wav` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics/Guitar_Not_Mono_Compatible.m4a` | Microphones: Characteristics (exact duplicate of plusgtr-01, merged) |
| `DAPR-2000--Digital_Audio_Essentials/microphones-characteristics/essentails-piano-plusgtr-03.wav` | `DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics/Piano_and_Guitar-Stereo_Spaced_Pair.m4a` | Microphones: Characteristics |

## 6. Unresolved

- `DAPR-2000--Digital_Audio_Essentials/microphones-characteristics/essentails-piano-01.wav` has **no current file**. Its SHA-256 (`bc4188f0…`) matches none of the three audio files now in `Microphones__Characteristics/`. The original is still in the `CloudFlare copy` backup folder. It needs a name and a decision before it comes back, or a decision that it stays gone.
- `essentails-piano-plusgtr-01.wav` and `essentails-piano-plusgtr-02.wav` were byte identical (SHA-256 `9c4927a8…`). They are now one file, `Guitar_Not_Mono_Compatible.m4a`. Any page that linked to `-02` must point at that single file.
- All five of these were named `.wav` but were actually M4A files, which is why Canvas showed "Your browser cannot play this file." The extensions are now correct.

## 7. Reference rewrite status

Every reference inside the `Classes/` tree of this repo has been rewritten to the new paths. What has **not** been rewritten:

- The Canvas cartridge for this course. That is the job this file exists for.
- Live Canvas pages. They only change when the rebuilt cartridge is imported.
- Files under `_briefs/` and `_superseded/`. Those are historical working notes and were left alone on purpose.
- `DAPR-2000--Digital_Audio_Essentials--Image-Reference.html` at the course root, if one exists. It is a generated sheet and should be regenerated rather than patched.

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
