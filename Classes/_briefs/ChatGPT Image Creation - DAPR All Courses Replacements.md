# ChatGPT Image Creation - DAPR All Courses Replacements

Written 2026-09-23. Every image below is on disk now but looks wrong: a watermark or a third party credit, a resolution too low for a Canvas page, or a made up software screen that Canvas Standards 20.1 rule 3 does not allow.

**How to use this file**

1. Run each prompt on its own in ChatGPT. One image per prompt.
2. Save the result over the exact file shown, with the exact filename. The folder and the name are already right, so the pages and `Link_Map.tsv` need no change.
3. ChatGPT returns PNG. Where the destination ends in `.jpg`, save the PNG anywhere, then run the `sips` line under that image. It's done when the `%` prompt comes back.
4. Check every label and line before you keep it. Regenerate rather than hand fix. Schematic symbols especially: compare against the old file before you overwrite it.
5. When you finish a batch, tell me or push the repo so the new pictures go live.

**Not for ChatGPT (real products must be sourced, per 20.1 rule 3):** `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Adam_Audio_Monitors.jpg` is a 225 pixel product photo. Replace it with a photo of the real monitors (your own shot or the manufacturer's press image) at 1600 pixels wide, same filename.

---

## Image 01. DAPR 2000: Cardioid polar chart (replaces a SoundGuys watermarked image)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics_Selection_and_Stereo_Techniques/Cardioid_Polar_Chart.png
```

**Prompt:**

```
Create a 1600 x 1600 pixel PNG with a fully transparent background. A clean microphone polar plot seen flat from above: five evenly spaced concentric circles and twelve thin radial lines every 30 degrees in light gray, with a single bold cardioid pickup curve in blue #0D47A1, widest at the top (0 degrees) and pinched to a point at the bottom (180 degrees). Flat technical diagram, crisp even line weights. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 02. DAPR 2000: Frequency and wavelength (replaces an Encyclopaedia Britannica image)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Frequency_and_Wavelength.png
```

**Prompt:**

```
Create a 1600 x 900 pixel PNG with a fully transparent background. Two horizontal sine waves stacked, each on its own thin dark center line #212121. Top wave in blue #0D47A1 with many tightly packed cycles (high frequency). Bottom wave in green #1B5E20 with the same height but only three wide cycles (low frequency). Above each wave, one thin bracket spanning exactly one crest to the next crest, showing a short wavelength on top and a long wavelength below. Flat technical diagram. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 03. DAPR 2000: Omnidirectional pickup sphere, 3D (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics_Selection_and_Stereo_Techniques/Polar_Pattern.jpg
```

ChatGPT gives a PNG. Convert it into place (drag the downloaded PNG into Terminal where it says the path):

```
sips -s format jpeg -s formatOptions 88 "PASTE_DOWNLOADED_PNG_PATH" --out "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics_Selection_and_Stereo_Techniques/Polar_Pattern.jpg"
```

**Prompt:**

```
Create a 1600 x 1600 pixel photorealistic image on a smooth dark gray studio background. A generic black side-address studio condenser microphone standing upright, centered inside a large translucent glass-like wireframe sphere that surrounds it evenly on all sides, showing equal pickup in every direction. Soft studio lighting, shallow depth of field. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 04. DAPR 2000: Cardioid pickup balloon, 3D (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics_Selection_and_Stereo_Techniques/Polar_Pattern_Alt.jpg
```

ChatGPT gives a PNG. Convert it into place (drag the downloaded PNG into Terminal where it says the path):

```
sips -s format jpeg -s formatOptions 88 "PASTE_DOWNLOADED_PNG_PATH" --out "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics_Selection_and_Stereo_Techniques/Polar_Pattern_Alt.jpg"
```

**Prompt:**

```
Create a 1600 x 1600 pixel photorealistic image on a smooth dark gray studio background. A generic black side-address studio condenser microphone standing upright inside a translucent glass-like wireframe pickup shape that is a 3D cardioid: a large rounded lobe in front of the microphone face, shrinking to a dimple directly behind it. Soft studio lighting, shallow depth of field. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 05. DAPR 2000: Supercardioid polar chart (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics_Selection_and_Stereo_Techniques/Polar_Pattern_Supercardioid.png
```

**Prompt:**

```
Create a 1600 x 1600 pixel PNG with a fully transparent background. A clean microphone polar plot seen flat from above: five evenly spaced concentric circles and twelve thin radial lines every 30 degrees in light gray, with a single bold supercardioid curve in dark #212121: a large front lobe toward the top (0 degrees), deep nulls near 125 and 235 degrees, and a small rear lobe at the bottom (180 degrees). Flat technical diagram. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.

Save the same result a second time as `Polar_Pattern_Unlabeled.png` in the same folder (it is the same chart).
```

---

## Image 06. DAPR 2000: Two waves 90 degrees apart, quiz distractor (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Digital_Audio__The_Digital_Domain/Phase_Offset_Distractor.png
```

**Prompt:**

```
Create a 1600 x 900 pixel PNG with a fully transparent background. Two sine waves of identical height and length on one shared horizontal center line: one in orange #993300, the second in gray, shifted a quarter cycle to the right. Two full cycles each. Flat technical diagram. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 07. DAPR 2000: Sampled waveform, fine and coarse, quiz distractor (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Digital_Audio__The_Digital_Domain/Sampled_Waveform_Distractor.png
```

**Prompt:**

```
Create a 1600 x 900 pixel PNG with a fully transparent background. Two side by side panels, each showing one cycle of a sine wave drawn as vertical sample stems with a dot at the top of each stem, in blue #0D47A1. Left panel: many closely spaced stems that trace the curve smoothly. Right panel: only a few widely spaced stems that make a blocky staircase outline. Flat technical diagram. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 08. DAPR 2255: Assorted battery types (low resolution photo with brand names)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Batteries/Types_Assorted.jpg
```

ChatGPT gives a PNG. Convert it into place (drag the downloaded PNG into Terminal where it says the path):

```
sips -s format jpeg -s formatOptions 88 "PASTE_DOWNLOADED_PNG_PATH" --out "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Batteries/Types_Assorted.jpg"
```

**Prompt:**

```
Create a 1600 x 900 pixel photorealistic product photograph on a seamless light gray background. Assorted plain unbranded batteries laid out left to right from smallest to largest: a coin cell, AAA, AA, C, D, a 9 volt battery, and a rectangular rechargeable lithium pack. Plain metallic and matte wraps with no printing. Soft studio lighting, gentle shadows, shallow depth of field. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 09. DAPR 3255: Relay schematic symbol (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Final_Exam/Relays.png
```

**Prompt:**

```
Create a 1200 x 1200 pixel PNG with a fully transparent background. The standard electronic schematic symbol for a single pole double throw relay: a coil drawn as a row of loops on the left, a dashed line linking it to a switch arm on the right that sits between two contacts. Uniform line weight in red #B71C1C with small open circles at the four terminal ends. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated. Draw only the standard symbol; do not invent extra parts.
```

---

## Image 10. DAPR 3255: Motor schematic symbol (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Final_Exam/Motors.png
```

**Prompt:**

```
Create a 1200 x 1200 pixel PNG with a fully transparent background. The standard electronic schematic symbol for a DC motor: a circle with one lead going up and one lead going down, each ending in a small open circle. Inside the circle, the single letter "M" (the only text allowed). Uniform line weight in red #B71C1C. No other text.
```

---

## Image 11. DAPR 3255: Diode schematic symbol (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Final_Exam/Diode.png
```

**Prompt:**

```
Create a 1200 x 600 pixel PNG with a fully transparent background. The standard schematic symbol for a diode: a filled triangle pointing right into a straight vertical bar, with a horizontal lead on each side ending in a small open circle. Uniform line weight in red #B71C1C. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 12. DAPR 3255: SPST switch schematic symbol (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Final_Exam/Switch_SPST.png
```

**Prompt:**

```
Create a 1200 x 600 pixel PNG with a fully transparent background. The standard schematic symbol for a single pole single throw switch: two small open circle contacts on a horizontal line with the switch arm hinged at the left contact and angled up and open, not touching the right contact. Uniform line weight in red #B71C1C. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 13. DAPR 3255: DPDT switch schematic symbol (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Final_Exam/Switches_DPDT.png
```

**Prompt:**

```
Create a 1200 x 1600 pixel PNG with a fully transparent background. The standard schematic symbol for a double pole double throw switch: two identical switch arms stacked vertically, each hinged at a common contact on the left and able to touch either of two contacts on the right, joined by a vertical dashed line showing they move together. Small open circles at all six terminals. Uniform line weight in red #B71C1C. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 14. DAPR 3255: Center tapped transformer schematic symbol (low resolution original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Final_Exam/Transformer_Center_Tapped.png
```

**Prompt:**

```
Create a 1200 x 1200 pixel PNG with a fully transparent background. The standard schematic symbol for a center tapped transformer: a primary coil of four loops on the left, two parallel vertical core lines in the middle, a secondary coil of four loops on the right with a third lead leaving from the exact middle of the secondary. Uniform line weight in dark #212121. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 15. DAPR 3340: Quadraphonic speaker layout (tiny original)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Introduction_to_Surround_and_Multichannel_Audio/Quadraphonic_Speaker_Layout.png
```

**Prompt:**

```
Create a 1600 x 1200 pixel PNG with a fully transparent background. A top down diagram of a listening room: a simple head seen from above at the exact center, and four identical loudspeakers seen from above at the four corners of a square around it, each angled to face the head. Thin dashed lines from each speaker to the head. Speakers in blue #0D47A1, head in dark #212121. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 16. DAPR 3345: FMOD module banner (current one shows a fake DAW screen)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/FMOD__Implementation_in_FMOD_Studio/Implementation_Desk_Banner.jpg
```

ChatGPT gives a PNG. Convert it into place (drag the downloaded PNG into Terminal where it says the path):

```
sips -s format jpeg -s formatOptions 88 "PASTE_DOWNLOADED_PNG_PATH" --out "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/FMOD__Implementation_in_FMOD_Studio/Implementation_Desk_Banner.jpg"
```

**Prompt:**

```
Create a 1942 x 809 pixel photorealistic image. A dim game audio implementation desk at night: a keyboard, a game controller, over-ear headphones, a small notebook, and a desk lamp casting warm light. Two computer monitors in the background are switched off, their screens plain black glass with a faint reflection of the lamp. Nothing is displayed on any screen. Shallow depth of field, warm and cool contrast. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 17. DAPR 3345: Interactive Audio module banner (current one shows a fake DAW and engine screen)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Interactive_Audio__Foundations_of_Interactive_Spatial_Audio/Workstation_Banner.jpg
```

ChatGPT gives a PNG. Convert it into place (drag the downloaded PNG into Terminal where it says the path):

```
sips -s format jpeg -s formatOptions 88 "PASTE_DOWNLOADED_PNG_PATH" --out "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Interactive_Audio__Foundations_of_Interactive_Spatial_Audio/Workstation_Banner.jpg"
```

**Prompt:**

```
Create a 1942 x 809 pixel photorealistic image. A dark home studio workstation seen from behind an empty mesh office chair: two studio monitor speakers, a keyboard, a game controller, and headphones on a wooden desk. Two computer monitors are switched off, plain black glass reflecting a warm lamp. Nothing is displayed on any screen. Moody low light, shallow depth of field. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---
