# DAPR 2010 Core Recording Image Brief: corrections

Generated 2026-09-22. Run each prompt separately in ChatGPT. Save each result with the
exact filename shown, into the exact folder shown. Do not rename.

**This replaces nothing.** The two originals stay on disk. Standards 20.4 says a revised
image gets the next number and the original is never overwritten, which is why the
filenames below end in `-03` and `-02`.

**Background: fully transparent, and every label sits on its own filled chip.**
A figure has to survive whatever color the page behind it is. An opaque white plate looks
like a white slab the moment the page is tinted, so the background is transparent PNG-24.
The failure transparency used to cause, dark line work going invisible on a dark page, is
fixed in the drawing rather than in the background: every text label, value and caption sits
inside its own filled shape, a white or light gray chip with a `#212121` outline, rather than
floating naked on the background. Boxes, chips and panels keep their solid fills. Only the
area outside the artwork is transparent. Canvas itself pins the page wrapper to `#ffffff`
under Standards 1, so this costs nothing there and buys a figure that also reads on a tinted
page, in the cartridge preview and in a dark mode viewer.

**Photographs, console panel crops and application screenshots are the exception.** Those
are rectangular rasters with no background to remove, so they stay opaque and full bleed.

**Palette, from Standards Section 3.** Body text and outlines `#212121`. Green `#1B5E20`.
Blue `#0D47A1`. Red `#B71C1C`. Copper and orange `#993300`. Violet `#4A148C`. Muted gray
`#616161`.

**One prompt per ChatGPT message.** Two pasted together come back as one crowded composite.

---

## Correction 1 of 2 - Three to one rule

Two attempts have now missed the ratio in opposite directions. The `-01` drew about 2 to 1.
The `-02` drew exactly 4 to 1. The caption on the page says three times, so the picture has
contradicted its own caption both times. This prompt gives pixel lengths rather than a ratio
in words, because describing the ratio in words has now failed twice.

| Field | Value |
|---|---|
| Filename | `miking-techniques-three-to-one-rule-03.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 800 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/miking-techniques/` |
| Used on | Canvas page `Miking Techniques: Five Stereo Arrays` |
| Caption | `Figure 3. The three to one rule. Each microphone sits one unit from its own source, and the two microphones sit at least three units apart.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 800 pixel PNG with a fully transparent background. Every text label sits on its own filled chip, never naked on the background.

Flat vector-style geometric diagram, top-down plan view. Clean line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

THE ONE REQUIREMENT THAT MATTERS MOST, and two previous attempts got it wrong in opposite
directions: the horizontal arrow must be EXACTLY THREE TIMES the length of one vertical
arrow. Not two times. Not four times. Make each vertical arrow exactly 180 pixels long and
the horizontal arrow exactly 540 pixels long. Measure both before you finish.

Draw two sound sources as filled circles on a lower horizontal line: a #B71C1C circle on the
left and a #0D47A1 circle on the right.

Directly above each source, at the same height, draw a microphone as a small triangle
outlined in #212121 with a white fill, pointing down at its own source.

Draw a #1B5E20 double headed vertical arrow from the left source up to the microphone above
it, exactly 180 pixels long. Draw an identical #1B5E20 double headed vertical arrow from the
right source up to its own microphone, also exactly 180 pixels long. Both must be the same
length.

Draw a #0D47A1 double headed horizontal arrow between the two microphones, exactly 540
pixels long.

Draw a #616161 dashed diagonal line from the left source to the microphone above the right
source.

Label in #212121 beneath the circles, exactly: "Source A", "Source B".
Label the two vertical arrows in #1B5E20, exactly: "1 unit", "1 unit".
Label the horizontal arrow in #0D47A1, exactly: "3 units minimum".
Label the dashed diagonal in #616161, exactly: "Leakage path".
```

---

## Correction 2 of 2 - Spaced and near coincident arrays

The `-01` draws the ORTF capsules pointing inward toward each other while printing 110
degrees, so the drawn angle contradicts the printed number. NOS is missing entirely.

| Field | Value |
|---|---|
| Filename | `miking-techniques-spaced-arrays-02.png` |
| Format | PNG-24, fully transparent background |
| Dimensions | 1600 x 700 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/miking-techniques/` |
| Used on | Canvas page `Miking Techniques: Five Stereo Arrays` |
| Caption | `Figure 1. The spaced and near coincident arrays. Separating the capsules adds arrival time difference to the level difference.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 700 pixel PNG with a fully transparent background. Every text label sits on its own filled chip, never naked on the background.

Flat vector-style geometric diagram, top-down plan view. Clean line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Three panels of equal width, separated by thin vertical #616161 divider lines.

In every panel each microphone is drawn as a small cardioid polar pattern, a single rounded
lobe outlined in #212121, with a short line through it showing the direction the capsule
faces. THE CAPSULES ALWAYS SPLAY OUTWARD, AWAY FROM EACH OTHER. They must never point inward
toward each other. That is the error in the previous version.

Left panel: two cardioids side by side, widely separated, both facing straight forward and
parallel to each other. Draw a #0D47A1 horizontal dimension line between them with arrowheads
at both ends.

Middle panel: two cardioids whose bases are close together, splayed OUTWARD so the angle
between the two facing directions measures 110 degrees. Draw a #0D47A1 arc between the two
facing directions and a #0D47A1 horizontal dimension line between the bases. The drawn angle
must actually measure 110 degrees.

Right panel: two cardioids whose bases are about twice as far apart as the middle panel,
splayed OUTWARD at 90 degrees between the facing directions. Draw a #0D47A1 arc and a #0D47A1
horizontal dimension line. The drawn angle must actually measure 90 degrees.

The base spacing must be proportional across the three panels: middle panel narrowest, right
panel about twice the middle, left panel widest of all.

Label the panels across the top in #212121, exactly: "SPACED PAIR A-B", "ORTF", "NOS".
Label the dimension lines and arcs in #0D47A1, exactly: "3 to 10 feet", "17 cm, 110 degrees",
"30 cm, 90 degrees".
Label beneath each panel in smaller #212121 text, exactly: "Time differences, widest image",
"Time and level, ear spacing", "Wider than ORTF, one point of view".

Reading direction is left to right.
```
