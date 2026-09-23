# DAPR 3255 Image Brief - Regenerations 03

Generated 2026-09-22, after looking at all 45 generated figures in the repo
composited on white per Standards 20.4b. Four defects found. This brief replaces
`Regenerations 02.md`, whose three prompts were never run and whose style line
Standards 20.5a repealed on 2026-09-21.

Prompts here follow the current rules: a richly rendered dimensional diagram
rather than flat line art, and no text inside the image unless the prompt quotes
it, never more than three items.

| Figure | Verdict | State today |
|---|---|---|
| Op-amp inverting against non-inverting | **Wrong.** The non-inverting half has no input at all | **live on a page** |
| ARP resolution sequence | **Wrong.** A fifth arrow ends in mid-air and strikes through the caption | **live on a page** |
| NAT translation flow | Wrong. Both return-path labels read "from" | pulled in v5, still off the page |
| QoS DSCP priority queue | Wrong. Invents "EF 34" and "AF 26" | pulled in v5, still off the page |

The first two are the urgent ones. They are on pages students will read.

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

## Where the files go

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/electronics
```

1 file: `electronics-opamp-inverting-vs-noninverting-02.png`

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-diagnostics
```

1 file: `network-diagnostics-arp-resolution-sequence-02.png`

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/ip-addressing
```

1 file: `ip-addressing-nat-translation-flow-02.png`

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/network-architecture
```

1 file: `network-architecture-qos-dscp-priority-queue-02.png`

The four `-01` files stay where they are. 20.4 says a conforming filename is
permanent and never overwritten: the page's src moves to `-02` and the old file
remains.

---

## After the files land

Tell me and I will move the two live pages from `-01` to `-02`, put the NAT and
QoS figures back onto the two pages they were pulled from, and reship.
