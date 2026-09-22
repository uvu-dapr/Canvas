# DAPR 3255 Image Brief - Regenerations 02

Generated 2026-09-20. Run each prompt separately in ChatGPT. Save each result
with the exact filename shown, into the exact folder shown. Do not rename.

These three replace figures whose `-01` versions were judged on 2026-09-20 by
compositing each one on white first, per Standards 20.4b. Two of the three
assert something factually wrong and are currently **off their pages** in
`DAPR-3255-Course-Turnkey-v5.imscc`, so those pages ship with prose and no
figure until these land. The third is sound and its page points back at `-01`.

| Figure | Verdict | State in v5 |
|---|---|---|
| NAT translation flow | Wrong: both return-path labels read "from" | pulled off the page |
| QoS DSCP priority queue | Wrong: invents "EF 34" and "AF 26" | pulled off the page |
| Op-amp inverting vs non-inverting | Sound, but unlabeled signal path | page points at `-01` |

Once all three `-02` files exist and are pushed, the three `<img src>` values
move from `-01` to `-02` and the two pulled figures go back on their pages.

---

## Image 01 - NAT translation flow

| Field | Value |
|---|---|
| Filename | `ip-addressing-nat-translation-flow-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing/ip-addressing-nat-translation-flow-02.png` |
| Used on | Canvas page `Networking: Network Address Translation (NAT)` |
| Alt text | `Outbound packet source rewritten from a private address to a public one, and the reply addressed back` |
| Caption | `Figure 1. NAT rewrites the source address outbound and the destination address on the reply.` |

**What was wrong with -01:** on the return path both labels read "from". A
packet coming back from the internet is addressed **to** the public address,
then **to** the private one. As drawn, NAT appears to rewrite the source on the
way back, which is the opposite of what it does.

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical diagram. Clean line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

Draw a horizontal layout with three zones separated by two vertical dashed
grey lines. On the left, a rectangle labeled exactly "192.168.1.57". In the
middle, a solid orange rectangle labeled exactly "NAT". On the right, a cloud
shape labeled exactly "Internet".

Draw two horizontal arrows across the whole width.

The upper arrow points LEFT TO RIGHT and is dark green. Label the segment
between the host and NAT exactly: "src 192.168.1.57". Label the segment
between NAT and the Internet exactly: "src 203.0.113.9".

The lower arrow points RIGHT TO LEFT and is blue. Label the segment between
the Internet and NAT exactly: "dst 203.0.113.9". Label the segment between NAT
and the host exactly: "dst 192.168.1.57".

Put each of the four labels in a small white rectangle with a thin grey border,
sitting on its arrow segment.

Use #212121 for all text and outlines, #993300 for the NAT rectangle fill with
white text, dark green for the upper arrow and #0D47A1 for the lower arrow.

Reading direction is left to right for the outbound path.

Do not draw any logo, brand mark, model number, product photograph, or router
hardware. Do not include borders, frames, title bars, or caption text. Do not
add any text other than the labels listed above.
```

---

## Image 02 - QoS DSCP priority queue

| Field | Value |
|---|---|
| Filename | `network-architecture-qos-dscp-priority-queue-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture/network-architecture-qos-dscp-priority-queue-02.png` |
| Used on | Canvas page `Networking: Quality of Service` |
| Alt text | `Four traffic types entering a switch and leaving in DSCP priority order, clock first` |
| Caption | `Figure 1. DSCP marking decides what leaves the switch first when the link is full.` |

**What was wrong with -01:** it invented two class names. There is no "EF 34"
(EF is DSCP 46 only; 34 is AF41) and no "AF 26" (26 is AF31). It also marked
clock as EF 46 and audio as EF 34, where Audinate's Dante scheme puts
time-critical PTP events at CS7 56 and audio and PTP at EF 46.

**Verify the marking values against Audinate's current Dante QoS documentation
before running this prompt.** The values below are the ones to teach unless
Audinate has changed them.

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style technical diagram. Clean line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

On the left, four horizontal rows of small squares entering from the left edge,
each row a different color, each with a text label to its left. Label the rows
from top to bottom exactly: "PTP clock", "Audio", "Video", "File transfer".

In the middle, a funnel shape narrowing left to right, containing four stacked
horizontal lanes. Label the lanes from top to bottom exactly: "CS7 56",
"EF 46", "AF41 34", "BE 0".

On the right, a single horizontal row of squares leaving the funnel, ordered so
that all squares of the top lane color come first, then the second lane color,
then the third, then the fourth.

Use dark red for PTP clock and the CS7 lane, dark green for Audio and the EF
lane, #0D47A1 for Video and the AF41 lane, and grey #616161 for File transfer
and the BE lane. Use #212121 for all text and outlines.

Reading direction is left to right.

Do not draw any logo, brand mark, model number, product photograph, or switch
hardware. Do not include borders, frames, title bars, or caption text. Do not
add any text other than the eight labels listed above.
```

---

## Image 03 - Op-amp inverting vs non-inverting

| Field | Value |
|---|---|
| Filename | `electronics-opamp-inverting-vs-noninverting-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics/electronics-opamp-inverting-vs-noninverting-02.png` |
| Used on | Canvas page `Electronics: Op-amp Circuits` |
| Alt text | `Inverting and non-inverting op-amp configurations with input and output marked on each` |
| Caption | `Figure 1. Where the signal enters is what makes one inverting and the other not.` |

**What was wrong with -01:** nothing false. Both topologies are drawn
correctly. The non-inverting side leaves the signal path into the plus input as
an unlabeled stub, and neither side marks Vin or Vout, so a student cannot see
the one thing the figure exists to show. **The page currently uses `-01`, so
this is an improvement rather than a repair.**

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

Flat vector-style schematic drawing. Clean line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.

Draw two op-amp circuits side by side, separated by a thin vertical grey line.

Left circuit: a triangle pointing right with a minus sign on the upper input
and a plus sign on the lower input. A resistor labeled exactly "Rin" runs from
a line entering at the far left into the minus input. A resistor labeled
exactly "Rf" runs from the minus input over the top of the triangle to the
output line. The plus input connects down to a ground symbol. Label the line
entering at the far left exactly "Vin" and the line leaving the triangle tip
exactly "Vout". Label this circuit exactly "Inverting".

Right circuit: a triangle pointing right with a minus sign on the LOWER input
and a plus sign on the UPPER input. A line enters the plus input from the far
left. A resistor labeled exactly "Rg" runs from the minus input down to a
ground symbol. A resistor labeled exactly "Rf" runs from the minus input over
the top of the triangle to the output line. Label the line entering at the far
left exactly "Vin" and the line leaving the triangle tip exactly "Vout". Label
this circuit exactly "Non-inverting".

Use #0D47A1 for both triangles and #212121 for all wires, resistors, ground
symbols and text.

Reading direction is left to right, input on the left and output on the right.

Do not draw any logo, brand mark, model number, part number, product
photograph, or breadboard. Do not include borders, frames, title bars, or
caption text. Do not add any text other than the labels listed above.
```

---

## Where the files go

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing
```

1 file: `ip-addressing-nat-translation-flow-02.png`

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture
```

1 file: `network-architecture-qos-dscp-priority-queue-02.png`

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics
```

1 file: `electronics-opamp-inverting-vs-noninverting-02.png`
