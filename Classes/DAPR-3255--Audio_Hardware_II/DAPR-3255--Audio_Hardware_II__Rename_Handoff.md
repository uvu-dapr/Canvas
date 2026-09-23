# DAPR-3255--Audio_Hardware_II — Rename Handoff

**Date:** 2026-09-22  
**Course folder:** `DAPR-3255--Audio_Hardware_II`  
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

**122 files.** Base URL: `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/`

| Old path | New path |
|---|---|
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-aes50-point-to-point-chain-01.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Daisy_Chained_Boxes_and_No_Switch.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-aes50-point-to-point-chain-02.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Four_Blue_Cubes_Linked_in_Line.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-aes67-interoperability-overlap-01.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Three_Circle_Venn_With_Shared_Center.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-aes67-interoperability-overlap-02.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Overlapping_Translucent_Colored_Spheres.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-avb-milan-reserved-bandwidth-01.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Split_Bandwidth_Bar_Above_Switch_Row.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-avb-milan-reserved-bandwidth-02.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Cutaway_Pipe_With_Green_Core.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-dante-network-topology-01.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Star_Wired_Devices_With_Subscription_Arrows.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-dante-network-topology-02.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Isometric_Hub_With_Glowing_Arcs.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-ndi-bandwidth-tiers-01.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Descending_Labeled_Bandwidth_Bars.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-ndi-bandwidth-tiers-02.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Three_Pipes_of_Decreasing_Diameter.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-protocol-comparison-matrix-01.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Scatter_Plot_of_Latency_and_Channels.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-protocol-comparison-matrix-02.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Colored_Spheres_on_Grid_Plane.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-protocol-osi-layer-map-01.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Layer_Bars_With_Protocol_Pills.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-protocol-osi-layer-map-02.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Exploded_Slabs_With_White_Markers.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-smpte-2110-essence-separation-01.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Source_Splitting_into_Three_Streams.png` |
| `DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-smpte-2110-essence-separation-02.png` | `DAPR-3255--Audio_Hardware_II/Audio_Protocols/Black_Block_With_Three_Segmented_Cables.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-ac-vs-dc-waveform-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Flat_Line_and_Sine_Graphs.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-ac-vs-dc-waveform-02.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Straight_and_Wavy_Extruded_Ribbons.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-bjt-voltage-divider-bias-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Transistor_Schematic_With_Four_Resistors.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-bjt-voltage-divider-bias-02.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Rendered_Resistors_and_Transistor_Disc.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-breadboard-internal-connections-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Breadboard_Internal_Connections.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-capacitor-electrolytic-cutaway-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Capacitor_Electrolytic_Cutaway.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-constant-q-against-proportional-q-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Constant_Q_Against_Proportional_Q.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-current-path-through-body-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Current_Path_Through_Body.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-electrical-safety-current-path-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Body_Outlines_With_Current_Paths.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-electrical-safety-current-path-02.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Grey_Mannequins_With_Glowing_Paths.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-filter-alignments-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Sharp_Knee_Rolloff_Curve_Trio.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-filter-alignments-02.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Early_Peaking_Gradual_Rolloff_Curves.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-filter-q-against-bandwidth-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Filter_Q_Against_Bandwidth.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-frequency-scaling-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Frequency_Scaling.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-good-vs-cold-solder-joint-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Good_vs_Cold_Solder_Joint.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-opamp-inverting-vs-noninverting-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Two_Labeled_Amplifier_Schematics.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-opamp-inverting-vs-noninverting-02.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Rendered_Triangles_With_Banded_Resistors.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-opamp-inverting-vs-noninverting-03.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Rendered_Triangles_With_Tan_Resistors.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-opamp-summing-amplifier-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Virtual_Ground_Node_and_Three_Inputs.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-opamp-summing-amplifier-02.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Red_Node_Merging_Rendered_Resistor_Inputs.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-parametric-eq-boost-and-cut-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Parametric_EQ_Boost_and_Cut.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-peak-p2p-rms-voltage-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Peak_P2p_RMS_Voltage.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-resistors-assorted-types-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Resistors_Assorted_Types.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-rms-peak-peak-to-peak-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Sine_Wave_With_Amplitude_Reference_Lines.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-rms-peak-peak-to-peak-02.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Wave_Ribbon_With_Measurement_Arrows.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-semiconductor-pn-junction-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Doped_Blocks_and_Depletion_Gap.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-semiconductor-pn-junction-02.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Rendered_Slab_With_Bubbles_and_Spheres.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-solder-joint-macro-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Solder_Joint_Macro.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-symbol-battery-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Battery.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-symbol-capacitor-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Capacitor.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-symbol-diode-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Diode.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-symbol-fet-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Fet.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-symbol-ground-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Ground.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-symbol-inductor-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Inductor.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-symbol-opamp-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Opamp.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-symbol-resistor-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Resistor.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-symbol-switch-spst-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Switch_Spst.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-symbol-transformer-01.png` | `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Transformer.png` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-talkback-box-assembled-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Talkback_Box_Assembled.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-talkback-box-din-solder-joints-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Talkback_Box_Din_Solder_Joints.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-talkback-box-internal-wiring-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Close_Up_of_Soldered_Connector_Lugs.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-talkback-box-internal-wiring-02.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Aluminum_Panel_With_Three_Connectors.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-talkback-box-kit-contents-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Talkback_Box_Kit_Contents.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-talkback-box-panel-connectors-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Talkback_Box_Panel_Connectors.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-three-bjt-amplifier-configs-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Three_BJT_Amplifier_Configs.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-xlr-female-pin-numbering-01.jpg` | `DAPR-3255--Audio_Hardware_II/Electronics/Xlr_Female_Pin_Numbering.jpg` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-cidr-block-sizes-01.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Prefix_Table_and_Tapering_Triangle.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-cidr-block-sizes-02.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Row_of_Shrinking_Blue_Cubes.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-ipv4-address-anatomy-01.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Octet_Boxes_With_Network_Host_Braces.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-ipv4-address-anatomy-02.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Three_Blue_Blocks_and_One_Green.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-ipv6-address-anatomy-01.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Segmented_Bar_Over_Hexadecimal_Address.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-ipv6-address-anatomy-02.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Three_Segment_Extruded_Bar.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-nat-translation-flow-01.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Host_and_Cloud_Across_Translation_Box.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-nat-translation-flow-02.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Rendered_Packets_Changing_Color_Midstream.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-private-address-ranges-01.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Labeled_Range_Bars_of_Increasing_Length.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-private-address-ranges-02.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Three_Extruded_Bars_Increasing_in_Length.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-subnet-mask-bit-boundary-01.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Stacked_Bars_Split_into_Usable_Halves.png` |
| `DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-subnet-mask-bit-boundary-02.png` | `DAPR-3255--Audio_Hardware_II/IP_Addressing/Rendered_Bars_Divided_into_Equal_Pieces.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-igmp-snooping-effect-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Flooded_Versus_Selective_Port_Delivery.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-igmp-snooping-effect-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Red_and_Green_Columns_Under_Bars.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-multicast-vs-unicast-flow-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Four_Copies_Versus_One_Branch.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-multicast-vs-unicast-flow-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Tube_Bundle_Beside_Branching_Stem.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-ptp-clock-hierarchy-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Three_Tier_Clock_Tree.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-ptp-clock-hierarchy-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Red_Cube_Above_Orange_and_Grey.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-qos-dscp-priority-queue-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Funnel_Sorting_Packets_into_Queues.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-qos-dscp-priority-queue-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Wedge_Merging_Four_Cube_Rows.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-trunk-port-tagging-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Tagged_Frames_on_Link_Between_Switches.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-trunk-port-tagging-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Cube_Chain_With_Yellow_Tags.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-vlan-segmentation-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/One_Switch_and_Dashed_Divider.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-vlan-segmentation-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Architecture/Red_Wall_Separating_Green_and_Blue.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-configuration/network-configuration-dhcp-four-step-handshake-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Configuration/Client_and_Server_Four_Message_Exchange.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-configuration/network-configuration-dhcp-four-step-handshake-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Configuration/Alternating_Arrows_Between_Two_Posts.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-configuration/network-configuration-dns-resolution-chain-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Configuration/Box_Chain_With_Return_Arc.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-configuration/network-configuration-dns-resolution-chain-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Configuration/Rounded_Cubes_and_Orange_Arrows.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-configuration/network-configuration-managed-vs-unmanaged-switch-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Configuration/Managed_vs_Unmanaged_Switch.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-configuration/network-configuration-static-vs-dhcp-assignment-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Configuration/Hand_Labeled_Devices_Versus_Central_Server.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-configuration/network-configuration-static-vs-dhcp-assignment-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Configuration/Separate_Knobs_Versus_Shared_Manifold.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-arp-resolution-sequence-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Broadcast_Question_and_Single_Reply.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-arp-resolution-sequence-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Fanned_Orange_Arrows_and_Green_Return.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-arp-resolution-sequence-03.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Wide_Source_Block_With_Converging_Arrows.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-capture-point-placement-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Inline_Tap_and_Mirror_Port_Wiring.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-capture-point-placement-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Block_Clusters_With_Tube_Junctions.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-diagnostic-ladder-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Six_Rung_Ladder_With_Tool_Labels.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-diagnostic-ladder-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Staircase_of_Six_Colored_Slabs.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-mirror-against-tap-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Mirror_Against_Tap.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-ping-round-trip-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Echo_Request_and_Reply_Timing.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-ping-round-trip-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Opposing_Arrows_and_Vertical_Measure.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-traceroute-hop-discovery-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Expanding_Arrows_Halting_Along_Hop_Chain.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-traceroute-hop-discovery-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Green_Arrows_Bursting_Against_Posts.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-troubleshooting-decision-tree-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Flowchart_of_Diamonds_and_Outcomes.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-troubleshooting-decision-tree-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Diagnostics/Blue_Diamonds_Branching_to_Grey_Blocks.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-analog-snake-vs-network-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/Analog_Snake_vs_Network.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-layer2-switch-frame-forwarding-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/Switch_Table_and_Forwarded_Path.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-layer2-switch-frame-forwarding-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/Green_Pipe_Arching_Between_Cubes.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-layer3-router-between-subnets-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/Two_Subnet_Groups_and_Central_Router.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-layer3-router-between-subnets-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/Orange_Sphere_Bridging_Two_Plates.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-osi-seven-layer-stack-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/Seven_Colored_Layers_Labeled_in_Order.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-osi-seven-layer-stack-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/Exploded_Stack_of_Seven_Slabs.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-straight-through-vs-crossover-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/Straight_Through_vs_Crossover.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-t568a-t568b-pin-order-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/T568a_T568b_Pin_Order.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-tcp-vs-udp-comparison-01.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/Two_Arrow_Ladders_With_Dropped_Packet.png` |
| `DAPR-3255--Audio_Hardware_II/Images/network-foundations/network-foundations-tcp-vs-udp-comparison-02.png` | `DAPR-3255--Audio_Hardware_II/Network__Foundations/Cube_Tray_With_Missing_Piece.png` |
| `DAPR-3255--Audio_Hardware_II/Images/wireless/wireless-antenna-patterns-01.png` | `DAPR-3255--Audio_Hardware_II/Wireless/Antenna_Patterns.png` |
| `DAPR-3255--Audio_Hardware_II/Images/wireless/wireless-microphone-against-iem-direction-01.png` | `DAPR-3255--Audio_Hardware_II/Wireless/Microphone_Against_Iem_Direction.png` |
| `DAPR-3255--Audio_Hardware_II/Images/wireless/wireless-multipath-null-and-diversity-01.png` | `DAPR-3255--Audio_Hardware_II/Wireless/Multipath_Null_and_Diversity.png` |
| `DAPR-3255--Audio_Hardware_II/Images/wireless/wireless-third-order-intermodulation-01.png` | `DAPR-3255--Audio_Hardware_II/Wireless/Third_Order_Intermodulation.png` |

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
- `DAPR-3255--Audio_Hardware_II--Image-Reference.html` at the course root, if one exists. It is a generated sheet and should be regenerated rather than patched.

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
