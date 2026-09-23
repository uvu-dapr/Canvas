# DAPR-3340--Spatial_Audio_I — Rename Handoff

**Date:** 2026-09-22  
**Course folder:** `DAPR-3340--Spatial_Audio_I`  
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

**427 files.** Base URL: `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/`

| Old path | New path |
|---|---|
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-ambisonics-versus-binaural-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonics_Ambisonics_versus_Binaural.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-ambix-versus-fuma-channel-order-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonics_Ambix_versus_Fuma_Channel_Order.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-and-binaural-audio-360-control-and-spatialiser-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Audio_360_Control_and_Spatialiser.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-and-binaural-exercise-music-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonic_Strings_Clip_Track_List.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-and-binaural-exercise-music-02.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Spot_Dialog_With_Timecode_Fields.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-and-binaural-exercise-music-03.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonic_Input_Format_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-and-binaural-exercise-post-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Exercise_Post.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-and-binaural-pt-atmos-binaural-mode-menu-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Pt_Atmos_Binaural_Mode_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-and-binaural-pt-immersive-panner-lcr-object-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Pt_Immersive_Panner_Lcr_Object.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-and-binaural-pt-immersive-panner-mpegh-speaker-layout-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Pt_Immersive_Panner_Mpegh_Speaker_Layout.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-and-binaural-render-mode-near-mid-far-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Render_Mode_Near_Mid_Far.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-basics-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonics_Basics.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-nine-zero-four-speaker-layout-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonics_Nine_Zero_Four_Speaker_Layout.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-paths-in-i-slash-o-setup-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/New_Path_Format_Menu_With_Ambisonics.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/ambisonics-paths-in-i-slash-o-setup-02.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonic_Bus_Rows_in_Bus_Tab.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/binaural-basics-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Dummy_Head_Binaural_Microphone.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/binaural-basics-02.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/In_Ear_Binaural_Microphone_Photo.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/binaural-basics-03.jpg` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Hexagon_Grid_Speaker_Layout_Editor.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/binaural-basics-04.jpg` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/AirPods_and_iPhone_Spatial_Audio_Setup.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/decoding-ambisonics-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/SoundField_Decoder_Plugin_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/decoding-ambisonics-02.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonic_Decoder_Plugin_Insert_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/decoding-ambisonics-03.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonic_Track_Strip_Routed_to_Bus.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/decoding-ambisonics-04.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonic_Input_Format_Dropdown_Open.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/importing-ambisonics-files-in-pro-tools-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Clips_List_With_Ambisonic_Files.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/importing-ambisonics-files-in-pro-tools-02.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/B_Format_Clips_List_Expanded.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/importing-ambisonics-files-in-pro-tools-03.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Clip_List_of_Ambisonic_Component_Channels.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/importing-ambisonics-files-in-pro-tools-04.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonic_and_Quad_Tracks_With_Waveforms.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/recording-ambisonics-01.jpeg` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Recording_Ambisonics.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/recording-ambisonics-02.jpg` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Tetrahedral_Ambisonic_Microphone_Capsules.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/recording-ambisonics-03.jpg` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Handheld_Ambisonic_Recorder_Photo.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/working-with-binaural-in-pro-tools-01.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Binaural_Encoder_Plugin_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/working-with-binaural-in-pro-tools-02.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Sound_Field_Plugin_Menu_Showing_HEar.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/working-with-binaural-in-pro-tools-03.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Channel_Strip_With_Binaural_Insert.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/working-with-binaural-in-pro-tools-04.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Binaural_Renderer_Channel_Strip.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/working-with-binaural-in-pro-tools-05.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Routing_Matrix_Grid_Close_Up.png` |
| `DAPR-3340--Spatial_Audio_I/Images/ambisonics-and-binaural/working-with-binaural-in-pro-tools-06.png` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Channel_Order_Matrix_and_Format_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/boaa-lab-path-selector-search-bus-01.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Path_Selector_Search_Bus.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/boaa-lab-room-layout-01.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Room_Layout.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/boaa-lab-send-assign-menu-bus-or-track-01.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Send_Assign_Menu_Bus_or_Track.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-02-understanding-output-paths-and-monitoring-01.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Annotated_Audio_Interface_Front_Panel.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-02-understanding-output-paths-and-monitoring-02.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Interface_and_Headphone_Amp_Routing_Diagram.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-01.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Mac_Desktop_With_Dock_and_Notification.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-02.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Pro_Tools_Splash_With_Microphone_Alert.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-03.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Microphone_Access_Alert_at_Startup.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-04.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Microphone_Access_Permission_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-05.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Local_Network_Permission_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-06.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Prompt_to_Select_Playback_Engine_Device.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-07.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Playback_Engine_Set_to_Aggregate_I-O.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-08.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Playback_Engine_Device_List.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-09.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Playback_Engine_Set_to_Volt_Interface.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-10.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Avid_Diagnostic_Data_Consent_Prompt.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-11.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Session_Dashboard_With_Welcome_Popup.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-12.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/New_Session_Dashboard_Settings.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-13.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Dashboard_New_Session_Location_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-14.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Dashboard_New_Session_Configuration_Panel.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-15.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Dashboard_Interleaved_Option_Tooltip.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-16.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Dolby_Atmos_Template_List_Expanded.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-17.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Finder_Window_Showing_New_Folder.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-18.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Finder_Window_With_Session_Template_File.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-19.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Save_New_Session_As_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-03-first-launch-of-pro-tools-20.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Empty_Edit_Window_Single_Track.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-06-optional-presonus-faderport-8-configuration-01.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Setup_Menu_Open_in_Edit_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-06-optional-presonus-faderport-8-configuration-02.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Peripherals_MIDI_Controllers_Predefined_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-1-studio-login-and-file-access-01.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Empty_Desktop_Finder_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-1-studio-login-and-file-access-02.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Finder_Menu_Settings_Highlighted.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-1-studio-login-and-file-access-03.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Finder_Settings_General_Pane.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-1-studio-login-and-file-access-04.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Finder_Settings_General_Pane_Open.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-1-studio-login-and-file-access-05.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Finder_Settings_Sidebar_Preferences.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-1-studio-login-and-file-access-06.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Macintosh_HD_Root_Folders.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-1-studio-login-and-file-access-08.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Macintosh_HD_Root_Folders_in_Finder.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-1-studio-login-and-file-access-10.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Users_Folder_With_Shared_Selected.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-1-studio-login-and-file-access-11.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Shared_Folder_With_Lab_Files.png` |
| `DAPR-3340--Spatial_Audio_I/Images/boaa-lab/lesson-1-studio-login-and-file-access-12.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Shared_Template_File_in_Finder.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-audio-and-network-settings-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Renderer_Preferences_Devices_and_Monitoring.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-audio-and-network-settings-02.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Playback_Engine_Set_to_Dolby_Bridge.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-audio-and-network-settings-03.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Red_Arrow_Pointing_to_Atmos_Tab.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-audio-and-network-settings-04.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Renderer_Host_Address_Field_Arrow.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-bed-versus-object-decision-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Bed_versus_Object_Decision.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-music-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Input_Configuration_List_of_Object_Assignments.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-music-02.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Renderer_Groups_List_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-music-03.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Input_Configuration_Object_Group_Assignments.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-music-04.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Atmos_Submix_Channel_Strip_Bank.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-music-05.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Mixer_Strips_Assigned_to_Objects.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-post-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Input_Configuration_Bed_and_Object_Rows.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-post-02.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Groups_Window_With_Group_List.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-post-03.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Input_Assignment_List_With_Groups.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-post-04.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Dolby_Atmos_Tab_Bed_and_Object_List.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-post-05.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Bus_List_of_Atmos_Stems.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-post-06.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Green_Submix_and_Reverb_Strips.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-exercise-post-07.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Object_Assigned_Post_Mixer_Strips.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-pt-atmos-object-assignment-dropdown-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Pt_Atmos_Object_Assignment_Dropdown.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-pt-atmos-object-group-menu-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Pt_Atmos_Object_Group_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-for-atmos-renderer-selector-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Renderer_Selector.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Create_Stereo_Objects_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-02.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Bed_and_Object_Path_Creation_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-03.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Atmos_Tab_With_Object_Paths.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-04.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Default_Format_Path_Order_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-05.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/New_Paths_Dialog_for_Bed_and_Objects.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-06.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Output_Paths_for_Bed_and_Objects.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-07.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Object_Paths_Mapped_to_Outputs.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-08.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Playback_Engine_Focusrite_Selection.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-09.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Aux_Device_List_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-10.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Audio_Device_List_With_Bridge_Checked.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-pro-tools-i-slash-o-for-dolby-atmos-mixing-11.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Output_Tab_Channel_Grid_Assignments.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-the-dolby-atmos-renderers-input-configuration-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Bed_Channels_and_Object_Rows.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-the-dolby-atmos-renderers-input-configuration-02.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Renaming_an_Object_Input_Row.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-the-dolby-atmos-renderers-input-configuration-03.gif` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Configuring_the_Dolby_Atmos_Renderers_Input_Configuration.gif` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-the-dolby-atmos-renderers-input-configuration-04.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Close_Up_of_Groups_Button.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-the-dolby-atmos-renderers-input-configuration-05.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Typing_a_New_Group_Name.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/configuring-the-dolby-atmos-renderers-input-configuration-06.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Object_Group_Assignment_Dropdown.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/routing-tracks-to-beds-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Output_Menu_Listing_Bed_Formats.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/routing-tracks-to-beds-02.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Track_Output_Assigned_to_Bed_Bus.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/routing-tracks-to-objects-01.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Track_Output_Selector_Showing_Object.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/routing-tracks-to-objects-02.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Object_Output_Selection_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/routing-tracks-to-objects-03.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Narrow_Strip_With_Object_Output.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/routing-tracks-to-objects-04.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Annotated_Object_Panel_Controls.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/routing-tracks-to-objects-05.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Green_Triangle_Output_Button.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/routing-tracks-to-objects-06.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Red_Record_Enable_Button_Icon.png` |
| `DAPR-3340--Spatial_Audio_I/Images/configuring-pro-tools-for-atmos/routing-tracks-to-objects-07.png` | `DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos/Tiny_Right_Arrow_Button_Icon.png` |
| `DAPR-3340--Spatial_Audio_I/Images/course-orientation/syllabus-3-01.jpg` | `DAPR-3340--Spatial_Audio_I/Course_Orientation/Campus_Waterfall_Behind_Concrete_Beams.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/binaural-settings-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Binaural_Settings.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/creating-re-renders-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Rerender_Window_With_Live_Layouts.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/creating-re-renders-02.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Re_Render_Layout_Dropdown_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/creating-re-renders-03.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Re_Render_Properties_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/dolby-atmos-deliverables-audio-vivid-renderer-select-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Audio_Vivid_Renderer_Select.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/dolby-atmos-deliverables-bounce-mix-adm-bwf-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Bounce_Mix_ADM_Bwf.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/dolby-atmos-deliverables-deliverable-tree-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Deliverable_Tree.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/dolby-atmos-deliverables-mpeg-h-renderer-bed-assign-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Mpeg_H_Renderer_Bed_Assign.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/dolby-atmos-deliverables-walkmix-360ra-headphone-view-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Walkmix_360ra_Headphone_View.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/dolby-atmos-deliverables-walkmix-360ra-speaker-view-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Walkmix_360ra_Speaker_View.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/exporting-deliverables-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Export_Master_to_ADM_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/exporting-deliverables-02.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Export_Master_to_IMF_IAB_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/exporting-deliverables-03.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Export_Master_to_MP_Four_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/exporting-deliverables-04.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Export_Re_Renders_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/loudness-analysis-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Loudness_Analysis_Window_Before_Measuring.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/loudness-analysis-02.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Loudness_Analysis_Results_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/recording-a-dolby-atmos-master-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Recording_a_Dolby_Atmos_Master.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/unlocking-and-modifying-a-master-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Unlock_Master_File_Button.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-deliverables/unlocking-and-modifying-a-master-02.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Deliverables/Record_In_and_Out_Toggle.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-dolby-atomos-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Dolby_Atomos.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-input-configuration-groups-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Input_Configuration_Groups.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Renderer_Window_With_Meters_and_Room.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-02.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Monitoring_Selector_Set_to_Physical.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-03.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Source_Input_and_Master_Toggle.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-04.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Timecode_Counter_and_Transport_Buttons.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-05.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Record_In_and_Out_Toggle_Close_Up.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-06.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Output_Gain_With_DIM_and_MUTE.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-07.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Master_File_Timecode_Header_Bar.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-08.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Master_File_FFOA_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-09.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Input_Channel_Status_Grid.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-10.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Row_of_Input_Status_Indicator_Circles.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-11.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Numbered_Input_Indicator_Circles.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-12.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Input_Signal_Indicator_Lights.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-13.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Bed_Channel_Meter_Bank.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-14.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Channel_Level_Meters_for_Bed_Speakers.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-15.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Vertical_Limiter_Meter_Pair.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-16.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Binaural_and_Limiter_Meters.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-17.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Binaural_Output_Meter_Close_Up.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-18.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Speaker_Layout_Map_With_Flagged_Speaker.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-19.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Room_View_With_Object_Spheres.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-20.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Room_View_With_Object_Trajectory.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-21.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Three_Dimensional_Room_View_With_Objects.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-22.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Room_View_With_Single_Object_Sphere.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-23.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/View_and_Show_Options_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-24.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Room_View_With_Listener_Silhouette.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-25.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Front_View_of_Object_Position_Dots.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-interface-overview-26.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Room_View_of_Many_Object_Spheres.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-main-window-room-view-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Main_Window_Room_View.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-person-view-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Person_View.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-renderer-system-topology-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Renderer_System_Topology.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-theater-view-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Theater_View.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/dolby-atmos-renderer-trim-and-downmix-session-data-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Trim_and_Downmix_Session_Data.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/headphone-only-mode-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Headphone_Only_Mode.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/room-setup-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Speaker_Layout_Map_in_Room_Setup.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/room-setup-02.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Speaker_Routing_Position_Map.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/room-setup-03.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Room_Setup_Monitoring_Speaker_Layout.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/room-setup-04.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Add_Layout_Button_and_Layout_List.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/speaker-calibration-and-room-eq-for-monitoring-01.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Speaker_EQ_Calibration_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/speaker-calibration-and-room-eq-for-monitoring-02.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Signal_Generator_Source_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/speaker-calibration-and-room-eq-for-monitoring-03.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Signal_Generator_Pink_Noise_Control.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/speaker-calibration-and-room-eq-for-monitoring-04.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Pink_Noise_Rotate_Mode_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/speaker-calibration-and-room-eq-for-monitoring-05.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Editing_Speaker_Gain_Value.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/speaker-calibration-and-room-eq-for-monitoring-06.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Room_EQ_Curve_and_Sliders.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/speaker-calibration-and-room-eq-for-monitoring-07.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Speaker_and_Headphone_Delay_Field.png` |
| `DAPR-3340--Spatial_Audio_I/Images/dolby-atmos-renderer/speaker-calibration-and-room-eq-for-monitoring-08.png` | `DAPR-3340--Spatial_Audio_I/Dolby_Atmos_Renderer/Speaker_Delay_Tab_of_Room_Setup.png` |
| `DAPR-3340--Spatial_Audio_I/Images/final-project-and-final-exam/final-project-and-final-exam-course-concept-map-01.png` | `DAPR-3340--Spatial_Audio_I/Final_Project_and_Final_Exam/Course_Concept_Map.png` |
| `DAPR-3340--Spatial_Audio_I/Images/final-project-and-final-exam/final-project-and-final-exam-final-exam-coverage-map-01.png` | `DAPR-3340--Spatial_Audio_I/Final_Project_and_Final_Exam/Final_Exam_Coverage_Map.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-analog-digital-delivery-evolution-41.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Analog_Digital_Delivery_Evolution.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-atmos-monitoring-reference-levels-51.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Atmos_Monitoring_Reference_Levels.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-blu-ray-disc-22.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Blu_Ray_Disc.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-compact-disc-16.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Compact_Disc.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dangerous-monitor-stsr-54.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dangerous_Monitor_Stsr.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-delivered-vs-receiver-processing-40.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Delivered_vs_Receiver_Processing.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dolby-pro-logic-04.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dolby_Pro_Logic.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dolby-pro-logic-history-overview-44.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dolby_Pro_Logic_History_Overview.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dolby-pro-logic-history-timeline-39.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dolby_Pro_Logic_History_Timeline.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dolby-pro-logic-i-ix-06.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dolby_Pro_Logic_I_Ix.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dolby-pro-logic-i-iz-07.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dolby_Pro_Logic_I_Iz.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dolby-pro-logic-ii-05.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dolby_Pro_Logic_Ii.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dolby-surround-03.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dolby_Surround.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dts-08.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dts.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dts-9624-13.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dts_9624.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dts-digital-surround-09.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dts_Digital_Surround.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dts-neo-6-11.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dts_Neo_6.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dts-neo-x-12.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dts_Neo_X.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dtses-10.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dtses.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dtshd-high-resolution-14.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dtshd_High_Resolution.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dtshd-master-audio-15.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dtshd_Master_Audio.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dvd-audio-20.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dvd_Audio.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-dvd-video-19.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Dvd_Video.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-five-point-one-to-seven-point-one-extension-29.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Five_Point_One_to_Seven_Point_One_Extension.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-grouped-monitor-control-47.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Grouped_Monitor_Control.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-hddvd-21.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Hddvd.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-itu-51-speaker-layout-23.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Itu_51_Speaker_Layout.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-itu-71-speaker-layout-24.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Itu_71_Speaker_Layout.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-laser-disc-17.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Laser_Disc.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-legacy-dolby-hardware-milestones-43.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Legacy_Dolby_Hardware_Milestones.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-lfe-vs-bass-management-25.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/LFE_vs_Bass_Management.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-matrix-encoder-decoder-42.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Matrix_Encoder_Decoder.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-modern-71-side-rear-layout-28.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Modern_71_Side_Rear_Layout.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-modern-atmos-monitoring-path-50.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Modern_Atmos_Monitoring_Path.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-multichannel-calibration-workflow-48.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Multichannel_Calibration_Workflow.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-multichannel-output-counts-45.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Multichannel_Output_Counts.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-pro-logic-i-ix-vs-i-iz-30.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Pro_Logic_I_Ix_vs_I_Iz.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-quadraphonic-speaker-layout-01.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Quadraphonic_Speaker_Layout.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-red-net-control-grouped-outputs-52.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Red_Net_Control_Grouped_Outputs.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-red-net-control-output-trim-53.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Red_Net_Control_Output_Trim.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-sacd-18.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Sacd.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-sdds-71-five-front-layout-27.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Sdds_71_Five_Front_Layout.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-sdds-educational-badge-36.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Sdds_Educational_Badge.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-seven-point-one-and-height-formats-31.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Seven_Point_One_and_Height_Formats.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-seven-point-one-channel-order-vs-labels-38.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Seven_Point_One_Channel_Order_vs_Labels.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-seven-point-one-families-comparison-35.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Seven_Point_One_Families_Comparison.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-seven-point-one-music-use-34.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Seven_Point_One_Music_Use.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-seven-point-one-naming-crosswalk-26.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Seven_Point_One_Naming_Crosswalk.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-software-vs-hardware-monitor-control-49.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Software_vs_Hardware_Monitor_Control.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-star-wars-dolby-stereo-02.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Star_Wars_Dolby_Stereo.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-stereo-to-immersive-progression-01.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Stereo_to_Immersive_Progression.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-surround-format-timeline-01.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Surround_Format_Timeline.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-surround-monitoring-signal-flow-46.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Surround_Monitoring_Signal_Flow.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-windows-media-audio-9-pro-71-32.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Windows_Media_Audio_9_Pro_71.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-windows-media-audio-9-pro-badge-37.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Windows_Media_Audio_9_Pro_Badge.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/introduction-to-surround-and-multichannel-audio-windows-media-vs-windows-spatial-sound-33.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Windows_Media_vs_Windows_Spatial_Sound.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/welcome-surround-mixing-and-immersive-audio-01.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Welcome_Surround_Mixing_and_Immersive_Audio.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/what-does-5-dot-1-or-7-dot-1-refer-to-01.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Listener_Surrounded_by_Speaker_Circle.png` |
| `DAPR-3340--Spatial_Audio_I/Images/introduction-to-surround-and-multichannel-audio/what-does-5-dot-1-or-7-dot-1-refer-to-02.png` | `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround/Overhead_Speaker_Layout_Diagram.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/atmos-panning-in-pro-tools-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Two_Object_Panner_Windows_Side_by_Side.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/atmos-panning-in-pro-tools-02.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Panner_Mode_Menu_With_Theater_Chosen.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/atmos-panning-in-pro-tools-03.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Miniature_Panner_Room_Thumbnail.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/atmos-panning-in-pro-tools-04.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Pan_Curve_Shape_Icons.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/atmos-panning-in-pro-tools-05.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Auto_Height_Override_Context_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/atmos-panning-in-pro-tools-06.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Panner_Grid_Icon_Dropdown_Open.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/atmos-panning-in-pro-tools-07.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Object_Panner_With_Position_Controls.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/atmos-panning-in-pro-tools-08.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Highlighted_Panner_Toolbar_Button.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/mixing-in-dolby-atmos-bed-and-object-structure-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Bed_and_Object_Structure.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/mixing-in-dolby-atmos-object-assignment-strips-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Object_Assignment_Strips.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/mixing-in-dolby-atmos-pt-immersive-panner-lcr-object-channels-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Pt_Immersive_Panner_Lcr_Object_Channels.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/mixing-in-dolby-atmos-pt-immersive-panner-mono-object-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Pt_Immersive_Panner_Mono_Object.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/mixing-in-dolby-atmos-pt-immersive-panner-stereo-object-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Pt_Immersive_Panner_Stereo_Object.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/mixing-in-dolby-atmos-pt-immersive-panner-top-view-speakers-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Pt_Immersive_Panner_Top_View_Speakers.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/mixing-in-dolby-atmos-pt-object-track-xyz-automation-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Pt_Object_Track_Xyz_Automation.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/mixing-in-dolby-atmos-track-output-bed-or-object-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Track_Output_Bed_or_Object.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/reverbs-in-an-atmos-mix-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Reverbs_in_an_Atmos_Mix.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/synchronizing-pro-tools-and-the-renderer-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Timecode_Rate_Dropdown_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/synchronizing-pro-tools-and-the-renderer-02.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Frame_Rate_Menu_in_Renderer_Preferences.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/synchronizing-pro-tools-and-the-renderer-03.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Output_Paths_Including_LTC_Channel.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/synchronizing-pro-tools-and-the-renderer-04.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/LTC_Generator_Plugin_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/synchronizing-pro-tools-and-the-renderer-05.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/LTC_Generator_Track_Strip.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/synchronizing-pro-tools-and-the-renderer-06.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Renderer_Device_Settings_and_LTC_Channel.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/synchronizing-pro-tools-and-the-renderer-07.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Transport_Bar_Sync_Button_Highlighted.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/the-atmos-music-panner-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Music_Panner_Network_Address_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/the-atmos-music-panner-02.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Music_Panner_Object_Selection_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/the-atmos-music-panner-03.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Music_Panner_Object_Pair_Linking.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/the-atmos-music-panner-04.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Music_Panner_Plugin_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/the-atmos-music-panner-05.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Music_Panner_Path_Shape_Buttons.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/the-atmos-music-panner-06.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Sequencer_Step_Buttons_Panel.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/the-atmos-music-panner-07.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Music_Panner_Sequencer_Step_Buttons.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/the-atmos-music-panner-08.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Sequencer_Step_Duration_Dropdown.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/the-atmos-music-panner-09.gif` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/The_Atmos_Music_Panner.gif` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/using-groups-and-vcas-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Guitar_Object_Channel_Strips.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/using-groups-and-vcas-02.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Group_Assignment_Buttons_Highlighted.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/using-groups-and-vcas-03.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Create_Group_Dialog_for_Guitar_Mix.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/using-groups-and-vcas-04.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Red_Arrow_to_VCA_Master_Strip.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/using-groups-and-vcas-05.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Modify_Groups_Attributes_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/using-groups-and-vcas-06.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Guitar_Strips_With_EQ_Plugin_Open.png` |
| `DAPR-3340--Spatial_Audio_I/Images/mixing-in-dolby-atmos/working-with-multiple-beds-01.png` | `DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Working_with_Multiple_Beds.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/limiting-and-brickwall-limiters-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Limiting_and_Brickwall_Limiters.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/loudness-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Equal_Loudness_Contour_Chart.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/loudness-02.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Short_Chain_of_Boxed_Processor_Icons.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/loudness-03.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Full_Chain_of_Boxed_Processor_Icons.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/mid-slash-side-processing-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Mid_Slash_Side_Processing.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/multiband-compression-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Multiband_Compression.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-encoding-plugins-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Surround_Encoding_Plugins.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-encoding-plugins-02.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Surround_Encoding_Plugins.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-encoding-software-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Surround_Encoding_Software.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-encoding-software-02.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Surround_Encoding_Software.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-common-audio-meters-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Common_Audio_Meters.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-dither-quantization-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Dither_Quantization.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-dither-versus-truncation-noise-floor-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Dither_versus_Truncation_Noise_Floor.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-music-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Exercise_Music.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-music-02.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Mastering_Chain_and_Print_Track_Strips.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-music-03.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Finder_Folder_of_Split_Master_Files.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-music-04.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Channel_File_Assignment_for_Encoding.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-music-05.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Dolby_Digital_Encoding_Preset_Window.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-post-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Pro_Limiter_Plugin_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-post-02.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/EQ_Low_Pass_Filter_On_Sub.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-post-03.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Limiter_Plugin_With_Loudness_Readouts.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-post-04.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Multichannel_Stem_File_List.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-post-05.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Channel_File_Slot_Assignment_Dialog.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-exercise-post-06.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Compressor_Batch_With_Dolby_Digital_Preset.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-limiter-ceiling-and-intersample-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Limiter_Ceiling_and_Intersample.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-mastering-signal-chain-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Mastering_Signal_Chain.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-mixing-versus-mastering-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Mixing_versus_Mastering.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-multiband-crossover-bands-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Multiband_Crossover_Bands.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-pt-io-setup-dolby-atmos-tab-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Pt_IO_Setup_Dolby_Atmos_Tab.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-pt-io-setup-output-atmos-objects-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Pt_IO_Setup_Output_Atmos_Objects.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-and-encoding-surround-delivery-formats-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Surround_Delivery_Formats.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-plugins-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Mastering_Suite_With_EQ_Curve.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-plugins-02.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Surround_Limiter_Plugin_Window.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-plugins-03.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Down_Mixer_Plugin_Window.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-plugins-04.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Waves_Surround_Mixdown_Plugin_Window.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-plugins-05.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Upmix_Plugin_Polar_Display.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-mastering-plugins-06.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Upmix_Plugin_Channel_Meters.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mastering-and-encoding/surround-metering-plugins-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mastering_and_Encoding/Surround_Metering_Plugins.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/advanced-mixing-concepts-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Wide_Mixer_View_With_Highlighted_Strips.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/advanced-mixing-concepts-02.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Send_Assignment_Context_Menu_On_Strip.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/advanced-mixing-concepts-03.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Track_Assignment_Context_Menu.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/advanced-mixing-concepts-04.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Drum_Mixer_Strips_With_Inserts.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/automation-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Automation_Breakpoints_over_Colored_Clips.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/automation-02.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Automation_Window_with_Write_Enable_Buttons.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/final-mix-creation-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Post_Production_Mix_Workflow_Chart.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/final-mix-creation-02.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Production_Session_Flow_Chart.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/final-mix-creation-03.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Export_to_AAF_Options_Dialog.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/loudness-metering-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Loudness_Metering.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/multi-channel-panning-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Surround_Panner_Output_Window.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/multi-channel-panning-02.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Linked_Dual_Surround_Panner_Grids.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/output-configuration-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Guitar_and_Piano_Mixer_Strips.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/output-configuration-02.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Horn_Track_Strips_on_Shared_Bus.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/output-configuration-03.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Wide_Mix_Window_of_Colored_Strips.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/output-configuration-04.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Output_Path_Submenu_of_Subpaths.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/output-configuration-05.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Decca_Tree_Microphone_Channel_Strips.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/output-configuration-06.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Output_Path_Menu_With_Studio_Main.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/output-configuration-07.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Output_Window_With_Highlighted_LFE_Fader.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-color-coded-input-output-and-bus-paths-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Color_Coded_Input_Output_and_Bus_Paths.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-divergence-front-rear-link-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Divergence_Front_Rear_Link.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-music-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Bus_Tab_Listing_Surround_Busses.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-music-02.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Submix_Strips_Feeding_Main_Mix.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-music-03.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/String_Section_Strips_Routed_to_Submix.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-music-04.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Create_Group_Dialog_for_Drum_Tracks.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-music-05.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Drum_Strips_With_VCA_Master.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-music-06.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Compressor_Limiter_Over_Drum_Strips.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-music-07.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Exercise_Music.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-music-08.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Export_Selected_Dialog_High_Sample_Rate.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-post-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Bus_Paths_Mapped_to_Surround_Monitors.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-post-02.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Stem_and_Submix_Channel_Strips.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-post-03.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Reverb_Auxiliary_and_Object_Strips.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-post-04.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Dialogue_and_Background_Stem_Strips.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-post-05.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Create_Group_Dialog_for_Dialog_Tracks.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-post-06.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Dialog_Strips_Under_VCA_Master.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-post-07.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Surround_Panner_and_Automation_Ramp.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-exercise-post-08.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Export_Selected_Dialog_Video_Sample_Rate.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-io-setup-path-color-selector-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/IO_Setup_Path_Color_Selector.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-loudness-integrated-shortterm-truepeak-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Loudness_Integrated_Shortterm_Truepeak.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-pt-mix-window-atmos-bed-objects-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Pt_Mix_Window_Atmos_Bed_Objects.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-pt-surround-panner-annotated-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Pt_Surround_Panner_Annotated.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-pt-surround-panner-mode-menu-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Pt_Surround_Panner_Mode_Menu.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-static-versus-dynamic-automation-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Static_versus_Dynamic_Automation.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-surround-mix-workflow-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Surround_Mix_Workflow.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-surround-panner-window-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Surround_Panner_Window.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-mixing-surround-session-routing-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Surround_Session_Routing.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-plug-ins-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Two_Lindell_Channel_Strip_Windows.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-plug-ins-02.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Plugin_Channel_Selection_Dropdown.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-mixing/surround-plug-ins-03.png` | `DAPR-3340--Spatial_Audio_I/Surround__Mixing/Surround_Plug_Ins.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/consumer-listening-environment-01.jpeg` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Consumer_Listening_Environment.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/consumer-listening-environment-02.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Consumer_Listening_Environment.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/professional-mixing-environment-01.jpeg` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Professional_Mixing_Environment.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/professional-mixing-environment-02.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Professional_Mixing_Environment.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/room-design-and-acoustics-01.jpeg` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Studio_Live_Room_Photo.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/room-design-and-acoustics-02.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Room_Design_and_Acoustics.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/room-design-and-acoustics-03.jpeg` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Room_Correction_EQ_Curve_Display.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/speaker-placement-01.jpeg` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Speaker_Placement.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-bass-management-signal-path-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Bass_Management_Signal_Path.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-calibration-order-of-operations-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Calibration_Order_of_Operations.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-consumer-room-compromises-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Consumer_Room_Compromises.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-exercise-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/New_Tracks_Dialog_for_Pink_Noise.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-exercise-02.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Signal_Generator_Set_to_Pink_Noise.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-exercise-03.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Pink_Noise_Test_Channel_Strip.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-monitoring-environments-comparison-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Monitoring_Environments_Comparison.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-placement-height-distance-toe-in-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Placement_Height_Distance_Toe_in.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-pt-51-format-channel-assignments-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Pt_51_Format_Channel_Assignments.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-pt-mix-window-51-surround-routing-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Pt_Mix_Window_51_Surround_Routing.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/surround-monitoring-theatrical-versus-home-scale-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Theatrical_versus_Home_Scale.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/system-calibration-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/System_Calibration.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-monitoring/theatrical-listening-environment-01.jpeg` | `DAPR-3340--Spatial_Audio_I/Surround__Monitoring/Theatrical_Listening_Environment.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/introduction-to-surround-recording-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Introduction_to_Surround_Recording.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-exercise-01.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Input_Setup_Channel_Mapping_Matrix.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-exercise-02.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Output_Tab_of_Thunderbolt_Interface_Paths.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-exercise-03.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/New_Paths_Dialog_for_Surround_Output.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-exercise-04.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Output_Path_Routing_Matrix.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-exercise-05.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Session_Monitor_Path_Settings.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-exercise-06.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/New_Paths_Dialog_for_Surround_Busses.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-exercise-07.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/New_Tracks_Dialog_Creating_Mono_Tracks.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-exercise-08.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Surround_Output_Assignment_Menu.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-exercise-09.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Mic_Input_Strips_With_Channel_Labels.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-exercise-10.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/New_Tracks_Dialog_for_Surround_Track.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-fukada-tree-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Fukada_Tree.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-hamasaki-square-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Hamasaki_Square.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-irt-cross-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Irt_Cross.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-location-monitoring-chain-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Location_Monitoring_Chain.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-modified-decca-tree-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Modified_Decca_Tree.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-pt-surround-panner-plugin-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Pt_Surround_Panner_Plugin.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-surround-array-geometry-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Surround_Array_Geometry.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/surround-recording-wide-cardioid-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Wide_Cardioid.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-standard-microphones-01.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Microphone_Spacing_Distance_Diagram.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-standard-microphones-03.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Cardioid_Pattern_Array_Layout.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-standard-microphones-05.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Spaced_Cardioid_Array_Spacing_Diagram.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-standard-microphones-06.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Five_Microphone_Surround_Array_Diagram.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-standard-microphones-08.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Surround_Microphone_Array_With_Angles.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-standard-microphones-10.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Microphone_Spacing_Diagram_With_Measurements.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-standard-microphones-11.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Facing_Bidirectional_Polar_Pattern_Diagram.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-standard-microphones-12.jpg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Using_Standard_Microphones.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-standard-microphones-13.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Three_Cardioid_Front_Array_Diagram.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-standard-microphones-14.png` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Cardioid_Array_With_Labeled_Distances.png` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-surround-microphones-01.jpeg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Rounded_Mesh_Covered_Microphone_Housing.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-surround-microphones-02.jpeg` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Ambisonic_Microphone_With_Capsules_Exposed.jpg` |
| `DAPR-3340--Spatial_Audio_I/Images/surround-recording/using-surround-microphones-03.gif` | `DAPR-3340--Spatial_Audio_I/Surround__Recording/Using_Surround_Microphones.gif` |
| `DAPR-3340--Spatial_Audio_I/Images/wiki-banners/boaa-lab-welcome-banner.png` | `DAPR-3340--Spatial_Audio_I/BOAA_Lab/Boaa_Lab_Welcome_Banner.png` |

## 5. Cloudflare download renames

**10 files.** Base URL: `https://uvu-files.adamo.workers.dev/`

| Old path | New path | Module |
|---|---|---|
| `DAPR-3340--Spatial_Audio_I/A_Horse_is_Not_a_Home_-_Consolidated.zip` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/A_Horse_is_Not_a_Home-Consolidated.zip` | M06: Ambisonics and Binaural (Week 9) |
| `DAPR-3340--Spatial_Audio_I/Ambeo.zip` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambeo.zip` | M06: Ambisonics and Binaural (Week 9) |
| `DAPR-3340--Spatial_Audio_I/Desert_Ambience-AmbiX.zip` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Desert_Ambience-AmbiX.zip` | M06: Ambisonics and Binaural (Week 9) |
| `DAPR-3340--Spatial_Audio_I/Footsteps_Binaural.wav` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Footsteps_Binaural.wav` | M06: Ambisonics and Binaural (Week 9) |
| `DAPR-3340--Spatial_Audio_I/Incubate.zip` | `DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Incubate.zip` | M04: Surround Mixing and Surround Plugins (Week 6) |
| `DAPR-3340--Spatial_Audio_I/Natures_Fury_Dolby_Demo.zip` | `DAPR-3340--Spatial_Audio_I/The_Dolby_Atmos_Renderer/Natures_Fury_Dolby_Demo.zip` | M07: The Dolby Atmos Renderer (Week 10) |
| `DAPR-3340--Spatial_Audio_I/Prop_Plane_Binaural.wav` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Prop_Plane_Binaural.wav` | M06: Ambisonics and Binaural (Week 9) |
| `DAPR-3340--Spatial_Audio_I/Sennheiser-Ambeo-A-B-Converter-1-2-1-Mac.zip` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Sennheiser_Ambeo-A-B_Converter-Mac.zip` | NO MODULE REFERENCE |
| `DAPR-3340--Spatial_Audio_I/Those_Who_Love-Strings-AmbiX.zip` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Those_Who_Love-Strings-AmbiX.zip` | M06: Ambisonics and Binaural (Week 9) |
| `DAPR-3340--Spatial_Audio_I/Those_Who_Love.zip` | `DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Those_Who_Love.zip` | M04: Surround Mixing and Surround Plugins (Week 6) |

## 6. Unresolved

None for this course.

## 7. Reference rewrite status

Every reference inside the `Classes/` tree of this repo has been rewritten to the new paths. What has **not** been rewritten:

- The Canvas cartridge for this course. That is the job this file exists for.
- Live Canvas pages. They only change when the rebuilt cartridge is imported.
- Files under `_briefs/` and `_superseded/`. Those are historical working notes and were left alone on purpose.
- `DAPR-3340--Spatial_Audio_I--Image-Reference.html` at the course root, if one exists. It is a generated sheet and should be regenerated rather than patched.

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
