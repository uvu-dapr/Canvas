# DAPR 2255 Image Brief v78

Generated 2026-09-22. Run each prompt separately in ChatGPT. Save each result with the exact
filename shown, into the exact folder shown. Do not rename.

**Disregard every earlier DAPR 2255 image brief, including v77.** Work only from this file.
**There is exactly one prompt in this brief.** That is not an error. The reason is in Part 1.

---

## Part 1. Why v77 shrank from eight prompts to one

All 232 images referenced by DAPR 2255 were re-inspected at full resolution on 2026-09-22.
Six of the eight v77 prompts are cancelled. Here is what each one turned out to be.

| v77 prompt | Outcome | Reason |
|---|---|---|
| `midi-dmx-fixture-02.jpg` | **Cancelled, superseded** | Your new `midi-dmx-fixture-03.jpg` was checked at full resolution. Top connector: five pins. Bottom connector: five holes. Male input above, female output below, which is the correct DMX convention. It is good. The `-02` file is never referenced by any page and needs no replacement. |
| `power-doubling-is-3db-03.png` | **Cancelled, not needed** | The page runs on `power-doubling-is-3db-01.png`, not `-02`. The `-01` file is correct: two columns, the right one twice the height of the left, both fully inside the frame. Nothing was ever broken on that page. |
| `midi-gm-channel-10-03.png` | **Cancelled, not needed** | The page runs on `midi-gm-channel-10-01.png`, not `-02`. The `-01` file is correct: sixteen squares, the tenth one orange. Counted. Nothing was ever broken on that page. |
| `midi-din-cable-seated-in-jack-01.jpg` | **Done** | Already on disk and correct. A DIN plug fully seated in a panel jack. Nothing more needed. |
| `midi-troubleshooting-cable-pulled-01.jpg` | **Done** | Already on disk and correct. The unplugged connector reads as the subject. Nothing more needed. |
| `midi-rtp-two-interfaces-one-cable-01.jpg` | **Done** | Already on disk and correct. Two rack units, one cable between them. Nothing more needed. |
| `midi-dmx-terminator-02.jpg` | **Removed from ChatGPT entirely** | Standards §20.1 rule 3: a connector face is sourced, never generated. See Part 3. |
| `midi-osc-din-beside-ethernet-01.jpg` | **The one prompt below** | Rewritten so nothing in the frame is a connector face. |

**The rule I broke, stated plainly.** Standards §20.1 rule 3 and §20.5a both say that a
connector face with countable contacts is sourced, never generated, and §20.5a names the two
failures this course already had: an XLR drawn with two pins, and a DIN jack numbered wrong.
The DMX fixture is a connector face. Briefing it to a generator three times was wrong each
time, and the three wrong pin counts that came back are exactly what the rule predicts. The
version that finally came back correct came back correct by luck. Nothing in this brief asks
a generator to draw contacts again.

---

## Part 2. The one image to generate

| # | Kind | File | Page |
|---|---|---|---|
| 01 | photo | `midi-osc-din-beside-ethernet-01.jpg` | MIDI: Open Sound Control Compared to MIDI |

### Image 01, a MIDI cable and a network cable side by side

| Field | Value |
|---|---|
| Filename | `midi-osc-din-beside-ethernet-01.jpg` |
| Format | JPEG, quality 88, on its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Images/midi/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2255--Audio_Hardware_I/_unplaced/MIDI/Osc_Din_Beside_Ethernet.jpg` |
| Used on | Canvas page `MIDI: Open Sound Control Compared to MIDI` |
| Alt text | `A round MIDI cable lying beside a flat network patch cable on a studio bench` |
| Caption | `The difference that matters most is the wire. MIDI gets a cable of its own. OSC rides the same network as everything else in the building.` |

**What this image has to do on the page.** The page argues that the real split between MIDI
and OSC is the transport, not the message. The picture carries that argument by showing two
cables that clearly are not the same kind of cable. It does not need to show a plug face, and
it must not, because that is where every previous failure happened.

**ChatGPT prompt, paste as is:**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft even lighting from above and slightly to the left,
shallow depth of field so the far ends of both cables fall gently out of focus, real cable
jacket texture, on a clean matte dark grey studio bench surface.

Two cables lie side by side across the frame, running roughly left to right, close enough to
compare and clearly separate from each other.

The upper cable is a thick round black cable with a heavy moulded strain relief, photographed
strictly from the SIDE and slightly BEHIND its connector, so the connector reads as a barrel
shape in profile. The face of that connector is turned away from the camera and is not
visible at any point in the frame.

The lower cable is a thin flat blue network patch cable with a small translucent plastic clip
on its end, also photographed from the SIDE, with its contact face turned away from the
camera and not visible.

The clear visual difference between the two is thickness and shape: one thick and round, one
thin and flat.

CRITICAL: no connector face, no contact face, no plug end pointing toward the camera, and no
pins, holes, contacts or blades visible anywhere in the image. If any connector opening is
facing the camera, redo the image with both connectors turned away.

Reading direction is left to right.

No text anywhere in the image. No logo, brand mark, model number, printed cable legend, or
port label. No borders, frames, title bars, or caption text. No hands, no people, no
watermark, no signature. No other cables, no gear, no rack, no patch panel.
```

**Check before you accept it:** look at both connector ends. If you can see into either one,
it is wrong, regardless of how good the rest of the picture looks.

---

## Part 3. Not for ChatGPT. Do not paste this section.

These two items are held to Standards §20.1 rule 3 and go on a capture sheet under §20.6.

| Item | What it needs |
|---|---|
| `midi-dmx-terminator-02.jpg` | A photograph of a real DMX terminator: a five pin XLR shell with a resistor inside and nothing leaving the back. You have lighting gear in reach. Shoot it, or shoot a five pin XLR male plug with the shell open enough to show the resistor. Two minutes with a phone beats a fourth generator attempt. |
| `resistors-audio-applications-infographic.png` | Its XLR pin number panel shows male and female faces with numbered contacts. The two faces mirror each other correctly, and the phantom power claim of two 6.81 kilohm resistors feeding pins 2 and 3 is right. What I cannot certify from the image alone is whether pin 3 belongs at the bottom of the triangle. You wire XLRs. Confirm or correct it. |

---

## Part 4. Two text defects that are being fixed in HTML, not regenerated

Standards §20.5 records that twelve of the first twenty eight generated images for this course
failed, and every failure was text rather than drawing. Sending these two back to a generator
buys two new text defects. Both become HTML on the page instead, the same treatment the seven
MIDI label figures got in v76. No action from you.

| File | Defect |
|---|---|
| `schematics-reference-designators.png` | The subtitle renders PCB with a reversed C, so it reads "P Ɔ B layouts". Every row of the table itself is correct. |
| `resistors-four-band-worked.png` | The instruction reads "Start from the tolerance band and read away from it." Read literally that gives gold, orange, black, brown, which is backwards. The worked arithmetic under it is right: 10 times 1000 is 10,000 ohms, which is 10 kilohms. |
