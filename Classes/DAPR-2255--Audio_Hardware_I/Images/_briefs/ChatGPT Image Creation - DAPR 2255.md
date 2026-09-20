# DAPR 2255 Image Brief - Diode Protection Circuits
Generated 2026-09-16. Run each prompt separately in ChatGPT. Save each result
with the exact filename shown, into the exact folder shown. Do not rename.

Two images. They replace the two panels of `diodes-leds-protection-circuits-diagram.png`
on the Canvas page `Diodes & LEDs: Applications in Audio Circuits`. The existing file
stays in the repo under its current name per the never-rename rule; the page's `src`
moves to the two new files.

**Why it is being replaced.** In the current figure's flyback panel, D1 is drawn anode
to the top node and cathode to the bottom node. With the high-side switch closed that
diode is forward biased and shorts the supply. The orange current arrows agree with the
symbol and are wrong in the same direction. Both new images use the canonical low-side
switch arrangement, where the polarity is unambiguous.

---

## Image 01 - Reverse polarity protection

| Field | Value |
|---|---|
| Filename | `diodes-leds-reverse-polarity-protection-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/diodes-leds/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-reverse-polarity-protection-01.png` |
| Used on | Canvas page `Diodes & LEDs: Applications in Audio Circuits` |
| Alt text | `Series diode between a DC supply and a load, blocking current when the supply is reversed` |
| Caption | `Figure 1. A series diode passes current at correct polarity and blocks it when the supply is reversed.` |

**ChatGPT prompt (paste as-is):**

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

---

## Image 02 - Flyback protection across a relay coil

| Field | Value |
|---|---|
| Filename | `diodes-leds-flyback-protection-01.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/diodes-leds/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/Images/diodes-leds/diodes-leds-flyback-protection-01.png` |
| Used on | Canvas page `Diodes & LEDs: Applications in Audio Circuits` |
| Alt text | `Flyback diode across a relay coil, cathode to the positive supply rail, with a low-side switch` |
| Caption | `Figure 2. The flyback diode sits across the coil with its cathode at the positive rail, reverse biased until the switch opens.` |

**ChatGPT prompt (paste as-is):**

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

---

# Check the returned images before saving

| Check | Image 01 | Image 02 |
|---|---|---|
| Background is fully transparent, no white box | yes | yes |
| Every label spelled exactly as quoted | 5 labels | 5 labels |
| Diode bar orientation | bar on the right of the triangle tip | **bar on TOP, triangle pointing up** |
| No borders, frames, or caption baked in | yes | yes |
| PNG under 1 MB | yes | yes |

Image 02's diode orientation is the whole point of the redraw. If the bar comes back
at the bottom, regenerate with that sentence quoted more explicitly rather than
accepting it or editing it by hand.

---

# Destination folder

/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/diodes-leds

Expected file count in that folder after this brief: **2 new files**.

```
diodes-leds-reverse-polarity-protection-01.png
diodes-leds-flyback-protection-01.png
```

---

# Not in this brief, and why

**The five tables that are pictures.** The audio signal levels, the AWG chart, the
insulation materials, the BJT versus FET comparison and the battery capacity reference
all exist as images and only as images, and quiz items and assignment tasks depend on
data that lives only inside the pixels. Those images are fine. The fix is putting the
same facts into the page prose, which Section 20.5 requires anyway: text inside an
image is a bonus, never the delivery mechanism. That is a page edit, not a generation
job.

**The talkback switch table.** `switches-talkback-box-switches.png` has a baked-in
typo, "switch tyee" for "switch type", in its subtitle. It is not briefed here because
it is a composite built around photographs of real switches, and Section 20.6 says real
hardware is sourced and never generated. Regenerating it would replace real switch
photos with invented ones. It needs the original source file edited, or a capture sheet.

**Three figures I previously reported as wrong are correct.** I opened every one. The
battery series and parallel figure, the SPDT symbol, and the talkback wiring row all
say the right thing. I had been repeating a stale list without re-checking.
