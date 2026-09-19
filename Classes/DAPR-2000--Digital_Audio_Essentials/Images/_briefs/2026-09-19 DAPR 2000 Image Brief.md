# Image brief: DAPR 2000

**Date:** 2026-09-19
**Covers:** the seven new processing pages, plus every student-facing page in the course that currently has no image
**Governed by:** DAPR Canvas Standards Section 20

---

## Status: six images are already done

I pulled these straight out of the Avid plug-in documentation on your Dropbox and they
are already in the repo and already wired into the pages. **Nothing needed from you.**

| File | Folder | Source |
|---|---|---|
| `processing-compression-bf-2a-plugin-window-01.png` | `processing-compression/` | Plugins Guide p.63 |
| `processing-compression-impact-plugin-window-01.png` | `processing-compression/` | Plugins Guide p.114 |
| `processing-compression-fairchild-670-plugin-window-01.png` | `processing-compression/` | Plugins Guide p.106 |
| `processing-compression-compressor-limiter-iii-plugin-window-01.png` | `processing-compression/` | Plugins Guide p.89 |
| `processing-time-based-d-verb-plugin-window-01.png` | `processing-time-based/` | Plugins Guide p.195 |
| `processing-time-based-mod-delay-iii-plugin-window-01.png` | `processing-time-based/` | Plugins Guide p.248 |

Two already existed in the repo and are reused rather than duplicated:
`processing-compression-bf-76-peak-limiter-01.png` and
`processing-compression-la-2a-leveling-amplifier-01.png`.

**How I got them**, for next time:

```
pdfimages -f <page> -l <page+1> -png "Audio and MIDI Plugins Guide.pdf" <name>
```

Every remaining plug-in window in the program can come from the same place. I do not
need to ask you for a screenshot of any Avid plug-in again.

---

## Coverage: where the course actually stands

Measured against the v32 cartridge, counting only images students see and excluding the
icon set.

| | Pages | With art | Coverage |
|---|---|---|---|
| **Student facing** | 56 | 44 | **79%** |
| Instructor only, do not publish | 7 | n/a | excluded |
| **Target** | | | **85%** |

Four pages would get you to 85. Part A2 below fixes seven and takes it to **91%**.

### The twelve student-facing pages with nothing visual

| Page | Words | What it needs |
|---|---|---|
| Orientation: 3E) Course Legend | 2,017 | Nothing. It is wall to wall icons already, which the count excludes on purpose |
| Orientation: Course Schedule | 1,088 | Nothing. It is a date table and an image would get in the way |
| Orientation: Course Module Outline | 752 | Nothing. Same reason |
| Final Exam: Schedule and Location | 298 | Nothing. It is a room and a time |
| **Monitoring: Overview** | 156 | **A2-1** |
| **Sound: Overview, Sound & Hearing** | 153 | **A2-2** |
| **DAW: Overview, EQ & Dynamics** | 124 | **A2-3** |
| **Processing: Overview, Time-Based Effects** | 116 | **A2-4** |
| **Digital Audio: Overview, The Digital Domain** | 104 | **A2-5** |
| **Mixing & Mastering: Overview** | 104 | **A2-6** |
| **Microphones: Overview** | 95 | **A2-7** |
| Monitoring: Read About Monitoring the Mix | 90 | **Not an image problem.** 90 words is not a reading page. This needs writing, and I should do that rather than decorate it |

---

## Part A2: module overview topic art, seven images

Every module overview page is a short intro, 95 to 156 words, and every one of them opens
with a wall of text. One banner image each fixes the worst of the bare pages in the course
and takes coverage from 79 to 91 percent.

These are **stylized topic art**, which Section 20 permits. None of them depicts a real
product, a front panel, or software.

**Same three closing lines on every prompt**, with one change: these are banners, so they
are wider than they are tall.

```
Flat vector-style illustration. No photorealism, no 3D, no drop shadows, no gradients.
Transparent background. 1600 x 500 pixels, PNG-24.
No text of any kind anywhere in the image.
```

The no-text rule matters more here than anywhere else. Banner art with generated lettering
is where misspelled labels and invented model numbers show up, and there is no reason to
risk it when the page heading already says what the module is.

| # | Page | Filename | Folder |
|---|---|---|---|
| A2-1 | Monitoring: Overview | `monitoring-psychoacoustics-module-banner-01.png` | `monitoring-psychoacoustics/` |
| A2-2 | Sound: Overview | `sound-hearing-frequency-module-banner-01.png` | `sound-hearing-frequency/` |
| A2-3 | DAW: Overview | `daw-eq-dynamics-module-banner-01.png` | `daw-eq-dynamics/` |
| A2-4 | Processing: Overview | `processing-time-based-module-banner-01.png` | `processing-time-based/` |
| A2-5 | Digital Audio: Overview | `digital-domain-module-banner-01.png` | `digital-domain/` |
| A2-6 | Mixing & Mastering: Overview | `mixing-mastering-module-banner-01.png` | `mixing-mastering/` |
| A2-7 | Microphones: Overview | `microphones-characteristics-module-banner-01.png` | `microphones-characteristics/` |

### A2-1 Monitoring

**Alt text:** A stylized overhead view of a listening position between two monitor speakers, with sound paths reflecting off the side walls

```
A wide banner illustration, overhead view, of a listening position in a small room.
Two speaker shapes at the top angled inward toward a single head shape at the bottom
center, forming a triangle. Straight lines run from each speaker to the head. Additional
lines bounce off the left and right walls before reaching the head, drawn lighter to show
they are reflections. Deep blue and warm grey palette.
```

### A2-2 Sound and hearing

**Alt text:** A stylized sound wave traveling left to right and widening into a spectrum of frequency bands

```
A wide banner illustration. On the left, a simple sine wave. Moving right, the wave
gradually separates into a series of vertical bars of increasing then decreasing height,
suggesting a frequency spectrum. The bars run from tall on the left to short on the right.
Deep teal and warm grey palette.
```

### A2-3 EQ and dynamics

**Alt text:** A stylized EQ curve with a boost and a cut, above a compression transfer curve that bends at a threshold point

```
A wide banner illustration split into two halves by a thin vertical divider.
Left half: a smooth horizontal frequency response curve with one broad hump above the
center line and one narrow dip below it.
Right half: a straight diagonal line rising at forty five degrees that bends to a shallower
slope partway up, with a small dot marking the bend.
Amber and charcoal palette.
```

### A2-4 Time-based effects

**Alt text:** A stylized impulse followed by a series of diminishing echoes spreading outward into a diffuse tail

```
A wide banner illustration. On the left, a single tall vertical spike. To its right, a
series of shorter vertical spikes at increasing intervals and decreasing height. Further
right, the spikes become dense and blur together into a soft diminishing shape that fades
out at the right edge. Deep orange and charcoal palette.
```

### A2-5 The digital domain

**Alt text:** A smooth analog wave overlaid with a stepped staircase of sample points showing quantization

```
A wide banner illustration. A smooth continuous sine wave runs left to right. Overlaid on
it, a stepped staircase shape follows the same contour in discrete horizontal steps. Small
dots mark where each step meets the smooth curve. Deep violet and warm grey palette.
```

### A2-6 Mixing and mastering

**Alt text:** A stylized row of mixer faders at varying heights feeding into a single output meter

```
A wide banner illustration. A row of eight vertical fader tracks with knobs at varying
heights across the left two thirds. Lines from the bottom of each track converge toward
the right into a single vertical meter bar. Slate grey and deep green palette.
```

### A2-7 Microphones

**Alt text:** Three stylized polar pattern shapes side by side, showing omnidirectional, cardioid and figure of eight

```
A wide banner illustration showing three polar pattern diagrams side by side, evenly spaced.
Left: a perfect circle.
Center: a heart shape with the point facing downward.
Right: a figure of eight, two circles stacked vertically touching at the middle.
Each shape has a small dot at its center marking the microphone position.
Deep red and warm grey palette.
```

---

## Part A: for ChatGPT to generate

All six are **conceptual diagrams**, which Section 20 allows. None of them depicts a real
product, a front panel, or a piece of software.

**Every prompt below ends with the same three lines. Do not drop them.**

```
Flat vector-style technical diagram. No photorealism, no 3D, no drop shadows, no gradients.
Transparent background. 1600 pixels wide, PNG-24.
Labels in a clean sans-serif. Spell every label exactly as written. Do not add any label I have not listed.
```

### A1. Attack and release on a drum transient

**Goes on:** Processing: Read - Attack and Release
**Filename:** `processing-compression-attack-release-envelope-01.png`
**Folder:** `Classes/DAPR-2000--Digital_Audio_Essentials/Images/processing-compression/`
**Alt text:** Three waveform envelopes of the same snare hit showing a fast attack flattening the transient, a medium attack letting the transient through, and a slow attack barely compressing

```
A technical diagram showing three copies of the same drum hit waveform envelope, stacked
vertically, each in its own labeled row.

Row 1, labeled "Fast attack, under 1 ms": the sharp initial spike is flattened down to
nearly the same height as the body that follows.
Row 2, labeled "Medium attack, 10 to 30 ms": the initial spike passes through at full
height, and the body behind it is visibly reduced.
Row 3, labeled "Slow attack, 50 ms and up": the spike and most of the body both pass at
close to full height.

A dashed horizontal line runs across all three rows labeled "Threshold".
A short caption under the stack reads "Same hit, same threshold, same ratio. Only attack changed."
```

### A2. Release too fast, right, and too slow

**Goes on:** Processing: Read - Attack and Release
**Filename:** `processing-compression-release-behavior-01.png`
**Alt text:** Three gain reduction traces over four drum hits showing release too fast recovering within each cycle, release correct recovering between hits, and release too slow never recovering

```
A technical diagram with three stacked graphs. Each graph plots a gain reduction line
over time beneath four evenly spaced drum hits shown as small vertical marks along the top.
The vertical axis is labeled "Gain reduction" with 0 dB at the top and -10 dB at the bottom.

Graph 1, labeled "Too fast": the line dips and returns to 0 dB many times between each hit,
looking jagged.
Graph 2, labeled "Right": the line dips at each hit and returns most of the way to 0 dB
just before the next hit arrives.
Graph 3, labeled "Too slow": the line dips at the first hit and never returns to 0 dB,
staying low across all four hits.
```

### A3. Parallel compression routing

**Goes on:** Processing: Read - Parallel Compression
**Filename:** `processing-compression-parallel-routing-01.png`
**Alt text:** A routing diagram showing a drum track splitting to both the mix output and a send feeding an auxiliary input with a heavy compressor, with both paths blending at the output

```
A left to right signal routing diagram made of labeled rectangular blocks joined by arrows.

Start at a block labeled "Drum tracks".
One arrow goes straight right to a block labeled "Mix output", along a line labeled "Dry, untouched".
A second arrow branches downward from "Drum tracks" along a line labeled "Send", into a
block labeled "Aux input: Drum Crush", then into a block labeled "Compressor, 10:1, fast
attack, 10 to 20 dB reduction", then rejoins the "Mix output" block from below.
A small fader icon sits on the lower path just before it rejoins, labeled "Blend to taste".
```

### A4. Send versus insert

**Goes on:** Processing: Read - Send Versus Insert
**Filename:** `processing-time-based-send-vs-insert-01.png`
**Folder:** `Classes/DAPR-2000--Digital_Audio_Essentials/Images/processing-time-based/`
**Alt text:** Two routing diagrams side by side, one showing all audio passing through an insert plugin, the other showing a copy branching to an auxiliary input while the original continues untouched

```
Two routing diagrams side by side, each in its own bordered panel with a heading.

Left panel, heading "Insert": a block labeled "Track" with a single arrow passing straight
through a block labeled "Plug-in" and on to a block labeled "Mix output". A caption under
it reads "All of the audio goes through it."

Right panel, heading "Send": a block labeled "Track" with one arrow going straight to
"Mix output", and a second arrow branching off to a block labeled "Aux input" holding a
block labeled "Reverb, 100 percent wet", which then rejoins "Mix output". A caption under
it reads "A copy goes somewhere else. The original continues untouched."
```

### A5. Delay time note value grid

**Goes on:** Processing: Read - Delay Timing and Modulation
**Filename:** `processing-time-based-delay-note-values-01.png`
**Alt text:** A grid showing one bar of four four time with quarter, eighth, dotted eighth and sixteenth note delay positions marked against the beat

```
A rhythm grid showing one bar of 4/4 time. A horizontal line runs across with four evenly
spaced beat markers labeled 1, 2, 3 and 4.

Below the line, four rows of small marks show where each delay repeat falls:
Row 1, labeled "Quarter note": marks land exactly on beats 2, 3 and 4.
Row 2, labeled "Eighth note": marks land on every beat and every half beat.
Row 3, labeled "Dotted eighth": marks land between the beats, clearly off the grid lines.
Row 4, labeled "Sixteenth note": marks land four times per beat.

A caption reads "The dotted eighth lands between the beats. That is why it sounds like
rhythm instead of an echo."
```

### A6. What pre-delay does

**Goes on:** Processing: Read - Reverb Anatomy
**Filename:** `processing-time-based-pre-delay-01.png`
**Alt text:** Two timeline diagrams showing a vocal word with reverb starting immediately versus reverb starting forty milliseconds later, leaving the word clear

```
Two horizontal timeline diagrams stacked vertically, each showing time running left to right
with a millisecond scale from 0 to 200.

Top timeline, labeled "No pre-delay": a solid block labeled "Word" starts at 0, and a
shaded region labeled "Reverb" starts at 0 as well, overlapping the word completely.
Bottom timeline, labeled "40 ms pre-delay": the same solid "Word" block starts at 0, and
the shaded "Reverb" region does not begin until the 40 ms mark, leaving the start of the
word clear.

A caption reads "Same reverb, same decay. The word stays intelligible."
```

---

## Part B: public domain hardware photos, if you want them

**Optional.** The pages already show the Avid plug-in windows, which is what students will
actually open. These would be a nice addition showing the real units the plug-ins model.

Section 20 rule 3 is absolute here: **real hardware is never generated.** These have to be
genuine photographs, public domain or openly licensed.

| Subject | Where it would go | What the photo must show |
|---|---|---|
| Urei 1176 hardware unit | Four Compressors page, beside the BF76 window | The front panel, ideally with the four ratio buttons and the VU meter legible |
| Teletronix LA-2A hardware unit | Four Compressors page, beside the BF-2A window | The front panel with Gain and Peak Reduction visible |
| Fairchild 670 hardware unit | Four Compressors page, beside the Fairchild 670 window | The front panel. This one is rare enough that any clear shot is a win |
| EMT 140 plate reverb | Reverb Anatomy page | The steel plate in its frame, to show why it is called a plate |

**Naming when you find them:**

```
processing-compression-1176-hardware-01.jpg
processing-compression-la-2a-hardware-01.jpg
processing-compression-fairchild-670-hardware-01.jpg
processing-time-based-emt-140-plate-hardware-01.jpg
```

JPEG, quality 85 to 90, 1600 px wide, under 500 KB. Drop them in the folders above and
tell me, and I will write the `img` tags and captions.

**Check the license before you take one.** Wikimedia Commons lists it on the file page.
Public domain or CC BY works. CC BY-NC does not, because this is a university course.

---

## What I still need from you

1. **Nothing on plug-ins.** I can pull any Avid plug-in window from the Plugins Guide myself.
2. **Run Part A and Part A2 through ChatGPT.** Thirteen images total, six diagrams and seven
   banners. That takes student-facing image coverage from 79 percent to 91 percent.
3. **Part B only if you want it.** The pages work without it.
4. **One decision:** the new pages currently use colors I picked. Each module has an existing
   color in the course. Tell me whether to match the existing colors or re-sequence the whole
   course against the Section 3 resistor code, and I will make every page consistent in one pass.
