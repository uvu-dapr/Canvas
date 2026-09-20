# DAPR 2255 Image Brief - v69, every page that still has no image
Generated 2026-09-20. Run each prompt separately in ChatGPT. Save each result
with the exact filename shown, into the exact folder shown. Do not rename.

Thirty-two images, all generated. The twenty images that are sourced rather than
generated are not in this file; they are on the capture sheets listed at the end,
because Standards 20.1 rule 3 keeps real hardware and real software out of a
generator. This brief supersedes `ChatGPT Image Creation - DAPR 2255 v67 Eleven
Images.md`: every prompt in that file is reissued here in the locked 20.5 form.

Three of these replace a file already in the repo that is wrong. Each replacement
lands under a new conforming filename and the old file is then dead:

| New file | Replaces | Why |
|---|---|---|
| `multimeters-jack-selection-01.png` | `multimeters-jack-selection.png` | Two labels print on top of each other |
| `resistors-color-digit-chart-01.png` | `resistors-color-digit-chart.png` | Prints "colour" and "Grey" |
| `diodes-leds-led-circuit-01.png` | `diodes-leds-led-circuit.jpg` | The two emission arrows are detached from the diode body |

One folder does not exist yet and is created by the first save into it:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current
```

**Two rules every prompt below obeys.** Never bake a pin function, a value, or a
table into the pixels where a table on the page would do; three images in this
course have now been caught with a wrong fact painted on. And US spelling
everywhere: gray and color, never grey or colour.

---

## Image 01 - Jack selection

| Field | Value |
|---|---|
| Filename | `multimeters-jack-selection-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/multimeters/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/multimeters/multimeters-jack-selection-01.png` |
| Used on | Canvas page `Multimeters: Measuring DC Voltage` |
| Alt text | `Three multimeter input jacks with the current jack and the volts jack called out separately` |
| Caption | `Figure 1. The black lead stays in COM. Which red jack you choose decides what the meter can measure.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a light gray rounded rectangle panel filling the middle of the frame. Inside it,
centered and evenly spaced left to right, draw three solid #212121 filled circles of equal
size representing multimeter input jacks.

Under each circle, in bold #212121, print exactly: "A mA" under the left circle, "COM"
under the middle circle, "V ohm" under the right circle.

Above the LEFT circle, print in #993300: "Current only". Draw a short #993300 arrow from
that text down to the left circle.

Above the RIGHT circle, print in #993300: "Volts, ohms, continuity, diode test". Draw a
short #993300 arrow from that text down to the right circle.

Above the MIDDLE circle, print in #212121 on its own line, clear of the other two labels:
"Black lead lives here and never moves". Position this text ABOVE the two #993300 labels so
that no two pieces of text touch or overlap at any point. Leave at least 40 pixels of clear
space between every label.

Across the bottom of the frame draw a solid #993300 bar with white bold text reading
exactly: "LEADS LEFT IN THE CURRENT JACK ACROSS A VOLTAGE SOURCE IS A SHORT CIRCUIT".

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right across the three jacks.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 7 labels listed above.
```

---

## Image 02 - Color digit chart

| Field | Value |
|---|---|
| Filename | `resistors-color-digit-chart-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/resistors/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-color-digit-chart-01.png` |
| Used on | Canvas page `Resistors: Reading Resistor Color Codes` |
| Alt text | `Ten resistor band colors in order with the digit each one stands for and its multiplier` |
| Caption | `Figure 1. The first two bands are digits, the third is the multiplier, and gold or silver is tolerance only.` |

> **32 labels, over the 20.5 budget of about twelve.** This one is a chart and the
> text is the content, so it cannot be trimmed. Expect to run it more than once.
> Check every word against the table on the page before saving, and if a single
> label comes back wrong, regenerate with that word quoted again rather than
> patching it in an editor.

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw ten filled rectangles in a single evenly spaced row across the frame, each with a thin
light gray outline. In order left to right the fill colors are: black, brown, red, orange,
yellow, green, blue, violet, gray, white.

Beneath each swatch print its name in #212121, spelled exactly: Black, Brown, Red, Orange,
Yellow, Green, Blue, Violet, Gray, White. Use US spelling for every one of these names.

Beneath each name print its digit in bold #1B5E20: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

Beneath the digits print the multiplier in medium gray under the first eight swatches only:
1, 10, 100, 1k, 10k, 100k, 1M, 10M. Leave the multiplier row blank under gray and white.

At the far left of the digit row print the small gray word "digit" and at the far left of the
multiplier row print the small gray word "multiplier". Place both labels in clear margin space
to the LEFT of the first swatch so that neither one overlaps any swatch, digit or multiplier.

Below everything, centered, draw two small filled rectangles side by side, the first metallic
gold and the second metallic silver, with #212121 text to the right of each reading exactly
"Gold plus or minus 5 percent" and "Silver plus or minus 10 percent".

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right, black through white.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 32 labels listed above.
```

---

## Image 03 - LED circuit

| Field | Value |
|---|---|
| Filename | `diodes-leds-led-circuit-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/diodes-leds/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-led-circuit-01.png` |
| Used on | Canvas page `Diodes & LEDs: Light-Emitting Diodes` |
| Alt text | `A series LED circuit with a battery, a current-limiting resistor, and light leaving the LED body` |
| Caption | `Figure 2. Both emission arrows spring from the triangle. The resistor sets the current; the LED does not limit itself.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw one closed rectangular circuit loop. On the left side a battery symbol as alternating
long and short plates, plus sign beside the top plate, minus beside the bottom, labeled "9 V".
Along the top wire, left to right: a short arrow pointing right labeled "15 mA", then a
resistor drawn as a zigzag labeled "R = 470 ohm", then an LED.

Draw the LED as a triangle pointing RIGHT with a vertical bar touching its right tip. Label
the wire entering the triangle "A" and the wire leaving the bar "K". Above the device print
"LED".

The two light emission arrows are the part to get right. Draw them as a matched pair of short
parallel arrows in #993300, both starting from just outside the upper edge of the TRIANGLE
body, both angled up and to the right at about 45 degrees, both pointing away from the diode.
They must be clearly attached to the triangle, the same length as each other, and evenly
spaced. Neither arrow may start in empty space and neither may touch the "K" label.

Draw every wire, the battery, the resistor and the diode outline in #212121.

Leave at least 30 pixels of clear space between every label and every line.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right around the loop.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 8 labels listed above.
```

---

## Image 04 - Reservoir analogy

| Field | Value |
|---|---|
| Filename | `voltage-current-reservoir-analogy-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-reservoir-analogy-01.png` |
| Used on | Canvas page `Voltage & Current: Read About Basic Current and Voltage and Resistance` |
| Alt text | `A water tank feeding a pipe with a narrow section, labeled as voltage, current, and resistance` |
| Caption | `Figure 1. Height pushes, flow rate is current, and the narrow section is resistance.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

On the left draw a tall open-topped tank on legs, filled to about three quarters with a flat
#0D47A1 block representing water. From the bottom of the tank draw a horizontal pipe running
to the right, drawn as two parallel #212121 lines. Partway along the pipe, narrow the gap
between the two lines to about one third for a short section, then widen it again. At the far
right end of the pipe draw a simple open valve and a few short #0D47A1 lines leaving it to
suggest flow.

Draw a vertical double-headed #1B5E20 arrow at the left edge spanning from the water surface
down to the level of the pipe. Label it in bold #1B5E20: "Voltage, the height that does the
pushing".

Draw a horizontal #993300 arrow inside the wide part of the pipe pointing right. Label it in
bold #993300: "Current, the rate of flow".

Draw a leader line from the narrowed section of pipe to a label in bold #212121: "Resistance,
the narrow section".

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right, tank to outlet.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 3 labels listed above.
```

---

## Image 05 - Conventional vs electron flow

| Field | Value |
|---|---|
| Filename | `voltage-current-conventional-vs-electron-flow-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-conventional-vs-electron-flow-01.png` |
| Used on | Canvas page `Voltage & Current: Read About Basic Current and Voltage and Resistance` |
| Alt text | `One circuit loop with conventional current drawn one way and electron drift drawn the other` |
| Caption | `Figure 2. Both describe the same circuit. Every schematic and formula in this course uses conventional current.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a single closed rectangular circuit loop in #212121. On the left side place a battery
symbol drawn as two long plates and two short plates alternating, with a plus sign beside the
top terminal and a minus sign beside the bottom terminal. On the right side place a resistor
drawn as a plain open rectangle.

On the TOP wire draw a solid #993300 arrow pointing right, from the battery toward the
resistor. Label it in bold #993300: "Conventional current, plus to minus".

Directly below the top wire, inside the loop, draw a dashed #212121 arrow pointing left. Label
it in #212121: "Electron drift, the other way".

Beneath the whole circuit print in bold #1B5E20, on one line: "Both describe the same circuit."

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right along the top wire.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 3 labels listed above.
```

---

## Image 06 - Complete path

| Field | Value |
|---|---|
| Filename | `voltage-current-complete-path-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/voltage-current-complete-path-01.png` |
| Used on | Canvas page `Voltage & Current: Read About Basic Current and Voltage and Resistance` |
| Alt text | `Two identical circuit loops side by side, one closed and carrying current, one broken and dark` |
| Caption | `Figure 3. One break anywhere in a series loop stops the current everywhere in it.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw two rectangular circuit loops side by side, left and right, identical in size, both in
#212121.

LEFT loop: closed and unbroken. Battery symbol on the left side drawn as alternating long and
short plates, a lamp symbol on the right side drawn as a circle with an X through it. Draw
three small #993300 arrows spaced around the loop, all pointing the same way around it. Under
this loop print in bold #1B5E20: "Closed loop, current flows".

RIGHT loop: identical, except the TOP wire has a clear gap in it about one eighth of the loop
width, with the two cut ends drawn as small vertical stubs. No arrows anywhere on this loop.
The lamp circle is drawn with a thin light gray outline instead of #212121. Under this loop
print in bold #993300: "One break anywhere, current stops everywhere".

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left loop, then right loop.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 2 labels listed above.
```

---

## Image 07 - DIN connector face

| Field | Value |
|---|---|
| Filename | `midi-din-connector-face-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-din-connector-face-01.png` |
| Used on | Canvas page `MIDI: Device Roles Interfaces and Signal Flow` |
| Alt text | `The face of a 5-pin DIN jack with the keyway up and the five pins numbered along the arc` |
| Caption | `Figure 1. Looking into the jack, the arc reads 1, 4, 2, 5, 3. What each pin does is in the table below.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw one large circle centered in the frame in #212121, representing the face of a 5-pin DIN
connector viewed head on. Inside the top of the circle draw a wide shallow notch, a rectangular
keyway opening upward, so the orientation is unmistakable.

Inside the circle draw five small solid #212121 filled circles arranged on a single arc that
opens downward, all below the keyway, evenly spaced.

Number the pins with #212121 numerals placed just outside each pin. Read the arc strictly left
to right and number them in exactly this order and no other: the leftmost pin is "1", the next
one to its right is "4", the pin at the center is "2", the next one to its right is "5", and
the rightmost pin is "3". The center pin must carry the numeral 2. Do not reorder these.

Print nothing else inside the circle. Do not label any pin with a function, a signal name, a
voltage or a color.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right across the arc.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 6 labels listed above.
```

---

## Image 08 - TRS type a vs type B

| Field | Value |
|---|---|
| Filename | `midi-trs-type-a-vs-type-b-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-trs-type-a-vs-type-b-01.png` |
| Used on | Canvas page `MIDI: Device Roles Interfaces and Signal Flow` |
| Alt text | `Two identical TRS plugs in profile with tip and ring marked, labeled Type A and Type B` |
| Caption | `Figure 2. The jack is the same on both. The wiring behind it is not, and they do not interoperate.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw two identical 3.5 mm TRS plugs in side profile in #212121, one above the other, each
drawn as a long horizontal shaft with two thin insulating rings dividing it into three
conductor sections: a rounded tip at the right end, a middle band, and a long sleeve running
to the left into a barrel.

On the UPPER plug, draw thin #212121 leader lines from the tip section and the middle band out
to labels reading exactly "Tip" and "Ring". To the left of the upper plug print in bold
#1B5E20: "Type A".

On the LOWER plug, draw the same two leader lines and the same two labels, "Tip" and "Ring".
To the left of the lower plug print in bold #1B5E20: "Type B".

Between the two plugs, centered, print in bold #993300 on one line: "Same jack, different
wiring".

Do not label any conductor with a pin number, a signal name or a manufacturer.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Top plug, then bottom plug.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 6 labels listed above.
```

---

## Image 09 - Byte structure

| Field | Value |
|---|---|
| Filename | `midi-byte-structure-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-byte-structure-01.png` |
| Used on | Canvas page `MIDI: Message Architecture and Data Structure` |
| Alt text | `Two eight-cell byte rows, one with a leading 1 marked status and one with a leading 0 marked data` |
| Caption | `Figure 1. The most significant bit is the whole trick: 1 starts a message, 0 is a value inside it.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw two horizontal rows, one above the other, each made of eight equal square cells outlined
in #212121, representing the eight bits of a byte. Leave generous vertical space between the
two rows.

UPPER ROW: fill the leftmost cell solid #1B5E20 and print a white "1" in it. Leave the other
seven cells empty with thin outlines. Above the row print in bold #1B5E20: "Status byte". To
the right of the row print in #212121: "Most significant bit is 1".

Beneath the upper row, bracket the leftmost four cells with a #1B5E20 brace labeled "message
type", and bracket the rightmost four cells with a #1B5E20 brace labeled "channel".

LOWER ROW: fill the leftmost cell solid #993300 and print a white "0" in it. Leave the other
seven cells empty with thin outlines. Above the row print in bold #993300: "Data byte". To the
right of the row print in #212121: "Most significant bit is 0".

Beneath the lower row print in #212121, centered: "Seven bits of value".

Do not print any hexadecimal values, decimal ranges or example messages.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Top row, then bottom row.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 8 labels listed above.
```

---

## Image 10 - Thru chain vs thru box

| Field | Value |
|---|---|
| Filename | `midi-thru-chain-vs-thru-box-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-thru-chain-vs-thru-box-01.png` |
| Used on | Canvas page `MIDI: Routing Channelization and Thru Management` |
| Alt text | `A four-device daisy chain above a Thru box feeding four devices in parallel` |
| Caption | `Figure 1. A chain adds a little delay at every hop. A Thru box hands the same message to everything at once.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Split the frame into an upper half and a lower half. Draw everything in #212121 unless a
color is named.

UPPER HALF: draw one rounded rectangle at the far left labeled "Sequencer", then four more
rounded rectangles in a horizontal row to its right, each labeled "Device". Connect them left
to right in a single chain with straight arrows, each arrow leaving one box and entering the
next. Above each arrow after the first, print a small #993300 label reading "plus delay". At
the right end print in bold #993300: "Delay adds up". Label this half in bold #212121 at the
far left: "Daisy chain".

LOWER HALF: draw the same "Sequencer" rounded rectangle at the far left. To its right draw a
single taller rounded rectangle labeled "Thru box". From the right edge of the Thru box draw
four separate arrows fanning out to four "Device" rounded rectangles stacked vertically. Print
in bold #1B5E20 at the right: "All at the same time". Label this half in bold #212121 at the
far left: "Thru box".

Do not print any millisecond values.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right in both halves.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 9 labels listed above.
```

---

## Image 11 - Local control double trigger

| Field | Value |
|---|---|
| Filename | `midi-local-control-double-trigger-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-local-control-double-trigger-01.png` |
| Used on | Canvas page `MIDI: Device Roles Interfaces and Signal Flow` |
| Alt text | `A keyboard triggering its own sound engine directly and again through a DAW echoing MIDI back` |
| Caption | `Figure 3. Two paths reach the same sound engine from one key press. Turning Local Control off removes the first.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

On the left draw a wide rounded rectangle in #212121 labeled "Keyboard". Inside it, at the
bottom, draw a smaller nested rounded rectangle labeled "Internal sound engine".

On the right draw a rounded rectangle labeled "DAW". Inside it print in smaller #212121 text:
"MIDI Thru on".

Draw a short #993300 arrow from the top of the Keyboard box curving down into the nested
Internal sound engine box, staying entirely inside the Keyboard. Label it in #993300: "Path 1,
Local Control on".

Draw a second #993300 arrow leaving the right edge of the Keyboard, entering the DAW, turning
around inside it, leaving the DAW, and entering the Internal sound engine box from the right.
Label it in #993300: "Path 2, echoed back by the DAW".

Beneath both, centered, print in bold #1B5E20: "Fix: set Local Control off".

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right, keyboard out to DAW and back.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 7 labels listed above.
```

---

## Image 12 - Clock vs MTC

| Field | Value |
|---|---|
| Filename | `midi-clock-vs-mtc-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-clock-vs-mtc-01.png` |
| Used on | Canvas page `MIDI: Timing Clocking and Synchronization` |
| Alt text | `A metronome tick track beside a timeline with a playhead, contrasting tempo with position` |
| Caption | `Figure 1. Tempo and position are two different jobs, and many rigs run both at once.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Split the frame into a left half and a right half with a thin vertical #212121 divider.

LEFT HALF: print in bold #1B5E20 at the top: "MIDI Clock". Beneath, draw a horizontal #212121
line with a row of short evenly spaced vertical tick marks standing on it, like a metronome
track. Under the line print in #212121: "Tells a device how fast". Under that print in #993300:
"Does not say where you are".

RIGHT HALF: print in bold #1B5E20 at the top: "MIDI Time Code". Beneath, draw a horizontal
#212121 timeline bar with a small triangular playhead marker sitting partway along it, and a
few evenly spaced division marks on the bar. Under the bar print in #212121: "Tells a device
where you are". Under that print in #993300: "Does not say how fast".

Do not print any BPM values, timecode values, frame rates or pulse counts.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left half, then right half.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 7 labels listed above.
```

---

## Image 13 - What MIDI carries

| Field | Value |
|---|---|
| Filename | `midi-what-midi-carries-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-what-midi-carries-01.png` |
| Used on | Canvas page `MIDI: What MIDI Is and Why It Exists` |
| Alt text | `Four things MIDI transmits on one side and a struck-through waveform for audio on the other` |
| Caption | `Figure 1. A MIDI file is a set of instructions. The sound comes from whatever plays them.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Split the frame into a left half and a right half, divided by a thin vertical #212121 line.

LEFT: print in bold #1B5E20 at the top: "MIDI carries". Under it draw four small labeled rows,
each a simple #212121 icon beside a word: a single piano key with a downward arrow labeled
"which note", a hand pressing with a small speed arrow labeled "how hard", a rotary knob
labeled "controller position", and a plain numbered box labeled "which patch".

RIGHT: print in bold #993300 at the top: "MIDI does not carry". Under it draw one large
#212121 waveform inside a circle, with a diagonal #993300 line struck through the whole
circle, labeled "audio".

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left half, then right half.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 7 labels listed above.
```

---

## Image 14 - Note on note off timeline

| Field | Value |
|---|---|
| Filename | `midi-note-on-note-off-timeline-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-note-on-note-off-timeline-01.png` |
| Used on | Canvas page `MIDI: Channel Voice Messages and Musical Control` |
| Alt text | `A held note bounded by Note On and Note Off beside a note whose Note Off never arrived` |
| Caption | `Figure 1. A note is two messages. Lose the second one and the note never stops.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a horizontal #212121 time axis with an arrow at its right end labeled "time". Above it
draw one long rounded rectangle representing a held note. At the left end of that rectangle
draw a vertical tick going down to the axis, labeled in bold #1B5E20 "Note On". At the right
end draw a matching tick labeled in bold #1B5E20 "Note Off". Inside the rectangle print "the
note sounds".

To the right of that, draw a second rectangle with a Note On tick at its left and NO tick at
its right, its right edge drawn as a ragged torn edge continuing off the frame. Label it in
bold #993300 "Note Off never arrived", and under it print "stuck note".

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right along the time axis.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 6 labels listed above.
```

---

## Image 15 - Same file two synths

| Field | Value |
|---|---|
| Filename | `midi-same-file-two-synths-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-same-file-two-synths-01.png` |
| Used on | Canvas page `MIDI: What MIDI Is Not and Common Misunderstandings` |
| Alt text | `One MIDI file feeding two different synths that produce two different waveforms` |
| Caption | `Figure 1. The same file, the same notes, two completely different sounds.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw one #212121 document icon at the top center labeled "one MIDI file". From it draw two
#212121 arrows fanning down, one to the lower left and one to the lower right.

At the end of the left arrow draw a rounded rectangle labeled "Synth A", and beneath it a
small waveform drawn as a smooth rounded shape.

At the end of the right arrow draw a rounded rectangle labeled "Synth B", and beneath it a
small waveform drawn as a jagged square shape.

Between the two waveforms print in bold #993300: "same notes, different sound".

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Top to bottom, file down to the two synths.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 5 labels listed above.
```

---

## Image 16 - 1.0 vs 2.0 resolution

| Field | Value |
|---|---|
| Filename | `midi-1-vs-2-resolution-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-1-vs-2-resolution-01.png` |
| Used on | Canvas page `MIDI: MIDI 2 0 What Changed and Why It Matters` |
| Alt text | `A coarse stepped bar labeled MIDI 1.0 above a smooth bar labeled MIDI 2.0` |
| Caption | `Figure 1. Both devices have to agree to speak 2.0. If either one cannot, the pair falls back to 1.0.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw two horizontal bars of equal length in #212121, one above the other, with generous space
between them.

UPPER: divide it into a small number of wide visible steps, like a coarse staircase drawn along
its top edge. Label it in bold #212121 "MIDI 1.0" and to its right print "coarse steps you can
hear".

LOWER: draw the same bar with a smooth unbroken line along its top edge. Label it in bold
#1B5E20 "MIDI 2.0" and to its right print "smooth".

Beneath both print in bold #1B5E20: "Both devices must agree".

Do not print any bit counts or step counts.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Top bar, then bottom bar.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 5 labels listed above.
```

---

## Image 17 - OSC address anatomy

| Field | Value |
|---|---|
| Filename | `midi-osc-address-anatomy-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-osc-address-anatomy-01.png` |
| Used on | Canvas page `MIDI: Open Sound Control Compared to MIDI` |
| Alt text | `One OSC message split into its address, type tag, and value by three braces` |
| Caption | `Figure 1. The address must match exactly, capital letters included.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Print one OSC message across the middle of the frame in a large monospaced #212121 font, with
clear gaps between its three parts, exactly:

/mixer/ch/4/fader     ,f     0.75

Under each of the three parts draw a #1B5E20 brace, and under each brace a #212121 label:
under the first, "address, where it goes";
under the second, "type tag, what kind of value";
under the third, "the value".

Do not add any further text.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right across the message.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 5 labels listed above.
```

---

## Image 18 - MSC device ID

| Field | Value |
|---|---|
| Filename | `midi-msc-device-id-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-msc-device-id-01.png` |
| Used on | Canvas page `MIDI: MIDI Show Control Protocol` |
| Alt text | `A console addressing audio, lighting, and video, each with an empty device ID tag` |
| Caption | `Figure 1. A broadcast ID reaches all three at once. So does a shared ID set by accident.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw one rounded rectangle at the left in #212121 labeled "Console", with an arrow leaving it
to the right that splits into three arrows.

Each of the three arrows ends at its own rounded rectangle, stacked vertically and labeled
"Audio playback", "Lighting" and "Video".

Beside each of the three boxes print a small #212121 tag reading "Device ID" with an empty box
after it, drawn as an outlined rectangle with nothing inside.

Beneath everything print in bold #993300: "A shared ID does the same thing".

Do not print any actual ID numbers or hexadecimal values.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right, console out to the three departments.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 8 labels listed above.
```

---

## Image 19 - DMX universe addressing

| Field | Value |
|---|---|
| Filename | `midi-dmx-universe-addressing-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-dmx-universe-addressing-01.png` |
| Used on | Canvas page `MIDI: DMX512 Protocol and Signal Structure` |
| Alt text | `A row of DMX channels with three fixture ranges bracketed and a gap of unused channels` |
| Caption | `Figure 1. A universe is a row of channels. Two fixtures whose ranges overlap both answer to the same channel.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a long horizontal bar across the frame in #212121, divided into many equal narrow cells,
like a ruler, representing one DMX universe. Do not number the cells.

Above the bar, bracket three separate runs of adjacent cells with #1B5E20 braces. Label the
first brace "Dimmer rack", the second "Wash fixture 1", the third "Wash fixture 2".

Leave a visible gap of unbracketed cells between the second and third brace, and mark that gap
with a small #993300 label reading "unused".

Beneath the bar print in bold #993300: "Overlapping ranges collide".

Do not print any channel numbers or addresses.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right along the universe.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 5 labels listed above.
```

---

## Image 20 - CC to DMX scaling

| Field | Value |
|---|---|
| Filename | `midi-cc-to-dmx-scaling-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-cc-to-dmx-scaling-01.png` |
| Used on | Canvas page `MIDI: MIDI to DMX Integration and Conversion` |
| Alt text | `A MIDI CC range bar above a DMX range bar with dashed lines mapping the ends and the middle` |
| Caption | `Figure 1. Two ranges, different sizes. The bridge has to scale, not just pass the number through.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw two horizontal bars in #212121, one above the other, left ends aligned and right ends
aligned.

UPPER bar labeled at its left "MIDI CC" in bold #1B5E20. Mark only its two ends with small
ticks and print "min" under the left tick and "max" under the right.

LOWER bar labeled at its left "DMX" in bold #1B5E20, marked the same way with "min" and "max".

Between the bars draw three vertical dashed #212121 lines connecting matching positions: at the
two ends and at the middle.

To the right of both, print in bold #993300: "The bridge has to scale".

Do not print any numeric ranges.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Top bar down to bottom bar.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 7 labels listed above.
```

---

## Image 21 - Serial vs network transport

| Field | Value |
|---|---|
| Filename | `midi-serial-vs-network-transport-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-serial-vs-network-transport-01.png` |
| Used on | Canvas page `MIDI: Over USB and Network` |
| Alt text | `Three separate serial MIDI cables above one network cable carrying five device connections` |
| Caption | `Figure 1. Serial MIDI gives one connection per cable. A network carries many streams down one.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Split the frame into an upper half and a lower half. Draw everything in #212121 unless a color
is named.

UPPER, labeled in bold #212121 at the far left "Serial MIDI": draw three pairs of boxes, each
pair joined by its own separate line, so three cables carry three connections. Print to the
right in #212121: "one connection per cable".

LOWER, labeled in bold #1B5E20 at the far left "Network MIDI": draw one horizontal line across
the frame, with five boxes hanging off it by short stubs. Print to the right in #1B5E20: "many
streams, one cable".

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Top half, then bottom half.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 4 labels listed above.
```

---

## Image 22 - RTP session handshake

| Field | Value |
|---|---|
| Filename | `midi-rtp-session-handshake-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-rtp-session-handshake-01.png` |
| Used on | Canvas page `MIDI: RTP MIDI and AppleMIDI` |
| Alt text | `An initiator and a responder exchanging invitations on two ports before MIDI flows` |
| Caption | `Figure 1. Two invitations, two acceptances, then clock sync. MIDI only flows after all four.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw two vertical #212121 lines, one on the left and one on the right, each topped with a
rounded rectangle, the left labeled "Initiator" and the right labeled "Responder".

Between them draw four horizontal arrows stacked top to bottom, alternating direction, each
labeled in #212121 beside the arrow:
first, pointing right, "invite on the control port";
second, pointing left, "accepted";
third, pointing right, "invite on the data port";
fourth, pointing left, "accepted".

Below those draw a fifth double-headed arrow labeled in bold #1B5E20: "clock sync, then MIDI
flows".

Do not print any port numbers.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Top to bottom down the two timelines.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 7 labels listed above.
```

---

## Image 23 - VLAN segmentation

| Field | Value |
|---|---|
| Filename | `midi-vlan-segmentation-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-vlan-segmentation-01.png` |
| Used on | Canvas page `MIDI: Network Architecture and Topology` |
| Alt text | `One switch split into a control VLAN and a lighting VLAN with three devices in each` |
| Caption | `Figure 1. Same hardware, separated traffic. A VLAN is a boundary drawn in configuration, not in cable.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a large rounded rectangle in #212121 representing one physical switch, labeled "One
switch".

Inside it draw two clearly separated rounded regions with a gap between them, the left tinted
very light #1B5E20 and the right tinted very light #993300.

In the left region draw three small boxes labeled "Console", "Media server" and "MIDI". In the
right region draw three small boxes labeled "Lighting", "Lighting" and "Lighting".

Label the left region "Control VLAN" and the right region "Lighting VLAN".

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left region, then right region.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 9 labels listed above.
```

---

## Image 24 - Jitter buffer tradeoff

| Field | Value |
|---|---|
| Filename | `midi-jitter-buffer-tradeoff-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-jitter-buffer-tradeoff-01.png` |
| Used on | Canvas page `MIDI: Synchronization Over IP` |
| Alt text | `Timing instability falling and added delay rising as buffer depth increases, crossing in the middle` |
| Caption | `Figure 1. A bigger buffer buys stability and costs delay. The useful setting is near the crossing.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a horizontal #212121 axis with an arrow at its right end labeled "buffer depth".

Draw two curves across it that cross near the middle.

The first curve starts high on the left and falls to the right, drawn in #993300, labeled
"timing instability".

The second starts low on the left and rises to the right, drawn in #1B5E20, labeled "added
delay".

At the crossing point draw a small vertical dashed #212121 line down to the axis and label it
in bold #212121 "the trade".

Do not print any millisecond values.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right with increasing buffer depth.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 4 labels listed above.
```

---

## Image 25 - Show control hub

| Field | Value |
|---|---|
| Filename | `midi-show-control-hub-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-show-control-hub-01.png` |
| Used on | Canvas page `MIDI: Network Based Show Control Systems` |
| Alt text | `A show control hub reaching audio, lighting, video, and automation over four different protocols` |
| Caption | `Figure 1. Four legs, four protocols. Test each one on its own before you test them together.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw one rounded rectangle at the center in #212121 labeled "Show control hub". From it draw
four arrows out to four rounded rectangles arranged around it, labeled "Audio", "Lighting",
"Video" and "Stage automation".

Draw the arrow to Audio as a solid line labeled "MIDI", the arrow to Lighting as a dashed line
labeled "DMX over Ethernet", the arrow to Video as a solid line labeled "OSC", and the arrow to
Stage automation as a dotted line labeled "vendor protocol".

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Center outward to the four departments.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 9 labels listed above.
```

---

## Image 26 - Cross protocol isolation

| Field | Value |
|---|---|
| Filename | `midi-cross-protocol-isolation-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-cross-protocol-isolation-01.png` |
| Used on | Canvas page `MIDI: Extended Protocols Troubleshooting Checklist` |
| Alt text | `Six troubleshooting layers stacked from physical up to architecture, each with what to check` |
| Caption | `Figure 1. Work down the stack, not around it. Most cross-protocol faults are settled in the first two layers.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a vertical stack of six rounded rectangles in #212121 connected top to bottom by downward
arrows, each labeled in bold #1B5E20, in this order: "Physical", "Transport", "Protocol mode",
"Addressing", "Message structure", "Architecture".

To the right of each box print one short line in #212121:
beside Physical, "cable, termination, power";
beside Transport, "DIN, USB, UDP, RS-485";
beside Protocol mode, "which version, which namespace";
beside Addressing, "channel, device ID, IP, universe";
beside Message structure, "status bytes, type tags, scaling";
beside Architecture, "one clock master, no duplicate addresses".

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Top to bottom down the stack.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 12 labels listed above.
```

---

## Image 27 - GM channel 10

| Field | Value |
|---|---|
| Filename | `midi-gm-channel-10-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/midi-gm-channel-10-01.png` |
| Used on | Canvas page `MIDI: Timeline General MIDI and MMC` |
| Alt text | `Sixteen channel squares with the tenth filled, bracketed as percussion against fifteen melodic` |
| Caption | `Figure 1. General MIDI reserves one channel for percussion. Send a melodic part there and it comes back as drums.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw sixteen small squares in a single row, evenly spaced, each outlined in #212121.

Fill the tenth square solid #993300. Leave the other fifteen unfilled.

Under the row, draw a #1B5E20 brace under the fifteen unfilled squares as a group and label it
"melodic instruments". Draw a separate #993300 brace under the single filled square and label
it "percussion".

Beneath everything print in bold #993300: "Send a melodic part there and it comes back as
drums."

Do not print channel numbers on the squares.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right across the sixteen channels.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 3 labels listed above.
```

---

## Image 28 - AC vs DC at a glance

| Field | Value |
|---|---|
| Filename | `ac-dc-electricity-ac-vs-dc-at-a-glance-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/ac-dc-electricity/ac-dc-electricity-ac-vs-dc-at-a-glance-01.png` |
| Used on | Canvas page `AC & DC: Overview` |
| Alt text | `A sine wave beside a flat horizontal line, one labeled AC and the other DC` |
| Caption | `Figure 1. One reverses direction over and over; the other does not reverse at all.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Split the frame into a left half and a right half with generous space between them and no
divider line.

LEFT: draw one smooth sine wave of about two full cycles in #1B5E20, centered on a thin
horizontal #212121 zero line that runs the width of the half. Label it in bold #1B5E20 "AC".

RIGHT: draw one flat horizontal #993300 line sitting well above a thin horizontal #212121 zero
line of the same width. Label it in bold #993300 "DC".

Both zero lines must sit at the same height so the two halves read as one comparison.

No numbers, no axis ticks, no units anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right, AC then DC.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 2 labels listed above.
```

---

## Image 29 - In circuit parallel path

| Field | Value |
|---|---|
| Filename | `resistors-in-circuit-parallel-path-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/resistors/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/resistors/resistors-in-circuit-parallel-path-01.png` |
| Used on | Canvas page `Resistors: Measuring Resistance` |
| Alt text | `Two resistors on a board with a leader line showing the second path a meter reads through` |
| Caption | `Figure 1. In circuit, the meter reads every path between its probes, not just the part you meant.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a plain light gray rectangle representing a small circuit board. On it draw two resistors
side by side in #212121, each as a rectangle with a lead leaving each end, wired so that the two
resistors share both of their end nodes.

Draw two #212121 meter probes touching the two shared nodes, each drawn as a simple pointed
stylus with a lead running off the frame. Label them "probe" and "probe".

Trace the path through the FIRST resistor with a #1B5E20 line and label it "the part you meant
to measure".

Trace the path through the SECOND resistor with a #993300 line and label it "the other path the
meter also sees".

No numbers, no resistance values, no color bands anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left to right across the board.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 4 labels listed above.
```

---

## Image 30 - Doubling is 3 dB

| Field | Value |
|---|---|
| Filename | `power-doubling-is-3db-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/power/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/power/power-doubling-is-3db-01.png` |
| Used on | Canvas page `Power: Power in Decibels - dBW & dBm` |
| Alt text | `A bar and a second bar twice its height joined by an arrow marked plus 3 dB` |
| Caption | `Figure 1. Doubling the power is plus 3 dB, whatever the starting number happens to be.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw two solid vertical bars standing on a thin horizontal #212121 baseline, well separated.

The LEFT bar is drawn in #1B5E20. The RIGHT bar is drawn in #1B5E20 at exactly twice the height
of the left bar and the same width.

Label the left bar beneath it in #212121: "power". Label the right bar beneath it in #212121:
"twice the power".

Draw a curved #993300 arrow from the top of the left bar to the top of the right bar, and print
along it in bold #993300: "plus 3 dB".

Do not print any watt values, decibel values other than the one label, axis ticks or units.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left bar to right bar.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 3 labels listed above.
```

---

## Image 31 - Current path through body

| Field | Value |
|---|---|
| Filename | `wiring-safety-current-path-through-body-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/wiring-safety/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/wiring-safety/wiring-safety-current-path-through-body-01.png` |
| Used on | Canvas page `Wiring & Safety: Electric Shock and the Human Body` |
| Alt text | `A human outline with a hand-to-hand path across the chest and a hand-to-foot path marked` |
| Caption | `Figure 1. What decides the injury is the path, not only the current. Hand to hand crosses the heart.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw one simple human outline standing facing forward, arms out to the sides, drawn as a plain
#212121 line figure with no facial features and no clothing detail.

Draw one path in #993300 entering at the LEFT hand, running across the chest, and leaving at the
RIGHT hand. Label it in bold #993300: "hand to hand, across the chest".

Draw a second path in #212121 entering at the LEFT hand, running down the torso and the left leg,
and leaving at the LEFT foot. Label it in #212121: "hand to foot".

Mark the position of the heart with a small #B71C1C outline shape on the chest, on the first
path. Label it in #B71C1C: "heart".

Do not print any current values, voltage values, or resistance values.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Top to bottom through the body.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 4 labels listed above.
```

---

## Image 32 - Heatsink why fins work

| Field | Value |
|---|---|
| Filename | `power-heatsink-why-fins-work-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/power/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/power/power-heatsink-why-fins-work-01.png` |
| Used on | Canvas page `Power: Power, Heat, & Component Ratings` |
| Alt text | `A bare device with three heat arrows beside a finned heat sink with an arrow off every fin` |
| Caption | `Figure 1. Fins do not move heat faster. They give it more places to leave.` |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Split the frame into a left half and a right half.

LEFT: draw a plain solid #212121 rectangle standing on a base, no fins. Draw three short #993300
arrows leaving its top edge, pointing up and away. Label it in bold #212121 "bare device" and
beneath it print "little surface touching the air".

RIGHT: draw a rectangle of the same width with a row of tall thin vertical fins rising from its
top edge, at least eight fins, all in #212121. Draw a #993300 arrow leaving the tip of every
fin, pointing up and away, so the right side visibly has many more arrows than the left. Label
it in bold #1B5E20 "same device, finned heat sink" and beneath it print "far more surface
touching the air".

No numbers anywhere in the image.

Use #212121 for outlines and body text, #1B5E20 for the primary accent, #993300 for the
warning accent, #0D47A1 for measurement or secondary accents, and #B71C1C only if it is
named above. Use no other colors.

Reading direction: Left half, then right half.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add any
text other than the 4 labels listed above.
```

---

## The sourced images are not in this file

Twenty more images finish the course and none of them may be generated. They are on
four capture sheets in this same folder, one per topic folder, because each sheet's
preview slots resolve `../<topic>/` relative to where the sheet sits:

| Sheet | Images |
|---|---|
| `2026-09-20-dapr-2255-capture-sheet-midi.html` | 14 |
| `2026-09-20-dapr-2255-capture-sheet-diodes-leds.html` | 1 |
| `2026-09-20-dapr-2255-capture-sheet-power.html` | 4 |
| `2026-09-20-dapr-2255-capture-sheet-resistors.html` | 1 |

**Standards 20.6 step 1 was run before those sheets were written.** The general
manual library and the per-course `Instructor Stuff/Manuals/` folder were both
searched. No manual on disk supplies any of the twenty. The SSL Duality SE
Operator's Manual is the only one on disk with substantial MIDI content and its
MIDI pages are text and tables; its only screenshots are Pro Tools 7 and Logic Pro
8, both far too old to teach from. The general library's `Lighting/`,
`Networking & Sync/` and `Interfaces & Converters/` folders, which is where a DMX
fixture, a managed switch or a MIDI interface manual would sit, are empty. Step 2
finds nothing to download either, because every remaining item is Adam's own gear
or his own screen.
