# Image Fixes For Later: DAPR All Courses

Parked 2026-09-23 so the course builds can move. Nothing here blocks a rebuild; the current files work, they are just weaker than they should be. Paths are under:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/
```

## Claude can finish these (just say go)

| File | What is wrong | Plan |
|---|---|---|
| `DAPR-3255--Audio_Hardware_II/Electronics/Rendered_Triangles_With_Banded_Resistors.png` and `..._Tan_Resistors.png` | Ground resistor drawn on top of the input wire | Redraw both op amp circuits cleanly (Image 21 in the ChatGPT file also covers it) |
| `DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/DMX_Universe_Addressing.png` | Caption says ranges overlap; none do in the drawing | Redraw with two overlapping fixture ranges |
| `DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/TRS_MIDI_Cables_3.5mm.jpg` | Nothing shows Type A vs Type B | Draw a Type A vs Type B wiring diagram |
| `DAPR-2255--Audio_Hardware_I/Schematics/Logic_Gates.png` | OR, NOR, XOR, XNOR input leads stop short | Touch up the leads |
| `DAPR-3255--Audio_Hardware_II/Final_Exam/Schematic_Symbols.png` and `Transformer_Symbols.jpg` | Low resolution, labels unreadable | Rebuild from SparkFun open symbols (CC BY-SA 4.0) |
| `DAPR-3340--Spatial_Audio_I/Surround_Monitoring/Speaker_Placement.jpg`, `Theatrical_Listening_Environment.jpg` | Small third party figures, notes unreadable | Redraw as clean diagrams |
| `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround_and_Multichannel_Audio/Analog_Digital_Delivery_Evolution.png` | 639 px wide, text too small | Rebuild at 1600 wide |
| `DAPR-2020--Core_Mixing/Effects__Spectral_Effects_and_EQ/Vocal_EQ_Frequency_Band_Chart.jpg` | Washed out third party chart | Rebuild as a clean chart |
| Denon AVR-5803 rear photo (held, not placed) | Serial number visible | Blur the serial before any page uses it |
| `DAPR-2020--Core_Mixing/Effects__Dynamic_Effects/Compression_Switch.png` | Five numbered callouts with no legend, so the numbers mean nothing. Purple and cyan, off the section 3 palette. The picture is a side-chain trigger, not a compression switch, so the filename and the folder are both wrong | Redraw on palette with a legend, rename to what it shows, and move it to `Effects__Frequency_Dynamics_and_Side-Chains/` |
| `DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Please_Complete_Your_Course_Evaluations.png` | Another student's name is readable in the second browser tab. Section 4 rule 4 says blur other people's names | Blur the tab title, then it can go on the Course Evaluations page beside the other two screenshots |
| `DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Course_Outline_Banner_Alt.png` | Square at 1024 by 1024, so it crops badly wherever a banner is wide. The wide `Course_Outline.png` is the one in use | Re-render wide, or retire it |
| `DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Dark_Purple_Course_Title_Card.jpg` | Reads "Course Outline & Industry Roadmap", which is a different artifact from this course's outline. 655 by 550 | Re-render with the right words, or retire it |

## Needs Adam (photo, screenshot, or a decision)

| File | What to do |
|---|---|
| `DAPR-3255--Audio_Hardware_II/Electronics/Talkback_Box_Assembled.jpg` | Phone photo of a finished talkback box (current file is a hand and a cable) |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Time_Machine_Restore.jpg` | Real screenshot (current is a phone photo of a screen) |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Screenshot_Options_Menu_over_System_Settings.jpg` | Real screenshot |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Terminal_Pwd_Ls_Cd.png` | Narrow Terminal window running pwd, ls, cd |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Function_Keys_Panel.png` | System Settings, Keyboard, Function Keys |
| `DAPR-2010--Core_Recording/Studio_Use_and_Care/Studio_Floor_Plan.png` | Send room names and rough layout; Claude draws it |
| `DAPR-2010--Core_Recording/Studio_Use_and_Care/Power_Up_Sequence_Alt.png` | Decide which power up order is right (it disagrees with Power_Up_Sequence.png) |
| `DAPR-2000--Digital_Audio_Essentials/Monitoring__Psychoacoustics/Sound_Field_Speaker_Placement.png` | Re-export larger from its source |
| `DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics_Selection_and_Stereo_Techniques/Channel_Strip_with_Centered_Pan_Knobs.png` | Sharper recapture: the current file is 81 px wide. Pro Tools Mix window, one stereo channel strip with both pan knobs centered, captured at Retina resolution, same name. Its twin `Channel_Strip_with_Hard_Panned_Knobs.png` (also used as `DAW__Your_First_Mix/Pro_Tools_Hard_Panned_Channel.png`) is the same width, so capture both states in one sitting |
| `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Inductor.png` | Re-export the full strip from its source |
| `All/DAPR_Introduce_Yourself/Example_Headshot.jpg` | Confirm consent or AI origin, or swap in your own |
| `DAPR-3345--Spatial_Audio_II/Interactive_Audio__Foundations_of_Interactive_Spatial_Audio/Workstation_Banner.jpg` and `_Alt` | Made up DAW screens; replace with real FMOD or Wwise captures when you have them |
| `DAPR-2255--Audio_Hardware_I/Power/Wattmeter.jpg` | Optional: page link for the plug in meter photo, for the credit line |
| `DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Core_Recording_DAPR_2010_002.png` | A DAPR 2010 title card sitting in the DAPR 2020 folder. Moving it is on the v31 approval table; say yes there and it goes to `DAPR-2010--Core_Recording/Course_Orientation/` |

| `DAPR-2010--Core_Recording/Studio_Use_and_Care/Control_Room.png` | Photo of the Studio B control room in its resting state, as a session should find it |
| `DAPR-2010--Core_Recording/Studio_Use_and_Care/Live_Room.png` | Photo of the Studio B live room at the end of a session: stands down, cables hung, nothing on the floor |
| `DAPR-2010--Core_Recording/Microphones/Mic_Locker.png` | Photo of the mic locker with the cabinet open |
| `DAPR-2010--Core_Recording/Console_Operation/Cue_Station.png` | Photo of a headphone cue station as a performer sees it |
| `DAPR-2010--Core_Recording/Patch_Bays/Studio_B_Bay_Installed.png` | Photo of the Studio B patch bay installed in the rack, close enough to read the labels |
| `DAPR-2010--Core_Recording/Pro_Tools_for_Tracking/Course_Template_Session.png` | Screenshot of the course Pro Tools template session open, Edit window |
| `All/DAPR_Canvas_Icon_Reference/Instructor.png` | Instructor portrait or avatar for the orientation page |

Added 2026-09-24 during the DAPR 2010 v20 build. Seven placeholders the cartridge references and no file exists for. All are dropped cleanly, so nothing renders broken; each page simply carries one fewer figure until the photograph arrives.

Added 2026-09-23 during the DAPR 2020 v31 build, under section 4 rule 3 of Decisions Already Made: keep the weak image, log it, do not stop the build.


## DAPR 3340 figures whose file no longer exists (found 2026-09-23 during the v50 rebuild)

Ten pages carry an `<img>` whose GitHub URL returns 404. The original files are not in the
repo under any name, including `_unused` and every `Archive`. The prose around each one says
"see Figure N", so the page reads wrong without it. None of these blocks the v50 import; the
course imports unpublished.

| Page | Missing file | Old alt text, which names the original | Proposed fix |
|---|---|---|---|
| `ambisonics-basics` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonics_Basics.png` | `Fig06_01-AmbisonicsLogo.png` | Point at `Ambisonic_Logo.png`, already in that folder and clearly the same picture |
| `working-with-binaural-in-pro-tools` | `Ambisonics_and_Binaural/Channel_Strip_With_Binaural_Insert.png` | `Fig06_20a-Select-IRCAMHEAR-StereoOut.png` | Point at `Binaural_Renderer_Channel_Strip.png`, already in that folder |
| `exercise-ambisonics-and-binaural-post` | `Ambisonics_and_Binaural/Exercise_Post.png` | `2024-08-23_11-12-38.png` | Recapture: the Quad clip in the Pro Tools clip list |
| `multichannel-formats-emerge` | `Introduction_to_Surround_and_Multichannel_Audio/Star_Wars_Dolby_Stereo.png` | `Historical Star Wars and Dolby Stereo image` | Source a licensable 1977 Dolby Stereo print image, or drop the figure and keep the prose |
| `exercise-surround-mastering-music` | `Surround_Mastering_and_Surround_Encoding/Exercise_Music.png` | `Fig5.31-ImportAudioDialog.png` | Recapture: the Import Audio dialog with Copy showing |
| `exercise-surround-mastering-post` | `Surround_Mastering_and_Surround_Encoding/Pro_Limiter_Plugin_Window.png` | `2024-08-21_12-45-57.png` | Recapture, or point at `Surround_Limiter_Plugin_Window.jpg` in that folder if it shows the ceiling at zero |
| `exercise-surround-mixing-and-surround-plugins-music` | `Surround_Mixing_and_Surround_Plugins/Exercise_Music.jpg` | `4-X Automation-cropped.jpg` | Recapture: a track header with automation lanes shown |
| `room-design-and-acoustics` | `Surround_Monitoring/Room_Design_and_Acoustics.png` | `image.png` | Recapture or redraw: the room treatment tool the paragraph describes |
| `introduction-to-surround-recording` | `Surround_Recording/Introduction_to_Surround_Recording.png` | `Spacial Impression.png` | Redraw: localization against envelopment, the two ideas the paragraph sets up |
| `using-surround-microphones` | `Surround_Recording/Using_Surround_Microphones.gif` | `Ambisonics.gif` | Redraw as a still: decoding to an arbitrary speaker layout. It was an animated GIF; a labelled diagram carries the same point |

Separately, 34 URLs in the DAPR 3340 cartridge pointed at real files under the wrong spelling
(`Dts_Neo_6` for `DTS_Neo_6`, `bounce-mix.jpg` for `Bounce_Mix.jpg`, `.png` where the file is
`.jpg`). Those were corrected in the cartridge in v50. macOS hid them because it is case
insensitive; raw.githubusercontent.com is not.


## DAPR 3340 placeholder images placed to satisfy rule 2 (2026-09-24, v51)

Rule 2 of Decisions Already Made says every student visible page carries a real image and
no page ships bare. Twenty eight DAPR 3340 pages had none. Each now carries a real file
already live in the repo. Twenty one of them are a genuine fit for the page. The seven
below are honest placeholders: they satisfy the rule and read acceptably, but the page
deserves a picture of its own subject.

| Page | Placeholder now on it | What the page actually wants |
|---|---|---|
| `Orientation: Prerequisites` | `Course_Orientation/Campus_Waterfall_Behind_Concrete_Beams.jpg` | A shot of the lab or a Pro Tools splash, something about getting set up |
| `Course Policies and Expectations` | same campus photo | The point-to-time scale drawn as a chart, which the page already describes in prose |
| `Instructor Information and Office Hours` | same campus photo | A photo of Adam, or of the office door and its hours card |
| `Auxiliary Resources` | same campus photo | A frame from the UVU Symphony session, or the session opened in Pro Tools |
| `Roll Call Attendance` | same campus photo | Nothing pressing. It is an LTI stub students rarely open |
| `Instructor: v35 Punch List` | `Final_Project_and_Final_Exam/Course_Concept_Map.png` | Instructor only, so low priority |
| `Course Development Task List` | `Final_Project_and_Final_Exam/Course_Concept_Map.png` | Instructor only, so low priority |

### Cross-module image references in DAPR 3340 v51

Section 8.0.1 prefers a module-local copy over a cross-module URL. Seven pages now point at
an image sitting in another module's folder, because the right picture already existed there
and copying files into the repo is Adam's call, not the build's. Each one works today. To
close them, copy the file into the page's own module folder under the same name and repoint
the page.

| Page, and the module it is in | Image it points at |
|---|---|
| `Assignment - Pro Tools Routing 1`, Introduction to Surround | `Surround_Mixing_and_Surround_Plugins/Color_Coded_Input_Output_and_Bus_Paths.png` |
| `Assignment - Pro Tools Routing 2`, Introduction to Surround | `Surround_Mixing_and_Surround_Plugins/Aux_Input_Strip_Annotated.png` |
| `Signal Routing: I/O Setup for Surround`, Introduction to Surround | `Surround_Mixing_and_Surround_Plugins/Bus_Tab_Listing_Surround_Busses.png` |
| `Signal Routing: Multichannel Track Assignments`, Introduction to Surround | `Surround_Mixing_and_Surround_Plugins/Track_Assignment_Context_Menu.jpg` |
| `Course Description, Learning Outcomes, and Requirements`, Course Orientation | `Final_Project_and_Final_Exam/Course_Concept_Map.png` |
| `Syllabus`, Course Orientation | `Final_Project_and_Final_Exam/Course_Concept_Map.png` |
| `Auxiliary Resources`, Auxiliary Resources | `Course_Orientation/Campus_Waterfall_Behind_Concrete_Beams.jpg` |

`Classes/DAPR-3340--Spatial_Audio_I/Auxiliary_Resources/` is empty in the repo. It holds no
images yet, only the Cloudflare download on the other side.

## DAPR 2000 - Digital Audio Essentials, logged 2026-09-24 (v63)

**Resolved in v65 (2026-09-24).** The seven Edit tool screenshots were never missing: the originals were in `apps/GitHub copy/Canvas/.../Images/daw-eq-dynamics/`. Copied, not moved, to `DAW__EQ_and_Dynamics/Edit_Tools_Smart_Tool.png` through `Edit_Tools_Pencil.png` and relinked. The sound supplemental page alt texts were never offset; the v61 filenames were mislabeled. All seven slots now carry the byte identical originals (Phase_Offset.png twice, on purpose), and the stereo mic techniques Center Panned slot carries `Channel_Strip_with_Centered_Pan_Knobs.png`.

**Over the size cap.** `Sound__Wave_Properties_Hearing_and_Frequency/Time_Domain_vs_Frequency_Domain.png` is 1,054,804 bytes at 4010 x 2189, just over the 1 MB PNG cap. Claude can re-export it at 1600 wide under the same name; needs a yes because it replaces the file.

**Placeholder or loose-fit images placed to satisfy the image-on-every-page rule.** Each works, none is ideal:

| Page | Image used | Why it is a placeholder |
|---|---|---|
| roll-call-attendance.html | Course_Orientation/Course_Card.png | An attendance page has no topical image of its own |
| ws-signal-flow.html | Signal_Flow__Cables_and_Connections/MIDI_5_Pin_DIN_Pin_Layout.png | A general cable overview would suit a worksheet better than one connector pinout |
| m04-p2-daw-mix-1-six-of-one.html | Project__Mix_2_-_Six_of_One_Revision/Mix_Arc.png | Mix 1A has no image folder, so this reaches into the Mix 2 folder |
| m08-mix-peer-review-submission-six-of-one.html | Project__Mix_2_-_Six_of_One_Revision/Mix_Arc.png | Mix 1B has no image folder, same reach |
| sound-introducing-the-digital-audio-workstation-daw.html | DAW__EQ_and_Dynamics/Pro_Tools_Blank_Edit_Window.png | The DAW screenshots live in the EQ and Dynamics folder, not in Sound: The Decibel |
| sound-watch-more-db-videos-if-you-wish.html | Sound__The_Decibel/Decibel_Log_Scale.jpg | Reused, the decibel module has only one spare image |

**Unreferenced images worth a look.** `Sound__Wave_Properties_Hearing_and_Frequency/` holds 32 images nothing references, including 19 `Diagram_*` files and 8 `Photo_*` files. One of them is a Dropbox conflicted copy: `Photo_Hero_Utah_Valley_Dawn (Adam Olson's conflicted copy 2026-09-23).jpg`.

---

## DAPR 3255 Audio Hardware II, pages with no real image (2026-09-24, from v10)

Seventeen student visible pages ship bare. Nothing in the course folder fits any of them, so
none has a placeholder yet. Grouped by what would actually fix it.

### Course Orientation, 8 pages
`Course_Orientation/` is empty on both hosts for this course, and Standards 8.0.1 says that
folder holds images only, never decks or handouts. These eight need one banner each, or one
shared orientation banner copied into the folder.

| Page | What would fit |
|---|---|
| MOO: a) Prerequisites | A banner, or a simple prerequisite chain graphic (DAPR 2250 to 2255 to 3255) |
| MOO: b) Course Description, Learning Outcomes, and Requirements | A banner |
| MOO: c) Universal Class Policies and Expectations | A banner |
| MOO: d) Instructor Information and Office Hours | A photo of Adam, or the studio door |
| MOO: b) Canvas Student Orientation | A captured Canvas dashboard screenshot |
| MOO: c) Update Profile and Notifications | A captured Canvas notification settings screenshot |
| MOO: a) Resources and Links | A banner |
| MOO: c) How to Make a PDF | A captured macOS print dialog showing Save as PDF |

The four captures are real software screens, so per rule 4.2 they must be captured, never
generated. Adam is the only one who can take them.

### Networking: Foundations of Audio Networking, 4 pages
All four rescued renders for this module are already placed on other pages.

| Page | What would fit |
|---|---|
| Networking: Layer 1: Point-to-Point Protocols | Two endpoints joined by one cable, no switch |
| Networking: Layer 5: Session, Presentation, and Application | The top three layers of the stack lit, the lower four dim |
| Networking: Layer 6 Presentation | The same frame encoded two ways, one readable |
| Networking: Layer 7 Application | An application icon row sitting on top of the stack |

### Software Tools, 4 pages
`Software_Tools/` is empty on both hosts. Every page here is about a real software product, so
every image must be a capture, not a render.

| Page | What would fit |
|---|---|
| Software: Dante Controller and the Dante Essentials | A Dante Controller routing grid capture |
| Software: Wireless System Management | A Shure Wireless Workbench or Sennheiser WSM capture |
| Software: Network Capture and Analysis | A Wireshark capture window with an audio filter applied |
| Software: DSP and System Configuration Platforms | A Q-SYS Designer or Symetrix Composer capture |

### Wireless Systems, 1 page
| Page | What would fit |
|---|---|
| Wireless: RF Spectrum Fundamentals | A spectrum plot with the UHF TV band and the usable gaps marked |

## DAPR 2020 pages carrying a stand-in image (rule 2, added 2026-09-24)

Rule 2 says every student visible page carries a real image, and to log the ones where nothing purpose-made existed yet. All 45 pages below now carry a real image from their own module folder. These are the ones where the same image had to cover more than one page, so a purpose-made figure would be better.

| Image | Pages it now covers | Module short of figures |
|---|---|---|
| `Five_Pass_Mix_Order.png` | 4 | Mixing__In-Class_Mixing |
| | in-class-mix-01.html, in-class-mixing-common-mistakes-and-how-to-hear-them.html, in-class-mixing-repeatable-workflow-guide.html, mixing-in-class-mixing-overview.html | |
| `PT_Identify_Beat_Bar_Beat_Markers.jpg` | 3 | Pro_Tools__Fundamentals |
| | pro-tools-lab-pro-tools-assignment.html, pro-tools-fundamentals-course-learning-outcomes.html, pro-tools-fundamentals-prerequisites.html | |
| `Gain_Staging_Chain.png` | 2 | Mixing__Essential_Groundwork |
| | essential-groundwork-lab.html, mix-prep-assignment.html | |
| `Professional_Practice_Bounce_Specification.png` | 2 | Final__Final_Mix_and_Final_Exam |
| | final-mix-a-horse-is-not-a-home-2.html, final-mix-and-final-exam-study-guide.html | |
| `Core_Mixing_Lab_DAPR_2020L.png` | 2 | Professional_Practice__Presentations_and_Sessions |
| | presentations-mixing-topic-presentation-10-minutes.html, professional-practice-presentations-sessions-overview.html | |

---

## DAPR 3345 Spatial Audio II, placeholders from the v10 build (2026-09-24)

Standards 0 now requires a real image on every student visible page. DAPR 3345 had 79 pages with no
image and 37 image files, so 50 pages carry an image reused from elsewhere in the same section. Each one
is honest about what it shows and none of them is wrong, but none of them is about that page either.
They are listed by the file doing the work, heaviest first.

| Image doing placeholder duty | Pages carrying it | What those pages actually need |
|---|---|---|
| `Atmos_Room_Banner.jpg` | 12: dolby-certification-atmos-essentials, dolby-certification-content-creation-for-games, dolby-certification-course-links, dolby-certification-mix-room-design-and-dardt-bonus and more | A Dolby Learning Portal screen capture, and a certificate example |
| `Implementation_Desk_Banner.jpg` | 5: fmod-assignment-1-setup-and-training, fmod-assignment-3-project-a-parameter-design, fmod-assignment-5-video-proof-and-written-reflection, fmod-buses-snapshots-and-the-mixer and more | Real FMOD Studio captures: event editor, mixer, bank build |
| `Distance_Minimum_and_Maximum.jpg` | 3: fmod-assignment-4-project-b-your-choice, fmod-banks-building-and-engine-integration, fmod-parameters-and-real-time-control | FMOD parameter and bank captures |
| `Angled_Stage_View_with_Boom_Array.jpg` | 3: orchestral-recording-1-2-stereo-mix, orchestral-recording-1-4-reflection, spatial-recording-from-multitrack-to-beds-and-objects | Session captures from the February recording: track layout, bed and object routing |
| `Middleware_Desk_Banner.jpg` | 3: wwise-assignment-1-fundamentals-101, wwise-professional-submission-standards-for-assignments, wwise-the-project-hierarchy | Real Wwise Authoring captures: project hierarchy, events, SoundBanks, profiler |
| `Listener_Placement.jpg` | 2: implementation-assignment-audio-scripting, implementation-section-overview | An engine editor capture showing the listener component |
| `Rooms_and_Portals.jpg` | 2: orchestral-recording-1-3-spatial-mix, wwise-assignment-2-interactive-music-201-bonus | Wwise interactive music and optimization captures |
| `Team_Room_Banner.jpg` | 2: asset-pipeline-asset-tracking-and-task-tracking, asset-pipeline-source-control-for-audio | A real repository view and a task board capture |
| `Team_Room_Banner_Alt.jpg` | 2: asset-pipeline-git-and-git-lfs-in-practice, asset-pipeline-working-on-a-shared-repository | A real repository view and a task board capture |
| `Crowded_Scene_Banner.jpg` | 2: implementation-debugging-and-remote-profiling, voice-budget-writing-a-prioritization-plan | A profiler capture of a busy scene showing the voice count |
| `Controller_Position_Banner.jpg` | 2: interactive-mix-bus-structure-and-submixing, interactive-mix-loudness-and-platform-delivery | Middleware mixer and snapshot captures, and a loudness meter reading |
| `Virtual_Voices_Alt.jpg` | 2: interactive-mix-ducking-and-dynamic-range, voice-budget-memory-streaming-and-prefetch | A memory and streaming view from a real profiler |
| `Study_Guide_Banner_Alt.jpg` | 1: final-project-proposal-and-scope | A milestone or scope diagram for the final project |
| `Crowded_Scene_Banner_Alt.jpg` | 1: voice-budget-assignment-voice-budget-audit-and-priority-plan | A profiler capture of a busy scene showing the voice count |
| `Rooms_and_Portals_Alt.jpg` | 1: wwise-assignment-3-performance-optimization-251-bonus | Wwise interactive music and optimization captures |
| `Study_Guide_Banner.jpg` | 1: final-project-scope-milestones-and-deliverables | A milestone or scope diagram for the final project |
| `Listener_Placement_Alt.jpg` | 1: implementation-basic-scripting-for-audio | A script or code capture driving audio from gameplay |
| `Emitter_Trigger_Zone_Alt.jpg` | 1: implementation-the-engine-editor-for-audio-people | An engine editor capture of the audio tools panel |
| `Controller_Position_Banner_Alt.jpg` | 1: interactive-mix-snapshots-states-and-mix-changes | A figure for that page topic |
| `Workstation_Banner.jpg` | 1: orientation-3d-software-and-hardware-setup | A real DAW and game engine side by side. This file fabricates both screens and breaks 20.1 rule 3 |
| `Randomization_Dimensions_Banner.jpg` | 1: variation-how-much-variation-is-enough | A variation settings capture with ranges visible |
| `Layered_Recombination_Alt.jpg` | 1: variation-sample-start-point-randomization | A sample start point randomization control, captured |

**One file in that table is not just weak, it is non compliant.** `Interactive_Audio__Foundations_of_Interactive_Spatial_Audio/Workstation_Banner.jpg` and its `_Alt` show a fabricated DAW timeline and a fabricated engine viewport, which Standards 20.1 rule 3 forbids. Adam asked on 2026-09-24 to keep them until a real capture exists. They are on the course overview, the orientation setup page and the syllabus.

The four captures that would clear most of this table: FMOD Studio, Wwise Authoring, the engine editor, and one photograph of a DAW and an engine running side by side.

### Needs Adam: the conflicted copy has no twin, DAPR 2000

`Sound__Wave_Properties_Hearing_and_Frequency/Photo_Hero_Utah_Valley_Dawn (Adam Olson's conflicted copy 2026-09-23).jpg`, 296,220 bytes, SHA-256 starting `1cf40617be707f83`.

There is no `Photo_Hero_Utah_Valley_Dawn.jpg` beside it, and no other copy anywhere under `Classes/`. It is the only version of that photo, so it must not go to `_unused`. It is also the only conflicted copy left in the whole repo. Nothing references it.

Proposed, needs a yes: rename in place to `Photo_Hero_Utah_Valley_Dawn.jpg`, dropping the conflicted-copy suffix. No move, no delete.

## DAPR 3255 Audio Hardware II, v11 update (2026-09-24)

The seventeen bare pages listed above are closed in v11. Eight of them (the MOO pages) left
the cartridge: six are Student Essentials that live in the Unified Class Content module, and
the other two became Orientation: Prerequisites and Orientation: Course Description, Learning
Outcomes, and Requirements. Every student visible page now has an image. None is a
placeholder, so nothing waits on ChatGPT for this course.

| Page | Image now on it |
|---|---|
| Orientation: Prerequisites | `Course_Orientation/Course_Sequence_Prerequisites.png`, drawn in code |
| Orientation: Course Description, Learning Outcomes, and Requirements | `Course_Orientation/Points_By_Course_Area.png`, drawn in code |
| Orientation: Schedule & Module Outline | `Course_Orientation/Term_Schedule_Gantt.png`, drawn in code |
| Syllabus, Roll Call Attendance | `Course_Orientation/Grade_Weighting.png`, drawn in code |
| Networking: Layer 1: Point-to-Point Protocols | `Networking__Foundations_of_Audio_Networking/Layer_1_Point_to_Point_vs_Switched.png`, drawn in code |
| Networking: Layer 5, Layer 6, Layer 7 pages | `Networking__Foundations_of_Audio_Networking/OSI_Stack_*.png`, three stacks drawn in code |
| Networking: Assignment - Terminate a Working Network Cable | `Networking__Foundations_of_Audio_Networking/T568a_T568b_Pin_Order.png`, existing, pin order checked |
| The four Software Tools pages | `Software_Tools/*.png`, four diagrams drawn in code |
| Wireless: RF Spectrum Fundamentals | `Wireless_Systems/Wireless_Audio_Bands.png`, drawn in code |

Still worth doing later: a real Dante Controller routing grid capture and a real Wireshark
capture would beat the drawn diagrams on the Software Tools pages. Both are real software
screens, so Adam captures them; they are never generated.
