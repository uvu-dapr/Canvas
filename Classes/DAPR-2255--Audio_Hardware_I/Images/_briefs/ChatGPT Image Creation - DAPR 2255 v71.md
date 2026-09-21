# DAPR 2255 Image Brief - v71, rewritten photorealistic
Generated 2026-09-21. Run each prompt separately in ChatGPT. Save each result
with the exact filename shown, into the exact folder shown. Do not rename.

## What changed, and why this brief looks nothing like the last one

Standards 20.5 used to lock every generated image to "flat vector-style illustration,
clean line weights, no gradients, no drop shadows, no 3D, no photorealism." Adam never set
that line and does not want it. It is what produced the thin line art and the stick figure
on the electric-shock page. **It was removed program wide on 2026-09-21** and replaced with
new 20.5a: photorealistic is the house style for every course.

Three rules come out of that, and they are why every prompt below reads differently.

**1. Most of these are now photographs.** Twenty of the 30 are photorealistic studio shots
of real components on a real bench: resistors with their bands showing, a lit LED on a
breadboard, a heat sink with a device bolted to it, a tray of tools. Those are JPEGs on their
own background, not transparent PNGs, because a photograph's lighting and shadow are part of
the picture and cannot be lifted off.

**2. No text inside any image.** Every one of the twelve defects in the last batch was a text
defect: a label clipped by the frame, two labels printed over each other, a label silently
dropped. Not one was a drawing problem. So the prompts now forbid text outright, in a
paragraph near the end that is deliberately blunt. The page already carries the heading, the
caption, the table and the prose.

**3. What cannot be photographed is rendered, not drawn.** A status byte is not a thing. A
VLAN is not a thing. Those 10 become richly rendered dimensional diagrams: solid isometric
shapes with depth, shading and contact shadows, on a transparent background. Still not thin
line drawings.

**One limit did not change, and it matters.** 20.1 rule 3 still stands: real hardware and
real software are never generated. Photorealistic is a style, not permission to invent a
front panel. Nothing below asks for a connector face with numbered pins, a named product, a
silkscreened panel or a software window. Every prompt ends with a paragraph forbidding
exactly that, because a photorealistic render of a wrong DIN pinout would be more convincing
and just as wrong as the flat one we already found.

## Two images from the last brief are gone on purpose

| Was | Why it is not here |
|---|---|
| `midi-osc-address-anatomy` | The picture was a line of text with three labels under it. That is not an image, it is a code block. It belongs on the page as styled HTML, where it can be copied, searched and corrected without regenerating anything. |
| `voltage-current-what-to-watch-for` | That page is the Watch page. The video is the medium. An image listing what to watch for is filler, and 8.1 says filler does not get briefed. |

Both pages get HTML from me in the next build instead.

## The list

| # | Kind | File | Page |
|---|---|---|---|
| 01 | photo | `ac-dc-electricity-outlet-and-battery-01.jpg` | AC & DC: Overview |
| 02 | rendered | `midi-1-vs-2-resolution-02.png` | MIDI: MIDI 2 0 What Changed and Why It Matters |
| 03 | rendered | `midi-cc-to-dmx-scaling-02.png` | MIDI: MIDI to DMX Integration and Conversion |
| 04 | rendered | `midi-local-control-double-trigger-02.png` | MIDI: Device Roles Interfaces and Signal Flow |
| 05 | rendered | `midi-msc-device-id-02.png` | MIDI: MIDI Show Control Protocol |
| 06 | rendered | `midi-note-on-note-off-timeline-02.png` | MIDI: Channel Voice Messages and Musical Control |
| 07 | photo | `resistors-in-circuit-parallel-path-02.jpg` | Resistors: Measuring Resistance |
| 08 | rendered | `midi-serial-vs-network-transport-02.png` | MIDI: Over USB and Network |
| 09 | rendered | `midi-thru-chain-vs-thru-box-02.png` | MIDI: Routing Channelization and Thru Management |
| 10 | rendered | `power-doubling-is-3db-02.png` | Power: Power in Decibels - dBW & dBm |
| 11 | rendered | `wiring-safety-current-path-through-body-02.png` | Wiring & Safety: Electric Shock and the Human Body |
| 12 | photo | `ac-dc-electricity-battery-lamp-circuit-01.jpg` | AC & DC: What Is Direct Current? |
| 13 | photo | `voltage-current-breadboard-circuit-01.jpg` | Voltage & Current: Overview Basic Electronics: Voltage and Current |
| 14 | rendered | `voltage-current-orders-of-magnitude-01.png` | Voltage & Current: The Numbers You Will Actually See |
| 15 | photo | `wiring-safety-conductor-progression-01.jpg` | Wiring & Safety: History - Electrical Safety Standards |
| 16 | photo | `syllabus-bench-overview-01.jpg` | DAPR 2255 Audio Hardware I: Syllabus |
| 17 | photo | `ohms-law-assignment-bench-01.jpg` | Ohm's Law: Assignment - Applying V = IR |
| 18 | photo | `resistors-assignment-bench-01.jpg` | Resistors: Assignment - Color Codes, Power, & Audio Applications |
| 19 | photo | `series-parallel-assignment-bench-01.jpg` | Series & Parallel Circuits: Assignment - Circuit Analysis & Audio Applications |
| 20 | photo | `multimeters-assignment-bench-01.jpg` | Multimeters: Assignment - Reading & Interpreting Measurements |
| 21 | photo | `power-assignment-bench-01.jpg` | Power: Assignment - Power Calculations & Amplifier Matching |
| 22 | photo | `batteries-assignment-bench-01.jpg` | Batteries: Assignment - Battery Selection & Runtime Calculations |
| 23 | photo | `diodes-leds-assignment-bench-01.jpg` | Diodes & LEDs: Assignment - Applying Diode & LED Principles |
| 24 | photo | `transistors-assignment-bench-01.jpg` | Transistors: Assignment - Applying BJT & FET Concepts |
| 25 | photo | `capacitors-assignment-bench-01.jpg` | Capacitors: Assignment - Markings, Reactance, & Audio Applications |
| 26 | photo | `inductors-transformers-assignment-bench-01.jpg` | Inductors & Transformers: Assignment - Turns Ratios, Reactance, & Audio Applications |
| 27 | photo | `switches-assignment-bench-01.jpg` | Switches: Assignment - Selecting & Wiring Audio Switches |
| 28 | photo | `schematics-assignment-bench-01.jpg` | Schematics: Assignment - Symbols, Conventions, & Signal Tracing |
| 29 | photo | `wiring-safety-assignment-bench-01.jpg` | Wiring & Safety: Assignment - Cable, Solder, & Component Safety |
| 30 | photo | `ac-dc-electricity-assignment-bench-01.jpg` | AC & DC: Assignment - Sine Waves, RMS, & Signal Levels |

**One folder does not exist yet** and is created by the first save into it:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/syllabus
```

---

## Image 01 - Outlet and battery

| Field | Value |
|---|---|
| Filename | `ac-dc-electricity-outlet-and-battery-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-outlet-and-battery-01.jpg` |
| Used on | Canvas page `AC & DC: Overview` |
| Alt text | `A mains wall outlet lying beside a nine volt battery and a pair of alkaline cells on a bench` |
| Caption | `Figure 1. Alternating current comes out of the wall. Direct current comes out of a cell. Nearly everything in this course runs on the second one.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

A plain white mains wall outlet, removed from the wall and lying face up on the LEFT side of
the frame, its two sockets clearly visible, a short length of stripped three-conductor cable
still attached and coiled behind it.

On the RIGHT side of the frame, a rectangular nine volt battery standing upright on its
terminals, with two cylindrical alkaline cells lying on their sides beside it.

A clear, deliberate gap of empty background between the left group and the right group, so the
image reads as two things being compared rather than one pile.

Shot from slightly above, both groups equally sharp, on a light grey seamless surface.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 02 - 1.0 vs 2.0 resolution

| Field | Value |
|---|---|
| Filename | `midi-1-vs-2-resolution-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-1-vs-2-resolution-02.png` |
| Used on | Canvas page `MIDI: MIDI 2 0 What Changed and Why It Matters` |
| Alt text | `A coarse stepped ramp rendered beside a smooth continuous ramp, showing resolution as physical steps` |
| Caption | `Figure 1. The coarse steps are the ones you can hear. Both devices have to agree to speak 2.0, and if either one cannot, the pair falls back to 1.0.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Richly rendered dimensional diagram, drawn in three-quarter isometric perspective with real
depth. Solid saturated colour fills, soft ambient shading and gentle contact shadows under
each element, smooth rounded edges, a subtle glossy highlight on the top face of each solid.
This is a designed object, not a line drawing: no thin hairline outlines, no flat unshaded
shapes, no wireframe, no sketch texture, no watermark, no signature.

Two solid three-dimensional ramps sit side by side on a shared invisible ground plane, each
rising from left to right, each about the same length and the same final height.

The LEFT ramp is built as a staircase: six or seven wide, deep, chunky steps in warm orange
#993300, each step a solid block with a visible top face and front face, so the discrete jumps
are unmistakable.

The RIGHT ramp is a single smooth continuous wedge in deep green #1B5E20, its upper surface
polished and unbroken from bottom left to top right, with no steps at all.

Render both with soft shading and a gentle contact shadow beneath. The contrast between
chunky and smooth is the entire content of the picture.

Build the colour scheme from these and nothing else: deep green #1B5E20, warm orange
#993300, deep blue #0D47A1, near-black #212121, and light neutral greys. Lighter and
darker shades of those five for the shading are fine.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 03 - Cc to DMX scaling

| Field | Value |
|---|---|
| Filename | `midi-cc-to-dmx-scaling-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-cc-to-dmx-scaling-02.png` |
| Used on | Canvas page `MIDI: MIDI to DMX Integration and Conversion` |
| Alt text | `A short segmented bar feeding a longer segmented bar through a tapered funnel, showing two ranges rescaled` |
| Caption | `Figure 1. Two ranges, different sizes. The bridge has to scale the number, not just pass it through.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Richly rendered dimensional diagram, drawn in three-quarter isometric perspective with real
depth. Solid saturated colour fills, soft ambient shading and gentle contact shadows under
each element, smooth rounded edges, a subtle glossy highlight on the top face of each solid.
This is a designed object, not a line drawing: no thin hairline outlines, no flat unshaded
shapes, no wireframe, no sketch texture, no watermark, no signature.

Two solid three-dimensional bars lie horizontally, one above the other, on a shared invisible
ground plane, both starting at the same left edge.

The UPPER bar is deep green #1B5E20, divided across its length into a modest number of wide
segments with visible grooves between them.

The LOWER bar is deep blue #0D47A1, clearly LONGER than the upper one, divided into many more
and much narrower segments.

Between them, a smooth tapered funnel or wedge in warm orange #993300 connects the right end
of the upper bar down and outward to the right end of the lower bar, visibly stretching the
narrow range into the wide one.

Render everything with soft shading, rounded edges and contact shadows.

Build the colour scheme from these and nothing else: deep green #1B5E20, warm orange
#993300, deep blue #0D47A1, near-black #212121, and light neutral greys. Lighter and
darker shades of those five for the shading are fine.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 04 - Local control double trigger

| Field | Value |
|---|---|
| Filename | `midi-local-control-double-trigger-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-local-control-double-trigger-02.png` |
| Used on | Canvas page `MIDI: Device Roles Interfaces and Signal Flow` |
| Alt text | `One input feeding a sound engine twice, once directly inside the device and once via a long external loop` |
| Caption | `Figure 3. One key press, two arrivals. The direct path is Local Control; turning it off leaves only the loop.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Richly rendered dimensional diagram, drawn in three-quarter isometric perspective with real
depth. Solid saturated colour fills, soft ambient shading and gentle contact shadows under
each element, smooth rounded edges, a subtle glossy highlight on the top face of each solid.
This is a designed object, not a line drawing: no thin hairline outlines, no flat unshaded
shapes, no wireframe, no sketch texture, no watermark, no signature.

A large rounded slab in near-black #212121 occupies the LEFT half of the frame, rendered in
three-quarter perspective with visible depth. Set into its surface, toward the bottom, is a
smaller raised pad in deep green #1B5E20 that reads as a component mounted on the slab.

A second, smaller rounded slab in deep blue #0D47A1 sits in the RIGHT half of the frame.

A thick, glossy, tube-like conduit in warm orange #993300 leaves the TOP of the left slab and
curves down a short direct route into the green pad.

A second identical orange conduit leaves the RIGHT edge of the left slab, travels all the way
across to the blue slab, loops around inside it, comes back across the frame, and enters the
SAME green pad from the right.

Both conduits clearly terminate at the same green pad. One route is short and internal, the
other is long and goes out and back. Render with soft shading and contact shadows.

Build the colour scheme from these and nothing else: deep green #1B5E20, warm orange
#993300, deep blue #0D47A1, near-black #212121, and light neutral greys. Lighter and
darker shades of those five for the shading are fine.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 05 - MSC device ID

| Field | Value |
|---|---|
| Filename | `midi-msc-device-id-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-msc-device-id-02.png` |
| Used on | Canvas page `MIDI: MIDI Show Control Protocol` |
| Alt text | `One source slab broadcasting along three identical conduits to three identical receiving slabs` |
| Caption | `Figure 1. A broadcast identifier reaches all three at once. So does an identifier two of them share by accident.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Richly rendered dimensional diagram, drawn in three-quarter isometric perspective with real
depth. Solid saturated colour fills, soft ambient shading and gentle contact shadows under
each element, smooth rounded edges, a subtle glossy highlight on the top face of each solid.
This is a designed object, not a line drawing: no thin hairline outlines, no flat unshaded
shapes, no wireframe, no sketch texture, no watermark, no signature.

A single large rounded slab in deep blue #0D47A1 sits on the LEFT, rendered in three-quarter
perspective with visible depth and a soft contact shadow.

Three identical rounded slabs in near-black #212121 are stacked vertically on the RIGHT, evenly
spaced, all the same size.

Three thick glossy conduits in warm orange #993300 fan out from a single point on the right
face of the blue slab, one to each black slab, entering each one at the same place on its left
face. The three conduits are identical in thickness and finish, so nothing suggests one is
favoured.

On the front face of each black slab, a small empty recessed rectangular socket, unfilled and
unmarked, as though waiting to be set.

Generous empty background around the whole group.

Build the colour scheme from these and nothing else: deep green #1B5E20, warm orange
#993300, deep blue #0D47A1, near-black #212121, and light neutral greys. Lighter and
darker shades of those five for the shading are fine.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 06 - Note on note off timeline

| Field | Value |
|---|---|
| Filename | `midi-note-on-note-off-timeline-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-note-on-note-off-timeline-02.png` |
| Used on | Canvas page `MIDI: Channel Voice Messages and Musical Control` |
| Alt text | `A capped green bar beside an orange bar with a torn open end, running along a shared rail` |
| Caption | `Figure 1. A note is two messages. The bar that never gets its closing cap is the stuck note.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Richly rendered dimensional diagram, drawn in three-quarter isometric perspective with real
depth. Solid saturated colour fills, soft ambient shading and gentle contact shadows under
each element, smooth rounded edges, a subtle glossy highlight on the top face of each solid.
This is a designed object, not a line drawing: no thin hairline outlines, no flat unshaded
shapes, no wireframe, no sketch texture, no watermark, no signature.

A long, low, three-dimensional rail in light neutral grey runs horizontally across the lower
third of the frame, receding slightly in perspective.

Standing on the LEFT portion of that rail, a solid deep green #1B5E20 bar lies along it,
finished at BOTH ends with a distinct raised cap, like a bookend, closing it neatly.

Standing on the RIGHT portion of the same rail, after a clear gap, a solid warm orange #993300
bar of similar height. It has the same raised cap at its LEFT end only. Its RIGHT end is
ragged and torn, as though the bar has been broken off, and it continues off the right edge of
the frame unfinished.

Render both bars with soft shading, glossy top faces and contact shadows on the rail.

Build the colour scheme from these and nothing else: deep green #1B5E20, warm orange
#993300, deep blue #0D47A1, near-black #212121, and light neutral greys. Lighter and
darker shades of those five for the shading are fine.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 07 - In circuit parallel path

| Field | Value |
|---|---|
| Filename | `resistors-in-circuit-parallel-path-02.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/resistors/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-in-circuit-parallel-path-02.jpg` |
| Used on | Canvas page `Resistors: Measuring Resistance` |
| Alt text | `Two resistors sharing both nodes on a breadboard with two multimeter probes touching those nodes` |
| Caption | `Figure 1. In circuit, the meter reads every path between its probes, not only the one you meant to measure.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

A white solderless breadboard fills the frame, shot from directly above and slightly angled.

Two small axial resistors are pushed into the board side by side, clearly wired so that both of
their left leads land in the SAME column and both of their right leads land in the SAME column,
forming an obvious parallel pair. Nothing else is plugged into the board.

A red multimeter probe tip rests on the left shared column and a black multimeter probe tip
rests on the right shared column, their leads running off opposite edges of the frame.

Sharp enough that the individual breadboard holes and the resistor bodies read clearly. The
parallel wiring is the subject and must be unmistakable.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 08 - Serial vs network transport

| Field | Value |
|---|---|
| Filename | `midi-serial-vs-network-transport-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-serial-vs-network-transport-02.png` |
| Used on | Canvas page `MIDI: Over USB and Network` |
| Alt text | `Three separate paired cables above one thick trunk carrying five branches` |
| Caption | `Figure 1. Serial MIDI gives one connection per cable. A network carries many streams down one.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Richly rendered dimensional diagram, drawn in three-quarter isometric perspective with real
depth. Solid saturated colour fills, soft ambient shading and gentle contact shadows under
each element, smooth rounded edges, a subtle glossy highlight on the top face of each solid.
This is a designed object, not a line drawing: no thin hairline outlines, no flat unshaded
shapes, no wireframe, no sketch texture, no watermark, no signature.

Split the frame into an upper band and a lower band with clear empty space between.

UPPER: three separate pairs of small rounded blocks in near-black #212121, each pair joined by
its own short thick glossy conduit in light neutral grey. Three pairs, three separate
conduits, nothing shared between them.

LOWER: one single thick glossy trunk in deep green #1B5E20 running horizontally the width of
the band. Five small rounded blocks in near-black #212121 sit above it, each connected down to
the trunk by a short stub.

The contrast between three isolated links and one shared trunk is the whole picture. Render
with soft shading and contact shadows.

Build the colour scheme from these and nothing else: deep green #1B5E20, warm orange
#993300, deep blue #0D47A1, near-black #212121, and light neutral greys. Lighter and
darker shades of those five for the shading are fine.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 09 - Thru chain vs thru box

| Field | Value |
|---|---|
| Filename | `midi-thru-chain-vs-thru-box-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-thru-chain-vs-thru-box-02.png` |
| Used on | Canvas page `MIDI: Routing Channelization and Thru Management` |
| Alt text | `A chain of four blocks in series above one hub fanning out to four blocks in parallel` |
| Caption | `Figure 1. A chain adds a little delay at every hop. A Thru box hands the same message to everything at once.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Richly rendered dimensional diagram, drawn in three-quarter isometric perspective with real
depth. Solid saturated colour fills, soft ambient shading and gentle contact shadows under
each element, smooth rounded edges, a subtle glossy highlight on the top face of each solid.
This is a designed object, not a line drawing: no thin hairline outlines, no flat unshaded
shapes, no wireframe, no sketch texture, no watermark, no signature.

Split the frame into an upper band and a lower band with clear empty space between.

UPPER: one rounded block in deep blue #0D47A1 at the far left, then four identical rounded
blocks in near-black #212121 in a row to its right, all joined left to right in a single chain
by short glossy conduits in warm orange #993300. Each conduit is visibly a little LONGER than
the one before it, so the chain stretches as it goes.

LOWER: the same deep blue block at the far left, joined by one short conduit to a single taller
rounded hub in deep green #1B5E20. From the right face of that hub, four glossy conduits of
IDENTICAL length fan out to four identical near-black blocks stacked vertically.

Render with soft shading, rounded edges and contact shadows.

Build the colour scheme from these and nothing else: deep green #1B5E20, warm orange
#993300, deep blue #0D47A1, near-black #212121, and light neutral greys. Lighter and
darker shades of those five for the shading are fine.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 10 - Doubling is 3 dB

| Field | Value |
|---|---|
| Filename | `power-doubling-is-3db-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/power/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/power/power-doubling-is-3db-02.png` |
| Used on | Canvas page `Power: Power in Decibels - dBW & dBm` |
| Alt text | `One solid column beside a second column rendered at exactly twice its height` |
| Caption | `Figure 1. Doubling the power is plus 3 dB, whatever the starting number happens to be.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Richly rendered dimensional diagram, drawn in three-quarter isometric perspective with real
depth. Solid saturated colour fills, soft ambient shading and gentle contact shadows under
each element, smooth rounded edges, a subtle glossy highlight on the top face of each solid.
This is a designed object, not a line drawing: no thin hairline outlines, no flat unshaded
shapes, no wireframe, no sketch texture, no watermark, no signature.

Two solid three-dimensional columns stand side by side on a shared invisible ground plane,
rendered in three-quarter perspective, both exactly the same width and depth, well separated.

Both are deep green #1B5E20 with a glossy top face and a soft contact shadow.

The RIGHT column is EXACTLY TWICE the height of the LEFT column. Measure it. This two-to-one
ratio is the entire content of the image; if the right column is not visibly double, the image
is wrong.

A smooth glossy arc in warm orange #993300 springs from the top of the left column, rises, and
lands on the top of the right column.

Nothing else in the frame. Plenty of empty background above and around both columns.

Build the colour scheme from these and nothing else: deep green #1B5E20, warm orange
#993300, deep blue #0D47A1, near-black #212121, and light neutral greys. Lighter and
darker shades of those five for the shading are fine.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 11 - Current path through body

| Field | Value |
|---|---|
| Filename | `wiring-safety-current-path-through-body-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/wiring-safety/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-current-path-through-body-02.png` |
| Used on | Canvas page `Wiring & Safety: Electric Shock and the Human Body` |
| Alt text | `A matte figure with one glowing path arm to arm across the chest and a second arm to foot` |
| Caption | `Figure 1. What decides the injury is the path, not only the current. Arm to arm crosses the heart.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Richly rendered dimensional diagram, drawn in three-quarter isometric perspective with real
depth. Solid saturated colour fills, soft ambient shading and gentle contact shadows under
each element, smooth rounded edges, a subtle glossy highlight on the top face of each solid.
This is a designed object, not a line drawing: no thin hairline outlines, no flat unshaded
shapes, no wireframe, no sketch texture, no watermark, no signature.

A smooth, featureless, matte light grey artist's mannequin figure stands facing the viewer with
both arms held straight out to the sides, rendered in three-quarter perspective with soft
studio shading. No face, no clothing, no detail beyond the form. It stands slightly LEFT of
centre so the right side of the frame stays open.

One glowing warm orange #993300 tube enters at the LEFT hand, runs straight across the chest,
and exits at the RIGHT hand, sitting on the surface of the figure and emitting a soft glow.

A second glowing tube in deep blue #0D47A1 enters at the LEFT hand, runs down the torso and
the left leg, and exits at the LEFT foot.

Inside the chest, on the orange path, a small deep red #B71C1C glow shows through the surface
where the heart sits, clearly intersected by the orange tube and clearly missed by the blue one.

Calm and clinical, not gruesome. No injury, no sparks, no burns.

Build the colour scheme from these and nothing else: deep green #1B5E20, warm orange
#993300, deep blue #0D47A1, near-black #212121, and light neutral greys. Lighter and
darker shades of those five for the shading are fine.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 12 - Battery lamp circuit

| Field | Value |
|---|---|
| Filename | `ac-dc-electricity-battery-lamp-circuit-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-battery-lamp-circuit-01.jpg` |
| Used on | Canvas page `AC & DC: What Is Direct Current?` |
| Alt text | `A nine volt battery wired through a resistor to a lit lamp on a bench` |
| Caption | `Figure 1. Direct current holds one polarity and one direction for as long as the circuit is closed.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

A rectangular nine volt battery lies on a clean light grey bench surface. Two insulated
jumper leads, one red and one black, run from its terminals to a small incandescent lamp in a
simple holder, with a small axial resistor spliced into the red lead partway along.

The lamp is lit, glowing warm and steady, bright enough to read clearly but not blown out.

Shot from a low three-quarter angle so the run of the two leads from battery to lamp is easy to
follow across the frame. Shallow depth of field with the lamp and the battery both sharp.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 13 - Breadboard circuit

| Field | Value |
|---|---|
| Filename | `voltage-current-breadboard-circuit-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-breadboard-circuit-01.jpg` |
| Used on | Canvas page `Voltage & Current: Overview Basic Electronics: Voltage and Current` |
| Alt text | `A small breadboard circuit with a battery, a resistor, and a lit LED` |
| Caption | `Figure 1. Voltage pushes, current flows, resistance limits. Every circuit in this course is these three quantities.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

A white solderless breadboard on a clean light grey bench, shot from a low three-quarter angle.

Plugged into it: a single axial resistor and a single 5 mm LED, wired in series, with two
jumper leads running off the left edge of the frame to a battery holder holding two cylindrical
cells.

The LED is lit and glowing clearly.

Shallow depth of field, the LED and the resistor sharp, the far end of the board falling off
softly. The breadboard holes, the resistor body and the LED lens should all read clearly.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 14 - Orders of magnitude

| Field | Value |
|---|---|
| Filename | `voltage-current-orders-of-magnitude-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-orders-of-magnitude-01.png` |
| Used on | Canvas page `Voltage & Current: The Numbers You Will Actually See` |
| Alt text | `A stepped tower of five blocks rising steeply, the top step dwarfing the bottom ones` |
| Caption | `Figure 1. Audio spans an enormous range. The unit prefix is doing most of the work, not the digits.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Richly rendered dimensional diagram, drawn in three-quarter isometric perspective with real
depth. Solid saturated colour fills, soft ambient shading and gentle contact shadows under
each element, smooth rounded edges, a subtle glossy highlight on the top face of each solid.
This is a designed object, not a line drawing: no thin hairline outlines, no flat unshaded
shapes, no wireframe, no sketch texture, no watermark, no signature.

Five solid three-dimensional blocks stand in a row on a shared invisible ground plane,
rendered in three-quarter perspective, all the same width and depth, rising sharply in height
from left to right.

The rise is steep and accelerating: the second block is clearly taller than the first, the
third clearly taller again, and the fifth towers over all of them, so the range reads as
enormous rather than linear.

The lowest TWO blocks are deep green #1B5E20. The middle two are deep blue #0D47A1. The tallest
single block is warm orange #993300.

Glossy top faces, soft ambient shading, contact shadows. Plenty of empty background above the
tallest block.

Build the colour scheme from these and nothing else: deep green #1B5E20, warm orange
#993300, deep blue #0D47A1, near-black #212121, and light neutral greys. Lighter and
darker shades of those five for the shading are fine.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 15 - Conductor progression

| Field | Value |
|---|---|
| Filename | `wiring-safety-conductor-progression-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/wiring-safety/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-conductor-progression-01.jpg` |
| Used on | Canvas page `Wiring & Safety: History - Electrical Safety Standards` |
| Alt text | `Four wire samples in a row from bare copper through insulated and jacketed to a grounded three conductor cable` |
| Caption | `Figure 1. Every rule on this page exists because something went wrong before it was written.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Four short lengths of wire lie parallel in a row on a clean light grey surface, shot from
directly above, evenly spaced with clear gaps between them.

Left to right: a length of bare bright copper conductor with no covering at all; a length of
single-conductor wire with coloured plastic insulation; a length of two-conductor jacketed
cable with the outer jacket peeled back at one end to show the two insulated conductors inside;
and a length of three-conductor grounded cable with its jacket peeled back to show two
insulated conductors plus a bare copper ground wire.

All four cut square, all four equally sharp, all four the same length. The progression from
naked copper to fully jacketed and grounded is the subject.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 16 - Bench overview

| Field | Value |
|---|---|
| Filename | `syllabus-bench-overview-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/syllabus/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/syllabus/syllabus-bench-overview-01.jpg` |
| Used on | Canvas page `DAPR 2255 Audio Hardware I: Syllabus` |
| Alt text | `An electronics bench laid out with a meter, a breadboard, hand tools and loose components` |
| Caption | `Figure 1. Where the semester goes: safety, the parts, the math, and circuits you build with your own hands.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

A clean, well-organised electronics workbench shot from directly above, filling the frame.

Laid out on it with generous space between: a handheld digital multimeter with its red and
black leads coiled beside it, a white solderless breadboard with a few components already
plugged in, a soldering iron resting in its stand, a pair of wire strippers and a pair of side
cutters, a small coil of solder, and a loose scatter of resistors, capacitors and LEDs.

Warm, inviting, purposeful. Everything unbranded and anonymous. Shot on a neutral bench
surface with soft overhead light and no harsh shadows.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 17 - Assignment bench

| Field | Value |
|---|---|
| Filename | `ohms-law-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/ohms-law/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/ohms-law/ohms-law-assignment-bench-01.jpg` |
| Used on | Canvas page `Ohm's Law: Assignment - Applying V = IR` |
| Alt text | `A multimeter, a battery and a single resistor arranged on a bench for a simple measurement` |
| Caption | `Figure 1. Three quantities and one resistor. That is the whole worksheet.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Shot from directly above on a clean light grey surface: a handheld digital multimeter in the
lower left with its red and black probe leads laid out neatly, a rectangular nine volt battery
in the upper left, and a single axial resistor lying alone in the centre right with clear
empty space around it.

The resistor is the sharpest thing in the frame and its colour bands are clearly legible.

Generous empty background. Calm and uncluttered.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 18 - Assignment bench

| Field | Value |
|---|---|
| Filename | `resistors-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/resistors/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-assignment-bench-01.jpg` |
| Used on | Canvas page `Resistors: Assignment - Color Codes, Power, & Audio Applications` |
| Alt text | `Assorted resistors of different wattages laid out with their colour bands facing the camera` |
| Caption | `Figure 1. Read the bands, check the wattage, then decide where it belongs in the circuit.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Shot from directly above on a clean light grey surface: a row of a dozen axial resistors laid
out parallel with even spacing, all with their colour bands facing the camera and clearly
legible.

The row deliberately mixes physical sizes, from small quarter-watt bodies at one end up to two
or three noticeably larger, fatter power resistors at the other, so the size difference reads
as a difference in rating.

Sharp across the whole row. Generous empty background above and below.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 19 - Assignment bench

| Field | Value |
|---|---|
| Filename | `series-parallel-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/series-parallel/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/series-parallel/series-parallel-assignment-bench-01.jpg` |
| Used on | Canvas page `Series & Parallel Circuits: Assignment - Circuit Analysis & Audio Applications` |
| Alt text | `One breadboard wired as a series chain beside a second wired as a parallel pair` |
| Caption | `Figure 1. Decide which arrangement you are looking at first. The method follows from that.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Two identical white solderless breadboards lie side by side on a clean light grey surface,
shot from directly above with a clear gap between them.

On the LEFT board, two axial resistors are plugged in end to end in a single line, so the
current has one obvious path straight through both.

On the RIGHT board, two axial resistors are plugged in side by side sharing the same two
columns, so they visibly sit on two separate branches between the same pair of points.

Nothing else on either board. Both equally sharp, both lit the same way, so the only difference
a reader sees is the wiring.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 20 - Assignment bench

| Field | Value |
|---|---|
| Filename | `multimeters-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/multimeters/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-assignment-bench-01.jpg` |
| Used on | Canvas page `Multimeters: Assignment - Reading & Interpreting Measurements` |
| Alt text | `A handheld digital multimeter with its leads plugged in, on a bench with a small circuit` |
| Caption | `Figure 1. Three settings, three different ways to connect the meter. Getting that wrong is how meters die.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

A handheld digital multimeter lies on a clean light grey bench, shot from a low three-quarter
angle so its rotary dial and its input jacks are both clearly visible.

The black lead is plugged into the common jack and the red lead into the voltage jack, both
leads running forward toward the camera and out of frame.

Just behind the meter, slightly out of focus, a small breadboard with a couple of components
plugged into it.

The dial face and the input jacks are the sharpest part of the frame. No brand name, no model
number, and no readable text on the display: show the display dark or blank.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 21 - Assignment bench

| Field | Value |
|---|---|
| Filename | `power-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/power/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/power/power-assignment-bench-01.jpg` |
| Used on | Canvas page `Power: Assignment - Power Calculations & Amplifier Matching` |
| Alt text | `A large finned heat sink with a power device bolted to it beside two power resistors` |
| Caption | `Figure 1. Power is the part of a circuit you can feel. Everything on this worksheet ends up as heat.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

A substantial black anodised aluminium heat sink with deep fins sits on a clean light grey
bench, shot from a low three-quarter angle so the depth of the fins is obvious.

A single TO-220 power device is bolted to its flat face with a visible mounting screw and a
thin insulating washer at the joint.

Two large cement-bodied power resistors lie on the bench in front of it, well separated and in
focus.

Shallow depth of field, the mounting joint and the resistors sharp, the far fins falling off
softly. No printed markings legible on any part.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 22 - Assignment bench

| Field | Value |
|---|---|
| Filename | `batteries-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/batteries/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/batteries/batteries-assignment-bench-01.jpg` |
| Used on | Canvas page `Batteries: Assignment - Battery Selection & Runtime Calculations` |
| Alt text | `A battery holder wired for series beside a second wired for parallel, with loose cells` |
| Caption | `Figure 1. Series stacks voltage. Parallel stacks runtime. The wiring decides which you get.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Shot from directly above on a clean light grey surface.

On the LEFT, a plastic battery holder carrying four cylindrical cells arranged end to end in a
single line, so they read as a chain.

On the RIGHT, four cylindrical cells laid out side by side in a row, all pointing the same way,
with short jumper leads bridging all four positive ends together and all four negative ends
together.

A clear gap of empty background between the two groups. Both equally sharp. No printed labels
legible on the cells: show them plain and unbranded.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 23 - Assignment bench

| Field | Value |
|---|---|
| Filename | `diodes-leds-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/diodes-leds/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-assignment-bench-01.jpg` |
| Used on | Canvas page `Diodes & LEDs: Assignment - Applying Diode & LED Principles` |
| Alt text | `Rectifier diodes with their cathode bands showing laid out beside assorted LEDs` |
| Caption | `Figure 1. Forward biased it conducts, reverse biased it does not. The band tells you which end is which.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Shot from directly above on a clean light grey surface.

On the LEFT, a row of five small black rectifier diodes laid out parallel with even spacing,
every one turned so its light-coloured cathode band is clearly visible and all the bands point
the same way.

On the RIGHT, a loose scatter of six 5 mm LEDs in different lens colours, red, green, yellow,
blue and clear, lying on their sides with their two legs of obviously unequal length visible.

A clear gap between the two groups. Everything sharp. Generous empty background.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 24 - Assignment bench

| Field | Value |
|---|---|
| Filename | `transistors-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/transistors/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/transistors/transistors-assignment-bench-01.jpg` |
| Used on | Canvas page `Transistors: Assignment - Applying BJT & FET Concepts` |
| Alt text | `Small signal transistors in TO-92 packages beside a larger TO-220 power device` |
| Caption | `Figure 1. A small current at the base controls a much larger one through the device. The packages tell you how much.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Shot from directly above on a clean light grey surface.

On the LEFT, four small black TO-92 transistors with their flat faces up and their three legs
splayed, laid out in a neat row with even spacing.

On the RIGHT, a single much larger TO-220 power transistor with its metal mounting tab, lying
flat with its three heavy legs toward the camera.

The size difference between the small signal parts and the power part is the subject and should
be obvious at a glance. No printed part numbers legible on any of them: show the packages
plain.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 25 - Assignment bench

| Field | Value |
|---|---|
| Filename | `capacitors-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/capacitors/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/capacitors/capacitors-assignment-bench-01.jpg` |
| Used on | Canvas page `Capacitors: Assignment - Markings, Reactance, & Audio Applications` |
| Alt text | `Electrolytic, film and ceramic capacitors of several sizes laid out together` |
| Caption | `Figure 1. Three families, three sets of markings, and three different jobs in an audio circuit.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Shot from directly above on a clean light grey surface.

Three groups laid out left to right with clear gaps between them: a pair of cylindrical
aluminium electrolytic capacitors standing on end, one small and one noticeably larger; three
boxy rectangular film capacitors lying flat; and four small disc ceramic capacitors with their
two legs splayed.

The difference in body shape and size between the three families is the subject.

Everything sharp, evenly lit, no printed values legible. Generous empty background.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 26 - Assignment bench

| Field | Value |
|---|---|
| Filename | `inductors-transformers-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/inductors-transformers/inductors-transformers-assignment-bench-01.jpg` |
| Used on | Canvas page `Inductors & Transformers: Assignment - Turns Ratios, Reactance, & Audio Applications` |
| Alt text | `A toroidal transformer, a laminated transformer and two inductors laid out on a bench` |
| Caption | `Figure 1. All of these are coils of wire around a core. The ratio between the windings is what changes.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Shot from a low three-quarter angle on a clean light grey bench.

A doughnut-shaped toroidal transformer, its copper windings wrapped visibly around the ring,
sits on the LEFT. A rectangular laminated steel transformer with its stacked E-shaped plates
and bobbin visible sits in the CENTRE. Two small inductors, one an air-cored coil of bare
copper and one a small ferrite-cored choke, lie on the RIGHT.

The copper windings on the toroid and the stacked laminations on the rectangular unit should
both read clearly.

Shallow depth of field with the toroid and the laminated core sharp. No labels legible.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 27 - Assignment bench

| Field | Value |
|---|---|
| Filename | `switches-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/switches/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/switches/switches-assignment-bench-01.jpg` |
| Used on | Canvas page `Switches: Assignment - Selecting & Wiring Audio Switches` |
| Alt text | `Toggle, rocker, slide and rotary switches laid out with their solder lugs facing the camera` |
| Caption | `Figure 1. Poles are how many circuits it handles. Throws are how many positions each one has. Count the lugs.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Shot from a low three-quarter angle on a clean light grey surface, chosen so the SOLDER LUGS on
the underside of each switch are clearly visible rather than hidden.

Four switches laid out in a row with even spacing: a metal-bodied toggle switch, a plastic
rocker switch, a small slide switch, and a rotary switch with a round body and a shaft.

The lug count differs visibly between them, and the lugs are the sharpest thing in the frame.

No printed ratings or markings legible on any body.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 28 - Assignment bench

| Field | Value |
|---|---|
| Filename | `schematics-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/schematics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/schematics/schematics-assignment-bench-01.jpg` |
| Used on | Canvas page `Schematics: Assignment - Symbols, Conventions, & Signal Tracing` |
| Alt text | `A populated circuit board shot close so individual components and traces are legible` |
| Caption | `Figure 1. A schematic is the map. This is the territory it describes.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

A green fibreglass printed circuit board, populated with through-hole components, fills the
frame at a low three-quarter angle.

Resistors, a few electrolytic capacitors standing on end, a couple of small transistors and an
integrated circuit in a socket are all visible, and the copper traces running between them are
clearly readable across the board surface.

Shallow depth of field, the nearer third of the board tack sharp, the far end falling away.

No silkscreen text, part numbers or logos legible anywhere: show the board's printed markings
as indistinct.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 29 - Assignment bench

| Field | Value |
|---|---|
| Filename | `wiring-safety-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/wiring-safety/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-assignment-bench-01.jpg` |
| Used on | Canvas page `Wiring & Safety: Assignment - Cable, Solder, & Component Safety` |
| Alt text | `Wire strippers, solder, heat shrink and stripped cable laid out on a bench` |
| Caption | `Figure 1. Pick the gauge, make the joint, protect it. This worksheet is the three of those in order.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

Shot from directly above on a clean light grey surface, laid out with generous space between
each item.

A pair of wire strippers. A short coil of solder. Three lengths of heat-shrink tubing in
different diameters. Two lengths of stranded cable with the insulation stripped back cleanly at
one end to show bright twisted copper. A soldering iron tip resting at the edge of the frame.

Neat and deliberate, like a tray laid out before a job. Everything sharp and evenly lit, no
brand markings legible.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Image 30 - Assignment bench

| Field | Value |
|---|---|
| Filename | `ac-dc-electricity-assignment-bench-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-assignment-bench-01.jpg` |
| Used on | Canvas page `AC & DC: Assignment - Sine Waves, RMS, & Signal Levels` |
| Alt text | `A bench power supply beside a signal cable and a battery, shot on a workbench` |
| Caption | `Figure 1. A steady supply, a changing signal, and the arithmetic that describes both.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft, even, slightly directional lighting from above and
to the left. Shallow depth of field with the subject sharp and the background falling off.
Real materials with visible surface texture: brushed and anodized metal, matte and glossy
plastic, bright copper, fibreglass board. Shot square to the subject on a clean seamless
light grey sweep unless the block below says otherwise. Colour-accurate, natural contrast,
no heavy stylisation, no illustration, no cartoon, no render-engine look.

A small bench power supply with a blank, unlit, unreadable display sits at the back of a clean
light grey workbench, shot from a low three-quarter angle.

In front of it, laid out with clear space between them: a short black shielded audio cable
coiled loosely, and a rectangular nine volt battery standing on its terminals.

Shallow depth of field with the cable and the battery sharp and the supply softening behind
them.

No text, no numbers, no digits legible anywhere, including on the supply's display, its knobs
or its panel. Show every marking as indistinct.

NO TEXT. Do not write, print, letter, label, caption, title or stamp a single word, number,
digit or symbol anywhere in this image. Not on the subject, not beside it, not in a corner,
not as a watermark. Every word this figure needs is already on the Canvas page beneath it.
If you are tempted to add a label, add clearer shape or colour instead.

Nothing in the frame may claim to be a particular product. No logo, no brand mark, no model
number, no printed silkscreen, no serial number, no software window or user interface, and no
connector drawn with numbered pins. Generic, unbranded, anonymous hardware only. No hands, no
people, no faces.
```

---

## Saving these

ChatGPT will hand you a zip. Do not unpack it by hand and do not rename anything inside it.
Drop the zip anywhere and run the filer:

```
python3 "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Build-Tools/file_images.py" ~/Downloads
```

It unpacks, matches each image to its entry in this brief even when ChatGPT has dropped the
`-01` or changed the extension, writes it into the right topic folder under the right name,
and prints what landed and what is still missing. It is done when the prompt comes back and
the missing list is empty.

After that: push, and the next cartridge places all of these, moves the replaced pages to
their new filenames, and regenerates the Image Reference. The twenty photographs on the four
capture sheets in this folder are the only thing left after that.
