# DAPR 3255 Image Brief - v6 New Pages

Rewritten 2026-09-22. Supersedes the 2026-09-20 version of this file completely.
Run each prompt separately in ChatGPT. Save each result with the exact filename
shown, into the exact folder shown. Do not rename.

## Why this was rewritten

The 2026-09-20 version of this brief was written the day before Standards 20.5a,
and every one of its thirteen prompts broke the rule that section created. Do not
run that version. Three things changed:

| | 2026-09-20 brief said | Standards now say |
|---|---|---|
| Style | "Flat vector-style. No photorealism." | 20.5a repealed that exact line on 2026-09-21. Photorealistic is the house style, and the subjects that are not things get a **richly rendered dimensional diagram**, not flat line art |
| Text | Five to eleven exact labels per image | 20.5: **ask for no text at all**, and never more than four. Twelve of the first twenty-eight DAPR 2255 images failed, and every failure was text |
| Format | PNG-24 on white | Photoreal takes its own background as JPEG. The dimensional-diagram exception stays transparent PNG |

## What that did to the image list

Every subject here is an abstraction rather than an object, so all but one fall
under 20.5a's exception: a richly rendered dimensional diagram, transparent PNG.

Two images from the old brief are **gone**, because they cannot carry their
meaning in four words or fewer and the page already carries the same content as
a table. 20.5a and 8.1 both say an image with no reason to exist does not get
briefed:

- the spectrum-band chart, which needed five band names plus five tick labels
- the four loss mechanisms, which needed four panel labels and four captions

One image is **not generated at all**, because the correct file already exists in
the repo and has been sitting unused: `electronics-opamp-summing-amplifier-01.png`.
It is a correct drawing of exactly the circuit the new Summing Amplifier page
teaches. It goes back on a page rather than being replaced.

That leaves **eleven prompts** below, down from thirteen.

## House rules that apply to every prompt here

- Richly rendered dimensional diagram. Three-quarter or isometric view, real
  depth and shading, solid color fills, on a fully transparent background.
- Palette, from Standards 3: `#212121` body dark, `#1B5E20` green, `#0D47A1`
  blue, `#B71C1C` red, `#993300` orange, `#616161` grey.
- **No text anywhere**, unless the prompt quotes an exact label. None quotes more
  than three.
- No logo, brand mark, model number, product photograph, software interface,
  decorative people, borders, frames, title bars, or caption text baked in.
- One image per prompt.

---

## Image 01 - Q against bandwidth

| Field | Value |
|---|---|
| Filename | `electronics-filter-q-against-bandwidth-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-filter-q-against-bandwidth-01.png` |
| Used on | Canvas page `Electronics: Active Filters, Order, and Q` |
| Alt text | `Three bandpass curves sharing one center frequency, each narrower than the last` |
| Caption | `Figure 1. One center frequency, three values of Q. Widest is Q of 1, narrowest is Q of 10.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth and
shading and solid color fills. Not flat line art.

Three bandpass filter response curves rise from a common baseline and all peak at
the same point along the horizontal axis, at the same height. They are nested
inside one another. The widest curve is a broad gentle hill in blue #0D47A1. The
middle curve is noticeably narrower, in green #1B5E20. The narrowest is a tall
thin spike, in red #B71C1C. Each curve is rendered as a solid ribbon with
thickness and a soft shadow beneath it, so the three read as stacked physical
forms rather than drawn lines.

A thin dark #212121 baseline runs the width of the frame beneath them.

Reading direction is left to right.

No text anywhere in the image. No axis labels, no numbers, no legend. No logo,
brand mark, model number, or product photograph. No borders, frames, title bars,
or caption text. No watermark, no signature.
```

---

## Image 02 - Three second-order filter alignments

| Field | Value |
|---|---|
| Filename | `electronics-filter-alignments-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-filter-alignments-01.png` |
| Used on | Canvas page `Electronics: Active Filters, Order, and Q` |
| Alt text | `Three lowpass curves at the knee: one rolling off early, one flat to the corner, one peaking before it falls` |
| Caption | `Figure 2. Green is Bessel, blue is Butterworth, red is Chebyshev. Same order, three choices of Q.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth and
shading and solid color fills. Not flat line art.

Three lowpass filter response curves run left to right across the frame. All
three start flat at the same height on the left and fall away together on the
right at the same steep slope. They differ only at the knee where they turn down.

The green #1B5E20 curve begins bending downward earliest and has the gentlest,
roundest knee. The blue #0D47A1 curve stays flat further and turns down with a
sharper corner and no rise. The red #B71C1C curve rises into a small visible bump
just before the corner, then falls most steeply of the three.

Each curve is rendered as a solid ribbon with thickness and a soft shadow, so the
three read as stacked physical forms rather than drawn lines. A thin dark #212121
baseline runs beneath them.

Reading direction is left to right.

No text anywhere in the image. No axis labels, no numbers, no legend. No logo,
brand mark, model number, or product photograph. No borders, frames, title bars,
or caption text. No watermark, no signature.
```

---

## Image 03 - Parametric EQ boost and cut

| Field | Value |
|---|---|
| Filename | `electronics-parametric-eq-boost-and-cut-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-parametric-eq-boost-and-cut-01.png` |
| Used on | Canvas page `Electronics: Parametric EQ` |
| Alt text | `A family of EQ curves rising above and dipping below a flat center line, all at one frequency` |
| Caption | `Figure 1. Boost above, cut below, mirror images of each other. One filter produces both.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth and
shading and solid color fills. Not flat line art.

A straight horizontal reference line in dark #212121 runs across the middle of
the frame with visible thickness, like a flat ribbon seen at a slight angle.

Above it, three curves bulge upward, all centered at the same point along the
line, each taller than the last, in green #1B5E20. Below it, three curves dip
downward, exactly mirroring the three above in shape and depth, in red #B71C1C.

Every curve is rendered as a solid ribbon with thickness and a soft shadow so the
family reads as stacked physical forms. The symmetry between the curves above and
the curves below is exact and obvious.

Reading direction is left to right.

No text anywhere in the image. No axis labels, no numbers, no legend. No logo,
brand mark, model number, or product photograph. No borders, frames, title bars,
or caption text. No watermark, no signature.
```

---

## Image 04 - Constant Q against proportional Q

| Field | Value |
|---|---|
| Filename | `electronics-constant-q-against-proportional-q-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-constant-q-against-proportional-q-01.png` |
| Used on | Canvas page `Electronics: Parametric EQ` |
| Alt text | `Two families of boost curves side by side, one keeping its width as it grows, the other narrowing` |
| Caption | `Figure 2. Constant Q on the left, proportional Q on the right. Watch the width as the gain rises.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth and
shading and solid color fills. Not flat line art. The frame is divided into a
left half and a right half by a narrow vertical gap.

In the left half, four boost curves rise above a flat horizontal baseline, all
centered at the same point, each taller than the last. Every one of the four is
exactly the same width at its base. They are blue #0D47A1.

In the right half, four boost curves rise above a flat horizontal baseline to the
same four heights as the left half, but each taller curve is visibly narrower at
its base than the one below it, so the tallest is a thin spike. They are orange
#993300.

All curves are solid ribbons with thickness and soft shadows so they read as
physical forms. Baselines are dark #212121.

Reading direction is left to right.

No text anywhere in the image. No axis labels, no numbers, no legend, no panel
titles. No logo, brand mark, model number, or product photograph. No borders,
frames, title bars, or caption text. No watermark, no signature.
```

---

## Image 05 - Frequency scaling

| Field | Value |
|---|---|
| Filename | `electronics-frequency-scaling-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-frequency-scaling-01.png` |
| Used on | Canvas page `Electronics: Frequency and Component Scaling` |
| Alt text | `The same filter curve drawn twice, identical in shape, the second one shifted to the right` |
| Caption | `Figure 1. Scale the capacitors and the whole curve slides. The shape, which is Q, does not change.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, three-quarter view, with real depth and
shading and solid color fills. Not flat line art.

Two lowpass filter response curves sit on a common horizontal baseline. They are
identical in every dimension: same height, same width, same knee shape, same
roll-off slope. The only difference is position. The first, in grey #616161, sits
toward the left of the frame. The second, in blue #0D47A1, is the same curve
moved bodily to the right, well clear of the first.

A horizontal arrow in orange #993300 runs from the knee of the grey curve to the
knee of the blue curve, showing the shift.

Both curves are solid ribbons with thickness and soft shadows so they read as
physical forms. The baseline is dark #212121.

Reading direction is left to right.

No text anywhere in the image. No axis labels, no numbers, no component values,
no legend. No logo, brand mark, model number, or product photograph. No borders,
frames, title bars, or caption text. No watermark, no signature.
```

---

## Image 06 - A sound solder joint, macro

| Field | Value |
|---|---|
| Filename | `electronics-solder-joint-macro-01.jpg` |
| Format | **JPEG, quality 88, its own background** |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-solder-joint-macro-01.jpg` |
| Used on | Canvas page `Electronics: Soldering Technique and Inspection` |
| Alt text | `Macro photograph of a through-hole solder joint with a smooth concave fillet rising to the lead` |
| Caption | `Figure 3. What a passing joint looks like. Solder has flowed onto the pad and up the lead, and the fillet curves inward.` |

This is the one photorealistic image in the brief. A solder joint is a real object
and 20.5a says a real object is photographed, not drawn. It carries no text, so
the page's table does the work of naming what passes and what does not.

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic macro photograph. Soft diffused studio lighting from above and
slightly to one side, very shallow depth of field, real metal with real surface
texture and real specular highlights.

Extreme close-up of a single through-hole solder joint on a green circuit board.
A tinned component lead rises vertically out of a copper pad. The solder has
flowed onto the pad and climbed the lead, forming a smooth fillet that curves
inward in a shallow concave sweep from the pad up to the lead. The joint is
bright and slightly satin, not dull and not mirror-bright. The outline of the
lead is still visible through the solder rather than buried in it.

The board fills the lower part of the frame and falls out of focus toward the
back. One or two neighboring pads are visible but soft.

No text anywhere in the image. No silkscreen legend, no printed part numbers, no
component markings, no logo, brand mark, or model number. No hands, no tools, no
people. No borders, frames, title bars, or caption text. No watermark, no
signature.
```

---

## Image 07 - Microphone system against in-ear system

| Field | Value |
|---|---|
| Filename | `wireless-microphone-against-iem-direction-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless/wireless-microphone-against-iem-direction-01.png` |
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

## Image 08 - Antenna radiation patterns

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

## Image 09 - Multipath null and diversity spacing

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

## Image 10 - Third order intermodulation

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

## Image 11 - Port mirroring against a network tap

| Field | Value |
|---|---|
| Filename | `network-diagnostics-mirror-against-tap-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/network-diagnostics-mirror-against-tap-01.png` |
| Used on | Canvas page `Software: Network Capture and Analysis` |
| Alt text | `A switch copying traffic out to a third device on the left, and a small unit inserted in the link doing the same on the right` |
| Caption | `Figure 1. Port mirroring on the left is a switch feature you configure. A tap on the right is a device you insert.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric view, with real depth and
shading and solid color fills. Not flat line art.

The frame is divided into a left half and a right half by a narrow vertical gap.

In the left half, two small rounded blocks sit at the top, both connected by
thick blue #0D47A1 tubes down into one wide flat slab below them, drawn in
isometric with visible thickness and a shadow, in dark #212121. From one end of
that slab, a thinner grey #616161 tube runs down and out to a third small rounded
block at the bottom.

In the right half, two small rounded blocks sit at the left and right of a
horizontal blue #0D47A1 tube that connects them directly. A small cube in grey
#616161 is inserted into the middle of that tube, sitting inline with it. From
the underside of that cube, a thinner grey tube runs down to a third small rounded
block at the bottom.

Both halves show the same outcome reached two different ways, and the difference
between a copy taken out of a slab and a unit inserted into the line should be
obvious.

Reading direction is left to right.

No text anywhere in the image. No labels, no port numbers, no legend, no titles.
No logo, brand mark, model number, product photograph, rack ears, or front-panel
detail. No borders, frames, title bars, or caption text. No watermark, no
signature.
```

---

## Where the files go

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics
```

6 files: `electronics-filter-q-against-bandwidth-01.png`,
`electronics-filter-alignments-01.png`,
`electronics-parametric-eq-boost-and-cut-01.png`,
`electronics-constant-q-against-proportional-q-01.png`,
`electronics-frequency-scaling-01.png`,
`electronics-solder-joint-macro-01.jpg`

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless
```

4 files: `wireless-microphone-against-iem-direction-01.png`,
`wireless-antenna-patterns-01.png`,
`wireless-multipath-null-and-diversity-01.png`,
`wireless-third-order-intermodulation-01.png`

**This folder does not exist. Create it.**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics
```

1 file: `network-diagnostics-mirror-against-tap-01.png`

---

## What the pages get instead of the two dropped images

- **Wireless: RF Spectrum Fundamentals** already carries the band table and the
  quarter-wave length table. They say everything the dropped spectrum chart would
  have said, and they say it in text a screen reader can read.
- The same page already carries the four loss mechanisms as a three-column table
  with the response to each. That is better than four unlabeled panels.

Neither page needs an image added. 8.1: an image with no reason to exist does not
get briefed.

---

## After the files land

Tell me and I will write the img tags onto the pages in one pass with the alt
text and captions above, and reship the cartridge. Nothing on those pages points
at these filenames yet, so no page is showing a broken box in the meantime.
