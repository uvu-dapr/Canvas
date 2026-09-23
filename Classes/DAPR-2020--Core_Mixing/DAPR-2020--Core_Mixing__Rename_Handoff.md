# DAPR-2020--Core_Mixing — Rename Handoff

**Date:** 2026-09-22  
**Course folder:** `DAPR-2020--Core_Mixing`  
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

**135 files.** Base URL: `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/`

| Old path | New path |
|---|---|
| `DAPR-2020--Core_Mixing/Images/Balancing_and_Reverb/balancing-and-reverb-d-verb-algorithms-and-decay-01.png` | `DAPR-2020--Core_Mixing/Balancing_and_Reverb/D_Verb_Algorithms_and_Decay.png` |
| `DAPR-2020--Core_Mixing/Images/Balancing_and_Reverb/balancing-and-reverb-send-versus-insert-routing-01.png` | `DAPR-2020--Core_Mixing/Balancing_and_Reverb/Send_versus_Insert_Routing.png` |
| `DAPR-2020--Core_Mixing/Images/Balancing_and_Reverb/balancing-and-reverb-space-scale-comparison-01.png` | `DAPR-2020--Core_Mixing/Balancing_and_Reverb/Space_Scale_Comparison.png` |
| `DAPR-2020--Core_Mixing/Images/Calibration_and_Monitoring/calibration-and-monitoring-gain-stages-chain-01.png` | `DAPR-2020--Core_Mixing/Calibration_and_Monitoring/Gain_Stages_Chain.png` |
| `DAPR-2020--Core_Mixing/Images/Calibration_and_Monitoring/calibration-and-monitoring-gain-staging-chain-01.png` | `DAPR-2020--Core_Mixing/Calibration_and_Monitoring/Gain_Staging_Chain.png` |
| `DAPR-2020--Core_Mixing/Images/Calibration_and_Monitoring/calibration-and-monitoring-head-torso-measurement-01.png` | `DAPR-2020--Core_Mixing/Calibration_and_Monitoring/Head_Torso_Measurement.png` |
| `DAPR-2020--Core_Mixing/Images/Calibration_and_Monitoring/calibration-and-monitoring-headphone-seal-cross-section-01.png` | `DAPR-2020--Core_Mixing/Calibration_and_Monitoring/Headphone_Seal_Cross_Section.png` |
| `DAPR-2020--Core_Mixing/Images/Calibration_and_Monitoring/calibration-and-monitoring-metering-preferences-01.png` | `DAPR-2020--Core_Mixing/Calibration_and_Monitoring/Metering_Preferences.png` |
| `DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement/comping-and-arrangement-crossfade-placement-01.png` | `DAPR-2020--Core_Mixing/Comping_and_Arrangement/Green_to_Blue_Waveform_Splice_Pair.png` |
| `DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement/comping-and-arrangement-crossfade-placement-02.png` | `DAPR-2020--Core_Mixing/Comping_and_Arrangement/Gray_Clips_with_Star_and_Crossfade.png` |
| `DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement/comping-and-arrangement-playlist-comp-lanes-01.png` | `DAPR-2020--Core_Mixing/Comping_and_Arrangement/Playlist_Comp_Lanes.png` |
| `DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement/pro-tools-playlist-selector-new-playlist.png` | `DAPR-2020--Core_Mixing/Comping_and_Arrangement/Pro_Tools_Playlist_Selector_New_Playlist.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Core_Mixing_-_DAPR_2020.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Core_Mixing_DAPR_2020.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Core_Recording_-_DAPR_2010-002.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Core_Recording_DAPR_2010_002.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Course_Outline.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Course_Outline.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Gemini_Generated_Image_31wn4e31wn4e31wn.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Gemini_Generated_Image_31wn4e31wn4e31wn.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Open_Canvas_Page_in_New_Tab.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Open_Canvas_Page_in_New_Tab.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Please_Complete_Your_Course_Evaluations_.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Please_Complete_Your_Course_Evaluations.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Screenshot_2026-04-29_at_8.20.14AM.jpg` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Dark_Purple_Course_Title_Card.jpg` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Student_Course_Evaluations.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Student_Course_Evaluations.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/avtech-engage.jpg` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Avtech_Engage.jpg` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/course-orientation-and-feedback-grade-breakdown-01.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Grade_Breakdown.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/course-orientation-and-feedback-learning-outcomes-01.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Learning_Outcomes.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/course-orientation-and-feedback-weekly-rhythm-01.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Weekly_Rhythm.png` |
| `DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/course-orientation-and-feedback-worksheet-to-pdf-flow-01.png` | `DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Worksheet_to_Pdf_Flow.png` |
| `DAPR-2020--Core_Mixing/Images/Dynamic_Effects/Compression_Switch.png` | `DAPR-2020--Core_Mixing/Dynamic_Effects/Compression_Switch.png` |
| `DAPR-2020--Core_Mixing/Images/Dynamic_Effects/Six_Rules_of_Compression.png` | `DAPR-2020--Core_Mixing/Dynamic_Effects/Six_Rules_of_Compression.png` |
| `DAPR-2020--Core_Mixing/Images/Dynamic_Effects/dynamic-effects-attack-too-fast-transient-loss-01.png` | `DAPR-2020--Core_Mixing/Dynamic_Effects/Attack_Too_Fast_Transient_Loss.png` |
| `DAPR-2020--Core_Mixing/Images/Dynamic_Effects/dynamic-effects-dyn3-compressor-controls-01.png` | `DAPR-2020--Core_Mixing/Dynamic_Effects/Dyn3_Compressor_Controls.png` |
| `DAPR-2020--Core_Mixing/Images/Dynamic_Effects/dynamic-effects-pro-compressor-side-chain-key-input-01.png` | `DAPR-2020--Core_Mixing/Dynamic_Effects/Pro_Compressor_Side_Chain_Key_Input.png` |
| `DAPR-2020--Core_Mixing/Images/Dynamic_Effects/dynamic-effects-side-chain-filter-kick-pumping-01.png` | `DAPR-2020--Core_Mixing/Dynamic_Effects/Side_Chain_Filter_Kick_Pumping.png` |
| `DAPR-2020--Core_Mixing/Images/Focus_and_Balance/Owen_Peterson_-_Technical_Ear_Trainer.png` | `DAPR-2020--Core_Mixing/Focus_and_Balance/Owen_Peterson_Technical_Ear_Trainer.png` |
| `DAPR-2020--Core_Mixing/Images/Focus_and_Balance/Pro_Tools_-_Mix_Window.png` | `DAPR-2020--Core_Mixing/Focus_and_Balance/Pro_Tools_Mix_Window.png` |
| `DAPR-2020--Core_Mixing/Images/Focus_and_Balance/focus-and-balance-channel-strip-anatomy-01.png` | `DAPR-2020--Core_Mixing/Focus_and_Balance/Channel_Strip_Anatomy.png` |
| `DAPR-2020--Core_Mixing/Images/Focus_and_Balance/focus-and-balance-drum-mic-path-lengths-01.png` | `DAPR-2020--Core_Mixing/Focus_and_Balance/Drum_Mic_Path_Lengths.png` |
| `DAPR-2020--Core_Mixing/Images/Focus_and_Balance/focus-and-balance-five-pass-mix-order-01.png` | `DAPR-2020--Core_Mixing/Focus_and_Balance/Five_Pass_Mix_Order.png` |
| `DAPR-2020--Core_Mixing/Images/Focus_and_Balance/focus-and-balance-multi-system-playback-check-01.png` | `DAPR-2020--Core_Mixing/Focus_and_Balance/Multi_System_Playback_Check.png` |
| `DAPR-2020--Core_Mixing/Images/Focus_and_Balance/focus-and-balance-solo-versus-context-01.png` | `DAPR-2020--Core_Mixing/Focus_and_Balance/Single_Blue_Burst_beside_Stacked_Tracks.png` |
| `DAPR-2020--Core_Mixing/Images/Focus_and_Balance/focus-and-balance-solo-versus-context-02.png` | `DAPR-2020--Core_Mixing/Focus_and_Balance/Single_Clip_beside_Stacked_Track_Rows.png` |
| `DAPR-2020--Core_Mixing/Images/Focus_and_Balance/focus-and-balance-stereo-field-map-01.png` | `DAPR-2020--Core_Mixing/Focus_and_Balance/Stereo_Field_Map.png` |
| `DAPR-2020--Core_Mixing/Images/Mid_Side_Technique/mid-side-technique-figure-8-null-plane-01.png` | `DAPR-2020--Core_Mixing/Mid-Side_Technique/Figure_8_Null_Plane.png` |
| `DAPR-2020--Core_Mixing/Images/Mid_Side_Technique/mid-side-technique-ms-matrix-signal-flow-01.png` | `DAPR-2020--Core_Mixing/Mid-Side_Technique/Ms_Matrix_Signal_Flow.png` |
| `DAPR-2020--Core_Mixing/Images/Mix_Acoustics/mix-acoustics-first-reflection-points-01.png` | `DAPR-2020--Core_Mixing/Mix_Acoustics/First_Reflection_Points.png` |
| `DAPR-2020--Core_Mixing/Images/Mix_Acoustics/mix-acoustics-listening-triangle-overhead-01.png` | `DAPR-2020--Core_Mixing/Mix_Acoustics/Listening_Triangle_Overhead.png` |
| `DAPR-2020--Core_Mixing/Images/Mix_Acoustics/mix-acoustics-thin-foam-versus-broadband-01.png` | `DAPR-2020--Core_Mixing/Mix_Acoustics/Thin_Foam_versus_Broadband.png` |
| `DAPR-2020--Core_Mixing/Images/Mix_Acoustics/mix-acoustics-treatment-types-comparison-01.png` | `DAPR-2020--Core_Mixing/Mix_Acoustics/Treatment_Types_Comparison.png` |
| `DAPR-2020--Core_Mixing/Images/Pro_Tools_Fundamentals/PT_identify_beat_bar_beat_markers.jpg` | `DAPR-2020--Core_Mixing/Pro_Tools_Fundamentals/PT_Identify_Beat_Bar_Beat_Markers.jpg` |
| `DAPR-2020--Core_Mixing/Images/Pro_Tools_Fundamentals/pro-tools-fundamentals-dashboard-new-session-01.png` | `DAPR-2020--Core_Mixing/Pro_Tools_Fundamentals/Dashboard_New_Session.png` |
| `DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Core_Mixing_Lab_-_DAPR_2020L.png` | `DAPR-2020--Core_Mixing/Professional_Practice_Presentations_and_Sessions/Core_Mixing_Lab_DAPR_2020L.png` |
| `DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/professional-practice-bounce-specification-01.png` | `DAPR-2020--Core_Mixing/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Bounce_Specification.png` |
| `DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/professional-practice-bounce-truncation-01.png` | `DAPR-2020--Core_Mixing/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Bounce_Truncation.png` |
| `DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/professional-practice-delivery-verification-checklist-01.png` | `DAPR-2020--Core_Mixing/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Delivery_Verification_Checklist.png` |
| `DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/professional-practice-multitrack-download-flow-01.png` | `DAPR-2020--Core_Mixing/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Multitrack_Download_Flow.png` |
| `DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/professional-practice-network-drive-path-01.png` | `DAPR-2020--Core_Mixing/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Network_Drive_Path.png` |
| `DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/professional-practice-session-delivery-package-01.png` | `DAPR-2020--Core_Mixing/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Session_Delivery_Package.png` |
| `DAPR-2020--Core_Mixing/Images/Spectral_Effects_and_EQ/VocalEQCheatSheet.JPG` | `DAPR-2020--Core_Mixing/Spectral_Effects_and_EQ/Vocal_EQ_Frequency_Band_Chart.jpg` |
| `DAPR-2020--Core_Mixing/Images/Spectral_Effects_and_EQ/spectral-effects-and-eq-304e-equalizer-window-01.png` | `DAPR-2020--Core_Mixing/Spectral_Effects_and_EQ/304e_Equalizer_Window.png` |
| `DAPR-2020--Core_Mixing/Images/Spectral_Effects_and_EQ/spectral-effects-and-eq-boost-wide-cut-narrow-01.png` | `DAPR-2020--Core_Mixing/Spectral_Effects_and_EQ/Boost_Wide_Cut_Narrow.png` |
| `DAPR-2020--Core_Mixing/Images/Timing/pro-tools-tce-plugin-preferences.png` | `DAPR-2020--Core_Mixing/Timing/Pro_Tools_Tce_Plugin_Preferences.png` |
| `DAPR-2020--Core_Mixing/Images/Timing/timing-elastic-audio-warp-markers-01.png` | `DAPR-2020--Core_Mixing/Timing/Elastic_Audio_Warp_Markers.png` |
| `DAPR-2020--Core_Mixing/Images/Timing/timing-quantize-strength-comparison-01.png` | `DAPR-2020--Core_Mixing/Timing/Waveform_Rows_against_Grid_Lines.png` |
| `DAPR-2020--Core_Mixing/Images/Timing/timing-quantize-strength-comparison-02.png` | `DAPR-2020--Core_Mixing/Timing/Marker_Rows_at_Varying_Offsets.png` |
| `DAPR-2020--Core_Mixing/Images/Timing/timing-tuning-correction-amount-comparison-02.png` | `DAPR-2020--Core_Mixing/Tuning/Correction_Amount_Comparison_Boxed.png` |
| `DAPR-2020--Core_Mixing/Images/Timing/timing-tuning-scale-and-target-notes-02.png` | `DAPR-2020--Core_Mixing/Tuning/Scale_and_Target_Notes_Boxed.png` |
| `DAPR-2020--Core_Mixing/Images/Timing/tuning-correction-amount-comparison-01.png` | `DAPR-2020--Core_Mixing/Tuning/Correction_Amount_Comparison_Curves.png` |
| `DAPR-2020--Core_Mixing/Images/Timing/tuning-correction-speed-scoop-01.png` | `DAPR-2020--Core_Mixing/Tuning/Correction_Speed_Scoop.png` |
| `DAPR-2020--Core_Mixing/Images/Timing/tuning-scale-and-target-notes-01.png` | `DAPR-2020--Core_Mixing/Tuning/Scale_and_Target_Notes_Curves.png` |
| `DAPR-2020--Core_Mixing/Images/delay-and-stereo-enhancements/delay-and-stereo-enhancements-mono-collapse-check-01.png` | `DAPR-2020--Core_Mixing/Delay_and_Stereo_Enhancements/Mono_Collapse_Check.png` |
| `DAPR-2020--Core_Mixing/Images/delay-and-stereo-enhancements/delay-and-stereo-enhancements-moogerfooger-analog-delay-01.png` | `DAPR-2020--Core_Mixing/Delay_and_Stereo_Enhancements/Moogerfooger_Analog_Delay.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/aax_plugins_folder.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Aax_Plugins_Folder.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/about_general_settings.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/About_General_Settings.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/about_this_mac.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/About_This_MAC.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/about_this_mac_m5.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/About_This_MAC_M5.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/activity_monitor_cpu_tab.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Activity_Monitor_Cpu_Tab.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/air_effects_pkg_installer.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Air_Effects_Pkg_Installer.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/apogee_installer_example.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Apogee_Installer_Example.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/app_leftover_files.svg` | `DAPR-2020--Core_Mixing/macOS_Foundations/App_Leftover_Files.svg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/application_support_folder.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Application_Support_Folder.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/audio_devices_window.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Audio_Devices_Window.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/audio_midi_setup_midi_studio.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Audio_MIDI_Setup_MIDI_Studio.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/cd_alias_icon.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Cd_Alias_Icon.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/cloud_status_icon.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Cloud_Status_Icon.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/cmd_opt_h_after.jpg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Cmd_Opt_H_After.jpg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/cmd_opt_h_before.jpg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Cmd_Opt_H_Before.jpg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/compress_context_menu.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Compress_Context_Menu.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/compressed_zip_result.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Compressed_Zip_Result.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/console_no_messages.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Console_No_Messages.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/cpu_architecture_timeline.svg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Cpu_Architecture_Timeline.svg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/disk_utility_erase_dialog.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Disk_Utility_Erase_Dialog.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/disk_utility_macintosh_hd.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Disk_Utility_Macintosh_Hd.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/dmg_pkg_exe_flow.svg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Dmg_Pkg_Exe_Flow.svg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/dolby_audio_bridge_speaker_config.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Dolby_Audio_Bridge_Speaker_Config.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/dropbox_installer.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Dropbox_Installer.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/external_drive_sidebar.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/External_Drive_Sidebar.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/file_system_timeline.svg` | `DAPR-2020--Core_Mixing/macOS_Foundations/File_System_Timeline.svg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/finder_settings_advanced.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Finder_Settings_Advanced.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/finder_settings_general.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Finder_Settings_General.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/finder_view_options.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Finder_View_Options.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/force_quit_window.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Force_Quit_Window.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/function_keys_panel.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Function_Keys_Panel.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/get_info_kind_architecture.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Get_Info_Kind_Architecture.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/go_to_folder_autocomplete.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Go_to_Folder_Autocomplete.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/hardware_software_firmware_stack.svg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Hardware_Software_Firmware_Stack.svg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/home_folder_contents.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Home_Folder_Contents.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/launch_agents_daemons_folders.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Launch_Agents_Daemons_Folders.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/launch_agents_vs_daemons.svg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Launch_Agents_vs_Daemons.svg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/launchctl_list_terminal.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Launchctl_List_Terminal.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/leftover_folder_diagram.svg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Leftover_Folder_Diagram.svg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/library_audio_folder.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Library_Audio_Folder.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/login_items_panel.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Login_Items_Panel.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/macintosh_hd_get_info.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Macintosh_Hd_Get_Info.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/mouse_settings_panel.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Mouse_Settings_Panel.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/new_smart_folder_menu.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/New_Smart_Folder_Menu.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/package_contents_folder.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Package_Contents_Folder.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/package_contents_menu.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Package_Contents_Menu.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/privacy_security_pane.svg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Privacy_Security_Pane.svg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/quick_look_preview.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Quick_Look_Preview.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/root_folder_tree.svg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Root_Folder_Tree.svg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/screenshot_toolbar_diagram.svg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Dark_Toolbar_with_Labeled_Capture_Buttons.svg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/screenshot_toolbar_options.jpg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Screenshot_Options_Menu_over_System_Settings.jpg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/sharing_permissions.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Sharing_Permissions.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/skim_dmg_drag_to_applications.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Skim_Dmg_Drag_to_Applications.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/smart_folder_icon.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Smart_Folder_Icon.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/smart_folder_results.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Smart_Folder_Results.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/sound_output_list.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Sound_Output_List.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/spotlight_audio_midi_setup.jpg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Spotlight_Audio_MIDI_Setup.jpg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/spotlight_pro_tools.jpg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Spotlight_Pro_Tools.jpg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/system_info_memory.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/System_Info_Memory.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/system_information_usb.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/System_Information_USB.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/terminal_pwd_ls_cd.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Terminal_Pwd_Ls_Cd.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/time_machine_restore.jpg` | `DAPR-2020--Core_Mixing/macOS_Foundations/Time_Machine_Restore.jpg` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/turbotax_leftover_folder.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Turbotax_Leftover_Folder.png` |
| `DAPR-2020--Core_Mixing/Images/macOS_Foundations/utilities_folder.png` | `DAPR-2020--Core_Mixing/macOS_Foundations/Utilities_Folder.png` |
| `DAPR-2020--Core_Mixing/Images/master-buss-processing-and-endgame/master-buss-processing-and-endgame-channel-strip-full-window-01.png` | `DAPR-2020--Core_Mixing/Master_Bus_Processing_and_Endgame/Channel_Strip_Full_Window.png` |
| `DAPR-2020--Core_Mixing/Images/master-buss-processing-and-endgame/master-buss-processing-and-endgame-headroom-on-delivery-01.png` | `DAPR-2020--Core_Mixing/Master_Bus_Processing_and_Endgame/Headroom_on_Delivery.png` |

## 5. Cloudflare download renames

**27 files.** Base URL: `https://uvu-files.adamo.workers.dev/`

| Old path | New path | Module |
|---|---|---|
| `DAPR-2020--Core_Mixing/Calibration/Calibration-MNoise-96kHz-16bit.wav` | `DAPR-2020--Core_Mixing/Calibration_and_Monitoring/Calibration_MNoise_96kHz_16bit.wav` | Calibration & Monitoring |
| `DAPR-2020--Core_Mixing/Calibration/Calibration-PinkNoise-48kHz-24bit.wav` | `DAPR-2020--Core_Mixing/Calibration_and_Monitoring/Calibration_PinkNoise_48kHz_24bit.wav` | Calibration & Monitoring |
| `DAPR-2020--Core_Mixing/Presentations/calibration.pptx` | `DAPR-2020--Core_Mixing/Calibration.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Presentations/comping-and-arrangement.pptx` | `DAPR-2020--Core_Mixing/Comping_and_Arrangement.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Presentations/delay-and-chorus.pptx` | `DAPR-2020--Core_Mixing/Delay_and_Chorus.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Presentations/distortion.pptx` | `DAPR-2020--Core_Mixing/Distortion.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Presentations/dynamic-effects.pptx` | `DAPR-2020--Core_Mixing/Dynamic_Effects.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Presentations/focus-balance-and-interest-05.pptx` | `DAPR-2020--Core_Mixing/Archive/Focus_Balance_and_Forward_Motion_Sixteen_Slide.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Presentations/focus-balance-and-interest-07.pptx` | `DAPR-2020--Core_Mixing/Focus_Balance_and_Forward_Motion.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Presentations/mix-room-setup.pptx` | `DAPR-2020--Core_Mixing/Mix_Room_Setup.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Presentations/serial-and-parallel-processing.pptx` | `DAPR-2020--Core_Mixing/Serial_and_Parallel_Processing.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Presentations/spectral-effects.pptx` | `DAPR-2020--Core_Mixing/Spectral_Effects.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Presentations/time-based-effects.pptx` | `DAPR-2020--Core_Mixing/Time_Based_Effects.pptx` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Sessions/A_Horse_is_Not_a_Home-Consolidated.zip` | `DAPR-2020--Core_Mixing/Tuning/A_Horse_is_Not_a_Home-Consolidated.zip` | Tuning |
| `DAPR-2020--Core_Mixing/Sessions/Al_James-Full.zip` | `DAPR-2020--Core_Mixing/In-Class_Mixing/Al_James-Full.zip` | In-Class Mixing |
| `DAPR-2020--Core_Mixing/Sessions/Asam_Classical_Soloists-Jesu_Joy-Full.zip` | `DAPR-2020--Core_Mixing/Asam_Classical_Soloists-Jesu_Joy-Full.zip` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Sessions/Billy_Morgan_and_Friends-Nowhere-Full.zip` | `DAPR-2020--Core_Mixing/Focus_and_Balance/Billy_Morgan_and_Friends-Nowhere-Full.zip` | Focus & Balance |
| `DAPR-2020--Core_Mixing/Sessions/Blue_Lit_Moon-Full.zip` | `DAPR-2020--Core_Mixing/Delay_and_Stereo_Enhancements/Blue_Lit_Moon-Full.zip` | Delay & Stereo Enhancements |
| `DAPR-2020--Core_Mixing/Sessions/Jeff_Hirata-Sunshine-Full.zip` | `DAPR-2020--Core_Mixing/Final_Mix_and_Final_Exam/Jeff_Hirata-Sunshine-Full.zip` | Final Mix & Final Exam |
| `DAPR-2020--Core_Mixing/Sessions/North_To_Alaska-Full.zip` | `DAPR-2020--Core_Mixing/Master-Bus_Processing_and_Endgame/North_to_Alaska-Full.zip` | Master-Buss Processing & Endgame |
| `DAPR-2020--Core_Mixing/Sessions/Rod_Alexander-Tears_In_The_Rain-Full.zip` | `DAPR-2020--Core_Mixing/Rod_Alexander-Tears_in_the_Rain-Full.zip` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Sessions/Salon_8_Gokyuzu-Full.zip` | `DAPR-2020--Core_Mixing/Essential_Groundwork/Salon_8-Gokyuzu-Full.zip` | Essential Groundwork |
| `DAPR-2020--Core_Mixing/Sessions/Signe-Jakobsen-Full.zip` | `DAPR-2020--Core_Mixing/Final_Mix_and_Final_Exam/Signe_Jakobsen-Full.zip` | Final Mix & Final Exam |
| `DAPR-2020--Core_Mixing/Sessions/Strobe_Nostalgic_Full.zip` | `DAPR-2020--Core_Mixing/Essential_Groundwork/Strobe-Nostalgic-Full.zip` | Essential Groundwork |
| `DAPR-2020--Core_Mixing/Sessions/Swinging_Steaks-Lost_My_Way-Full.zip` | `DAPR-2020--Core_Mixing/Swinging_Steaks-Lost_My_Way-Full.zip` | NO MODULE REFERENCE |
| `DAPR-2020--Core_Mixing/Sessions/Triviul_ToSamRawfers_Full.zip` | `DAPR-2020--Core_Mixing/Essential_Groundwork/Triviul-To_Sam_Rawfers-Full.zip` | Essential Groundwork |
| `DAPR-2020--Core_Mixing/Templates/Mix_Space_Assessment-Template.xlsx` | `DAPR-2020--Core_Mixing/Mix_Space_Assessment_Template.xlsx` | NO MODULE REFERENCE |

## 6. Unresolved

None for this course.

## 7. Reference rewrite status

Every reference inside the `Classes/` tree of this repo has been rewritten to the new paths. What has **not** been rewritten:

- The Canvas cartridge for this course. That is the job this file exists for.
- Live Canvas pages. They only change when the rebuilt cartridge is imported.
- Files under `_briefs/` and `_superseded/`. Those are historical working notes and were left alone on purpose.
- `DAPR-2020--Core_Mixing--Image-Reference.html` at the course root, if one exists. It is a generated sheet and should be regenerated rather than patched.

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
