# DAPR 2000 Image Brief - v34 Corrections
Generated 2026-09-20. Every image in this file already exists and was rejected on visual
review. Run each prompt separately in ChatGPT and overwrite the existing file with the
exact same filename, into the same folder. Do not rename and do not create a `-02`.

Three of the nine images reviewed passed and are already wired into the cartridge:
`daw-first-mix-three-checks-01.png`, `processing-compression-parallel-routing-01.png`,
and `processing-time-based-send-vs-insert-01.png`. The six below did not.

**The defect is named at the top of each prompt on purpose.** The generator got the concept
right and the detail wrong every time, so the prompt has to say which detail.

**Two of these are wrong in a way a student would read off the picture and believe.**
Images 01 and 02 are the priority. The other four are quality problems.

---

## 01. Pre-delay, PRIORITY, currently wrong

| Field | Value |
|---|---|
| Filename | `processing-time-based-pre-delay-01.png` |
| Folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Images/processing-time-based/` |
| Used on | `Processing: Read - Reverb Anatomy` |
| What is wrong now | The panel labeled **No pre-delay** shows the reverb starting at about 40 ms on its own axis. With no pre-delay the reverb starts at 0 ms, at the same instant as the word. As drawn, a student reads 40 ms off the chart and learns the opposite of the point |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 500 pixel PNG with a white background.

Flat vector-style technical illustration. Clean line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Two panels side by side, each showing a waveform on a time axis labeled in milliseconds with
ticks at 0, 50, 100, 150 and 200.

Left panel, titled "No pre-delay": a short blue speech burst labeled "Word" starting at 0 ms
and lasting about 30 ms. A purple reverb tail labeled "Reverb" that ALSO starts at 0 ms, at
exactly the same instant as the word, overlapping it completely from the start, and decaying
to nothing by 200 ms. There must be no gap of any kind between the start of the word and the
start of the reverb.

Right panel, titled "40 ms pre-delay": the identical blue word starting at 0 ms, then a flat
silent line, then the identical purple reverb tail beginning exactly at the 40 ms tick and
decaying to nothing by 200 ms. The gap between 0 ms and 40 ms must be visibly empty and must
line up with the 40 ms tick on the axis.

The reverb tail must be the same shape and the same length in both panels.

Beneath both panels, one line of text, centered, exactly:
"Same reverb, same decay. The word stays intelligible."

Use #212121 for axes, ticks, tick numbers and text. Use #0D47A1 for the word. Use #4A148C for
the reverb.

Do not draw any logo, brand mark, model number, or product photograph. Do not include borders,
frames, title bars, or rounded colored label pills. Do not add any text other than the labels
listed above. Use American spelling in every label.
```

---

## 02. Sample peak versus true peak, PRIORITY, currently wrong

| Field | Value |
|---|---|
| Filename | `mixing-mastering-sample-vs-true-peak-01.png` |
| Folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Images/mixing-mastering/` |
| Used on | `Mixing & Mastering: Read - Loudness, True Peak and Streaming Targets` |
| What is wrong now | Two faults. The shaded region sits **below** the 0.0 dBFS line, so it marks the area under the ceiling instead of the overshoot above it, which is the entire point. And the two panels use different sample positions, so they read as two different signals rather than one signal measured two ways |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a white background.

Flat vector-style technical illustration. Clean line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Two panels side by side. Both panels show THE SAME seven sample points at exactly the same
horizontal and vertical positions as each other. This is essential: it is one signal shown
two ways, not two signals.

Place the seven sample dots so they rise to a single crest and fall away: low, low-mid, mid,
high, HIGHEST, high, mid. The HIGHEST dot sits exactly on a horizontal dashed line labeled
"0.0 dBFS". No dot is above that line in either panel.

Left panel, titled "Sample peak": connect the seven dots with straight line segments only.
Nothing rises above the 0.0 dBFS line anywhere. Beneath the panel:
"Every sample is at or below the ceiling."

Right panel, titled "True peak": the same seven dots in the same positions, now connected by
a smooth curved line that passes through every dot and overshoots between them, so the curve
rises ABOVE the 0.0 dBFS dashed line near the crest.

Shade ONLY the area that is above the 0.0 dBFS dashed line and below the curve. That shaded
area is a thin sliver at the top of the curve. Do not shade anything below the dashed line.
Label that sliver "+1.2 dBTP" with the label placed clear of the curve so no text overlaps
any line. Beneath the panel:
"The waveform between the samples is higher than either one."

Below both panels, one line of text, centered, exactly:
"This is why masters are delivered at minus 1.0 dBTP."

Use #212121 for the dashed line, axes and all text. Use #0D47A1 for the sample dots and both
connecting lines. Use #B71C1C for the shaded sliver above the ceiling and its label.

Do not draw any logo, brand mark, model number, or product photograph. Do not include borders,
frames, title bars, or rounded colored label pills. Do not add any text other than the labels
listed above. Use American spelling. Write the word "minus" rather than a minus sign.
```

---

## 03. Attack on a drum transient

| Field | Value |
|---|---|
| Filename | `processing-compression-attack-release-envelope-01.png` |
| Folder | `.../Images/processing-compression/` |
| Used on | `Processing: Read - Attack and Release` |
| What is wrong now | The compressed output peaks at the threshold line in all three panels, so the slow attack looks exactly as clamped as the fast one. With a slow attack the output should visibly rise well above the threshold before the compressor catches it. The "Threshold" labels are also clipped at the right edge |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a white background.

Flat vector-style technical illustration. Clean line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

Three stacked panels, each showing the same drum hit envelope: a very fast rise to a sharp
peak, then a decay to silence. Draw that original envelope in light gray in all three panels,
identical every time. Draw a horizontal dashed line across each panel labeled "Threshold",
placed at about 40 percent of the peak height. Place the word "Threshold" ABOVE the dashed
line at the left end, fully inside the panel, never at the right edge.

Over the gray envelope, draw the compressed output as a solid red line.

Panel 1, labeled "Fast attack, under 1 ms": the red line rises with the gray envelope but is
pulled down to the threshold almost immediately, so its peak barely exceeds the dashed line.

Panel 2, labeled "Medium attack, 10 to 30 ms": the red line rises with the gray envelope and
reaches ABOUT HALFWAY between the threshold and the gray peak before being pulled back down.

Panel 3, labeled "Slow attack, 50 ms and up": the red line rises with the gray envelope and
reaches NEARLY THE FULL GRAY PEAK before being pulled back down.

The three red peaks must be visibly different heights, lowest in panel 1 and highest in panel
3. That difference is the whole point of the figure.

Beneath all three panels, one line of text, centered, exactly:
"Same hit, same threshold, same ratio. Only attack changed."

Use #212121 for text and the dashed threshold line. Use #BDBDBD for the original envelope.
Use #B71C1C for the compressed output.

Do not draw any logo, brand mark, model number, or product photograph. Do not include borders,
frames, title bars, or rounded colored label pills. Do not let any text touch or cross a panel
edge. Use American spelling.
```

---

## 04. Release behavior

| Field | Value |
|---|---|
| Filename | `processing-compression-release-behavior-01.png` |
| Folder | `.../Images/processing-compression/` |
| Used on | `Processing: Read - Attack and Release` |
| What is wrong now | The **Too slow** panel has its transitions inverted. At each hit the trace jumps upward toward 0 dB and then curves down, when a hit must drive gain reduction DOWNWARD and the recovery between hits must move it back UP toward 0 dB |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a white background.

Flat vector-style technical illustration. Clean line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature.

At the top, a row of four evenly spaced drum hits drawn as a black waveform.

Below that, three stacked panels, each a gain reduction meter trace over the same four hits.
Each panel has a vertical axis labeled "Gain reduction" with 0 dB at the TOP and minus 10 dB
at the BOTTOM. In every panel, each hit drives the trace sharply DOWNWARD from 0 dB toward
minus 10 dB, and the recovery between hits moves the trace back UPWARD toward 0 dB. Never the
reverse.

Panel 1, titled "Too fast": each hit drops the trace to minus 10 dB and it returns all the way
up to 0 dB almost instantly, well before the next hit, giving four sharp isolated spikes.

Panel 2, titled "Right": each hit drops the trace to minus 10 dB and it recovers smoothly back
up to 0 dB, just reaching 0 dB shortly before the next hit arrives.

Panel 3, titled "Too slow": each hit drops the trace to minus 10 dB and it recovers upward only
part way, reaching about minus 4 dB before the next hit drops it again. The trace never returns
to 0 dB at any point after the first hit.

Use #212121 for axes and text, #B71C1C for panel 1, #1B5E20 for panel 2, #0D47A1 for panel 3.

Do not draw any logo, brand mark, model number, or product photograph. Do not include borders,
frames, title bars, or rounded colored label pills. Write "minus 10 dB" and "minus 4 dB" using
the word minus. Use American spelling.
```

---

## 05. Delay note values

| Field | Value |
|---|---|
| Filename | `processing-time-based-delay-note-values-01.png` |
| Folder | `.../Images/processing-time-based/` |
| Used on | `Processing: Read - Delay Timing and Modulation` |
| What is wrong now | The dotted eighth row appears to place dots on beats 2 and 3, which contradicts its own caption. A dotted eighth is three sixteenths, so in one bar it falls on beat 1, off the beat three times, on beat 4, then off the beat again. The style is also a bright infographic that does not match any other image in the course |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a white background.

Flat vector-style technical illustration. Clean thin line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature. Plain sans serif text in a
normal weight. Do not use rounded colored label pills or heavy bold display type.

Draw one bar of 4/4. Place four vertical dashed guide lines across the whole figure at beats
1, 2, 3 and 4, numbered 1, 2, 3, 4 along the top.

Draw four horizontal rows. Each row has a plain left-aligned text label and a line of dots
marking where each delay repeat falls. Divide the bar into 16 equal sixteenth-note positions,
numbered 0 through 15, and place dots exactly on these positions:

Row 1, "Quarter note": positions 0, 4, 8, 12. Four dots, one on each numbered beat.
Row 2, "Eighth note": positions 0, 2, 4, 6, 8, 10, 12, 14. Eight dots.
Row 3, "Dotted eighth": positions 0, 3, 6, 9, 12, 15. Six dots only. Note that this lands on
beat 1 and on beat 4, and falls between the beats everywhere else.
Row 4, "Sixteenth note": positions 0 through 15, all sixteen.

The dots must line up exactly with those positions relative to the dashed beat lines. Row 3
having exactly six dots, not seven and not eight, is the point of the figure.

Beneath the rows, one line of text, centered, exactly:
"The dotted eighth lands on beats 1 and 4 and between the beats everywhere else."

Use #212121 for the beat numbers, dashed lines and labels. Use #B71C1C for row 1 dots,
#0D47A1 for row 2, #1B5E20 for row 3, #E65100 for row 4.

Do not draw any logo, brand mark, model number, or product photograph. Do not include borders,
frames or title bars. Use American spelling.
```

---

## 06. Mix bus versus master fader

| Field | Value |
|---|---|
| Filename | `mixing-mastering-mix-bus-vs-master-fader-01.png` |
| Folder | `.../Images/mixing-mastering/` |
| Used on | `Mixing & Mastering: Read - The Mix Bus` |
| What is wrong now | The signal flow is correct, but the insert box text is clipped. It reads "Glue compres" and "Broad EC" instead of "Glue compressor" and "Broad EQ", and the two insert boxes overlap each other |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a white background.

Flat vector-style technical illustration. Clean line weights, no gradients, no drop shadows,
no 3D, no photorealism, no watermark, no signature. Do not imitate any real mixing console or
software interface.

Every text label must fit completely inside its box with clear margin on all sides. Size each
box to its text. No label may be clipped, truncated or overlap another box. This is the fault
being corrected, so check it.

Signal flow running left to right.

On the left, five plain rectangles stacked vertically, labeled top to bottom exactly:
"Drums", "Bass", "Guitars", "Keys", "Vocals".

All five have arrows converging into one taller rectangle in the center, labeled on two lines:
"Mix Bus" and beneath it "(stereo aux)".

Above the Mix Bus rectangle, draw two separate non-overlapping boxes side by side, labeled
exactly "Glue comp" and "Broad EQ". Directly beneath those two boxes and above the Mix Bus,
one small caption reading exactly "Inserts are pre fader".

An arrow runs from the Mix Bus to a rectangle labeled "Master Fader". Above it, one box
labeled exactly "Meter only", and beneath that box one small caption reading exactly
"Inserts are post fader".

A final arrow runs from Master Fader to a smaller rectangle labeled "Output".

Fill the frame. Do not leave a large empty area in the lower right.

Use #212121 for all box outlines and text, #F5F5F5 for box fills, and #0D47A1 for the signal
arrows.

Do not draw any logo, brand mark, model number, or product photograph. Do not include borders,
frames, title bars, or caption text outside the diagram. Use American spelling.
```

---

## Two notes for the next batch

**Style drift is the recurring fault.** The six rejected images came back as bright infographic
art with saturated color pills and heavy display type, which does not match anything else in
the course. Every prompt above now names the style exclusions explicitly. Keep that block in
future prompts.

**Transparent backgrounds caused trouble.** Several images came back with transparent
backgrounds and visible edge artifacts around the shapes. All six prompts above ask for a
white background instead, which matches the page wrapper and avoids the artifacting.
