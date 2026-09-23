# ChatGPT Image Creation - DAPR 3255 v7

Generated 2026-09-22. **This is the only DAPR 3255 image brief.** It replaces
`Regenerations 01`, `Regenerations 02`, `Regenerations 03` and the
`v6 New Pages` brief, which are superseded and have been moved to
`Images/_briefs/_superseded/`.

Fifty-one prompts. Run each one separately in ChatGPT. Save each result with the
exact filename shown, into the exact folder shown. Do not rename anything.

## How to work this file

Work the groups in order. Group A is the urgent one.

| Group | What it is | Prompts | Why now |
|---|---|---|---|
| **A** | Figures that are on a page right now and are **wrong** | 01 to 04 | Two of the four are live in front of students. Do these first |
| **B** | Pages that have **no figure at all** | 05 to 15 | The fifteen pages added in v6. Nothing is broken, they are just bare |
| **C** | Figures that are correct but in the **old flat-vector style** | 16 to 51 | Cosmetic. The course reads fine today. Do these last |

Every prompt is self-contained. Nothing here depends on anything else here, so
you can stop after any group and the course is in a consistent state.

## The style, and why it changed

Standards 20.5a, set 2026-09-21, repealed the flat-vector line that governed every
image in this course until now. Everything below asks for a **richly rendered
dimensional diagram**: isometric or three-quarter, with real depth, shading, solid
fills and soft shadows. One prompt, number 09, asks for a photograph instead,
because a solder joint is a real object and 20.5a says a real object is
photographed rather than drawn.

**No prompt below asks for any text inside the image.** That is deliberate.
Standards 20.5 records that twelve of the first twenty-eight images generated for
DAPR 2255 failed, and every single failure was text: a label clipped by the frame,
two labels printed over each other, or a label silently dropped. The page carries
the heading, the caption, the table and the prose. The picture does not need a
word.

If a returned image has text in it anyway, regenerate. Do not accept it and do not
patch it in an editor.

## Palette, from Standards 3

`#212121` body dark, `#1B5E20` green, `#0D47A1` blue, `#B71C1C` red, `#993300`
orange, `#616161` grey, `#5D4037` brown.

## Five figures that are deliberately not in this file

These cannot be generated at all. Standards 20.1 rule 3 is locked and 20.5a
reaffirms it: a connector face with numbered pins, a front panel with ports, real
gear. A generated version comes back plausible and wrong, and a photorealistic
wrong answer is more convincing than a flat-vector one, not less.

| File | Why it is off limits | What to do instead |
|---|---|---|
| `network-foundations-t568a-t568b-pin-order-01.png` | Wire colors in numbered pin order. **I checked this one wire by wire on 2026-09-22 and it is correct.** Regenerating it risks trading a verified-correct figure for a wrong one | Leave it exactly as it is |
| `network-foundations-straight-through-vs-crossover-01.png` | RJ45 connector ends | Leave, or photograph two real cables |
| `network-configuration-managed-vs-unmanaged-switch-01.png` | Switch front panels with port detail | Leave, or use manufacturer product images |
| `network-foundations-analog-snake-vs-network-01.png` | Multicore with connector ends | Leave, or photograph the real thing |
| `electronics-breadboard-internal-connections-01.png` | The exact internal hole grouping is the teaching point, and a generator will get it wrong | Leave it as it is |

The seven Talkback Box photographs are already real photographs and are not in
this file either.


---

# Group A

**Group A. Wrong figures, live on pages.** Four. Two of these are in front of students right now. Everything else in this file can wait; these cannot.

---

## Image 01 - Op-amp inverting against non-inverting

| Field | Value |
|---|---|
| Filename | `electronics-opamp-inverting-vs-noninverting-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Used on | Canvas page `Electronics: Op-amp Circuits` |
| Alt text | `Inverting and non-inverting op-amp circuits side by side, each with its input and output shown` |
| Caption | `Figure 1. Where the signal enters is the whole difference. Left enters through a resistor to the minus input, right enters straight at the plus input.` |

**What is wrong with `-01`.** The inverting half on the left is correct and
complete. The non-inverting half on the right has the right topology, Rf from the
output back to the minus input and Rg from the minus input to ground, but **the
plus input is a bare stub that terminates in empty space.** There is no input
line and no source. The one thing the figure exists to show, that the signal
enters at the plus input, is the one thing missing. A student comparing the two
halves sees an amplifier with no input.

This was identified on 2026-09-20 and the replacement was never generated, so it
is still the live figure on the page.

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram of two electronic circuits, three-quarter
view, with real depth and shading and solid color fills. Components sit slightly
raised off the plane with soft shadows beneath them. Not flat line art.

The frame is divided into a left half and a right half by a narrow vertical gap.

LEFT CIRCUIT. An amplifier drawn as a triangle pointing right, in blue #0D47A1,
rendered with thickness like a solid wedge. A minus sign on its upper input, a
plus sign on its lower input. A horizontal wire enters from the far left edge of
the frame, passes through a resistor, and arrives at the minus input. A second
resistor runs from that same minus input node, up and over the top of the
triangle, and down to the wire leaving the triangle's tip. The plus input
connects downward to a ground symbol. The wire leaving the tip continues to the
right edge of the frame.

RIGHT CIRCUIT. An identical blue triangle pointing right, but with the plus sign
on its UPPER input and the minus sign on its LOWER input. A horizontal wire
enters from the far left of this half of the frame and runs directly to the plus
input, with no resistor in its path. This input wire must be clearly present and
must reach the edge of the frame, exactly as prominent as the input wire in the
left circuit. A resistor runs from the minus input down to a ground symbol. A
second resistor runs from that same minus input node, up and over the top of the
triangle, and down to the wire leaving the tip. The wire leaving the tip
continues to the right edge of the frame.

Both circuits must have a visible input wire entering from the left and a visible
output wire leaving to the right. Neither may have a wire that stops in empty
space.

All wires, resistors and ground symbols are dark #212121.

Reading direction is left to right, input on the left, output on the right.

No text anywhere in the image. No component values, no labels, no titles. No
logo, brand mark, model number, product photograph, or breadboard. No borders,
frames, title bars, or caption text. No watermark, no signature.
```

---

## Image 02 - ARP resolution sequence

| Field | Value |
|---|---|
| Filename | `network-diagnostics-arp-resolution-sequence-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/` |
| Used on | Canvas page `Networking: Address Resolution Protocol` |
| Alt text | `One device sending a question to four others, with only one of the four sending a reply back` |
| Caption | `Figure 1. The request goes to everyone. Only the device that owns the address answers, and it answers only the asker.` |

**What is wrong with `-01`.** Four hosts, so four request arrows. The figure draws
**five.** The fifth leaves the asking device, heads down and to the right, and
ends with an arrowhead in empty space. Worse, that arrowhead lands on top of the
caption text and strikes through the middle of the word "answers". Standards 20.4b
calls this class of defect presentation rather than substance, but it survives
compositing on white, so it is real.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric view, with real depth and
shading and solid color fills. Blocks sit raised off the plane with soft shadows.
Not flat line art.

One rounded block sits alone at the left of the frame, drawn in blue #0D47A1.

Four identical rounded blocks are stacked in a vertical column at the right of
the frame, evenly spaced, drawn in light blue.

EXACTLY FOUR thick arrows leave the left block, one to each of the four right
blocks, in orange #993300. Every arrow must terminate with its head touching the
edge of its destination block. There must be no fifth arrow, and no arrow that
ends anywhere other than on a block.

ONE thick arrow in green #1B5E20 returns from the third block down to the left
block. It is the only arrow travelling right to left, and it is noticeably
thicker than the orange ones so it reads as the single reply.

The count is the whole point: four out, one back.

Reading direction is left to right for the question, right to left for the reply.

No text anywhere in the image. No IP addresses, no device names, no letters, no
labels, no captions. No logo, brand mark, model number, or product photograph. No
borders, frames, title bars, or caption text. No watermark, no signature.
```

---

## Image 03 - NAT translation flow

| Field | Value |
|---|---|
| Filename | `ip-addressing-nat-translation-flow-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/` |
| Used on | Canvas page `Networking: Network Address Translation (NAT)` |
| Alt text | `A packet leaving with one address and returning with another, rewritten in the middle both ways` |
| Caption | `Figure 1. NAT rewrites the source address on the way out and the destination address on the reply. Outbound above, return below.` |

**What is wrong with `-01`.** On the return path both labels read "from". A packet
coming back from the internet is addressed **to** the public address, then **to**
the private one. As drawn, NAT appears to rewrite the source on the way back,
which is the opposite of what it does. It has been off the page since v5.

The rewrite below drops the address labels entirely, which removes the defect at
its root: the page's prose and table already carry the addresses.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric view, with real depth and
shading and solid color fills. Not flat line art.

Three objects sit in a row across the frame. At the left, a small rounded block in
blue #0D47A1. In the middle, a larger solid cube in orange #993300, raised higher
than the others with a clear shadow. At the right, a soft rounded cloud shape in
grey #616161.

An upper thick arrow in green #1B5E20 runs left to right, from the block, through
the orange cube, and on to the cloud. On the left side of the cube this arrow
carries three small blue cubes riding along it. On the right side of the cube, the
three small cubes riding along it are orange instead. The change of color happens
exactly at the cube.

A lower thick arrow in blue #0D47A1 runs right to left, from the cloud, through
the orange cube, and back to the block. On the right side of the cube this arrow
carries three small orange cubes riding along it. On the left side of the cube,
the three small cubes riding along it are blue instead. Again the change happens
exactly at the cube.

The symmetry is the point: something is swapped in the middle in both directions,
and the direction of travel differs between the two arrows.

Reading direction is left to right for the upper arrow.

No text anywhere in the image. No IP addresses, no numbers, no labels. No logo,
brand mark, model number, router hardware, or product photograph. No borders,
frames, title bars, or caption text. No watermark, no signature.
```

---

## Image 04 - QoS DSCP priority queue

| Field | Value |
|---|---|
| Filename | `network-architecture-qos-dscp-priority-queue-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture/` |
| Used on | Canvas page `Networking: Quality of Service` |
| Alt text | `Four streams of traffic entering a switch in mixed order and leaving sorted by priority` |
| Caption | `Figure 1. Marking decides what leaves first when the link is full. Red is clock, green is audio, blue is video, grey is everything else.` |

**What is wrong with `-01`.** It invents two class names. There is no "EF 34", EF
is DSCP 46 only and 34 is AF41, and there is no "AF 26", 26 is AF31. It has been
off the page since v5.

The rewrite drops the class names entirely rather than risking them again. The
page's table carries the correct markings, and those come from Audinate's current
Dante QoS documentation, not from the picture.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric view, with real depth and
shading and solid color fills. Not flat line art.

At the left of the frame, four horizontal streams of small cubes flow in from the
left edge toward the center, one stream above the other, evenly spaced. The top
stream is red #B71C1C, the second green #1B5E20, the third blue #0D47A1, the
fourth grey #616161. Within each stream the cubes are evenly spaced.

In the center, a solid three-dimensional wedge narrows from left to right, drawn
in dark #212121 with visible depth and a shadow beneath it. All four streams enter
its wide left face.

From its narrow right face, one single stream of cubes leaves toward the right
edge of the frame. In that stream the cubes are sorted: first all the red ones in
a tight group, then all the green, then all the blue, then all the grey. The
mixing on the left and the sorting on the right is the whole point.

Reading direction is left to right.

No text anywhere in the image. No class names, no numbers, no labels, no legend.
No logo, brand mark, model number, switch hardware, or product photograph. No
borders, frames, title bars, or caption text. No watermark, no signature.
```


---

# Group B

**Group B. Pages with no figure.** Eleven. The fifteen pages added in v6 carry no diagram at all. Nothing is broken, the pages simply have nothing to look at.

---

## Image 05 - Q against bandwidth

| Field | Value |
|---|---|
| Filename | `electronics-filter-q-against-bandwidth-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Filter_Q_Against_Bandwidth.png` |
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

## Image 06 - Three second-order filter alignments

| Field | Value |
|---|---|
| Filename | `electronics-filter-alignments-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Sharp_Knee_Rolloff_Curve_Trio.png` |
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

## Image 07 - Parametric EQ boost and cut

| Field | Value |
|---|---|
| Filename | `electronics-parametric-eq-boost-and-cut-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Parametric_EQ_Boost_and_Cut.png` |
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

## Image 08 - Constant Q against proportional Q

| Field | Value |
|---|---|
| Filename | `electronics-constant-q-against-proportional-q-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Constant_Q_Against_Proportional_Q.png` |
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

## Image 09 - Frequency scaling

| Field | Value |
|---|---|
| Filename | `electronics-frequency-scaling-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Frequency_Scaling.png` |
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

## Image 10 - A sound solder joint, macro

| Field | Value |
|---|---|
| Filename | `electronics-solder-joint-macro-01.jpg` |
| Format | **JPEG, quality 88, its own background** |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Solder_Joint_Macro.jpg` |
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

## Image 11 - Microphone system against in-ear system

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

## Image 12 - Antenna radiation patterns

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

## Image 13 - Multipath null and diversity spacing

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

## Image 14 - Third order intermodulation

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

## Image 15 - Port mirroring against a network tap

| Field | Value |
|---|---|
| Filename | `network-diagnostics-mirror-against-tap-01.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Diagnostics/Mirror_Against_Tap.png` |
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

# Group C

**Group C. Correct figures in the old style.** Thirty-six. Every one of these is accurate and readable today. This group exists only because 20.5a changed the house style, so it is the group to skip if you run out of patience.

---

## Image 16 - ac vs dc waveform

| Field | Value |
|---|---|
| Filename | `electronics-ac-vs-dc-waveform-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Straight_and_Wavy_Extruded_Ribbons.png` |
| Replaces | `electronics-ac-vs-dc-waveform-01.png` |
| Used on | Canvas page `Electronics: AC & DC Circuits` |
| Alt text | `A flat steady ribbon beside a rolling wave ribbon, both running left to right` |
| Caption | `Figure 1. DC on the left holds its level. AC on the right swings above and below it.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

The frame is split into a left half and a right half by a narrow vertical gap.

In the left half, a single ribbon runs left to right at a constant height above a
flat base plane, perfectly straight and level, in blue #0D47A1.

In the right half, a ribbon of the same width runs left to right but rises and
falls in two full smooth waves, crossing the base plane each time, in green
#1B5E20.

Both ribbons have real thickness, rounded edges and soft shadows on the plane
beneath them, so they read as solid objects rather than drawn lines. The base
plane is dark #212121.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 17 - bjt voltage divider bias

| Field | Value |
|---|---|
| Filename | `electronics-bjt-voltage-divider-bias-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Rendered_Resistors_and_Transistor_Disc.png` |
| Replaces | `electronics-bjt-voltage-divider-bias-01.png` |
| Used on | Canvas page `Electronics: Transistor Biasing` |
| Alt text | `A transistor circuit with two resistors setting the base voltage and one resistor in each of the other legs` |
| Caption | `Figure 1. Two resistors form the divider that sets the base. One sits in the collector leg and one in the emitter leg.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A single transistor circuit. Components sit slightly raised off the plane with
soft shadows beneath them.

A horizontal supply rail runs across the top of the frame. A ground symbol sits at
the bottom.

Two resistors are stacked vertically in a column on the left, one above the other,
connected end to end. The top of the upper one reaches the supply rail and the
bottom of the lower one reaches ground. The junction between the two connects
rightward to the base of a transistor drawn as a circle with three leads, in blue
#0D47A1.

A third resistor runs from the supply rail down to the transistor's collector. A
fourth runs from the transistor's emitter down to ground.

All wires, resistors and the ground symbol are dark #212121. The transistor is the
only blue object.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 18 - electrical safety current path

| Field | Value |
|---|---|
| Filename | `electronics-electrical-safety-current-path-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Grey_Mannequins_With_Glowing_Paths.png` |
| Replaces | `electronics-electrical-safety-current-path-01.png` |
| Used on | Canvas page `Electronics: Electrical Safety` |
| Alt text | `Two paths of current through a torso, one crossing the chest and one running down one side` |
| Caption | `Figure 1. The path on the left crosses the chest. The path on the right does not. That difference is the whole hazard.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A simplified human torso and arms, shown twice side by side, separated by a narrow
vertical gap. The torso is a smooth featureless grey #616161 form with real volume
and shading, like a shop mannequin, with no face, no hair, no clothing and no
detail of any kind.

In the left figure, a thick glowing tube in red #B71C1C enters at one hand, runs
up that arm, straight across the upper chest, and down the other arm to the other
hand. A small solid heart shape in deeper red sits in the chest directly on that
path.

In the right figure, a thick glowing tube in orange #993300 enters at one hand,
runs up that arm, down the same side of the torso and out at the foot on that same
side. The identical heart shape sits in the chest, clearly off to one side of the
path and untouched by it.

Both figures are lit the same way. The contrast between a path that meets the heart
and one that misses it is the only difference.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 19 - opamp summing amplifier

| Field | Value |
|---|---|
| Filename | `electronics-opamp-summing-amplifier-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Red_Node_Merging_Rendered_Resistor_Inputs.png` |
| Replaces | `electronics-opamp-summing-amplifier-01.png` |
| Used on | Canvas page `Electronics: The Summing Amplifier` |
| Alt text | `Three input resistors meeting at one op-amp summing node, with a single feedback resistor to the output` |
| Caption | `Figure 1. Three sources, one node, one output. The node in red is the virtual ground.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A single op-amp circuit. Components sit slightly raised off the plane with soft
shadows beneath them.

An amplifier drawn as a triangle pointing right, in blue #0D47A1, rendered as a
solid wedge with thickness. A minus sign on its upper input, a plus sign on its
lower input. The plus input connects down to a ground symbol.

Three horizontal wires enter from the left edge of the frame, stacked one above
another. Each passes through its own resistor. All three then converge on one
single junction immediately to the left of the minus input. That junction is a
prominent sphere in red #B71C1C, raised above the plane and clearly the focal
point of the picture.

A fourth resistor runs from that red junction up and over the top of the triangle
and down to the wire leaving the triangle's tip, which continues to the right edge
of the frame.

All wires, resistors and the ground symbol are dark #212121.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 20 - rms peak peak to peak

| Field | Value |
|---|---|
| Filename | `electronics-rms-peak-peak-to-peak-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Wave_Ribbon_With_Measurement_Arrows.png` |
| Replaces | `electronics-rms-peak-peak-to-peak-01.png` |
| Used on | Canvas page `Electronics: AC & DC Circuits` |
| Alt text | `A wave with three measurement markers: one to its crest, one lower, and one from crest to trough` |
| Caption | `Figure 1. Peak is crest to center, peak to peak is crest to trough, and RMS sits below peak at about seven tenths of it.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A smooth rolling wave ribbon runs left to right across the frame in green #1B5E20,
completing two full cycles above and below a flat horizontal centre plane in dark
#212121. The ribbon has real thickness, rounded edges and a soft shadow.

Three measurement markers stand beside it, each a solid three-dimensional arrow
with visible depth:

A short red #B71C1C vertical arrow runs from the centre plane up to the exact height
of the wave's crest.

A shorter orange #993300 vertical arrow, beside the red one, runs from the centre
plane up to roughly seven tenths of that height, clearly lower than the red arrow
and obviously not a full crest.

A tall blue #0D47A1 vertical double-headed arrow, set further to the right, runs
from the very bottom of a trough all the way up to the very top of a crest, so it
is visibly about twice the red arrow.

The three different lengths are the point and must be unmistakable.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 21 - semiconductor pn junction

| Field | Value |
|---|---|
| Filename | `electronics-semiconductor-pn-junction-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Rendered_Slab_With_Bubbles_and_Spheres.png` |
| Replaces | `electronics-semiconductor-pn-junction-01.png` |
| Used on | Canvas page `Electronics: Semiconductors, Transistors, and Op-amps` |
| Alt text | `Two joined slabs of material with a clear empty band where they meet` |
| Caption | `Figure 1. Two differently doped regions and the depletion region between them, which is empty of free carriers.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Two rectangular slabs of solid material sit end to end in the centre of the frame,
drawn in isometric with real thickness, shading on their sides and a shadow beneath
them.

The left slab is blue #0D47A1 and holds a scattering of small hollow spheres,
rendered as open bubbles with visible rims.

The right slab is green #1B5E20 and holds a scattering of small solid spheres,
rendered filled and glossy.

Between the two slabs sits a narrow vertical band of the same thickness and shape
as the slabs, but pale and completely empty, containing no spheres of either kind.
It reads as a gap in an otherwise continuous block.

The emptiness of the middle band against the busy regions either side is the
point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 22 - protocols aes50 point to point chain

| Field | Value |
|---|---|
| Filename | `audio-protocols-aes50-point-to-point-chain-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Audio_Protocols/Four_Blue_Cubes_Linked_in_Line.png` |
| Replaces | `audio-protocols-aes50-point-to-point-chain-01.png` |
| Used on | Canvas page `Networking: AES50` |
| Alt text | `Four devices joined one to the next in a single line, with no central box anywhere` |
| Caption | `Figure 1. AES50 runs device to device. There is no switch in the path.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Four identical rounded blocks sit in a single horizontal row across the frame,
evenly spaced, drawn in isometric with real depth and shadows, in blue #0D47A1.

Each block is joined to the next by a short thick tube in dark #212121, so the four
form one unbroken chain from left to right. The first block has nothing to its left
and the last has nothing to its right.

There is no fifth object of any kind. Nothing sits above, below or between the
chain. The absence of any central hub is the point of the picture.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 23 - protocols aes67 interoperability overlap

| Field | Value |
|---|---|
| Filename | `audio-protocols-aes67-interoperability-overlap-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Audio_Protocols/Overlapping_Translucent_Colored_Spheres.png` |
| Replaces | `audio-protocols-aes67-interoperability-overlap-01.png` |
| Used on | Canvas page `Networking: AES67` |
| Alt text | `Three translucent volumes overlapping, with a small solid core where all three meet` |
| Caption | `Figure 1. AES67 is the region all three protocols share, and it is smaller than any of them.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Three large translucent spheres sit in the centre of the frame, arranged so that
each overlaps the other two and all three share one small central region. They are
rendered with real volume, soft internal shading and highlights, like coloured glass
balls, casting a soft shadow on the plane beneath.

The first is blue #0D47A1, the second green #1B5E20, the third orange #993300.

Where all three intersect, a small solid opaque core glows brighter than the
surrounding glass, clearly denser and smaller than any one sphere.

The smallness of the shared core relative to the three spheres is the point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 24 - protocols avb milan reserved bandwidth

| Field | Value |
|---|---|
| Filename | `audio-protocols-avb-milan-reserved-bandwidth-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Audio_Protocols/Cutaway_Pipe_With_Green_Core.png` |
| Replaces | `audio-protocols-avb-milan-reserved-bandwidth-01.png` |
| Used on | Canvas page `Networking: AVB and Milan` |
| Alt text | `A pipe mostly filled by one reserved block with a smaller unreserved remainder` |
| Caption | `Figure 1. AVB sets aside a share of the link before any audio moves. What is left over takes its chances.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A single large horizontal pipe runs across the frame, drawn in three-quarter view
as a solid cylinder with real depth, thickness and a shadow, in dark #212121, open
at the near end so its interior is visible.

Inside the pipe, a solid green #1B5E20 block fills about three quarters of the
cross-section and runs the full length of the pipe. It is smooth and continuous.

The remaining quarter of the cross-section is filled with a loose scatter of small
grey #616161 cubes of varying spacing, clearly not packed and clearly a different
kind of thing from the smooth green block.

The contrast between the reserved smooth block and the loose leftover is the
point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 25 - protocols dante network topology

| Field | Value |
|---|---|
| Filename | `audio-protocols-dante-network-topology-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Audio_Protocols/Isometric_Hub_With_Glowing_Arcs.png` |
| Replaces | `audio-protocols-dante-network-topology-01.png` |
| Used on | Canvas page `Networking: Dante` |
| Alt text | `Several devices all connected to one central box, with routing shown as separate curved links between them` |
| Caption | `Figure 1. Every device connects once to the switch. The routing between them is made in software, not with patch cables.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

One large flat slab sits in the centre of the frame, drawn in isometric with real
thickness and a shadow, in dark #212121.

Five rounded blocks in blue #0D47A1 are arranged in a ring around it, evenly spaced,
each joined to the central slab by one straight thick tube in grey #616161. Every
device has exactly one such tube and they are all the same.

Separately, three curved glowing arcs in green #1B5E20 arc through the air from one
blue block to another, passing over the top of the central slab without touching
it. These are clearly a different kind of connection from the grey tubes: they float,
they are coloured differently, and they do not follow the cabling.

The difference between the physical star of grey tubes and the free routing of the
green arcs is the point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 26 - protocols ndi bandwidth tiers

| Field | Value |
|---|---|
| Filename | `audio-protocols-ndi-bandwidth-tiers-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Audio_Protocols/Three_Pipes_of_Decreasing_Diameter.png` |
| Replaces | `audio-protocols-ndi-bandwidth-tiers-01.png` |
| Used on | Canvas page `Networking: NDI` |
| Alt text | `Three pipes of decreasing diameter carrying the same flow` |
| Caption | `Figure 1. The three NDI tiers, widest bandwidth at the top down to the most compressed at the bottom.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Three horizontal pipes are stacked vertically in the frame, drawn in three-quarter
view as solid cylinders with real depth and shadows, each open at the near end so the
bore is visible.

The top pipe is the widest by a clear margin, in red #B71C1C. The middle pipe is
noticeably narrower, in orange #993300. The bottom pipe is narrower again, in green
#1B5E20, and is obviously the smallest of the three.

All three are the same length and are aligned at their left ends. The stepping down
in diameter from top to bottom is the only thing that differs and must be
unmistakable.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 27 - protocols protocol comparison matrix

| Field | Value |
|---|---|
| Filename | `audio-protocols-protocol-comparison-matrix-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Audio_Protocols/Colored_Spheres_on_Grid_Plane.png` |
| Replaces | `audio-protocols-protocol-comparison-matrix-01.png` |
| Used on | Canvas page `Networking: Protocol Comparison` |
| Alt text | `Markers scattered across a floor, spread between two directions of increase` |
| Caption | `Figure 1. Latency increases to the right, channel count increases toward the back. Each marker is one protocol.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A flat square floor plane in pale grey is seen in three-quarter view, receding into
the frame, with a subtle grid ruled on it.

Eight small spheres sit on that floor at different positions, each raised slightly
and casting its own shadow. They are spread out so no two sit at the same spot, and
they occupy the whole plane rather than clustering.

Three of the spheres are green #1B5E20, three are blue #0D47A1, one is orange
#993300, one is red #B71C1C.

At the near right edge of the floor, a solid arrow in dark #212121 lies flat on the
plane pointing right. At the near left edge, another solid arrow lies flat pointing
away from the viewer into the depth of the scene.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 28 - protocols protocol osi layer map

| Field | Value |
|---|---|
| Filename | `audio-protocols-protocol-osi-layer-map-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Audio_Protocols/Exploded_Slabs_With_White_Markers.png` |
| Replaces | `audio-protocols-protocol-osi-layer-map-01.png` |
| Used on | Canvas page `Networking: Protocol Comparison` |
| Alt text | `Four stacked slabs with small tiles resting on two of them` |
| Caption | `Figure 1. Six protocols sit on the network layer and two sit on the data link layer beneath it.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Four broad flat slabs are stacked one on top of another like the floors of a
building, drawn in isometric with real thickness, shading on their edges and shadows
between them.

From the bottom up they are brown #5D4037, red #B71C1C, orange #993300 and green
#1B5E20. Each is the same size and they are aligned squarely.

Resting on the top surface of the orange slab, six small identical tiles in pale
grey stand upright in a row.

Resting on the top surface of the red slab below it, two of the same tiles stand
upright.

The other two slabs carry nothing. The count, six on one floor and two on the floor
below, is the point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 29 - protocols smpte 2110 essence separation

| Field | Value |
|---|---|
| Filename | `audio-protocols-smpte-2110-essence-separation-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Audio_Protocols/Black_Block_With_Three_Segmented_Cables.png` |
| Replaces | `audio-protocols-smpte-2110-essence-separation-01.png` |
| Used on | Canvas page `Networking: SMPTE ST 2110` |
| Alt text | `One source splitting into three separate streams that travel alongside each other` |
| Caption | `Figure 1. ST 2110 carries video, audio and data as three separate streams sharing one clock.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

One solid cube in dark #212121 sits at the left of the frame, drawn in isometric with
real depth and a shadow.

Three thick tubes leave its right face and run to the right edge of the frame, stacked
one above another, parallel and never touching. The top tube is blue #0D47A1, the
middle green #1B5E20, the bottom orange #993300.

Each tube carries a line of small cubes of its own colour flowing along it, and the
cubes in all three tubes are aligned with each other across the three streams, so the
three flows are visibly in step.

Reading direction is left to right.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 30 - addressing cidr block sizes

| Field | Value |
|---|---|
| Filename | `ip-addressing-cidr-block-sizes-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/IP_Addressing/Row_of_Shrinking_Blue_Cubes.png` |
| Replaces | `ip-addressing-cidr-block-sizes-01.png` |
| Used on | Canvas page `Networking: Subnet Masks and CIDR` |
| Alt text | `A row of blocks each half the size of the one before it` |
| Caption | `Figure 1. Each step up in prefix length halves the block. Left is a /24 and the halving runs to the right.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Seven solid cubes stand in a row across the frame on a flat plane, drawn in isometric
with real depth, shading and shadows, in blue #0D47A1.

The leftmost cube is the largest. Each cube to its right is exactly half the volume of
the one to its left, so the row shrinks steeply and the rightmost is very small beside
the first.

All seven sit on the same baseline and are evenly spaced. The halving is the only
thing the picture shows.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 31 - addressing ipv4 address anatomy

| Field | Value |
|---|---|
| Filename | `ip-addressing-ipv4-address-anatomy-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/IP_Addressing/Three_Blue_Blocks_and_One_Green.png` |
| Replaces | `ip-addressing-ipv4-address-anatomy-01.png` |
| Used on | Canvas page `Networking: IP Addressing Fundamentals` |
| Alt text | `A bar of four segments, the first three one color and the last another` |
| Caption | `Figure 1. With a /24 mask the first three groups name the network and the last names the host.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A single long rectangular bar runs horizontally across the centre of the frame, drawn
in isometric with real thickness, shading on its sides and a shadow beneath it.

The bar is divided into four equal segments by narrow grooves cut across it.

The first three segments from the left are blue #0D47A1. The fourth and last segment
is green #1B5E20 and stands slightly proud of the others, raised a little higher so it
reads as separate.

Reading direction is left to right.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 32 - addressing ipv6 address anatomy

| Field | Value |
|---|---|
| Filename | `ip-addressing-ipv6-address-anatomy-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/IP_Addressing/Three_Segment_Extruded_Bar.png` |
| Replaces | `ip-addressing-ipv6-address-anatomy-01.png` |
| Used on | Canvas page `Networking: IPv6 Basics Overview` |
| Alt text | `A bar of three unequal segments, the last one half the whole length` |
| Caption | `Figure 1. Routing prefix, subnet, and interface identifier. The interface identifier is half the address.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A single long rectangular bar runs horizontally across the centre of the frame, drawn
in isometric with real thickness, shading on its sides and a shadow beneath it.

The bar is divided into three unequal segments by narrow grooves. The first segment
takes a little over a third of the length, in blue #0D47A1. The second is short,
taking about an eighth, in orange #993300. The third takes exactly half the whole bar,
in green #1B5E20.

The third segment being as long as the other two together is the point.

Reading direction is left to right.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 33 - addressing private address ranges

| Field | Value |
|---|---|
| Filename | `ip-addressing-private-address-ranges-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/IP_Addressing/Three_Extruded_Bars_Increasing_in_Length.png` |
| Replaces | `ip-addressing-private-address-ranges-01.png` |
| Used on | Canvas page `Networking: IP Address Ranges to Memorize` |
| Alt text | `Three blocks of very different sizes stacked one above another` |
| Caption | `Figure 1. The three private ranges, smallest at the top. The bottom one holds far more addresses than the other two together.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Three solid rectangular blocks are stacked vertically in the frame, all aligned at
their left ends, drawn in isometric with real thickness, shading and shadows.

The top block is the shortest, in green #1B5E20. The middle block is clearly longer,
in blue #0D47A1. The bottom block is far longer than either, running nearly the full
width of the frame, in deep purple.

The difference in scale between the three is extreme and is the whole point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 34 - addressing subnet mask bit boundary

| Field | Value |
|---|---|
| Filename | `ip-addressing-subnet-mask-bit-boundary-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/IP_Addressing/Rendered_Bars_Divided_into_Equal_Pieces.png` |
| Replaces | `ip-addressing-subnet-mask-bit-boundary-01.png` |
| Used on | Canvas page `Networking: Subnet Masks and CIDR` |
| Alt text | `One long block, then the same length split in two, then split in four` |
| Caption | `Figure 1. The same address space divided three ways. Each row splits every block of the row above it in half.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Three horizontal rows sit one above another in the frame, all exactly the same total
length and aligned at their left and right ends, drawn in isometric with real thickness
and shadows.

The top row is one single unbroken block in blue #0D47A1.

The middle row is the same length but cut into two equal blocks with a narrow gap
between them, the left one blue #0D47A1 and the right one green #1B5E20.

The bottom row is the same length again but cut into four equal blocks with narrow
gaps, alternating blue and green from left to right.

The rows being identical in total length while differing in how many pieces they hold
is the point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 35 - architecture igmp snooping effect

| Field | Value |
|---|---|
| Filename | `network-architecture-igmp-snooping-effect-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Architecture/Red_and_Green_Columns_Under_Bars.png` |
| Replaces | `network-architecture-igmp-snooping-effect-01.png` |
| Used on | Canvas page `Networking: Multicast and IGMP` |
| Alt text | `The same device sending to every outlet above, and to only two outlets below` |
| Caption | `Figure 1. Without snooping the switch feeds every port. With snooping it feeds only the ports that asked.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

The frame is divided into an upper half and a lower half by a narrow horizontal gap.

In the upper half, a wide flat slab in dark #212121 sits across the top, drawn in
isometric. Six thick tubes in red #B71C1C drop from its underside to six identical
small blocks in a row beneath it. Every one of the six blocks has a tube.

In the lower half, an identical slab sits across the top with six identical blocks
beneath it in the same positions. Only two thick tubes in green #1B5E20 drop from the
slab, to the first and second blocks. The other four blocks have nothing reaching them
at all.

The count, six against two, is the point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 36 - architecture multicast vs unicast flow

| Field | Value |
|---|---|
| Filename | `network-architecture-multicast-vs-unicast-flow-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Architecture/Tube_Bundle_Beside_Branching_Stem.png` |
| Replaces | `network-architecture-multicast-vs-unicast-flow-01.png` |
| Used on | Canvas page `Networking: Multicast and IGMP` |
| Alt text | `Four separate streams from one source on the left, one shared stream that splits late on the right` |
| Caption | `Figure 1. Unicast sends a copy per listener. Multicast sends one copy that splits as late as possible.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

The frame is divided into a left half and a right half by a narrow vertical gap.

In the left half, one cube in dark #212121 sits at the top. Four separate thick tubes
in red #B71C1C leave it, each running the whole distance down to one of four small
blocks arranged in a row at the bottom. The four tubes run side by side the entire way
and never merge.

In the right half, an identical cube sits at the top. One single thick tube in green
#1B5E20 leaves it and runs most of the way down before reaching a junction sphere, from
which four short branches fan out to four small blocks in a row at the bottom.

The four full-length tubes on the left against the one long tube on the right is the
point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 37 - architecture ptp clock hierarchy

| Field | Value |
|---|---|
| Filename | `network-architecture-ptp-clock-hierarchy-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Architecture/Red_Cube_Above_Orange_and_Grey.png` |
| Replaces | `network-architecture-ptp-clock-hierarchy-01.png` |
| Used on | Canvas page `Networking: Clocking and PTP` |
| Alt text | `One block at the top feeding two in the middle, each feeding three at the bottom` |
| Caption | `Figure 1. One leader clock at the top. Everything below it follows, directly or through an intermediate device.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A three-tier arrangement drawn in isometric with real depth and shadows.

At the top of the frame, one large cube in red #B71C1C, raised highest and clearly the
largest object in the picture.

Below it, two medium cubes in orange #993300, each joined to the top cube by a thick
tube in dark #212121.

Below those, six small cubes in grey #616161 in a row, three joined to each orange
cube by thinner tubes.

The size and height of the three tiers steps down clearly from top to bottom, so the
hierarchy reads at a glance.

Reading direction is top to bottom.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 38 - architecture trunk port tagging

| Field | Value |
|---|---|
| Filename | `network-architecture-trunk-port-tagging-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Architecture/Cube_Chain_With_Yellow_Tags.png` |
| Replaces | `network-architecture-trunk-port-tagging-01.png` |
| Used on | Canvas page `Networking: VLANs, Trunk Ports, and Audio over IP` |
| Alt text | `Cubes travelling between two boxes carrying a colored tab that is present only between them` |
| Caption | `Figure 1. The tag is added when traffic enters the link between switches and removed when it leaves.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Two large flat slabs in dark #212121 sit at the left and right of the frame, drawn in
isometric with real thickness and shadows. One thick tube joins them across the middle.

Below the left slab, two small blocks hang, one green #1B5E20 and one blue #0D47A1, each
joined to the slab by a short tube. The same pair hangs below the right slab.

Travelling along the tube between the two slabs are several small cubes, alternating
green and blue. Each cube on that middle tube carries a small bright yellow tab stuck to
its top face.

Cubes on the short tubes below either slab are the same green and blue but carry no tab
at all.

The tab existing only on the middle run is the point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 39 - architecture vlan segmentation

| Field | Value |
|---|---|
| Filename | `network-architecture-vlan-segmentation-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Architecture/Red_Wall_Separating_Green_and_Blue.png` |
| Replaces | `network-architecture-vlan-segmentation-01.png` |
| Used on | Canvas page `Networking: VLANs, Trunk Ports, and Audio over IP` |
| Alt text | `One box with two separate groups hanging from it, divided by a solid wall` |
| Caption | `Figure 1. One switch, two networks. Nothing crosses the wall without a router.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

One wide flat slab in dark #212121 runs across the upper part of the frame, drawn in
isometric with real thickness and a shadow.

Three small blocks in green #1B5E20 hang below its left portion, each joined to it by a
short tube. Three small blocks in blue #0D47A1 hang below its right portion in the same
way.

A solid opaque wall in red #B71C1C rises vertically through the middle of the scene,
passing through the slab and continuing well below it, completely separating the green
group from the blue group. The wall is thick and clearly impassable, not a dashed line.

Reading direction is left to right.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 40 - configuration dhcp four step handshake

| Field | Value |
|---|---|
| Filename | `network-configuration-dhcp-four-step-handshake-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-configuration/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Configuration/Alternating_Arrows_Between_Two_Posts.png` |
| Replaces | `network-configuration-dhcp-four-step-handshake-01.png` |
| Used on | Canvas page `Networking: DHCP` |
| Alt text | `Four arrows alternating direction between two upright posts` |
| Caption | `Figure 1. Four messages, alternating direction. Discover and Request go out, Offer and Acknowledge come back.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Two tall upright posts stand at the left and right of the frame on a flat plane, drawn
in isometric with real thickness and shadows, in dark #212121.

Four thick arrows run horizontally between them, stacked one above another from top to
bottom, each a solid three-dimensional form with depth.

The first and third arrows from the top point left to right and are green #1B5E20. The
second and fourth point right to left and are blue #0D47A1.

The strict alternation of direction down the stack is the point.

Reading direction is top to bottom.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 41 - configuration dns resolution chain

| Field | Value |
|---|---|
| Filename | `network-configuration-dns-resolution-chain-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-configuration/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Configuration/Rounded_Cubes_and_Orange_Arrows.png` |
| Replaces | `network-configuration-dns-resolution-chain-01.png` |
| Used on | Canvas page `Networking: DNS` |
| Alt text | `A question passing along a row of four stops and the answer returning directly` |
| Caption | `Figure 1. The question walks the chain one stop at a time. The answer comes straight back.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Five rounded blocks stand in a row across the frame on a flat plane, evenly spaced,
drawn in isometric with real depth and shadows. The leftmost is dark #212121, the second
blue #0D47A1, and the remaining three green #1B5E20.

Short thick arrows in orange #993300 run between each adjacent pair, left to right, so
the question steps along the row one block at a time.

One long curved arrow in orange sweeps out from the rightmost block, arcs below the row
clear of every block, and returns all the way to the leftmost block in a single
unbroken move.

The contrast between the stepwise outward path and the single sweeping return is the
point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 42 - configuration static vs dhcp assignment

| Field | Value |
|---|---|
| Filename | `network-configuration-static-vs-dhcp-assignment-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-configuration/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Configuration/Separate_Knobs_Versus_Shared_Manifold.png` |
| Replaces | `network-configuration-static-vs-dhcp-assignment-01.png` |
| Used on | Canvas page `Networking: Address Configuration and Interface Priority` |
| Alt text | `Four devices each set individually on the left, four fed from one source on the right` |
| Caption | `Figure 1. Static sets every device by hand. DHCP sets them from one place.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

The frame is divided into a left half and a right half by a narrow vertical gap.

In the left half, four identical small blocks stand in a row on a flat plane. Above each
one, separately, floats its own small dial or knob object, one per block, four in total.
Nothing joins the four blocks to each other.

In the right half, four identical small blocks stand in the same arrangement. Above them
sits one single larger slab in blue #0D47A1, and four thick tubes drop from it, one to
each block.

Four separate controls against one shared source is the point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 43 - diagnostics capture point placement

| Field | Value |
|---|---|
| Filename | `network-diagnostics-capture-point-placement-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Diagnostics/Block_Clusters_With_Tube_Junctions.png` |
| Replaces | `network-diagnostics-capture-point-placement-01.png` |
| Used on | Canvas page `Networking: Wireshark Setup and Capture Basics` |
| Alt text | `A third device fed from a box on the left and from a unit inserted in the line on the right` |
| Caption | `Figure 1. A copy taken from the switch on the left, a device inserted in the link on the right.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

The frame is divided into a left half and a right half by a narrow vertical gap.

In the left half, two rounded blocks sit at the top joined down into one wide flat slab in
dark #212121 by thick blue #0D47A1 tubes. A thinner grey #616161 tube leaves one end of
the slab and runs down to a third block at the bottom.

In the right half, two rounded blocks sit left and right joined directly by one horizontal
blue tube. A small grey cube is inserted inline into the middle of that tube. A thinner
grey tube drops from the underside of that cube to a third block at the bottom.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 44 - diagnostics diagnostic ladder

| Field | Value |
|---|---|
| Filename | `network-diagnostics-diagnostic-ladder-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Diagnostics/Staircase_of_Six_Colored_Slabs.png` |
| Replaces | `network-diagnostics-diagnostic-ladder-01.png` |
| Used on | Canvas page `Networking: Diagnostic Ladder` |
| Alt text | `Six rungs climbing upward, each a different color` |
| Caption | `Figure 1. Six rungs, bottom to top. Start at the bottom every time.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Six broad flat slabs are stacked one above another like steps rising from the bottom
left toward the top right, drawn in isometric with real thickness, shading on their edges
and shadows between them. Each step is set back slightly from the one below so the stack
climbs.

From the bottom up they are brown #5D4037, red #B71C1C, orange #993300, yellow, green
#1B5E20 and blue #0D47A1.

Reading direction is bottom to top.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 45 - diagnostics ping round trip

| Field | Value |
|---|---|
| Filename | `network-diagnostics-ping-round-trip-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Diagnostics/Opposing_Arrows_and_Vertical_Measure.png` |
| Replaces | `network-diagnostics-ping-round-trip-01.png` |
| Used on | Canvas page `Networking: Ping` |
| Alt text | `One arrow out and one arrow back between two posts, with a marker measuring the pair` |
| Caption | `Figure 1. One packet out, one packet back. The round trip time measures both legs together.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Two tall upright posts stand at the left and right of the frame on a flat plane, drawn
in isometric with real thickness and shadows, in dark #212121.

One thick arrow runs from the left post to the right post, pointing right, in green
#1B5E20. Below it, a second thick arrow runs from the right post back to the left post,
pointing left, in blue #0D47A1. Both are solid three-dimensional forms with depth.

Beside the left post, a vertical double-headed arrow in red #B71C1C spans the full
height from the upper arrow down to the lower one, measuring the pair together.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 46 - diagnostics traceroute hop discovery

| Field | Value |
|---|---|
| Filename | `network-diagnostics-traceroute-hop-discovery-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Diagnostics/Green_Arrows_Bursting_Against_Posts.png` |
| Replaces | `network-diagnostics-traceroute-hop-discovery-01.png` |
| Used on | Canvas page `Networking: Traceroute` |
| Alt text | `Three probes of increasing length along a row of posts, each stopping one post further on` |
| Caption | `Figure 1. Each probe reaches one hop further than the last, and each one reports back.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A row of five upright posts stands across the frame on a flat plane, evenly spaced, in
dark #212121, drawn in isometric with shadows.

Three thick arrows in green #1B5E20 leave the leftmost post, stacked one above another. The
lowest and shortest stops at the second post. The middle one stops at the third post. The
top and longest stops at the fourth post. Each ends in a small red #B71C1C burst marker at
the post where it stops.

From each of those three burst markers, a thin dashed blue #0D47A1 line curves back to the
leftmost post.

The stepping of the three lengths is the point.

Reading direction is left to right.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 47 - diagnostics troubleshooting decision tree

| Field | Value |
|---|---|
| Filename | `network-diagnostics-troubleshooting-decision-tree-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Diagnostics/Blue_Diamonds_Branching_to_Grey_Blocks.png` |
| Replaces | `network-diagnostics-troubleshooting-decision-tree-01.png` |
| Used on | Canvas page `Networking: Troubleshooting Decision Tree` |
| Alt text | `Four decision points in a column, each with a branch leading off to one side` |
| Caption | `Figure 1. Four questions in order. A no at any point sends you off the main path.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

A vertical column of four diamond-shaped solids runs down the centre of the frame, evenly
spaced, drawn in isometric with real thickness, shading and shadows, in blue #0D47A1.

Each diamond is joined to the one below it by a short thick vertical tube in green #1B5E20.

From the right-hand point of each diamond, a thick horizontal arrow in red #B71C1C runs out
to its own small flat slab in grey #616161, four slabs in total, stacked down the right side
of the frame.

Above the topmost diamond sits one solid cube in red #B71C1C.

Reading direction is top to bottom.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 48 - foundations layer2 switch frame forwarding

| Field | Value |
|---|---|
| Filename | `network-foundations-layer2-switch-frame-forwarding-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-foundations/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Foundations/Green_Pipe_Arching_Between_Cubes.png` |
| Replaces | `network-foundations-layer2-switch-frame-forwarding-01.png` |
| Used on | Canvas page `Networking: Layer 2 Switched Protocols` |
| Alt text | `One box feeding a single outlet out of four, the other three untouched` |
| Caption | `Figure 1. A switch sends the frame to the one port that owns the address, not to all of them.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

One wide flat slab in dark #212121 runs across the upper part of the frame, drawn in
isometric with real thickness and a shadow.

Four identical small blocks stand in a row beneath it, evenly spaced.

One thick green #1B5E20 tube rises from the first block, enters the slab, and a second
thick green tube leaves the slab and drops to the third block. The path from first to third
is continuous and obvious.

The second and fourth blocks have nothing reaching them at all. No tube, no arrow, nothing.

The single path against the three untouched blocks is the point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 49 - foundations layer3 router between subnets

| Field | Value |
|---|---|
| Filename | `network-foundations-layer3-router-between-subnets-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-foundations/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Foundations/Orange_Sphere_Bridging_Two_Plates.png` |
| Replaces | `network-foundations-layer3-router-between-subnets-01.png` |
| Used on | Canvas page `Networking: Layer 3 Routable IP Protocols` |
| Alt text | `Two separate groups of devices joined only through one object between them` |
| Caption | `Figure 1. Two networks that can only reach each other through the router in the middle.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Two groups sit at the left and right of the frame. Each group is three small blocks
standing on a raised platform, drawn in isometric with real thickness and shadows. The left
platform and its blocks are blue #0D47A1, the right platform and its blocks green #1B5E20.

Between the two platforms, in the centre of the frame and raised higher than either, sits a
single solid sphere in orange #993300, clearly the largest and most prominent object in the
picture.

One thick tube runs from the left platform to the sphere, and one from the sphere to the
right platform. There is no other connection of any kind between the two sides.

Reading direction is left to right.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 50 - foundations osi seven layer stack

| Field | Value |
|---|---|
| Filename | `network-foundations-osi-seven-layer-stack-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-foundations/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Foundations/Exploded_Stack_of_Seven_Slabs.png` |
| Replaces | `network-foundations-osi-seven-layer-stack-01.png` |
| Used on | Canvas page `Networking: Introduction to Audio Networking` |
| Alt text | `Seven stacked slabs with a bracket marking the lowest four` |
| Caption | `Figure 1. Seven layers. Audio networking lives in the bottom four.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

Seven broad flat slabs are stacked squarely one on top of another like the floors of a
building, drawn in isometric with real thickness, shading on their edges and shadows between
them. All seven are the same size and aligned.

From the bottom up they are brown #5D4037, red #B71C1C, orange #993300, yellow, green
#1B5E20, blue #0D47A1 and deep purple.

A solid three-dimensional bracket in dark #212121 stands alongside the stack on the right,
spanning only the lowest four slabs and clearly not reaching the upper three.

Reading direction is bottom to top.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 51 - foundations tcp vs udp comparison

| Field | Value |
|---|---|
| Filename | `network-foundations-tcp-vs-udp-comparison-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-foundations/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Foundations/Cube_Tray_With_Missing_Piece.png` |
| Replaces | `network-foundations-tcp-vs-udp-comparison-01.png` |
| Used on | Canvas page `Networking: Layer 4 Transport Protocols` |
| Alt text | `A stream that pauses to resend a lost item on the left, and one that carries on without it on the right` |
| Caption | `Figure 1. TCP notices the gap and fills it. UDP carries on and leaves the gap.` |

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric or three-quarter view, with real
depth, shading and solid color fills. Objects sit on or above a plane and cast soft
shadows. Not flat line art.

The frame is divided into a left half and a right half by a narrow vertical gap. Each half
shows a flat plane with a stream of small cubes travelling left to right along it.

In the left half, the stream of blue #0D47A1 cubes is evenly spaced except at one point where
a cube is missing. Directly above that gap, a single cube is shown arcing back from further
along the stream to drop into it, so the gap is being filled. By the right edge the row is
complete and unbroken.

In the right half, the stream of green #1B5E20 cubes has the same gap at the same point, and
nothing is above it. The gap simply continues to the right edge of the frame, and the row
arrives incomplete.

The gap being filled on one side and left open on the other is the point.

No text anywhere in the image. No labels, no numbers, no legend, no titles. No logo,
brand mark, model number, product photograph, or front-panel detail. No borders,
frames, title bars, or caption text. No hands, no people, no watermark, no signature.
```

---

## Where every file goes

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/wireless
```

**This folder does not exist. Create it before saving anything from group B.**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/audio-protocols
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-configuration
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-foundations
```

A `-02` file never replaces its `-01`. Standards 20.4: a conforming filename is
permanent and is never overwritten. The old file stays on disk and the page's
`src` moves to the new one.

## After the files land

Tell me which groups you finished. I will move every page's `src` to the new
filenames, put the NAT and QoS figures back onto the two pages they were pulled
from in v5, and reship the cartridge. Nothing points at any of these filenames
yet, so nothing is showing a broken box while you work.

## Still needing a camera, not ChatGPT

Separate from this file, eight shots need photographing or sourcing rather than
generating. They are on the capture sheet, which has live preview slots that fill
in as each file lands:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/_briefs/2026-09-20-dapr-3255-capture-sheet-v6-pages.html
```
