# ChatGPT Image Creation - DAPR 2020 v12

Generated 2026-09-20 for the DAPR 2020 Core Mixing turnkey v12 build.
29 images across 13 topic folders.

Every entry below gives three things: the **name** to save the file as, a **description** of
what the picture must show, and the exact **file path** to drop it into. Save the filename
exactly as written, including the `-01` counter. The pages already reference these paths, so a
correct filename makes the image appear and a wrong one leaves a broken box.

## Before you judge any result

These come back as transparent PNGs. A transparent PNG on a dark background looks broken in a
specific and misleading way: dark labels vanish and the edges speckle. Composite on white
first, which is what a Canvas page actually is (Standards 20.4b).

```
python3 -c "
from PIL import Image; import sys
im=Image.open(sys.argv[1])
bg=Image.new('RGB',im.size,(255,255,255))
bg.paste(im,mask=im.split()[-1]) if im.mode in ('RGBA','LA') else None
(bg if im.mode in ('RGBA','LA') else im.convert('RGB')).save('/tmp/on_white.png')
print('/tmp/on_white.png')" "<the image>"
```

## All 29 at a glance

| # | Name | Description | File path |
|---|---|---|---|
| 1 | `balancing-and-reverb-send-versus-insert-routing-01.png` | Routing diagram contrasting reverb on an insert with reverb on a send and return | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Balancing_and_Reverb/Balancing_and_Reverb__Send_versus_Insert_Routing.png` |
| 2 | `calibration-and-monitoring-gain-staging-chain-01.png` | Gain staging through a channel showing where level is set at each stage | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Calibration_and_Monitoring/Calibration_and_Monitoring__Gain_Staging_Chain.png` |
| 3 | `comping-and-arrangement-crossfade-placement-01.png` | Two waveform joins comparing an edit on the transient with one placed before it | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement/Comping_and_Arrangement__Green_to_Blue_Waveform_Splice_Pair.png` |
| 4 | `comping-and-arrangement-playlist-comp-lanes-01.png` | Playlist lanes with selected regions assembled into a composite take | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement/Comping_and_Arrangement__Playlist_Comp_Lanes.png` |
| 5 | `course-orientation-and-feedback-grade-breakdown-01.png` | Stacked bar showing how the course grade divides across work types | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Course_Orientation_and_Feedback__Grade_Breakdown.png` |
| 6 | `course-orientation-and-feedback-weekly-rhythm-01.png` | Diagram of the weekly rhythm from module opening to Friday deadline | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Course_Orientation_and_Feedback__Weekly_Rhythm.png` |
| 7 | `course-orientation-and-feedback-worksheet-to-pdf-flow-01.png` | Four-step flow from copying a worksheet block to uploading a PDF | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Course_Orientation_and_Feedback__Worksheet_to_Pdf_Flow.png` |
| 8 | `dynamic-effects-attack-too-fast-transient-loss-01.png` | Two drum waveforms comparing a preserved transient with one flattened by a fast attack | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Dynamic_Effects/Dynamic_Effects__Attack_Too_Fast_Transient_Loss.png` |
| 9 | `dynamic-effects-side-chain-filter-kick-pumping-01.png` | Gain reduction traces with and without a high-pass filter on the side-chain | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Dynamic_Effects/Dynamic_Effects__Side_Chain_Filter_Kick_Pumping.png` |
| 10 | `focus-and-balance-channel-strip-anatomy-01.png` | Labeled diagram of a mixer channel strip from input to output | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance/Focus_and_Balance__Channel_Strip_Anatomy.png` |
| 11 | `focus-and-balance-five-pass-mix-order-01.png` | Five-step flow showing the order of a mix pass | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance/Focus_and_Balance__Five_Pass_Mix_Order.png` |
| 12 | `focus-and-balance-solo-versus-context-01.png` | Two panels contrasting a decision made in solo with the same decision in context | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance/Focus_and_Balance__Single_Blue_Burst_beside_Stacked_Tracks.png` |
| 13 | `mid-side-technique-ms-matrix-signal-flow-01.png` | Signal flow of a mid-side encode and decode matrix | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mid-Side_Technique/Mid-Side_Technique__Ms_Matrix_Signal_Flow.png` |
| 14 | `mix-acoustics-first-reflection-points-01.png` | Overhead plan of a control room with first reflection paths traced | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mix_Acoustics/Mix_Acoustics__First_Reflection_Points.png` |
| 15 | `mix-acoustics-thin-foam-versus-broadband-01.png` | Cross-section comparing thin foam with a deep broadband absorber and their effect by frequency | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mix_Acoustics/Mix_Acoustics__Thin_Foam_versus_Broadband.png` |
| 16 | `professional-practice-bounce-specification-01.png` | Diagram of the four fields that define a bounce specification | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Bounce_Specification.png` |
| 17 | `professional-practice-bounce-truncation-01.png` | Two waveforms comparing a full bounce with one truncated before the tail ends | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Bounce_Truncation.png` |
| 18 | `professional-practice-delivery-verification-checklist-01.png` | Checklist of the verification steps before a mix is submitted | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Delivery_Verification_Checklist.png` |
| 19 | `professional-practice-multitrack-download-flow-01.png` | Flow from downloading a multitrack archive to an open session | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Multitrack_Download_Flow.png` |
| 20 | `professional-practice-network-drive-path-01.png` | Flat diagram of connecting to a network share and locating the course folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Network_Drive_Path.png` |
| 21 | `professional-practice-session-delivery-package-01.png` | Folder structure of a complete session delivery package | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Session_Delivery_Package.png` |
| 22 | `spectral-effects-and-eq-boost-wide-cut-narrow-01.png` | EQ curve comparing a wide musical boost with a narrow surgical cut | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Spectral_Effects_and_EQ/Spectral_Effects_and_EQ__Boost_Wide_Cut_Narrow.png` |
| 23 | `timing-elastic-audio-warp-markers-01.png` | Waveform with warp markers showing a transient pulled onto the grid | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing/Timing__Elastic_Audio_Warp_Markers.png` |
| 24 | `timing-quantize-strength-comparison-01.png` | Three waveform rows comparing original, partial and full quantization against a grid | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing/Timing__Waveform_Rows_against_Grid_Lines.png` |
| 25 | `tuning-correction-amount-comparison-01.png` | Pitch curves at three correction amounts | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Tuning/Tuning__Correction_Amount_Comparison_Curves.png` |
| 26 | `tuning-correction-speed-scoop-01.png` | Pitch curves comparing a natural scoop into a note with one removed by fast correction | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Tuning/Tuning__Correction_Speed_Scoop.png` |
| 27 | `tuning-scale-and-target-notes-01.png` | Piano roll grid showing target notes constrained to a scale | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Tuning/Tuning__Scale_and_Target_Notes_Curves.png` |
| 28 | `delay-and-stereo-enhancements-mono-collapse-check-01.png` | Stereo signal shown wide then summed to mono with the width cancelling | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Delay_and_Stereo_Enhancements/Delay_and_Stereo_Enhancements__Mono_Collapse_Check.png` |
| 29 | `master-buss-processing-and-endgame-headroom-on-delivery-01.png` | Level meter comparison showing a mix with headroom and one pushed into the ceiling | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Master_Bus_Processing_and_Endgame/Master_Bus_Processing_and_Endgame__Headroom_on_Delivery.png` |

## Create the folders first

Three of these folders do not exist yet. One command makes all of them:

```
mkdir -p "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Balancing_and_Reverb" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Calibration_and_Monitoring" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Dynamic_Effects" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mid_Side_Technique" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mix_Acoustics" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Spectral_Effects_and_EQ" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/delay-and-stereo-enhancements" "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/master-buss-processing-and-endgame"
```

## Push when you are done

Per Standards 20.4c I write images into the repo and you commit and push them.

```
cd "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas" && git add Classes/DAPR-2020--Core_Mixing && git commit -m "DAPR 2020 v12: generated course figures" && git push
```

## The prompts

### 1. `balancing-and-reverb-send-versus-insert-routing-01.png`

| | |
|---|---|
| **Name** | `balancing-and-reverb-send-versus-insert-routing-01.png` |
| **Description** | Routing diagram contrasting reverb on an insert with reverb on a send and return |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Balancing_and_Reverb/Balancing_and_Reverb__Send_versus_Insert_Routing.png` |
| **Used on** | Reverb: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Balancing_and_Reverb/Send_versus_Insert_Routing.png` |

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

### 2. `calibration-and-monitoring-gain-staging-chain-01.png`

| | |
|---|---|
| **Name** | `calibration-and-monitoring-gain-staging-chain-01.png` |
| **Description** | Gain staging through a channel showing where level is set at each stage |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Calibration_and_Monitoring/Calibration_and_Monitoring__Gain_Staging_Chain.png` |
| **Used on** | Session Preparation: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Calibration_and_Monitoring/Gain_Staging_Chain.png` |

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

### 3. `comping-and-arrangement-crossfade-placement-01.png`

| | |
|---|---|
| **Name** | `comping-and-arrangement-crossfade-placement-01.png` |
| **Description** | Two waveform joins comparing an edit on the transient with one placed before it |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement/Comping_and_Arrangement__Green_to_Blue_Waveform_Splice_Pair.png` |
| **Used on** | Comping: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Comping_and_Arrangement/Green_to_Blue_Waveform_Splice_Pair.png` |

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

### 4. `comping-and-arrangement-playlist-comp-lanes-01.png`

| | |
|---|---|
| **Name** | `comping-and-arrangement-playlist-comp-lanes-01.png` |
| **Description** | Playlist lanes with selected regions assembled into a composite take |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Comping_and_Arrangement/Comping_and_Arrangement__Playlist_Comp_Lanes.png` |
| **Used on** | Comping: The Controls and the Decisions |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Comping_and_Arrangement/Playlist_Comp_Lanes.png` |

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

### 5. `course-orientation-and-feedback-grade-breakdown-01.png`

| | |
|---|---|
| **Name** | `course-orientation-and-feedback-grade-breakdown-01.png` |
| **Description** | Stacked bar showing how the course grade divides across work types |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Course_Orientation_and_Feedback__Grade_Breakdown.png` |
| **Used on** | Orientation: 1B) Course Description, Learning Outcomes, and Requirements |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Grade_Breakdown.png` |

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

### 6. `course-orientation-and-feedback-weekly-rhythm-01.png`

| | |
|---|---|
| **Name** | `course-orientation-and-feedback-weekly-rhythm-01.png` |
| **Description** | Diagram of the weekly rhythm from module opening to Friday deadline |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Course_Orientation_and_Feedback__Weekly_Rhythm.png` |
| **Used on** | Course Schedule: Week by Week |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/Course_Orientation_and_Feedback/Weekly_Rhythm.png` |

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

### 7. `course-orientation-and-feedback-worksheet-to-pdf-flow-01.png`

| | |
|---|---|
| **Name** | `course-orientation-and-feedback-worksheet-to-pdf-flow-01.png` |
| **Description** | Four-step flow from copying a worksheet block to uploading a PDF |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Course_Orientation_and_Feedback/Course_Orientation_and_Feedback__Worksheet_to_Pdf_Flow.png` |
| **Used on** | Orientation: 3C) How to Make a PDF |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Course_Orientation_and_Feedback/Worksheet_to_Pdf_Flow.png` |

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

### 8. `dynamic-effects-attack-too-fast-transient-loss-01.png`

| | |
|---|---|
| **Name** | `dynamic-effects-attack-too-fast-transient-loss-01.png` |
| **Description** | Two drum waveforms comparing a preserved transient with one flattened by a fast attack |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Dynamic_Effects/Dynamic_Effects__Attack_Too_Fast_Transient_Loss.png` |
| **Used on** | Compression: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Dynamic_Effects/Attack_Too_Fast_Transient_Loss.png` |

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

### 9. `dynamic-effects-side-chain-filter-kick-pumping-01.png`

| | |
|---|---|
| **Name** | `dynamic-effects-side-chain-filter-kick-pumping-01.png` |
| **Description** | Gain reduction traces with and without a high-pass filter on the side-chain |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Dynamic_Effects/Dynamic_Effects__Side_Chain_Filter_Kick_Pumping.png` |
| **Used on** | Side-Chains: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Dynamic_Effects/Side_Chain_Filter_Kick_Pumping.png` |

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

### 10. `focus-and-balance-channel-strip-anatomy-01.png`

| | |
|---|---|
| **Name** | `focus-and-balance-channel-strip-anatomy-01.png` |
| **Description** | Labeled diagram of a mixer channel strip from input to output |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance/Focus_and_Balance__Channel_Strip_Anatomy.png` |
| **Used on** | Focus and Balance: Mix-Window Procedure Guide |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/Focus_and_Balance/Channel_Strip_Anatomy.png` |

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

### 11. `focus-and-balance-five-pass-mix-order-01.png`

| | |
|---|---|
| **Name** | `focus-and-balance-five-pass-mix-order-01.png` |
| **Description** | Five-step flow showing the order of a mix pass |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance/Focus_and_Balance__Five_Pass_Mix_Order.png` |
| **Used on** | A Repeatable Order of Operations |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Focus_and_Balance/Five_Pass_Mix_Order.png` |

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

### 12. `focus-and-balance-solo-versus-context-01.png`

| | |
|---|---|
| **Name** | `focus-and-balance-solo-versus-context-01.png` |
| **Description** | Two panels contrasting a decision made in solo with the same decision in context |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Focus_and_Balance/Focus_and_Balance__Single_Blue_Burst_beside_Stacked_Tracks.png` |
| **Used on** | Balance: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Focus_and_Balance/Single_Blue_Burst_beside_Stacked_Tracks.png` |

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

### 13. `mid-side-technique-ms-matrix-signal-flow-01.png`

| | |
|---|---|
| **Name** | `mid-side-technique-ms-matrix-signal-flow-01.png` |
| **Description** | Signal flow of a mid-side encode and decode matrix |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mid-Side_Technique/Mid-Side_Technique__Ms_Matrix_Signal_Flow.png` |
| **Used on** | MS (Mid-Side) Matrix |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/Calibration_and_Monitoring/Ms_Matrix_Signal_Flow.png` |

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

### 14. `mix-acoustics-first-reflection-points-01.png`

| | |
|---|---|
| **Name** | `mix-acoustics-first-reflection-points-01.png` |
| **Description** | Overhead plan of a control room with first reflection paths traced |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mix_Acoustics/Mix_Acoustics__First_Reflection_Points.png` |
| **Used on** | What the Room Does to What You Hear |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Mix_Acoustics/First_Reflection_Points.png` |

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

### 15. `mix-acoustics-thin-foam-versus-broadband-01.png`

| | |
|---|---|
| **Name** | `mix-acoustics-thin-foam-versus-broadband-01.png` |
| **Description** | Cross-section comparing thin foam with a deep broadband absorber and their effect by frequency |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Mix_Acoustics/Mix_Acoustics__Thin_Foam_versus_Broadband.png` |
| **Used on** | Acoustics: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Mix_Acoustics/Thin_Foam_versus_Broadband.png` |

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

### 16. `professional-practice-bounce-specification-01.png`

| | |
|---|---|
| **Name** | `professional-practice-bounce-specification-01.png` |
| **Description** | Diagram of the four fields that define a bounce specification |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Bounce_Specification.png` |
| **Used on** | Final Mix: Delivery and Verification Procedure |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/Final_Mix_and_Final_Exam/Professional_Practice_Bounce_Specification.png` |

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

### 17. `professional-practice-bounce-truncation-01.png`

| | |
|---|---|
| **Name** | `professional-practice-bounce-truncation-01.png` |
| **Description** | Two waveforms comparing a full bounce with one truncated before the tail ends |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Bounce_Truncation.png` |
| **Used on** | Delivery: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Bounce_Truncation.png` |

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

### 18. `professional-practice-delivery-verification-checklist-01.png`

| | |
|---|---|
| **Name** | `professional-practice-delivery-verification-checklist-01.png` |
| **Description** | Checklist of the verification steps before a mix is submitted |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Delivery_Verification_Checklist.png` |
| **Used on** | Delivery: Verifying Before You Submit |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Delivery_Verification_Checklist.png` |

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

### 19. `professional-practice-multitrack-download-flow-01.png`

| | |
|---|---|
| **Name** | `professional-practice-multitrack-download-flow-01.png` |
| **Description** | Flow from downloading a multitrack archive to an open session |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Multitrack_Download_Flow.png` |
| **Used on** | Sessions: Free DAW Session Track Downloads |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Multitrack_Download_Flow.png` |

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

### 20. `professional-practice-network-drive-path-01.png`

| | |
|---|---|
| **Name** | `professional-practice-network-drive-path-01.png` |
| **Description** | Flat diagram of connecting to a network share and locating the course folder |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Network_Drive_Path.png` |
| **Used on** | Sessions: Accessing Course Files on the Network Drive (DGM Assets) |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Network_Drive_Path.png` |

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

### 21. `professional-practice-session-delivery-package-01.png`

| | |
|---|---|
| **Name** | `professional-practice-session-delivery-package-01.png` |
| **Description** | Folder structure of a complete session delivery package |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Presentations_and_Sessions__Professional_Practice_Session_Delivery_Package.png` |
| **Used on** | Delivering Work Other People Can Open |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Professional_Practice_Presentations_and_Sessions/Professional_Practice_Session_Delivery_Package.png` |

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

### 22. `spectral-effects-and-eq-boost-wide-cut-narrow-01.png`

| | |
|---|---|
| **Name** | `spectral-effects-and-eq-boost-wide-cut-narrow-01.png` |
| **Description** | EQ curve comparing a wide musical boost with a narrow surgical cut |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Spectral_Effects_and_EQ/Spectral_Effects_and_EQ__Boost_Wide_Cut_Narrow.png` |
| **Used on** | EQ: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Spectral_Effects_and_EQ/Boost_Wide_Cut_Narrow.png` |

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

### 23. `timing-elastic-audio-warp-markers-01.png`

| | |
|---|---|
| **Name** | `timing-elastic-audio-warp-markers-01.png` |
| **Description** | Waveform with warp markers showing a transient pulled onto the grid |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing/Timing__Elastic_Audio_Warp_Markers.png` |
| **Used on** | Timing: The Controls and What They Cost |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Timing/Elastic_Audio_Warp_Markers.png` |

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

### 24. `timing-quantize-strength-comparison-01.png`

| | |
|---|---|
| **Name** | `timing-quantize-strength-comparison-01.png` |
| **Description** | Three waveform rows comparing original, partial and full quantization against a grid |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Timing/Timing__Waveform_Rows_against_Grid_Lines.png` |
| **Used on** | Timing: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Timing/Waveform_Rows_against_Grid_Lines.png` |

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

### 25. `tuning-correction-amount-comparison-01.png`

| | |
|---|---|
| **Name** | `tuning-correction-amount-comparison-01.png` |
| **Description** | Pitch curves at three correction amounts |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Tuning/Tuning__Correction_Amount_Comparison_Curves.png` |
| **Used on** | Tuning: What to Correct and What to Leave |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Tuning/Correction_Amount_Comparison_Curves.png` |

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

### 26. `tuning-correction-speed-scoop-01.png`

| | |
|---|---|
| **Name** | `tuning-correction-speed-scoop-01.png` |
| **Description** | Pitch curves comparing a natural scoop into a note with one removed by fast correction |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Tuning/Tuning__Correction_Speed_Scoop.png` |
| **Used on** | Tuning: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Tuning/Correction_Speed_Scoop.png` |

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

### 27. `tuning-scale-and-target-notes-01.png`

| | |
|---|---|
| **Name** | `tuning-scale-and-target-notes-01.png` |
| **Description** | Piano roll grid showing target notes constrained to a scale |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Tuning/Tuning__Scale_and_Target_Notes_Curves.png` |
| **Used on** | Tuning: Pitch-Correction Procedure Guide |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/Tuning/Scale_and_Target_Notes_Curves.png` |

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

### 28. `delay-and-stereo-enhancements-mono-collapse-check-01.png`

| | |
|---|---|
| **Name** | `delay-and-stereo-enhancements-mono-collapse-check-01.png` |
| **Description** | Stereo signal shown wide then summed to mono with the width cancelling |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Delay_and_Stereo_Enhancements/Delay_and_Stereo_Enhancements__Mono_Collapse_Check.png` |
| **Used on** | Delay and Width: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Delay_and_Stereo_Enhancements/Mono_Collapse_Check.png` |

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

### 29. `master-buss-processing-and-endgame-headroom-on-delivery-01.png`

| | |
|---|---|
| **Name** | `master-buss-processing-and-endgame-headroom-on-delivery-01.png` |
| **Description** | Level meter comparison showing a mix with headroom and one pushed into the ceiling |
| **File path** | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Images/Master_Bus_Processing_and_Endgame/Master_Bus_Processing_and_Endgame__Headroom_on_Delivery.png` |
| **Used on** | Master Buss: Common Mistakes and How to Hear Them |
| **Live URL after push** | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2020--Core_Mixing/_unplaced/Master_Bus_Processing_and_Endgame/Headroom_on_Delivery.png` |

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

