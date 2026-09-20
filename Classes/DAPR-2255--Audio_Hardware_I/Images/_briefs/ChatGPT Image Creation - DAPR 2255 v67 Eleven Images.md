# DAPR 2255: Eleven Images to Generate (v67)

Written 2026-09-20 from the v67 build. Two of these replace images already in the repo
that are defective. Nine are new, filling the two modules that currently have no images
at all.

Copy one prompt block at a time. Save each result with the exact filename shown, into
the folder shown. All are transparent PNG at 1600 x 900 unless a block says otherwise.

**Two folders do not exist yet and need creating:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/voltage-current/
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/
```

The other two live in folders that already exist:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/multimeters/
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/resistors/
```

## Index

| # | Shows | Filename | Folder | Status |
|---|---|---|---|---|
| 1 | Multimeter jack selection | `multimeters-jack-selection.png` | multimeters | **Replaces a broken file** |
| 2 | Resistor color to digit chart | `resistors-color-digit-chart.png` | resistors | **Replaces a broken file** |
| 3 | Reservoir analogy | `voltage-current-reservoir-analogy-01.png` | voltage-current | New |
| 4 | Conventional current and electron flow | `voltage-current-conventional-vs-electron-flow-01.png` | voltage-current | New |
| 5 | A complete path is required | `voltage-current-complete-path-01.png` | voltage-current | New |
| 6 | 5-pin DIN connector face | `midi-din-connector-face-01.png` | midi | New |
| 7 | TRS MIDI, two standards | `midi-trs-type-a-vs-type-b-01.png` | midi | New |
| 8 | Status byte and data byte | `midi-byte-structure-01.png` | midi | New |
| 9 | Thru chain against a Thru box | `midi-thru-chain-vs-thru-box-01.png` | midi | New |
| 10 | The double trigger path | `midi-local-control-double-trigger-01.png` | midi | New |
| 11 | MIDI Clock against MTC | `midi-clock-vs-mtc-01.png` | midi | New |

## Two rules that apply to every block below

1. **Never bake a pin function, an impedance, a polarity or a numeric value into the
   picture where a table would do.** Images 6 and 7 are the ones at risk. Both are written
   to show the connector and number the pins only. The functions live in the page table
   beside them, where a correction costs an edit rather than a regeneration.
2. **US spelling everywhere.** Gray, color, not grey or colour. The chart being replaced
   as image 2 is being replaced for exactly this.

---

## Image 1: Multimeter jack selection

Save as `multimeters-jack-selection.png` in **multimeters**.

Why it is being replaced: the current file has two text labels printed on top of each
other and neither is readable. The content is right, the layout is not.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a light gray rounded rectangle panel filling the middle of the frame. Inside it,
centered and evenly spaced left to right, draw three solid black filled circles of
equal size representing multimeter input jacks.

Under each circle, in bold dark gray, print exactly: "A mA" under the left circle,
"COM" under the middle circle, "V ohm" under the right circle.

Above the LEFT circle, print in orange: "Current only". Draw a short orange arrow from
that text down to the left circle.

Above the RIGHT circle, print in orange: "Volts, ohms, continuity, diode test". Draw a
short orange arrow from that text down to the right circle.

Above the MIDDLE circle, print in dark gray on its own line, clear of the other two
labels: "Black lead lives here and never moves". Position this text ABOVE the orange
labels so that no two pieces of text touch or overlap at any point. Leave at least
40 pixels of clear space between every label.

Across the bottom of the frame draw a solid orange bar with white bold text reading
exactly: "LEADS LEFT IN THE CURRENT JACK ACROSS A VOLTAGE SOURCE IS A SHORT CIRCUIT".

Title at top left in bold dark green: "Which jack, and why it matters".
```

---

## Image 2: Resistor color to digit chart

Save as `resistors-color-digit-chart.png` in **resistors**.

Why it is being replaced: the current file prints "colour" in the title and "Grey" in
the swatch row. The course uses US spelling and the pages were changed from Grey to Gray
in v66, so the image now contradicts the text beside it.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style chart. Clean uniform line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Title at top left in bold dark green, spelled exactly: "Resistor color to digit chart".

Draw ten filled rectangles in a single evenly spaced row across the frame, each with a
thin light gray outline. In order left to right the fill colors are: black, brown, red,
orange, yellow, green, blue, violet, gray, white.

Beneath each swatch print its name in dark gray, spelled exactly: Black, Brown, Red,
Orange, Yellow, Green, Blue, Violet, Gray, White.

Beneath each name print its digit in bold dark green: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

Beneath the digits print the multiplier in medium gray under the first eight swatches
only: 1, 10, 100, 1k, 10k, 100k, 1M, 10M. Leave the multiplier row blank under gray and
white.

At the far left of the digit row print the small gray word "digit" and at the far left
of the multiplier row print the small gray word "multiplier". Place both labels in
clear margin space to the LEFT of the first swatch so that neither one overlaps any
swatch, digit or multiplier value.

Below everything, centered, print in bold dark green: "Tolerance only, not digits".
Under that draw two small filled rectangles side by side, the first metallic gold and
the second metallic silver, with dark gray text to the right of each reading exactly
"Gold plus or minus 5 percent" and "Silver plus or minus 10 percent".
```

---

## Image 3: Reservoir analogy

Save as `voltage-current-reservoir-analogy-01.png` in **voltage-current**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

On the left draw a tall open-topped tank on legs, filled to about three quarters with a
flat blue block representing water. From the bottom of the tank draw a horizontal pipe
running to the right, drawn as two parallel lines. Partway along the pipe, narrow the
gap between the two lines to about one third for a short section, then widen it again.
At the far right end of the pipe draw a simple open valve and a few short blue lines
leaving it to suggest flow.

Draw a vertical double-headed dark green arrow at the left edge spanning from the water
surface down to the level of the pipe. Label it in bold dark green: "Voltage, the height
that does the pushing".

Draw a horizontal orange arrow inside the wide part of the pipe pointing right. Label it
in bold orange: "Current, the rate of flow".

Draw a leader line from the narrowed section of pipe to a label in bold dark gray:
"Resistance, the narrow section".

Title at top left in bold dark green: "The reservoir analogy".

No numbers anywhere in the image.
```

---

## Image 4: Conventional current and electron flow

Save as `voltage-current-conventional-vs-electron-flow-01.png` in **voltage-current**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style schematic. Clean uniform line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Draw a single closed rectangular circuit loop. On the left side place a battery symbol
drawn as two long plates and two short plates alternating, with a plus sign beside the
top terminal and a minus sign beside the bottom terminal. On the right side place a
resistor drawn as a plain open rectangle.

On the TOP wire draw a solid orange arrow pointing right, from the battery toward the
resistor. Label it in bold orange: "Conventional current, plus to minus".

Directly below the top wire, inside the loop, draw a dashed dark gray arrow pointing
left. Label it in dark gray: "Electron drift, the other way".

Beneath the whole circuit print in bold dark green, on one line:
"Both describe the same circuit. Every formula and schematic in this course uses
conventional current."

Title at top left in bold dark green: "Two ways to describe the same flow".

No numbers anywhere in the image.
```

---

## Image 5: A complete path is required

Save as `voltage-current-complete-path-01.png` in **voltage-current**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style schematic. Clean uniform line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Draw two rectangular circuit loops side by side, left and right, identical in size.

LEFT loop: closed and unbroken. Battery symbol on the left side drawn as alternating
long and short plates, a lamp symbol on the right side drawn as a circle with an X
through it. Draw three small orange arrows spaced around the loop, all pointing the same
way around it. Under this loop print in bold dark green: "Closed loop, current flows".

RIGHT loop: identical, except the TOP wire has a clear gap in it about one eighth of the
loop width, with the two cut ends drawn as small vertical stubs. No arrows anywhere on
this loop. The lamp circle is drawn with a thin gray outline instead of a dark one.
Under this loop print in bold orange: "One break anywhere, current stops everywhere".

Title at top left in bold dark green: "A complete path is required".

No numbers anywhere in the image.
```

---

## Image 6: 5-pin DIN connector face

Save as `midi-din-connector-face-01.png` in **midi**.

Deliberately carries **no pin functions**. The function of each pin lives in the table on
the page beside it, where a correction is an edit rather than a regeneration.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw one large circle centered in the frame, representing the face of a 5-pin DIN
connector viewed head on. Inside the top of the circle draw a wide shallow notch, a
rectangular keyway opening upward, so the orientation of the connector is unmistakable.

Inside the circle draw five small solid black filled circles arranged in the standard
180 degree DIN semicircle, all below the keyway, evenly spaced along an arc that opens
downward.

Number the pins with dark gray numerals placed just outside each pin, in the standard
DIN order reading the face of a female jack: the leftmost pin on the arc is 1, the
rightmost is 3, and 2, 4 and 5 fall in the standard positions between them.

Print nothing else inside the circle. Do not label any pin with a function, a signal
name, a voltage or a color.

Title at top left in bold dark green: "5-pin DIN, looking at the jack".

Beneath the circle print in medium gray on one line: "Pin functions are in the table on
this page."
```

---

## Image 7: TRS MIDI, two standards

Save as `midi-trs-type-a-vs-type-b-01.png` in **midi**.

Same rule as image 6. It shows **where tip and ring are on the plug** and names the two
standards. It does not say which conductor carries what. That is a table.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean uniform line weights, no gradients,
no drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw two identical 3.5 mm TRS plugs in side profile, one above the other, each drawn as
a long horizontal shaft with two thin insulating rings dividing it into three conductor
sections: a rounded tip at the right end, a middle band, and a long sleeve running to
the left into a barrel.

On the UPPER plug, draw thin dark gray leader lines from the tip section and the middle
band out to labels reading exactly "Tip" and "Ring". To the left of the upper plug print
in bold dark green: "Type A".

On the LOWER plug, draw the same two leader lines and the same two labels, "Tip" and
"Ring". To the left of the lower plug print in bold dark green: "Type B".

Between the two plugs, centered, print in bold orange on one line:
"Same jack, different wiring. They do not interoperate."

Do not label any conductor with a pin number, a signal name or a manufacturer.

Title at top left in bold dark green: "TRS MIDI comes in two standards".
```

---

## Image 8: Status byte and data byte

Save as `midi-byte-structure-01.png` in **midi**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style diagram. Clean uniform line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Draw two horizontal rows, one above the other, each made of eight equal square cells
outlined in dark gray, representing the eight bits of a byte. Leave generous vertical
space between the two rows.

UPPER ROW: fill the leftmost cell solid dark green and print a white "1" in it. Leave the
other seven cells empty with thin outlines. Above the row print in bold dark green:
"Status byte". To the right of the row print in dark gray: "Most significant bit is 1".

Beneath the upper row, bracket the leftmost four cells with a dark green brace labeled
"message type", and bracket the rightmost four cells with a dark green brace labeled
"channel".

LOWER ROW: fill the leftmost cell solid orange and print a white "0" in it. Leave the
other seven cells empty with thin outlines. Above the row print in bold orange:
"Data byte". To the right of the row print in dark gray: "Most significant bit is 0".

Beneath the lower row print in dark gray, centered: "Seven bits of value".

Title at top left in bold dark green: "How a receiver tells a status byte from a data
byte".

Do not print any hexadecimal values, decimal ranges or example messages.
```

---

## Image 9: Thru chain against a Thru box

Save as `midi-thru-chain-vs-thru-box-01.png` in **midi**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style block diagram. Clean uniform line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

Split the frame into an upper half and a lower half.

UPPER HALF: draw one rounded rectangle at the far left labeled "Sequencer", then four
more rounded rectangles in a horizontal row to its right, each labeled "Device". Connect
them left to right in a single chain with straight arrows, each arrow leaving one box and
entering the next. Above each arrow after the first, print a small orange label reading
"plus delay". At the right end print in bold orange: "Delay adds up along the chain".
Label this half in bold dark gray at the far left: "Daisy chain".

LOWER HALF: draw the same "Sequencer" rounded rectangle at the far left. To its right
draw a single taller rounded rectangle labeled "Thru box". From the right edge of the
Thru box draw four separate arrows fanning out to four "Device" rounded rectangles
stacked vertically. Print in bold dark green at the right: "Every device gets it at the
same time". Label this half in bold dark gray at the far left: "Thru box".

Title at top left in bold dark green: "Past three devices, use a Thru box".

Do not print any millisecond values. The delay figures are in the table on the page.
```

---

## Image 10: The double trigger path

Save as `midi-local-control-double-trigger-01.png` in **midi**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style block diagram. Clean uniform line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

On the left draw a wide rounded rectangle labeled "Keyboard". Inside it, at the bottom,
draw a smaller nested rounded rectangle labeled "Internal sound engine".

On the right draw a rounded rectangle labeled "DAW". Inside it print in smaller dark gray
text: "MIDI Thru on".

Draw a short orange arrow from the top of the Keyboard box curving down into the nested
Internal sound engine box, staying entirely inside the Keyboard. Label it in orange:
"Path 1, Local Control on".

Draw a second orange arrow leaving the right edge of the Keyboard, entering the DAW,
turning around inside it, leaving the DAW, and entering the Internal sound engine box
from the right. Label it in orange: "Path 2, echoed back by the DAW".

Beneath both, centered, print in bold orange: "One key press, two triggers, a flam on
every note".

Beneath that print in bold dark green: "Fix: set Local Control off".

Title at top left in bold dark green: "Where the double trigger comes from".
```

---

## Image 11: MIDI Clock against MTC

Save as `midi-clock-vs-mtc-01.png` in **midi**.

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style diagram. Clean uniform line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Split the frame into a left half and a right half with a thin vertical divider.

LEFT HALF: title it in bold dark green: "MIDI Clock". Beneath, draw a horizontal line
with a row of short evenly spaced vertical tick marks standing on it, like a metronome
track. Under the line print in dark gray: "Tells a device how fast". Under that print in
orange: "Does not say where you are".

RIGHT HALF: title it in bold dark green: "MIDI Time Code". Beneath, draw a horizontal
timeline bar with a small triangular playhead marker sitting partway along it, and a few
evenly spaced division marks on the bar. Under the bar print in dark gray: "Tells a
device where you are on the timeline". Under that print in orange: "Does not say how
fast".

Across the bottom of the frame, spanning both halves, print in bold dark green:
"Many setups run both: MTC for position, MIDI Clock for tempo."

Title at top left in bold dark green: "Tempo and position are two different jobs".

Do not print any BPM values, timecode values, frame rates or pulse counts.
```
