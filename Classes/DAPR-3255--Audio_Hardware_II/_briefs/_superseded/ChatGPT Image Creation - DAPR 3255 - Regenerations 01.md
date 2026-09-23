# DAPR 3255 Image Brief - Regenerations 01
Generated 2026-09-16. Run each prompt separately in ChatGPT. Save each result
with the exact filename shown, into the exact folder shown. Do not rename.

Three images from the first brief teach something false and are replaced here. Per
Section 20.4 a revised image is `-02` and the original `-01` file stays where it is,
never renamed and never overwritten. The page `src` moves to the `-02` file.

Every one of these three was caused by wording in my own prompt, not by the
generator. The corrected wording is in each prompt below.

---

## Image R01 - Op-amp inverting versus non-inverting

| Field | Value |
|---|---|
| Filename | `electronics-opamp-inverting-vs-noninverting-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Electronics/Rendered_Triangles_With_Banded_Resistors.png` |
| Used on | Canvas page `Electronics: 07 Opamp Circuits` |
| Alt text | `Inverting and non inverting op amp topologies side by side with input and feedback resistors labeled` |
| Caption | `Figure 7. The same part, two arrangements, two behaviors.` |
| What was wrong in -01 | The non-inverting circuit had no input signal connected. The plus input ended in a floating stub, so the circuit as drawn has no input at all. |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean line weights, no gradients, no
drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw two op amp circuits side by side, separated by a thin vertical divider line in
#616161, both in clean single weight schematic line art.

Draw each op amp as a triangle pointing right with two input leads on the left flat
edge and one output lead at the right point. Mark the upper input with a minus sign
and the lower input with a plus sign.

LEFT CIRCUIT, labeled exactly "Inverting":
Draw an input signal line entering from the far left edge of the canvas, passing
through a resistor labeled exactly "Rin", then continuing to the minus input. Tie the
plus input to ground with a standard ground symbol. Run a feedback resistor labeled
exactly "Rf" from the output back to the minus input. Label the input line at its
left end exactly "In".

RIGHT CIRCUIT, labeled exactly "Non-inverting":
Draw an input signal line entering from the left and connecting DIRECTLY to the plus
input, with no resistor in that path. This input line must be clearly connected to the
plus input and must not end in a floating stub. Label it at its left end exactly "In".
Run a feedback resistor labeled exactly "Rf" from the output back to the minus input.
Run a second resistor labeled exactly "Rg" from the minus input down to ground with a
standard ground symbol.

Every wire must terminate at a component, a ground symbol, or a labeled input or
output. No wire ends in empty space.

Draw both triangles in #0D47A1 and everything else in #212121.

Reading direction is left to right.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add
any text other than the labels listed above.
```

---

## Image R02 - NAT translation flow

| Field | Value |
|---|---|
| Filename | `ip-addressing-nat-translation-flow-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/IP_Addressing/Rendered_Packets_Changing_Color_Midstream.png` |
| Used on | Canvas page `Networking: Network Address Translation (NAT)` |
| Alt text | `NAT rewriting the source address outbound and the destination address on the return path` |
| Caption | `Figure 5. NAT rewrites the source on the way out and the destination on the way back.` |
| What was wrong in -01 | The return arrow was labeled "from" on both sides. On the return path NAT rewrites the destination, not the source, so the old labels taught the mechanism backwards. |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean line weights, no gradients, no
drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a horizontal flow across the canvas with three zones separated by two vertical
dashed lines in #616161.

In the left zone draw a small square labeled exactly "192.168.1.57". In the middle
zone draw a rectangle filled #E65100 with white text reading exactly "NAT". In the
right zone draw a cloud shape outlined #212121 labeled exactly "Internet".

Draw a solid arrow in #1B5E20 running left to right across the top half, with a small
tag above the line in the left zone reading exactly "src 192.168.1.57" and a second
tag above the line in the right zone reading exactly "src 203.0.113.9".

Draw a second solid arrow in #0D47A1 running right to left across the bottom half,
with a small tag below the line in the right zone reading exactly "dst 203.0.113.9"
and a second tag below the line in the left zone reading exactly "dst 192.168.1.57".

Label the top arrow at its far left, outside the zones, exactly "Outbound". Label the
bottom arrow at its far left, outside the zones, exactly "Return".

Use #212121 for all text outside filled shapes.

Reading direction is left to right on the top arrow and right to left on the bottom
arrow.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add
any text other than the labels listed above.
```

---

## Image R03 - QoS priority queues

| Field | Value |
|---|---|
| Filename | `network-architecture-qos-dscp-priority-queue-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/_unplaced/Network__Architecture/Wedge_Merging_Four_Cube_Rows.png` |
| Used on | Canvas page `Networking: Quality of Service` |
| Alt text | `Mixed traffic sorted into DiffServ priority queues so clock and audio leave the port first` |
| Caption | `Figure 5. QoS decides what leaves first when the port is full.` |
| What was wrong in -01 | The queue labels read "EF 46", "EF 34", "AF 26", "BE 0". EF is DSCP 46 only. DSCP 34 is AF41 and DSCP 26 is AF31, so "EF 34" names a code point that does not exist. |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical illustration. Clean line weights, no gradients, no
drop shadows, no 3D, no photorealism, no watermark, no signature.

Draw a funnel shape opening on the left and narrowing to a single output on the
right.

Into the wide left end feed four labeled streams, each a row of small squares in a
different color, labeled exactly "Clock", "Audio", "Video", "File transfer". Use
#B71C1C for Clock, #1B5E20 for Audio, #0D47A1 for Video, #616161 for File transfer.

Inside the funnel draw four stacked horizontal lanes, with Clock in the top lane,
Audio in the second, Video in the third, File transfer in the bottom.

Label the lanes on their left edge, top to bottom, exactly: "CS7  DSCP 56",
"EF  DSCP 46", "AF41  DSCP 34", "BE  DSCP 0".

Out of the narrow right end draw one line carrying the squares in the order Clock,
Audio, Video, File transfer.

Use #212121 for all text.

Reading direction is left to right.

Do not draw any logo, brand mark, model number, product photograph, or software
interface. Do not include borders, frames, title bars, or caption text. Do not add
any text other than the labels listed above.
```

---

## Destination folders

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics
```
1 file
```
electronics-opamp-inverting-vs-noninverting-02.png
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing
```
1 file
```
ip-addressing-nat-translation-flow-02.png
```

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture
```
1 file
```
network-architecture-qos-dscp-priority-queue-02.png
```
