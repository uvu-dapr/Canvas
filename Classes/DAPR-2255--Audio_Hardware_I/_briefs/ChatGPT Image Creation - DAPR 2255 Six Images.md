# DAPR 2255: Six Images to Generate

Copy one prompt block at a time. Save each result with the exact filename shown,
into the folder shown. Six images, all transparent PNG at 1600 x 900.

## Folders

Images 1 and 2:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/diodes-leds/
```

Images 3 through 6:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/schematics/
```

## Index

| # | Shows | Filename | Folder |
|---|---|---|---|
| 1 | Reverse polarity protection | `diodes-leds-reverse-polarity-protection-01.png` | diodes-leds |
| 2 | Flyback diode across a relay coil | `diodes-leds-flyback-protection-01.png` | diodes-leds |
| 3 | Loudspeaker symbol | `schematics-loudspeaker-symbol-01.png` | schematics |
| 4 | Microphone symbol | `schematics-microphone-symbol-01.png` | schematics |
| 5 | Fuse symbol, IEC and ANSI | `schematics-fuse-symbol-01.png` | schematics |
| 6 | Plug and jack symbols | `schematics-connector-jack-symbol-01.png` | schematics |

---

## Image 1: Reverse polarity protection

Save as `diodes-leds-reverse-polarity-protection-01.png` in **diodes-leds**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration of an electronic schematic. Clean
uniform line weights, no gradients, no drop shadows, no 3D, no photorealism,
no watermark, no signature.

Draw a single closed rectangular circuit loop. On the left side of the loop
place a battery symbol drawn as two long plates and two short plates
alternating, with a plus sign above the top terminal and a minus sign below
the bottom terminal. Along the top wire place a diode symbol: a solid
triangle pointing to the right with a vertical bar touching its right-hand
tip. On the right side of the loop place a resistor drawn as a plain open
rectangle.

Reading direction is left to right: the current leaves the battery's positive
terminal, passes through the diode, reaches the resistor, and returns along
the bottom wire.

Place one arrowhead on the top wire between the diode and the resistor,
pointing right.

Label in dark gray #212121, spelled exactly: "DC Supply", "12 V", "D1",
"Load", "Current flow".

Use #212121 for all wires, component outlines, and text. Use #0D47A1 for the
single current arrow only.

Do not draw any logo, brand mark, model number, product photograph, or
connector. Do not include borders, frames, title bars, or caption text. Do
not add any text other than the five labels listed above.
```

**Check:** transparent background, five labels spelled exactly, diode bar on the RIGHT of the triangle tip.

---

## Image 2: Flyback diode across a relay coil

Save as `diodes-leds-flyback-protection-01.png` in **diodes-leds**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration of an electronic schematic. Clean
uniform line weights, no gradients, no drop shadows, no 3D, no photorealism,
no watermark, no signature.

Draw a rectangular circuit. On the left side place a battery symbol drawn as
two long plates and two short plates alternating, with a plus sign above the
top terminal and a minus sign below the bottom terminal.

From the battery's positive terminal run a wire right along the top to an
upper node. From that upper node run a wire straight down to a lower node,
and in that vertical run place a coil drawn as four tight semicircular loops
in a vertical line.

From the lower node continue down and then right to an open switch drawn as
two small circles with a straight line hinged upward from the left circle.
From the switch run a wire right, then up, then left along the bottom back to
the battery's negative terminal. The switch is below the coil, not above it.

Draw a second vertical branch to the right of the coil, connecting the same
upper node to the same lower node, and place a diode in it. The diode must be
drawn as a solid triangle pointing UP with a horizontal bar touching its
upper tip, so the bar sits at the top, nearest the upper node.

Label in dark gray #212121, spelled exactly: "DC Supply", "12 V", "Relay
Coil", "D1", "Switch".

Use #212121 for all wires, component outlines, and text. Use #B71C1C for a
single curved arrow that runs from the lower node, up through the diode
branch, and into the upper node, indicating the direction current takes when
the switch opens.

Reading direction is top to bottom.

Do not draw any logo, brand mark, model number, product photograph, or
connector. Do not include borders, frames, title bars, or caption text. Do
not add any text other than the five labels listed above.
```

**Check:** the diode bar must be on TOP with the triangle pointing up. That orientation is the whole reason this image is being redrawn. If the bar comes back at the bottom, regenerate.

---

## Image 3: Loudspeaker symbol

Save as `schematics-loudspeaker-symbol-01.png` in **schematics**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration of a single electronic schematic
symbol, drawn large and centered. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw the standard loudspeaker schematic symbol: a small upright rectangle
on the left, and attached to its right-hand edge a trapezoid whose short
parallel side touches the rectangle and whose long parallel side opens to
the right. The rectangle and trapezoid share an edge and form one connected
outline.

From the left-hand edge of the rectangle draw two short horizontal leads
going left, one from the upper portion and one from the lower portion.
Place a plus sign just above the upper lead.

Label in dark gray #212121, spelled exactly: "Loudspeaker", "LS1", "Voice
coil", "Cone", "+".

Place "Voice coil" with a thin leader line pointing at the rectangle. Place
"Cone" with a thin leader line pointing at the trapezoid. Place "LS1" just
above the whole symbol. Place "Loudspeaker" centered below the whole symbol.

Use #212121 for all lines, outlines, leader lines, and text.

Do not draw any logo, brand mark, model number, product photograph, cabinet,
grille, or driver photo. Do not include borders, frames, title bars, or
caption text. Do not add any text other than the five labels listed above.
```

**Check:** the trapezoid opens to the RIGHT, away from the leads.

---

## Image 4: Microphone symbol

Save as `schematics-microphone-symbol-01.png` in **schematics**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration of a single electronic schematic
symbol, drawn large and centered. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw the standard microphone schematic symbol: a circle, with a straight
vertical line drawn across the inside of its left-hand side, like a chord of
the circle. The vertical line must sit inside the circle, not outside it.

From the right-hand side of the circle draw two short horizontal leads going
right, one from the upper right and one from the lower right.

Label in dark gray #212121, spelled exactly: "Microphone", "MIC1",
"Diaphragm".

Place "Diaphragm" with a thin leader line pointing at the vertical line
inside the circle. Place "MIC1" just above the circle. Place "Microphone"
centered below the circle.

Use #212121 for all lines, outlines, leader lines, and text.

Do not draw any logo, brand mark, model number, product photograph,
microphone body, grille ball, shock mount, or stand. Do not include borders,
frames, title bars, or caption text. Do not add any text other than the
three labels listed above.
```

**Check:** the vertical bar must be INSIDE the circle, and the circle must not turn into a picture of a microphone.

---

## Image 5: Fuse symbol, both standards

Save as `schematics-fuse-symbol-01.png` in **schematics**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration of two electronic schematic symbols
side by side, each drawn large. Clean uniform line weights, no gradients, no
drop shadows, no 3D, no photorealism, no watermark, no signature.

On the left half of the image, draw the IEC fuse symbol: a horizontal
rectangle with a single straight horizontal line running through the middle
of it and continuing out both ends as leads, so the line enters the left
side of the rectangle and exits the right side.

On the right half of the image, draw the ANSI fuse symbol: a short
horizontal lead on the left, then a smooth S-shaped curve, then a short
horizontal lead on the right. The S-curve replaces the middle of the wire.
Do not draw a rectangle around it.

Label in dark gray #212121, spelled exactly: "IEC", "ANSI", "F1", "Fuse".

Place "IEC" centered above the left symbol and "ANSI" centered above the
right symbol. Place "F1" just below the left symbol. Place "Fuse" centered
along the bottom of the image, between and below both symbols.

Use #212121 for all lines, outlines, and text.

Do not draw any logo, brand mark, model number, product photograph, glass
cartridge fuse, fuse holder, or panel. Do not include borders, frames, title
bars, or caption text. Do not add any text other than the four labels listed
above.
```

**Check:** the IEC line passes all the way THROUGH the rectangle and out both sides.

---

## Image 6: Plug and jack symbols

Save as `schematics-connector-jack-symbol-01.png` in **schematics**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration of electronic schematic symbols.
Clean uniform line weights, no gradients, no drop shadows, no 3D, no
photorealism, no watermark, no signature.

Draw two rows, each showing a plug symbol and a socket symbol.

The plug symbol is a small solid triangle pointing to the right, with a
short horizontal lead attached to its left-hand side.

The socket symbol is a curved bracket shaped like a shallow letter C opening
to the left, with a short horizontal lead attached to the middle of its
right-hand side.

In the upper row, draw the plug on the left and the socket on the right with
a visible gap between the triangle's tip and the opening of the bracket, so
they are clearly separated.

In the lower row, draw the same plug and socket with the triangle's tip
nested inside the opening of the bracket, so they are clearly mated.

Label in dark gray #212121, spelled exactly: "Plug (P1)", "Jack (J1)",
"Unmated", "Mated".

Place "Plug (P1)" below the plug in the upper row and "Jack (J1)" below the
socket in the upper row. Place "Unmated" at the left edge of the upper row
and "Mated" at the left edge of the lower row.

Use #212121 for all lines, outlines, and text.

Do not draw any logo, brand mark, model number, product photograph, XLR
shell, TRS barrel, pin numbers, or cable. Do not include borders, frames,
title bars, or caption text. Do not add any text other than the four labels
listed above.
```

**Check:** the triangle must be SOLID and point right, into the bracket's opening.
