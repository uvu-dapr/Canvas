# DAPR 2010 Core Recording Image Brief: the full run

Generated 2026-09-22. **31 prompts.** Run each one in its own ChatGPT message. Save each
result with the exact filename shown, into the exact folder shown. Do not rename.

Everything in this file is one complete pass: the figures that are wrong and need replacing,
the figures that are nearly right and need one thing fixed, and the new figures that take the
course from 31 of 56 pages carrying an image to 53 of 56, which is the 95 percent target.

## Read this before you start

**Background is opaque white, not transparent.** This differs from the two earlier briefs in
this folder, deliberately. Fourteen images in this course shipped transparent and render as
invisible dark line work anywhere that does not composite them on white, which is how the
polar patterns plate came back black on screen. Canvas is safe because Standards 1 pins the
page wrapper to white. A local browser, the cartridge preview and any dark mode viewer are
not.

**Numbers drawn in pixels must match numbers printed in labels.** This is the single most
common defect in this course. Three separate figures have shipped with a ratio, an angle or a
bar length that contradicts its own caption. Where a prompt gives exact pixel measurements,
they are there because a previous attempt got it wrong.

**Palette, Standards Section 3.** Outlines and body text `#212121`. Green `#1B5E20`. Blue
`#0D47A1`. Red `#B71C1C`. Copper `#993300`. Violet `#4A148C`. Gray `#616161`. Gold `#F9A825`.

**House style for every prompt below.** Flat vector style, clean line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature. Real readable lettering.
American spelling. No dashes of any kind in any label.

**Repo base folder**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/
```

## Not in this file, because ChatGPT cannot do them

| Item | Who does it |
|---|---|
| `console-signal-flow-asp4816-strip-input-02.png` | Re-crop from the Audient manual, landscape, 1600 px long edge. The other five strips are done |
| `console-operation-asp4816-connector-panel-02.png` | Re-crop into two or three zoomed sections so the port labels are readable |
| `console-signal-flow-asp4816-full-panel-02.png` | Re-crop to one channel strip plus one master section |
| `digital-recording-pro-tools-playback-engine-02.png` | A real Pro Tools screenshot. The current one is a drawn imitation |
| `tracking-pro-tools-record-arm-controls-02.png` | Re-annotate the existing screenshot. Two leader lines are cut off at the left edge and point at nothing |
| `studio-care-studio-floor-plan-02.png` | Waiting on your studio photos or a facilities drawing |

---

# PART 1. Wrong, must be replaced (2)

## 1. Three to one rule

Two attempts have missed the ratio in opposite directions. The `-01` drew about 2 to 1. The
`-02` drew exactly 4 to 1. The caption says three times. Pixel lengths are given because
describing the ratio in words has failed twice.

| Field | Value |
|---|---|
| Filename | `miking-techniques-three-to-one-rule-03.png` |
| Folder | `Images/miking-techniques/` |
| Format | PNG-24, opaque white background |
| Dimensions | 1600 x 800 px |

```text
Create a 1600 x 800 pixel PNG with a solid opaque white background. No transparency.
Flat vector geometric diagram, top-down plan view. No gradients, shadows, 3D or photorealism.

THE REQUIREMENT THAT MATTERS MOST, and two previous attempts got it wrong in opposite
directions: the horizontal arrow must be EXACTLY THREE TIMES the length of one vertical
arrow. Make each vertical arrow exactly 180 pixels long and the horizontal arrow exactly 540
pixels long. Measure both before you finish.

Two sound sources as filled circles on a lower horizontal line: a #B71C1C circle left, a
#0D47A1 circle right. Directly above each, at the same height, a microphone drawn as a small
white triangle outlined in #212121, pointing down at its own source.

A #1B5E20 double headed vertical arrow from the left source up to its microphone, exactly 180
pixels. An identical #1B5E20 double headed vertical arrow on the right, also exactly 180
pixels. A #0D47A1 double headed horizontal arrow between the two microphones, exactly 540
pixels. A #616161 dashed diagonal from the left source to the right microphone.

Labels in #212121 beneath the circles, exactly: "Source A", "Source B".
Labels on the vertical arrows in #1B5E20, exactly: "1 unit", "1 unit".
Label on the horizontal arrow in #0D47A1, exactly: "3 units minimum".
Label on the dashed diagonal in #616161, exactly: "Leakage path".
```

## 2. Spaced and near coincident arrays

The `-01` points the ORTF capsules inward at each other while printing 110 degrees, so the
drawn angle contradicts the printed number. NOS is missing entirely.

| Field | Value |
|---|---|
| Filename | `miking-techniques-spaced-arrays-02.png` |
| Folder | `Images/miking-techniques/` |
| Format | PNG-24, opaque white background |
| Dimensions | 1600 x 700 px |

```text
Create a 1600 x 700 pixel PNG with a solid opaque white background. No transparency.
Flat vector geometric diagram, top-down plan view. No gradients, shadows, 3D or photorealism.

Three panels of equal width separated by thin vertical #616161 dividers.

In every panel each microphone is a small cardioid polar pattern, one rounded lobe outlined
in #212121, with a short line through it showing the facing direction. THE CAPSULES ALWAYS
SPLAY OUTWARD, AWAY FROM EACH OTHER. They must never point inward at each other. That is the
error in the previous version.

Left panel: two cardioids widely separated, both facing straight forward and parallel. A
#0D47A1 horizontal dimension line between them with arrowheads at both ends.

Middle panel: two cardioids with bases close together, splayed OUTWARD so the angle between
the facing directions measures 110 degrees. A #0D47A1 arc between the facing directions and a
#0D47A1 dimension line between the bases.

Right panel: two cardioids with bases about twice as far apart as the middle panel, splayed
OUTWARD at 90 degrees. A #0D47A1 arc and a #0D47A1 dimension line.

Base spacing must be proportional across the three panels: middle narrowest, right about
twice the middle, left widest of all.

Panel titles across the top in #212121, exactly: "SPACED PAIR A-B", "ORTF", "NOS".
Dimension and arc labels in #0D47A1, exactly: "3 to 10 feet", "17 cm, 110 degrees",
"30 cm, 90 degrees".
Captions beneath each panel in smaller #212121 text, exactly: "Time differences, widest
image", "Time and level, ear spacing", "Wider than ORTF, one point of view".
```

---

# PART 2. Nearly right, one thing to fix (10)

## 3. Polar patterns

The cardioid rear is a three scallop wave with a bump at 180 instead of one smooth minimum.
The dB rings carry no numbers.

| Field | Value |
|---|---|
| Filename | `microphones-polar-patterns-03.png` |
| Folder | `Images/microphones/` |
| Dimensions | 1600 x 560 px, opaque white |

```text
Create a 1600 x 560 pixel PNG with a solid opaque white background. No transparency.
Flat vector technical diagram. No gradients, shadows or 3D.

Five polar response plots in one row, equally spaced. Each plot is a circular polar grid of
five thin #616161 concentric rings. On the FIRST plot only, print the ring values along the
vertical axis from the outer ring inward, exactly: "0 dB", "-5", "-10", "-15", "-20". Zero
degrees is straight up. A thin #212121 arrow above each plot pointing up, labeled "Front"
above the first plot only.

Fill each response curve solid medium green with a thin darker green outline.

Plot 1, OMNIDIRECTIONAL: a full circle touching the 0 dB ring at every angle.

Plot 2, CARDIOID: the curve r = 1 + cos(theta). ONE smooth rounded lobe facing up, widest
across the middle, narrowing smoothly and continuously to touch the exact center point only
at 180 degrees straight down. The rear must be a single smooth minimum. It must NOT have
scallops, ripples, a wave, or a bump at 180 degrees, and it must not look like a valentine
heart.

Plot 3, SUPERCARDIOID: narrower forward lobe, nulls at plus and minus 126 degrees, small rear
lobe reaching about -12 dB, joined to the front lobe at the nulls.

Plot 4, HYPERCARDIOID: narrower still, nulls at plus and minus 110 degrees, larger rear lobe
reaching about -6 dB, joined at the nulls.

Plot 5, FIGURE-OF-EIGHT: two equal lobes up and down meeting at the center, nulls at exactly
90 and 270 degrees. A small #212121 plus sign inside the upper lobe, a minus sign inside the
lower lobe.

Under each plot its name in bold #212121 capitals, exactly: "OMNIDIRECTIONAL", "CARDIOID",
"SUPERCARDIOID", "HYPERCARDIOID", "FIGURE-OF-EIGHT".
```

## 4. Decibel scales

Tick spacing is correct now, but the red NOMINAL annotation overprints the VU "+3" label into
unreadable garble.

| Field | Value |
|---|---|
| Filename | `gain-staging-decibel-scales-03.png` |
| Folder | `Images/gain-staging/` |
| Dimensions | 1600 x 900 px, opaque white |

```text
Create a 1600 x 900 pixel PNG with a solid opaque white background. No transparency.
Flat vector technical diagram. No gradients, shadows or 3D.

Three vertical scales side by side, evenly spaced, each drawn as a tall #212121 line with
horizontal tick marks and numeric labels to its LEFT. Titles above each in bold #212121,
exactly: "dBFS", "dBu", "VU".

dBFS scale, ticks and labels top to bottom, exactly: "0", "-6", "-12", "-18", "-24", "-30",
"-40", "-60". Spacing must be linear in decibels, so the gap from 0 to -6 equals the gap from
-6 to -12, and the gap from -40 to -60 is proportionally larger.

dBu scale, ticks top to bottom, exactly: "+24", "+18", "+12", "+4", "0", "-10", "-20".
Linear in decibels.

VU scale, ticks top to bottom, exactly: "+3", "0", "-5", "-10", "-20". Linear in decibels.

Draw ONE horizontal #B71C1C dashed line all the way across the three scales, crossing dBFS at
-18, dBu at +4, and VU at 0. Label this line "NOMINAL" in #B71C1C placed in the clear white
space to the RIGHT of the third scale, on the same horizontal line. THE LABEL MUST NOT
OVERLAP ANY TICK NUMBER. Keep at least 30 pixels of clear space between the label and the
nearest number.

Beneath the three scales, one line of #212121 text, exactly: "Same signal, three ways of
measuring it. Line up the nominal line, not the numbers."
```

## 5. Voltage divider

The circuit is right but the source return conductor stops in empty space under the ground
symbol, so the circuit reads as open.

| Field | Value |
|---|---|
| Filename | `impedance-voltage-divider-03.png` |
| Folder | `Images/impedance/` |
| Dimensions | 1600 x 760 px, opaque white |

```text
Create a 1600 x 760 pixel PNG with a solid opaque white background. No transparency.
Flat vector schematic. No gradients, shadows or 3D.

Left half: a complete closed circuit drawn in #212121 with standard schematic symbols.

A voltage source drawn as a circle with a plus above a minus inside it. From the plus
terminal, a wire runs right then down through a zigzag resistor labeled "Z source". Below
that resistor, a junction dot, and from the junction a wire runs right to an arrowhead
labeled "Output". Continuing down from the junction, a second zigzag resistor labeled
"Z load", and below it a wire down to a standard ground symbol of three shortening horizontal
bars.

CRITICAL: from the ground symbol a wire must run LEFT and then UP, all the way back to the
minus terminal of the voltage source, closing the loop. Every conductor must terminate on a
component or a junction. NO wire may end in empty space. The previous version left this
return conductor unconnected.

Right half: a three row table with a #212121 border, two columns, header row filled #0D47A1
with white text. Header cells exactly: "Load compared to source", "Voltage at the output".
Rows exactly: "10 times the source" and "91 percent"; "Equal to the source" and "50 percent";
"One tenth of the source" and "9 percent".

Beneath the table, one line of #212121 text, exactly: "Bridging means the load is at least
ten times the source. That is why studio gear barely loses any level."
```

## 6. Normalling types

Only the top jack plug case is drawn. The bottom jack case is described in the caption but
never shown, and it is the case that defines half normal.

| Field | Value |
|---|---|
| Filename | `patch-bays-normalling-types-03.png` |
| Folder | `Images/patch-bays/` |
| Dimensions | 1600 x 1000 px, opaque white |

```text
Create a 1600 x 1000 pixel PNG with a solid opaque white background. No transparency.
Flat vector schematic. No gradients, shadows or 3D.

A grid three columns wide and three rows tall.

Column titles across the top in bold #212121 capitals, exactly: "FULL NORMAL", "HALF NORMAL",
"OPEN".
Row labels down the left side in #212141 text, exactly: "Nothing plugged in", "Plug in the
TOP jack", "Plug in the BOTTOM jack".

Every cell shows the same pair of jacks in cross section: an upper jack labeled "TOP: source
out" and a lower jack labeled "BOTTOM: destination in", small #212121 text. Between them draw
the internal normal connection as a #1B5E20 line when signal passes, and as a #1B5E20 line
with a clear gap and a small #B71C1C X on the gap when the normal is broken. Where a patch
cable is inserted, draw it as a #0D47A1 line leaving the jack to the edge of the cell.

Row 1: all three columns show no patch cable. Full normal and half normal show an unbroken
green line. Open shows NO line at all between the two jacks, just a clear gap.

Row 2, plug in the top jack: Full normal shows the green line BROKEN with the red X, plus a
blue cable from the top jack. Half normal shows the green line UNBROKEN and continuing to the
bottom jack, PLUS a blue cable from the top jack, so signal goes both ways. Open shows the
blue cable only, still no green line.

Row 3, plug in the bottom jack: Full normal shows the green line broken with the red X, plus
a blue cable into the bottom jack. Half normal ALSO shows the green line broken with the red
X, plus a blue cable into the bottom jack. Open shows the blue cable only.

Every green and blue line must terminate at a jack or leave the cell edge. No line may end in
empty space.

One line of #212121 text beneath the grid, exactly: "Half normal is the only one where a plug
in the top jack leaves the normal intact."
```

## 7. Drum overhead techniques

Only two techniques are shown, the coincident pair is drawn as two near parallel mics rather
than a crossed XY, and the equal distance label sits on the panel divider.

| Field | Value |
|---|---|
| Filename | `drums-overhead-techniques-02.png` |
| Folder | `Images/drums/` |
| Dimensions | 1600 x 700 px, opaque white |

```text
Create a 1600 x 700 pixel PNG with a solid opaque white background. No transparency.
Flat vector diagram, top-down plan view. No gradients, shadows or 3D.

Three panels of equal width separated by thin vertical #616161 dividers. Titles in bold
#212121 capitals, exactly: "SPACED PAIR", "COINCIDENT XY", "RECESSED, THREE MIC".

In every panel draw a simple top-down drum kit: a large circle for the kick at the front, a
medium circle labeled "Snare" to the left of center, two smaller circles for toms, and two
large thin circles for cymbals. Keep the kit identical in all three panels. Microphones are
small #212121 triangles.

Panel 1, SPACED PAIR: two microphones above the kit, well apart, both pointing straight down
at the kit. A #0D47A1 dashed line from each microphone to the snare, both lines clearly the
SAME length, with a #0D47A1 label placed on the lines themselves, exactly: "Equal distance to
the snare".

Panel 2, COINCIDENT XY: two microphones whose bodies CROSS at a single point above the center
of the kit, angled 90 degrees apart, one pointing down-left and one pointing down-right. They
must visibly cross, not sit parallel. A #0D47A1 arc between them labeled "90 degrees".

Panel 3, RECESSED, THREE MIC: one microphone above the snare pointing down, one over the
drummer's right shoulder pointing at the snare, and one to the left of the floor tom pointing
across the kit at the snare. #0D47A1 dashed lines from the two overheads to the snare, drawn
the SAME length, labeled on the lines, exactly: "Equal distance to the snare".

No label may sit on a panel divider. Every label sits inside its own panel.
```

## 8. DI and amp blend

The split is drawn at a bare junction ahead of the DI rather than at the DI thru output, and
nothing addresses polarity or time alignment.

| Field | Value |
|---|---|
| Filename | `guitar-bass-di-and-amp-blend-02.png` |
| Folder | `Images/guitar-bass/` |
| Dimensions | 1600 x 800 px, opaque white |

```text
Create a 1600 x 800 pixel PNG with a solid opaque white background. No transparency.
Flat vector signal flow diagram, left to right. No gradients, shadows or 3D.

Draw rounded rectangles outlined in #212121 connected by #212121 arrows.

Chain: a box labeled "Bass or guitar" on the far left. An arrow to a box labeled "DI box".
From the DI box, TWO outputs leave, and they must leave from the DI box itself, not from a
bare junction before it.

Upper output, labeled on the arrow "THRU output, unbalanced": an arrow to a box labeled
"Amplifier", then an arrow to a box labeled "Speaker cabinet", then an arrow to a small
#212121 triangle labeled "Microphone", then an arrow to a box labeled "Preamp", then an arrow
to a box labeled "DAW track 2, amp".

Lower output, labeled on the arrow "XLR output, balanced": a long arrow running straight to a
box labeled "Preamp", then an arrow to a box labeled "DAW track 1, DI".

Draw the two paths clearly separated vertically so they never cross.

Below the two DAW track boxes, a #F9A825 filled callout box with #212121 text reading exactly:
"The mic path arrives later than the DI path. Nudge the amp track earlier until the low end
locks, then check the pair in mono. If the low end disappears, flip polarity on one track."
```

## 9. Speaker cone positions

Four labels serve three microphone positions, two leader lines point at the same spot, and
label text overlaps the speaker outline.

| Field | Value |
|---|---|
| Filename | `guitar-bass-speaker-cone-positions-02.png` |
| Folder | `Images/guitar-bass/` |
| Dimensions | 1600 x 900 px, opaque white |

```text
Create a 1600 x 900 pixel PNG with a solid opaque white background. No transparency.
Flat vector diagram. No gradients, shadows or 3D.

Draw one guitar speaker seen face on, as a large #212121 circle with a smaller concentric
circle for the cone and a small filled circle at the exact center for the dust cap. Place it
on the LEFT half of the image, leaving the right half clear for labels.

Place exactly THREE microphone positions, each a small #212121 triangle touching the speaker
face, each numbered in a small filled #0D47A1 circle:

1. Dead center on the dust cap.
2. Halfway between the dust cap and the outer edge of the cone.
3. At the outer edge of the cone.

From each numbered microphone draw one #616161 leader line to the RIGHT, into the clear half
of the image. Each leader line ends at its own label, and the three labels are stacked
vertically with clear space between them. No leader line may cross another and no label may
overlap the speaker.

Label 1 exactly: "1. On the dust cap. Brightest, most aggressive, most upper midrange."
Label 2 exactly: "2. Halfway out. The usual starting point. Balanced."
Label 3 exactly: "3. At the cone edge. Darkest and warmest, least bite."

Beneath the speaker, one line of #212121 text, exactly: "Moving from the center to the edge
rolls off the top end. Move the microphone before you reach for an equalizer."
```

## 10. Early reflections

Angle of incidence does not equal angle of reflection, the reflection points float inside the
room rather than sitting on the wall, and no time gap is shown.

| Field | Value |
|---|---|
| Filename | `acoustics-early-reflections-02.png` |
| Folder | `Images/acoustics/` |
| Dimensions | 1600 x 900 px, opaque white |

```text
Create a 1600 x 900 pixel PNG with a solid opaque white background. No transparency.
Flat vector diagram, top-down plan view. No gradients, shadows or 3D.

Upper two thirds: a rectangular room drawn as four #212121 walls. Inside, near the top wall,
two speakers drawn as small trapezoids angled inward. Below them, centered, a small circle
labeled "Listening position".

From the LEFT speaker draw three #0D47A1 rays to the listening position:
1. A straight direct ray, labeled on the line "Direct".
2. A ray that strikes the LEFT side wall and continues to the listener. The bounce point must
   sit exactly ON the wall line, marked with a small filled dot. The angle between the
   incoming ray and the wall must EQUAL the angle between the outgoing ray and the wall. Draw
   a thin #616161 dashed line perpendicular to the wall at the bounce point and mark both
   angles with matching arcs labeled "a" and "a".
3. A ray that strikes the ceiling, drawn the same way with its bounce point on the wall line
   and matching angles.

Lower third: a horizontal #212121 time axis labeled "Time". Draw four vertical bars rising
from it. The first is tall and labeled "Direct sound". Then a clear horizontal gap. Then two
shorter bars close together labeled "Early reflections". Then a cluster of many very short
bars labeled "Reverberation". Mark the gap between the first bar and the second with a
#B71C1C dimension arrow labeled "The gap your ear uses to locate the source".
```

## 11. Reflection, absorption, diffusion

In the diffusion panel the incoming ray overlaps a scattered ray and collides with a stray
arrowhead, so the incident direction is unreadable.

| Field | Value |
|---|---|
| Filename | `acoustics-reflection-absorption-diffusion-02.png` |
| Folder | `Images/acoustics/` |
| Dimensions | 1600 x 700 px, opaque white |

```text
Create a 1600 x 700 pixel PNG with a solid opaque white background. No transparency.
Flat vector diagram. No gradients, shadows or 3D.

Three panels of equal width separated by thin vertical #616161 dividers. Titles in bold
#212121 capitals, exactly: "REFLECTION", "ABSORPTION", "DIFFUSION".

In every panel draw the same wall as a thick vertical #212121 line on the RIGHT side of the
panel, and bring one incoming #0D47A1 ray in from the upper LEFT, striking the wall at the
same point in all three panels. The incoming ray must be clearly the thickest line in the
panel and nothing may cross it or touch it.

Panel 1, REFLECTION: one #0D47A1 outgoing ray leaving the strike point at the mirror angle,
heading to the lower left. Thin #616161 dashed normal at the strike point, with matching arcs
on both sides. Caption beneath in #212121, exactly: "Angle in equals angle out. The room
sends it straight back at you."

Panel 2, ABSORPTION: draw the wall with a hatched #993300 panel on its face. The incoming ray
stops at the panel. One much thinner, shorter #0D47A1 ray leaves at the mirror angle. Small
#993300 squiggles inside the panel. Caption exactly: "Most of the energy turns into heat
inside the material. Very little comes back."

Panel 3, DIFFUSION: draw the wall with a stepped #4A148C block of uneven depths on its face.
From the strike point, FIVE thin #0D47A1 rays fan outward in clearly different directions,
every one of them heading LEFT and DOWN, well below the incoming ray so that none of them
overlaps or touches it. Caption exactly: "The energy still comes back, spread across many
directions instead of one."
```

## 12. Drum microphone placement

A second rack tom is drawn with no mic and no label, and the two overhead sightlines are
clearly unequal distances from the snare.

| Field | Value |
|---|---|
| Filename | `drums-microphone-placement-02.png` |
| Folder | `Images/drums/` |
| Dimensions | 1600 x 1000 px, opaque white |

```text
Create a 1600 x 1000 pixel PNG with a solid opaque white background. No transparency.
Flat vector diagram, top-down plan view. No gradients, shadows or 3D.

Draw a five piece drum kit from above in #212121 outline: a large circle at the front for the
kick, a medium circle labeled "Snare", ONE rack tom, ONE floor tom, a hi hat, and two cymbals
drawn as large thin circles. Every drum and cymbal in the picture must have a label and a
microphone. Do not draw any drum you do not label.

Microphones are small #212121 triangles, each numbered in a filled #0D47A1 circle:
1. Inside the kick, pointing at the beater.
2. Above the snare, pointing down at the center of the head, angled away from the hi hat.
3. Above the rack tom.
4. Above the floor tom.
5. Above the hi hat, pointing down at the outer edge.
6. Overhead left.
7. Overhead right.

Draw #0D47A1 dashed sightlines from microphone 6 and from microphone 7 to the center of the
snare. THESE TWO LINES MUST BE DRAWN EXACTLY THE SAME LENGTH. Label them on the lines,
exactly: "Equal distance to the snare".

To the right of the kit, a numbered key in #212121 listing 1 through 7, exactly: "1 Kick",
"2 Snare top", "3 Rack tom", "4 Floor tom", "5 Hi hat", "6 Overhead left",
"7 Overhead right".
```

---

# PART 3. New figures, module reading pages (5)

## 13. Pressure versus pressure gradient

Replaces `microphones-se-gradient-diagram.png`, which is a photo of a console rear panel and
not a transducer diagram at all.

| Field | Value |
|---|---|
| Filename | `microphones-pressure-vs-gradient-01.png` |
| Folder | `Images/microphones/` |
| Dimensions | 1600 x 700 px, opaque white |

```text
Create a 1600 x 700 pixel PNG with a solid opaque white background. No transparency.
Flat vector cross section diagram. No gradients, shadows or 3D.

Two panels of equal width separated by a thin vertical #616161 divider. Titles in bold
#212121 capitals, exactly: "PRESSURE", "PRESSURE GRADIENT".

Left panel: a microphone capsule in cross section as a sealed cylindrical housing outlined in
#212121. One diaphragm across the front. The rear of the housing is CLOSED and sealed, with
one tiny hole labeled "static vent only". #0D47A1 arrows arrive at the diaphragm from the
front, from both sides and from behind, all reaching it. Below the capsule a small polar plot
showing a complete circle, labeled "Omnidirectional". Caption in #212121, exactly: "Sealed at
the back. Responds to pressure alone, so it hears every direction equally."

Right panel: a capsule whose diaphragm is OPEN TO THE AIR ON BOTH SIDES, drawn as a thin
membrane suspended in a frame with clear open space in front of it and behind it. #0D47A1
arrows arrive at the front face and at the rear face. Arrows arriving from directly left and
right strike the diaphragm edge on and are marked with a small #B71C1C X. Below the capsule a
small polar plot of two equal lobes, one up and one down, meeting at the center, labeled
"Bidirectional, figure of eight", with a #212121 plus sign in the upper lobe and a minus sign
in the lower. Caption exactly: "Open on both sides. Responds to the difference between front
and back, so sound from the sides cancels."

The sealed rear on the left and the open rear on the right are the entire point. Do not draw
the gradient capsule with a sealed back.
```

## 14. Preparing the kit

| Field | Value |
|---|---|
| Filename | `drums-tuning-and-prep-01.png` |
| Folder | `Images/drums/` |
| Dimensions | 1600 x 800 px, opaque white |
| Used on | `Drums: Preparing the Kit` |

```text
Create a 1600 x 800 pixel PNG with a solid opaque white background. No transparency.
Flat vector diagram. No gradients, shadows or 3D.

Left half: one drum seen from directly above, drawn in #212121 as two concentric circles with
eight tension rods evenly spaced around the rim, each rod a small filled square. Number the
rods 1 through 8 in small #0D47A1 circles following a STAR pattern, not a circle: place 1 at
the top, 2 at the bottom, 3 at the right, 4 at the left, 5 upper right, 6 lower left, 7 upper
left, 8 lower right. Draw thin #616161 lines connecting 1 to 2, 3 to 4, 5 to 6 and 7 to 8 to
make the star visible. Caption beneath in #212121, exactly: "Tune in opposite pairs, never
around the rim."

Right half: a vertical checklist of five rounded rectangles outlined in #212121, each with a
small #1B5E20 check mark at its left, stacked with clear space between them. Text inside
each, exactly:
"Seat every head, then tune in pairs"
"Kill the ring with tape or a gel, one at a time"
"Tighten every lug and every stand"
"Move squeaking pedals and rattling hardware"
"Fresh sticks, spare heads, spare batteries"

Title across the top in bold #212121 capitals, exactly: "BEFORE A MICROPHONE GOES UP".
```

## 15. Handling gear that can be destroyed

| Field | Value |
|---|---|
| Filename | `studio-care-gear-handling-01.png` |
| Folder | `Images/studio-care/` |
| Dimensions | 1600 x 800 px, opaque white |
| Used on | `Studio Care: Handling Gear That Can Be Destroyed` |

```text
Create a 1600 x 800 pixel PNG with a solid opaque white background. No transparency.
Flat vector diagram. No gradients, shadows or 3D.

Four panels of equal width separated by thin vertical #616161 dividers. Each panel has a
title in bold #212121 capitals at the top, a simple line drawing in the middle, and one line
of caption text at the bottom.

Panel 1, title "RIBBON MICROPHONE". Draw a ribbon microphone body with a #B71C1C circle
around it containing a diagonal bar over a small phantom power symbol reading "48V", and a
second #B71C1C crossed-out symbol over a small drawing of a hand held in front of the mic
blowing air. Caption exactly: "Phantom power and moving air both kill ribbons."

Panel 2, title "CONDENSER MICROPHONE". Draw a large diaphragm condenser in a shock mount with
#0D47A1 arrows showing it being lifted straight up and out. Caption exactly: "Lift by the
body, never by the basket. Case it the moment it comes down."

Panel 3, title "CABLES". Draw a cable coiled in smooth even loops, with a #1B5E20 check mark
beside it, and beside that a cable wrapped tight around an elbow with a #B71C1C X. Caption
exactly: "Over under, every time. Wrapping around your arm twists the conductor."

Panel 4, title "MONITORS". Draw a powered monitor with a #212121 power switch, and a numbered
order in #0D47A1 circles: 1 beside a source box, 2 beside a console, 3 beside the monitor.
Caption exactly: "Monitors go on last and off first. A pop at full gain costs a driver."
```

## 16. Connecting real studio gear without damage

| Field | Value |
|---|---|
| Filename | `impedance-safe-interconnection-01.png` |
| Folder | `Images/impedance/` |
| Dimensions | 1600 x 800 px, opaque white |
| Used on | `Impedance: Connecting Real Studio Gear Without Damage` |

```text
Create a 1600 x 800 pixel PNG with a solid opaque white background. No transparency.
Flat vector diagram. No gradients, shadows or 3D.

Three rows, each a short left to right signal chain of rounded rectangles outlined in #212121
joined by arrows. Each row has a verdict badge at its right end: a filled #1B5E20 circle with
a white check mark, or a filled #B71C1C circle with a white X.

Row 1: "Microphone, 150 ohms" arrow "Preamp input, 2 kilohms" then a green check. Label above
the arrow in #1B5E20, exactly: "Load is 13 times the source. Bridging."

Row 2: "Line output, 100 ohms" arrow "Line input, 10 kilohms" then a green check. Label above
the arrow in #1B5E20, exactly: "Load is 100 times the source. Bridging."

Row 3: "Amplifier speaker output" arrow "Line input, 10 kilohms" then a red X. Label above
the arrow in #B71C1C, exactly: "Never. Speaker level into a line input destroys the input."

Beneath the three rows, a #F9A825 filled callout with #212121 text, exactly: "The rule is ten
to one. If the load is at least ten times the source impedance you keep your level. If it is
lower you lose level, and if it is a speaker output you lose the gear."
```

## 17. What an assistant actually does

| Field | Value |
|---|---|
| Filename | `studio-etiquette-assistant-timeline-01.png` |
| Folder | `Images/studio-etiquette/` |
| Dimensions | 1600 x 800 px, opaque white |
| Used on | `Studio Etiquette: What an Assistant Actually Does` |

```text
Create a 1600 x 800 pixel PNG with a solid opaque white background. No transparency.
Flat vector timeline diagram. No gradients, shadows or 3D.

One horizontal #212121 timeline arrow running left to right across the middle of the image,
with four evenly spaced milestone dots. Above each dot a title in bold #212121 capitals,
below each dot a stacked list of three short lines in smaller #212121 text.

Milestone 1, title "BEFORE, 60 MINUTES". Lines exactly: "Room set, cables run", "Session
template open and named", "Headphone mixes built".

Milestone 2, title "SETUP, 30 MINUTES". Lines exactly: "Microphones placed and labeled",
"Levels checked on every channel", "Talkback tested".

Milestone 3, title "DURING". Lines exactly: "Take notes on every pass", "Anticipate the next
request", "Say nothing about the performance".

Milestone 4, title "AFTER". Lines exactly: "Back up before anyone leaves", "Coil and return
every cable", "Room reset for the next session".

Color the first two milestone dots #1B5E20, the third #0D47A1, the fourth #4A148C.

Beneath the timeline, one line of #212121 text, exactly: "The engineer is paid for the two
hours in the middle. You are paid for the hour on either side."
```

---

# PART 4. New figures, module overview pages (14)

Each of these is one wide banner figure that sits under the page title on a module overview.
They all share a layout so the course reads as one system: a wide strip, a single subject
drawn left of center, and three short labeled callouts stacked on the right.

Common instruction for all 14 prompts below: **1600 x 500 pixels, solid opaque white
background, no transparency, flat vector, no gradients, shadows or 3D, real readable Arial
style lettering, American spelling, no dashes of any kind.**

## 18 to 31. The fourteen overview banners

| # | Filename | Folder | Subject drawn on the left | Three callouts on the right, exact text |
|---|---|---|---|---|
| 18 | `studio-etiquette-overview-banner-01.png` | `studio-etiquette/` | A control room seen from behind the console, two figures at the desk, one standing at the back | "Be early", "Be invisible", "Be useful" |
| 19 | `studio-care-overview-banner-01.png` | `studio-care/` | A tidy equipment rack with coiled cables hung beside it | "Power in order", "Handle with two hands", "Leave it better" |
| 20 | `microphones-overview-overview-banner-01.png` | `microphones/` | Three microphones side by side in silhouette: a handheld dynamic, a large diaphragm condenser, a ribbon | "Type", "Pattern", "Placement" |
| 21 | `patch-bays-overview-banner-01.png` | `patch-bays/` | A patch bay row of 24 jacks with two patch cables crossing in front of it | "Source on top", "Destination below", "The normal does the work" |
| 22 | `console-signal-flow-overview-banner-01.png` | `console-signal-flow/` | One console channel strip in silhouette from input at the top to fader at the bottom | "In at the top", "Down the strip", "Out at the bus" |
| 23 | `console-operation-overview-banner-01.png` | `console-operation/` | A pair of hands on a console center section with monitor and talkback controls | "Gain first", "Route second", "Monitor last" |
| 24 | `gain-staging-overview-banner-01.png` | `gain-staging/` | Three meters in a row, one too low, one correct, one clipping in red | "Too quiet is noise", "Too loud is distortion", "Aim for the middle" |
| 25 | `impedance-overview-banner-01.png` | `impedance/` | A source box and a load box joined by a cable, with a simple resistor symbol in each | "Source low", "Load high", "Ten to one" |
| 26 | `digital-recording-overview-banner-01.png` | `digital-recording/` | A smooth analog wave on the left turning into a stair stepped digital wave on the right | "Sample rate is how often", "Bit depth is how finely", "Headroom is your insurance" |
| 27 | `tracking-overview-banner-01.png` | `tracking/` | A Pro Tools style edit window in simple outline with four tracks and a playhead | "Template first", "Name before you record", "Back up before you leave" |
| 28 | `miking-techniques-overview-banner-01.png` | `miking-techniques/` | Two microphones on a stereo bar aimed at an acoustic guitar | "One point or two", "Time or level", "Check it in mono" |
| 29 | `acoustics-overview-banner-01.png` | `acoustics/` | A room in cross section with sound rays bouncing off the walls to a listener | "Direct sound", "Early reflections", "Reverberation" |
| 30 | `drums-overview-banner-01.png` | `drums/` | A drum kit seen from the front with microphone stands around it | "Tune it first", "Close and far", "Mono is the test" |
| 31 | `guitar-bass-overview-banner-01.png` | `guitar-bass/` | A guitar amplifier with a microphone on a short stand at the grille, and a bass DI box beside it | "Amp or DI", "Or both", "Align before you blend" |

**Prompt template. Paste this once per row, swapping only the two bracketed parts.**

```text
Create a 1600 x 500 pixel PNG with a solid opaque white background. No transparency.
Flat vector illustration in a clean editorial style. No gradients, no drop shadows, no 3D, no
photorealism, no watermark, no signature.

Left two thirds: [SUBJECT FROM THE TABLE], drawn as a simple #212121 line illustration with
flat fills in #616161 and one accent color of #1B5E20. Keep it uncluttered and readable at a
glance. No text anywhere in the illustration itself.

Right one third: three short labels stacked vertically with generous space between them, each
preceded by a small filled #1B5E20 circle. The three labels, in #212121, exactly:
"[CALLOUT ONE]"
"[CALLOUT TWO]"
"[CALLOUT THREE]"

Nothing else in the image. No title, no border, no caption, no extra words.
```

---

## When you are done

Save every file into the folder named in its table, then push:

```
cd "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas" && git add Classes/DAPR-2010--Core_Recording && git commit -m "DAPR 2010: image pass, corrections and overview banners" && git push origin main
```

Tell me when it is pushed and I will open every one of them, wire them into the pages, rebuild
and run both gates.
