# ChatGPT Image Creation - DAPR 3255 v9

Generated 2026-09-22. **This is the only DAPR 3255 image brief.** It replaces
`ChatGPT Image Creation - DAPR 3255 v8.md`, which is superseded.

**Seven prompts.** The v8 file had eleven. Four of those eleven turned out to be
unnecessary, and finding out why also turned up a mistake of mine that had to be
undone. Both are explained below, because the reason matters more than the count.

| | Prompts |
|---|---|
| v7 brief | 51 |
| v8 brief, after I found you had already run 47 of them | 11 |
| **v9 brief, after checking what is actually on the pages today** | **7** |

## Why four prompts came off the list

In v8 I sent seven figures back as defective. That was right about the new `-02`
files. What I had not done was look at the `-01` file each one was replacing. On
four of the seven the `-01` sitting on the page right now is **correct, labelled
and better than anything a retry would produce.** There is nothing to fix.

| Dropped prompt | What the `-01` on the page actually is |
|---|---|
| AC against DC | A correct two-panel plot with a dashed zero line, labelled axes reading Volts and Time, labelled DC and AC, and an AC wave that clearly crosses above and below zero. Exactly the figure the `-02` failed to be |
| Voltage divider bias | A fully correct schematic, labelled +V, R1, R2, Rc, Re, with both divider legs reaching a common ground rail and an NPN whose emitter arrow points the right way |
| Subnet mask bit boundary | Three labelled bars reading 254 usable, two of 126 usable, four of 62 usable. The arithmetic is right |
| Protocol comparison | A labelled scatter with latency across the bottom, channel count up the side, and eight protocols named on it: AES50, AVB, Dante, AES67, Livewire+, Ravenna, SMPTE ST 2110, NDI |

### And one of those four was my error, not a generator error

I told you the subnet mask `-02` was wrong because its third row alternated
blue, green, blue, green, and that a subnet mask cannot alternate because it is
contiguous ones then contiguous zeros. **That was wrong.** Looking at the `-01`,
the alternating colours never meant network against host bits. They mean four
separate subnets carved out of the block, which is correct and is what the `-01`
labels say. The `-02`'s only real problem is that the numbers are gone. I was
right that it is weaker and wrong about why.

That is the third thing I have had to correct in this set. The first two are in
the v8 brief.

## The bigger thing this turned up

I checked all thirty two figures I moved from `-01` to `-02` in the v9 cartridge,
by running OCR over both generations and counting the characters each one
carries. Twenty eight of the thirty two lost their labels.

| Figure | Labels on the -01 | On the -02 |
|---|---|---|
| Static against DHCP assignment | 128 characters | 0 |
| Troubleshooting decision tree | 114 | 0 |
| AVB and Milan reserved bandwidth | 110 | 0 |
| OSI seven layer stack | 91 | 0 |
| IPv6 address anatomy | 88 | 0 |
| Capture point placement | 86 | 0 |
| Ping round trip | 85 | 0 |
| Diagnostic ladder | 82 | 0 |
| plus twenty more | 13 to 78 | 0 |

A decision tree with no decisions written in it is not a decision tree. A seven
layer OSI stack with no layer names is seven coloured slabs. I had reviewed those
`-02` files for whether they were **correct** and they were. I never asked
whether they still **taught**, and on those twenty eight pages they do not.

All twenty eight are reverted in the v10 cartridge. Four figures stay on the
`-02`, because their `-01` carried no labels either and there the restyle is a
clean win.

**This is a standards question, not a prompt question.** Standards 20.5 says ask
for no text at all, and it is right about why: twelve of the first twenty eight
DAPR 2255 images failed and every failure was text. But that rule is aimed at a
figure whose subject is a shape. For a figure whose subject **is** its labels, an
address anatomy, a layer stack, a decision tree, a comparison scatter, it deletes
the content. 20.5 needs that distinction written into it, and that is your call.

Until it is, the gate carries it: preflight now hard fails a build that places a
figure carrying no labels when an older generation of the same figure carries
them. Run this after any new batch of images lands, before I build anything:

```
bash "/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Applications/AI Projects Standards/Work/Utah Valley University/Build Tools/ocr_census.sh" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images"
```

I have already run it once. It measured 103 figures, 43 of which carry labels.

## What the seven prompts are

| Group | What it is | Prompts |
|---|---|---|
| **A** | The four `wireless/` figures that were never generated | 01 to 04 |
| **B** | Three figures where the `-01` on the page is genuinely defective | 05 to 07 |

Group B is short now because in most cases the old figure was fine. These three
are not:

| Prompt | The figure on the page today | Why it has to be replaced |
|---|---|---|
| 05 | `electronics-opamp-inverting-vs-noninverting-01.png` | The non-inverting half has **no input at all**, just a bare stub ending in empty space. The `-02` retry then put the feedback on the plus input. Two wrong versions, so this prompt spells the wiring out node by node |
| 06 | nothing, the page has no alignments figure | The `-01` has the three stopband slopes in reverse order, so it was never placed. This is the page's only shot at the figure |
| 07 | `network-diagnostics-arp-resolution-sequence-01.png` | A fifth arrow ends in mid-air and its arrowhead strikes through the caption. The `-02` fixed the geometry and came back with red and cyan speckle across the frame |

**Prompt 05 and prompt 07 are the two that are in front of students.** If you only
run two, run those.

## A note on text in these seven

Six of the seven ask for no text, per Standards 20.5, and for these six that is
the right call: they are shapes, patterns and a schematic, not labelled data.
Prompt 05 is the exception and asks for the plus and minus signs inside the
op-amp triangles, because which input the feedback lands on is the entire point
of the figure and it cannot be read without them.

If a returned image has text in it beyond what its prompt asks for, regenerate.
Do not accept it and do not patch it in an editor.

## Palette, from Standards 3

`#212121` body dark, `#1B5E20` green, `#0D47A1` blue, `#B71C1C` red, `#993300`
orange, `#616161` grey, `#5D4037` brown.

## Filenames never get overwritten

Standards 20.4: a conforming filename is permanent. Every retry gets the next
number, not the number it replaces. The old file stays on disk and the page's
`src` moves. That is why prompts 05 and 07 end `-03`.

---

# Group A

**The four figures that were never generated.** The `wireless/` folder does not
exist. Create it before saving anything in this group:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless
```

These four are unchanged from the v7 and v8 briefs. Nothing about them was ever
wrong; they simply never ran.

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

---

## Image 06 - Three filter alignments, second attempt

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

---

## Image 07 - ARP resolution sequence, third attempt

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
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics
```

## After the files land

Run the OCR census, then tell me. I will place the four wireless figures, move
the op-amp and ARP pages onto the retries, put the filter alignments figure on
the Active Filters page, and ship the next cartridge.

Nothing points at any filename in this file yet, so nothing is showing a broken
image box while you work.

## Still needing a camera, not ChatGPT

Eight shots need photographing or sourcing rather than generating. They are on
the capture sheet, which has live preview slots that fill as each file lands:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/_briefs/2026-09-20-dapr-3255-capture-sheet-v6-pages.html
```

## The review material

The nine contact sheets I read every generated figure on, and the OCR label
census, are both here:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/_briefs/_review
```
