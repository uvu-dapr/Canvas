# DAPR 3255 Image Brief - v6 New Pages

Generated 2026-09-20. Thirteen conceptual diagrams for the fifteen pages added
in v6. Run each prompt separately in ChatGPT. Save each result with the exact
filename shown, into the exact folder shown. Do not rename.

Real hardware and real software are **not** in this brief. Those are on the
capture sheet that ships beside it:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/_briefs/2026-09-20-dapr-3255-capture-sheet-v6-pages.html
```

Every prompt below asks for a **white background**, per Section 20.5, so the
compositing question in 20.4b never arises. All are PNG-24 at 1600 x 900.

## House rules that apply to every prompt here

- Flat vector-style technical diagram. Clean line weights.
- No gradients, no drop shadows, no 3D, no photorealism, no watermark, no signature.
- No logo, brand mark, model number, product photograph or hardware likeness.
- No borders, frames, title bars or caption text.
- No text other than the labels each prompt lists.
- Palette: `#212121` for text and outlines, `#0D47A1` blue, `#1B5E20` green,
  `#B71C1C` red, `#E65100` orange, `#616161` grey.

---

## Electronics

### Image 01 - Summing amplifier at the virtual ground

| Field | Value |
|---|---|
| Filename | `electronics-summing-node-isolation-01.png` |
| Folder | `Images/electronics/` |
| Used on | `Electronics: The Summing Amplifier` |
| Alt text | `Three input resistors meeting at an op-amp summing node held at zero volts, with one feedback resistor to the output` |
| Caption | `Figure 1. Three sources, one node, and no path between them.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style schematic drawing. Clean line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

Draw an op-amp as a triangle pointing right, with a minus sign on the upper
input and a plus sign on the lower input. The plus input connects down to a
ground symbol.

From the far left, draw three horizontal signal lines stacked vertically,
labeled exactly "V1", "V2" and "V3" at their left ends. Each line passes through
its own resistor, labeled exactly "R1", "R2" and "R3", and then all three meet at
a single junction dot immediately to the left of the minus input.

Label that junction dot with a small callout box reading exactly "0 V".

Draw a resistor labeled exactly "Rf" running from the junction, over the top of
the triangle, down to the output line. Label the line leaving the triangle tip
exactly "Vout".

Use #0D47A1 for the triangle, #1B5E20 for the junction dot and its callout box
outline, and #212121 for all wires, resistors, ground symbol and text.

Reading direction is left to right.

Do not draw any logo, brand mark, model number, product photograph or breadboard.
Do not include borders, frames, title bars or caption text. Do not add any text
other than the labels listed above.
```

### Image 02 - Q against bandwidth

| Field | Value |
|---|---|
| Filename | `electronics-filter-q-against-bandwidth-01.png` |
| Folder | `Images/electronics/` |
| Used on | `Electronics: Active Filters, Order, and Q` |
| Alt text | `Three bandpass curves on one set of axes, all centered at one kilohertz, narrowing as Q rises` |
| Caption | `Figure 1. Same center frequency, three values of Q. High Q means narrow.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style line graph. Clean line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Draw a horizontal axis labeled exactly "Frequency" with three tick labels
reading exactly "100 Hz", "1 kHz" and "10 kHz", spaced logarithmically. Draw a
vertical axis labeled exactly "Level" with tick labels reading exactly "0 dB"
and "-3 dB".

Draw a horizontal dashed grey line across the plot at the -3 dB level.

Draw three bandpass response curves, all peaking at 1 kHz at the 0 dB level.
The widest is #0D47A1 and labeled exactly "Q = 1". The middle one is #1B5E20 and
labeled exactly "Q = 5". The narrowest is #B71C1C and labeled exactly "Q = 10".
Place each label at the top of its own curve.

Where the widest curve crosses the dashed -3 dB line, draw a horizontal
double-headed arrow between the two crossing points, labeled exactly "BW".

Use #212121 for axes, text and the arrow.

Do not draw any logo, brand mark or product photograph. Do not include borders,
frames, title bars or caption text. Do not add any text other than the labels
listed above.
```

### Image 03 - Three second-order filter alignments

| Field | Value |
|---|---|
| Filename | `electronics-filter-alignments-bessel-butterworth-chebyshev-01.png` |
| Folder | `Images/electronics/` |
| Used on | `Electronics: Active Filters, Order, and Q` |
| Alt text | `Three lowpass responses compared at the knee: Bessel rolling off earliest, Butterworth flat to the corner, Chebyshev peaking before it falls` |
| Caption | `Figure 2. The same order, three choices of Q, three different knees.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style line graph. Clean line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Draw a horizontal axis labeled exactly "Frequency" and a vertical axis labeled
exactly "Level", with a horizontal dashed grey line labeled exactly "-3 dB".

Draw three lowpass response curves that share the same cutoff region and then
fall away together at the same slope.

The first is #1B5E20, labeled exactly "Bessel  Q = 0.577", and begins rolling off
earliest with the gentlest knee and no peak.

The second is #0D47A1, labeled exactly "Butterworth  Q = 0.707", stays flat
further than the first and turns down with no peak.

The third is #B71C1C, labeled exactly "Chebyshev  Q = 2", rises into a small
visible peak just before the cutoff and then falls most steeply.

Place each label to the right of its own curve, clear of the others.

Use #212121 for axes and text.

Do not draw any logo, brand mark or product photograph. Do not include borders,
frames, title bars or caption text. Do not add any text other than the labels
listed above.
```

### Image 04 - Parametric EQ, boost and cut from one bandpass

| Field | Value |
|---|---|
| Filename | `electronics-parametric-eq-boost-and-cut-01.png` |
| Folder | `Images/electronics/` |
| Used on | `Electronics: Parametric EQ` |
| Alt text | `A bandpass filter tapped off the main signal path and returned through a center-detented control that adds it in phase or out of phase` |
| Caption | `Figure 1. One filter, one control. In phase is boost, out of phase is cut.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style block diagram. Clean line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

Draw a horizontal main signal path across the upper third of the image, entering
at the far left labeled exactly "Vin" and ending at a circle containing a plus
sign on the right, whose output line is labeled exactly "Vout".

From a junction dot early on that main path, draw a line downward into a
rectangle labeled exactly "Bandpass filter". Beneath that rectangle place two
small labels reading exactly "Frequency" and "Q", each with a short arrow
pointing up into the rectangle.

From the right side of the rectangle, draw a line into a vertical
potentiometer symbol drawn as a rectangle with a wiper arrow at its middle.
Label the top end exactly "+", the middle exactly "flat", and the bottom end
exactly "-". Label the potentiometer itself exactly "Gain".

Draw a line from the wiper up and to the right into the circle containing the
plus sign.

In the lower right corner, draw three small response curves stacked vertically:
one rising into a bump labeled exactly "boost", one flat line labeled exactly
"flat", and one dipping into a notch labeled exactly "cut".

Use #0D47A1 for the bandpass rectangle outline, #1B5E20 for the boost curve,
#B71C1C for the cut curve, and #212121 for everything else.

Reading direction is left to right.

Do not draw any logo, brand mark, model number or product photograph. Do not
include borders, frames, title bars or caption text. Do not add any text other
than the labels listed above.
```

### Image 05 - Constant Q against proportional Q

| Field | Value |
|---|---|
| Filename | `electronics-constant-q-against-proportional-q-01.png` |
| Folder | `Images/electronics/` |
| Used on | `Electronics: Parametric EQ` |
| Alt text | `Two families of EQ boost curves, one keeping its width as gain rises and one narrowing as gain rises` |
| Caption | `Figure 2. The same gain settings, two design philosophies.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style line graph, drawn as two panels side by side separated by a
thin vertical grey line. Clean line weights, no gradients, no drop shadows, no
3D, no photorealism, no watermark, no signature.

Each panel has a horizontal axis labeled exactly "Frequency" and a vertical axis
labeled exactly "Gain", with a horizontal line through the middle labeled
exactly "0 dB".

In the left panel, draw four boost curves rising above the 0 dB line, all
centered at the same frequency and all exactly the same width, with peaks at
progressively greater heights. Title this panel exactly "Constant Q".

In the right panel, draw four boost curves centered at the same frequency with
peaks at the same four heights as the left panel, but each taller curve is
visibly narrower than the one below it. Title this panel exactly "Proportional Q".

Use #0D47A1 for every curve in the left panel and #E65100 for every curve in the
right panel. Use #212121 for axes, titles and text.

Do not draw any logo, brand mark or product photograph. Do not include borders,
frames, title bars or caption text. Do not add any text other than the labels
listed above.
```

### Image 06 - Frequency scaling

| Field | Value |
|---|---|
| Filename | `electronics-frequency-scaling-same-filter-01.png` |
| Folder | `Images/electronics/` |
| Used on | `Electronics: Frequency and Component Scaling` |
| Alt text | `The same filter drawn twice with the capacitor divided by ten, and the response curve moving up one decade` |
| Caption | `Figure 1. Divide the capacitors by ten and the cutoff moves a decade. Q does not move.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style technical diagram. Clean line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

Divide the image into an upper half and a lower half with a thin horizontal grey
line.

In the upper half, on the left, draw a simple RC lowpass: a horizontal line from
the left through a resistor labeled exactly "R = 15.9k" to a junction, with a
capacitor from that junction down to a ground symbol, labeled exactly "C = 10 nF".
On the right of the upper half, draw a lowpass response curve with its corner
marked by a vertical dashed line labeled exactly "1 kHz".

In the lower half, draw the identical circuit with the resistor labeled exactly
"R = 15.9k" and the capacitor labeled exactly "C = 1 nF", and a lowpass response
curve of exactly the same shape with its corner marked exactly "10 kHz",
positioned one decade to the right of the upper one.

Between the two halves on the left, draw a downward arrow labeled exactly
"C divided by 10".

Use #0D47A1 for both response curves, #E65100 for the two capacitor labels and
the downward arrow, and #212121 for everything else.

Do not draw any logo, brand mark, model number or product photograph. Do not
include borders, frames, title bars or caption text. Do not add any text other
than the labels listed above.
```

### Image 07 - Solder joint acceptance

| Field | Value |
|---|---|
| Filename | `electronics-solder-fillet-acceptance-01.png` |
| Folder | `Images/electronics/` |
| Used on | `Electronics: Soldering Technique and Inspection` |
| Alt text | `Cross sections of three through-hole solder joints: a concave wetted fillet, a convex unwetted blob, and a joint with a void` |
| Caption | `Figure 3. Concave and wetted passes. Convex and balled does not.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style cross-section diagram, drawn as three panels side by side
separated by thin vertical grey lines. Clean line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

Each panel shows the same cross section: a horizontal board drawn as a thin
rectangle, a plated hole through it, a vertical component lead passing through
the hole, and a copper pad on the top surface.

In the first panel, draw the solder as a smooth concave fillet curving up from
the pad to the lead at a shallow angle, with the outline of the lead still
visible through it. Label this panel exactly "Acceptable". Draw a small angle
marker where the solder meets the pad, labeled exactly "shallow wetting angle".

In the second panel, draw the solder as a rounded convex ball sitting on top of
the pad, meeting it at a steep angle and not spreading. Label this panel exactly
"Not wetted".

In the third panel, draw a concave fillet with a visible round gap inside the
solder body. Label this panel exactly "Void".

Use #1B5E20 for the solder in the first panel, #B71C1C for the solder in the
second and third panels, and #212121 for the board, pad, lead and all text.

Do not draw any logo, brand mark, model number or product photograph. Do not
include borders, frames, title bars or caption text. Do not add any text other
than the labels listed above.
```

---

## Wireless

### Image 08 - Where audio sits in the spectrum

| Field | Value |
|---|---|
| Filename | `wireless-audio-bands-on-the-spectrum-01.png` |
| Folder | `Images/wireless/` (create it) |
| Used on | `Wireless: RF Spectrum Fundamentals` |
| Alt text | `A logarithmic frequency axis from thirty megahertz to six gigahertz with the bands used by professional wireless audio marked on it` |
| Caption | `Figure 1. Four bands, and only one of them is where the work happens.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style diagram. Clean line weights, no gradients, no drop shadows, no
3D, no photorealism, no watermark, no signature.

Draw one long horizontal axis across the image, with logarithmic tick labels
reading exactly "30 MHz", "300 MHz", "1 GHz", "3 GHz" and "6 GHz".

Above the axis, draw four horizontal bars of different colors spanning their
frequency ranges, each with a label above it:

A bar from 30 MHz to 300 MHz labeled exactly "VHF".
A wide bar from 470 MHz to 700 MHz labeled exactly "UHF".
A narrow bar from 902 MHz to 928 MHz labeled exactly "900 MHz ISM".
A narrow bar from 2400 MHz to 2483 MHz labeled exactly "2.4 GHz ISM".
A bar from 5150 MHz to 5850 MHz labeled exactly "5 GHz".

Below the axis, draw a bracket under the UHF bar with a label reading exactly
"where professional wireless audio lives".

Use #616161 for the VHF bar, #0D47A1 for the UHF bar, and #E65100 for the three
remaining bars. Use #212121 for the axis, the bracket and all text.

Reading direction is left to right, low frequency to high.

Do not draw any logo, brand mark, model number or product photograph. Do not
include borders, frames, title bars or caption text. Do not add any text other
than the labels listed above.
```

### Image 09 - The four loss mechanisms

| Field | Value |
|---|---|
| Filename | `wireless-four-loss-mechanisms-01.png` |
| Folder | `Images/wireless/` |
| Used on | `Wireless: RF Spectrum Fundamentals` |
| Alt text | `One stage scene showing signal spreading with distance, being absorbed by an audience, reflecting off a wall, and competing with another transmitter` |
| Caption | `Figure 2. Four different problems, four different fixes.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style diagram divided into four equal panels in a two by two grid,
separated by thin grey lines. Clean line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Panel one, top left: a small circle on the left with three expanding arcs
spreading to the right and becoming fainter. Label this panel exactly
"Free space path loss" and add a small label reading exactly "-6 dB per doubling".

Panel two, top right: a small circle on the left, a row of simple filled ovals
representing an audience in the middle, and a weakened arrow emerging on the
right. Label this panel exactly "Absorption".

Panel three, bottom left: a small circle on the left with two arrows reaching the
same point on the right, one direct and one bouncing off a vertical line at the
top. At the meeting point draw a small burst marker. Label this panel exactly
"Multipath".

Panel four, bottom right: two small circles on the left, each with an arrow
pointing to the same receiver on the right, one arrow drawn as a solid line and
one as a jagged line. Label this panel exactly "Interference".

Use #0D47A1 for the wanted signal in every panel, #B71C1C for the jagged
interfering signal and the burst marker, #616161 for the audience ovals and the
reflecting wall, and #212121 for all text.

Do not draw any logo, brand mark, model number, product photograph or recognisable
microphone. Do not include borders, frames, title bars or caption text. Do not add
any text other than the labels listed above.
```

### Image 10 - Microphone system against IEM system

| Field | Value |
|---|---|
| Filename | `wireless-microphone-against-iem-direction-01.png` |
| Folder | `Images/wireless/` |
| Used on | `Wireless: System Architecture` |
| Alt text | `A microphone system with many transmitters on stage feeding one rack, beside an in-ear system with one rack transmitter feeding many bodypacks` |
| Caption | `Figure 1. The arrows point the other way, and that changes the deployment.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style block diagram, drawn as two panels side by side separated by a
thin vertical grey line. Clean line weights, no gradients, no drop shadows, no
3D, no photorealism, no watermark, no signature.

In the left panel, draw three small rectangles stacked vertically on the left,
labeled exactly "TX", "TX" and "TX", with a bracket beside them labeled exactly
"stage". Draw three arrows from them pointing right into a single larger
rectangle labeled exactly "RX rack". Title this panel exactly
"Wireless microphones".

In the right panel, draw one larger rectangle on the left labeled exactly
"TX rack", with three arrows pointing right into three small rectangles stacked
vertically, labeled exactly "RX", "RX" and "RX", with a bracket beside them
labeled exactly "stage". Title this panel exactly "In-ear monitors".

Use #0D47A1 for every arrow in the left panel and #E65100 for every arrow in the
right panel. Use #212121 for all rectangles, brackets and text.

Do not draw any logo, brand mark, model number or product photograph. Do not
include borders, frames, title bars or caption text. Do not add any text other
than the labels listed above.
```

### Image 11 - Antenna patterns

| Field | Value |
|---|---|
| Filename | `wireless-antenna-patterns-01.png` |
| Folder | `Images/wireless/` |
| Used on | `Wireless: Antennas and Distribution` |
| Alt text | `Four radiation patterns drawn in plan view: omnidirectional, a wide directional lobe, a narrow directional lobe, and a dipole figure of eight` |
| Caption | `Figure 1. Gain is pattern concentration, not amplification.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style polar pattern diagram, drawn as four equal panels in a row
separated by thin vertical grey lines. Clean line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

Each panel contains a small dot at its center representing the antenna, with two
faint concentric grey circles behind the pattern for scale.

Panel one: a full circle around the dot. Label it exactly "Quarter wave whip"
and beneath that exactly "omnidirectional, 0 dBi".

Panel two: a figure of eight pattern, two equal lobes pointing left and right.
Label it exactly "Half wave dipole" and beneath that exactly "omnidirectional in
plan, about 2 dBi".

Panel three: one broad lobe pointing right with a small lobe behind it pointing
left. Label it exactly "Log periodic" and beneath that exactly
"directional, 5 to 7 dBi".

Panel four: one narrow lobe pointing right, longer and thinner than panel three,
with almost nothing behind it. Label it exactly "Helical" and beneath that
exactly "directional, 8 to 12 dBi".

Use #0D47A1 for every pattern outline, filled with a very light tint of the same
color. Use #212121 for the center dots and all text, and light grey for the
scale circles.

Do not draw any logo, brand mark, model number, product photograph or antenna
hardware. Do not include borders, frames, title bars or caption text. Do not add
any text other than the labels listed above.
```

### Image 12 - Multipath null and diversity spacing

| Field | Value |
|---|---|
| Filename | `wireless-multipath-null-and-diversity-01.png` |
| Folder | `Images/wireless/` |
| Used on | `Wireless: Antennas and Distribution` |
| Alt text | `A direct path and a reflected path arriving out of phase at one antenna while a second antenna a wavelength away receives them in phase` |
| Caption | `Figure 2. A null is a place, not a frequency. Two antennas are rarely in the same place.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style diagram. Clean line weights, no gradients, no drop shadows, no
3D, no photorealism, no watermark, no signature.

On the left, draw a small circle labeled exactly "TX".

On the right, draw two short vertical lines representing antennas, one above the
other, separated by a clear vertical gap. Label the upper one exactly "Antenna A"
and the lower one exactly "Antenna B". Draw a vertical double-headed arrow
between them labeled exactly "one wavelength".

From the TX, draw two paths to Antenna A: one straight line labeled exactly
"direct", and one that travels up, bounces off a horizontal line at the top of
the image labeled exactly "reflecting surface", and comes down to Antenna A.

Beside Antenna A, draw two small sine waves one above the other, drawn exactly
out of phase with each other, and beneath them a flat line. Label this group
exactly "arrives out of phase: null".

Beside Antenna B, draw two small sine waves one above the other, drawn in phase
with each other, and beneath them a larger sine wave. Label this group exactly
"arrives in phase: signal".

Use #0D47A1 for the direct path, #E65100 for the reflected path, #B71C1C for the
flat line at Antenna A, #1B5E20 for the larger sine at Antenna B, and #212121 for
everything else.

Do not draw any logo, brand mark, model number, product photograph or antenna
hardware. Do not include borders, frames, title bars or caption text. Do not add
any text other than the labels listed above.
```

### Image 13 - Third order intermodulation

| Field | Value |
|---|---|
| Filename | `wireless-third-order-intermodulation-01.png` |
| Folder | `Images/wireless/` |
| Used on | `Wireless: Frequency Coordination and Troubleshooting` |
| Alt text | `Two carriers on a frequency axis with their two third order products falling either side of them at equal spacing` |
| Caption | `Figure 1. Two transmitters, four signals. The two you did not plan for are the problem.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style frequency plot. Clean line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

Draw a horizontal frequency axis with tick labels reading exactly "545.000",
"550.000", "555.000" and "560.000", evenly spaced, and an axis label reading
exactly "MHz".

At 550.000 and 555.000 draw two tall solid vertical bars. Label the first exactly
"f1" and the second exactly "f2".

At 545.000 and 560.000 draw two shorter dashed vertical bars, about half the
height of the solid ones. Label the one at 545.000 exactly "2f1 - f2" and the one
at 560.000 exactly "2f2 - f1".

Beneath the axis, draw a bracket spanning all four bars with a label reading
exactly "two transmitters, four signals in the air".

Use #0D47A1 for the two solid bars and #B71C1C for the two dashed bars. Use
#212121 for the axis, bracket and all text.

Reading direction is left to right, low frequency to high.

Do not draw any logo, brand mark, model number or product photograph. Do not
include borders, frames, title bars or caption text. Do not add any text other
than the labels listed above.
```

---

## Networking and software

### Image 14 - Port mirroring against a network tap

| Field | Value |
|---|---|
| Filename | `network-diagnostics-mirror-against-tap-01.png` |
| Folder | `Images/network-diagnostics/` |
| Used on | `Software: Network Capture and Analysis` |
| Alt text | `A switch copying traffic from one port to a capture laptop, beside a passive tap inserted in the link doing the same thing` |
| Caption | `Figure 1. One is a switch feature you configure. The other is a device you insert.` |

```text
Create a 1600 x 900 pixel PNG on a solid white background.

Flat vector-style network diagram, drawn as two panels side by side separated by
a thin vertical grey line. Clean line weights, no gradients, no drop shadows, no
3D, no photorealism, no watermark, no signature.

In the left panel, draw two rectangles at the top labeled exactly "Device A" and
"Device B", both connected down into a wide rectangle labeled exactly "Managed
switch". From the switch, draw a dashed line down to a rectangle labeled exactly
"Capture laptop". Label the dashed line exactly "mirrored copy". Title this panel
exactly "Port mirroring".

In the right panel, draw two rectangles labeled exactly "Device A" and "Device B"
with a horizontal line between them. Insert a small square in the middle of that
line labeled exactly "Tap". From the tap, draw a dashed line down to a rectangle
labeled exactly "Capture laptop". Title this panel exactly "Network tap".

Use #0D47A1 for the solid data links, #616161 for both dashed capture lines, and
#212121 for all rectangles and text.

Do not draw any logo, brand mark, model number, product photograph or rack
hardware. Do not include borders, frames, title bars or caption text. Do not add
any text other than the labels listed above.
```

---

## Where the files go

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics
```

7 files: `electronics-summing-node-isolation-01.png`,
`electronics-filter-q-against-bandwidth-01.png`,
`electronics-filter-alignments-bessel-butterworth-chebyshev-01.png`,
`electronics-parametric-eq-boost-and-cut-01.png`,
`electronics-constant-q-against-proportional-q-01.png`,
`electronics-frequency-scaling-same-filter-01.png`,
`electronics-solder-fillet-acceptance-01.png`

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless
```

6 files: `wireless-audio-bands-on-the-spectrum-01.png`,
`wireless-four-loss-mechanisms-01.png`,
`wireless-microphone-against-iem-direction-01.png`,
`wireless-antenna-patterns-01.png`,
`wireless-multipath-null-and-diversity-01.png`,
`wireless-third-order-intermodulation-01.png`

This folder does not exist yet. Create it.

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics
```

1 file: `network-diagnostics-mirror-against-tap-01.png`

---

## After the files land

Tell me and I will write the `<img>` tags onto the seven pages in one pass, with
the alt text and captions above, and reship the cartridge. Nothing on those pages
points at these filenames yet, so no page is showing a broken box in the meantime.
