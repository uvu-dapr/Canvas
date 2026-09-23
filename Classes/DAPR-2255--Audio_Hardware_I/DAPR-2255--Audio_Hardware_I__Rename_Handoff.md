# DAPR-2255--Audio_Hardware_I — Rename Handoff

**Date:** 2026-09-22  
**Course folder:** `DAPR-2255--Audio_Hardware_I`  
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

**238 files.** Base URL: `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/`

| Old path | New path |
|---|---|
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-ac-vs-dc-traces.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/AC_vs_DC_Traces.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-ac-waveform.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/AC_Waveform.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-audio-ac-vs-power-ac.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Audio_AC_vs_Power_AC.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-audio-signal-levels.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Audio_Signal_Levels.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-battery-lamp-circuit-01.jpg` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Battery_Lamp_Circuit.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-bench-psu.jpg` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Bench_Psu.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-frequency-and-period.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Frequency_and_Period.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-frequency-worked-examples.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Frequency_Worked_Examples.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-nikola-tesla.jpg` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Nikola_Tesla.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-outlet-and-battery-02.jpg` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Outlet_and_Battery.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-peak-p2p-rms-voltage.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Peak_P2p_RMS_Voltage.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-polarity-phase-delay.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Polarity_Phase_Delay.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-power-sources-audio.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Power_Sources_Audio.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-sine-wave-parts.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Sine_Wave_Parts.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-thomas-edison.jpg` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Thomas_Edison.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-why-this-matters.png` | `DAPR-2255--Audio_Hardware_I/AC-DC_Electricity/Why_This_Matters.png` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Batteries/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-car-battery.jpg` | `DAPR-2255--Audio_Hardware_I/Batteries/Car_Battery.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-chemistries-audio.png` | `DAPR-2255--Audio_Hardware_I/Batteries/Chemistries_Audio.png` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-coin-cell.jpg` | `DAPR-2255--Audio_Hardware_I/Batteries/Coin_Cell.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-disposal-recycling-guide.png` | `DAPR-2255--Audio_Hardware_I/Batteries/Disposal_Recycling_Guide.png` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-galvanic-cell.jpg` | `DAPR-2255--Audio_Hardware_I/Batteries/Galvanic_Cell.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-history-timeline.png` | `DAPR-2255--Audio_Hardware_I/Batteries/History_Timeline.png` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-lithium-ion.jpg` | `DAPR-2255--Audio_Hardware_I/Batteries/Lithium_Ion.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-primary-cell-diagram.jpg` | `DAPR-2255--Audio_Hardware_I/Batteries/Primary_Cell_Diagram.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-runtime-estimation.png` | `DAPR-2255--Audio_Hardware_I/Batteries/Runtime_Estimation.png` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-studio-backup-power-reference.png` | `DAPR-2255--Audio_Hardware_I/Batteries/Studio_Backup_Power_Reference.png` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-symbol.png` | `DAPR-2255--Audio_Hardware_I/Batteries/Symbol.png` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-types-assorted.jpg` | `DAPR-2255--Audio_Hardware_I/Batteries/Types_Assorted.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-volta-portrait.jpg` | `DAPR-2255--Audio_Hardware_I/Batteries/Volta_Portrait.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-voltaic-pile.jpg` | `DAPR-2255--Audio_Hardware_I/Batteries/Voltaic_Pile.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-zinc-carbon-diagram.jpg` | `DAPR-2255--Audio_Hardware_I/Batteries/Zinc_Carbon_Diagram.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Capacitors/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-axial.jpg` | `DAPR-2255--Audio_Hardware_I/Capacitors/Axial.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-ceramic-3-digit-code.png` | `DAPR-2255--Audio_Hardware_I/Capacitors/Ceramic_3_Digit_Code.png` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-ceramic.jpg` | `DAPR-2255--Audio_Hardware_I/Capacitors/Ceramic.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-charging-graph.jpg` | `DAPR-2255--Audio_Hardware_I/Capacitors/Charging_Graph.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-electrolytic-aluminum.png` | `DAPR-2255--Audio_Hardware_I/Capacitors/Electrolytic_Aluminum.png` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-film-cap.jpg` | `DAPR-2255--Audio_Hardware_I/Capacitors/Film_Cap.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-history-timeline.png` | `DAPR-2255--Audio_Hardware_I/Capacitors/History_Timeline.png` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-leyden-jar.png` | `DAPR-2255--Audio_Hardware_I/Capacitors/Leyden_Jar.png` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-pass-ac-frequency-dependent.png` | `DAPR-2255--Audio_Hardware_I/Capacitors/Pass_AC_Frequency_Dependent.png` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-rc-filter.jpg` | `DAPR-2255--Audio_Hardware_I/Capacitors/Rc_Filter.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-supercap.jpg` | `DAPR-2255--Audio_Hardware_I/Capacitors/Supercap.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Capacitors/Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-types-in-audio-circuits.png` | `DAPR-2255--Audio_Hardware_I/Capacitors/Types_in_Audio_Circuits.png` |
| `DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-various-types.jpg` | `DAPR-2255--Audio_Hardware_I/Capacitors/Various_Types.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-1n4001-diode.jpg` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/1n4001_Diode.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-braun-portrait.jpg` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Braun_Portrait.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-bridge-rectifier.jpg` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Bridge_Rectifier.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-cathode-band-and-symbol.png` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Cathode_Band_and_Symbol.png` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-colors.png` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Colors.png` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-diode-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Diode_Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-led-circuit-01.png` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/LED_Circuit.png` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-photodiode-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Photodiode_Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-protection-circuits-diagram.png` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Protection_Circuits_Diagram.png` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-rgb-led.jpg` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Rgb_LED.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-schottky-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Schottky_Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-zener-photo.jpg` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Zener_Photo.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-zener-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Zener_Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-air-coil.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Air_Coil.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-assorted-inductors.png` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Assorted_Inductors.png` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-audio-voltage-current-impedance.png` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Audio_Voltage_Current_Impedance.png` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-chip-inductor-internal-structure.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Chip_Inductor_Internal_Structure.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-choke.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Choke.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-faraday-portrait.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Faraday_Portrait.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-ferrite-bead-cable.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Ferrite_Bead_Cable.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-ferrite-bead.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Ferrite_Bead.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-pcb-transformer.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Pcb_Transformer.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-power-xfmr.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Power_Xfmr.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-toroidal-xfmr.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Toroidal_Xfmr.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-toroidal.jpg` | `DAPR-2255--Audio_Hardware_I/Inductors_and_Transformers/Toroidal.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-1-vs-2-resolution-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/1_vs_2_Resolution.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-audio-midi-setup-midi-studio.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Audio_MIDI_Setup_MIDI_Studio.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-cc-to-dmx-scaling-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Cc_to_DMX_Scaling.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-clock-vs-mtc-02.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Clock_vs_MTC.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-device-gm-mmc-properties-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Device_GM_Mmc_Properties.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-din-5-pin-female-jack.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Din_5_Pin_Female_Jack.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-din-5-pin-male-plug.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Din_5_Pin_Male_Plug.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-din-cable-seated-in-jack-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Din_Cable_Seated_in_Jack.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-din-connector-face-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Din_Connector_Face.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-dmx-fixture-02.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/PAR_Fixture_Showing_DIP_Switch_Bank.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-dmx-fixture-03.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/PAR_Fixture_on_Double_Yoke_Bracket.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-gm-channel-10-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/GM_Channel_10.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-interface-rear-panel-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Interface_Rear_Panel.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-jitter-buffer-tradeoff-02.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Jitter_Buffer_Tradeoff.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-keyboard-controller-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Keyboard_Controller.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-local-control-double-trigger-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Local_Control_Double_Trigger.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-managed-switch-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Managed_Switch.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-monitor-window-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Monitor_Window.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-msc-device-id-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Msc_Device_Id.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-network-midi-preferences-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Network_MIDI_Preferences.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-note-on-note-off-timeline-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Note_on_Note_Off_Timeline.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-osc-din-beside-ethernet-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Osc_Din_Beside_Ethernet.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-qlab-cue-list-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Qlab_Cue_List.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-rack-sound-module-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Rack_Sound_Module.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-rtp-two-interfaces-one-cable-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Rtp_Two_Interfaces_One_Cable.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-same-file-two-synths-02.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Same_File_Two_Synths.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-serial-vs-network-transport-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Serial_vs_Network_Transport.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-test-kit-layout-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Test_Kit_Layout.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-thru-box-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Thru_Box.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-thru-chain-vs-thru-box-01.png` | `DAPR-2255--Audio_Hardware_I/MIDI/Thru_Chain_vs_Thru_Box.png` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-troubleshooting-cable-pulled-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Troubleshooting_Cable_Pulled.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-trs-type-a-vs-type-b-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/Trs_Type_a_vs_Type_B.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-usb-b-cable-end-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/USB_B_Cable_End.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-usb-c-instrument-rear-01.jpg` | `DAPR-2255--Audio_Hardware_I/MIDI/USB_C_Instrument_Rear.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/midi/midi-what-midi-carries-02.png` | `DAPR-2255--Audio_Hardware_I/MIDI/What_MIDI_Carries.png` |
| `DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-analog-meter.jpg` | `DAPR-2255--Audio_Hardware_I/Multimeters/Analog_Meter.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Multimeters/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-clamp-meter.jpg` | `DAPR-2255--Audio_Hardware_I/Multimeters/Clamp_Meter.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-digital-meter.jpg` | `DAPR-2255--Audio_Hardware_I/Multimeters/Digital_Meter.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-jack-selection-01.jpg` | `DAPR-2255--Audio_Hardware_I/Multimeters/Jack_Selection.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-oersted-portrait.jpg` | `DAPR-2255--Audio_Hardware_I/Multimeters/Oersted_Portrait.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-oscilloscope.jpg` | `DAPR-2255--Audio_Hardware_I/Multimeters/Oscilloscope.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-overview-hero.png` | `DAPR-2255--Audio_Hardware_I/Multimeters/Overview_Hero.png` |
| `DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-test-leads.jpg` | `DAPR-2255--Audio_Hardware_I/Multimeters/Test_Leads.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-wheatstone-bridge.jpg` | `DAPR-2255--Audio_Hardware_I/Multimeters/Wheatstone_Bridge.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ohms-law/ohms-law-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Ohms_Law/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ohms-law/ohms-law-circuit-diagram.png` | `DAPR-2255--Audio_Hardware_I/Ohms_Law/Circuit_Diagram.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ohms-law/ohms-law-georg-ohm-portrait.jpg` | `DAPR-2255--Audio_Hardware_I/Ohms_Law/Georg_Ohm_Portrait.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ohms-law/ohms-law-overview-hero.png` | `DAPR-2255--Audio_Hardware_I/Ohms_Law/Overview_Hero.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ohms-law/ohms-law-potentiometer.jpg` | `DAPR-2255--Audio_Hardware_I/Ohms_Law/Potentiometer.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ohms-law/ohms-law-voltage-divider.jpg` | `DAPR-2255--Audio_Hardware_I/Ohms_Law/Voltage_Divider.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/ohms-law/ohms-law-wheel-basic.png` | `DAPR-2255--Audio_Hardware_I/Ohms_Law/Wheel_Basic.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ohms-law/ohms-law-wheel-colorcoded-numbers.png` | `DAPR-2255--Audio_Hardware_I/Ohms_Law/Wheel_Colorcoded_Numbers.png` |
| `DAPR-2255--Audio_Hardware_I/Images/ohms-law/ohms-law-wheel-colorcoded.png` | `DAPR-2255--Audio_Hardware_I/Ohms_Law/Wheel_Colorcoded.png` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-amplifier-specs-infographic.png` | `DAPR-2255--Audio_Hardware_I/Power/Amplifier_Specs_Infographic.png` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Power/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-doubling-is-3db-01.png` | `DAPR-2255--Audio_Hardware_I/Power/Doubling_is_3dB.png` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-heatsink-amplifier-chassis-01.jpg` | `DAPR-2255--Audio_Hardware_I/Power/Heatsink_Amplifier_Chassis.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-heatsink-cpu-cooler-01.jpg` | `DAPR-2255--Audio_Hardware_I/Power/Heatsink_Cpu_Cooler.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-heatsink-to220-pair.jpg` | `DAPR-2255--Audio_Hardware_I/Power/Heatsink_To220_Pair.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-heatsink-why-fins-work-02.png` | `DAPR-2255--Audio_Hardware_I/Power/Heatsink_Why_Fins_Work.png` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-heatsink.jpg` | `DAPR-2255--Audio_Hardware_I/Power/Heatsink.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-james-watt-portrait.jpg` | `DAPR-2255--Audio_Hardware_I/Power/James_Watt_Portrait.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-joule-portrait.jpg` | `DAPR-2255--Audio_Hardware_I/Power/Joule_Portrait.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-watt-steam-engine.jpg` | `DAPR-2255--Audio_Hardware_I/Power/Watt_Steam_Engine.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/power/power-wattmeter.jpg` | `DAPR-2255--Audio_Hardware_I/Power/Wattmeter.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Resistors/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-assorted-types.jpg` | `DAPR-2255--Audio_Hardware_I/Resistors/Assorted_Types.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-audio-applications-infographic.png` | `DAPR-2255--Audio_Hardware_I/Resistors/Audio_Applications_Infographic.png` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-color-code-png.png` | `DAPR-2255--Audio_Hardware_I/Resistors/Color_Code_Png.png` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-four-band-worked.png` | `DAPR-2255--Audio_Hardware_I/Resistors/Four_Band_Worked.png` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-in-circuit-parallel-path-01.jpg` | `DAPR-2255--Audio_Hardware_I/Resistors/In_Circuit_Parallel_Path.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-ldr.jpg` | `DAPR-2255--Audio_Hardware_I/Resistors/Ldr.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-pcb-resistor.jpg` | `DAPR-2255--Audio_Hardware_I/Resistors/Pcb_Resistor.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-potentiometer-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Resistors/Potentiometer_Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-power-ratings.jpg` | `DAPR-2255--Audio_Hardware_I/Resistors/Power_Ratings.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-smd-resistors.jpg` | `DAPR-2255--Audio_Hardware_I/Resistors/Smd_Resistors.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-symbol-ansi.jpg` | `DAPR-2255--Audio_Hardware_I/Resistors/Symbol_Ansi.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-symbol-iec.jpg` | `DAPR-2255--Audio_Hardware_I/Resistors/Symbol_Iec.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Schematics/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-breadboard-circuit.jpg` | `DAPR-2255--Audio_Hardware_I/Schematics/Breadboard_Circuit.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-circuit-board-detail.jpg` | `DAPR-2255--Audio_Hardware_I/Schematics/Circuit_Board_Detail.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-connector-jack-symbol-01.png` | `DAPR-2255--Audio_Hardware_I/Schematics/Connector_Jack_Symbol.png` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-fuse-symbol-01.png` | `DAPR-2255--Audio_Hardware_I/Schematics/Fuse_Symbol.png` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-ground-symbols.jpg` | `DAPR-2255--Audio_Hardware_I/Schematics/Ground_Symbols.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-loudspeaker-symbol-01.png` | `DAPR-2255--Audio_Hardware_I/Schematics/Loudspeaker_Symbol.png` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-microphone-symbol-01.png` | `DAPR-2255--Audio_Hardware_I/Schematics/Microphone_Symbol.png` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-opamp-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Schematics/Opamp_Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-pcb-photo.jpg` | `DAPR-2255--Audio_Hardware_I/Schematics/Pcb_Photo.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-reference-designators.png` | `DAPR-2255--Audio_Hardware_I/Schematics/Reference_Designators.png` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-voltage-source.jpg` | `DAPR-2255--Audio_Hardware_I/Schematics/Voltage_Source.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-wire-junction.png` | `DAPR-2255--Audio_Hardware_I/Schematics/Wire_Junction.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-circuit-schematic.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Circuit_Schematic.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-kcl.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Kcl.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-kirchhoff-portrait.jpg` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Kirchhoff_Portrait.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-kirchhoffs-laws.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Kirchhoffs_Laws.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-kvl.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Kvl.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-loaded-voltage-divider.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Loaded_Voltage_Divider.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-parallel-formula.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Parallel_Formula.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-parallel-resistor-example.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Parallel_Resistor_Example.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-parallel.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Parallel.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-series-example.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Series_Example.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-series-voltage-drops.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Series_Voltage_Drops.png` |
| `DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-voltage-divider-infographic.png` | `DAPR-2255--Audio_Hardware_I/Series-Parallel/Voltage_Divider_Infographic.png` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-3pdt-toggle-photo.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/3pdt_Toggle_Photo.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-dip-switch.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Dip_Switch.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-dpdt-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Dpdt_Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-dpst-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Dpst_Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-evolution-of-switching.png` | `DAPR-2255--Audio_Hardware_I/Switches/Evolution_of_Switching.png` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-push-button-box.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Push_Button_Box.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-pushbutton-sparkfun.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Pushbutton_Sparkfun.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-relay-schematic-symbols.png` | `DAPR-2255--Audio_Hardware_I/Switches/Relay_Schematic_Symbols.png` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-rocker-switch.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Rocker_Switch.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-rotary-switch.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Rotary_Switch.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-slide-switch.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Slide_Switch.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-spdt-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Spdt_Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-spst-symbol.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Spst_Symbol.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-talkback-box-switches.png` | `DAPR-2255--Audio_Hardware_I/Switches/Talkback_Box_Switches.png` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-throws-and-poles.png` | `DAPR-2255--Audio_Hardware_I/Switches/Throws_and_Poles.png` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-toggle-switch-photo.png` | `DAPR-2255--Audio_Hardware_I/Switches/Toggle_Switch_Photo.png` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-types-in-audio-equipment.png` | `DAPR-2255--Audio_Hardware_I/Switches/Types_in_Audio_Equipment.png` |
| `DAPR-2255--Audio_Hardware_I/Images/switches/switches-wiring-diagrams.jpg` | `DAPR-2255--Audio_Hardware_I/Switches/Wiring_Diagrams.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/syllabus/syllabus-bench-overview-01.jpg` | `DAPR-2255--Audio_Hardware_I/Syllabus/Bench_Overview.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-amplifier-circuit.jpg` | `DAPR-2255--Audio_Hardware_I/Transistors/Amplifier_Circuit.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-applications-in-audio.png` | `DAPR-2255--Audio_Hardware_I/Transistors/Applications_in_Audio.png` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Transistors/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-assorted-types.png` | `DAPR-2255--Audio_Hardware_I/Transistors/Assorted_Types.png` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-bell-labs-inventors.jpg` | `DAPR-2255--Audio_Hardware_I/Transistors/Bell_Labs_Inventors.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-bjt-vs-fet-audio.png` | `DAPR-2255--Audio_Hardware_I/Transistors/BJT_vs_Fet_Audio.png` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-fet-symbols.jpg` | `DAPR-2255--Audio_Hardware_I/Transistors/Fet_Symbols.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-first-transistor-replica.jpg` | `DAPR-2255--Audio_Hardware_I/Transistors/First_Transistor_Replica.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-first-transistor-to-microprocessor.png` | `DAPR-2255--Audio_Hardware_I/Transistors/First_Transistor_to_Microprocessor.png` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-heatsink.png` | `DAPR-2255--Audio_Hardware_I/Transistors/Heatsink.png` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-inside-integrated-circuits.png` | `DAPR-2255--Audio_Hardware_I/Transistors/Inside_Integrated_Circuits.png` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-npn-pnp-symbols.png` | `DAPR-2255--Audio_Hardware_I/Transistors/Npn_Pnp_Symbols.png` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-three-bjt-amplifier-configs.png` | `DAPR-2255--Audio_Hardware_I/Transistors/Three_BJT_Amplifier_Configs.png` |
| `DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-to92-package.png` | `DAPR-2255--Audio_Hardware_I/Transistors/To92_Package.png` |
| `DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-breadboard-circuit-01.jpg` | `DAPR-2255--Audio_Hardware_I/Voltage-Current/Breadboard_Circuit.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-complete-path-01.png` | `DAPR-2255--Audio_Hardware_I/Voltage-Current/Complete_Path.png` |
| `DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-conventional-vs-electron-flow-01.png` | `DAPR-2255--Audio_Hardware_I/Voltage-Current/Conventional_vs_Electron_Flow.png` |
| `DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-orders-of-magnitude-01.png` | `DAPR-2255--Audio_Hardware_I/Voltage-Current/Orders_of_Magnitude.png` |
| `DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-reservoir-analogy-02.png` | `DAPR-2255--Audio_Hardware_I/Voltage-Current/Reservoir_Analogy.png` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-assignment-bench-01.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Assignment_Bench.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-awg-wire-gauge-chart.png` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/AWG_Wire_Gauge_Chart.png` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-breadboard-photo.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Breadboard_Photo.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-breadboard.png` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Breadboard.png` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-cable-insulation-materials.png` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Cable_Insulation_Materials.png` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-conductor-progression-01.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Conductor_Progression.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-current-path-through-body-01.png` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Current_Path_Through_Body.png` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-esd-wrist-strap.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Esd_Wrist_Strap.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-flux.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Flux.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-footswitch.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Footswitch.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-good-vs-cold-solder-joint.png` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Good_vs_Cold_Solder_Joint.png` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-heat-shrink.png` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Heat_Shrink.png` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-helping-hands.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Helping_Hands.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-overview-hero.png` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Overview_Hero.png` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-solder-wire.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Solder_Wire.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-soldering-iron.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Soldering_Iron.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-wire-stripper-photo.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Wire_Stripper_Photo.jpg` |
| `DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-wire-stripper.jpg` | `DAPR-2255--Audio_Hardware_I/Wiring_Safety/Wire_Stripper.jpg` |

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
- `DAPR-2255--Audio_Hardware_I--Image-Reference.html` at the course root, if one exists. It is a generated sheet and should be regenerated rather than patched.

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
