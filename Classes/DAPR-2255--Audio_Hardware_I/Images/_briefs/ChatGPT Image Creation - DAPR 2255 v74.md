# DAPR 2255 Image Brief - the flat diagrams, rebuilt

Generated 2026-09-21, against the 2026-09-21 Standards. Run each prompt separately in ChatGPT.
Save each result with the exact filename shown, into the exact folder shown. Do not rename.

**Disregard every earlier DAPR 2255 image brief.** The v69, v71 and v72 briefs are superseded.
Work only from this file. If a prompt here contradicts something you were told before, this file wins.

## Why these eight and not the other twenty-three

I pulled all 110 diagrams the course references, measured them, and looked at them. They fall into
three groups, and only one of the three belongs to you.

| Group | Count | Who does it |
|---|---|---|
| Concept illustrations still rendered as thin flat line art | 8 | **This brief. ChatGPT.** |
| Diagrams whose content is really a set of labels | 7 | Claude, rebuilt as HTML on the page |
| Real hardware | 16 | Adam, with a camera. Standards 20.1 rule 3 |
| Engineering notation, correct as it is | rest | Nobody. Leave them alone |

**That last row matters.** A transistor symbol, a fuse symbol, a wire junction, a circuit
schematic and a waveform plot are *supposed* to be clean line art. That is what the notation is.
Rendering an NPN symbol in glossy isometric would be wrong, not better. The flat-vector rule was
removed because flat line art was being used for things it had no business illustrating, not
because line art is banned everywhere.

## The eight

| # | File | Page | Why it is being redone |
|---|---|---|---|
| 01 | `voltage-current-reservoir-analogy-02.png` | Voltage & Current: Read About Basic Current and Voltage and Resistance | Flat line art. |
| 02 | `power-heatsink-why-fins-work-02.png` | Power: Power, Heat, & Component Ratings | Flat line art. |
| 03 | `power-doubling-is-3db-02.png` | Power: Power in Decibels - dBW & dBm | The delivered version is close but not right. |
| 04 | `midi-gm-channel-10-02.png` | MIDI: Timeline General MIDI and MMC | Flat line art, sixteen outlined squares. |
| 05 | `midi-same-file-two-synths-02.png` | MIDI: What MIDI Is Not and Common Misunderstandings | Flat line art with three text labels doing all the work. |
| 06 | `midi-clock-vs-mtc-02.png` | MIDI: Timing Clocking and Synchronization | Flat line art, two tick marks on two lines. |
| 07 | `midi-what-midi-carries-02.png` | MIDI: What MIDI Is and Why It Exists | Flat line art with four tiny outlined glyphs and a struck-through circle. |
| 08 | `midi-jitter-buffer-tradeoff-02.png` | MIDI: Synchronization Over IP | Flat line art, two hairline strokes and four labels, two of which sit on top of the lines. |

Every one of these keeps its `-01` file exactly where it is until the `-02` is saved. The page
moves to the new name in the next cartridge and the old file dies then, not before.

---

## Image 01 - voltage current reservoir analogy

> **Replaces `voltage-current-reservoir-analogy-01.png`.** Flat line art. A tank, a pipe and a constriction are physical things and this is the one figure on the page a student is meant to picture, so it is the figure that gains most from real depth.

| Field | Value |
|---|---|
| Filename | `voltage-current-reservoir-analogy-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-reservoir-analogy-02.png` |
| Used on | Canvas page `Voltage & Current: Read About Basic Current and Voltage and Resistance` |
| Alt text | `A raised water tank feeding a pipe that narrows partway along before opening out again` |
| Caption | `Figure 1. Height pushes, flow rate is current, and the narrow section is resistance.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Render it as a richly rendered dimensional diagram, not a flat drawing and not a line
drawing. Three-quarter isometric perspective with real depth. Solid saturated colour fills,
soft ambient shading across every surface, a gentle contact shadow under every object where it
meets the ground plane, smooth rounded edges, a subtle glossy highlight on upward-facing
surfaces. Objects should look like solid physical things you could pick up, sitting on an
invisible floor.

A tall open-topped rectangular water tank stands raised on the LEFT, drawn as a solid
three-dimensional box with visible thickness in its walls, filled about three quarters full with
translucent blue-tinted water that has a flat, slightly reflective surface.

From the BOTTOM of the tank a solid cylindrical pipe runs to the RIGHT along the ground plane. The
pipe is a real tube with visible wall thickness and a rounded, shaded body. Partway along its run
the pipe narrows sharply into a much thinner section for a short distance, then opens back out to
full bore and continues to the right edge, where it ends in an open mouth with water spilling from
it in a short arc.

The narrow section is the most important feature in the picture and must be unmistakable: cut the
diameter to roughly one third and make the shoulders where it steps down and back up clearly
visible and clearly shaded.

Inside the pipe, a few smooth solid orange #993300 arrows lie along the axis pointing right,
bunched close together inside the narrow section and spread further apart in the wide sections.

A tall vertical double-headed green #1b5e20 arrow stands against the outside of the tank wall,
running from the water surface down to the pipe, showing the height of the column.

Nothing else in the frame. Generous empty background all around.

Colours, and only these: deep green #1b5e20, warm orange #993300, deep blue #0d47a1,
near-black #212121, mid grey #616161, light grey #e0e0e0, white #ffffff.

NO TEXT ANYWHERE IN THIS IMAGE. Not a title, not a label, not a caption, not an axis name,
not a unit, not a legend, not a watermark, not a single stray letter or digit. Every one of the
twelve defects in an earlier batch was a text defect: a label clipped by the frame, two labels
printed over each other, a label silently dropped. None of them were drawing problems. The
Canvas page already carries the heading, the caption, the table and the prose, so every name in
this picture is supplied by the page. If you think a label is needed, leave it out and make the
shape clearer instead.

Do not draw any real hardware and do not invent one. No connector faces with pins, no
front or rear panels, no jacks, no sockets, no knobs, no product shapes, no brand marks, no
software windows. This is an abstract diagram of an idea. A convincing render of a wrong
connector is worse than no picture at all.
```

---

## Image 02 - power heatsink why fins work

> **Replaces `power-heatsink-why-fins-work-01.png`.** Flat line art. The whole point is surface area, which is a three-dimensional property and cannot be shown honestly in a flat side-on drawing.

| Field | Value |
|---|---|
| Filename | `power-heatsink-why-fins-work-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/power/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/power/power-heatsink-why-fins-work-02.png` |
| Used on | Canvas page `Power: Power, Heat, & Component Ratings` |
| Alt text | `A bare block with three heat arrows beside an identical block under a finned sink with many arrows` |
| Caption | `Figure 1. Fins do not move heat faster. They give it more places to leave.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Render it as a richly rendered dimensional diagram, not a flat drawing and not a line
drawing. Three-quarter isometric perspective with real depth. Solid saturated colour fills,
soft ambient shading across every surface, a gentle contact shadow under every object where it
meets the ground plane, smooth rounded edges, a subtle glossy highlight on upward-facing
surfaces. Objects should look like solid physical things you could pick up, sitting on an
invisible floor.

Two objects stand side by side on a shared invisible ground plane, well separated, with a clear
gap of empty background between them so they read as a comparison.

On the LEFT, a small solid rectangular block in near-black #212121, plain on every face, with a
gentle contact shadow beneath it. Three smooth solid orange #993300 arrows rise from its flat top
face, evenly spaced, pointing up and slightly outward.

On the RIGHT, an identical near-black block of exactly the same size, but with a dense stack of
thin parallel light grey #e0e0e0 fins rising from its top face. The fins are solid plates with real
thickness, evenly spaced, running front to back, at least twelve of them, each one shaded so the
gaps between them read as depth rather than as stripes. A smooth solid orange arrow rises from the
top edge of every single fin.

Both blocks are the same size and sit at the same height. The difference in the number of arrows is
the entire content of the picture, so make the right side visibly crowded with them.

Nothing else in the frame.

Colours, and only these: deep green #1b5e20, warm orange #993300, deep blue #0d47a1,
near-black #212121, mid grey #616161, light grey #e0e0e0, white #ffffff.

NO TEXT ANYWHERE IN THIS IMAGE. Not a title, not a label, not a caption, not an axis name,
not a unit, not a legend, not a watermark, not a single stray letter or digit. Every one of the
twelve defects in an earlier batch was a text defect: a label clipped by the frame, two labels
printed over each other, a label silently dropped. None of them were drawing problems. The
Canvas page already carries the heading, the caption, the table and the prose, so every name in
this picture is supplied by the page. If you think a label is needed, leave it out and make the
shape clearer instead.

Do not draw any real hardware and do not invent one. No connector faces with pins, no
front or rear panels, no jacks, no sockets, no knobs, no product shapes, no brand marks, no
software windows. This is an abstract diagram of an idea. A convincing render of a wrong
connector is worse than no picture at all.
```

---

## Image 03 - power doubling is 3db

> **Replaces `power-doubling-is-3db-01.png`.** The delivered version is close but not right. Measured off the file, the right column is 1.83 times the height of the left, not 2.00, about nine percent short. Widths are fine at 0.995. For a figure whose entire content is the word EXACTLY, nine percent is the whole figure.

| Field | Value |
|---|---|
| Filename | `power-doubling-is-3db-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/power/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/power/power-doubling-is-3db-02.png` |
| Used on | Canvas page `Power: Power in Decibels - dBW & dBm` |
| Alt text | `One solid column beside a second column rendered at exactly twice its height` |
| Caption | `Figure 1. Doubling the power is plus 3 dB, whatever the starting number happens to be.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Render it as a richly rendered dimensional diagram, not a flat drawing and not a line
drawing. Three-quarter isometric perspective with real depth. Solid saturated colour fills,
soft ambient shading across every surface, a gentle contact shadow under every object where it
meets the ground plane, smooth rounded edges, a subtle glossy highlight on upward-facing
surfaces. Objects should look like solid physical things you could pick up, sitting on an
invisible floor.

Two solid rectangular columns stand side by side on a shared invisible ground plane, well
separated, both in deep green #1b5e20, both with real depth, soft shading and a contact shadow.

Both columns are EXACTLY the same width and EXACTLY the same depth as each other.

The RIGHT column is EXACTLY TWICE the height of the LEFT column, measured from the ground plane to
the top face. Not a little more, not two and a bit, and not one and eight tenths. Build it by
stacking the left column's exact height twice. This one ratio is the entire content of the image.

A smooth glossy arc in warm orange #993300, solid and rounded like a bent tube rather than a thin
line, springs from the top face of the left column, rises, and lands on the top face of the right
column.

Nothing else in the frame. Generous empty background above and around both columns.

Colours, and only these: deep green #1b5e20, warm orange #993300, deep blue #0d47a1,
near-black #212121, mid grey #616161, light grey #e0e0e0, white #ffffff.

NO TEXT ANYWHERE IN THIS IMAGE. Not a title, not a label, not a caption, not an axis name,
not a unit, not a legend, not a watermark, not a single stray letter or digit. Every one of the
twelve defects in an earlier batch was a text defect: a label clipped by the frame, two labels
printed over each other, a label silently dropped. None of them were drawing problems. The
Canvas page already carries the heading, the caption, the table and the prose, so every name in
this picture is supplied by the page. If you think a label is needed, leave it out and make the
shape clearer instead.

Do not draw any real hardware and do not invent one. No connector faces with pins, no
front or rear panels, no jacks, no sockets, no knobs, no product shapes, no brand marks, no
software windows. This is an abstract diagram of an idea. A convincing render of a wrong
connector is worse than no picture at all.
```

---

## Image 04 - midi gm channel 10

> **Replaces `midi-gm-channel-10-01.png`.** Flat line art, sixteen outlined squares. The idea is that one channel is set apart, which reads far better as one block physically lifted out of a row than as one square filled in.

| Field | Value |
|---|---|
| Filename | `midi-gm-channel-10-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-gm-channel-10-02.png` |
| Used on | Canvas page `MIDI: Timeline General MIDI and MMC` |
| Alt text | `Sixteen identical blocks in a row with the tenth one raised and coloured differently` |
| Caption | `Figure 1. General MIDI reserves the tenth channel for percussion. Send a melodic part there and it comes back as drums.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Render it as a richly rendered dimensional diagram, not a flat drawing and not a line
drawing. Three-quarter isometric perspective with real depth. Solid saturated colour fills,
soft ambient shading across every surface, a gentle contact shadow under every object where it
meets the ground plane, smooth rounded edges, a subtle glossy highlight on upward-facing
surfaces. Objects should look like solid physical things you could pick up, sitting on an
invisible floor.

Sixteen identical solid cubes stand in a single straight row on an invisible ground plane, evenly
spaced with a small consistent gap between neighbours, receding slightly into the distance in
three-quarter isometric perspective.

Fifteen of the cubes are deep green #1b5e20.

Counting from the LEFT, the TENTH cube is warm orange #993300 and is raised clear of the row,
floating a little above the ground plane with its own contact shadow on the floor beneath it, so it
is obviously singled out. Every other cube sits flat on the floor.

All sixteen cubes are the same size. The count must be exactly sixteen and the raised one must be
the tenth from the left. Nothing else in the frame.

Colours, and only these: deep green #1b5e20, warm orange #993300, deep blue #0d47a1,
near-black #212121, mid grey #616161, light grey #e0e0e0, white #ffffff.

NO TEXT ANYWHERE IN THIS IMAGE. Not a title, not a label, not a caption, not an axis name,
not a unit, not a legend, not a watermark, not a single stray letter or digit. Every one of the
twelve defects in an earlier batch was a text defect: a label clipped by the frame, two labels
printed over each other, a label silently dropped. None of them were drawing problems. The
Canvas page already carries the heading, the caption, the table and the prose, so every name in
this picture is supplied by the page. If you think a label is needed, leave it out and make the
shape clearer instead.

Do not draw any real hardware and do not invent one. No connector faces with pins, no
front or rear panels, no jacks, no sockets, no knobs, no product shapes, no brand marks, no
software windows. This is an abstract diagram of an idea. A convincing render of a wrong
connector is worse than no picture at all.
```

---

## Image 05 - midi same file two synths

> **Replaces `midi-same-file-two-synths-01.png`.** Flat line art with three text labels doing all the work. The two different waveform shapes are the content and they deserve to be objects, not outlines.

| Field | Value |
|---|---|
| Filename | `midi-same-file-two-synths-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-same-file-two-synths-02.png` |
| Used on | Canvas page `MIDI: What MIDI Is Not and Common Misunderstandings` |
| Alt text | `One block splitting along two paths into two boxes that emit two different waveform shapes` |
| Caption | `Figure 1. The same file, the same notes, two completely different sounds. The file holds instructions, not audio.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Render it as a richly rendered dimensional diagram, not a flat drawing and not a line
drawing. Three-quarter isometric perspective with real depth. Solid saturated colour fills,
soft ambient shading across every surface, a gentle contact shadow under every object where it
meets the ground plane, smooth rounded edges, a subtle glossy highlight on upward-facing
surfaces. Objects should look like solid physical things you could pick up, sitting on an
invisible floor.

One solid rounded block in deep blue #0d47a1 sits at the TOP CENTRE of the frame, raised slightly
above the ground plane.

Two smooth solid grey #616161 tubes leave its underside and curve down and outward, one to the
lower left and one to the lower right, each ending at its own solid box. The two boxes are
identical in size and shape, both in mid grey #616161, both standing on the ground plane with
contact shadows.

From the top face of the LEFT box rises a smooth, rounded, solid green #1b5e20 ribbon shaped as a
gentle SINE wave, two full cycles, like a length of bent tube.

From the top face of the RIGHT box rises a solid orange #993300 ribbon of the same thickness and
the same overall length shaped as a hard SQUARE wave, two full cycles, with sharp right-angle
corners.

The contrast between the smooth curved ribbon and the hard-cornered one is the whole picture, so
make both large and unmistakable. Nothing else in the frame.

Colours, and only these: deep green #1b5e20, warm orange #993300, deep blue #0d47a1,
near-black #212121, mid grey #616161, light grey #e0e0e0, white #ffffff.

NO TEXT ANYWHERE IN THIS IMAGE. Not a title, not a label, not a caption, not an axis name,
not a unit, not a legend, not a watermark, not a single stray letter or digit. Every one of the
twelve defects in an earlier batch was a text defect: a label clipped by the frame, two labels
printed over each other, a label silently dropped. None of them were drawing problems. The
Canvas page already carries the heading, the caption, the table and the prose, so every name in
this picture is supplied by the page. If you think a label is needed, leave it out and make the
shape clearer instead.

Do not draw any real hardware and do not invent one. No connector faces with pins, no
front or rear panels, no jacks, no sockets, no knobs, no product shapes, no brand marks, no
software windows. This is an abstract diagram of an idea. A convincing render of a wrong
connector is worse than no picture at all.
```

---

## Image 06 - midi clock vs mtc

> **Replaces `midi-clock-vs-mtc-01.png`.** Flat line art, two tick marks on two lines. The difference between a repeating pulse and a single position on a timeline is a difference in kind and should look like one.

| Field | Value |
|---|---|
| Filename | `midi-clock-vs-mtc-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-clock-vs-mtc-02.png` |
| Used on | Canvas page `MIDI: Timing Clocking and Synchronization` |
| Alt text | `A row of evenly spaced upright markers beside a long bar carrying one travelling pointer` |
| Caption | `Figure 1. MIDI Clock says how fast. MIDI Time Code says where you are. Many rigs run both at once.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Render it as a richly rendered dimensional diagram, not a flat drawing and not a line
drawing. Three-quarter isometric perspective with real depth. Solid saturated colour fills,
soft ambient shading across every surface, a gentle contact shadow under every object where it
meets the ground plane, smooth rounded edges, a subtle glossy highlight on upward-facing
surfaces. Objects should look like solid physical things you could pick up, sitting on an
invisible floor.

The frame is split into two halves by a generous gap of empty background, no divider line.

In the LEFT half, a row of twelve identical small solid upright green #1b5e20 posts stands on an
invisible ground plane, evenly spaced along a straight line running left to right, all exactly the
same height, like a row of fence posts. Regular, repeating, no beginning and no end implied: the
row runs off both edges of its half.

In the RIGHT half, one long solid horizontal bar in light grey #e0e0e0 lies flat along the ground
plane, clearly finite with a visible start and a visible end. Standing on that bar, about a third
of the way along from its left end, is a single solid orange #993300 pointer shaped like a rounded
downward-pointing wedge, taller than the bar is thick, casting its own small shadow on the bar.

The left half is many identical things repeating. The right half is one thing at one place on a
finite line. Nothing else in the frame.

Colours, and only these: deep green #1b5e20, warm orange #993300, deep blue #0d47a1,
near-black #212121, mid grey #616161, light grey #e0e0e0, white #ffffff.

NO TEXT ANYWHERE IN THIS IMAGE. Not a title, not a label, not a caption, not an axis name,
not a unit, not a legend, not a watermark, not a single stray letter or digit. Every one of the
twelve defects in an earlier batch was a text defect: a label clipped by the frame, two labels
printed over each other, a label silently dropped. None of them were drawing problems. The
Canvas page already carries the heading, the caption, the table and the prose, so every name in
this picture is supplied by the page. If you think a label is needed, leave it out and make the
shape clearer instead.

Do not draw any real hardware and do not invent one. No connector faces with pins, no
front or rear panels, no jacks, no sockets, no knobs, no product shapes, no brand marks, no
software windows. This is an abstract diagram of an idea. A convincing render of a wrong
connector is worse than no picture at all.
```

---

## Image 07 - midi what midi carries

> **Replaces `midi-what-midi-carries-01.png`.** Flat line art with four tiny outlined glyphs and a struck-through circle. The naming is done by the caption and by the table already on the page, so this figure only has to carry the contrast.

| Field | Value |
|---|---|
| Filename | `midi-what-midi-carries-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-what-midi-carries-02.png` |
| Used on | Canvas page `MIDI: What MIDI Is and Why It Exists` |
| Alt text | `Four small solid objects grouped on one side and a waveform ribbon crossed out on the other` |
| Caption | `Figure 1. MIDI carries which note, how hard, controller position and which patch. It does not carry audio. A MIDI file is a set of instructions, and the sound comes from whatever plays them.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Render it as a richly rendered dimensional diagram, not a flat drawing and not a line
drawing. Three-quarter isometric perspective with real depth. Solid saturated colour fills,
soft ambient shading across every surface, a gentle contact shadow under every object where it
meets the ground plane, smooth rounded edges, a subtle glossy highlight on upward-facing
surfaces. Objects should look like solid physical things you could pick up, sitting on an
invisible floor.

The frame is split into two halves by a generous gap of empty background, no divider line.

In the LEFT half, four small solid distinct objects sit grouped together on an invisible ground
plane, each with its own contact shadow, all in deep green #1b5e20 and all clearly different from
one another in shape: one upright rectangular key-like slab, one short wedge, one round dial-like
disc lying flat, and one small cube. They are a set of four separate things, obviously countable.

In the RIGHT half, a single smooth solid ribbon in mid grey #616161 shaped as a sine wave lies
across the space, the same style of solid bent-tube ribbon used elsewhere in the course. Across it,
a thick solid warm orange #993300 bar lies diagonally from upper left to lower right, passing over
the ribbon and clearly crossing it out. The orange bar sits in front of the ribbon and casts a soft
shadow onto it.

Four solid things on one side, one thing struck out on the other. Nothing else in the frame.

Colours, and only these: deep green #1b5e20, warm orange #993300, deep blue #0d47a1,
near-black #212121, mid grey #616161, light grey #e0e0e0, white #ffffff.

NO TEXT ANYWHERE IN THIS IMAGE. Not a title, not a label, not a caption, not an axis name,
not a unit, not a legend, not a watermark, not a single stray letter or digit. Every one of the
twelve defects in an earlier batch was a text defect: a label clipped by the frame, two labels
printed over each other, a label silently dropped. None of them were drawing problems. The
Canvas page already carries the heading, the caption, the table and the prose, so every name in
this picture is supplied by the page. If you think a label is needed, leave it out and make the
shape clearer instead.

Do not draw any real hardware and do not invent one. No connector faces with pins, no
front or rear panels, no jacks, no sockets, no knobs, no product shapes, no brand marks, no
software windows. This is an abstract diagram of an idea. A convincing render of a wrong
connector is worse than no picture at all.
```

---

## Image 08 - midi jitter buffer tradeoff

> **Replaces `midi-jitter-buffer-tradeoff-01.png`.** Flat line art, two hairline strokes and four labels, two of which sit on top of the lines. The shape of the trade is the content and it can be carried by two solid ribbons with no words at all.

| Field | Value |
|---|---|
| Filename | `midi-jitter-buffer-tradeoff-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-jitter-buffer-tradeoff-02.png` |
| Used on | Canvas page `MIDI: Synchronization Over IP` |
| Alt text | `Two solid ribbons crossing, one falling from left to right and one rising, over a plain floor` |
| Caption | `Figure 1. As buffer depth grows, timing instability falls and added delay rises. The useful setting is near the crossing.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Render it as a richly rendered dimensional diagram, not a flat drawing and not a line
drawing. Three-quarter isometric perspective with real depth. Solid saturated colour fills,
soft ambient shading across every surface, a gentle contact shadow under every object where it
meets the ground plane, smooth rounded edges, a subtle glossy highlight on upward-facing
surfaces. Objects should look like solid physical things you could pick up, sitting on an
invisible floor.

A wide, flat, light grey #e0e0e0 rectangular floor plane lies in three-quarter isometric
perspective, like a low platform.

Two smooth solid ribbons, each the thickness of a finger and rounded in section, run across that
floor from its left edge to its right edge, raised above it on thin invisible supports so each one
casts a soft shadow down onto the floor.

The ORANGE #993300 ribbon starts HIGH at the left edge and descends steadily to LOW at the right
edge.

The GREEN #1b5e20 ribbon starts LOW at the left edge and rises steadily to HIGH at the right edge.

They cross near the middle of the span. At the crossing the green ribbon passes in front of the
orange one, and the crossing point sits close to the centre of the frame so it reads as the
subject.

Along the left edge of the floor, a plain vertical solid grey #616161 post with a simple arrowhead
at the top. Along the front edge, a plain horizontal grey post with an arrowhead at the right. Both
are bare: no ticks, no numbers, no names.

Nothing else in the frame.

Colours, and only these: deep green #1b5e20, warm orange #993300, deep blue #0d47a1,
near-black #212121, mid grey #616161, light grey #e0e0e0, white #ffffff.

NO TEXT ANYWHERE IN THIS IMAGE. Not a title, not a label, not a caption, not an axis name,
not a unit, not a legend, not a watermark, not a single stray letter or digit. Every one of the
twelve defects in an earlier batch was a text defect: a label clipped by the frame, two labels
printed over each other, a label silently dropped. None of them were drawing problems. The
Canvas page already carries the heading, the caption, the table and the prose, so every name in
this picture is supplied by the page. If you think a label is needed, leave it out and make the
shape clearer instead.

Do not draw any real hardware and do not invent one. No connector faces with pins, no
front or rear panels, no jacks, no sockets, no knobs, no product shapes, no brand marks, no
software windows. This is an abstract diagram of an idea. A convincing render of a wrong
connector is worse than no picture at all.
```

---

## Saving these

ChatGPT will hand back a zip, or eight separate downloads. Do not unpack it by hand and do not
rename anything. Drop whatever you get into Downloads and run the filer:

```
python3 "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Build-Tools/file_images.py" ~/Downloads
```

It matches each image to its entry above even when the `-02` has been dropped or the extension
changed, writes it into the right topic folder under the right name, and prints what landed and
what is still missing. It refuses to overwrite anything. It is done when the missing list is empty.

Then `git add`, commit, push. The next cartridge repoints all eight pages and retires the `-01` files.

## What is deliberately NOT in this brief

**Seven diagrams are coming out as images entirely.** Their content is a set of labels, and a
generated label is a defect waiting to happen: the OSC anatomy figure currently on the page has
two labels printed on top of each other and reads `what kind of valuthe value`. These become
HTML on the page, where the text is real text a student can search, copy and read on a phone:

| File coming off the page | Page |
|---|---|
| `midi-osc-address-anatomy-01.png` | Open Sound Control Compared to MIDI |
| `midi-byte-structure-01.png` | Message Architecture and Data Structure |
| `midi-cross-protocol-isolation-01.png` | Extended Protocols Troubleshooting Checklist |
| `midi-vlan-segmentation-01.png` | Network Architecture and Topology |
| `midi-show-control-hub-01.png` | Network Based Show Control Systems |
| `midi-rtp-session-handshake-01.png` | RTP MIDI and AppleMIDI |
| `midi-dmx-universe-addressing-01.png` | DMX512 Protocol and Signal Structure |

The DMX one also has a content defect worth recording: its caption reads *two fixtures whose
ranges overlap both answer to the same channel*, and the picture shows three brackets that do
not overlap at all. The HTML version will show the overlap the caption describes.

**Sixteen images are photographs and must not be generated.** Standards 20.1 rule 3. We have
already shipped an XLR drawn with two pins and a DIN jack numbered wrong, and a photorealistic
render of a wrong pinout is more convincing and just as wrong. Students wire from these.

| Photograph | Page |
|---|---|
| A North American duplex outlet beside a 9 V battery and two cells | AC & DC: Overview, replacing a delivered image that shows a European round-pin outlet |
| A keyboard controller | What MIDI Is and Why It Exists |
| A rack sound module front panel | Device Roles Interfaces and Signal Flow |
| A multi port MIDI interface rear panel | Device Roles Interfaces and Signal Flow |
| A MIDI Thru box | Routing Channelization and Thru Management |
| A USB-B plug beside a USB-A plug | MIDI Over USB and Network |
| A USB-C port beside two DIN jacks | MIDI 2.0 What Changed and Why It Matters |
| The face of a 5-pin DIN socket | Device Roles Interfaces and Signal Flow |
| Two 3.5 mm TRS plugs, Type A against Type B | Device Roles Interfaces and Signal Flow |
| An LED wash fixture showing data in and data out | DMX512 Protocol and Signal Structure |
| A DMX terminator seated in a fixture | DMX512 Protocol and Signal Structure |
| A managed network switch front | Network Architecture and Topology |
| The test kit laid out flat | The Test Kit and How to Use It, a page that currently has no figure |
| A multimeter's three input jacks | Multimeters: Measuring DC Voltage, a page that currently has no figure |
| A finned CPU cooler | Power, Heat, & Component Ratings |
| An amplifier chassis heat sink | Power, Heat, & Component Ratings |

Four capture sheets for that shoot are already in `Images/_briefs/`. You own twelve of the
sixteen subjects, and the rest are a forty minute session on a sheet of white paper.
