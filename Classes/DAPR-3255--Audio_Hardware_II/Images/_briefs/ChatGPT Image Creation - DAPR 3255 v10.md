# ChatGPT Image Creation - DAPR 3255 v10

Generated 2026-09-22. **This is the only DAPR 3255 image brief.** It replaces
`ChatGPT Image Creation - DAPR 3255 v9.md`, which is superseded.

**Five prompts.** I re-read Standards §20 and the cartridge skill properly and then
opened every image in the course, composited on white first. That found four
things ChatGPT cannot fix and removed one prompt that was never needed.

| | Prompts |
|---|---|
| v7 brief | 51 |
| v8, after finding you had already run 47 | 11 |
| v9, after checking the `-01` files on the pages | 7 |
| v10, after the full review | 6 |
| **v10 as shipped, after finding one already generated** | **5** |

## What I had been reading wrong

Two rules I was not applying, both of which changed the answer.

**§20.4b: composite on white before judging.** A transparent PNG viewed on a dark
background shows white speckle at every edge and looks like a botched matte. I
condemned two figures for exactly that and put a retry prompt in the brief for
one of them. Composited on white they are both clean.

| Figure | What I said | On white |
|---|---|---|
| `network-diagnostics-arp-resolution-sequence-02.png` | red and cyan speckle across the frame | **clean.** Four broadcast arrows, one reply, correct geometry. Prompt dropped |
| `ip-addressing-nat-translation-flow-02.png` | speckle at the edges | **clean.** Already on its page and correct |

**§20.5 and §20.5a: the image is not the delivery mechanism.** Every fact a figure
states also has to be in the page prose or the caption, and when a subject does
not fit a picture the honest answer is an HTML table instead of a picture. I had
been arguing with myself about labelled figures against unlabelled ones when the
rule was never about the image at all. Three page fixes came out of that, below.

## Four things that are not prompts

These are the real findings and none of them belongs in this file.

### Three defects inside the final exam

The skill says to open every image that appears in a quiz. Ten images carry
eleven graded questions on the final and **not one had ever been opened.** Three
were wrong. All three are fixed in the v11 cartridge by cropping, because they
are sourced schematic art and §20.1 rule 3 says a schematic symbol is never
generated.

| Image | Defect | Fix |
|---|---|---|
| `final-exam-symbol-07.png` | The word **SPST** is printed under the symbol, and SPST is the keyed answer. The question was a free point | Cropped the answer off |
| `final-exam-symbol-04.png` | Shows three inductor variants, the third being the International filled rectangle. **Resistor** is a distractor on this question, and the International resistor symbol on question 06 is the same rectangle | Cropped to the two US coil forms |
| `final-exam-symbol-10.png` | The stem reads "the symbols shown below are common ground symbols". Half the image is VCC, 5V and V+ **power** flags | Cropped to the three ground symbols |

The other seven are correct. Symbol 05 in particular is a good op-amp figure and
answers both questions that use it.

### A four-pin XLR on a student page

`network-foundations-analog-snake-vs-network-01.png` fans an analog multicore out
to fourteen connectors. **Every connector face is drawn with four holes.** An XLR
has three pins. It has been on `Networking: Introduction to Audio Networking` in
every version, in a course that teaches pin 2 hot and pin 3 cold on the Talkback
Box build in the same semester.

This is §20.1 rule 3, third scalp for the program after the two in DAPR 2255. It
was on the "cannot be generated" list in brief v7 and I left it on the page
anyway instead of pulling it.

**Removed from the page in v11.** It cannot be re-prompted. It needs a photograph
of a real multicore fan-out, so it is now on the capture sheet.

## Three page fixes, made in v11

Each one is a case of §20.5: the image states a fact the page did not.

| Page | What was wrong |
|---|---|
| `Networking: Subnet Masks and CIDR` | `ip-addressing-cidr-block-sizes-01.png` **is a table**: seven prefixes against seven host counts, rendered as pixels. §20.5a says that is an HTML table on the page, not a picture. Replaced with a real table, header cells and caption |
| `Networking: IP Address Ranges to Memorize` | The caption read "drawn to relative scale" and the bars are nowhere near it. A /8 is 256 times a /16 and the bar is about four times longer. Caption now states the true ratio in words |
| `Networking: IP Addressing Fundamentals` | The figure works 192.168.10.57 against 255.255.255.0 and the page never named either. Caption now states the example |
| `Networking: AVB and Milan` | The figure prints a 75 percent reserved, 25 percent best effort split and the page text never mentioned it. Caption now carries it |

Also removed: `network-diagnostics-mirror-against-tap-01.png` from the Wireshark
capture page. I put it there in v9 without noticing `capture-point-placement-01`
was already on that page showing a mirror and a tap, labelled and better.

## What the six prompts are

| Group | What it is | Prompts |
|---|---|---|
| **A** | The three `wireless/` figures still missing | 01 to 03 |
| **B** | Two figures where the one on the page teaches something false | 04, 05 |

### One wireless figure was already done, and Dropbox had hidden it

`wireless-microphone-against-iem-direction-01.png` exists, 1600 x 900, transparent
PNG, correct: three transmitters converging on one receiver, one transmitter
fanning out to three receivers. I did not find it in the last three passes because
Dropbox had put it in a folder called

```
wireless (Adam Olson's conflicted copy 2026-09-22)
```

rather than `wireless`. §20.4a renames a non conforming name on sight, so I have
copied the file into a proper `wireless/` folder and **placed it** on
`Wireless: System Architecture`, which had no figure at all.

**The conflicted copy folder is still there and I cannot delete it.** Delete it by
hand so the repo does not carry the picture twice:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless (Adam Olson's conflicted copy 2026-09-22)
```

| Prompt | The figure today | Why it must be replaced |
|---|---|---|
| 04 | `electronics-opamp-inverting-vs-noninverting-01.png` | The non-inverting half has **no input at all**, a bare stub ending in empty space. The `-02` retry then ran the feedback to the plus input alongside the signal, which is positive feedback with no negative feedback. Two wrong versions, so this prompt spells the wiring out node by node |
| 05 | nothing, the page has no alignments figure | The `-01` has the three stopband slopes in reverse order, so it was never placed |

**Prompt 04 is the only one of the five that a student can see today.** If you run
one, run that.

## Format, and a correction to the last three briefs

§20.5a: photorealistic is the house style, and **format follows style**. A
photorealistic image has its own lighting and shadow, so it is JPEG at quality 85
to 90 on its own background, never a transparent PNG. The transparent PNG rows in
§20.2 apply only to the one exception: a subject that is not a thing, which
becomes a richly rendered dimensional diagram.

All five prompts below are that exception, so all five are transparent PNG and
that is correct. §20.4b adds one thing I had not been asking for and now do: **the
prompts ask for a clean transparent background with no coloured fringe**, because
a bad matte is what made me condemn two good figures.

## Palette, from §3

`#212121` body dark, `#1B5E20` green, `#0D47A1` blue, `#B71C1C` red, `#993300`
orange, `#616161` grey, `#5D4037` brown.

## Text inside these images

§20.5: ask for no text at all. Prompt 04 is the single exception and asks for the
plus and minus signs inside the op-amp triangles, because which input the feedback
lands on is the whole point of the figure. That is two quoted characters, well
under the limit of four.

## Filenames

§20.4: a conforming filename is permanent and the revision counter is two digits.
Every retry gets the next number and the old file stays on disk; only the page's
`src` moves.

---

# Group A

**The three wireless figures still missing.** The `wireless/` folder now exists,
because I created it and moved the finished figure into it:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless
```

---

## Image 01 - Antenna radiation patterns

| Field | Value |
|---|---|
| Filename | `wireless-antenna-patterns-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/wireless-antenna-patterns-01.png` |
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

---

## Image 02 - Multipath null and diversity spacing

| Field | Value |
|---|---|
| Filename | `wireless-multipath-null-and-diversity-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/wireless-multipath-null-and-diversity-01.png` |
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

---

## Image 03 - Third order intermodulation

| Field | Value |
|---|---|
| Filename | `wireless-third-order-intermodulation-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/wireless-third-order-intermodulation-01.png` |
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

---

## Image 04 - Inverting against non-inverting, third attempt

| Field | Value |
|---|---|
| Filename | `electronics-opamp-inverting-vs-noninverting-03.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-opamp-inverting-vs-noninverting-03.png` |
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

---

## Image 05 - Three filter alignments, second attempt

| Field | Value |
|---|---|
| Filename | `electronics-filter-alignments-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-filter-alignments-02.png` |
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

---

## Where every file goes

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless
```

**This folder does not exist. Create it before saving anything from Group A.**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics
```

## Needs a camera, not ChatGPT

Nine shots now, up from eight. The multicore fan-out is the new one and it is the
only one of the nine that is replacing a figure already on a page.

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/_briefs/2026-09-20-dapr-3255-capture-sheet-v6-pages.html
```

## After the files land

Run the OCR label census, then tell me:

```
bash "/Users/adamwolson/Library/CloudStorage/Dropbox/Reference Files/Applications/AI Projects Standards/Work/Utah Valley University/Build Tools/ocr_census.sh" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images"
```

I will place the four wireless figures, move the op-amp page onto its retry, put
the alignments figure on the Active Filters page, and ship the next cartridge.

## The review material

Every image in the course, composited on white per §20.4b, plus the contact
sheets and the OCR census:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/_briefs/_review
```
