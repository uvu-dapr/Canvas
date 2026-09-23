# ChatGPT Image Creation - DAPR 3255 v8

Generated 2026-09-22. **This is the only DAPR 3255 image brief.** It replaces
`ChatGPT Image Creation - DAPR 3255 v7.md`, which is superseded.

**Eleven prompts.** The v7 file had fifty-one. You already ran forty-seven of
them, tonight, between 00:55 and 01:18. They are on disk. I reviewed every one
of them by eye before writing this file, and forty of the forty-seven are good
enough to go on a page as they are.

This file is what is actually left.

## Why this file is short

I checked the folder against the v7 brief filename by filename. Here is the count.

| | Prompts | State |
|---|---|---|
| v7 brief total | 51 | |
| Already generated and **approved** | 40 | On disk. Nothing to do. I will place them |
| Already generated but **came back wrong** | 7 | In this file, as a corrected retry |
| Never generated (the `wireless/` folder was never created) | 4 | In this file, unchanged from v7 |
| **This file** | **11** | |

Forty prompts came off the list because the file already exists and is correct.
That is the whole reason this went from 51 to 11.

## How to work this file

| Group | What it is | Prompts | Why |
|---|---|---|---|
| **A** | The four `wireless/` figures that were never generated | 01 to 04 | Four pages in the Wireless module have no figure at all |
| **B** | Seven figures that came back with a real error in them | 05 to 11 | Each one teaches something false as drawn |

Group A is new work. Group B is a second attempt at something the generator got
wrong, and each Group B prompt says plainly what went wrong so you can check the
result against it before you save.

Every prompt is self-contained. Stop after either group and the course is in a
consistent state.

## What I found wrong, in one table

I looked at all forty-seven generated files. These seven are the ones I am
sending back. Everything not in this table is approved.

| File as generated | What is wrong with it | Prompt |
|---|---|---|
| `electronics-opamp-inverting-vs-noninverting-02.png` | The non-inverting half has the feedback resistor landing on the **plus** input, together with the signal. The minus input only goes to ground. That is positive feedback with no negative feedback: as drawn it latches, it does not amplify | 05 |
| `electronics-ac-vs-dc-waveform-02.png` | The AC ribbon never crosses below the baseline. It is a unipolar ripple sitting on top of the plinth. Polarity reversal is the one thing that makes AC different from DC, and the figure does not show it | 06 |
| `electronics-bjt-voltage-divider-bias-02.png` | The lower divider resistor ends on a floating ball terminal instead of ground. Only the emitter resistor reaches ground, so the divider has no return path and the base sits at the supply rail through one resistor | 07 |
| `electronics-filter-alignments-01.png` | In the stopband the slopes are in reverse order. The figure shows the gentlest alignment falling fastest and the sharpest falling slowest. A student reads it as Bessel being the most aggressive filter, which is backwards | 08 |
| `ip-addressing-subnet-mask-bit-boundary-02.png` | The third row alternates network, host, network, host. A mask is contiguous ones then contiguous zeros. A non-contiguous mask is exactly the misconception a boundary figure exists to kill | 09 |
| `network-diagnostics-arp-resolution-sequence-02.png` | The structure is right and the mid-air arrow from the `-01` is gone, but there is red and cyan speckle scattered across the middle of the frame from a botched background matte | 10 |
| `audio-protocols-protocol-comparison-matrix-02.png` | A grey grid with seven colored balls dropped on it and two arrows off to the side. No rows, no columns, nothing to compare. It carries no information at all. The `-01` it replaced was more useful | 11 |

## Two things I got wrong on first look, and corrected

Being straight about this because I nearly sent you two extra prompts.

- I flagged `audio-protocols-aes50-point-to-point-chain-02.png` as having a
  missing last link between the third and fourth box. At full resolution all
  three cables are present. **I was wrong.** The chain is complete and the file
  is approved.
- I flagged the transistor in `electronics-bjt-voltage-divider-bias-02.png` as a
  PNG drawn PNP. At full resolution the emitter arrow points away from the base,
  which is NPN and matches the wiring. **I was wrong about that too.** The
  floating divider leg in prompt 07 is real; the symbol is fine.

## Five files that are over budget and are not your problem

Standards 20.3 caps a PNG at 1 MB and a JPEG at 500 KB. Five files are over. This
is a re-encode, not a regeneration, and I will do it. Listed so you know I saw it.

| File | Size | Cap |
|---|---|---|
| `electronics-solder-joint-macro-01.jpg` | 1,853,216 | 512,000 |
| `electronics-semiconductor-pn-junction-02.png` | 1,216,555 | 1,048,576 |
| `audio-protocols-ndi-bandwidth-tiers-02.png` | 1,150,781 | 1,048,576 |
| `electronics-breadboard-internal-connections-01.png` | 1,072,054 | 1,048,576 |
| `audio-protocols-avb-milan-reserved-bandwidth-02.png` | 1,058,777 | 1,048,576 |

## The style

Standards 20.5a, set 2026-09-21: photorealistic is the house style, and a real
object is photographed rather than drawn. Nothing in this file is a real object.
All eleven are things that are not things, so all eleven ask for a **richly
rendered dimensional diagram**: isometric or three-quarter, real depth, shading,
solid fills, soft shadows, on a transparent background.

**No prompt below asks for any text inside the image.** Standards 20.5 records
that twelve of the first twenty-eight DAPR 2255 images failed and every single
failure was text. The page carries the heading, the caption and the prose. The
picture does not need a word. If a returned image has text in it anyway,
regenerate. Do not accept it and do not patch it in an editor.

## Palette, from Standards 3

`#212121` body dark, `#1B5E20` green, `#0D47A1` blue, `#B71C1C` red, `#993300`
orange, `#616161` grey, `#5D4037` brown.

Several of the approved files use purple, yellow or brown outside this list. I am
letting those stand rather than spend a prompt on a color.

## Filenames never get overwritten

Standards 20.4: a conforming filename is permanent. So every retry in Group B
gets the next number, not the number it is replacing. The old file stays on disk
and the page's `src` moves to the new one. That is why Group B filenames end
`-03` where a `-02` already exists.

---

# Group A

**Group A. The four figures that were never generated.** The `wireless/` folder
does not exist. Create it before saving anything in this group:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless
```

These four prompts are unchanged from the v7 brief. Nothing about them was wrong;
they simply never ran.

---
## Image 01 - Microphone system against in-ear system

| Field | Value |
|---|---|
| Filename | `wireless-microphone-against-iem-direction-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Wireless/Microphone_Against_Iem_Direction.png` |
| Used on | Canvas page `Wireless: System Architecture` |
| Alt text | `Many small units feeding one large unit on the left, one large unit feeding many small units on the right` |
| Caption | `Figure 1. Microphones on the left, in-ear monitors on the right. The arrows point the other way, and that changes where the antennas go.` |

**This folder does not exist yet. Create `Images/wireless/` before saving.**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric view, with real depth and
shading and solid color fills. Not flat line art.

The frame is divided into a left half and a right half by a narrow vertical gap.

In the left half, three small rounded blocks are stacked vertically near the left
edge, drawn in isometric with visible depth and shadow, in green #1B5E20. Three
thick arrows in green sweep from them rightward and converge into one large
rounded block near the center divider, drawn larger and deeper, in dark #212121.

In the right half, the arrangement is mirrored in direction: one large rounded
block in dark #212121 sits near the center divider, and three thick arrows in
orange #993300 sweep rightward from it and fan out to three small rounded blocks
stacked vertically near the right edge, in orange.

The contrast between many-to-one on the left and one-to-many on the right is the
whole point and should be unmistakable at a glance.

Reading direction is left to right in both halves.

No text anywhere in the image. No labels, no titles, no legend. No logo, brand
mark, model number, product photograph, microphone, or antenna hardware. No
borders, frames, title bars, or caption text. No watermark, no signature.
```

---

## Image 02 - Antenna radiation patterns

| Field | Value |
|---|---|
| Filename | `wireless-antenna-patterns-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Wireless/Antenna_Patterns.png` |
| Used on | Canvas page `Wireless: Antennas and Distribution` |
| Alt text | `Four radiation patterns in a row: a circle, a figure of eight, a broad lobe, and a narrow lobe` |
| Caption | `Figure 1. Left to right: quarter wave whip, half wave dipole, log periodic, helical. Gain concentrates the pattern, it does not amplify.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth and
shading and solid color fills. Not flat line art.

Four radiation patterns sit in a row across the frame, evenly spaced, each
centered on a small dark #212121 sphere that represents the antenna. Each pattern
is rendered as a solid translucent volume in blue #0D47A1 with visible depth,
soft internal shading and a shadow on the ground plane beneath it, so it reads as
a three-dimensional balloon of energy rather than an outline.

The first is a full sphere surrounding its center point evenly in every direction.

The second is two equal rounded lobes pointing left and right from its center,
pinched to nothing above and below, a figure of eight.

The third is a single broad lobe pointing right, wide and rounded, with a small
bump pointing left behind the center.

The fourth is a single long narrow lobe pointing right, clearly longer and
thinner than the third, with almost nothing behind the center.

The progression from omnidirectional to increasingly concentrated is obvious
across the row.

Reading direction is left to right.

No text anywhere in the image. No labels, no numbers, no legend, no degree marks.
No logo, brand mark, model number, product photograph, or antenna hardware. No
borders, frames, title bars, or caption text. No watermark, no signature.
```

---

## Image 03 - Multipath null and diversity spacing

| Field | Value |
|---|---|
| Filename | `wireless-multipath-null-and-diversity-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Wireless/Multipath_Null_and_Diversity.png` |
| Used on | Canvas page `Wireless: Antennas and Distribution` |
| Alt text | `A direct path and a reflected path reaching two receive antennas, cancelling at the upper one and adding at the lower` |
| Caption | `Figure 2. The upper antenna sits in a null, the lower one does not. A null is a place, which is why two antennas beat one.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth and
shading and solid color fills. Not flat line art.

A small dark #212121 sphere sits at the left, representing a transmitter. Two
upright rods stand at the right, one above the other with a clear vertical gap
between them, representing two receive antennas. Both rods are rendered with
metallic shading and cast shadows.

A thick blue #0D47A1 tube of energy runs in a straight line from the sphere to
the upper rod. A second thick orange #993300 tube leaves the sphere, rises,
bounces off a flat horizontal surface across the top of the frame, and comes down
to the same upper rod.

Beside the upper rod, two wave forms of equal size are drawn one above the other,
exactly out of step with each other so their crests align with the other's
troughs, and beneath them a flat line with no wave at all, in red #B71C1C.

Beside the lower rod, two wave forms of equal size are drawn one above the other,
exactly in step so their crests align, and beneath them a single larger wave, in
green #1B5E20.

All wave forms are solid ribbons with thickness and shadow so they read as
physical objects.

Reading direction is left to right.

No text anywhere in the image. No labels, no numbers, no legend. No logo, brand
mark, model number, product photograph, or recognizable antenna product. No
borders, frames, title bars, or caption text. No watermark, no signature.
```

---

## Image 04 - Third order intermodulation

| Field | Value |
|---|---|
| Filename | `wireless-third-order-intermodulation-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Wireless/Third_Order_Intermodulation.png` |
| Used on | Canvas page `Wireless: Frequency Coordination and Troubleshooting` |
| Alt text | `Two tall bars on a frequency axis with two shorter bars falling either side of them at equal spacing` |
| Caption | `Figure 1. Two transmitters, four signals. The tall blue pair are the carriers. The short red pair are the third order products nobody planned for.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth and
shading and solid color fills. Not flat line art.

A flat horizontal base plane runs across the lower part of the frame in dark
#212121, seen at a slight angle so it has depth.

Four vertical bars stand on that plane, evenly spaced across it, rendered as
solid three-dimensional columns with shading on their sides and shadows on the
plane.

The second and third bars from the left are tall and blue #0D47A1, and they are
the same height as each other.

The first and fourth bars are red #B71C1C and about half the height of the blue
ones. The first sits as far to the left of the first blue bar as the two blue
bars are apart from each other, and the fourth sits the same distance to the
right of the second blue bar, so all four are evenly spaced.

Reading direction is left to right.

No text anywhere in the image. No axis labels, no frequency numbers, no legend.
No logo, brand mark, model number, or product photograph. No borders, frames,
title bars, or caption text. No watermark, no signature.
```

---

---

# Group B

**Group B. Seven figures that came back wrong.** Each one below already exists on
disk and each one teaches something false as drawn. The prompt says what went
wrong so you can hold the new image up against it before saving.

---

## Image 05 - Inverting against non-inverting, third attempt

| Field | Value |
|---|---|
| Filename | `electronics-opamp-inverting-vs-noninverting-03.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Rendered_Triangles_With_Tan_Resistors.png` |
| Replaces | `electronics-opamp-inverting-vs-noninverting-02.png` |
| Used on | Canvas page `Electronics: Op-amp Circuits` |
| Alt text | `Inverting amplifier on the left and non-inverting amplifier on the right, feedback to the minus input in both` |
| Caption | `Figure 1. Both circuits feed back to the minus input. What changes is where the signal goes in.` |

**What went wrong twice.** The `-01` drew the non-inverting half with no input at
all, a bare stub in empty space. The `-02` gave it an input but ran the feedback
resistor from the output back to the **plus** input, the same node the signal
arrives on, and left the minus input tied to ground through a resistor with
nothing else on it. That is positive feedback and no negative feedback. Read the
wiring description below literally and check the result node by node before
saving. The feedback resistor must reach the **minus** input in both halves. That
is the point of the figure.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth,
shading, solid color fills and soft shadows. Not flat line art. Wires are thick
rounded dark #212121 tubes. Junction dots are small dark spheres. Resistors are
small horizontal or vertical cylinders in a muted tan body.

Two separate circuits, side by side, with a clear gap between them. Each circuit
is built around a solid blue #0D47A1 triangle pointing to the right, with a
white minus sign inside it near the upper left edge and a white plus sign inside
it near the lower left edge. The output wire leaves the sharp right-hand tip of
each triangle and runs to the right edge of its half of the frame.

LEFT CIRCUIT, wire by wire:
- A horizontal wire enters from the left edge, passes through one resistor, and
  arrives at a junction dot.
- From that junction dot a short wire runs right and touches the flat left edge
  of the triangle at the MINUS sign.
- From that same junction dot a wire rises, runs right along the top through a
  second resistor, then turns down and joins the output wire at the triangle tip.
- A separate wire leaves the flat left edge of the triangle at the PLUS sign,
  runs down, and ends in a ground symbol of three stacked horizontal bars of
  decreasing width.

RIGHT CIRCUIT, wire by wire:
- A horizontal wire enters from the left edge with NO resistor in it and runs
  directly to the flat left edge of the triangle at the PLUS sign.
- A separate junction dot sits to the left of the MINUS sign. A short wire runs
  from it right to the flat left edge of the triangle at the MINUS sign.
- From that same junction dot a wire rises, runs right along the top through a
  resistor, then turns down and joins the output wire at the triangle tip.
- From that same junction dot a second wire runs downward through a vertical
  resistor and ends in a ground symbol of three stacked horizontal bars.

The signal wire on the right must not touch the top feedback wire anywhere. The
top feedback wire in both circuits must arrive at the minus input, never the plus
input.

No text anywhere in the image except the single plus and minus signs inside each
triangle. No numbers, no component values, no labels, no titles, no legend. No
borders, frames or caption text. No watermark, no signature.
```

---

## Image 06 - AC against DC, second attempt

| Field | Value |
|---|---|
| Filename | `electronics-ac-vs-dc-waveform-03.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-ac-vs-dc-waveform-03.png` |
| Replaces | `electronics-ac-vs-dc-waveform-02.png` |
| Used on | Canvas page `Electronics: AC & DC Circuits` |
| Alt text | `A flat steady ribbon above a baseline beside a wave ribbon crossing above and below the same baseline` |
| Caption | `Figure 1. DC holds one polarity. AC reverses, and the baseline is where it changes sign.` |

**What went wrong.** The `-02` drew the AC ribbon sitting entirely on top of the
plinth with its lowest points just touching the surface. Nothing ever goes below
the line. That is a rectified ripple, not AC. Polarity reversal is the one thing
the figure exists to show. The baseline has to be a line the wave passes
**through**, not a floor it rests on.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth,
shading, solid color fills and soft shadows. Not flat line art.

Two panels side by side with a clear gap between them.

In each panel a single thin dark #212121 horizontal reference bar runs left to
right across the vertical middle of that panel, like a rail seen slightly from
above. This bar is the zero line. It is thin and it is NOT a solid plinth, a
slab, a table or a floor. There must be open transparent space both above and
below it.

LEFT PANEL: a thick ribbon in blue #0D47A1 runs left to right at a constant
height ABOVE the reference bar, perfectly level for its whole length, with a
short vertical drop down to the bar at each end. It never crosses the bar.

RIGHT PANEL: a thick ribbon in green #1B5E20 runs left to right as a smooth
sine wave of two and a half full cycles. Its crests rise above the reference bar
and its troughs fall BELOW the reference bar by the same distance the crests rise
above it. The ribbon passes cleanly through the reference bar five times. The
troughs must be clearly below the bar with transparent space visible underneath
them. The wave is symmetric about the bar.

No text anywhere in the image. No labels, no axis marks, no numbers, no titles,
no legend. No borders, frames or caption text. No watermark, no signature.
```

---

## Image 07 - Voltage divider bias, second attempt

| Field | Value |
|---|---|
| Filename | `electronics-bjt-voltage-divider-bias-03.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-bjt-voltage-divider-bias-03.png` |
| Replaces | `electronics-bjt-voltage-divider-bias-02.png` |
| Used on | Canvas page `Electronics: Transistor Biasing` |
| Alt text | `Voltage divider biasing an NPN transistor with collector and emitter resistors, both legs returning to ground` |
| Caption | `Figure 2. Two resistors set the base voltage. Both legs have to reach ground or nothing is set.` |

**What went wrong.** The `-02` ended the lower divider resistor on a floating ball
terminal in empty space instead of a ground symbol. Only the emitter resistor
reached ground. With no return path the divider does nothing and the base sits at
the supply rail through one resistor. Four things in this circuit touch ground and
the figure has to show all four reaching the same ground.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth,
shading, solid color fills and soft shadows. Not flat line art. Wires are thick
rounded dark #212121 tubes. Junction dots are small dark spheres. Resistors are
vertical cylinders with a muted tan body and colored bands.

One horizontal supply rail runs across the top of the frame.

LEFT BRANCH: from a junction dot on the supply rail a wire runs down through a
resistor to a junction dot at mid height, then continues down through a second
resistor and ends in a GROUND SYMBOL: three stacked horizontal bars of decreasing
width. Not a ball, not a bare wire end, not a dot. A ground symbol.

From the mid-height junction dot a horizontal wire runs right to the vertical base
bar of a transistor.

The transistor is a solid blue #0D47A1 circle. Inside it a short vertical bar is
the base. Two leads leave the bar: one goes up and right to the collector
terminal, one goes down and right to the emitter terminal. The emitter lead
carries a solid arrowhead pointing AWAY from the base bar, outward along the lead.
This is an NPN.

RIGHT BRANCH: from a second junction dot on the supply rail a wire runs down
through a resistor to the collector terminal of the transistor. From the emitter
terminal a wire runs down through a fourth resistor and ends in a GROUND SYMBOL,
three stacked horizontal bars of decreasing width.

Both ground symbols sit at the same height along the bottom of the frame and look
identical. No wire in this image ends in a bare ball, stub or open terminal.

No text anywhere in the image. No component values, no labels, no numbers, no
titles, no legend. No borders, frames or caption text. No watermark, no signature.
```

---

## Image 08 - Three filter alignments, second attempt

| Field | Value |
|---|---|
| Filename | `electronics-filter-alignments-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Early_Peaking_Gradual_Rolloff_Curves.png` |
| Replaces | `electronics-filter-alignments-01.png` |
| Used on | Canvas page `Electronics: Active Filters, Order, and Q` |
| Alt text | `Three low pass curves sharing a corner, one with a passband peak, ordered by how steeply they fall` |
| Caption | `Figure 2. Same order, three alignments. What you trade for a flatter passband is how fast it falls.` |

**What went wrong.** The `-01` got the passband right and the stopband backwards.
It showed the gentlest alignment falling fastest and the peaking one falling
slowest, and all three converging on one point so they never cross. The ordering
below the corner must be the reverse of that, and the three curves must stay
separated all the way down.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth,
shading and solid color fills. Not flat line art. Each curve is a thick rounded
ribbon with visible thickness and a soft shadow.

One thin dark #212121 horizontal baseline runs along the bottom of the frame.

Three low pass response ribbons run left to right. All three start at the same
height on the left, flat and overlapping, in the left third of the frame. They
separate in the middle third and fall toward the baseline on the right.

RED #B71C1C ribbon: stays flat, then rises into one rounded bump above its own
flat level just before it turns down, then falls. Of the three it falls the
STEEPEST and is the LEFTMOST of the three in the lower half of the frame.

BLUE #0D47A1 ribbon: stays flat the longest and the flattest with no bump at all,
then turns down. It falls less steeply than red and sits BETWEEN red and green
in the lower half of the frame.

GREEN #1B5E20 ribbon: begins drooping gently earliest, well before the other two
leave their flat level, but falls the SHALLOWEST of the three. It is the
RIGHTMOST of the three in the lower half of the frame.

Read at any height in the lower half of the frame, left to right, the order across
the frame is red, then blue, then green. The three ribbons cross each other once
in the middle third of the frame and stay clearly separated after that. They do
NOT converge to a single common point at the bottom right.

No text anywhere in the image. No labels, no axis marks, no numbers, no titles,
no legend. No borders, frames or caption text. No watermark, no signature.
```

---

## Image 09 - Subnet mask bit boundary, second attempt

| Field | Value |
|---|---|
| Filename | `ip-addressing-subnet-mask-bit-boundary-03.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-subnet-mask-bit-boundary-03.png` |
| Replaces | `ip-addressing-subnet-mask-bit-boundary-02.png` |
| Used on | Canvas page `Networking: Subnet Masks and CIDR` |
| Alt text | `Three address bars with the network and host boundary moved further right on each one` |
| Caption | `Figure 3. The boundary slides. It never breaks into pieces: ones on the left, zeros on the right, always.` |

**What went wrong.** The `-02` drew the third row as blue, green, blue, green. On a
figure where blue reads as network bits and green as host bits, that says a mask
can alternate. It cannot. A mask is contiguous ones followed by contiguous zeros,
and a non-contiguous mask is the exact misconception this figure exists to
prevent. Every row must have exactly one boundary.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth,
shading, solid color fills and soft shadows. Not flat line art. Each bar is a
long low rectangular slab seen slightly from above with visible thickness.

Three horizontal bars, stacked with even vertical spacing. All three bars are the
same total length and the same thickness and they are left aligned with each
other.

Every bar is made of exactly TWO segments butted end to end: a blue #0D47A1
segment on the LEFT and a green #1B5E20 segment on the RIGHT. There is exactly
one color change in each bar. No bar has three or more segments. No bar alternates
colors. No bar starts with green.

TOP BAR: the blue segment is one quarter of the total length, the green segment
is the remaining three quarters.
MIDDLE BAR: the blue segment is one half of the total length, the green segment
is the other half.
BOTTOM BAR: the blue segment is three quarters of the total length, the green
segment is the remaining one quarter.

The three color changes therefore sit at one quarter, one half and three quarters
across, forming a staircase that steps to the right as the eye moves down. That
staircase is the subject of the image.

No text anywhere in the image. No numbers, no bit values, no labels, no titles,
no legend. No borders, frames or caption text. No watermark, no signature.
```

---

## Image 10 - ARP resolution sequence, third attempt

| Field | Value |
|---|---|
| Filename | `network-diagnostics-arp-resolution-sequence-03.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Diagnostics/Wide_Source_Block_With_Converging_Arrows.png` |
| Replaces | `network-diagnostics-arp-resolution-sequence-02.png` |
| Used on | Canvas page `Networking: Address Resolution Protocol` |
| Alt text | `One unit asking all four units on the left, and one of the four answering back` |
| Caption | `Figure 1. Everyone is asked. One answers. That is the whole protocol.` |

**What went wrong.** The `-01` had a fifth arrow ending in mid-air with its
arrowhead striking through the caption. The `-02` fixed the geometry and got the
count right, then came back with red and cyan speckle scattered across the middle
of the frame from a botched background matte. The shapes were fine. The
transparency was not. This prompt is the `-02` again with the background handling
spelled out.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background. The
transparency must be clean: fully opaque inside every shape, fully transparent
everywhere else, with no colored fringe, halo, speckle or stray pixels anywhere in
the empty space. Do not render on a colored backdrop and cut it out.

A richly rendered dimensional diagram, isometric view, with real depth, shading,
solid color fills and soft shadows. Not flat line art.

One rounded rectangular block in blue #0D47A1, drawn larger, sits at the left of
the frame. Four rounded rectangular blocks in a lighter blue are stacked in an
evenly spaced vertical column at the right of the frame.

FOUR thick orange #993300 arrows sweep from the right face of the single left
block, one to each of the four right blocks. Each arrow ends in a solid arrowhead
that touches the left face of its block. Exactly four orange arrows. None of them
ends in empty space.

ONE thick green #1B5E20 arrow sweeps from the THIRD block down in the right
column back to the left block, ending in a solid arrowhead that touches the right
face of the left block. It is drawn slightly thicker than the orange arrows so it
reads as the single reply. Exactly one green arrow.

The arrows curve gently and do not cross each other. The empty area between the
left block and the right column is clean transparent space with nothing floating
in it.

No text anywhere in the image. No labels, no addresses, no numbers, no titles, no
legend. No borders, frames or caption text. No watermark, no signature.
```

---

## Image 11 - Protocol comparison, second attempt

| Field | Value |
|---|---|
| Filename | `audio-protocols-protocol-comparison-matrix-03.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols/audio-protocols-protocol-comparison-matrix-03.png` |
| Replaces | `audio-protocols-protocol-comparison-matrix-02.png` |
| Used on | Canvas page `Networking: Protocol Comparison` |
| Alt text | `Four stacks of blocks of different heights compared across four rows` |
| Caption | `Figure 1. Four protocols, four questions. Taller is more of the thing the row asks about.` |

**What went wrong.** The `-02` is a grey grid with seven colored balls dropped on
it and two arrows off to one side. No rows, no columns, nothing being compared.
It carries no information. A comparison figure with no text has to compare
something you can see, so this asks for height instead of a table: four columns,
four rows, block height carries the answer. The page's own table carries the
names and the detail.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric view, with real depth, shading,
solid color fills and soft shadows. Not flat line art.

A grid of stacked blocks, four columns across and four rows deep, sitting on a
thin dark #212121 base plate seen in isometric.

Each of the sixteen positions holds a short stack of identical cubes. The number
of cubes in each stack is what carries the meaning, and the stacks must be
obviously different heights so the pattern reads at a glance. Use these heights,
given as four rows of four columns:

Row nearest the viewer:   4, 3, 2, 1
Second row:               1, 4, 3, 2
Third row:                3, 1, 4, 2
Far row:                  2, 4, 1, 3

Each COLUMN has its own color for every cube in it: column one blue #0D47A1,
column two green #1B5E20, column three orange #993300, column four red #B71C1C.
So color identifies the column and height carries the value.

The grid is regular and evenly spaced, the base plate is plain, and nothing floats
above or beside the grid. No arrows, no annotations, no axis marks, no tick marks.

No text anywhere in the image. No numbers, no protocol names, no labels, no
titles, no legend. No borders, frames or caption text. No watermark, no signature.
```

---

## Where every file goes

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless
```

**This folder does not exist. Create it before saving anything from Group A.**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols
```

## After the files land

Tell me which group you finished, or that you finished both. Then I will:

1. Place the forty approved figures onto their pages. Twelve of them are
   referenced by nothing at all today, including every filter and EQ figure and
   the NAT and QoS figures that were pulled from their pages back in v5.
2. Move every page `src` from the `-01` name to the approved `-02` name.
3. Re-encode the five over-budget files listed above.
4. Ship the next cartridge.

Nothing points at any filename in this file yet, so nothing is showing a broken
image box while you work.

## Still needing a camera, not ChatGPT

Separate from this file, eight shots need photographing or sourcing rather than
generating. They are on the capture sheet, which has live preview slots that fill
in as each file lands:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/_briefs/2026-09-20-dapr-3255-capture-sheet-v6-pages.html
```

## The review contact sheets

The nine sheets I read every generated file on are here, if you want to see what
I saw:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/_briefs/_review
```
