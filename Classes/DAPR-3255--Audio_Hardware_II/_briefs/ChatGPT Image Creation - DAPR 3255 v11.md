# ChatGPT Image Creation - DAPR 3255 v11

Generated 2026-09-22. **This is the only DAPR 3255 image brief.** It replaces
`ChatGPT Image Creation - DAPR 3255 v10.md`, which is superseded.

**Two prompts.** Everything else is either done or is not a ChatGPT job.

| | Prompts |
|---|---|
| v7 | 51 |
| v8, after finding you had already run 47 of them | 11 |
| v9, after checking the `-01` files on the pages | 7 |
| v10, after the full review composited on white | 5 |
| **v11, after finding all four wireless figures finished** | **2** |

## All four wireless figures are done and placed

They were in a Dropbox conflicted copy folder, which is why three passes missed
them. All four are correct, 1600 x 900, transparent PNG, and all four are now
placed in the v12 cartridge:

| Figure | Page | Verdict |
|---|---|---|
| `wireless-microphone-against-iem-direction-01.png` | Wireless: System Architecture | Three transmitters converging on one receiver, one transmitter fanning to three. Correct |
| `wireless-antenna-patterns-01.png` | Wireless: Antennas and Distribution | Sphere, figure of eight, cardioid, narrow forward lobe. Correct progression of directivity |
| `wireless-multipath-null-and-diversity-01.png` | Wireless: Antennas and Distribution | Direct and reflected paths cancelling at one antenna and adding at the other. Exactly the diversity point |
| `wireless-third-order-intermodulation-01.png` | Wireless: Frequency Coordination | Two carriers with two products evenly spaced outside them. Correct |

**One thing for you:** I cannot delete, so the conflicted folder is still there and
the repo would carry one picture twice. Delete it by hand:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless (Adam Olson's conflicted copy 2026-09-22)
```

## What is left, and why only two

| Prompt | The figure today | Why it must be replaced |
|---|---|---|
| 01 | `electronics-opamp-inverting-vs-noninverting-01.png` | The non-inverting half has **no input at all**, a bare stub in empty space. The `-02` retry then ran the feedback to the plus input alongside the signal, which is positive feedback with no negative feedback. Two wrong versions, so this prompt spells the wiring out node by node |
| 02 | nothing, the page has no alignments figure | The `-01` has the three stopband slopes in reverse order, so it was never placed |

**Prompt 01 is the only one of the two that a student can see today.**

## The rest of the review is not ChatGPT work

Everything else the full image review turned up was fixed in the v12 cartridge
without a prompt, because §20.1 rule 3 forbids generating any of it. The v12
changelog has the detail. In short: three wrong images inside the final exam
cropped, a four-pin XLR pulled off a student page, eight destroyed figures
rebuilt on the schematic symbols page from sourced art, three hot-linked
Wikimedia images moved into the repo, and one figure that was really a table
turned into a table.

## Text inside these two images

§20.5: ask for no text at all. Prompt 01 is the exception and asks for the plus
and minus signs inside the op-amp triangles, because which input the feedback
lands on is the whole point of the figure. Two quoted characters, under the
limit of four.

## Palette, from §3

`#212121` body dark, `#1B5E20` green, `#0D47A1` blue, `#B71C1C` red, `#993300`
orange, `#616161` grey, `#5D4037` brown.

## Filenames

§20.4: a conforming filename is permanent and the revision counter is two digits.
Both retries below take the next number and the old file stays on disk.

## Still needs a camera, not ChatGPT

Nine shots, and the multicore fan-out is the one that replaces a figure already
pulled off a page:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/_briefs/2026-09-20-dapr-3255-capture-sheet-v6-pages.html
```

---

## Image 01 - Inverting against non-inverting, third attempt

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

---

---

## Image 02 - Three filter alignments, second attempt

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
