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

## Image 18. DAPR 2255: General MIDI channel 10 (current one runs off the edge)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__Foundation/GM_Channel_10.png
```

**Prompt:**

```
Create a 1600 x 900 pixel PNG with a fully transparent background. A single straight row of sixteen identical small rounded blocks seen at a slight three quarter angle, evenly spaced and fully inside the frame with generous margins. Fifteen blocks are green #1B5E20; the tenth block from the left is orange #993300 and very slightly taller. Soft studio lighting, subtle shadows. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 19. DAPR 2255: Alkaline cell cross section (the old one showed the zinc carbon layout)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Batteries/Alkaline_Cross_Section.png
```

**Prompt:**

```
Create a 1600 x 1600 pixel PNG with a fully transparent background. A clean cutaway of a cylindrical AA alkaline battery standing upright, cut in half lengthwise. From the outside in: a thin steel outer can; a thick dark gray manganese dioxide cathode layer pressed against the inside of the can; a thin light separator layer; a pale gray zinc gel anode filling the center; a thin brass collector pin running down the exact center; a plastic seal at the bottom; the raised positive cap at the top. Photorealistic materials, soft studio lighting. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated.
```

---

## Image 20. DAPR 2255: Batteries assignment bench (current parts do not read as batteries)

**Save as:**

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Batteries/Assignment_Bench.jpg
```

ChatGPT gives a PNG. Convert it into place:

```
sips -s format jpeg -s formatOptions 88 "PASTE_DOWNLOADED_PNG_PATH" --out "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Batteries/Assignment_Bench.jpg"
```

**Prompt:**

```
Create a 1600 x 900 pixel photorealistic bench photograph on a light gray anti static mat. Plain unbranded AA and AAA cells with visible positive nubs, a 9 volt battery with its two snap terminals, a four cell AA battery holder with red and black leads, and a digital multimeter with its probes lying beside them. Soft overhead lighting, shallow depth of field. No text, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no border or frame, no caption, no people unless stated. The meter display is blank.
```

---

# Part 2: not for ChatGPT

Found in the full image audit on 2026-09-23. Replace each file at the same path and name unless the Fix says otherwise.

## Capture or source a real photo or screenshot

Real hardware, real software, and third party figures are sourced, never generated (Canvas Standards 20.1 rule 3).

| File (full path) | Problem | Fix |
|---|---|---|
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Tt_Bantam_Plug.png` | Generated plug has four contacts; a TT plug has three (TRS) | Photograph a real TT patch cable end |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Db25_Female.png` | Generated shell has three rows of pins; a DB25 has 13 over 12 | Photograph a real DB25 female |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Db25_Male.png` | Same pin layout problem | Photograph a real DB25 male |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/TA5_Mini_XLR.png` | A large 1/4 inch plug dominates; mixed pin counts | Photograph a real TA5 pair |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Firewire_400_6_Pin.png` | Shell looks like FireWire 800, not the rounded 6 pin end | Photograph a real FireWire 400 cable |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Adam_Audio_Monitors.jpg` | 225 pixel thumbnail | Manufacturer press photo or your own shot, 1600 wide |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Capacitors/Electrolytic_Large_Bank.jpg` | Faint stock photo watermark | Licensed or your own photo |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Capacitors/Electrolytic_on_PCB.jpg` | 400 pixels wide | Photo 1600 wide |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Capacitors/Ceramic.jpg` | Thin 650 x 128 strip | Close up of ceramic disc capacitors |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Multimeters/Oscilloscope.jpg` | 510 x 280 | Photo 1600 wide |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Power/Wattmeter.jpg` | 413 x 491 | Larger photo |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Switches/3pdt_Toggle_Photo.jpg` | 320 x 320 | Photo 1200 wide or larger |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/PAR_Fixture_Side_XLR_Ports.jpg` | Renamed: it shows XLR ports, not the DIP switch bank the page needs | Photograph the DIP switches on a real PAR can; save as PAR_Fixture_DIP_Switch_Bank.jpg in the same folder |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/TRS_MIDI_Cables_3.5mm.jpg` | Renamed: two identical cables, nothing shows Type A vs Type B | Add a Type A vs Type B wiring diagram (Image Reference or hand drawn) |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Electronics/Talkback_Box_Assembled.jpg` | Shows a hand and a cable, no talkback box | Photograph the finished box |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Final_Exam/Schematic_Full.png` | 600 x 448, text unreadable | Higher resolution export of the RedBoard schematic |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Final_Exam/Schematic_Symbols.png` | 485 x 600, labels unreadable | Higher resolution symbol chart |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Final_Exam/Transformer_Symbols.jpg` | Table text unreadable | Rebuild as an HTML table on the page |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Track_Input_Selector.png` | Blurry manual figure | Capture from Pro Tools at native resolution |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Monitoring/Theatrical_Listening_Environment.jpg` | 624 x 666 third party figure, labels unreadable | Higher resolution source or redraw |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Monitoring/Speaker_Placement.jpg` | 592 x 648, notes unreadable | Higher resolution source or redraw |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Introduction_to_Surround_and_Multichannel_Audio/Analog_Digital_Delivery_Evolution.png` | 639 x 284, text too small | Export at 1600 wide |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Introduction_to_Surround_and_Multichannel_Audio/Dolby_Pro_Logic_History_Overview.png` | Generated collage with made up receivers | Remove, or rebuild from real product photos |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Introduction_to_Surround_and_Multichannel_Audio/Legacy_Dolby_Hardware_Milestones.png` | Receiver photos look generated | Real product photos |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mastering_and_Surround_Encoding/Common_Audio_Meters.png` | Generated meters that do not exist | Real meter screenshots |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Time_Machine_Restore.jpg` | Phone photo of a screen | Real screenshot |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Screenshot_Options_Menu_over_System_Settings.jpg` | Phone photo of a screen | Real screenshot |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Terminal_Pwd_Ls_Cd.png` | 5282 x 686, unreadable at page width | Recapture in a narrow Terminal window |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Function_Keys_Panel.png` | Mostly empty dark pane | Recapture the Keyboard, Function Keys dialog |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Effects__Spectral_Effects_and_EQ/Vocal_EQ_Frequency_Band_Chart.jpg` | Washed out third party chart | Rebuild as a clean chart |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Use_and_Care/Studio_Floor_Plan.png` | Nearly blank, labels unreadable | Redraw with room names |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/DAPR_Monitor/Sennheiser_HD_490_Pro.jpg` | Headphone cut off, 298 x 630 | Full product shot |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/DAPR_Monitor/PreSonus_Eris_E3.5.jpg` | 300 x 300, rear panels only | Larger front view |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/DAPR_Monitor/JBL_305P_MkII.png` | Award badges printed on the image | Clean product shot |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/DAPR_Monitor/Audio_Technica_ATH_R30x.png` | Looks like the ATH R70x | Check the model; replace or rename |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/DAPR_Monitor/Philips_SHP9500.png` | Closed cups; the SHP9500 has open grilles | Check the model; replace |

## Blur personal information before students see it

The repo is public. Blur in Preview (Tools, Annotate, a filled rectangle) or recapture.

| File (full path) | Problem | Fix |
|---|---|---|
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/About_This_MAC.png` | Mac serial number | Blur the serial |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/About_This_MAC_M5.png` | Mac serial number | Blur the serial |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Audio_Devices_Window.png` | Device named Adam Olson 16 Pro | Blur or rename the device, recapture |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/External_Drive_Sidebar.png` | Adam Olson UVU Time Machine | Blur |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Home_Folder_Contents.png` | /Users/adamwolson and personal folder names | Recapture on a clean demo account |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Turbotax_Leftover_Folder.png` | /Users/adamwolson and TurboTax contents | Recapture with a neutral app; name it Leftover_App_Support_Folder.png |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Login_Items_Panel.png` | Account name and photo in the sidebar | Blur the account block |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Sound_Output_List.png` | Account name and photo | Blur the account block |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/About_General_Settings.png` | Account name in the sidebar | Blur the account block |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Focus_and_Balance/Technical_Ear_Trainer_Settings.png` | Student name Owen Peterson visible | Blur the name (file already renamed) |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Essential_Groundwork/Dashboard_New_Session.png` | Probably /Users/name in the Location field | Check and blur |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Pro_Tools__Fundamentals/Dashboard_New_Session.png` | Same as above | Check and blur |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Pro_Tools_Dashboard_Key.png` | Location path may show a username | Check and blur |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Creating_Dolby_Atmos_Deliverables/Export_Master_to_ADM_Dialog.png` | /Users/ekuehnl path | Blur the path |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Creating_Dolby_Atmos_Deliverables/Export_Master_to_IMF_IAB_Dialog.png` | /Users/ekuehnl path | Blur the path |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Creating_Dolby_Atmos_Deliverables/Export_Master_to_MP_Four_Dialog.png` | /Users/ekuehnl path | Blur the path |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Creating_Dolby_Atmos_Deliverables/Export_Re_Renders_Dialog.png` | /Users/ekuehnl path | Blur the path |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Final_Project_and_Final_Exam/Export_Master_to_ADM_Dialog.png` | /Users/ekuehnl path (copy) | Replace with the blurred copy |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Export_Selected_Dialog_High_Sample_Rate.png` | Users:ekuehnl path | Blur the path |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Export_Selected_Dialog_Video_Sample_Rate.png` | Users:ekuehnl path | Blur the path |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/CS_623a_BOAA_Lab/Users_Folder_With_Shared_Selected.png` | /Users listing may show real account names | Check and blur |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/CS_623a_BOAA_Lab/Finder_Step_10.jpg` | Same /Users listing | Check and blur |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/DAPR_Introduce_Yourself/Canvas_Upload_Dialog.png` | Browser address bar and tabs | Crop to the dialog |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/DAPR_Introduce_Yourself/Example_Headshot.jpg` | Photo of a real looking person | Confirm consent or AI origin |

## Fix by hand

Small edits to existing files.

| File (full path) | Problem | Fix |
|---|---|---|
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Filter_Curve_4.png` | Red spell check squiggle under dB/oct (also 5 and 6) | Re-export from the slide with spell check off |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Diagram_Nondispersive_Arrival.jpg` | Top label clipped | Re-export with margins |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Diagram_Stiffness_vs_Density.jpg` | Labels and axis title cut off | Re-export with padding |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Monitoring__Psychoacoustics/Sound_Field_Speaker_Placement.png` | 740 x 359 heat map, labels unreadable | Re-export larger |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Course_Orientation/Course_Card.png` | Gemini sparkle mark bottom right | Crop or paint it out |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Course_Outline_Banner_Alt.png` | Gemini sparkle mark bottom right | Crop or paint it out |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Course_Orientation/Course_Card_Alt.png` | Visible seam in the bottom band | Crop the band off |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Use_and_Care/Power_Up_Sequence_Alt.png` | Gives a different power up order than Power_Up_Sequence.png | Decide the order; keep the one that matches |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__MIDI_Evolution_and_Extended_Protocols/OSC_Address_Anatomy.png` | Two labels print on top of each other | Space the labels |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Multimeters/Jack_Selection.png` | COM label garbled | Fix the label |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Series_Resistor_Method.png` | Step 4 text cut off | Re-layout |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Transistors/As_a_Switch.png` | NPN drawn without base bar or emitter arrow; label overprinted | Redraw the symbol |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Schematics/Logic_Gates.png` | 24 tiny gates, unreadable | Larger chart |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Inductor.png` | International symbol cut off | Re-export the full strip |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Electronics/Rendered_Triangles_With_Banded_Resistors.png` | Right op amp has plus and minus swapped | Use the Tan_Resistors version, or fix |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Industry_Network_Audio_Protocols/Descending_Labeled_Bandwidth_Bars.png` | NDI HX3 labeled lowest bandwidth; order is wrong | Fix the labels or put the numbers in a page table |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Direct_Early_Late_Reflections_Timeline.png` | Early and late ms labels look reversed | Fix the labels |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mastering_and_Surround_Encoding/Short_Chain_of_Boxed_Processor_Icons.jpg` | Label cut to Dynamics Processin (also Full_Chain_of_Boxed_Processor_Icons.png) | Re-export with the full label |
