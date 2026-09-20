# DAPR 2020 Core Mixing - ChatGPT Image Prompts

29 images. Paste each block below into ChatGPT, save the result under the filename given,
and put it in the folder given. Nothing else in this file needs reading.

---

## Do this once first

Create the folders. Three do not exist yet.

```
mkdir -p "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Balancing_and_Reverb" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Calibration_and_Monitoring" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Dynamic_Effects" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mid_Side_Technique" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mix_Acoustics" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Spectral_Effects_and_EQ" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/delay-and-stereo-enhancements" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/master-buss-processing-and-endgame"
```

## Do this once at the end

```
cd "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas" && git add Classes/DAPR-2020--Core_Mixing && git commit -m "DAPR 2020: generated course figures" && git push
```

## Check any result that looks broken

These come back as transparent PNGs. On a dark background they look like artifacting when they are fine.

```
python3 -c "
from PIL import Image; import sys
im=Image.open(sys.argv[1])
bg=Image.new('RGB',im.size,(255,255,255))
bg.paste(im,mask=im.split()[-1]) if im.mode in ('RGBA','LA') else None
(bg if im.mode in ('RGBA','LA') else im.convert('RGB')).save('/tmp/on_white.png')
print('/tmp/on_white.png')" "<the image>"
```

---

## 1. balancing-and-reverb-send-versus-insert-routing-01.png

Save as: `balancing-and-reverb-send-versus-insert-routing-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Balancing_and_Reverb/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Two routing diagrams side by side. Left, labeled Insert: one track passing through a reverb block to the mix buss. Right, labeled Send and Return: three tracks feeding one aux return carrying the reverb, with the dry signals also reaching the mix buss.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 2. calibration-and-monitoring-gain-staging-chain-01.png

Save as: `calibration-and-monitoring-gain-staging-chain-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Calibration_and_Monitoring/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Left to right signal chain: source, clip gain, input trim, insert chain, fader, buss, master. A small level indicator under each stage showing healthy level maintained throughout.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 3. comping-and-arrangement-crossfade-placement-01.png

Save as: `comping-and-arrangement-crossfade-placement-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Two waveform joins side by side. Left labeled On the Transient shows the edit line falling on a sharp attack with a click symbol. Right labeled Before the Transient shows the edit in the quiet preceding it with a smooth crossfade.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 4. comping-and-arrangement-playlist-comp-lanes-01.png

Save as: `comping-and-arrangement-playlist-comp-lanes-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Four stacked take lanes labeled Take 1 to Take 4 with different segments highlighted in each, and a fifth Comp lane below assembling the highlighted segments into one continuous take.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 5. course-orientation-and-feedback-grade-breakdown-01.png

Save as: `course-orientation-and-feedback-grade-breakdown-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

A single horizontal stacked bar divided into four labeled segments: Module Assignments, Module Quizzes, Projects, Final Exam. Labels only, no numbers baked in.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 6. course-orientation-and-feedback-weekly-rhythm-01.png

Save as: `course-orientation-and-feedback-weekly-rhythm-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

A horizontal week strip from Monday to Friday. Monday marked Module Opens, Friday marked Due 9:00 a.m. Arrows showing reading, practice and submission across the week.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 7. course-orientation-and-feedback-worksheet-to-pdf-flow-01.png

Save as: `course-orientation-and-feedback-worksheet-to-pdf-flow-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Left to right four steps with flat icons: select and copy the worksheet block, paste into a document, add screenshots, export as PDF and upload. Label each step.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 8. dynamic-effects-attack-too-fast-transient-loss-01.png

Save as: `dynamic-effects-attack-too-fast-transient-loss-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Dynamic_Effects/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Two drum waveforms stacked, same hit, labeled Slow Attack and Fast Attack. The top keeps a tall sharp initial spike; the bottom has that spike flattened while the body stays the same height. Annotate the flattened region.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 9. dynamic-effects-side-chain-filter-kick-pumping-01.png

Save as: `dynamic-effects-side-chain-filter-kick-pumping-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Dynamic_Effects/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Two gain reduction traces over time. Top labeled No Side-Chain Filter dips deeply on every kick hit. Bottom labeled High-Pass at 100 Hz shows much smaller, steadier movement. Kick hits marked along the bottom.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 10. focus-and-balance-channel-strip-anatomy-01.png

Save as: `focus-and-balance-channel-strip-anatomy-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

A single vertical mixer channel strip, generic and not any specific product, labeled top to bottom: input, inserts, sends, pan, solo and mute, fader, output assignment, meter.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 11. focus-and-balance-five-pass-mix-order-01.png

Save as: `focus-and-balance-five-pass-mix-order-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Left to right five-step flow, each step a labeled box: Balance, Subtractive, Dynamics, Placement, Automation. A single arrow through all five.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 12. focus-and-balance-solo-versus-context-01.png

Save as: `focus-and-balance-solo-versus-context-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Two panels. Left labeled In Solo shows one waveform alone. Right labeled In Context shows the same waveform layered with five others, partly masked. Same element highlighted in both.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 13. mid-side-technique-ms-matrix-signal-flow-01.png

Save as: `mid-side-technique-ms-matrix-signal-flow-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mid_Side_Technique/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Left to right flow. Left and Right inputs feed a sum block labeled Mid and a difference block labeled Side, then a decode stage returning Left and Right. Label M equals L plus R and S equals L minus R.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 14. mix-acoustics-first-reflection-points-01.png

Save as: `mix-acoustics-first-reflection-points-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mix_Acoustics/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Overhead plan of a rectangular control room. Listening position centered on the short wall, two monitors forming an equilateral triangle, dashed lines tracing first reflection paths off each side wall, the ceiling and the desk. Label the four reflection points.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 15. mix-acoustics-thin-foam-versus-broadband-01.png

Save as: `mix-acoustics-thin-foam-versus-broadband-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mix_Acoustics/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Two wall cross-sections side by side, thin foam panel and deep broadband absorber, each with a small absorption-versus-frequency curve beneath. The thin panel curve rises only at high frequencies; the deep one covers low and high.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 16. professional-practice-bounce-specification-01.png

Save as: `professional-practice-bounce-specification-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Four labeled boxes in a row: File Type, Sample Rate, Bit Depth, Mono or Stereo. Beneath, a single line showing the resulting file with a correct name.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 17. professional-practice-bounce-truncation-01.png

Save as: `professional-practice-bounce-truncation-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Two waveforms of the same mix. Top labeled Complete shows the reverb tail decaying to silence. Bottom labeled Truncated cuts off abruptly mid-tail with the cut marked.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 18. professional-practice-delivery-verification-checklist-01.png

Save as: `professional-practice-delivery-verification-checklist-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

A vertical checklist with flat checkbox icons: clear all solos and mutes, check peak level under 0 dBFS, bounce, play the bounced file end to end, check in mono, name to convention, upload.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 19. professional-practice-multitrack-download-flow-01.png

Save as: `professional-practice-multitrack-download-flow-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Four steps: download archive, expand it, import into a new session, set the session sample rate to match. Flat icons, labeled.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 20. professional-practice-network-drive-path-01.png

Save as: `professional-practice-network-drive-path-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Three steps left to right: a computer icon, a network share icon, and a folder tree with a course assets folder highlighted. Label each step.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 21. professional-practice-session-delivery-package-01.png

Save as: `professional-practice-session-delivery-package-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

A folder tree: a project folder containing a session file, an Audio Files folder, a Bounces folder holding the master, and a documentation PDF. Label each.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 22. spectral-effects-and-eq-boost-wide-cut-narrow-01.png

Save as: `spectral-effects-and-eq-boost-wide-cut-narrow-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Spectral_Effects_and_EQ/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

A single frequency response graph, 20 Hz to 20 kHz logarithmic, showing two curves: a wide gentle boost of a few dB around 3 kHz labeled Boost Wide, and a narrow deep cut around 400 Hz labeled Cut Narrow.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 23. timing-elastic-audio-warp-markers-01.png

Save as: `timing-elastic-audio-warp-markers-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

A drum waveform on a timeline grid with three warp markers. One transient clearly ahead of the beat, an arrow showing it moved onto the gridline, surrounding audio stretching to accommodate.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 24. timing-quantize-strength-comparison-01.png

Save as: `timing-quantize-strength-comparison-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Three stacked waveform rows against the same vertical gridlines, labeled Original, 60 percent, and 100 percent. Transients progressively move onto the gridlines; the bottom row sits exactly on them.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 25. tuning-correction-amount-comparison-01.png

Save as: `tuning-correction-amount-comparison-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Three pitch-over-time curves stacked, labeled No Correction, Partial, and Full. The top wanders around the target line, the middle sits close with movement intact, the bottom is a flat line on target.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 26. tuning-correction-speed-scoop-01.png

Save as: `tuning-correction-speed-scoop-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Two pitch-over-time curves stacked. Top labeled Slow Speed shows a curve sliding up into a held note. Bottom labeled Fast Speed shows the same note snapping instantly to a flat horizontal line.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 27. tuning-scale-and-target-notes-01.png

Save as: `tuning-scale-and-target-notes-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

A vertical piano keyboard on the left and a horizontal time grid to the right. Notes in the selected scale highlighted as target lines; notes outside the scale shown greyed out.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 28. delay-and-stereo-enhancements-mono-collapse-check-01.png

Save as: `delay-and-stereo-enhancements-mono-collapse-check-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/delay-and-stereo-enhancements/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Two panels. Left labeled Stereo shows a wide stereo image with left and right waveforms out of phase. Right labeled Summed to Mono shows the same content largely cancelling to a much smaller waveform. Arrow between them labeled Sum to mono.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
## 29. master-buss-processing-and-endgame-headroom-on-delivery-01.png

Save as: `master-buss-processing-and-endgame-headroom-on-delivery-01.png`
Put in: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/master-buss-processing-and-endgame/`

```
Create a 1600 x 900 pixel PNG with a fully transparent background.

Two vertical level meters side by side. Left labeled With Headroom peaks below the top with space remaining. Right labeled Pushed peaks flat against the ceiling with a clip indicator lit.

Palette: dark text #212121, primary green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300.
Style: flat vector-style illustration, clean even line weights, no gradients, no drop
shadows, no 3D, no photorealism, no watermark, no signature.
Do not draw: any manufacturer logo or brand mark, any model number, any software
interface or screenshot, decorative people, borders, frames, title bars, or caption
text baked into the image.
```
