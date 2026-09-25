# ChatGPT Image Creation: DAPR All Courses Line Drawing Replacements

ALL COURSES

Written 25 September 2026. Every image in the Canvas repo was checked (1,878 raster files, 1,805 unique) against the live cartridges: DAPR 2000 v71 and Spring 2027 v1, DAPR 2010 v25, DAPR 2020 v42, DAPR 2255 v87, DAPR 3255 v15, DAPR 3340 v57, DAPR 3345 v14, and the Universal Class Content export. This file holds only images a current page actually shows.

## How to use

1. Start with Part 1. Those line drawings are weak and also teach something wrong.
2. Paste one gray block into a new ChatGPT chat. The block already carries the course, file name, size, format and save path. One image per chat.
3. Save the result over the path on the "Save to (overwrite)" line, same name, same extension. If there is an "Also overwrite" line, save the same file there too.
4. Tell Claude which ones you saved. Claude crops to the size shown, keeps PNG under 1 MB and JPEG under 500 KB, and checks each one before you commit and push.

Every prompt asks for no text (or at most four quoted labels), no logos, no brand marks, no model numbers and no readable screens. Values and names stay in the page caption.

## Count

| Course | Part 1: wrong and weak | Part 2: weak only | Total |
|---|---|---|---|
| Shared: Classes/All (every course) | 2 | 10 | 12 |
| DAPR 2000 Digital Audio Essentials | 14 | 23 | 37 |
| DAPR 2010 Core Recording | 10 | 40 | 50 |
| DAPR 2020 Core Mixing | 13 | 34 | 47 |
| DAPR 2255 Audio Hardware I | 6 | 11 | 17 |
| DAPR 3255 Audio Hardware II | 11 | 33 | 44 |
| DAPR 3340 Spatial Audio I | 14 | 21 | 35 |
| DAPR 3345 Spatial Audio II | 2 | 13 | 15 |
| All courses | 72 | 185 | 257 |

Parts 3 to 7 cover images that are not line drawings but are wrong, things to capture instead of generating, files pages link that do not exist yet, page text to update, and what was left alone.

# Part 1. Make these first: line drawings that are also wrong

Each of these is a thin code drawn figure and it also states something false, clips its own labels, or contradicts its caption. The fix is written into the prompt.

### Shared: Classes/All (every course)

#### ALL COURSES Image 01. Live room and control room with the signal path through the wall

Now: A loose line drawing of two rooms with an arrow running right to left and the room names printed large.

What to fix: Signal path now reads left to right, with the live room on the left and the control room on the right.

```
ALL COURSES
Image: Live room and control room with the signal path through the wall
File name: Room_Layout.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/CS_623a_BOAA_Lab/Room_Layout.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: BOAA Lab: LC623a Studio Proficiency Assessment
Fix: Signal path now reads left to right, with the live room on the left and the control room on the right.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional isometric cutaway of a small recording studio, seen from above at a three quarter angle, with the walls cut off at waist height like an architect's model floating on white. Two rooms sit side by side and share one thick wall that holds a double pane glass window. The left room is the live room: warm wood floor in a pale tint of brown orange (#993300), two generic microphones on boom stands, a music stand, an acoustic guitar on a floor stand, and a small wall plate low on the shared wall with microphone cables plugged into it. The right room is the control room: pale charcoal (#212121) tinted floor, a generic mixing desk with a dark screen, two studio monitors on stands toed in toward an empty chair at the mix position, and a short equipment rack beside the desk. A glowing blue (#0D47A1) path starts at the microphones, runs along the cables to the wall plate, passes through the shared wall and continues to the desk, with small chevrons pointing right along its length. Soft even lighting, gentle shadows, clean matte materials. Quote only these two labels, in a clean bold sans serif in charcoal (#212121), set on the floor near the front edge of each room: "LIVE ROOM" and "CONTROL ROOM". No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### ALL COURSES Image 02. SI prefix ladder with an audio object on each rung

Now: A code drawn table of nine prefixes whose pico example gives 100 pF of cable capacitance per foot, which is too high.

What to fix: Typical microphone cable is about 30 pF per foot, not 100 pF. The new image carries no numbers, so put "about 30 pF per foot" in the caption and page text for the pico rung.

```
ALL COURSES
Image: SI prefix ladder with an audio object on each rung
File name: SI_Prefix_Ladder.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/Student_Essentials/SI_Prefix_Ladder.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Essentials: 3F) Metric Standards
Fix: Typical microphone cable is about 30 pF per foot, not 100 pF. The new image carries no numbers, so put "about 30 pF per foot" in the caption and page text for the pico rung.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional ladder standing upright in the center, seen in three quarter view, with exactly nine evenly spaced glossy rungs. The top four rungs are tints of blue (#0D47A1), the fifth (middle) rung is charcoal (#212121) and slightly thicker as the base unit, and the bottom four rungs are tints of green (#1B5E20). On each rung rests one small photoreal object, top to bottom: a generic external hard drive; a small wireless antenna with radiating rings; a quarter inch instrument cable plug; a short glowing sine ribbon dotted with dense sample points; a plain charcoal cube; a small shape of two repeating echo pulses; a blue electrolytic capacitor with two leads; a tiny yellow film capacitor; a short neat coil of black microphone cable. All components have blank bodies with no printed markings. To the left of the ladder stands a tall glossy green arrow pointing down; to the right stands a tall glossy blue arrow pointing up. Soft studio lighting, soft shadows, shallow depth of field on the objects. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 2000 Digital Audio Essentials

#### DAPR 2000 Image 01. Game audio pipeline from asset to runtime, with the feedback loop

Now: A generic four box flowchart with role names in text and a return arrow; flat and generic.

What to fix: Keep the four stages in order. Note for the caption: implementation is normally done inside the middleware by the technical sound designer, and the audio programmer integrates the middleware into the game engine, so the original "Implementation then Middleware" role split is worth rewording.

```
DAPR 2000 - Digital Audio Essentials
Image: Game audio pipeline from asset to runtime, with the feedback loop
File name: Game_Audio_Pipeline.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Careers__Audio_Careers/Game_Audio_Pipeline.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Careers: Games, Spatial Audio, Acoustics, Hardware & Audio Technology (Figure 1)
Fix: Keep the four stages in order. Note for the caption: implementation is normally done inside the middleware by the technical sound designer, and the audio programmer integrates the middleware into the game engine, so the original "Implementation then Middleware" role split is worth rewording.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram of four glossy pedestals in a row, left to right, on a pale gray floor tint, joined by a glowing path with chevrons pointing right. Pedestal one, blue (#0D47A1): a generic shotgun microphone beside a bright glowing waveform clip. Pedestal two, green (#1B5E20): a small node graph of connected glowing blocks with tiny sliders, standing for sound events being wired up. Pedestal three, brown orange (#993300): an interlocking gear with curly brace shapes (no readable code) plugging into a solid cube that stands for the game engine. Pedestal four, blue: a generic unbranded game controller with soft sound rings rising from it, next to a tiny three dimensional game world diorama of a hill and a tree. A curved glossy red (#B71C1C) return arrow sweeps under the row from pedestal four back to pedestal two, showing play testing feeding changes back into implementation. Soft studio lighting, soft shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 02. Live sound path with the monitor mix branching back to the stage

Now: An icon chain that runs console to monitor wedge to audience in series, which is wrong, because stage monitors are a separate feed back to the performers.

What to fix: Split the path after the stage box: the front of house console drives the main PA to the audience, and a separate monitor mix feeds floor wedges aimed back at the performers. The original drew the wedge in series between the console and the audience.

```
DAPR 2000 - Digital Audio Essentials
Image: Live sound path with the monitor mix branching back to the stage
File name: Live_Sound_Roles.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Careers__Audio_Careers/Live_Sound_Roles.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Careers: Live Sound, Theater, AV Systems & Audio Networking (Figure 1)
Fix: Split the path after the stage box: the front of house console drives the main PA to the audience, and a separate monitor mix feeds floor wedges aimed back at the performers. The original drew the wedge in series between the console and the audience.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional isometric diorama of a small concert, floating on white, reading left to right. On the left, a stage deck holds a vocal microphone on a stand and a generic stage box with two rows of XLR inputs; a thick multicore snake leaves the stage box. The snake splits into two glowing paths. Main path, glowing blue (#0D47A1): it runs right across the floor to a generic front of house mixing console on a small riser in the middle of the room, and from the console back to two tall line array speaker columns hanging at either side of the stage, both facing right. Soft green (#1B5E20) wavefronts spread from those columns over a crowd of simple smooth rounded figures standing on the right, with no faces. Second path, glowing brown orange (#993300): it runs from the stage box to a small monitor console at the side of the stage, then to two floor wedge monitors on the stage deck, angled up and back toward the microphone position, facing the performer and away from the audience. Soft studio lighting, soft shadows, matte stage materials. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands; the only people are the simple faceless audience figures.
```

#### DAPR 2000 Image 03. Post production audio chain from set to final mix

Now: Five flat icon boxes with titles; the dialogue edit box shows a field recorder, which is production sound gear, not editing.

What to fix: The dialogue edit stage now shows edited dialogue clips instead of a field recorder, which belongs to production sound.

```
DAPR 2000 - Digital Audio Essentials
Image: Post production audio chain from set to final mix
File name: Post_Production_Roles.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Careers__Audio_Careers/Post_Production_Roles.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Careers: Film, Television, Broadcast, Podcasting & Media (Figure 1)
Fix: The dialogue edit stage now shows edited dialogue clips instead of a field recorder, which belongs to production sound.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram of exactly five glossy pedestals in a row, left to right, joined by glowing arrows pointing right in blue (#0D47A1), green (#1B5E20), red (#B71C1C) and blue. Pedestal one: a boom pole with a shotgun microphone inside a furry windshield, angled down over a tiny film set corner with a director's chair. Pedestal two: a short stack of dialogue clips lying on a timeline strip, one clip being trimmed at its edge, beside a speech bubble shape. Pedestal three: several layered colorful waveforms stacked in depth with a bright spark between them. Pedestal four: a small Foley pit with a pair of leather shoes standing on a square of gravel next to a square of wood flooring, and a small prop door. Pedestal five: a wide generic dubbing console fader bank facing a large dark, softly defocused screen. Soft studio lighting, soft shadows, real textures. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 04. EQ curve and compressor transfer curve banner

Now: A flat orange line banner whose left curve is an arbitrary wiggle rather than a recognizable EQ curve.

What to fix: The left panel now shows a real EQ curve (high pass slope, a broad bell boost, a high shelf) instead of an arbitrary wiggle.

```
DAPR 2000 - Digital Audio Essentials
Image: EQ curve and compressor transfer curve banner
File name: Module_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/DAW__EQ_and_Dynamics/Module_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: DAW: Overview, EQ & Dynamics
Fix: The left panel now shows a real EQ curve (high pass slope, a broad bell boost, a high shelf) instead of an arbitrary wiggle.

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Two floating glossy dark charcoal (#212121) glass panels side by side, each tilted slightly back in three quarter view, each with a faint fine grid. Left panel: a thick glowing blue (#0D47A1) ribbon draws an equalizer curve from left to right: a steep roll off rising from the far left (high pass), a flat stretch, a smooth broad bell shaped boost in the middle, another flat stretch, then a gentle upward step to a higher flat plateau at the right (high shelf); the area under the curve is softly filled with translucent blue. Right panel: a compressor transfer curve drawn as a thick glowing brown orange (#993300) ribbon: a straight diagonal line rising at 45 degrees from the lower left to a bright red (#B71C1C) knee point about two thirds of the way across, then continuing to the right at a much shallower slope; a faint dotted ghost of the 45 degree line continues above it to show the level that was taken away. Soft reflections, studio lighting. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 05. Smooth wave with sample points and a quantized staircase banner

Now: A flat violet curve with small disconnected L shaped marks that do not form a proper sample and hold staircase.

What to fix: The staircase is now continuous: each step starts at a sample point, holds flat until the next one, and every step height sits on one fixed set of levels.

```
DAPR 2000 - Digital Audio Essentials
Image: Smooth wave with sample points and a quantized staircase banner
File name: Module_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Digital_Audio__The_Digital_Domain/Module_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Digital Audio: Overview, The Digital Domain
Fix: The staircase is now continuous: each step starts at a sample point, holds flat until the next one, and every step height sits on one fixed set of levels.

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. A richly rendered dimensional diagram in a slight three quarter view: a thick glowing violet (#4A148C) ribbon traces two full cycles of a smooth sine wave across the banner. At exactly equal intervals along it sit glossy violet beads, about 14 per cycle. Directly behind the ribbon stands a continuous translucent charcoal (#212121) staircase built from glossy blocks: each step begins at a bead, holds perfectly flat until the next bead, then jumps, and every step top sits on one of a set of faint, evenly spaced horizontal guide lines etched into a pale floor plane, so the blocks sit just above or below the smooth curve. Soft studio lighting, soft shadows, gentle reflections. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 06. Sampling and quantization on one evenly spaced grid

Now: A code drawn wave and a staircase drawn apart from it, with uneven sample spacing and quantized levels that do not sit on a consistent grid.

What to fix: Sample intervals are exactly equal, the staircase is overlaid on the wave as the alt text says, and every step snaps to one evenly spaced set of quantization levels. In the original the sample spacing varies and two nearly equal samples land on levels only a few pixels apart.

```
DAPR 2000 - Digital Audio Essentials
Image: Sampling and quantization on one evenly spaced grid
File name: Sampling_Quantization.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Digital_Audio__The_Digital_Domain/Sampling_Quantization.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Digital Audio: Understanding The Digital Domain (Figure 1)
Fix: Sample intervals are exactly equal, the staircase is overlaid on the wave as the alt text says, and every step snaps to one evenly spaced set of quantization levels. In the original the sample spacing varies and two nearly equal samples land on levels only a few pixels apart.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram on a pale floor plane seen in a slight three quarter view. A faint grid of exactly 8 evenly spaced horizontal level lines and exactly 14 evenly spaced vertical sample lines. A smooth charcoal gray (#212121) analog wave ribbon runs one and a half cycles from left to right across the grid. Where each vertical sample line meets the wave sits a glowing blue (#0D47A1) bead. Overlaid on the same grid, a glossy raised brown orange (#993300) staircase: each step starts exactly at a sample line, holds flat until the next sample line, and its height is snapped to the nearest horizontal level line, so small visible gaps appear between each blue bead and its step (the rounding error). Soft studio lighting, soft shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 07. Omni, cardioid and figure eight pickup patterns banner

Now: A flat line drawing of six polar patterns with a printed title, while the page alt text describes three patterns.

What to fix: Shows the three patterns the alt text names (omni, cardioid, figure eight) and drops the title text baked into the current banner.

```
DAPR 2000 - Digital Audio Essentials
Image: Omni, cardioid and figure eight pickup patterns banner
File name: Module_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics_Selection_and_Stereo_Techniques/Module_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Microphones: Overview
Fix: Shows the three patterns the alt text names (omni, cardioid, figure eight) and drops the title text baked into the current banner.

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Three richly rendered translucent pickup pattern shapes in a row, each floating above its own glossy circular polar grid disc seen in three quarter view, each with a small generic microphone capsule at its center whose front faces toward the back of the disc. Left: a perfect glowing sphere (omnidirectional). Center: a rounded apple shaped cardioid, fullest toward the front, narrowing to a single dimple null at the rear. Right: a figure eight of two equal round lobes, one to the front and one to the rear, pinched to nulls at both sides. The shapes are translucent red (#B71C1C) glass with soft inner glow, the grid discs pale charcoal (#212121) tint with fine rings. Soft studio lighting, gentle reflections. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 08. Mastering chain: broad EQ, gentle compression, limiter

Now: A flat box chain with settings in text; the limiter box says the ceiling is minus 1.0 dBFS, while the page specifies a true peak ceiling of minus 1.0 dBTP.

What to fix: The limiter ceiling is true peak, minus 1.0 dBTP, as the caption says; the old in image label read dBFS. All settings stay in the caption.

```
DAPR 2000 - Digital Audio Essentials
Image: Mastering chain: broad EQ, gentle compression, limiter
File name: Mastering_Chain.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Mixing__Mixing_and_Mastering/Mastering_Chain.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mixing: Assignment, Master Your Mix (Figure 1); Mixing & Mastering: Read, What Mastering Does and What It Cannot Fix (Figure 1); Mixing & Mastering: Read About Mastering (Figure 1)
Fix: The limiter ceiling is true peak, minus 1.0 dBTP, as the caption says; the old in image label read dBFS. All settings stay in the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional signal chain reading left to right. At the far left, a glossy blue (#0D47A1) stereo waveform ribbon flows in. It passes through exactly three generic unbranded rack processor units in a row, each a thick charcoal (#212121) faceplate with real brushed metal texture and one glowing display that shows only a shape: first, an EQ with a very gentle, broad curve (a slight low tilt and one wide shallow bell); second, a compressor whose gain reduction needle has barely moved; third, a limiter whose display shows a thin horizontal ceiling line with a flat bar just touching it. Glossy green (#1B5E20) arrows join each stage. At the far right, the output waveform ribbon is slightly denser than the input, and its peaks stop just under a thin translucent red (#B71C1C) glass ceiling plane that runs above it. Soft studio lighting, soft shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 09. Energy arc of a song across its sections

Now: The file shows the Mix 1A, Mix 1B, Mix 2 assignment sequence with point values, but three of the four pages that use it describe the rise and fall of a song's energy.

What to fix: Draw the song energy arc that three of the four captions and alt texts describe. The Mix 2 Revision page caption describes the three stage assignment sequence instead; check which copy that page uses before overwriting the Project__Mix_2 copy, and give that page its own file if it keeps that caption.

```
DAPR 2000 - Digital Audio Essentials
Image: Energy arc of a song across its sections
File name: Mix_Arc.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Mixing__Mixing_and_Mastering/Mix_Arc.png
Do NOT overwrite yet: /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Project__Mix_2_-_Six_of_One_Revision/Mix_Arc.png (that copy shows the Mix 1A, 1B, 2 sequence, which is what the Mix 2 Revision page caption describes)
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: DAW: Assignment, Mix 1A, Six of One (Figure 1); Mixing: Assignment, Peer Review of Three Mixes (Figure 1); Mixing & Mastering: Read, Using a Reference Track (Figure 1); Mixing: Assignment, Mix 2, Six of One Revision (Figure 1)
Fix: Draw the song energy arc that three of the four captions and alt texts describe. The Mix 2 Revision page caption describes the three stage assignment sequence instead; check which copy that page uses before overwriting the Project__Mix_2 copy, and give that page its own file if it keeps that caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram seen in a slight three quarter view. A long pale floor is divided left to right into exactly eight section bands of similar width, alternating pale blue and pale green tints, standing for intro, verse, chorus, verse, chorus, bridge, final chorus, outro. Above the floor, a thick glossy ribbon traces the song's energy: low in the intro, moderate in the first verse, clearly higher in the first chorus, back down in the second verse but slightly above the first verse, higher again in the second chorus, a clear dip in the bridge, the highest peak of all in the final chorus, then falling away through the outro. The ribbon shades from blue (#0D47A1) where it is low through violet (#4A148C) to red (#B71C1C) at its highest, and casts a soft shadow on the floor bands. Soft studio lighting. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 10. Insert in line versus send to a reverb aux

Now: A two panel flat box diagram with sentences; the send side never returns the reverb aux to the mix output.

What to fix: The reverb aux output now joins the mix output; in the original the send path dead ends at the reverb, so the effect would never be heard.

```
DAPR 2000 - Digital Audio Essentials
Image: Insert in line versus send to a reverb aux
File name: Send_vs_Insert.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Processing__Time-Based_Effects/Send_vs_Insert.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Processing: Read, Send Versus Insert (Figure 1)
Fix: The reverb aux output now joins the mix output; in the original the send path dead ends at the reverb, so the effect would never be heard.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Two richly rendered dimensional panels side by side on a white floor, each a slightly raised glossy base. Left panel: a vertical chain from top to bottom: a blue (#0D47A1) track tile, then a generic plug in processor block sitting fully in line, then a brown orange (#993300) mix output tile; one thick glowing blue stream passes through the processor block with nothing going around it. Right panel: a blue track tile on the left sends a thick glowing blue stream straight right to a brown orange mix output tile. From underneath the track tile a thinner violet (#4A148C) copy stream taps off, runs down and right into an aux tile, through a generic reverb unit showing a soft diffuse cloud inside a glass window, and then rises back up into the same mix output tile, where the violet and blue streams merge. Soft studio lighting, soft shadows. Quote only these two labels, in a clean bold sans serif in charcoal (#212121), on the base of each panel: "INSERT" on the left and "SEND" on the right. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 11. Balanced cable: inverted cold leg cancels the noise

Now: A flat banner that draws the hot and cold signals in the same polarity and uses a loudspeaker icon as the balanced input.

What to fix: The cold conductor carries an upside down copy of the signal, while the noise lands on both conductors the same way up. The balanced input flips the cold leg back and adds the two, so the signal doubles and the noise cancels. The loudspeaker icon is replaced by a balanced input stage.

```
DAPR 2000 - Digital Audio Essentials
Image: Balanced cable: inverted cold leg cancels the noise
File name: Balanced_Audio.jpg
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Balanced_Audio.jpg
Size: 1600 x 600 px
Format: JPEG, quality 88
Used on: Signal Flow: Read, Balanced vs. Unbalanced Cables
Fix: The cold conductor carries an upside down copy of the signal, while the noise lands on both conductors the same way up. The balanced input flips the cold leg back and adds the two, so the signal doubles and the noise cancels. The loudspeaker icon is replaced by a balanced input stage.

Create a 1600 x 600 pixel JPEG, wide landscape banner, photorealistic studio shot on a seamless dark charcoal (#212121) backdrop with soft falloff. On the left, a generic unbranded handheld dynamic microphone lies on its side. From it runs a black microphone cable whose outer jacket is cut away along its length to reveal three conductors running left to right: a blue (#0D47A1) insulated hot conductor with a glowing smooth wave floating along it, a violet (#4A148C) insulated cold conductor with the same glowing wave floating along it but flipped upside down as an exact mirror image, and a bare braided silver shield. Midway along the cable, one burst of jagged red (#B71C1C) noise spikes strikes both the hot and the cold conductor identically, the same spikes pointing the same direction on both. On the right, the cable plugs into a small generic metal balanced input module; just inside its glass window the cold wave turns back upright and merges with the hot wave, and from the module's output emerges one single, larger, clean smooth wave in blue with no spikes at all. Shallow depth of field, rim lighting on the cable. Quote only these two labels, in a clean bold sans serif in white, beside the conductors near the microphone: "HOT" by the blue conductor and "COLD" by the violet conductor. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 12. Home studio signal flow on a real desk

Now: A collage of stock photos of recognizable branded gear and a photo of a real performer, joined by thin colored lines and a legend.

What to fix: Replace the recognizable branded interface, laptop, monitors and headphones and the stock photo of a real person with generic gear and an anonymous performer; keep the four color coded paths (mic, USB, monitors, headphones).

```
DAPR 2000 - Digital Audio Essentials
Image: Home studio signal flow on a real desk
File name: Home_Studio_Signal_Flow.jpg
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Home_Studio_Signal_Flow.jpg
Size: 1600 x 900 px
Format: JPEG, quality 88
Used on: Signal Flow: Example, The Home Studio Setup
Fix: Replace the recognizable branded interface, laptop, monitors and headphones and the stock photo of a real person with generic gear and an anonymous performer; keep the four color coded paths (mic, USB, monitors, headphones).

Create a 1600 x 900 pixel JPEG, wide landscape, a photorealistic three quarter bench shot of a tidy home studio desk against a softly lit wall with a few acoustic panels. In the center of the desk, a compact generic two input USB audio interface in charcoal with two gain knobs, one large monitor knob and a headphone jack, with no markings. To its left, a generic laptop with a dark screen. Behind them, a pair of white unbranded studio monitors on small desk stands. To the right, closed back headphones resting on a stand. At the far right, a condenser microphone on a boom arm with a round pop filter, and a singer behind it rendered softly out of focus with no face in focus. The cables glow gently in color along their length: a blue (#0D47A1) XLR cable from the microphone to the interface's first input; a green (#1B5E20) USB cable from the interface to the laptop; two brown orange (#993300) cables from the interface's rear outputs to the two monitors; a light orange headphone cable from the interface's headphone jack to the headphones. Shallow depth of field, warm practical lighting, real material textures. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands in view; the one person is out of focus with no face in focus.
```

#### DAPR 2000 Image 13. Sine wave with wavelength, amplitude and one cycle

Now: A tiny flat line drawing that labels amplitude as "(power)", which is wrong; amplitude is not power.

What to fix: Amplitude is the height of the wave from its center line, not power; drop "(power)". The note that frequency is cycles per second goes in the caption.

```
DAPR 2000 - Digital Audio Essentials
Image: Sine wave with wavelength, amplitude and one cycle
File name: Sine_Wave_with_Wavelength_and_Amplitude.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Sine_Wave_with_Wavelength_and_Amplitude.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Sound: Supplemental, Sound, Hearing, Frequency, Amplitude & Decibel
Fix: Amplitude is the height of the wave from its center line, not power; drop "(power)". The note that frequency is cycles per second goes in the caption.

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), landscape. A richly rendered dimensional diagram in a slight three quarter view: a thick glossy blue (#0D47A1) sine ribbon runs exactly two full cycles from left to right, starting at the center line and rising, above a thin charcoal (#212121) time axis with an arrowhead at the right. Above the wave, a green (#1B5E20) span bar with end stops runs exactly from the first crest to the second crest. On the right, a brown orange (#993300) double arrow stands vertically from the center line up to the level of the second crest, beside it. Below the wave, a charcoal span bar with end stops runs from the starting zero crossing to the next upward zero crossing, exactly one full cycle. Soft studio lighting, soft shadows. Quote only these four labels, in a clean bold sans serif in charcoal: "WAVELENGTH" above the green bar, "AMPLITUDE" beside the vertical arrow, "ONE CYCLE" below the lower bar, "TIME" at the tip of the axis arrow. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 14. Four waveform basics: envelope, sine, phase offset, cancellation

Now: A gray four panel board with tiny legends; the sine panel legend calls the wave peak a "Mode", which is not the term for a crest.

What to fix: The legend's "Mode (Peak of Wave)" is wrong; the peak is the crest (compression). The new image has no legends, so use "crest" in the caption.

```
DAPR 2000 - Digital Audio Essentials
Image: Four waveform basics: envelope, sine, phase offset, cancellation
File name: Waveform_Basics.jpg
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Waveform_Basics.jpg
Size: 1600 x 900 px
Format: JPEG, quality 88
Used on: Sound: Supplemental, Sound, Hearing, Frequency, Amplitude & Decibel
Fix: The legend's "Mode (Peak of Wave)" is wrong; the peak is the crest (compression). The new image has no legends, so use "crest" in the caption.

Create a 1600 x 900 pixel JPEG, wide landscape, photographic: four glossy acrylic display tiles arranged in a two by two grid, standing slightly tilted back on a seamless pale gray studio backdrop with soft falloff and gentle reflections below, each tile holding one richly rendered dimensional diagram. Top left: an amplitude envelope drawn as a glossy brown orange (#993300) ribbon: a steep straight rise, a short fall to a lower level, a long flat hold, then a straight fall to the floor, with a small charcoal arrow pointing down at the start and a small charcoal arrow pointing up where the final fall begins. Top right: a glossy red (#B71C1C) sine ribbon of three cycles around a charcoal (#212121) center line, with a small green (#1B5E20) bead on one crest and a small blue (#0D47A1) bead on one zero crossing. Bottom left: two identical glossy sine ribbons, one red and one blue, the blue shifted slightly later in time so the two are offset but overlapping. Bottom right: two identical glossy sine ribbons, blue and violet (#4A148C), with the violet an exact upside down mirror of the blue so each crest meets a trough, above a thin flat charcoal line showing their silent sum. Product photograph lighting, crisp detail, shallow depth of field toward the back tiles. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 2010 Core Recording

#### DAPR 2010 Image 01. Direct sound and first reflection points in a control room plan

Now: A flat room outline with thin colored lines and labels that sit on top of the lines; the bounce points are not drawn at the true mirror angle.

What to fix: Place each side wall reflection point by mirror geometry (angle in equals angle out), which puts it between the speaker and the listener along the wall, a little nearer the speaker; the current drawing places it too far back. Labels removed so nothing overlaps the paths.

```
DAPR 2010 - Core Recording
Image: Direct sound and first reflection points in a control room plan
File name: Room_Plan_with_Reflection_Points_Marked.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Acoustics/Room_Plan_with_Reflection_Points_Marked.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Acoustics assignment (acoustics-assignment.html), Figure 1; Acoustics: Working With the Room You Have, Figure 1
Fix: Place each side wall reflection point by mirror geometry (angle in equals angle out), which puts it between the speaker and the listener along the wall, a little nearer the speaker; the current drawing places it too far back. Labels removed so nothing overlaps the paths.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram: a top down view tilted slightly into three quarter, showing a rectangular control room built as a shallow open model with low light grey walls and a pale warm floor, floating on white. The front wall is at the top of the image. Near the front wall, two unbranded studio monitors in charcoal (#212121) stand on stands, toed in toward one listening chair. The chair sits centered left to right, about one third of the way back into the room, and the two speakers and the listener's head form an equilateral triangle. Mark the listener's head with a small charcoal sphere at ear height above the empty chair. From each speaker, a glowing green (#1B5E20) path runs straight to the head: the direct sound. From each speaker, a glowing red (#B71C1C) path runs to the nearest side wall and bounces to the head, obeying true mirror geometry so the angle in equals the angle out; the bounce point lands on the side wall between the speaker's depth and the listener's depth, slightly nearer the speaker. The red paths are visibly longer than the green ones. At each bounce point, a small glowing red square marker sits flat against the side wall surface, like a target where a panel belongs. Keep the whole layout mirror symmetric left to right.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 02. Three overhead placements, each measured to the snare

Now: Three cartoon kit panels with dashed lines; the snare sits beyond the kick among the toms, and the third panel's side mic sits on the hi hat side.

What to fix: The snare now sits in front of the drummer, beside the kick, closest to the throne (known issue). Also, in the three mic panel the low side mic moves to the drummer's right, beside the floor tom, aimed across the kit at the snare; the current drawing puts it on the hi hat side.

```
DAPR 2010 - Core Recording
Image: Three overhead placements, each measured to the snare
File name: Drum_Kit_Panels_with_Overhead_Options.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Drum_Recording/Drum_Kit_Panels_with_Overhead_Options.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Drums: Microphone Placement From the Overheads Down, Figure 3
Fix: The snare now sits in front of the drummer, beside the kick, closest to the throne (known issue). Also, in the three mic panel the low side mic moves to the drummer's right, beside the floor tom, aimed across the kit at the snare; the current drawing puts it on the hi hat side.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic, three equal panels side by side, each a high three quarter view looking down on the same generic unbranded right handed five piece drum kit on a seamless white floor, soft studio light. Get the kit layout exactly right in every panel: the empty drum throne at the bottom of the frame; the snare directly in front of the throne, slightly to the left, the drum nearest the throne; the kick drum just to the right of the snare, its pedal toward the throne and its front head pointing away, toward the top of the frame; one rack tom mounted above the kick; the floor tom to the right of the throne; the hi hat to the left of the snare; a crash cymbal upper left and a ride cymbal upper right. Brass cymbals, white coated heads, dark shells. Left panel: a spaced pair of small pencil condenser microphones on boom stands, high above the left and right sides of the kit, with two taut glowing blue (#0D47A1) strings running from each capsule to the center of the snare head, visibly equal in length. Middle panel: a coincident XY pair of small pencil condensers on one stereo bar, centered high above the kit, capsules touching and crossed at a right angle, with two glowing blue strings to the snare center, equal in length. Right panel: one microphone directly above the snare pointing straight down; a second microphone low on the drummer's right, beside the floor tom at about rim height, aimed across the kit at the snare; glowing blue strings from both capsules to the snare center, equal in length; and a third microphone just outside the kick drum's front head. Thin light grey divider gaps between panels.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 03. Top down drum kit plan with every microphone position

Now: Flat circles and red triangles with leader line labels; the kit layout is wrong, with the kick sitting where the drummer would be and the kick out mic on the drummer's side.

What to fix: Correct kit layout: throne at the bottom, snare nearest the throne, kick in front of the drummer with its front head facing away, and the kick out mic in front of that front head, on the far side from the drummer. The current drawing puts the kick where the throne should be and the kick out mic on the drummer's side.

```
DAPR 2010 - Core Recording
Image: Top down drum kit plan with every microphone position
File name: Overhead_Kit_Plan_with_Red_Markers.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Drum_Recording/Overhead_Kit_Plan_with_Red_Markers.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Drums assignment (drums-assignment.html), Figure 1; Drums: Microphone Placement From the Overheads Down, Figure 1
Fix: Correct kit layout: throne at the bottom, snare nearest the throne, kick in front of the drummer with its front head facing away, and the kick out mic in front of that front head, on the far side from the drummer. The current drawing puts the kick where the throne should be and the kick out mic on the drummer's side.

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), landscape close to 4:3. Photorealistic top down view, tilted very slightly into three quarter, of a generic unbranded right handed five piece drum kit on a seamless white floor, soft even studio light. Layout, exactly: the empty drum throne at the bottom center of the frame; the snare directly in front of the throne, slightly left; the kick drum centered in front of the drummer, its pedal toward the throne and its front head facing the top of the frame; two rack toms mounted above the kick; the floor tom to the right of the throne; the hi hat to the left of the snare; two crash cymbals above left and above right. Mark exactly ten microphone positions with small glowing red (#B71C1C) cone shaped markers, each pointing at its target: two overhead markers high above the left and right cymbals, joined to the snare center by two faint equal length dashed lines; one at the hi hat; one at the edge of the left rack tom head; one on the snare top head edge; one peeking from under the snare for the bottom head; one on the floor tom head edge; one inside the kick drum through the front head port; one just outside the kick's front head on the far side from the drummer; and one room marker well out in front of the kit toward the top right corner.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 04. Drum kit in perspective with microphone positions in placement order

Now: An outline kit in perspective with numbered blue badges; the numbering puts the overheads last (6 and 7) while the caption says overheads go first.

What to fix: The current numbers contradict the caption (kick 1, snare 2, overheads 6 and 7). The new image shows placement order with three color tiers instead of printed numbers: overheads first in green, kick and snare second in blue, toms and hi hat third in violet. Update the caption wording from "numbered" to "colored in the order you place them" and make the page table follow overheads, kick, snare, rack tom, floor tom, hi hat.

```
DAPR 2010 - Core Recording
Image: Drum kit in perspective with microphone positions in placement order
File name: Perspective_Kit_with_Numbered_Blue_Markers.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Drum_Recording/Perspective_Kit_with_Numbered_Blue_Markers.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Drums: Microphone Placement From the Overheads Down, Figure 2
Fix: The current numbers contradict the caption (kick 1, snare 2, overheads 6 and 7). The new image shows placement order with three color tiers instead of printed numbers: overheads first in green, kick and snare second in blue, toms and hi hat third in violet. Update the caption wording from "numbered" to "colored in the order you place them" and make the page table follow overheads, kick, snare, rack tom, floor tom, hi hat.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic high three quarter view from the front left of a generic unbranded right handed five piece drum kit on a seamless white floor, soft studio light, shallow depth of field. Correct layout: empty throne behind the kit; snare in front of the throne, slightly to the drummer's left; kick in the center with its pedal toward the throne and its front head facing the camera side; one rack tom above the kick; floor tom to the drummer's right; hi hat to the left of the snare; one crash cymbal on each side. Place seven microphone markers as small glowing cone shaped pins pointing at their targets, colored by the order they go up. First tier, green (#1B5E20): two overhead markers high above the left and right cymbals, each joined to the snare center by a faint equal length dashed line. Second tier, blue (#0D47A1): one marker aimed into the kick through its front head, and one at the edge of the snare top head. Third tier, violet (#4A148C): one at the rack tom edge, one at the floor tom edge, and one at the hi hat. Make the three tiers easy to tell apart at a glance.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 05. Three level meters: too low, right, and clipping

Now: Three cartoon LED ladders beside a bullet list; the middle and right meters leave the bottom segments dark, which a bar meter never does.

What to fix: Every meter fills continuously from the bottom segment up; the current drawing lights the middle of the middle and right meters with dark segments below.

```
DAPR 2010 - Core Recording
Image: Three level meters: too low, right, and clipping
File name: Wiki_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Gain_Staging/Wiki_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Gain Staging: Overview (page banner)
Fix: Every meter fills continuously from the bottom segment up; the current drawing lights the middle of the middle and right meters with dark segments below.

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide banner. Photorealistic product photograph on a seamless white background, soft studio light. Three identical generic hardware LED bar meters stand upright side by side in the left two thirds of the frame, each a vertical ladder of twelve rectangular segments in a dark charcoal (#212121) housing. Every meter lights from the bottom segment upward with no gaps. Left meter: only the bottom one segment lit green (#1B5E20), everything above dark (too quiet). Middle meter: the bottom seven or eight segments lit green, the rest dark (right level). Right meter: all segments lit, green up to the top, with the top segment lit hard red (#B71C1C) (clipping). The right third of the banner is clean white space.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 06. Cutaways of dynamic, condenser and ribbon transducers

Now: Three flat cutaway drawings with printed part labels; the ribbon panel draws the magnets as blocks at the top and bottom of the ribbon instead of beside it.

What to fix: In a ribbon motor the magnet pole pieces run along both long sides of the ribbon, and the ribbon is clamped at its two ends; the current drawing puts blue magnet blocks at the ends and nothing beside the ribbon.

```
DAPR 2010 - Core Recording
Image: Cutaways of dynamic, condenser and ribbon transducers
File name: Transducer_Types.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Microphones/Transducer_Types.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Microphones: Three Transducers, Figure 1
Fix: In a ribbon motor the magnet pole pieces run along both long sides of the ribbon, and the ribbon is clamped at its two ends; the current drawing puts blue magnet blocks at the ends and nothing beside the ribbon.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic cutaway models like precision museum sections, three equal panels side by side on seamless white, crisp studio light, shallow depth of field. Left, moving coil dynamic: a thin domed diaphragm facing left, attached at its rim to a copper voice coil wound on a short former; the coil sits in the narrow ring shaped gap of a magnet assembly (a central pole piece inside a ring, magnet steel finished in blue (#0D47A1)), sectioned so the coil can be seen inside the gap. Middle, condenser: a very thin gold coated diaphragm stretched flat and parallel a hair's width in front of a thick brass backplate drilled with many small holes, the pair sectioned edge on, with two fine wires running down to a small polarizing voltage cell. Right, ribbon: a very thin corrugated aluminum ribbon in a warm brown orange (#993300) tone, standing vertically, clamped at its top and bottom ends by small metal clamps, and suspended in the narrow gap between two tall magnet pole pieces in blue (#0D47A1) that run along its full length on its left and right sides.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 07. Spaced and near coincident stereo arrays seen from above

Now: Three line drawn mic pairs with printed spacings and angles; the spaced pair is drawn with cardioids, and the caption says two arrays while the image shows three.

What to fix: The spaced AB pair uses omnidirectional microphones, so its capsules are drawn as round omni heads pointing straight ahead. The image keeps three panels (spaced AB, ORTF, NOS); the caption and alt text say two spaced arrays, so either edit them to three or drop the NOS panel.

```
DAPR 2010 - Core Recording
Image: Spaced and near coincident stereo arrays seen from above
File name: Array_Panels_with_Drawn_Microphones.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Miking_Techniques/Array_Panels_with_Drawn_Microphones.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Miking Techniques: Five Stereo Arrays, Figure 1
Fix: The spaced AB pair uses omnidirectional microphones, so its capsules are drawn as round omni heads pointing straight ahead. The image keeps three panels (spaced AB, ORTF, NOS); the caption and alt text say two spaced arrays, so either edit them to three or drop the NOS panel.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic, three equal panels side by side, each a top down view tilted slightly into three quarter of small pencil condenser microphones on stands or a stereo bar, pointing toward the top of the frame, on a seamless white floor, crisp studio light. Around each capsule, a faint translucent glowing lobe shows its pickup pattern. Left panel, spaced pair: two omnidirectional pencil microphones on two separate stands, far apart, both pointing straight ahead and parallel, each with a round, circular pickup glow; a glowing blue (#0D47A1) line on the floor between the stands shows the wide spacing. Middle panel, ORTF: two cardioid pencil microphones on one stereo bar, capsules about a head's width apart, splayed outward at a wide angle, a little over a right angle, each with a heart shaped glow; a glowing blue arc between the two capsule axes shows the angle. Right panel, NOS: two cardioid pencil microphones on one stereo bar, capsules nearly twice as far apart as in the middle panel, splayed at exactly a right angle, with the same heart shaped glows and a glowing blue arc. Keep the scale the same across the middle and right panels so the difference in spacing is visible.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 08. A punch replaces one range on one playlist; the other playlists are kept

Now: Four pale bars under a tick ruler with printed labels, including the misspelling "ovewrritten" three times.

What to fix: Removes the misspelled "ovewrritten" labels; the kept playlists are shown visually instead.

```
DAPR 2010 - Core Recording
Image: A punch replaces one range on one playlist; the other playlists are kept
File name: Punch_and_Playlists.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Pro_Tools_for_Tracking/Punch_and_Playlists.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Tracking: Record Modes, Punching, & Playlists, Figure 2
Fix: Removes the misspelled "ovewrritten" labels; the kept playlists are shown visually instead.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter view. Across the top runs a slim glossy ruler with evenly spaced tick marks and no numbers. Below it, four long glossy trays are stacked top to bottom, each holding a full length audio waveform ribbon. Top tray: the waveform is green (#1B5E20) along most of its length, but between two tall translucent red (#B71C1C) vertical gate planes, placed a little right of center, that section has been replaced by a new red tinted waveform with a slightly different shape. The lower three trays each hold a complete, unbroken waveform in soft blue grey, each a different performance shape, with a gentle protective glass cover over each tray and a soft blue (#0D47A1) glow, showing they are kept whole and untouched. The red gates cut only the top tray.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 09. A studio rack with microphone cables coiled beside it

Now: A cartoon rack of network style gear with coiled Ethernet patch cables beside a printed bullet list.

What to fix: The coiled cables become XLR microphone cables; the current drawing shows Ethernet patch cables and a network switch, which is not the studio audio gear the page is about.

```
DAPR 2010 - Core Recording
Image: A studio rack with microphone cables coiled beside it
File name: Wiki_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Use_and_Care/Wiki_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Studio Care: Overview (page banner)
Fix: The coiled cables become XLR microphone cables; the current drawing shows Ethernet patch cables and a network switch, which is not the studio audio gear the page is about.

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide banner. Photorealistic product photograph on a seamless white background, soft studio light, shallow depth of field. In the left two thirds of the frame: a short open studio rack holding four units of generic unbranded audio gear (a preamp with knobs, a compressor with a small meter, a patch bay with two rows of jacks, and a power conditioner), each with a small soft green (#1B5E20) power light. Beside the rack, a wall rail with two hooks, each holding one XLR microphone cable coiled neatly over under, one green and one charcoal (#212121), the connectors hanging straight below. The right third of the banner is clean white space.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 10. From air to file and back: acoustic, analog and digital stages

Now: A row of eight text boxes with domain brackets; Source and Ears are labeled as the analog domain when they are acoustic.

What to fix: The source and the ears sit in the acoustic domain (sound in air), not the analog domain. The chain now reads acoustic, analog, digital, analog, acoustic, with the microphone and the monitor as the transducers at the two boundaries.

```
DAPR 2010 - Core Recording
Image: From air to file and back: acoustic, analog and digital stages
File name: Air_to_File.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/The_Digital_Recording_Process/Air_to_File.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Digital Recording: From Air to File, Figure 1; Orientation: Prerequisites, Figure 1
Fix: The source and the ears sit in the acoustic domain (sound in air), not the analog domain. The chain now reads acoustic, analog, digital, analog, acoustic, with the microphone and the monitor as the transducers at the two boundaries.

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide banner. Make it a richly rendered dimensional diagram in three quarter view: eight objects in one row on a long glossy floor strip, reading left to right, joined by one continuous path. In order: an acoustic guitar with sound ripples in the air; a large diaphragm condenser microphone; a microphone preamp unit; a small converter box (analog to digital); a computer with a dark, softly defocused screen; a second small converter box (digital to analog); a studio monitor speaker; and a plain featureless sculpted head in profile, facing left toward the speaker, with no facial detail, representing the listener's ears. The floor strip is colored by domain: green (#1B5E20) under the guitar and the air up to the microphone's diaphragm; brown orange (#993300) from the microphone's output through the preamp into the first converter; blue (#0D47A1) from the first converter through the computer to the second converter; brown orange from the second converter into the monitor; and green again from the monitor's cone through the air to the listener. The path is drawn as rippling rings in the green zones, a glowing copper cable in the brown orange zones, and a stream of small glowing cubes in the blue zone.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 2020 Core Mixing

#### DAPR 2020 Image 01. Control room cutaway with four first reflection points

Now: A thin line plan of a room that traces only the two side wall reflections, although the caption promises four first reflection points.

What to fix: The current drawing shows only two reflection points (the side walls). The new image shows all four the caption names: left wall, right wall, ceiling and floor.

```
DAPR 2020 - Core Mixing
Image: Control room cutaway with four first reflection points
File name: First_Reflection_Points.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Acoustics__Mix_Acoustics/First_Reflection_Points.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mix Acoustics: What the Room Does to What You Hear (Figure 1)
Fix: The current drawing shows only two reflection points (the side walls). The new image shows all four the caption names: left wall, right wall, ceiling and floor.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show a photorealistic architectural scale model of a small control room, cut away so we look in from a high three quarter angle: the front wall, both side walls, the floor and a clear glass ceiling panel are visible, the near wall and the rest of the ceiling removed. Materials are real: pale plaster walls in a light tint of charcoal (#212121), a light wood floor, soft studio lighting, gentle shadows. Against the front wall stand two small generic studio monitors on stands, toed in toward a single mix chair centered in the room. Mark the listening position with a small glowing white sphere at ear height above the chair headrest; do not show a person. From each monitor, a solid glowing blue (#0D47A1) beam runs straight to the sphere (direct sound). Then show four red (#B71C1C) glowing beams from the monitors that each bounce once before reaching the sphere: one off the left side wall, one off the right side wall, one off the ceiling panel, and one off the floor between the monitors and the chair. At each of the four bounce points place a small glowing red square patch on the surface, like a spot where a treatment panel belongs. The red beams are slightly thinner than the blue ones and clearly longer paths. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 02. Reverb on an insert against reverb on a shared send

Now: A flat box and arrow diagram whose send side is miswired: the Track 2 dry line ends at the reverb box and never reaches the mix buss.

What to fix: In the current drawing the Track 2 dry path runs into the reverb box instead of the mix buss. All three dry paths must reach the mix buss directly, with only the thin send cables feeding the reverb.

```
DAPR 2020 - Core Mixing
Image: Reverb on an insert against reverb on a shared send
File name: Send_versus_Insert_Routing.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Effects__Balancing_and_Reverb/Send_versus_Insert_Routing.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Quick Mix 3 (Figure 1); Balancing & Reverb: Common Mistakes and How to Hear Them (Figure 1)
Fix: In the current drawing the Track 2 dry path runs into the reverb box instead of the mix buss. All three dry paths must reach the mix buss directly, with only the thin send cables feeding the reverb.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram in a gentle three quarter view, glossy 3D tiles and glowing cables, soft shading, signal flowing top to bottom. Left third of the image (insert): one glossy green (#1B5E20) track tile at the top, a thick green cable running straight down into a glossy blue (#0D47A1) reverb block, and a blue cable continuing down into a glossy red (#B71C1C) mix buss slab. Everything from the track passes through the reverb. Right two thirds (send and return): three glossy green track tiles in a row at the top. From each track a thick green dry cable runs straight down, past the reverb, and plugs directly into one long red mix buss slab at the bottom; all three dry cables reach the slab. From the side of each track a thinner brown orange (#993300) send cable branches off and runs into one shared blue reverb block sitting between the tracks and the buss. A single blue return cable leaves the bottom of the reverb block and plugs into the mix buss, and on that return cable sits one small glossy fader cap. The three send cables must visibly merge into the one reverb block. Light tint floor under each half. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 03. Three sources at three depths with reverb halos

Now: A flat three band chart with dots and shaded circles and a column of settings text; the listener marker points away from the sources.

What to fix: The listener marker now points into the scene toward the sources instead of away from them. The settings text moves to the page.

```
DAPR 2020 - Core Mixing
Image: Three sources at three depths with reverb halos
File name: Three_Source_Depth_Map.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Effects__Balancing_and_Reverb/Three_Source_Depth_Map.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Balancing and Reverb: Worked Example, Three Sources at Three Depths (Figure 1)
Fix: The listener marker now points into the scene toward the sources instead of away from them. The settings text moves to the page.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: a shallow glossy stage floor seen from a high three quarter angle from the listener's side, divided into three depth bands from near to far: near band a light tint of green (#1B5E20), middle band a light tint of blue (#0D47A1), far band a light tint of brown orange (#993300). At the near edge, centered, a small charcoal (#212121) wedge marker points into the stage toward the sources, marking the listening position. Three glossy spheres sit on the floor: a green sphere near the center of the near band (lead vocal) wrapped in a small, tight, bright silvery translucent halo; a blue sphere left of center in the middle band (acoustic guitar) wrapped in a medium soft translucent halo; a brown orange sphere right of center in the far band (synth pad) wrapped in the largest soft translucent halo. The guitar and pad halos share the same misty violet tint (#4A148C, very light) to show they come from one shared reverb, while the vocal halo is a different, brighter silvery tint for its own separate reverb. All three spheres are the same physical size so only the halo changes. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 04. Figure of eight side pickup with its null plane

Now: A flat pair of teardrop lobes with a dashed line and several text labels; a real figure of eight pattern is two equal circles touching at the capsule.

What to fix: The lobes are drawn as teardrops; a figure of eight polar pattern is two equal round lobes touching at the capsule. The new image uses two equal spheres.

```
DAPR 2020 - Core Mixing
Image: Figure of eight side pickup with its null plane
File name: Figure_8_Null_Plane.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Effects__Delay_and_Stereo_Enhancements/Figure_8_Null_Plane.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Mix Delay and Stereo Enhancements (Figure 1); Delay and Stereo Enhancements: Width Without Losing Mono (Figure 2)
Fix: The lobes are drawn as teardrops; a figure of eight polar pattern is two equal round lobes touching at the capsule. The new image uses two equal spheres.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram seen from a gentle high three quarter angle. In the center, a small photorealistic generic side address microphone capsule, satin metal, mounted horizontally. Around it, two equal translucent glossy spheres touch exactly at the capsule: the left sphere glowing blue (#0D47A1) with a small raised "+" emboss on its surface, the right sphere glowing green (#1B5E20) with a small raised single horizontal bar emboss meaning negative polarity. Through the capsule, between the two spheres, stands a thin vertical sheet of clear glass with charcoal (#212121) edges, running from the front of the image to the back: the null plane. At the front edge of that glass sheet sits a small glowing white source sphere, and a faint white beam travels from it along the glass plane straight into the capsule without touching either lobe. The lobes are the same size and perfectly round. No text other than the quoted label, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 05. Overhead drum kit with snare to microphone path lengths

Now: A flat line plan of a drum kit that mixes plan and elevation views and places the snare in line between the kick and the toms.

What to fix: The current kit is not a real layout: the snare sits in line between the kick and the rack toms and the cymbals are drawn side on with tripod legs. The new image uses a real kit seen from directly above: rack toms mounted over the kick, snare beside the kick on the drummer's left, closest to the throne.

```
DAPR 2020 - Core Mixing
Image: Overhead drum kit with snare to microphone path lengths
File name: Drum_Mic_Path_Lengths.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Focus_and_Balance/Drum_Mic_Path_Lengths.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Focus and Balance: Mix Balancing (Figure 2)
Fix: The current kit is not a real layout: the snare sits in line between the kick and the rack toms and the cymbals are drawn side on with tripod legs. The new image uses a real kit seen from directly above: rack toms mounted over the kick, snare beside the kick on the drummer's left, closest to the throne.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic overhead product photograph of a generic unbranded five piece drum kit, shot straight down from above, the drummer's empty throne at the bottom center of the frame. Layout exactly as a real kit: the bass drum in the center pointing up the frame away from the throne; two rack toms mounted on top of the bass drum shell, angled toward the throne; the snare drum between the throne and the bass drum, just to the image left of the bass drum, closest to the throne; the hi hat further to the image left of the snare; the floor tom to the image right of the throne; a crash cymbal above left and a ride cymbal above right. Small generic microphones: one at the front of the bass drum, one clipped at the snare rim, one clipped on each rack tom, and two overhead microphones hanging high above the kit, one over the left side and one over the right side. From the center of the snare head, five glowing blue (#0D47A1) lines run out to the bass drum mic, the two tom mics and the two overhead mics, each a clearly different length, each with small evenly spaced tick marks along it like a measuring tape. Soft even studio light, natural drum finishes in deep charcoal (#212121) with brass cymbals. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 06. Warp markers pulling a late hit onto the grid

Now: Two flat waveform rows with diamond markers that are identical before and after, so no transient is actually shown moving onto the grid.

What to fix: The current "after" row is a copy of the "before" row: the third hit sits off the grid in both. The new image shows one late hit before, the same hit on its grid line after, and the audio between markers visibly squeezed on one side and stretched on the other.

```
DAPR 2020 - Core Mixing
Image: Warp markers pulling a late hit onto the grid
File name: Elastic_Audio_Warp_Markers.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Timing/Elastic_Audio_Warp_Markers.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mixing: Timing: Module Overview (Figure 1); Timing: The Controls and What They Cost (Figure 1)
Fix: The current "after" row is a copy of the "before" row: the third hit sits off the grid in both. The new image shows one late hit before, the same hit on its grid line after, and the audio between markers visibly squeezed on one side and stretched on the other.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: two long frosted glass lanes stacked top and bottom, seen from a slight three quarter angle, both crossed by the same set of evenly spaced thin vertical grid planes in a light tint of green (#1B5E20). Each lane holds a glossy blue (#0D47A1) waveform of three drum hits, each hit a sharp attack with a decaying tail, and each hit carries a small red (#B71C1C) diamond warp marker on a thin red stem at its attack. Top lane (before): the first and third hits sit exactly on grid planes; the middle hit lands clearly late, to the right of its grid plane. A thick brown orange (#993300) arrow points down from the top lane to the bottom lane. Bottom lane (after): all three hits and markers sit exactly on grid planes; the middle hit has been pulled left onto its plane. The waveform between the first and middle markers is visibly compressed, its ripples packed tighter and tinted slightly lighter; the waveform between the middle and third markers is visibly stretched, its ripples spread wider and tinted slightly lighter. Under each of those two regions float soft red double headed brackets. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 07. Piano roll with in key rows highlighted and a sung pitch line

Now: A flat piano roll whose keyboard is malformed (black keys drawn as full rows, stacked in pairs with no two and three grouping) and whose highlighted rows match no real key.

What to fix: The keyboard must be a real keyboard: black keys shorter than white keys, in groups of two and three, with no black key between E and F or between B and C. The highlighted rows must be the notes of one real key (C major, the white key rows), not an arbitrary pattern.

```
DAPR 2020 - Core Mixing
Image: Piano roll with in key rows highlighted and a sung pitch line
File name: Scale_and_Target_Notes_Boxed.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Tuning/Scale_and_Target_Notes_Boxed.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mixing: Tuning: Module Overview (Figure 1)
Fix: The keyboard must be a real keyboard: black keys shorter than white keys, in groups of two and three, with no black key between E and F or between B and C. The highlighted rows must be the notes of one real key (C major, the white key rows), not an arbitrary pattern.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram of a pitch editor piano roll, seen from a slight three quarter angle, glossy and dimensional. On the left edge, a vertical piano keyboard with the keys pointing right, lowest note at the bottom, covering one and a half octaves from C up to G. It is an accurate keyboard: white keys full length, black keys shorter and glossy black, arranged in groups of two and three exactly as on a real piano, with no black key between E and F or between B and C. To the right, a grid of horizontal rows, exactly one row per key, so twelve rows per octave. Every row that belongs to a white key (the notes of C major) is tinted light blue (#0D47A1 at a very light tint); every row that belongs to a black key is a plain light gray. Faint vertical beat lines cross the grid. A thick glossy green (#1B5E20) tube representing the sung pitch wanders upward from lower left to upper right, drifting in and out of the blue rows, sometimes sitting between rows. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 08. Target notes constrained to the rows of one scale

Now: A flat piano roll with colored target lines spaced evenly every two semitones, which is a whole tone scale, not a major or minor key.

What to fix: The current target lines are evenly spaced every whole step (a whole tone scale). A real major scale has seven targets per octave with half steps between E and F and between B and C, so two pairs of adjacent targets per octave sit only one row apart. The rainbow line colors also carry no meaning and are replaced by one color.

```
DAPR 2020 - Core Mixing
Image: Target notes constrained to the rows of one scale
File name: Scale_and_Target_Notes_Curves.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Tuning/Scale_and_Target_Notes_Curves.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Tuning: Pitch Correction Procedure Guide (Figure 1)
Fix: The current target lines are evenly spaced every whole step (a whole tone scale). A real major scale has seven targets per octave with half steps between E and F and between B and C, so two pairs of adjacent targets per octave sit only one row apart. The rainbow line colors also carry no meaning and are replaced by one color.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram of a pitch editor piano roll seen from a slight three quarter angle. On the left edge, an accurate vertical piano keyboard, keys pointing right, lowest note at the bottom, covering about one and a half octaves from C: white keys full length, black keys shorter and glossy black in groups of two and three, no black key between E and F or between B and C. To the right, a grid of horizontal rows, one row per key. On every row that belongs to a white key (the C major scale) lies a glowing green (#1B5E20) target rail running the full width; rows that belong to black keys have no rail and stay plain light gray. The rails are therefore not evenly spaced: most neighbours are two rows apart, but E to F and B to C are only one row apart. Along the rails sit several short glossy blue (#0D47A1) note blocks at different heights, each resting exactly on a green rail and never on a gray row, showing where the corrector will pull each sung note. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 09. Headphone measured on a head and torso simulator with a microphone at the eardrum

Now: A flat outline of a human head with a microphone dot at the ear canal opening, no headphone, and a line to a text labeled plot.

What to fix: The current drawing puts the microphone at the ear canal opening and shows no headphone, although the caption describes a headphone measurement with the microphone where the eardrum would be. The new image shows a headphone on a measurement dummy with the microphone at the inner end of the ear canal.

```
DAPR 2020 - Core Mixing
Image: Headphone measured on a head and torso simulator with a microphone at the eardrum
File name: Head_Torso_Measurement.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Monitoring__Calibration_and_Monitoring/Head_Torso_Measurement.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Pro Tools Lab 02 (Figure 1); Calibration: Speaker and Headphone Level Calibration (Figure 2)
Fix: The current drawing puts the microphone at the ear canal opening and shows no headphone, although the caption describes a headphone measurement with the microphone where the eardrum would be. The new image shows a headphone on a measurement dummy with the microphone at the inner end of the ear canal.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic product photograph on a seamless white sweep, soft studio light. Left half: a generic head and torso measurement simulator, a smooth matte light gray mannequin head and shoulders with simple sculpted ears and no facial detail beyond a smooth nose and brow, seen in profile facing left. It wears a generic over ear headphone in charcoal (#212121). A clean cutaway window through the headphone cup and the side of the head reveals the ear canal as a short tube running inward, and at its inner end, where the eardrum would be, a small satin metal measurement microphone capsule with a thin blue (#0D47A1) glowing cable. The cable runs out and to the right into a floating glossy panel in the right half of the image that holds a raised blue response curve ribbon: a gentle rise, a broad hump, a dip and a smaller peak, over a plain panel with no grid numbers. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people; the mannequin is a featureless measurement dummy.
```

#### DAPR 2020 Image 10. Course grade as one bar divided by work type

Now: A flat four color bar with text in each segment, and the four segments are nearly equal although the caption says module work is the bulk of the grade.

What to fix: The current segments are drawn at almost equal widths, which contradicts the caption. Set the widths to the real syllabus weights before generating (confirm them in the syllabus); the prompt below assumes module assignments largest and the final exam smallest.

```
DAPR 2020 - Core Mixing
Image: Course grade as one bar divided by work type
File name: Grade_Breakdown.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Grade_Breakdown.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Orientation: Course Description, Learning Outcomes, and Requirements (Figure 2); Instructor: Rubric Attachment Map (Figure 1)
Fix: The current segments are drawn at almost equal widths, which contradicts the caption. Set the widths to the real syllabus weights before generating (confirm them in the syllabus); the prompt below assumes module assignments largest and the final exam smallest.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: one long thick glossy bar lying across the middle of the image, seen from a slight three quarter angle, with soft shadow beneath, divided into four solid blocks that fit together with thin gaps. Left to right: a charcoal (#212121) block that is clearly the widest, labeled "ASSIGNMENTS"; a green (#1B5E20) block, the second widest, labeled "QUIZZES"; a blue (#0D47A1) block, narrower, labeled "PROJECTS"; a brown orange (#993300) block, the narrowest, labeled "FINAL". The two module blocks together (charcoal and green) take up well over half the bar. Labels in clean white lettering on the top face of each block. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 11. Two week module window from Monday open to Friday morning due

Now: Two rows of flat weekday calendar icons with a lot of text; weekends are left out, so the eleven day span shows as ten tiles.

What to fix: Weekends are included so the span from the first Monday to the second Friday reads as the full eleven days the caption describes, not ten weekday tiles.

```
DAPR 2020 - Core Mixing
Image: Two week module window from Monday open to Friday morning due
File name: Weekly_Rhythm.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Weekly_Rhythm.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Orientation: Schedule & Module Outline (Figure 1)
Fix: Weekends are included so the span from the first Monday to the second Friday reads as the full eleven days the caption describes, not ten weekday tiles.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: fourteen glossy 3D calendar tiles in two rows of seven, Monday to Sunday, seen from a slight three quarter angle, each tile with two small ring binder loops on top and a charcoal (#212121) header strip with no writing. The five weekday tiles in each row are white; the two weekend tiles at the right end of each row are a light gray tint. First row, first tile (Monday of week one) is green (#1B5E20) with a raised open book on it. Second row, fifth tile (Friday of week two) is red (#B71C1C) with a raised document and a small raised clock whose hands point to nine o'clock. A glowing ribbon path starts at the green tile, runs along every tile of the first row including the weekend, wraps down to the second row, and ends at the red tile. The last two tiles of the second row, after the red tile, are faded and translucent. Below the calendar, a glossy arrow band runs left to right in three blocks: green with a book symbol, blue (#0D47A1) with a gear symbol, red with a document symbol. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 12. App dragged to the Trash while its leftovers stay behind

Now: Flat text boxes with file paths and product names, and the "drag to Trash" label is clipped by the arrow and box.

What to fix: The "drag to Trash" label in the current image is cut off by the arrow and box. The new image carries no text; paths and utility names go in the page text.

```
DAPR 2020 - Core Mixing
Image: App dragged to the Trash while its leftovers stay behind
File name: App_Leftover_Files.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/App_Leftover_Files.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: macOS: P3: Removing Applications and Leftovers
Fix: The "drag to Trash" label in the current image is cut off by the arrow and box. The new image carries no text; paths and utility names go in the page text.

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide banner (generate it as a wide landscape; it will be cropped to a banner). A richly rendered dimensional diagram seen from a slight three quarter angle. Left: a glossy rounded square app tile in green (#1B5E20) with a plain abstract raised shape on its face (no logo), traveling along a glowing curved arc toward the right, where a generic glossy charcoal (#212121) trash bin with an open lid waits to receive it. Along the bottom of the image, left behind on the floor where the app started, sit two smaller glossy objects: a document tile with raised toggle switches on its face (the preferences file) and a folder with a raised gear on its face (the application support folder). Both leftovers are outlined in a soft violet (#4A148C) glow, and faint dotted violet tethers still connect them back to the spot the app left. Keep all objects on one horizontal band with white space above and below. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 13. Mac DMG and PKG installs beside a Windows EXE install

Now: Flat text boxes under "Mac" and "Windows" headings where the Mac steps run into the Windows column and the Windows row reads right to left.

What to fix: In the current layout the last Mac steps ("Drag to Applications", "Writes to protected system folders") sit under the Windows heading, and the EXE row flows right to left. The new image keeps the two Mac paths and the Windows path in separate lanes, all reading left to right.

```
DAPR 2020 - Core Mixing
Image: Mac DMG and PKG installs beside a Windows EXE install
File name: DMG_PKG_EXE_Flow.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/DMG_PKG_EXE_Flow.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: macOS: P3: Installing Software, DMG, APP, and PKG
Fix: In the current layout the last Mac steps ("Drag to Applications", "Writes to protected system folders") sit under the Windows heading, and the EXE row flows right to left. The new image keeps the two Mac paths and the Windows path in separate lanes, all reading left to right.

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide banner (generate it as a wide landscape; it will be cropped to a banner). A richly rendered dimensional diagram of three horizontal lanes stacked top to bottom, each a glossy floor strip, every lane reading left to right with glowing arrows between three objects. The top two lanes share a light blue tint (#0D47A1, very light) as the Mac lanes; the bottom lane has a light brown orange tint (#993300, very light) and is separated from them by a clear gap, as the Windows lane. Lane one: a glossy disk image tile labeled "DMG", then a mounted virtual drive, then an app tile being dropped into an applications folder. Lane two: a glossy parcel box labeled "PKG", then an installer panel with a raised padlock and key (the admin password), then a row of system folders each with a small lock. Lane three: a generic installer tile labeled "EXE", then three stacked wizard panels with next arrows (screens dark and defocused), then a program folder beside a small filing cabinet with open drawers (the registry). Objects in charcoal (#212121), green (#1B5E20) and red (#B71C1C) accents. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 2255 Audio Hardware I

#### DAPR 2255 Image 01. AC and DC as two glowing traces with charge flow

Now: A thin line chart of a sine wave over a flat line; the AC direction arrows both point at the trough, so the reversal is not clearly shown.

What to fix: The AC direction cues now point one way on every positive half cycle and the opposite way on every negative half cycle, instead of both arrows pointing at one trough.

```
DAPR 2255 - Audio Hardware I
Image: AC and DC as two glowing traces with charge flow
File name: AC_vs_DC_Traces.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/AC_and_DC_Electricity/AC_vs_DC_Traces.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: AC & DC: What Is Alternating Current? (Figure 1)
Fix: The AC direction cues now point one way on every positive half cycle and the opposite way on every negative half cycle, instead of both arrows pointing at one trough.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram seen from a gentle three quarter angle, with soft shading and depth, like glossy 3D glass and light. Show two long horizontal lanes stacked one above the other, each a thin frosted glass slab with a slim charcoal (#212121) zero line running along its middle from left to right. Upper lane: a glowing green (#1B5E20) tube shaped as a smooth sine wave, exactly three full cycles, rising above the zero line, crossing it, dipping below it the same distance, and crossing again. Along the tube travel small glossy spheres; on every section above the zero line the spheres carry small chevrons pointing to the right, and on every section below the line the chevrons point to the left, so the eye reads the flow reversing every half cycle. Lower lane: a glowing blue (#0D47A1) tube held perfectly flat and level a fixed distance above its zero line for the full length, with the same small spheres all carrying chevrons pointing right, evenly spaced, showing one direction and one level. Soft pale green (#E8F5E9) and pale blue (#E3F2FD) glows under each lane, gentle contact shadows on the white. Nothing else in the frame. No text of any kind, no numbers, no axis labels, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 02. Diode symbol aligned over a real diode, bar above band

Now: A flat diode symbol above a flat drawn diode, with the "Same end" label running over the connector line.

What to fix: Labels ran over lines in the current file; the new image uses only two short labels placed in clear white space, away from every line and edge.

```
DAPR 2255 - Audio Hardware I
Image: Diode symbol aligned over a real diode, bar above band
File name: Cathode_Band_and_Symbol.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Diodes_and_LEDs/Cathode_Band_and_Symbol.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Diodes & LEDs: Testing Diodes & LEDs (Figure 1)
Fix: Labels ran over lines in the current file; the new image uses only two short labels placed in clear white space, away from every line and edge.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Upper half: a richly rendered dimensional diode symbol, like a glossy 3D tile extruded from charcoal (#212121): a horizontal lead on the left entering a solid triangle that points to the right, the triangle tip touching a tall vertical bar, and a horizontal lead leaving the bar to the right. Lower half: a photorealistic through hole rectifier diode lying horizontally, studio lit like a product shot, matte black epoxy cylindrical body with a single painted silver grey band near its right end, bright tinned leads extending straight out left and right, soft shadow, shallow depth of field. The symbol's bar sits exactly above the diode's painted band, and a soft glowing green (#1B5E20) vertical light column links the bar down to the band so the viewer sees they mark the same end. A faint blue (#0D47A1) arrow of light runs along the symbol's left lead toward the triangle, showing the direction current flows. Place the label "A" in clear white space to the left of the upper symbol and "K" in clear white space to the right of the upper symbol, bold charcoal letters, with no line, lead or glow passing through or touching either letter. No text other than the quoted labels "A" and "K", no numbers, no logos, no brand marks, no model numbers or printed markings on the diode body, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 03. DMX universe as a row of channel tiles with two overlapping fixtures

Now: A thin grid of empty channel cells with three separate brackets; the caption describes an overlap that the drawing never shows.

What to fix: The caption says two fixture ranges overlap but the current drawing shows three separate ranges; the new image shows the two wash fixture ranges visibly overlapping on shared channels, with the shared tiles marked in red.

```
DAPR 2255 - Audio Hardware I
Image: DMX universe as a row of channel tiles with two overlapping fixtures
File name: DMX_Universe_Addressing.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/DMX_Universe_Addressing.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: MIDI: DMX512 Protocol and Signal Structure (Figure 4)
Fix: The caption says two fixture ranges overlap but the current drawing shows three separate ranges; the new image shows the two wash fixture ranges visibly overlapping on shared channels, with the shared tiles marked in red.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a three quarter view: one long straight row of about forty small glossy square tiles running left to right across the frame, like keys on a long tray, soft studio shading and gentle shadows. Unused tiles are pale grey. Starting at the left end, the first eight tiles are glossy green (#1B5E20) with a translucent green glass canopy arching over them, the dimmer rack's range. After a gap of a few grey tiles, a translucent blue (#0D47A1) glass canopy arches over a run of eight tiles, the first wash fixture. A translucent violet (#4A148C) glass canopy starts over the last three tiles of that blue run and continues over five more tiles, the second wash fixture, so the two canopies clearly overlap on exactly three shared tiles. Those three shared tiles glow solid red (#B71C1C) and sit slightly raised, with both the blue and violet canopies visibly passing over them. The remaining tiles to the right are plain pale grey and unused. Above the blue canopy float a small generic unbranded wash light fixture, and above the violet canopy a second identical fixture, each linked to its canopy by a thin glowing line; above the green canopy floats a small generic unbranded dimmer rack. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 04. Show control hub with four protocol legs

Now: A flat hub box with four arrows to audio, video, lighting and automation; the protocol labels are covered by the arrows.

What to fix: Labels were covered by arrows in the current file; the new image carries no text, and each protocol leg is told apart by cable color, with the protocol names moved to the caption.

```
DAPR 2255 - Audio Hardware I
Image: Show control hub with four protocol legs
File name: Show_Control_Hub.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/Show_Control_Hub.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: MIDI: Network Based Show Control Systems (Figure 1)
Fix: Labels were covered by arrows in the current file; the new image carries no text, and each protocol leg is told apart by cable color, with the protocol names moved to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic studio scene in a three quarter view from slightly above, clean white seamless surface. In the center sits a generic unbranded show control computer box, matte charcoal (#212121) with a dark front panel and a few small status lights. Four thick cables leave it, each a different color and each running to a different generic unbranded device placed at the four corners of the frame: upper left, a green (#1B5E20) cable to a compact studio loudspeaker (audio); lower left, a blue (#0D47A1) cable to a small projector (video); upper right, a brown orange (#993300) cable to a stage wash light fixture (lighting); lower right, a violet (#4A148C) cable to a small motorized chain hoist or winch (stage automation). Each cable has a small inline glowing ring near its device, as if that leg can be tested on its own. The cables curve cleanly and never cross each other or touch another device. Soft studio lighting, real materials, shallow depth of field. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 05. Four band resistor read from the end opposite the gold band

Now: A flat drawn resistor with labeled bands; its subtitle wrongly says to start reading from the tolerance band.

What to fix: The current subtitle says to start from the tolerance band; correct practice is to start at the end opposite the gold tolerance band. The new image shows a reading arrow starting at the brown band end and moving toward the gold band, and drops all text.

```
DAPR 2255 - Audio Hardware I
Image: Four band resistor read from the end opposite the gold band
File name: Four_Band_Worked.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Resistors/Four_Band_Worked.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Resistors: History: Ohm, Wheatstone, & the Color Code (Figure 1)
Fix: The current subtitle says to start from the tolerance band; correct practice is to start at the end opposite the gold tolerance band. The new image shows a reading arrow starting at the brown band end and moving toward the gold band, and drops all text.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic macro product shot of a single generic through hole carbon film resistor lying horizontally across the frame, beige tan body with rounded ends, bright tinned leads extending straight out to the left and right edges, studio lighting, real paint texture, shallow depth of field, soft shadow. Exactly four painted color bands. From the left: brown, then black, then orange, grouped close together near the left end; then a wide empty gap of plain body; then a single metallic gold band near the right end. Band colors must be exact and unmistakable: brown, black, orange, metallic gold. Below the resistor, a soft glowing green (#1B5E20) arrow begins under the brown band and points to the right, sweeping past the black and orange bands, showing that reading starts at the end opposite the gold band. No text of any kind, no numbers, no letters, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 06. Solderless breadboard with rails, terminal strips and center channel

Now: A flat hole grid with row letters and column numbers; the bottom column numbers are printed over the bottom red rail and the rightmost hole column is clipped.

What to fix: The current file prints the bottom column numbers over the bottom red rail, clips the last hole column at the right edge, and draws the power rails as plain lines with no holes. The new image shows complete hole rows, rail holes in groups of five, and one red and one blue rail on each long edge.

```
DAPR 2255 - Audio Hardware I
Image: Solderless breadboard with rails, terminal strips and center channel
File name: Breadboard.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Wiring_and_Safety/Breadboard.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Wiring & Safety: Handling Components Safely (Figure 2)
Fix: The current file prints the bottom column numbers over the bottom red rail, clips the last hole column at the right edge, and draws the power rails as plain lines with no holes. The new image shows complete hole rows, rail holes in groups of five, and one red and one blue rail on each long edge.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic top down product shot, tilted very slightly toward three quarter, of a generic unbranded full size solderless breadboard, white matte plastic with real surface texture, soft studio lighting, soft shadow. The whole board fits inside the frame with margin on every side; no holes are cut off. Layout: along each long edge runs a pair of power rails, one marked by a thin printed red (#B71C1C) stripe and one by a thin printed blue (#0D47A1) stripe, so each long edge has exactly one red rail and one blue rail; rail holes are grouped in clusters of five with small gaps between clusters. Between the two rail pairs lie two terminal strip areas, each exactly five rows of square holes running in columns across the board, separated by a recessed center channel running the full length of the board. Plug in a small amount of real work: one resistor and one red LED seated in separate columns in the upper strip, and two short jumper wires, one red from a red rail and one charcoal from a blue rail, feeding them. No text of any kind, no numbers, no letters, no printed row or column markings, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 3255 Audio Hardware II

#### DAPR 3255 Image 01. Hand to Hand Path Through the Heart Versus One Hand Path Down the Right Side

Now: Two outline body figures with current paths; the one hand figure has its heart drawn on the body's right side and runs the path down the body's left side, which is where the heart really is.

What to fix: Put the heart slightly left of center in the chest (the figure's own left, the viewer's right) on both figures, and run the one hand path in through the figure's right hand, down the right side of the torso and the right leg to the right foot, so it clearly stays away from the heart.

```
DAPR 3255 - Audio Hardware II
Image: Hand to Hand Path Through the Heart Versus One Hand Path Down the Right Side
File name: Body_Outlines_With_Current_Paths.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Electronics/Body_Outlines_With_Current_Paths.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Electronics: Electrical Safety, Figure 1
Fix: Put the heart slightly left of center in the chest (the figure's own left, the viewer's right) on both figures, and run the one hand path in through the figure's right hand, down the right side of the torso and the right leg to the right foot, so it clearly stays away from the heart.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two identical standing anatomical mannequin figures side by side, facing the viewer, arms held slightly away from the body, made of frosted translucent glass with no facial features, like a medical teaching model. Inside each chest a small glossy red heart sits slightly left of center in the body (the figure's own left, which is the viewer's right).

Left figure: a bright glowing red #B71C1C current path enters the palm of one hand, runs up that arm, crosses straight through the chest and through the heart, and runs down the other arm to the other palm. Small glowing beads along the path show the direction of flow. The heart glows hot where the path passes through it.

Right figure: a glowing brown orange #993300 current path enters the palm of the figure's right hand (the viewer's left), runs up the right arm to the shoulder, then straight down the right side of the torso and the right leg to the sole of the right foot, where it meets a small dark gray floor disk. The path stays well clear of the heart, which stays calm and unlit. The figure's left arm hangs relaxed at its side, touching nothing.

A thin soft gray vertical gap separates the two figures. Style: photorealistic studio render of real frosted glass mannequins, soft studio lighting, real material texture, gentle reflections, shallow depth of field, on a clean seamless white background. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens. No real product you could name. No real people and no faces; the figures are featureless glass mannequins.
```

#### DAPR 3255 Image 02. Breadboard With Its Hidden Strips Revealed

Now: A code drawn breadboard with both top rails red and both bottom rails blue, which no real board has.

What to fix: Each long edge gets one red (plus) rail and one blue (minus) rail, not two of the same color.

```
DAPR 3255 - Audio Hardware II
Image: Breadboard With Its Hidden Strips Revealed
File name: Breadboard_Internal_Connections.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Electronics/Breadboard_Internal_Connections.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Electronics: Breadboarding, Figure 1; Electronics: Assignment: Bias a Common Emitter Stage, Figure 1
Fix: Each long edge gets one red (plus) rail and one blue (minus) rail, not two of the same color.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show one generic full size white solderless breadboard lying flat, photographed from a high three quarter angle so the whole board fits the frame with its long axis running left to right. The white plastic is rendered partly translucent, like an X ray cutaway, so the nickel plated spring clip strips underneath the holes are clearly visible.

Geometry that must be exact: a recessed center channel runs the full length of the board and divides it into a top half and a bottom half. On each half, the holes form short vertical columns of five holes; each column of five sits on its own separate metal clip strip, and no strip crosses the center channel. Along the top long edge are two long rails, each a single long metal strip running the length of the board: one rail has a red #B71C1C stripe printed beside it and the other has a blue #0D47A1 stripe. The bottom long edge has the same pair: one red striped rail and one blue striped rail. So each long edge has exactly one red rail and one blue rail.

Make one single column of five holes in the upper half glow soft green #1B5E20 through the plastic, to show that those five holes are one connected node. The center channel is a clean empty groove with a faint pale gray shadow. No components or wires on the board.

Style: photorealistic product photograph with a technical cutaway, studio lighting, real plastic and metal texture, shallow depth of field at the far edges, clean seamless white background. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C.

No text of any kind, no plus or minus symbols, no numbers or letters along the board edges, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens. No real product you could name. No hands or people.
```

#### DAPR 3255 Image 03. P Type and N Type Blocks Meeting at a Depletion Region

Now: Two flat colored rectangles with circles and dots; the legend shows the electron as a black dot while the electrons in the N block are drawn white.

What to fix: Draw holes and electrons consistently (hollow rings for holes, solid glowing beads for electrons) with no mismatched legend, and leave the depletion region free of both.

```
DAPR 3255 - Audio Hardware II
Image: P Type and N Type Blocks Meeting at a Depletion Region
File name: Doped_Blocks_and_Depletion_Gap.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Electronics/Doped_Blocks_and_Depletion_Gap.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Electronics: Semiconductors, Transistors, and Op amps, Figure 2
Fix: Draw holes and electrons consistently (hollow rings for holes, solid glowing beads for electrons) with no mismatched legend, and leave the depletion region free of both.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two thick glossy crystal blocks pressed end to end in a three quarter view, like two slabs of polished semiconductor. The left block is blue #0D47A1 and the right block is green #1B5E20. Where they meet there is a narrow slice of pale, nearly clear crystal, about one sixth of the total length: the depletion region.

Inside the blue left block, scattered through its volume, float about eight small hollow glass rings (holes). Inside the green right block float about eight small solid glowing white beads (electrons). Inside the pale middle slice there are no rings and no beads at all; only a few tiny dull fixed studs set into the crystal lattice, dark on the blue facing side and light on the green facing side, to hint at the fixed charges left behind. Soft light falls across the blocks so the empty middle slice reads clearly as a gap.

Quote exactly two labels, each floating just above its block in clean bold white lettering: "P" above the blue block and "N" above the green block.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for the middle slice.

No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens. No real product you could name. No hands or people.
```

#### DAPR 3255 Image 04. Sine Wave With Peak, RMS and Peak to Peak Marked Correctly

Now: A code drawn sine with the RMS line at about two thirds of peak instead of 0.707, and peak to peak drawn as if it were a level line at the trough.

What to fix: Place the RMS level at 0.707 of the peak height above the center line, and show peak to peak as a vertical span from a trough to a crest, not as a level line.

```
DAPR 3255 - Audio Hardware II
Image: Sine Wave With Peak, RMS and Peak to Peak Marked Correctly
File name: Sine_Wave_With_Amplitude_Reference_Lines.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Electronics/Sine_Wave_With_Amplitude_Reference_Lines.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Electronics: AC & DC Circuits, Figure 3
Fix: Place the RMS level at 0.707 of the peak height above the center line, and show peak to peak as a vertical span from a trough to a crest, not as a level line.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show one thick glossy green #1B5E20 sine wave ribbon, two full cycles from left to right, centered on a charcoal #212121 horizontal center line (zero), with a charcoal vertical axis at the left. The wave rises and falls the same distance above and below the center line.

Add these references, each a thin translucent glowing plane seen edge on as a clean horizontal band:
1. A red #B71C1C band exactly level with the tops of the crests (peak).
2. A brown orange #993300 band placed at seven tenths of the distance from the center line up to the crest, so it sits clearly closer to the peak band than to the middle, cutting each crest just below its shoulders (RMS).
3. No band at the troughs. Instead, a glossy blue #0D47A1 vertical double headed arrow stands between the bottom of one trough and the top of the next crest, spanning the full height of the wave (peak to peak).

Quote exactly three labels, each placed in clear white space to the right of the wave so no label touches or overlaps any line or arrow: "PEAK" in red beside the red band, "RMS" in brown orange beside the brown orange band, and "PEAK TO PEAK" in blue beside the middle of the blue arrow.

Style: a richly rendered dimensional diagram with real depth, soft shading and solid color fills, like a glossy 3D ribbon with glowing reference planes. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C.

No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens. No real product you could name. No hands or people.
```

#### DAPR 3255 Image 05. One Switch Split Into Two Isolated VLANs

Now: A flat charcoal switch bar with a dashed divider; one of the three office boxes has no connection line.

What to fix: Every device on both sides has its own cable to its own port; no device is left unconnected.

```
DAPR 3255 - Audio Hardware II
Image: One Switch Split Into Two Isolated VLANs
File name: One_Switch_and_Dashed_Divider.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Audio_Network_Architecture/One_Switch_and_Dashed_Divider.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: VLANs, Trunk Ports, and Audio/Video over IP, Figure 1
Fix: Every device on both sides has its own cable to its own port; no device is left unconnected.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show one generic unbranded charcoal #212121 network switch, long and low, in a three quarter view, with eight ports along its front. The left four ports have green #1B5E20 port surrounds and the right four ports have blue #0D47A1 port surrounds.

Below the left half, three glossy green tinted device blocks each connect by their own green cable to one of the green ports. Below the right half, three glossy blue tinted device blocks each connect by their own blue cable to one of the blue ports. All six devices are connected; none is left without a cable.

A thin translucent red #B71C1C glass wall rises vertically through the middle of the switch, between the green ports and the blue ports, and continues down to the floor between the two groups of devices, so the two groups sit in separate halves that cannot see each other. Each half sits on a faint floor tile tinted to match its color.

Quote exactly two labels, bold, placed on the floor beneath each group: "AUDIO" under the green group and "OFFICE" under the blue group.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks and cables. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 06. TCP Handshake and Resend Versus UDP Steady Stream

Now: Two arrow ladders; the TCP side shows only a two leg exchange instead of the three leg handshake and never resends the dropped packet, so the lateness it claims is not shown.

What to fix: Show a three leg TCP handshake (out, back, out) before the data, and after the lost packet show the receiver asking again and the sender resending the same packet, with the packets behind it held waiting, so TCP visibly arrives complete but late. UDP keeps its even spacing and simply loses one packet.

```
DAPR 3255 - Audio Hardware II
Image: TCP Handshake and Resend Versus UDP Steady Stream
File name: Two_Arrow_Ladders_With_Dropped_Packet.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Foundations_of_Audio_Networking/Two_Arrow_Ladders_With_Dropped_Packet.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Layer 4: Transport Protocols, Figure 2
Fix: Show a three leg TCP handshake (out, back, out) before the data, and after the lost packet show the receiver asking again and the sender resending the same packet, with the packets behind it held waiting, so TCP visibly arrives complete but late. UDP keeps its even spacing and simply loses one packet.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two side by side timing ladders on pale floor tiles. Each ladder has two tall glossy charcoal #212121 posts, sender on the left post and receiver on the right post, with time flowing downward. Messages are glossy packet tiles sliding along glowing diagonal tracks that slope gently downward as they cross from one post to the other.

Left ladder (blue #0D47A1 packets): at the top, three short handshake tracks zig zag across: sender to receiver, receiver back to sender, sender to receiver. Then three data packets cross. The fourth data packet shatters into red #B71C1C fragments halfway across. A small blue track returns from the receiver to the sender, and the sender sends that same packet again lower down, marked with a faint glow ring. Beside the receiver post, the packets that followed wait stacked in a small queue until the resent packet arrives. The last packet reaches the receiver noticeably lower on the post than on the right ladder: it arrives late.

Right ladder (green #1B5E20 packets): no handshake. Six packets cross at perfectly even spacing. The third shatters into red fragments halfway across and is simply gone; the rest keep coming at the same even rhythm, and the last one reaches the receiver higher on the post than on the left ladder: on time.

Quote exactly two labels, bold, centered above each ladder: "TCP" above the left ladder and "UDP" above the right ladder.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D posts, tiles and glowing tracks. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 07. NAT Rewriting the Source Going Out and the Destination Coming Back

Now: A flat host box, NAT box and cloud with address labels; the return path is labeled "from" the private and public addresses, but on the way back NAT rewrites the destination, not the source.

What to fix: On the outbound packet the source tag changes from private to public; on the returning packet the destination tag changes from public back to private. The current image labels the return traffic "from" both addresses, which is wrong.

```
DAPR 3255 - Audio Hardware II
Image: NAT Rewriting the Source Going Out and the Destination Coming Back
File name: Host_and_Cloud_Across_Translation_Box.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__IP_Addressing/Host_and_Cloud_Across_Translation_Box.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Network Address Translation (NAT), Figure 1
Fix: On the outbound packet the source tag changes from private to public; on the returning packet the destination tag changes from public back to private. The current image labels the return traffic "from" both addresses, which is wrong.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show, left to right: a pale tinted room floor on the left holding one generic computer with a dark screen (the private network); a glossy brown orange #993300 translation block built into a low wall at the edge of that room; and a soft white and pale blue 3D cloud on the right (the internet).

Upper lane, left to right: a glossy packet leaves the computer carrying a small green #1B5E20 address tag on its back end (its sender tag). It enters the translation block, and on the far side the same packet emerges carrying a brown orange tag in the same back position, heading into the cloud.

Lower lane, right to left: a packet leaves the cloud carrying a brown orange address tag on its front end (its destination tag). It enters the translation block, and on the room side it emerges carrying a green tag in the same front position, heading to the computer.

The green tag never appears on the cloud side of the block. Quote exactly one label, bold, on the front face of the translation block: "NAT".

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks, packets and tags. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors and the cloud.

No text other than the quoted label, no numbers, no addresses, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 08. AES50 Devices Chained Port to Port With No Switch

Now: A row of flat labeled boxes under a "No switch" badge whose icon is a crossed out toggle switch, which reads as a power switch rather than a network switch.

What to fix: Show the missing device as a network switch (a box with a row of ports), not a toggle switch.

```
DAPR 3255 - Audio Hardware II
Image: AES50 Devices Chained Port to Port With No Switch
File name: Daisy_Chained_Boxes_and_No_Switch.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Industry_Network_Audio_Protocols/Daisy_Chained_Boxes_and_No_Switch.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Network: AES50, Figure 1
Fix: Show the missing device as a network switch (a box with a row of ports), not a toggle switch.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show four pieces of generic unbranded gear in a row, left to right, on a pale floor tile: a compact digital mixing console (charcoal body, faders, dark screen), a rack stage box, a second rack stage box, and a rack power amplifier. Short thick glossy violet #4A148C cables run directly from each device to the next, port to port, forming a daisy chain. Nothing sits between any two devices.

Above the middle of the chain floats a faded, ghostly translucent network switch (a flat box with a row of eight ports on its front), with a bold glossy red #B71C1C diagonal bar across it, to show there is no switch in this system.

Style: a richly rendered dimensional diagram in a three quarter view with realistic generic equipment models, real depth, soft shading, soft contact shadows and solid color fills. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 09. Audio Protocols Placed on the Layer Where They Run

Now: Four flat layer bars with protocol pills; AES50 is placed at Layer 2 beside AVB, but AES50 is a Layer 1 protocol.

What to fix: Move AES50 down to Layer 1 on its own. AVB stays alone at Layer 2. Dante, AES67, Ravenna, Livewire+, SMPTE ST 2110 and NDI stay at Layer 3. The caption should name the six Layer 3 protocols, since the image leaves them unlabeled.

```
DAPR 3255 - Audio Hardware II
Image: Audio Protocols Placed on the Layer Where They Run
File name: Layer_Bars_With_Protocol_Pills.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Industry_Network_Audio_Protocols/Layer_Bars_With_Protocol_Pills.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Protocol Comparison, Figure 1; Networking: Assignment: Choose a Protocol for Three Venues, Figure 1
Fix: Move AES50 down to Layer 1 on its own. AVB stays alone at Layer 2. Dante, AES67, Ravenna, Livewire+, SMPTE ST 2110 and NDI stay at Layer 3. The caption should name the six Layer 3 protocols, since the image leaves them unlabeled.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. On the left, show a stack of exactly four thick glossy slabs extending to the right like long shelves, seen in a three quarter view. From the bottom up: brown orange #993300 (layer one), red #B71C1C (layer two), blue #0D47A1 (layer three), green #1B5E20 (layer four).

On the bottom brown orange shelf sits exactly one glossy white rounded token. On the red shelf sits exactly one glossy white rounded token. On the blue shelf sit exactly six glossy white rounded tokens in a neat row. The green top shelf is empty. Each token casts a soft shadow on its shelf.

Quote exactly two labels, bold charcoal lettering printed on the face of the single tokens: "AES50" on the token on the bottom shelf and "AVB" on the token on the second shelf. The six tokens on the blue shelf are blank.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D slabs and tokens. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no layer numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 10. Resolver Walking Down the DNS Hierarchy and Answering the Client

Now: A flat chain of five boxes that implies each server passes the query to the next and the authoritative server answers the client directly, which is not how resolution works.

What to fix: The resolver does the walking. It asks the root, gets a referral back, asks the top level domain server, gets a referral back, asks the authoritative server, gets the answer back, and only then answers the client. The root does not forward to the next server, and the authoritative server does not answer the client directly.

```
DAPR 3255 - Audio Hardware II
Image: Resolver Walking Down the DNS Hierarchy and Answering the Client
File name: Box_Chain_With_Return_Arc.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Network_Configuration_and_Control/Box_Chain_With_Return_Arc.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Domain Name System (DNS), Figure 1
Fix: The resolver does the walking. It asks the root, gets a referral back, asks the top level domain server, gets a referral back, asks the authoritative server, gets the answer back, and only then answers the client. The root does not forward to the next server, and the authoritative server does not answer the client directly.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. On the far left, a small charcoal #212121 client block. Just right of it, a glossy blue #0D47A1 resolver block. On the right side, three glossy green #1B5E20 server blocks descend like steps from upper right to lower right: the root at the top, the top level domain server in the middle, the authoritative server at the bottom.

From the resolver, three separate pairs of glowing tracks go out and come back, one pair to each green server in turn from top to bottom: a brown orange #993300 track out with a small packet, and a lighter brown orange track straight back to the resolver. The return from the bottom authoritative server is brighter and carries a small glowing gold key, the answer. No tracks run between the green servers themselves.

Finally, one short bright track runs from the resolver back to the client, carrying the same gold key. The client connects only to the resolver.

Quote exactly four labels, bold charcoal, each on the front face of its block: "CLIENT", "RESOLVER", "ROOT" on the top green block, and "AUTHORITATIVE" on the bottom green block. The middle green block has no label.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks with glowing tracks. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 11. ARP Question Broadcast to All and Answered by One

Now: Flat boxes with orange broadcast arrows and one green reply; the reply note sits on top of an arrow and the question carries an IP address as text.

What to fix: No label or track may cross another; the single reply runs on its own clear path back to the asker.

```
DAPR 3255 - Audio Hardware II
Image: ARP Question Broadcast to All and Answered by One
File name: Broadcast_Question_and_Single_Reply.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Network_Diagnostics/Broadcast_Question_and_Single_Reply.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Address Resolution Protocol, Figure 1
Fix: No label or track may cross another; the single reply runs on its own clear path back to the asker.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. On the left, one glossy blue #0D47A1 asking device. On the right, four glossy pale gray device blocks stacked in a column with even gaps.

From the asking device, four glowing brown orange #993300 tracks fan out, one to each of the four devices, each carrying a small packet with a soft ring of light, so the question reaches everyone. Three of the four devices stay dim. The third device from the top lights up green #1B5E20.

From that green device, one single bright green track runs straight back to the asking device, carrying a small glossy tag (its hardware address). Route this reply slightly below the fan of brown orange tracks so it never crosses or overlaps any of them, and keep every track clearly separate.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks and glowing tracks. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text of any kind, no question marks, no numbers, no addresses, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 3340 Spatial Audio I

#### DAPR 3340 Image 01. Bed or object decision with static and moving examples

Now: A text flowchart with thin arrows; it also lists Dialogue under the object branch even though the test is whether the sound moves, and dialogue normally stays fixed in the center of the bed.

What to fix: The object branch example "Dialogue" is replaced by a pass by vehicle, so both object examples actually move; dialogue belongs with the fixed bed material in the page text.

```
DAPR 3340 - Spatial Audio I
Image: Bed or object decision with static and moving examples
File name: Bed_versus_Object_Decision.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Configuring_Pro_Tools_for_Atmos_Mixing/Bed_versus_Object_Decision.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Routing Tracks to Beds (Figure 1)
Fix: The object branch example "Dialogue" is replaced by a pass by vehicle, so both object examples actually move; dialogue belongs with the fixed bed material in the page text.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional decision diagram in a gentle isometric view, with soft shading and depth, like glossy 3D tiles joined by glowing cables. Top center: a glossy green (#1B5E20) tile holding a single raised audio clip block with a waveform relief. A short glowing cable drops to a raised charcoal (#212121) diamond pedestal just below it; on top of the diamond floats a small sphere tracing a curved dotted arc through the air, the symbol for "does it move". From the left point of the diamond a brown orange (#993300) glowing cable runs left and down, with the label "NO" floating beside it; from the right point a matching cable runs right and down with the label "YES". The left cable ends on a wide blue (#0D47A1) tile shaped like a fixed channel bed: a row of evenly spaced speaker sockets set flush into the tile, labeled "BED" in clear white space above it. The right cable ends on a matching blue tile with a glowing sphere hovering above it on a curved trajectory, labeled "OBJECT" in clear white space above it. Under the bed tile, two smaller pale blue (#E3F2FD) tiles hang from short cables: one holds a tiny forest of trees under soft rain (ambience), the other holds a small generic cello (music). Under the object tile, two smaller pale blue tiles: one holds a small generic helicopter on a curved flight arc passing overhead (flyover), the other holds a small generic car on a curved pass by path with faint motion streaks. Keep all labels in clear space, never touching a cable or tile edge. No text other than the quoted labels "NO", "YES", "BED" and "OBJECT", no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 02. Mastering chain from mix to master

Now: A row of flat text boxes under a meaningless green gradient bar, and the chain has no EQ stage even though the page alt text says it starts with equalization.

What to fix: An EQ stage is added after the mix so the image matches the alt text (equalization, compression, limiting, dither), and the unexplained gradient bar is removed. Order: mix, EQ, multiband compression, mid side, limiting, dither, master.

```
DAPR 3340 - Spatial Audio I
Image: Mastering chain from mix to master
File name: Mastering_Signal_Chain.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mastering_and_Surround_Encoding/Mastering_Signal_Chain.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mastering Overview
Fix: An EQ stage is added after the mix so the image matches the alt text (equalization, compression, limiting, dither), and the unexplained gradient bar is removed. Order: mix, EQ, multiband compression, mid side, limiting, dither, master.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional signal flow diagram in a gentle three quarter view, with soft shading and depth, like glossy 3D tiles joined by a glowing cable. Exactly seven glossy rounded tiles sit in one row from left to right, joined by a glowing brown orange (#993300) cable with small arrow shaped light pulses moving right. Tiles alternate green (#1B5E20) and blue (#0D47A1). Each tile carries one raised object: tile one, a stereo audio file block with a waveform relief (the mix); tile two, a smooth bell shaped frequency curve (EQ); tile three, four side by side frequency slabs of different heights, each pressed down by its own small plate (multiband compression); tile four, a block split into a bright center column and two separate side wings (mid side); tile five, a waveform pressed flat under a glowing ceiling (limiting); tile six, the quiet tail of a waveform dusted with a fine sparkling grain texture (dither); tile seven, a polished finished master disc resting on a small stand (master). Soft contact shadows on white. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 03. Surround delivery formats as five speaker arrangements

Now: A text table with dot patterns; the two 7.1 rows use the same five speaker dot pattern as the 5.1 rows, so they show the wrong channel count.

What to fix: The 7.1 rows now show seven ear level speakers plus a subwoofer (the current dots show only five). Format names and channel counts go in the caption, top to bottom: Dolby Digital 5.1, DTS 5.1, Dolby TrueHD 7.1, DTS HD Master Audio 7.1, Dolby Atmos object based.

```
DAPR 3340 - Spatial Audio I
Image: Surround delivery formats as five speaker arrangements
File name: Surround_Delivery_Formats.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mastering_and_Surround_Encoding/Surround_Delivery_Formats.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Common Surround Formats
Fix: The 7.1 rows now show seven ear level speakers plus a subwoofer (the current dots show only five). Format names and channel counts go in the caption, top to bottom: Dolby Digital 5.1, DTS 5.1, Dolby TrueHD 7.1, DTS HD Master Audio 7.1, Dolby Atmos object based.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram with soft shading and depth, like glossy 3D tiles. Five long, thin, rounded pale gray (#F1F3F1) tiles are stacked from top to bottom with equal gaps. On the center of each tile sits a miniature speaker arrangement seen from an elevated three quarter angle, around a small charcoal (#212121) listener sphere, with the front of every arrangement facing the top of the frame. Tiles one and two: exactly five small glossy green (#1B5E20) speakers (front left, center, front right, surround left, surround right) plus one small brown orange (#993300) subwoofer cube in front. Tiles three and four: exactly seven small glossy green speakers (front left, center, front right, side left, side right, rear left, rear right) plus one brown orange subwoofer cube in front. Tile five: the same seven green speakers and brown orange subwoofer, plus four small blue (#0D47A1) speakers hanging above on a faint ceiling ring, plus three small glowing violet (#4A148C) spheres floating freely at different heights between the speakers to suggest objects. Keep the left and right ends of every tile empty. Soft contact shadows. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 04. Integrated, short term and true peak on one loudness timeline

Now: A waveform with the integrated line drawn along its zero centerline and an unlabeled red peak marker, which misstates what integrated loudness is.

What to fix: Integrated loudness is drawn as a level line at the program average, well above the floor, not on the zero line; the true peak marker gets its label; short term is shown as a moving curve with its sliding window.

```
DAPR 3340 - Spatial Audio I
Image: Integrated, short term and true peak on one loudness timeline
File name: Loudness_Integrated_Shortterm_Truepeak.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Loudness_Integrated_Shortterm_Truepeak.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Loudness Metering
Fix: Integrated loudness is drawn as a level line at the program average, well above the floor, not on the zero line; the true peak marker gets its label; short term is shown as a moving curve with its sliding window.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram of one long glossy timeline slab seen from a gentle three quarter angle, with soft shading and depth, time running left to right and level rising upward from a flat pale gray (#F1F3F1) floor. Along the slab rises a one sided pale gray program envelope, a jagged mountain range that starts quiet at the left, swells into a loud section in the left half, falls back, swells into a smaller second section on the right, and fades out. Riding over the body of that envelope is a smooth glowing blue (#0D47A1) ribbon curve that rises and falls slowly with the program (the short term loudness); over one stretch of it sits a translucent blue glass bracket showing its short sliding window, labeled "SHORT TERM" in clear space above the bracket. Running the full length of the slab is one perfectly straight, level, solid green (#1B5E20) bar placed at the average height of the blue ribbon, clearly high above the floor and cutting through the middle of the ribbon's range, labeled "INTEGRATED" at its left end in clear space above the bar. At the single tallest spike of the envelope, which reaches higher than everything else, sits a small glossy red (#B71C1C) marker pin with its tip on the spike, labeled "TRUE PEAK" in clear space above the pin. No label touches a line or curve. No text other than the quoted labels "SHORT TERM", "INTEGRATED" and "TRUE PEAK", no numbers, no axis scale, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 05. Film audio from dialogue, effects and music through premix, final mix and printmaster to delivery

Now: A tall text heavy box chart in orange outlines; the top boxes cut off their own text mid sentence, and the Film delivery list includes DTS HD, which is a home disc format.

What to fix: All text moves to the caption (the current top boxes are truncated). In the caption's delivery lists, keep DTS HD under DVD and Blu ray only, not under Film.

```
DAPR 3340 - Spatial Audio I
Image: Film audio from dialogue, effects and music through premix, final mix and printmaster to delivery
File name: Post_Production_Mix_Workflow_Chart.jpg
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Post_Production_Mix_Workflow_Chart.jpg
Size: 1200 x 1800 px
Format: JPEG, quality 88
Used on: Final Mix Creation (Figure 1)
Fix: All text moves to the caption (the current top boxes are truncated). In the caption's delivery lists, keep DTS HD under DVD and Blu ray only, not under Film.

Create a 1200 x 1800 pixel JPEG, tall portrait. Make it a richly rendered dimensional flow diagram on a soft, evenly lit pale gray (#EEF0EE) seamless studio background, read from top to bottom, seen from a gentle three quarter angle, with soft shading and depth, like glossy 3D tiles joined by glowing cables. Top row, three glossy tiles side by side: left tile holds a generic boom microphone with a furry windscreen (dialogue), middle tile holds a small foley pit tray of gravel with a pair of shoes and a small door prop (sound effects and foley), right tile holds a generic violin resting on a stack of blank manuscript paper (music). Each tile sends a bundle of thin glowing cables straight down: green (#1B5E20) from dialogue, brown orange (#993300) from effects, blue (#0D47A1) from music. From the music tile only, one extra thin blue cable branches off to the right to a small separate tile holding a single blank album disc (soundtrack album). Second level: a wide glossy charcoal (#212121) premix slab; each bundle enters it and leaves as one thicker cable of the same color, the three kept in separate lanes. Third level: a large generic final mix console slab with rows of faders and blank panels, where the three thick cables plug in side by side. Fourth level: a printmaster slab holding a neat stack of thick multichannel master file blocks. Bottom row, fed by three cables fanning out: left tile holds a tiny cinema with a screen and rows of seats (film), middle tile holds a generic flat television beside a small broadcast tower (broadcast), right tile holds a blank optical disc beside a tiny home theater speaker set (home disc). Soft contact shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 06. Six tracks into dialogue, music and effects stems into one 5.1 output

Now: A flat routing chart where two tracks each feed both the Dialogue and Music buses and one green track feeds Effects with an orange line, which would double those tracks in the mix.

What to fix: Every source track now feeds exactly one submix bus (two dialogue tracks, two music tracks, two effects tracks), with track and cable colors matching their bus.

```
DAPR 3340 - Spatial Audio I
Image: Six tracks into dialogue, music and effects stems into one 5.1 output
File name: Surround_Session_Routing.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Surround_Session_Routing.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Output Configuration
Fix: Every source track now feeds exactly one submix bus (two dialogue tracks, two music tracks, two effects tracks), with track and cable colors matching their bus.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional routing diagram in a gentle three quarter view, read left to right, with soft shading and depth, like glossy 3D blocks joined by glowing cables. Left column: exactly six thin glossy track slabs stacked top to bottom, each with a waveform relief; the top two are green (#1B5E20), the middle two are blue (#0D47A1), the bottom two are brown orange (#993300). Middle column: exactly three thicker glossy bus blocks, green at the top, blue in the middle, brown orange at the bottom. Each track sends exactly one glowing cable of its own color to the bus of the same color, so the two green tracks go only to the green bus, the two blue tracks only to the blue bus, and the two brown orange tracks only to the brown orange bus; no cable crosses to a different bus. Right side: one tall glossy charcoal (#212121) output block. Each bus sends one thick ribbon cable made of six parallel strands into the output block. On the right face of the output block are exactly six output jacks in a column, each sending a short cable to one small speaker: five small speakers and one small subwoofer cube, arranged as a miniature 5.1 ring around a tiny listener sphere at the far right. Soft contact shadows on white. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 07. INA 5 five cardioid surround array seen from above

Now: A flat cartoon array whose C offset reads "17.5 cm / 14 in" (17.5 cm is about 7 in) and whose L capsule has a stray overlapping oval that looks like a rear lobe.

What to fix: 17.5 cm is about 7 in, not 14 in (distances go in the caption: C 17.5 cm, about 7 in, forward of the L R line; L to R 35 cm, about 14 in; rear pair 60 cm, about 24 in, apart and 60 cm, about 24 in, behind). The stray oval on L is removed; all five are plain cardioids. The page caption for Figure 14 also carries a stray "Fukada Tree" line that belongs to Figure 15.

```
DAPR 3340 - Spatial Audio I
Image: INA 5 five cardioid surround array seen from above
File name: Cardioid_Array_With_Labeled_Distances.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Cardioid_Array_With_Labeled_Distances.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 14)
Fix: 17.5 cm is about 7 in, not 14 in (distances go in the caption: C 17.5 cm, about 7 in, forward of the L R line; L to R 35 cm, about 14 in; rear pair 60 cm, about 24 in, apart and 60 cm, about 24 in, behind). The stray oval on L is removed; all five are plain cardioids. The page caption for Figure 14 also carries a stray "Fukada Tree" line that belongs to Figure 15.

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), wide landscape near 4:3. Make it a photorealistic top down product photograph, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte metal. On the white seamless surface lies a generic, unbranded surround microphone mounting frame holding exactly five identical small pencil condenser microphones with matte charcoal (#212121) bodies. The front of the array (toward the sound source) is the top of the frame. Front section: a short straight horizontal bar holds the L microphone at its left end pointing straight left and the R microphone at its right end pointing straight right; a short arm from the middle of that bar reaches forward and holds the C microphone pointing straight toward the top of the frame, the arm about half as long as the distance from the bar center to either end. Rear section: a longer arm runs straight back from the bar center to a second horizontal bar placed behind the front bar by about one and three quarter times the full L to R width; that rear bar holds two microphones spaced about one and three quarter times the L to R width apart, the left one aimed back and to the left and the right one aimed back and to the right, each about 150 degrees from straight ahead. Under each microphone a soft translucent green (#1B5E20) heart shaped cardioid pickup lobe glows on the white surface, pointing the way the microphone points, with its rear notch toward the array center; no microphone shows any extra rear lobe. Labels "L", "C" and "R" float in clear white space just beyond the tips of those three microphones. No text other than the quoted labels "L", "C" and "R", no numbers, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 08. IRT Cross of four outward facing cardioids

Now: Four flat cartoon cardioids on a thin X labeled "1 to 2 FT", which is far wider than a real IRT cross.

What to fix: Spacing corrected: a standard IRT cross uses about 20 to 25 cm (8 to 10 in) between capsules, not 1 to 2 ft; the new image shows a compact cross, and the spacing goes in the caption.

```
DAPR 3340 - Spatial Audio I
Image: IRT Cross of four outward facing cardioids
File name: IRT_Cross.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/IRT_Cross.png
Size: 1200 x 1200 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 7)
Fix: Spacing corrected: a standard IRT cross uses about 20 to 25 cm (8 to 10 in) between capsules, not 1 to 2 ft; the new image shows a compact cross, and the spacing goes in the caption.

Create a 1200 x 1200 pixel PNG with a solid white background (#FFFFFF), square. Make it a photorealistic top down product photograph, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte metal, shallow depth of field. The front (toward the sound source) is the top of the frame. At the center of the white seamless surface sits one compact generic, unbranded cross shaped microphone bar: two short straight arms crossing at right angles in an X. At the end of each arm is one identical small pencil condenser microphone with a matte charcoal (#212121) body, so the four capsules sit at the four corners of a small square. Each microphone points straight outward along its arm: front left, front right, rear left and rear right, exactly 90 degrees apart, each 45 degrees off the front to back line. Scale cue: the gap between neighboring capsules is only about one and a half times the length of one microphone body, so the cross is compact. Under each microphone a soft translucent green (#1B5E20) heart shaped cardioid pickup lobe glows on the white surface, pointing outward, rear notch toward the center of the cross. No text of any kind, no numbers, no angle marks, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 09. Location surround monitoring chain from array to headphones and speakers

Now: Flat boxes with clip art icons and text labels, and the speaker branch shows only a stereo pair for a surround monitoring chain.

What to fix: The speaker branch now shows a compact 5.1 monitoring set instead of a stereo pair, since the chain monitors a surround recording. Stage order stays microphone array, preamps, A to D conversion, multitrack recorder, monitor controller, then headphones and speakers.

```
DAPR 3340 - Spatial Audio I
Image: Location surround monitoring chain from array to headphones and speakers
File name: Location_Monitoring_Chain.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Location_Monitoring_Chain.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Monitoring while Recording in Surround
Fix: The speaker branch now shows a compact 5.1 monitoring set instead of a stereo pair, since the chain monitors a surround recording. Stage order stays microphone array, preamps, A to D conversion, multitrack recorder, monitor controller, then headphones and speakers.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a photorealistic product arrangement shot, soft studio lighting, real materials, gentle shallow depth of field, seen from a slight three quarter angle, with generic unbranded field recording gear lined up left to right across the white seamless surface and connected by real black cables. From left: a compact five capsule surround microphone array on a short stand; a small portable multichannel microphone preamp with a row of plain gain knobs; a small converter box with a row of tiny green (#1B5E20) signal lights; a compact field multitrack recorder with its small screen dark; a desktop monitor controller with one large central volume knob. From the monitor controller two cables branch: one rises up and right to a pair of generic closed back headphones resting on a small stand in the upper right, the other runs down and right to a compact surround monitoring set in the lower right made of exactly five small monitor speakers arranged in a small arc and ring plus one small subwoofer cube, finished in deep brown orange (#993300). Accent the cable path with a faint blue (#0D47A1) glow along the floor showing flow left to right. All panels blank. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 10. OCT front array ahead of a compact IRT Cross

Now: Flat cartoon capsules with an IRT cross drawn larger than the OCT and labeled "1 to 2 FT", far wider than a real IRT cross.

What to fix: IRT cross spacing corrected to about 20 to 25 cm (8 to 10 in) between capsules, not 1 to 2 ft, so the cross is drawn smaller than the OCT bar. Distances go in the caption (OCT L to R 40 to 100 cm; cross 80 to 100 cm behind).

```
DAPR 3340 - Spatial Audio I
Image: OCT front array ahead of a compact IRT Cross
File name: Surround_Microphone_Array_With_Angles.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Surround_Microphone_Array_With_Angles.png
Size: 1200 x 1600 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 8)
Fix: IRT cross spacing corrected to about 20 to 25 cm (8 to 10 in) between capsules, not 1 to 2 ft, so the cross is drawn smaller than the OCT bar. Distances go in the caption (OCT L to R 40 to 100 cm; cross 80 to 100 cm behind).

Create a 1200 x 1600 pixel PNG with a solid white background (#FFFFFF), tall portrait. Make it a photorealistic top down product photograph, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte metal. The front (toward the sound source) is the top of the frame. Near the top, a generic, unbranded straight microphone bar holds an OCT front array: a small pencil microphone at each end pointing straight outward left and right (supercardioids, each with a translucent green (#1B5E20) narrow front lobe and a small rear lobe beneath it), and at the bar center a very short forward stub holding a third small microphone pointing straight forward with a translucent green heart shaped cardioid lobe. A straight rod runs back from the bar center, about as long as the bar itself, to a compact cross shaped mount in the lower middle of the frame. That cross holds four identical small pencil microphones at the corners of a small square, the whole cross only about one third as wide as the OCT bar, each microphone pointing straight outward along its arm: front left, front right, rear left and rear right, 90 degrees apart. Under each of the four a translucent blue (#0D47A1) heart shaped cardioid lobe points outward. All bodies matte charcoal (#212121). No text of any kind, no numbers, no angle marks, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 11. INA 3 three cardioid front array

Now: Three flat cartoon cardioids whose C offset reads "17.5 cm / 14 in" (17.5 cm is about 7 in).

What to fix: 17.5 cm is about 7 in, not 14 in. Distances go in the caption (C 17.5 cm, about 7 in, forward; L to R 35 cm, about 14 in). All three are plain cardioids with no extra lobes.

```
DAPR 3340 - Spatial Audio I
Image: INA 3 three cardioid front array
File name: Three_Cardioid_Front_Array_Diagram.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Three_Cardioid_Front_Array_Diagram.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 13)
Fix: 17.5 cm is about 7 in, not 14 in. Distances go in the caption (C 17.5 cm, about 7 in, forward; L to R 35 cm, about 14 in). All three are plain cardioids with no extra lobes.

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), a wide banner (generate wide landscape; it will be cropped to a banner). Make it a photorealistic top down product photograph, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte metal. The front (toward the sound source) is the top of the frame. Across the middle of the white seamless surface lies a short, straight, generic, unbranded microphone bar. At its left end a small pencil condenser microphone points straight left, and at its right end an identical microphone points straight right. From the middle of the bar a forward arm, half as long as the distance from the bar center to either end, holds a third identical microphone pointing straight toward the top of the frame. All bodies matte charcoal (#212121). Under each microphone a soft translucent green (#1B5E20) heart shaped cardioid pickup lobe glows on the white surface, pointing the way the microphone points, with its rear notch toward the bar center; no extra rear lobes. Labels "L", "C" and "R" float in clear white space just beyond the tips of the three microphones. No text other than the quoted labels "L", "C" and "R", no numbers, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 12. Wide cardioid surround array with optional omni outriggers

Now: A flat cartoon array crowded with distance and angle text, and the drawn capsules aim about 45 degrees outward while their labels say 15 degrees off the front and rear axis.

What to fix: Aim corrected to match the stated angles: L at 345 degrees and R at 15 degrees (15 degrees off straight ahead), rear pair at 195 and 165 degrees (15 degrees off straight back) and tilted 30 degrees upward. Distances go in the caption (C 20 cm, about 8 in, forward; L and R each 60 to 75 cm, about 23 to 30 in, from center; rear pair 150 to 200 cm, about 59 to 79 in, behind and 120 to 150 cm, about 47 to 59 in, apart).

```
DAPR 3340 - Spatial Audio I
Image: Wide cardioid surround array with optional omni outriggers
File name: Wide_Cardioid.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Wide_Cardioid.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 4)
Fix: Aim corrected to match the stated angles: L at 345 degrees and R at 15 degrees (15 degrees off straight ahead), rear pair at 195 and 165 degrees (15 degrees off straight back) and tilted 30 degrees upward. Distances go in the caption (C 20 cm, about 8 in, forward; L and R each 60 to 75 cm, about 23 to 30 in, from center; rear pair 150 to 200 cm, about 59 to 79 in, behind and 120 to 150 cm, about 47 to 59 in, apart).

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a photorealistic top down product photograph of a generic, unbranded surround microphone rig, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte metal. The front (toward the sound source) is the top of the frame. Upper part of the frame: a straight horizontal bar with one small pencil microphone near each end (L and R), each aimed almost straight forward, turned outward only about 15 degrees. A short forward stub at the bar center, about one sixth of the L to R span, holds a third microphone (C) pointing straight forward. Farther out on each side, level with the bar and set apart from it, stands one omnidirectional microphone with a rounded ball tip on its own stand, drawn with a lighter pale green (#E8F5E9) disc beneath it to show it is optional. Lower part of the frame: a long rod runs straight back from the bar center, about one and a third times the L to R span, to a rear bar holding two microphones spaced about the same as the front L to R span, each aimed almost straight backward, turned outward only about 15 degrees, and visibly tipped upward toward the ceiling. Under each of the five main microphones a soft translucent green (#1B5E20) broad, wide cardioid lobe glows on the white surface, pointing the way the microphone points. All bodies matte charcoal (#212121). No text of any kind, no numbers, no angle marks, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 13. Atmos room with bed speakers, wides, subwoofer and four overhead speakers

Now: An outline speaker plan with text names where the right rear speaker is labeled "Left Rear Surround" and no LFE subwoofer is shown.

What to fix: The right rear speaker is Right Rear Surround (it was labeled Left Rear Surround), and an LFE subwoofer is added at the front. Speaker names go in the caption: Left, Center, Right, Left Wide, Right Wide, Left Surround, Right Surround, Left Rear Surround, Right Rear Surround, LFE, Left Top Front, Right Top Front, Left Top Rear, Right Top Rear.

```
DAPR 3340 - Spatial Audio I
Image: Atmos room with bed speakers, wides, subwoofer and four overhead speakers
File name: Dolby_Atmos_Speaker_Layout.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/The_Dolby_Atmos_Renderer/Dolby_Atmos_Speaker_Layout.png
Size: 1200 x 1200 px
Format: PNG, solid white background
Used on: Room Setup
Fix: The right rear speaker is Right Rear Surround (it was labeled Left Rear Surround), and an LFE subwoofer is added at the front. Speaker names go in the caption: Left, Center, Right, Left Wide, Right Wide, Left Surround, Right Surround, Left Rear Surround, Right Rear Surround, LFE, Left Top Front, Right Top Front, Left Top Rear, Right Top Rear.

Create a 1200 x 1200 pixel PNG with a solid white background (#FFFFFF), square. Make it a photorealistic architectural cutaway model of a small mixing room, seen from high above and behind the listening position at a three quarter angle, soft studio lighting, real materials: pale wood floor, matte pale gray walls cut away low so every speaker is visible, and a clear glass ceiling panel. At the center stands one empty generic studio chair facing the front wall. All speakers are generic, unbranded studio monitors aimed at the chair. Front wall: three deep blue (#0D47A1) monitors, left, center and right. Between the front wall and the side walls: one green (#1B5E20) monitor on each side (left wide and right wide). Side walls, level with the chair: one green monitor on each side (left surround and right surround). Rear corners: one brown orange (#993300) monitor on each side (left rear surround and right rear surround), mirror images of each other. On the floor just in front of the chair, near the front wall and slightly off center, one charcoal (#212121) subwoofer cube with a visible woofer cone. On the glass ceiling: exactly four pale blue (#90CAF9) monitors angled down at the chair, two above and slightly in front of the chair (top front left and top front right) and two above and slightly behind it (top rear left and top rear right). Every ear level speaker sits at the same height. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 14. Workstation feeding the Atmos renderer, which feeds speakers and headphones

Now: Flat boxes with clip art and brand name text, and the timecode arrow runs from the renderer back to Pro Tools, the reverse of how the renderer chases the DAW's timecode.

What to fix: Timecode now flows from the workstation to the renderer (Pro Tools sends LTC and the renderer follows it), not from the renderer back to Pro Tools. Product names (Pro Tools, Dolby Atmos Renderer) go in the caption.

```
DAPR 3340 - Spatial Audio I
Image: Workstation feeding the Atmos renderer, which feeds speakers and headphones
File name: Renderer_System_Topology.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/The_Dolby_Atmos_Renderer/Renderer_System_Topology.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Dolby Atmos Renderer: Window Overview and Track Bindings
Fix: Timecode now flows from the workstation to the renderer (Pro Tools sends LTC and the renderer follows it), not from the renderer back to Pro Tools. Product names (Pro Tools, Dolby Atmos Renderer) go in the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional system diagram in a gentle three quarter view, read left to right, with soft shading and depth, like glossy 3D objects joined by glowing cables. Left: a generic, unbranded workstation, a glossy green (#1B5E20) tower beside a monitor whose screen is dark and softly defocused, showing only blurred horizontal track lanes. Center: a glossy blue (#0D47A1) renderer unit, a generic rack computer, with a softly glowing brown orange (#993300) wireframe sphere floating above it dotted with small bright points (sounds placed in 3D). From the workstation to the renderer run two connections, both flowing left to right: one thick brown orange ribbon cable made of many parallel strands with light pulses moving right (beds and objects), and below it one thin dashed blue line with small pulses also moving right toward the renderer (timecode). From the right side of the renderer two glowing blue cables branch: the upper one to a miniature ring of small studio speakers around a tiny listener sphere with four more speakers on a faint ceiling ring above, the lower one to a pair of generic closed back headphones on a small stand. Soft contact shadows on white. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 3345 Spatial Audio II

#### DAPR 3345 Image 01. Credit hour rule as stacked hour blocks for lecture and lab credits

Now: A generated block chart showing only 1 CREDIT and 3 CREDITS to 9 HOURS PER WEEK, with a text legend; it does not match the shared update.

What to fix: Match the shared update: panels for 1 LECTURE CREDIT, 3 LECTURE CREDITS to 9 HOURS PER WEEK, and 1 LAB CREDIT to 3 HOURS PER WEEK. The IN CLASS and OUTSIDE OF CLASS legend moves to the caption (blue is in class or lab time, green is outside of class). This figure needs five short labels, one over the four label limit, because the shared update names all three panels.

```
DAPR 3345 - Spatial Audio II
Image: Credit hour rule as stacked hour blocks for lecture and lab credits
File name: Credit_Hour_Rule.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Course_Orientation/Credit_Hour_Rule.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Orientation: Course Description, Learning Outcomes, and Requirements (Figure 1)
Fix: Match the shared update: panels for 1 LECTURE CREDIT, 3 LECTURE CREDITS to 9 HOURS PER WEEK, and 1 LAB CREDIT to 3 HOURS PER WEEK. The IN CLASS and OUTSIDE OF CLASS legend moves to the caption (blue is in class or lab time, green is outside of class). This figure needs five short labels, one over the four label limit, because the shared update names all three panels.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a gentle three quarter view, like glossy 3D cubes on a white surface, soft studio shading and soft shadows. Three panels from left to right, separated by white space. Each cube is one hour. Panel one: exactly three cubes, one blue (#0D47A1) on top of two green (#1B5E20) side by side, with the label "1 LECTURE CREDIT" above it. Panel two: exactly nine cubes in a three by three block, the top row of three blue and the two lower rows of three green each, labeled "3 LECTURE CREDITS" above it, with a thick glossy charcoal (#212121) arrow to its right pointing to the label "9 HOURS PER WEEK". Panel three: exactly three blue cubes side by side, all blue because lab hours are spent in the lab, labeled "1 LAB CREDIT" above it, with a smaller glossy charcoal arrow to its right pointing to the label "3 HOURS PER WEEK". Labels are bold charcoal capitals in a clean sans serif, sitting in clear white space and never overlapping a cube or arrow. Count carefully: three, nine and three cubes. No text other than the quoted labels "1 LECTURE CREDIT", "3 LECTURE CREDITS", "9 HOURS PER WEEK", "1 LAB CREDIT" and "3 HOURS PER WEEK", no other numbers, no legend, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 02. 7.1.2 bed around a listener with one fixed and one moving object

Now: A flat top view circle of square speakers with text labels; it shows seven bed speakers and two heights but no LFE, so it is really a 7.0.2 layout.

What to fix: The current drawing has no LFE, so it shows 7.0.2, not 7.1.2; the new image adds one subwoofer at the front. Height speakers stay as two open squares overhead to match the caption.

```
DAPR 3345 - Spatial Audio II
Image: 7.1.2 bed around a listener with one fixed and one moving object
File name: Bed_and_Objects_7_1_2.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Spatial_Recording__Orchestral_Recording_and_Spatial_Mix/Bed_and_Objects_7_1_2.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Spatial Recording: From Multitrack to Beds and Objects (Figure 1)
Fix: The current drawing has no LFE, so it shows 7.0.2, not 7.1.2; the new image adds one subwoofer at the front. Height speakers stay as two open squares overhead to match the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram seen from a high three quarter view looking down, soft studio shading and gentle shadows. A round pale floor disc (#FCE4EC) in the center with a single charcoal (#212121) sphere at its middle for the listener, facing the top of the frame. Around the disc, on the floor, stand exactly seven small glossy red (#B71C1C) loudspeaker blocks, all angled toward the listener: three across the front (left, center, right, the center directly ahead); one on each side at about 90 to 110 degrees from center; one on each side at the rear at about 135 to 150 degrees. On the floor just in front of the disc, slightly left of center, sits one low glossy charcoal subwoofer cube, the LFE. Floating above the listener, one to the left and one to the right of overhead center, hang exactly two height speakers drawn as open square frames with hollow centers, red edged, on thin ceiling rods, with faint shadows on the disc below them. Inside the circle, front left between the left speaker and the listener, a glowing gold (#FFB300) sphere sits still, the fixed soloist object. A second gold sphere starts front right and travels toward the rear right, leaving a glowing brown orange (#993300) curved trail with an arrowhead. No text of any kind, no numbers, no channel labels, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

# Part 2. Line drawings to render again

Correct but thin: flat boxes, stick figures, default fonts. Same teaching point, richer picture.

### Shared: Classes/All (every course)

#### ALL COURSES Image 03. Nineteen day survey window on a tile track

Now: A code drawn timeline with a title, day counts and a bullet list all set as text, flat and text heavy.

```
ALL COURSES
Image: Nineteen day survey window on a tile track
File name: SRI_Survey_Window.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/Bonus__Assignments/SRI_Survey_Window.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Bonus: Student Rating of Instructor
Fix: None, same content, richer rendering (13 days before plus 6 days after equals the 19 day window).

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram seen in a gentle three quarter view from slightly above: a long straight track made of exactly 19 identical glossy square tiles laid edge to edge from left to right, each with a soft bevel and a soft contact shadow on the white floor. Between tile 13 and tile 14, counting from the left, a tall solid red (#B71C1C) post rises from the track like a finish line pole, so exactly 13 tiles sit to its left and exactly 6 tiles sit to its right. The 13 tiles before the post are a medium tint of green (#1B5E20); the 6 tiles after the post are a paler tint of the same green, so the before and after spans read at a glance. The first tile on the left has a small raised blue (#0D47A1) gate arm swung open above it, and the last tile on the right has a matching blue gate arm swung closed. Soft studio lighting, subtle reflections on the glossy tiles, calm and clean composition centered in the frame with generous white space. Quote only these three labels, in a clean bold sans serif in charcoal (#212121): "OPENS" above the first tile, "LAST DAY" above the red post, "CLOSES" above the last tile. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### ALL COURSES Image 04. Microphone to record enabled track, with the meter target zone

Now: A code drawn row of flat boxes that names specific products, with a flat meter bar and most of the teaching carried by text.

```
ALL COURSES
Image: Microphone to record enabled track, with the meter target zone
File name: BOAA_Input_Signal_Path.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/CS_623a_BOAA_Lab/BOAA_Input_Signal_Path.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: BOAA Lab: Lesson 04: Input Routing, Record Enable, & Signal Checking
Fix: None, same content, richer rendering. The interface and the recording software are shown as generic, unbranded gear; product names stay in the page text.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram in a three quarter view. Across the upper two thirds, five objects sit in a row on a pale gray floor tint, reading left to right, linked by one glowing blue (#0D47A1) path with small chevrons pointing right: (1) a generic unbranded large diaphragm condenser microphone on a short stand; (2) a loosely coiled black microphone cable with a three pin XLR connector on each end; (3) a compact generic desktop USB audio interface in charcoal (#212121) with two front combo inputs, two gain knobs and one small phantom power toggle, the cable plugged into the first input; (4) a generic laptop whose screen is dark and softly defocused, showing only one faint glowing blue track lane; (5) a round glossy record enable button glowing red (#B71C1C) with a soft pulsing halo. Across the lower third, a long horizontal level meter made of glossy illuminated segments: the leftmost 70 percent of its length is pale green, the band from 70 to 80 percent of its length is deep green (#1B5E20), glows brightest and has a small raised bracket above it marking it as the target zone, the band from 80 to 95 percent is yellow, and the last 5 percent at the right end is red (#B71C1C). Studio lighting, soft shadows, real material textures on the gear. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### ALL COURSES Image 05. Project folder tree from client down to deliverables

Now: A flat colored box chart with every folder name in small type.

```
ALL COURSES
Image: Project folder tree from client down to deliverables
File name: Folder_Hierarchy_and_Naming.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/DAW_Session_Structure/Folder_Hierarchy_and_Naming.png
Size: 1200 x 1200 px
Format: PNG, solid white background
Used on: Assignment: Asset Pipeline: Assignment, Build Your Project Repository and Asset Tracker (Figure 1); Asset Pipeline: Naming Conventions and Folder Structure (Figure 1)
Fix: None, same content, richer rendering.

Create a 1200 x 1200 pixel PNG with a solid white background (#FFFFFF), square. A richly rendered dimensional hierarchy that reads top to bottom, built from glossy tabbed file folder shapes with real thickness, soft bevels and soft shadows, joined by thin raised charcoal (#212121) rails, all seen in a slight three quarter view. Level one: a single violet (#4A148C) folder at top center. Level two: one green (#1B5E20) folder directly beneath it. Level three: one blue (#0D47A1) folder beneath that. Level four: a horizontal rail spreads to exactly four medium light blue folders side by side. Under the first (leftmost) of those four hangs one light teal green folder, and under that folder a vertical column of exactly five smaller charcoal gray folders; under the fifth gray folder a further column of exactly four small deep blue folders. Under the second of the four branch folders, a column of exactly two small light teal green folders. Under the third, a column of exactly five small light teal green folders. Under the fourth, a column of exactly three small light teal green folders. Every folder is blank on its face. Even spacing, tidy alignment, calm studio lighting. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### ALL COURSES Image 06. Where the action, callout and submit icons sit on an assignment page

Now: A code drawn page mockup with seven rows of text and three paragraphs of explanation beside it.

```
ALL COURSES
Image: Where the action, callout and submit icons sit on an assignment page
File name: Assignment_Page_Icon_Map.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/Student_Essentials/Assignment_Page_Icon_Map.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Essentials: 3E) Course Legend
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram. On the left two thirds, a tall glossy card shaped like a page stands tilted slightly back in three quarter view, holding exactly seven raised horizontal tiles stacked top to bottom, each with a sculpted glossy icon at its left end and soft blank bars in place of words. In this exact order: (1) pale red tile with a green (#1B5E20) shield bearing a white check mark; (2) pale blue tile with a blue (#0D47A1) cloud and a downward arrow; (3) pale blue tile with a clipboard holding a small checklist of ticked boxes; (4) pale yellow tile with an orange warning triangle bearing an exclamation mark; (5) pale green tile with a violet (#4A148C) light bulb; (6) pale blue tile with a round analog clock face with no numerals; (7) pale green tile with an upward arrow rising into a tray. On the right third, three small round pedestals float one above another, each holding miniature copies of one icon family: the top pedestal is blue and holds the cloud, the clipboard and the clock; the middle pedestal is red (#B71C1C) and holds the shield, the warning triangle and the light bulb; the bottom pedestal is green and holds the upload tray beside three tiny generic file tokens (a blank document, a zipped folder, an audio waveform card). Soft studio lighting and gentle reflections. No text of any kind, no letters, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### ALL COURSES Image 07. Attendance credit columns and the capped late work ramp

Now: A code drawn bar chart and line chart with percentages, axis numbers and policy sentences set as text.

```
ALL COURSES
Image: Attendance credit columns and the capped late work ramp
File name: Attendance_and_Late_Work_Chart.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/Student_Essentials/Attendance_and_Late_Work_Chart.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Essentials: 1A) Universal Class Policies & Expectations, Content
Fix: None, same content, richer rendering. All percentages and day counts move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Two richly rendered dimensional charts side by side, seen in a gentle three quarter view. Left chart: three positions on a thin charcoal (#212121) base slab. At the first position a tall glossy green (#1B5E20) column; at the second a glossy brown orange (#993300) column exactly 70 percent as tall as the green one; at the third position only a flat, empty, pale gray disc sitting on the base, showing nothing earned. Right chart: a pale floor grid with exactly 14 equal steps along its base. A thick glossy red (#B71C1C) ribbon starts at the front left corner at floor level, climbs in a perfectly straight line across the first 10 steps to a height equal to half the chart's height, then turns and runs perfectly flat for the remaining 4 steps to the right edge. A thin clear glass bar sits on top of the flat section like a lid, showing the cap. Soft studio lighting, soft shadows, clean surfaces. No text of any kind, no numbers, no percent signs, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### ALL COURSES Image 08. The four regions of a course page, lifted apart

Now: A code drawn page wireframe covered in menu words, with numbered badges.

```
ALL COURSES
Image: The four regions of a course page, lifted apart
File name: Canvas_Layout_Map.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/Student_Essentials/Canvas_Layout_Map.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Essentials: 2B) Canvas Student Orientation
Fix: None, same content, richer rendering. Region names move to the caption and are keyed by marker color.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional exploded view of a generic learning website layout, seen in three quarter view: four vertical slabs, left to right, each lifted slightly apart from its neighbors so the divisions are obvious, like glossy layered acrylic panels. Slab one: a narrow charcoal (#212121) rail holding six round white glossy icon buttons stacked vertically (a person silhouette, a gauge, a stack of books, a calendar, an envelope, a question mark). Slab two: a slightly wider pale gray column holding seven short blank text bars, the third bar highlighted in blue (#0D47A1). Slab three: a wide white main area holding three raised pale blue cards stacked vertically, each with a solid blue header strip and three blank lines of decreasing length. Slab four: a narrow pale yellow column with three blank yellow bars near its top and one small blank block lower down. Above each slab floats one glossy round marker pin: red (#B71C1C) over slab one, green (#1B5E20) over slab two, blue (#0D47A1) over slab three, brown orange (#993300) over slab four. All bars are blank shapes with no writing. Soft studio lighting, soft shadows. No text of any kind, no letters, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### ALL COURSES Image 09. Inbox as the main route to the instructor, with the other options below

Now: Six code drawn text boxes and a footnote; the idea is carried entirely by sentences.

```
ALL COURSES
Image: Inbox as the main route to the instructor, with the other options below
File name: Contacting_Your_Instructor.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/Student_Essentials/Contacting_Your_Instructor.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Essentials: 1C) Instructor Information & Office Hours
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram of glossy 3D tiles on a white floor, seen in three quarter view. Top row, left to right, three large tiles linked by a glowing blue (#0D47A1) path with chevrons pointing right: a blue tile holding a speech bubble with a question mark; a larger, brighter green (#1B5E20) tile holding a raised inbox tray with a letter dropping into it, clearly the main channel; a blue tile holding an envelope with a curved return arrow. Bottom row, set slightly back and smaller, three tiles: a blue tile holding a desk calendar with one day highlighted and two chairs facing each other (meeting by appointment); a red (#B71C1C) tile holding an envelope beside a small dimmed, unplugged power cord (email only when the platform is down); a charcoal (#212121) tile holding a phone handset, a text message bubble and a generic heart and share arrow, all three dimmed under a translucent gray circle with a diagonal slash (not used for course matters). Soft studio lighting, gentle reflections. The question mark is the only symbol; no letters. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### ALL COURSES Image 10. Student feedback loop on a circular track

Now: Four code drawn text boxes on a thin gray oval with a paragraph in the middle.

```
ALL COURSES
Image: Student feedback loop on a circular track
File name: Feedback_Loop.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/Student_Essentials/Feedback_Loop.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Essentials: 4A) Help Improve This Course
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: a glossy raised circular track, like a small ring road, lies on a white floor in three quarter view, with glowing arrows on its surface moving clockwise. Four stations sit on the ring. Top station: a blue (#0D47A1) tile holding a speech bubble and a pen resting on a small survey card. Right station: a green (#1B5E20) tile holding an open folder of cards with a magnifying glass over them. Bottom station: a red (#B71C1C) tile holding a wrench and a turning gear on top of a document page. Left station: a blue tile holding a small row of empty classroom chairs with a rising arrow above them. In the center of the ring, a small neat pile of glossy tokens standing for past changes: a thin study booklet, a calendar page with a small arrow sliding one week later, a clipboard agenda, and a short stack of presentation slides. All surfaces blank. Soft studio lighting, soft shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### ALL COURSES Image 11. Screenshots into one titled document in four steps

Now: Four code drawn text boxes with keyboard shortcuts and a mockup page, all carried by words.

```
ALL COURSES
Image: Screenshots into one titled document in four steps
File name: Screenshots_to_PDF_Workflow.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/Student_Essentials/Screenshots_to_PDF_Workflow.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Essentials: 3C) How to Make a PDF
Fix: None, same content, richer rendering. Shortcuts and menu paths stay in the page text.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram. Across the top half, four glossy tiles in a row, left to right, linked by a glowing path with chevrons pointing right: (1) blue (#0D47A1) tile with a crop selection frame with corner handles snapping over a small blank window, beside a camera shutter icon; (2) green (#1B5E20) tile with a document page where a dark blank title bar sits directly above a picture block; (3) blue tile with several loose pages sliding together into one thick single document with a folded corner; (4) red (#B71C1C) tile with that single document rising into a tray on an upward arrow. In the lower center, a larger close up of one document page, tilted back in three quarter view, holding two stacked sections: each section is a dark blank title bar directly above a framed image placeholder showing a soft defocused thumbnail. A small glossy red arrow points at the first title bar where it sits above its image. All bars are blank shapes. Soft studio lighting, soft shadows. No text of any kind, no letters, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### ALL COURSES Image 12. Seven common problems matched to the office that helps

Now: Fourteen code drawn text boxes in two columns; the matching is carried only by words.

```
ALL COURSES
Image: Seven common problems matched to the office that helps
File name: Where_to_Get_Help.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/All/Student_Essentials/Where_to_Get_Help.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Essentials: 3A) Resources & Links
Fix: None, same content, richer rendering. Office names go in the caption in the same top to bottom order.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram of exactly seven rows stacked top to bottom, each row a pair of glossy tiles joined by a short glowing arrow pointing right. Left tiles are pale gray and hold the problem; right tiles alternate between blue (#0D47A1) and green (#1B5E20) tints and hold the help. Rows in this exact order: (1) a cracked blank browser window, then a headset with a chat bubble; (2) a key, an envelope and a wireless signal fan, then a help desk counter with a small bell; (3) a sheet of paper with a pencil, then an open book with a pen and a check mark; (4) a stack of textbooks with a question mark, then two chairs at a small table with an open book; (5) a laptop, a handheld audio recorder and a camera, then a library shelf with a hanging checkout tag; (6) an empty bowl and a small house, then a glowing heart resting in a soft cushioned shield; (7) a simple circular accessibility figure with open arms, then an open door with a gentle ramp. All objects generic and blank. Soft studio lighting, soft shadows, even spacing. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 2000 Digital Audio Essentials

#### DAPR 2000 Image 15. Five stage music production chain

Now: Five flat outlined text boxes joined by arrows, with nothing to look at but the words.

```
DAPR 2000 - Digital Audio Essentials
Image: Five stage music production chain
File name: Music_Production_Roles.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Careers__Audio_Careers/Music_Production_Roles.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Careers: Recording, Music Production, Mixing & Mastering (Figure 1)
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram of exactly five glossy pedestals in a row, left to right, joined by glowing arrows pointing right. Pedestal one, blue (#0D47A1): a generic large diaphragm microphone on a short stand in front of a small guitar amplifier cabinet. Pedestal two, green (#1B5E20): closed back headphones hanging on a microphone stand fitted with a round pop filter. Pedestal three, brown orange (#993300): a glowing waveform clip cut into separate regions with small overlapping crossfades, and a pair of scissors hovering above the cut. Pedestal four, blue: a compact bank of eight glossy faders set at different heights. Pedestal five, green: a pair of tall stereo level meters standing beside a polished vinyl record and a glinting optical disc. Soft studio lighting, soft shadows, real material textures. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 16. One shared foundation branching into four career tracks

Now: A plain text box with four curved arrows to four more text boxes.

```
DAPR 2000 - Digital Audio Essentials
Image: One shared foundation branching into four career tracks
File name: Pathway_Map.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Careers__Audio_Careers/Pathway_Map.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Careers: Specialized Audio Jobs & Finding Your Career Path (Figure 1)
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram in three quarter view. On the left, a broad solid charcoal (#212121) foundation block like a cornerstone, with a softly glowing core and three small sculpted icons on its top face: a microphone, a waveform and a fader. From its right face, four glowing cables curve outward and fan right to four raised platforms stacked top to bottom along the right side. Top platform, blue (#0D47A1): an acoustic guitar and a small keyboard. Second, green (#1B5E20): a film clapperboard with blank stripes and a film reel. Third, brown orange (#993300): a small hanging line array speaker and a round ceiling speaker. Bottom, violet (#4A148C): a bare circuit board, a slim measurement microphone and a small oscilloscope with a dark screen. Each cable matches the color of the platform it reaches. Soft studio lighting, soft shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 17. Eight topic map of the final exam

Now: A plain circle with eight text boxes on colored spokes.

```
DAPR 2000 - Digital Audio Essentials
Image: Eight topic map of the final exam
File name: Final_Topic_Map.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/DAPR_2000__Final_Exam/Final_Topic_Map.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Final Exam: Study Guide (Figure 1); Final Exam: Schedule and Location (Figure 1)
Fix: None, same content, richer rendering. Topic names go in the caption, clockwise from the top.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional hub and spoke diagram seen in a gentle three quarter view. In the center, a glossy charcoal (#212121) disc with a softly glowing rim. Eight glossy spokes radiate to eight rounded square tiles evenly spaced around it, spoke colors alternating blue (#0D47A1), green (#1B5E20) and brown orange (#993300). Each tile holds one sculpted object, clockwise starting at the top: a human ear; an analog needle level meter with a blank scale; a glowing sine wave ribbon; a stepped staircase waveform made of small blocks; a generic handheld microphone; a coiled XLR cable with both connectors showing; a small compressor unit with a gain reduction needle; a single studio monitor speaker. Soft studio lighting, soft shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 18. Three mix checks: low level, mono, small speaker

Now: Flat outline speakers with abstract symbols that do not clearly show quiet playback, a mono sum or a small speaker.

```
DAPR 2000 - Digital Audio Essentials
Image: Three mix checks: low level, mono, small speaker
File name: Three_Checks.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/DAW__Your_First_Mix/Three_Checks.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: DAW: Read, Three Checks Before You Call It Done (Figure 1)
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Three product style stations in a row on a white floor, left to right, with a long glossy charcoal (#212121) arrow running beneath all three pointing right to show the order. Station one: a pair of generic studio monitors with a large round volume knob in front of them turned almost fully down, and only small faint sound rings leaving the speakers. Station two: the same pair of monitors, with a glowing beam from each speaker curving inward and merging into one single centered beam that lands on a single small speaker cone placed between them, showing both sides summed to one. Station three: one small portable cube speaker and a smartphone lying face up with a dark screen, tiny sound rings rising from both. Glowing accents in blue (#0D47A1). Photorealistic materials, soft studio lighting, shallow depth of field. Quote only these three labels, in a clean bold sans serif in charcoal (#212121), on the floor in front of each station: "LOW", "MONO", "SMALL". No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 19. Static fader line versus automated fader ride

Now: Two flat gray bars with section names and a thin line in each.

```
DAPR 2000 - Digital Audio Essentials
Image: Static fader line versus automated fader ride
File name: Automation_Timeline.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Mixing__Mixing_and_Mastering/Automation_Timeline.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mixing & Mastering: From Static to Dynamic, Breathing Life into the Mix (Figure 1)
Fix: None, same content, richer rendering. Section names go in the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram of two long glossy lanes stacked one above the other, seen in a slight three quarter view. Each lane floor is divided into exactly five equal section bands, alternating pale blue and pale green tints, standing for verse, chorus, verse, chorus, outro, and the band edges line up between the two lanes. Top lane: a perfectly flat glowing blue (#0D47A1) ribbon runs at mid height from end to end. Bottom lane: a glowing ribbon that sits low through the first band, rises smoothly to a crest in the second band, dips back down in the third, rises again in the fourth, and falls away through the fifth, shifting from green (#1B5E20) where it is low to brown orange (#993300) where it is high, with small glossy breakpoint beads at every band edge. Soft studio lighting, soft shadows. Quote only these two labels, in a clean bold sans serif in charcoal (#212121), at the left end of each lane: "STATIC" and "AUTOMATED". No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 20. Three masters before and after streaming normalization

Now: Flat stereo waveform blobs with LUFS values and row titles printed in the image.

```
DAPR 2000 - Digital Audio Essentials
Image: Three masters before and after streaming normalization
File name: Loudness_Ceiling.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Mixing__Mixing_and_Mastering/Loudness_Ceiling.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mixing: Assignment, Master Your Mix (Figure 2); Mixing & Mastering: Read About Mastering (Figure 2); Mixing & Mastering: Read, Loudness, True Peak and Streaming Targets (Figure 2)
Fix: None, same content, richer rendering. The minus 16, minus 14 and minus 8 LUFS values go in the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram of two rows of three stereo waveforms, each waveform built as a thick glossy extruded slab with two stacked channels, seen in a slight three quarter view. Top row, left to right: a blue (#0D47A1) waveform with tall sharp peaks and clear quiet valleys, very dynamic; a green (#1B5E20) waveform with moderate peaks and a fuller body; a red (#B71C1C) waveform that is a dense solid brick filling the full height with almost no variation, heavily limited. Bottom row, directly beneath: the blue and green waveforms are identical to the ones above them; the red waveform is scaled down vertically so its dense body sits at about the same average height as the green one, still flat topped and lifeless, clearly smaller than its top row twin. A thin frosted glass divider separates the two rows. Soft studio lighting, soft shadows. Quote only these two labels, in a clean bold sans serif in charcoal (#212121), rotated vertically at the left of each row: "DELIVERED" for the top row and "PLAYED BACK" for the bottom row. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 21. Mix bus aux with inserts versus a meter only master fader

Now: A flat box diagram with text labels; correct content but no sense of channel strips.

```
DAPR 2000 - Digital Audio Essentials
Image: Mix bus aux with inserts versus a meter only master fader
File name: Mix_Bus_vs_Master_Fader.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Mixing__Mixing_and_Mastering/Mix_Bus_vs_Master_Fader.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mixing & Mastering: Assignment, Your Mix Against a Reference (Figure 1)
Fix: None, same content, richer rendering (aux inserts are pre fader and master fader inserts are post fader, as the original states; keep that in the caption).

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional signal flow diagram reading left to right, seen in a slight three quarter view. On the left, exactly five small glossy source tiles stacked top to bottom, each holding one sculpted object: a drum kit, a bass guitar, an electric guitar, a small keyboard, a vocal microphone. Five glowing blue (#0D47A1) lines converge from them into a tall glossy channel strip in the middle: the mix bus, with exactly two lit insert slots near its top (one showing a small compressor needle glyph, one showing a gentle EQ curve glyph) and a fader below them. One thick glowing line runs from it right to a second tall channel strip, the master fader, whose top holds only a stereo level meter and no inserts. From the master fader a line runs right to an output tile holding a pair of studio monitors. Strips are charcoal (#212121) with real texture and soft reflections. Quote only these two labels, in a clean bold sans serif in charcoal, on the floor below each strip: "MIX BUS" under the first strip and "MASTER" under the second. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 22. Eight faders summing into one output meter banner

Now: Flat green and charcoal line art of faders and cables; clear but plain.

```
DAPR 2000 - Digital Audio Essentials
Image: Eight faders summing into one output meter banner
File name: Module_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Mixing__Mixing_and_Mastering/Module_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Mixing & Mastering: Overview
Fix: None, same content, richer rendering.

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. A richly rendered close view of exactly eight generic channel strips in a row, seen in a slight three quarter view, each a slim charcoal (#212121) strip with one round knob at its top and a glossy fader cap in a slot, the eight fader caps set at clearly different heights. From the bottom of each strip, a glowing green (#1B5E20) cable curves down and to the right, and all eight cables merge into one thick bundle that runs right into a single tall illuminated output meter at the far right, most of its segments lit green and its top few segments dark. Real materials, soft studio lighting, soft reflections, shallow depth of field. No text of any kind, no numbers, no scale markings, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 23. Monitors, listener and side wall reflections banner

Now: A flat navy top down drawing of two speakers, a head and dashed reflection lines.

```
DAPR 2000 - Digital Audio Essentials
Image: Monitors, listener and side wall reflections banner
File name: Module_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Monitoring__Psychoacoustics/Module_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Monitoring: Overview
Fix: None, same content, richer rendering.

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. A richly rendered dimensional top down view, tilted slightly, of a small control room modeled like an architect's model: raised charcoal (#212121) walls on a pale floor. Two generic studio monitors near the front wall are toed in so each points at a listening position at the lower center, marked by a simple rounded head shape seen from directly above (no face). A solid glowing blue (#0D47A1) beam runs from each monitor straight to the head. Fainter, thinner light blue beams leave each monitor toward the nearest side wall, bounce off it at matching angles, and arrive at the head from the sides, showing the first reflections. Soft studio lighting, soft shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people other than the simple head shape seen from above.
```

#### DAPR 2000 Image 24. Equilateral monitor triangle in a real control room

Now: A flat line drawing of the triangle with printed labels and a title in the image.

```
DAPR 2000 - Digital Audio Essentials
Image: Equilateral monitor triangle in a real control room
File name: Monitor_Triangle.jpg
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Monitoring__Psychoacoustics/Monitor_Triangle.jpg
Size: 1600 x 1200 px
Format: JPEG, quality 88
Used on: Studio: Read, Inside the Control Room (Figure 1); Monitoring: Read About Monitoring the Mix (Figure 1)
Fix: None, same content, richer rendering. The 60 degree angle, equal sides and tweeter height go in the caption.

Create a 1600 x 1200 pixel JPEG, landscape, a photorealistic overhead photograph looking straight down into a small, well treated control room. Dark wood floor, fabric covered acoustic panels on both side walls, a clean desk with a dark closed laptop. Two generic unbranded studio monitors on stands sit near the front wall, each toed in so its front baffle points directly at the listener's head. A person sits in a chair at the listening position, seen only as the top of the head and shoulders from above, with no face visible. The chair sits a little forward of the middle of the room. Three thin glowing green (#1B5E20) light lines are projected onto the scene forming a perfect equilateral triangle: one from the left monitor's tweeter to the right monitor's tweeter, one from each tweeter to the center of the listener's head, all three exactly equal in length. A thin glowing arc sits inside the triangle's corner at the listener, marking the angle between the two sides that meet there. Soft practical lighting, real materials, crisp focus on the triangle. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands; the one person is seen from above with no face.
```

#### DAPR 2000 Image 25. Parallel compression: dry path plus a crushed send blended back

Now: A brightly colored flat box diagram with settings and instructions written in the boxes.

```
DAPR 2000 - Digital Audio Essentials
Image: Parallel compression: dry path plus a crushed send blended back
File name: Parallel_Routing.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Processing__Compression/Parallel_Routing.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Processing: Read, Parallel Compression (Figure 1)
Fix: None, same content, richer rendering. Ratio, attack and gain reduction settings stay in the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional signal flow diagram, seen in a slight three quarter view. On the left, a glossy blue (#0D47A1) tile holding a small stack of drum waveform clips. Upper path: a straight, thick glowing green (#1B5E20) stream runs right from the drum tile to a large round glossy summing junction at the right edge, carrying a clean, untouched, spiky drum waveform. Lower path: a thinner violet (#4A148C) stream taps off the drum tile, drops down, passes a small send knob, enters a generic aux channel tile, then runs through a generic compressor unit whose gain reduction needle is pinned far over and whose small display shows a squashed, flattened waveform, then through a short aux fader, and finally rises up to join the same summing junction. The junction is brown orange (#993300). Soft studio lighting, soft shadows. Quote only these two labels, in a clean bold sans serif in charcoal (#212121): "DRY" above the upper stream and "SEND" beside the lower stream where it taps off. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 26. Echo repeats fading into a reverb tail banner

Now: A flat orange row of decaying spikes, plain and textureless.

```
DAPR 2000 - Digital Audio Essentials
Image: Echo repeats fading into a reverb tail banner
File name: Module_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Processing__Time-Based_Effects/Module_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Processing: Overview, Time Based Effects
Fix: None, same content, richer rendering.

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. A richly rendered dimensional row of glossy brown orange (#993300) sound pulses floating above a pale reflective floor, seen in a slight three quarter view. At the far left, one tall bright pulse; to its right, repeats at perfectly even spacing, each one clearly smaller and slightly softer than the one before, like echoes. Toward the right third the repeats crowd closer together and dissolve into a dense, soft, glowing haze that thins and fades to nothing at the right edge, like a reverb tail. Each pulse casts a faint reflection on the floor. Soft studio lighting. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 27. Four loudspeakers wired as two series pairs in parallel

Now: A flat schematic with a key panel and printed title; the wiring is correct but thin and hard to trace.

```
DAPR 2000 - Digital Audio Essentials
Image: Four loudspeakers wired as two series pairs in parallel
File name: Series_Parallel.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__The_Decibel/Series_Parallel.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Sound: Real Life Scenario, An Uber Decibel Problem
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered bench shot seen from above at a gentle three quarter angle: four identical generic loudspeaker drivers lying face up in a two by two grid on a pale gray board, each driver with one red terminal (positive) and one black terminal (negative) on its rim. At the upper left edge of the board, a pair of amplifier binding posts, one red and one black. Wiring, all clearly separated with no crossings hidden: a red (#B71C1C) wire runs from the red post to the red terminal of the top left driver and branches to the red terminal of the top right driver. A violet (#4A148C) jumper wire runs from the black terminal of the top left driver down to the red terminal of the bottom left driver. A second violet jumper runs from the black terminal of the top right driver down to the red terminal of the bottom right driver. A charcoal (#212121) wire runs from the black terminal of the bottom left driver and from the black terminal of the bottom right driver back to the black post. Each column is therefore one series pair, and the two columns are in parallel. Real cone textures, copper wire ends, soft studio lighting, shallow depth of field. No text of any kind, no plus or minus signs, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 28. ADSR envelope with key on and key off

Now: A small flat line chart with stage names, axis words and key markers set as text.

```
DAPR 2000 - Digital Audio Essentials
Image: ADSR envelope with key on and key off
File name: Adsr_Envelope.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Adsr_Envelope.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Sound: Supplemental, Sound, Hearing, Frequency, Amplitude & Decibel
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram seen in a slight three quarter view: a pale floor grid divided left to right into four tinted bands of these relative widths: narrow, narrow, wide, medium. A thick glossy brown orange (#993300) ribbon traces the envelope across them: a straight steep rise from floor level to its highest point across the first band, a straight fall to a lower level across the second band, a perfectly flat hold at that lower level across the third band, and a straight fall back to floor level across the fourth band. At the start of the first band, a glossy charcoal (#212121) arrow points down onto the ribbon (key pressed); at the start of the fourth band, a glossy charcoal arrow points up away from it (key released). Soft studio lighting, soft shadows. Quote only these four labels, in a clean bold sans serif in charcoal, centered above each band: "A", "D", "S", "R". No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 29. Anatomy of a sine wave: wavelength, amplitude, crest and trough

Now: A flat blue sine with many small labels and arrows.

```
DAPR 2000 - Digital Audio Essentials
Image: Anatomy of a sine wave: wavelength, amplitude, crest and trough
File name: Anatomy.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Anatomy.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Sound: Sound Wave Properties (Figure 1)
Fix: None, same content, richer rendering. Period and zero crossing move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram in a slight three quarter view: a thick glossy blue (#0D47A1) sine ribbon floating above a pale floor, running a little more than two and a half cycles from left to right, with three crests and two troughs, around a thin charcoal (#212121) center line. Small glossy brown orange (#993300) beads sit on every crest and every trough; one small green (#1B5E20) bead sits on one zero crossing. Above the wave, a green span bar with end stops runs exactly from the first crest to the second crest. A brown orange double arrow stands vertically from the center line straight up to the second crest. Soft studio lighting, soft shadows. Quote only these four labels, in a clean bold sans serif in charcoal: "WAVELENGTH" above the green span bar, "AMPLITUDE" beside the vertical arrow, "CREST" above the first crest, "TROUGH" below the first trough. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 30. Chorus as several slightly delayed copies of one wave

Now: Flat overlapping colored sine lines with plus and minus signs.

```
DAPR 2000 - Digital Audio Essentials
Image: Chorus as several slightly delayed copies of one wave
File name: Chorus.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Chorus.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Sound: Supplemental, Sound, Hearing, Frequency, Amplitude & Decibel
Fix: None, same content, richer rendering.

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), landscape. A richly rendered dimensional diagram in a three quarter view: five glossy sine ribbons, each two cycles long, layered one behind another in shallow depth like sheets of colored glass, all the same height. The front ribbon is bold charcoal (#212121), the original. Behind it, four copies, in red (#B71C1C), blue (#0D47A1) and two lighter charcoal tints, each shifted a small, different distance later in time, and each very slightly stretched or squeezed in wavelength, so their crests fan out into a soft cluster rather than lining up. A thin charcoal time axis with an arrowhead runs left to right through the middle of the stack. Soft studio lighting, soft shadows, gentle transparency where ribbons overlap. No text of any kind, no plus or minus signs, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 31. Hard clipping and soft clipping on a sine wave

Now: A small flat chart with text callouts for soft, hard and normal on a gray background.

```
DAPR 2000 - Digital Audio Essentials
Image: Hard clipping and soft clipping on a sine wave
File name: Clipping.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Clipping.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Sound: Supplemental, Sound, Hearing, Frequency, Amplitude & Decibel
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram in a slight three quarter view: a glossy blue (#0D47A1) sine ribbon runs three cycles from left to right. Two thin translucent horizontal glass planes cross the scene, one a little below the crests and one a little above the troughs, marking the limit. At every crest and trough, two versions of the clipped peak are overlaid on the faint original: a red (#B71C1C) version cut perfectly flat along the glass plane with sharp corners (hard clipping), and an orange version that bends smoothly and rounds gently into the plane (soft clipping). A thin charcoal (#212121) time axis arrow runs along the bottom left to right. Soft studio lighting, soft shadows. Quote only these two labels, in a clean bold sans serif in charcoal, near the first crest: "HARD" by the red flat top and "SOFT" by the orange rounded top. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 32. Clean wave versus the same wave clipped at the rails

Now: Thin black code drawn sine lines with faint green guide lines and short blue flats.

```
DAPR 2000 - Digital Audio Essentials
Image: Clean wave versus the same wave clipped at the rails
File name: Clipping_Distortion.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Clipping_Distortion.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Sound: Supplemental, Sound, Hearing, Frequency, Amplitude & Decibel
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Two richly rendered dimensional lanes stacked top and bottom, each with a pair of glossy green (#1B5E20) horizontal rails marking the same maximum level. Top lane: a smooth glossy charcoal (#212121) sine ribbon runs four cycles, its crests and troughs just touching the rails. Bottom lane: the same wave made larger, so it tries to go past the rails; every crest and trough is sliced perfectly flat along the rail, and each flat section glows blue (#0D47A1); the missing rounded peaks that would have gone beyond the rails are shown as faint pale gray ghost outlines above and below. Soft studio lighting, soft shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 33. High frequency short wavelength versus low frequency long wavelength

Now: A clean but flat two line chart with a title, subtitle and labels in the image.

```
DAPR 2000 - Digital Audio Essentials
Image: High frequency short wavelength versus low frequency long wavelength
File name: High_and_Low_Frequency_Wave_Comparison.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/High_and_Low_Frequency_Wave_Comparison.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Sound: Supplemental, Sound, Hearing, Frequency, Amplitude & Decibel
Fix: None, same content, richer rendering.

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), landscape. Two richly rendered glossy blue (#0D47A1) sine ribbons stacked one above the other, seen in a slight three quarter view, each floating over its own pale floor strip with a thin center line. Both ribbons start and end at exactly the same left and right positions and have exactly the same height. The top ribbon completes exactly 8 cycles; the bottom ribbon completes exactly 3 cycles. Beneath each ribbon, a glossy charcoal (#212121) span bar with end stops measures exactly one wavelength, crest to crest: short under the top ribbon, long under the bottom ribbon. Soft studio lighting, soft shadows. Quote only these two labels, in a clean bold sans serif in charcoal, at the left of each ribbon: "HIGH" for the top and "LOW" for the bottom. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 34. Tone flowing into its harmonic series banner

Now: A flat teal sine next to a row of flat alternating bars.

```
DAPR 2000 - Digital Audio Essentials
Image: Tone flowing into its harmonic series banner
File name: Module_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Module_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Sound: Overview, Sound & Hearing
Fix: None, same content, richer rendering.

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. A richly rendered dimensional composition in a slight three quarter view. On the left third, a thick glossy blue (#0D47A1) sine ribbon runs two cycles and flows directly into the base of a row of exactly fifteen glossy rectangular columns standing on a pale reflective floor across the right two thirds. The first column is the tallest, and each column after it is shorter than the one before, tapering smoothly toward the right edge, like the harmonics of a tone. Columns alternate between deep blue and a warm charcoal (#212121) tint. Soft studio lighting, soft reflections on the floor. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 35. Two identical waves 180 degrees apart cancel to silence

Now: A spreadsheet style line chart with numbered axes and gridlines, and no view of the result.

```
DAPR 2000 - Digital Audio Essentials
Image: Two identical waves 180 degrees apart cancel to silence
File name: Phase_Cancellation.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Phase_Cancellation.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Sound: Supplemental, Sound, Hearing, Frequency, Amplitude & Decibel
Fix: None, same content, richer rendering; adds the flat summed result below so the cancellation is visible.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram in a slight three quarter view with two lanes. Upper lane: two glossy sine ribbons of exactly the same size and wavelength share one center line and run just over three half cycles left to right: a blue (#0D47A1) one and a red (#B71C1C) one that is its exact upside down mirror, so every blue crest sits directly above a red trough and they cross the center line at the same points. Lower lane, below a small glossy plus shaped junction: a single perfectly flat charcoal (#212121) ribbon lying on its center line, showing that the two waves added together give nothing. Soft studio lighting, soft shadows. No text of any kind, no numbers, no axis scale, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 36. Phase offset between two waves, marked theta

Now: A flat red and blue line drawing with dashed guides; correct but plain.

```
DAPR 2000 - Digital Audio Essentials
Image: Phase offset between two waves, marked theta
File name: Phase_Offset.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Phase_Offset.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Sound: Supplemental, Sound, Hearing, Frequency, Amplitude & Decibel (used twice on this page)
Fix: None, same content, richer rendering.

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), landscape. A richly rendered dimensional diagram in a slight three quarter view: a thin charcoal (#212121) horizontal time axis with an arrowhead at the right and a short vertical axis at the left. Two glossy sine ribbons of exactly the same size and wavelength run about one and a half cycles each: a red (#B71C1C) one and a blue (#0D47A1) one that is the same wave shifted later in time by about one fifth of a cycle. At one place where the red wave crosses the axis going down, a thin vertical glass guide rises; at the matching place where the blue wave crosses the axis going down, a second guide rises; between the two guides, just below the axis, a pair of small glossy charcoal arrows point inward toward each other, marking the gap. Soft studio lighting, soft shadows. Quote only this one label, a Greek theta in a clean serif italic in charcoal, centered between the two small arrows: "θ". No text other than the quoted label, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2000 Image 37. Reflection, absorption and diffusion on real surfaces

Now: A small flat three panel graphic with titles and a color legend on a gray background.

```
DAPR 2000 - Digital Audio Essentials
Image: Reflection, absorption and diffusion on real surfaces
File name: Reflection_Absorption_and_Diffusion_Arrow_Panels.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Reflection_Absorption_and_Diffusion_Arrow_Panels.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Sound: Supplemental, Sound, Hearing, Frequency, Amplitude & Decibel
Fix: None, same content, richer rendering. The red for direct and blue for reflected key moves to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Three photoreal material samples side by side, each a square panel mounted face down as a ceiling slab at the top of its third of the frame, lit like a product shot. Each has one glossy red (#B71C1C) tube arrow rising from the lower left and striking the center of the panel's underside. Left: a smooth hard painted panel; one bold blue (#0D47A1) tube arrow leaves the strike point toward the lower right at the same angle it arrived, a mirror bounce. Center: a thick gray open cell acoustic foam panel; the red arrow sinks into the foam with a soft warm glow spreading inside it, and only one small thin faint blue arrow leaves toward the lower right. Right: a wooden stepped diffuser panel made of a row of wells of different depths; the red arrow strikes it and many small blue arrows scatter out in a wide even fan in many directions. Soft studio lighting, real textures, soft shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 2010 Core Recording

#### DAPR 2010 Image 11. Reflection, absorption and diffusion on three surfaces

Now: A three panel line drawing with thin arrows over flat bars and printed headings; correct, but it reads as clip art.

```
DAPR 2010 - Core Recording
Image: Reflection, absorption and diffusion on three surfaces
File name: Blue_Arrow_Panels_on_Flat_Surfaces.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Acoustics/Blue_Arrow_Panels_on_Flat_Surfaces.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Acoustics: What a Room Does to Sound, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a three quarter view with soft studio shading, solid color fills and real material texture. Show three equal panels side by side, left to right, each holding a thick slab of material resting on a pale blue floor tint (#E3EAF5) with a soft contact shadow. Left panel: a smooth, hard, polished slab in charcoal (#212121), like sealed plaster or lacquered hardwood. A glowing blue (#0D47A1) beam of sound, drawn as a luminous tube with faint ripple rings along it, arrives from the upper left, strikes the center of the slab, and leaves toward the upper right at exactly the mirror angle, just as bright as it arrived. Middle panel: a thick slab of soft fibrous acoustic absorber in deep green (#1B5E20) with visible mineral wool texture. The same blue beam arrives at the same angle, sinks into the surface and fades out inside the material, where a faint warm glow shows the energy turning into heat. Nothing leaves this slab. Right panel: a wooden well diffuser in brown orange (#993300) made of a row of wells cut to different depths. The same blue beam arrives at the same angle and breaks into seven thinner, dimmer beams that fan out in many directions across the whole space above the surface. Keep the arriving beam identical in all three panels so the only thing that changes is the surface. Leave generous white space between panels.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 12. The same small room set up badly and set up well

Now: Two outline room plans with labeled boxes over flat squares; the teaching is right but the drawing is sparse and text heavy.

```
DAPR 2010 - Core Recording
Image: The same small room set up badly and set up well
File name: Small_Room_Setup_Wrong_and_Right.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Acoustics/Small_Room_Setup_Wrong_and_Right.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Acoustics: Common Mistakes in a Small Control Room, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram: two identical small rectangular rooms, each longer front to back than side to side, shown as open top models in a top down three quarter view, side by side on white. The front wall of each room is at the top. Left room, the common setup: one unbranded charcoal (#212121) studio monitor is jammed into the front left corner, turned diagonally, and the other is pushed flat against the front wall, so the pair is lopsided. The listening chair sits dead center in the room. The walls are bare. A faint red (#B71C1C) glow tints the floor of this room. Right room, the better setup: both monitors are pulled forward off the front wall, placed symmetrically either side of the center line and aimed down the long axis of the room. The chair sits about four tenths of the way back from the front wall, and the two speakers and the chair form an equilateral triangle traced by a thin glowing green (#1B5E20) outline on the floor. Two thick fabric absorber panels in brown orange (#993300) hang on the left and right side walls at the first reflection points, level with the space between speakers and chair. Tall triangular bass traps in blue (#0D47A1) fabric fill all four vertical corners of the room. A faint green glow tints the floor of this room. Same room size, same furniture, only placement and treatment differ.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 13. First axial mode between two parallel walls

Now: A thin line drawing of a pressure envelope between two black bars with text labels; correct but flat.

```
DAPR 2010 - Core Recording
Image: First axial mode between two parallel walls
File name: Standing_Waves_Modes.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Acoustics/Standing_Waves_Modes.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Acoustics: What a Room Does to Sound, Figure 2
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a gentle three quarter view. At the far left and far right stand two thick, tall parallel walls in charcoal (#212121) with a matte plaster texture, facing each other across a pale blue floor strip (#E3EAF5). Between them floats a glowing translucent blue (#0D47A1) volume that shows the pressure of the first axial mode: it is tallest where it touches each wall, curves smoothly inward like half of a cosine wave, and pinches to a single point at the exact midpoint between the walls, perfectly mirror symmetric top to bottom and left to right. Place a glowing green (#1B5E20) sphere at the face of each wall where the envelope is widest (pressure peaks) and a glowing red (#B71C1C) sphere at the pinch point in the middle (the null). A thin, subtle grey line runs along the floor from wall to wall to show the room dimension. Soft shadows, clean studio lighting.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 14. Headphone cue mix path from the aux send to the performer

Now: A row of outlined boxes with arrows and capital labels; the mix bus branch leaves the channel without showing that it comes after the fader.

```
DAPR 2010 - Core Recording
Image: Headphone cue mix path from the aux send to the performer
File name: Headphone_Mix_Flow.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Operation/Headphone_Mix_Flow.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Console Operation assignment (console-operation-assignment.html), Figure 1; Console Operation: Building a Headphone Mix, Figure 2
Fix: None, same content; the control room path is now drawn leaving after the fader, which is what the caption says.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter isometric view with glossy tiles and glowing cable paths, reading left to right. At the left, a single generic console channel strip module lies on a charcoal (#212121) tile, with its knobs at the top and a long fader at the bottom. From the upper part of the strip, before the fader, a glowing blue (#0D47A1) path leaves and runs right through four more glossy tiles in a straight row: a tile holding one aux send knob with a brown orange (#993300) ring around it to mark it as pre fader; a tile holding a glowing blue bus rail (the cue bus); a tile holding a small unbranded headphone amplifier box with several volume knobs; and a final tile holding a pair of closed back studio headphones on a stand (the performer). Separately, from below the fader, a glowing green (#1B5E20) path drops down and runs right to a lower tile holding a glowing green bus rail that feeds a pair of small studio monitors (the control room mix). The blue and green paths never touch or cross. Soft shadows, clean studio light.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 15. Pre fader and post fader headphone sends with the fader pulled down

Now: Two stacked box diagrams with long printed sentences; accurate, but all of the teaching lives in the text.

```
DAPR 2010 - Core Recording
Image: Pre fader and post fader headphone sends with the fader pulled down
File name: Pre_versus_Post_Fader_Send.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Operation/Pre_versus_Post_Fader_Send.png
Size: 1000 x 1600 px
Format: PNG, solid white background
Used on: Console Operation: Common Mistakes on the ASP4816, Figure 1
Fix: None, same content, richer rendering

Create a 1000 x 1600 pixel PNG with a solid white background (#FFFFFF), tall portrait. Make it a richly rendered dimensional diagram in three quarter isometric view with glossy tiles, soft shading and glowing cable paths. Stack two matching panels, one above the other, each reading left to right. In each panel: a charcoal (#212121) input tile holding an XLR input jack, then a tile holding a physical console fader in its slot with the fader cap pulled far down toward the bottom of its travel (the same position in both panels), then a tile holding a small studio monitor (the control room mix). A grey path links the three. Top panel, green (#1B5E20) accents: the headphone send taps off the path between the input and the fader, before the fader, and runs down to a pair of studio headphones that glow bright green at full strength, untouched by the pulled down fader. Bottom panel, red (#B71C1C) accents: the headphone send taps off after the fader, and the path to the headphones is thin and dim, fading to almost nothing, so the headphones sit dark. The fader position is identical in both panels; only the tap point changes.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 16. No signal troubleshooting order from source to monitor

Now: A flowchart of six text diamonds and six text boxes; correct order, but it is a wall of words.

```
DAPR 2010 - Core Recording
Image: No signal troubleshooting order from source to monitor
File name: Troubleshooting_Order.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Operation/Troubleshooting_Order.png
Size: 1200 x 1600 px
Format: PNG, solid white background
Used on: Console Operation: Buses, Subgroups, & Troubleshooting Order, Figure 3
Fix: None, same content, richer rendering

Create a 1200 x 1600 pixel PNG with a solid white background (#FFFFFF), tall portrait. Make it a richly rendered dimensional diagram in three quarter isometric view: a single glowing path runs from the top of the image to the bottom through six glossy square tiles stacked in a vertical column, one stage per tile, in exactly this order from top to bottom. First, a tile holding an acoustic guitar with faint sound ripples (the source). Second, a tile holding a coiled XLR microphone cable with both connectors visible. Third, a tile holding a rotary input selector switch. Fourth, a tile holding a large gain knob. Fifth, a tile holding a row of routing assign buttons with one lit. Sixth, a tile holding a small studio monitor speaker. The path enters the top tile from a dark red (#B71C1C) glowing start disc (no signal) and leaves the bottom tile into a bright green (#1B5E20) glowing disc (signal found). Tiles are charcoal (#212121) with blue (#0D47A1) glowing edges. From the right side of each tile, a short red branch leads to a small matching tile holding a single chrome wrench, meaning fix it here and stop. The main path only moves downward, one stage at a time.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 17. Engineer's hands at a console, gain first

Now: A cartoon console with white cartoon hands and a bullet list printed beside it.

```
DAPR 2010 - Core Recording
Image: Engineer's hands at a console, gain first
File name: Wiki_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Operation/Wiki_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Console Operation: Overview (page banner)
Fix: None, same content, richer rendering

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide banner. Photorealistic studio photograph, shallow depth of field, soft top light. Seen from just behind and above an engineer's shoulders, a generic unbranded analog recording console fills the left two thirds of the frame, with rows of channel strips, knobs, lit buttons and long faders, two unbranded nearfield monitors on the meter bridge and small LED meter ladders glowing green (#1B5E20). The engineer's left hand rests on a gain knob at the very top of one channel strip, and the right hand rests on a fader further down: gain first. Sleeves in charcoal (#212121). Any screen in view is dark or softly defocused. The scene fades smoothly into pure white toward the right third of the banner, leaving calm empty space.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No faces; only forearms and hands.
```

#### DAPR 2010 Image 18. One microphone through ten stages to Pro Tools and back

Now: Ten outlined text boxes in a snake with a legend and a dashed note; accurate, but it is a table drawn as boxes.

```
DAPR 2010 - Core Recording
Image: One microphone through ten stages to Pro Tools and back
File name: One_Microphone_Every_Stage.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Signal_Flow/One_Microphone_Every_Stage.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Console Signal Flow: Worked Example: One Microphone, Every Stage, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide banner. Make it a richly rendered dimensional diagram in three quarter isometric view: ten glossy square tiles joined by one glowing cable path. The top row holds five tiles running left to right; the path drops down at the right end; the bottom row holds five tiles running right to left. Top row, left to right: tile one, a large diaphragm condenser microphone on a short stand with its XLR cable seated; tile two, a wall box plate with a row of XLR jacks; tile three, a patch bay section with two rows of jacks joined by a short patch cable; tile four, a console mic preamp section with a gain knob and an unlit phantom power button; tile five, a filter knob beside an insert button. Bottom row, right to left: tile six, a short channel fader; tile seven, a row of bus assign buttons with one lit; tile eight, a second patch bay section with two rows of jacks; tile nine, a computer monitor that is dark and softly defocused, with a small glowing red record arm dot in front of it; tile ten, a long console fader. Color the tiles by where they live: tiles one, two, three and eight in charcoal (#212121); tiles four, five, six and seven in blue (#0D47A1); tiles nine and ten in green (#1B5E20). The glowing path passes through every tile in order and never skips one.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 19. A single channel strip with the signal running top to bottom

Now: A cartoon channel strip beside a printed bullet list.

```
DAPR 2010 - Core Recording
Image: A single channel strip with the signal running top to bottom
File name: Wiki_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Signal_Flow/Wiki_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Console Signal Flow: Overview (page banner)
Fix: None, same content, richer rendering

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide banner. Photorealistic product photograph on a seamless white background, crisp studio lighting and soft shadows. A single generic unbranded console channel strip module stands upright, turned slightly into three quarter view, placed left of center. From top to bottom it has an XLR input jack, a small switch row, four rotary knobs with one green (#1B5E20) cap, a few square buttons, and a long fader at the bottom. A thin glowing green line of light enters the XLR jack at the top, runs down the face of the strip past each control, and leaves at the bottom into a short glowing bus rail that extends to the right. The rest of the banner is clean white space.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 20. Four stages of preparing a drum kit

Now: A four column infographic with outline drums, bullet lists and a title; dense with text and thin line art.

```
DAPR 2010 - Core Recording
Image: Four stages of preparing a drum kit
File name: Kit_Preparation.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Drum_Recording/Kit_Preparation.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Drums: Preparing the Kit, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic, four equal bench shot panels in a row, left to right, each on a seamless white sweep with soft studio light and shallow depth of field. Across the top of each panel runs a thin solid color band: green (#1B5E20), blue (#0D47A1), brown orange (#993300), red (#B71C1C), in that order. Panel one, hardware: a rack tom on its mount with a drum key fitted to one tension rod, a tightened wing nut on a cymbal stand, a small felt washer and a tiny oil bottle beside a bass drum pedal spring. Panel two, heads and tuning: a top down view of a drum head with eight lugs evenly spaced around the rim and a drum key on one lug; a thin glowing blue line traces the tuning order, and every step crosses the head to the lug directly opposite, forming an eight point star, never stepping to the neighboring lug. Panel three, damping: two identical toms side by side; the left one bare with faint wavy ring lines hovering above the head, the right one with one small clear gel pad near the edge of the head and a calm surface. Panel four, the snare: a snare drum tilted up to show both heads, with the snare wires stretched across the bottom head and the strainer visible on the shell. Clean, well lit gear, no clutter.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 21. Overheads at equal and unequal distances from the snare

Now: Two flat panels with dots, dashed lines and printed inch values; correct but schematic.

```
DAPR 2010 - Core Recording
Image: Overheads at equal and unequal distances from the snare
File name: Overheads_Equal_Distance_to_Snare.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Drum_Recording/Overheads_Equal_Distance_to_Snare.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Drums: Worked Example: Checking the Overheads & the Snare, Figure 1
Fix: None, same content, richer rendering; the 44 and 52 inch values move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic, two equal panels side by side, each a front view from slightly above of one snare drum on its stand with a pair of small pencil condenser microphones on booms above it, seamless white background, soft studio light. In each panel a taut glowing string runs from each microphone capsule to the center of the snare head. Left panel: green (#1B5E20) strings, the two microphones mirror symmetric over the snare, both strings visibly the same length, and a small glowing green sphere floats exactly midway between the two microphones to show the snare image sitting in the center. Right panel: red (#B71C1C) strings, the left microphone clearly closer to the snare so its string is visibly shorter, about one sixth shorter than the right one, and the small glowing sphere has slid toward the nearer left microphone. Put the letter "L" beside the left microphone and "R" beside the right microphone in both panels, in small clean charcoal (#212121) type.

No text other than the quoted labels "L" and "R", no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 22. Tuning in opposite pairs beside a drum prep checklist laid out on the bench

Now: A numbered lug diagram beside a five line printed checklist with green ticks; all of the checklist is text.

```
DAPR 2010 - Core Recording
Image: Tuning in opposite pairs beside a drum prep checklist laid out on the bench
File name: Tuning_and_Prep.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Drum_Recording/Tuning_and_Prep.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Drums: Preparing the Kit, Figure 2
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic bench photography on a seamless white surface, soft top light, shallow depth of field. Left half: a straight top down view of a drum with a white coated head and eight chrome lugs evenly spaced around the hoop, a drum key resting on the top lug. Four glowing straight lines cross the head, each joining one lug to the lug directly opposite it, forming an eight point star through the center; the first pair (top to bottom) glows brightest blue (#0D47A1) and each following pair is a slightly lighter tint of blue, so the order reads as opposite pairs, never around the rim. Right half: a tidy flat lay of five small groups arranged in a neat vertical column, each group sitting on its own pale green (#E8F1E8) tile with a small solid green (#1B5E20) check mark shape at its left edge: a fresh drum head beside a drum key; a clear gel damping pad beside a small roll of cloth tape; a drum key fitted to a cymbal stand wing nut; a small oil bottle beside a bass drum pedal spring; a pair of fresh drumsticks, a spare folded drum head and a spare rectangular battery.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 23. Level ladder from noise floor to clipping

Now: One flat colored bar with leader line labels; correct, but the headroom zone is filled solid red as if it were the danger zone itself.

```
DAPR 2010 - Core Recording
Image: Level ladder from noise floor to clipping
File name: Headroom_Noise_Floor.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Gain_Staging/Headroom_Noise_Floor.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Gain Staging assignment (gain-staging-assignment.html), Figure 1; Gain Staging: Headroom, Noise Floor, & Where to Set Level, Figure 1
Fix: None, same content; headroom is now drawn as clear safe space under a red ceiling, matching the caption's point that headroom is not wasted.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram: a tall glossy column built from stacked blocks, standing in three quarter view at the center of the frame on a soft shadow. From bottom to top: a short charcoal grey (#424242) block with a visible fuzzy grain texture like static (the noise floor); a tall solid green (#1B5E20) block (the usable range); a thin bright blue (#0D47A1) slab (nominal level); a tall block of clear glass with a faint pale red tint (#F6D5D5), empty and calm (headroom); and on top a hard, solid red (#B71C1C) ceiling plate (clipping). Beside the column, a glowing white and green audio waveform ribbon rides at the height of the blue slab, with its tallest peaks rising into the clear glass zone but stopping short of the red ceiling. Clean studio lighting, soft reflections.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 24. Bass or guitar split at the DI into a direct track and a miked amp track

Now: A text box flow chart with an orange paragraph printed across the bottom.

```
DAPR 2010 - Core Recording
Image: Bass or guitar split at the DI into a direct track and a miked amp track
File name: Detailed_Signal_Chain_with_Orange_Note.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Guitar_and_Bass_Recording/Detailed_Signal_Chain_with_Orange_Note.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Guitar & Bass: Acoustic Guitar & Bass, Figure 1
Fix: None, same content, richer rendering; the timing note moves to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter isometric view, reading left to right, with real looking gear on glossy tiles and glowing cable paths. At the left, a generic unbranded electric bass guitar on a stand, cabled into a small DI box. The DI box has two outputs. From its unbalanced thru jack, a thin brown orange (#993300) cable runs up and right to an upper row: a bass amplifier head on a speaker cabinet, a dynamic microphone on a short stand a few inches in front of the grille with faint sound ripples crossing the gap of air, then a preamp unit, then a tile holding a dark, softly defocused screen with a waveform lane. From the DI box's balanced XLR output, a thicker blue (#0D47A1) cable runs along a lower row to a second preamp unit and on to its own tile with a dark defocused screen and waveform lane. At the far right, the two waveform lanes are shown stacked as glossy ribbons: the lower blue one starts exactly on a vertical guide line, and the upper brown orange one starts slightly later, a small visible offset, showing that the miked path arrives later. The upper path is visibly longer than the lower path.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 25. One performance recorded two ways, DI and amp

Now: A plain box and arrow split with small colored captions.

```
DAPR 2010 - Core Recording
Image: One performance recorded two ways, DI and amp
File name: Instrument_Split_to_DI_and_Amp.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Guitar_and_Bass_Recording/Instrument_Split_to_DI_and_Amp.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Guitar and bass assignment (guitar-bass-assignment.html), Figure 1
Fix: None, same content; the split is shown at the DI box's thru jack, the way it is done in the studio.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic high three quarter view of a studio floor setup on a seamless white sweep, soft studio light. On the left, a generic unbranded electric bass leans on a stand, with its cable running to a small DI box on the floor. Two cables leave the DI box. Upper path: a brown orange (#993300) cable from the DI's thru jack runs to a bass combo amplifier; a dynamic microphone on a short stand faces the speaker grille from a few inches away; a faint haze of room ambience surrounds the amp. The microphone's cable continues right to the edge of a console, into one channel. Lower path: a green (#1B5E20) XLR cable from the DI's balanced output runs straight right into the neighboring console channel, clean and direct with no microphone or room. The console at the right is a generic unbranded section showing two adjacent channel strips, the brown orange cable landing in one and the green cable in the other.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 26. Guitar speaker seen face on with microphone positions from center to edge

Now: Concentric circles with numbered triangles and long printed descriptions; it shows three positions while the page alt text says four.

```
DAPR 2010 - Core Recording
Image: Guitar speaker seen face on with microphone positions from center to edge
File name: Speaker_Cone_with_Numbered_Blue_Callouts.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Guitar_and_Bass_Recording/Speaker_Cone_with_Numbered_Blue_Callouts.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Guitar & Bass: Electric Guitar & the Speaker Cone, Figure 1
Fix: None, same three positions (dust cap, halfway out, cone edge), richer rendering. Note: the page alt text says four positions; either edit the alt text to three or tell Claude to add a fourth marker at the edge of the dust cap.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic close up product photograph of a single generic unbranded guitar speaker, seen straight on, with the grille cloth removed, placed in the left half of the frame on a seamless white background, crisp studio light. Show the real parts: a dark domed dust cap at the center, a ribbed paper cone, a flexible surround at the outer edge, and the metal basket rim with mounting holes. Mark three positions with small glowing blue (#0D47A1) disc markers lying on a straight line from the center toward the lower edge: one on the center of the dust cap, one halfway out across the cone, and one at the outer edge of the cone just inside the surround. Behind the markers, lay a very soft radial glow over the cone that is bright and cool at the center and fades to a warm, darker tone toward the edge, suggesting bright at the center and dark at the edge. The right half of the frame is clean white space.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 27. Matched impedance versus bridging, shown as delivered voltage

Now: Two schematic circuits with printed ohm values and a red and green sentence under each; correct but schematic.

```
DAPR 2010 - Core Recording
Image: Matched impedance versus bridging, shown as delivered voltage
File name: Bridging_versus_Matching.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Impedance_and_Voltage/Bridging_versus_Matching.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Impedance: What It Is & Why Bridging Replaced Matching, Figure 2
Fix: None, same content, richer rendering; the ohm values move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter view, two panels side by side. Each panel is a small physical circuit laid out on a pale grey tile: a glossy charcoal (#212121) signal source block with a sine wave emblem embossed on its face, a series resistor (the source impedance) as a large realistic resistor component, and a load resistor across the output, all joined by glowing blue (#0D47A1) wires, with a small ground post. Draw every resistor's body length in proportion to its impedance. Left panel, matching: the source resistor and the load resistor are the same length. Right panel, bridging: the source resistor is short and the load resistor is very long, many times longer. Beside the load in each panel stands a glass gauge tube showing the voltage that arrives: in the left panel the tube is filled exactly halfway with glowing red (#B71C1C); in the right panel it is filled almost to the top with glowing green (#1B5E20).

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 28. Five studio connections and what each one needs

Now: A five row table of text boxes, arrows and orange or red pills; accurate but entirely text.

```
DAPR 2010 - Core Recording
Image: Five studio connections and what each one needs
File name: Five_Connection_Cases.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Impedance_and_Voltage/Five_Connection_Cases.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Impedance assignment (impedance-assignment.html), Figure 1; Impedance: Connecting Real Studio Gear Without Damage, Figure 1
Fix: None, same content, richer rendering; levels and impedances move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram: five horizontal rows stacked top to bottom, each row reading left to right on a long pale grey glossy tray in three quarter view. Each row has a source object at the left, an in between object in the middle, a destination object at the right, and a round glossy status gem at the far right. Row one: the pickup area of a generic electric guitar body with its jack and cable, then a small DI box, then a line input jack panel; brown orange (#993300) gem. Row two: a male XLR plug from a rack unit's line output, then an empty gap with a direct cable and no box, then a microphone input jack with small red sparks of overload; red (#B71C1C) gem with a white cross shape. Row three: a pair of RCA plugs from a consumer device, then a small level converter box, then an XLR professional input; brown orange gem. Row four: an XLR professional output, then a small inline pad box, then a pair of RCA consumer input jacks; brown orange gem. Row five: a line level XLR output, then a small reamp box, then the input jack of a guitar amplifier; brown orange gem. Keep every row aligned in the same three columns.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 29. Every connection is a voltage divider

Now: A schematic divider beside a printed three row table and a sentence of text.

```
DAPR 2010 - Core Recording
Image: Every connection is a voltage divider
File name: Resistor_Divider_with_Blue_Header_Table.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Impedance_and_Voltage/Resistor_Divider_with_Blue_Header_Table.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Impedance: What It Is & Why Bridging Replaced Matching, Figure 1
Fix: None, same content, richer rendering; the percentages move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter view. Left third: a physical voltage divider standing upright on a pale grey tile: a glossy charcoal (#212121) source block with a sine wave emblem, a wire rising to a top resistor (the source impedance), a glowing tap point below it where a short glowing blue (#0D47A1) output wire leaves to the right, then a bottom resistor (the load impedance) down to a ground post. Right two thirds: three glass gauge tubes standing in a row on their own tiles, each with a small pair of resistors at its base showing the ratio by body length. First tube: bottom resistor ten times longer than the top one, tube filled nine tenths full with glowing green (#1B5E20). Second tube: both resistors equal, tube filled exactly half with glowing blue (#0D47A1). Third tube: bottom resistor one tenth the length of the top one, tube filled only about one tenth with glowing red (#B71C1C). Soft studio light and reflections.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 30. Three sources, the wrong input and the right input for each

Now: Six framed text rows with red crosses and green ticks; the teaching is correct but it is all words.

```
DAPR 2010 - Core Recording
Image: Three sources, the wrong input and the right input for each
File name: Right_and_Wrong_Connections.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Impedance_and_Voltage/Right_and_Wrong_Connections.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Impedance: Worked Example: Three Sources, Three Right Inputs, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram: two columns of three rows, each row a glossy tray in three quarter view reading left to right. The left column trays have a thin red (#B71C1C) edge glow and a red gem with a white cross shape at the right end; the right column trays have a thin green (#1B5E20) edge glow and a green gem with a white check mark shape. The three rows are the same three sources in both columns. Row one source: the body of a generic electric guitar with its cable. Wrong: the cable goes straight into a line input jack, and the glowing signal along it is dull and muffled, a dim brownish glow. Right: the cable goes into a small DI box, then an XLR cable into a microphone input, with a bright clean glow. Row two source: the XLR line output of a rack unit. Wrong: it plugs into a microphone input that throws red overload sparks. Right: it plugs into a line input with a steady even glow. Row three source: a pair of RCA outputs from a consumer device. Wrong: into a professional input with the input gain knob turned fully down, the glow faint and thin. Right: into the same professional input with the gain knob turned well up, the glow full and even.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 31. Two bridging connections that are safe and one that destroys the input

Now: Three text rows with check and cross badges and an orange paragraph across the bottom.

```
DAPR 2010 - Core Recording
Image: Two bridging connections that are safe and one that destroys the input
File name: Safe_Interconnection.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Impedance_and_Voltage/Safe_Interconnection.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Impedance: Connecting Real Studio Gear Without Damage, Figure 2
Fix: None, same content, richer rendering; impedance values and the ten to one rule move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram: three horizontal glossy trays stacked top to bottom in three quarter view, each reading left to right with a source, a cable and a destination, and a status gem at the far right. At each end, show the impedance as a realistic resistor component whose body length is in proportion to its value. Row one: a dynamic microphone with a short resistor at its output, a blue (#0D47A1) XLR cable, and a preamp input with a resistor over ten times longer; steady even glow; green (#1B5E20) gem with a white check mark shape. Row two: a rack unit line output with a very short resistor, a blue XLR cable, and a line input with a far longer resistor; steady even glow; green gem with a white check mark shape. Row three: the heavy red and black binding post speaker terminals of a power amplifier, a thick speaker cable, and a delicate line input jack on a circuit board that is scorched, with sparks and a thin wisp of smoke; red (#B71C1C) gem with a white cross shape.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 32. Low source impedance feeding a high load impedance

Now: Two grey boxes with resistor symbols and a green line beside a printed bullet list.

```
DAPR 2010 - Core Recording
Image: Low source impedance feeding a high load impedance
File name: Wiki_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Impedance_and_Voltage/Wiki_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Impedance: Overview (page banner)
Fix: None, same content, richer rendering

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide banner. Make it a richly rendered dimensional diagram in three quarter view, occupying the left two thirds of the banner. At the left, a glossy charcoal (#212121) block (the source) with a glass window showing a short, stubby resistor inside. At the right, a matching glossy charcoal block (the load) with a glass window showing a resistor about ten times longer. A thick cable glowing green (#1B5E20) joins the two blocks through chrome jacks, bright and steady along its whole length. Soft shadow, clean studio light. The right third of the banner is clean white space.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 33. The six numbers on a microphone spec sheet, shown as what they measure

Now: A six row text table with blue leader lines to six printed explanations.

```
DAPR 2010 - Core Recording
Image: The six numbers on a microphone spec sheet, shown as what they measure
File name: Spec_Sheet_Anatomy.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Microphones/Spec_Sheet_Anatomy.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Microphones assignment (microphones-assignment.html), Figure 1; Microphones: Reading a Specification Sheet, Figure 1
Fix: None, same content, richer rendering; the six names move to the caption in the same order.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram: six glossy square tiles in two rows of three, in three quarter view, each holding one small 3D scene, read left to right, top row then bottom row. Tile one (sensitivity): a microphone capsule receiving gentle sound ripples, wired to a small analog needle meter whose needle swings well up. Tile two (self noise): a microphone capsule in a dark hush, surrounded by a very faint fine sparkle of grain like hiss. Tile three (maximum level): a strong burst of sound waves striking a hard red (#B71C1C) ceiling plate just above a capsule. Tile four (frequency response): a glowing blue (#0D47A1) curve ribbon, flat across the middle and gently rolling off at both ends, floating over a grid floor with no labels. Tile five (output impedance): a female XLR cable connector sliding into a chrome input jack. Tile six (polar pattern): a microphone capsule surrounded by a translucent glowing green (#1B5E20) heart shaped cardioid pickup lobe, largest in front and pinched to nothing behind. Tiles in charcoal (#212121) with thin blue edge glow, soft shadows.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 34. Dynamic, condenser and ribbon microphones side by side

Now: Three cartoon microphones beside a printed bullet list.

```
DAPR 2010 - Core Recording
Image: Dynamic, condenser and ribbon microphones side by side
File name: Wiki_Banner.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Microphones/Wiki_Banner.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Microphones: Overview (page banner)
Fix: None, same content, richer rendering

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide banner. Photorealistic product photograph on a seamless white background, soft studio light, gentle reflections. Three generic unbranded microphones stand side by side in the left two thirds of the frame, at similar heights: a handheld dynamic vocal microphone with a round steel mesh ball grille and a matte charcoal (#212121) body; a large diaphragm condenser in a spider shock mount with a rounded mesh head; and a ribbon microphone in a U shaped yoke mount with a tall rectangular slotted grille. The right third of the banner is clean white space.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 35. XY, Blumlein and mid side coincident pairs with their pickup lobes

Now: Thin polar outlines in three panels with printed headings, angles and a footnote sentence.

```
DAPR 2010 - Core Recording
Image: XY, Blumlein and mid side coincident pairs with their pickup lobes
File name: Coincident_Arrays.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Miking_Techniques/Coincident_Arrays.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Miking Techniques assignment (miking-techniques-assignment.html), Figure 1; Miking Techniques: Five Stereo Arrays, Figure 2
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram, three equal panels side by side, each a top down view tilted slightly into three quarter, with the front (the sound source direction) at the top of the frame. In every panel, two microphone capsules sit stacked at one single point in the middle of the panel, and each capsule's pickup pattern is drawn as a translucent glowing 3D lobe: one in charcoal (#212121) glass and one in blue (#0D47A1) glass. Left panel, XY: two heart shaped cardioid lobes sharing the center point, one aimed forward left and one aimed forward right, a right angle apart, each pinched to nothing at its rear. Middle panel, Blumlein: two figure eight lobes, each a pair of equal round lobes front and back, crossed at a right angle so the four lobes point forward left, forward right, rear left and rear right. Right panel, mid side: one charcoal cardioid lobe aimed straight forward, and one blue figure eight lobe aimed sideways, its left lobe in solid saturated blue and its right lobe in a pale blue tint (#BBD0EE) to show the two lobes have opposite polarity. A faint thin dashed line runs from the shared center point along each capsule's axis. Soft shadows on a pale grey floor.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 36. The three to one rule for two sources and two microphones

Now: Two colored dots, two triangles and printed unit labels with a dashed leakage line; correct but minimal.

```
DAPR 2010 - Core Recording
Image: The three to one rule for two sources and two microphones
File name: Untitled_Leakage_Path_Spacing_Diagram.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Miking_Techniques/Untitled_Leakage_Path_Spacing_Diagram.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Miking Techniques: Phase, Polarity, & the Three to One Rule, Figure 2
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a high three quarter view on a floor made of equal square glossy tiles in pale grey, each tile one unit. Near the bottom of the frame sit two small generic guitar amplifiers facing the camera side, spaced apart: the left one with red (#B71C1C) grille cloth (source A), the right one with blue (#0D47A1) grille cloth (source B). In front of each amplifier, exactly one floor tile away, a small dynamic microphone on a short stand points at its own amplifier's grille. The two microphones are exactly three floor tiles apart from each other. Highlight the one tile between each microphone and its amplifier in glowing green (#1B5E20), and highlight the row of three tiles between the two microphones in glowing blue. A faint dashed grey glowing line runs diagonally from source A to the microphone in front of source B, the leakage path, visibly longer than either green distance.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 37. What a plug in the top jack does in full normal, half normal and open bays

Now: Three columns of outlined jack boxes with printed labels and a title; correct but text heavy.

```
DAPR 2010 - Core Recording
Image: What a plug in the top jack does in full normal, half normal and open bays
File name: Normalling_Columns_with_Plain_Jack_Boxes.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Patch_Bays/Normalling_Columns_with_Plain_Jack_Boxes.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Patch Bays: Worked Example: The Patch That Killed the Vocal, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic cutaway rendering, three columns side by side, two rows. Each cell shows one vertical pair of chrome quarter inch patch bay jacks on a short brushed black panel section, the upper jack being the source output and the lower jack the destination input, with the panel cut away so the internal link between the two jacks is visible as a wire. A live, intact link glows green (#1B5E20). A broken link shows a clear gap with a small red (#B71C1C) spark at the break. Patch cables are blue (#0D47A1). Top row, nothing plugged in: left column full normal, link glowing green; middle column half normal, link glowing green; right column open, no link wire at all. Bottom row, a blue patch cable plugged into the upper jack: left column full normal, the link is broken with a red gap and the signal only leaves through the patch cable; middle column half normal, the link still glows green to the lower jack and a green glow also runs out along the patch cable, a tap that leaves the normal intact; right column open, no link, the signal leaves only through the patch cable. Thin pale grey gutters separate the columns.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 38. Full normal, half normal and open with no plug, a top plug and a bottom plug

Now: A three by three table of drawn jacks and blue cables with printed row, column and cell labels.

```
DAPR 2010 - Core Recording
Image: Full normal, half normal and open with no plug, a top plug and a bottom plug
File name: Normalling_Grid_with_Blue_Patch_Cables.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Patch_Bays/Normalling_Grid_with_Blue_Patch_Cables.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Patch Bays: Normalling & What a Cable Interrupts, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic cutaway rendering arranged as a clean three by three grid of cells with thin pale grey gutters. Columns left to right: full normal, half normal, open. Rows top to bottom: nothing plugged in, a plug in the upper jack, a plug in the lower jack. Every cell shows the same vertical pair of chrome quarter inch patch bay jacks on a brushed black panel section, upper jack the source output and lower jack the destination input, with the panel cut away to reveal the internal link wire between them. An intact link glows green (#1B5E20); a broken link shows a clear gap with a small red (#B71C1C) spark; patch cables are blue (#0D47A1) and leave toward the right. Full normal column: top row link intact; middle row plug in upper jack, link broken; bottom row plug in lower jack, link broken. Half normal column: top row link intact; middle row plug in upper jack, link still intact and glowing, with green glow also leaving along the patch cable; bottom row plug in lower jack, link broken. Open column: no link wire in any row; the middle and bottom rows show the blue cable in the upper and lower jack respectively. The half normal middle cell should be the only plugged cell with an intact green link.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 39. Punch in with pre roll and post roll: what is heard and what is recorded

Now: Three rows of text boxes with dashed punch lines and red labels.

```
DAPR 2010 - Core Recording
Image: Punch in with pre roll and post roll: what is heard and what is recorded
File name: Punch_In_With_Pre_and_Post_Roll.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Pro_Tools_for_Tracking/Punch_In_With_Pre_and_Post_Roll.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Tracking: Worked Example: Punching In One Vocal Line, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter view: three long glossy horizontal lanes stacked top to bottom, time running left to right, all cut by the same two tall translucent vertical gate planes glowing red (#B71C1C), the punch in on the left and the punch out on the right. Top lane, the timeline: a light grey segment before the first gate (pre roll), a solid blue (#0D47A1) segment between the gates (the punch range), and a light grey segment after the second gate (post roll). Middle lane, what the performer hears: a charcoal grey (#424242) waveform ribbon of the existing take runs before the first gate and after the second gate, and between the gates a bright green (#1B5E20) live waveform ribbon, with a small pair of headphones floating above the lane. Bottom lane, what is recorded: empty clear glass before and after the gates, and a solid red waveform ribbon only between the gates, with a small glowing red record dot above it. All three lanes are the same length and line up exactly at both gates.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 40. An assistant's session from load in to teardown

Now: A thin timeline with four dots and printed lists under each stage plus a bold sentence.

```
DAPR 2010 - Core Recording
Image: An assistant's session from load in to teardown
File name: Assistant_Timeline.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Session_Delivery_and_Archiving/Assistant_Timeline.png
Also overwrite: /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Etiquette/Assistant_Timeline.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Studio Etiquette assignment (studio-etiquette-assignment.html), Figure 1; Studio Etiquette: What an Assistant Actually Does, Figure 1; Session Delivery: Overview (page banner)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter view: a long glowing path runs left to right across the frame and passes over four raised glossy platforms, each holding a small detailed studio scene. First platform, green (#1B5E20), before anyone arrives: a tidy live room corner with chairs set, cables run neatly along the floor, and headphones hung on hooks at each position. Second platform, green, setup: microphones on stands with small blank tape labels on the stands, a talkback microphone on the console edge, and a meter bridge with softly glowing green meters. Third platform, blue (#0D47A1), during the session: the edge of a generic console with a notepad and pen resting beside it, the page blank. Fourth platform, violet (#4A148C), after: a small external backup drive with a glowing activity light on the console, cables coiled over under and hung on a hook, chairs pushed in. The first and last platforms sit slightly apart from the middle two, so the assistant's work visibly extends before and after the session.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 41. Four takes comped into one track

Now: Four white bars with one colored section each above a colored comp bar, joined by dashed lines.

```
DAPR 2010 - Core Recording
Image: Four takes comped into one track
File name: Comping_Playlists.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Session_Delivery_and_Archiving/Comping_Playlists.png
Also overwrite: /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Vocal_Recording/Comping_Playlists.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Session Delivery: Files Another Engineer Can Open, Figure 1; Vocals: Running the Session & Organizing Takes, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter view. Four long glossy take lanes are stacked in the upper part of the frame, each holding a vocal waveform ribbon divided into four equal phrase sections. In the first lane, the first section glows green (#1B5E20); in the second lane, the second section glows blue (#0D47A1); in the third lane, the third section glows brown orange (#993300); in the fourth lane, the fourth section glows violet (#4A148C). All other sections are muted pale grey but still present. Below, separated by a clear gap, one comp lane holds a single continuous waveform built from those four colored sections in order, green, blue, brown orange, violet, with a short soft crossfade blend at each of the three joins. Four faint vertical beams of light drop from each chosen section straight down to its place in the comp lane.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 42. One time studio costs against costs that repeat every month

Now: Two columns of six outlined text boxes under two headings.

```
DAPR 2010 - Core Recording
Image: One time studio costs against costs that repeat every month
File name: Cost_Breakdown.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Business/Cost_Breakdown.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Studio Business: What It Actually Costs, Figure 1
Fix: None, same content, richer rendering; the twelve category names move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter view with two zones. Left zone: one large glossy blue (#0D47A1) platform holding a single tidy pile of studio purchases, bought once: a small stack of lumber and drywall sheets (build out), a compact generic console with a short rack of outboard gear, a few microphones, a pair of studio monitors, a computer with a dark screen beside an audio interface, and coiled cables with folded mic stands. Right zone: a long row of identical glossy red (#B71C1C) tiles marching away from the viewer toward the horizon like a conveyor, so the row seems never to end. Every tile carries the same six small objects: a house key (rent), an electrical plug (power), a small shield (insurance), a glowing app tile (software subscriptions), a wrench (maintenance and repair), and a small megaphone (marketing). The nearest red tile is the largest and clearest; each following tile repeats the same set.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 43. Hourly, day and project rates when a session runs long

Now: Three sets of flat colored bars under headings with printed explanations.

```
DAPR 2010 - Core Recording
Image: Hourly, day and project rates when a session runs long
File name: Rate_Structures.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Business/Rate_Structures.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Studio Business assignment (studio-business-assignment.html), Figure 1; Studio Business: Rates, Clients, & Agreements, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter view, three equal panels side by side, each showing three sessions of increasing length stacked top to bottom as glossy bars. Left panel, hourly, green (#1B5E20): each bar is built from identical small green cubes, one cube per hour; the first bar is short, the second longer, the third longest, so a longer session is simply more cubes that the client pays for. Middle panel, day rate, blue (#0D47A1): three identical long blue slabs, one per day; inside each slab a lighter blue fill shows the hours used, growing from bar to bar, and in the third bar the fill reaches the end of the slab and a small extra blue block is attached beyond it, the next day starting. Right panel, project rate, violet (#4A148C): three identical violet slabs of the same fixed length; inside each a lighter violet fill shows the hours used, and in the second and third bars the fill spills past the end of the slab into a red (#B71C1C) tinted overflow that sits outside the slab on the studio's side, the overrun the studio absorbs. Keep the three panels aligned so bar lengths compare directly.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 44. Who decides what in a session, from client to assistant

Now: Four stacked colored text boxes with arrows and printed role descriptions.

```
DAPR 2010 - Core Recording
Image: Who decides what in a session, from client to assistant
File name: Session_Roles.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Etiquette/Session_Roles.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Studio Etiquette: The Unwritten Rules, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter view: four glossy tiers stacked top to bottom as a stepped tower, each tier a little narrower than the one above, joined down the center by a single glowing path with short downward arrow shaped links between tiers. Top tier, violet (#4A148C), the client: a small hourglass beside a neat stack of coins. Second tier, blue (#0D47A1), the producer: a pair of studio headphones resting on a closed notebook. Third tier, green (#1B5E20), the engineer: a compact section of a console with faders and knobs. Bottom tier, brown orange (#993300), the assistant: a coiled microphone cable beside a folded mic stand. Each object sits on top of its tier like a trophy. Soft studio lighting and shadows.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 45. Where the assistant stands in the control room

Now: A flat room plan with circles, dashed red zones and many printed labels.

```
DAPR 2010 - Core Recording
Image: Where the assistant stands in the control room
File name: Where_the_Assistant_Stands.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Etiquette/Where_the_Assistant_Stands.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Studio Etiquette: Common Mistakes in Your First Sessions, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), landscape close to 4:3. Make it a richly rendered isometric dimensional model of a control room seen from above at a three quarter angle, walls cut low so the whole floor is visible. Along the top wall, a wide window of blue (#0D47A1) tinted glass looks into the live room. In front of the glass sits a generic console with two unbranded studio monitors on its meter bridge, toed in toward the engineer's chair, which is centered behind the console. A thin dashed green (#1B5E20) sightline runs from the engineer's chair straight through the console to the glass. Along the right wall stands a tall rack holding a patch bay and outboard gear. A couch sits along the back wall, and a door opens in the lower left corner. Mark the people as glossy game pawns: a blue pawn in the engineer's chair, a charcoal (#212121) pawn on the couch for the producer, and a green pawn standing on a glowing green floor disc beside the rack, to the right of and slightly behind the console, where the engineer can see it without turning. Two translucent red (#B71C1C) floor zones mark keep out areas: one filling the space between the console and the glass, in front of the monitors, and one directly behind the engineer's chair.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 46. Five pieces of studio gear from most fragile to most forgiving

Now: Five outline icons on text cards with printed never and always rules.

```
DAPR 2010 - Core Recording
Image: Five pieces of studio gear from most fragile to most forgiving
File name: Fragile_Gear.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Use_and_Care/Fragile_Gear.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Studio Care: Handling Gear That Can Be Destroyed, Figure 1
Fix: None, same content, richer rendering; the never and always rules move to the caption or page.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic product photograph, five items in a single row, left to right, on a seamless white sweep, soft studio light, shallow depth of field, each item shown the right way to care for it. First: a generic ribbon microphone standing upright in an open padded flight case. Second: a large diaphragm condenser microphone in a spider shock mount, with a soft cloth dust bag folded beside it. Third: a handheld dynamic vocal microphone with a clean, round, undented mesh grille. Fourth: an XLR microphone cable coiled neatly over under and fastened with a hook and loop tie. Fifth: a pair of closed back studio headphones hanging by the headband from a wall hook, the cable coiled below. Under the row runs a thin glossy floor strip that shades smoothly from red (#B71C1C) under the ribbon microphone at the left to green (#1B5E20) under the headphones at the right.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 47. Power up order and the same order reversed for power down

Now: Two rows of five numbered text boxes with the speaker stages tinted red.

```
DAPR 2010 - Core Recording
Image: Power up order and the same order reversed for power down
File name: Power_Up_Sequence.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Use_and_Care/Power_Up_Sequence.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Studio Care assignment (studio-care-assignment.html), Figure 1; Studio Care: Power, Order, & Why It Matters, Figure 2
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in three quarter view: two rows of five glossy tiles, each tile holding one piece of generic unbranded studio gear with a small round power indicator light. Top row, power up, left to right: a computer tower with a small audio interface beside it; a short rack of outboard gear and converters; a compact console; a power amplifier; a powered studio monitor. In the top row the power lights glow green (#1B5E20), and a glowing green path runs left to right through the tiles. Bottom row, power down, left to right, the same objects in reverse order: powered studio monitor; power amplifier; compact console; rack of outboard gear and converters; computer with interface. In the bottom row the power lights are dark and a charcoal (#212121) path runs left to right. In both rows the amplifier and monitor tiles are tinted pale red (#F6D5D5) with red (#B71C1C) edges, and every other tile is pale grey, so the speakers are visibly last on and first off.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 48. Eight step session strike order with the protective steps in red

Now: Eight numbered text boxes in a snake with a red note; accurate but all text.

```
DAPR 2010 - Core Recording
Image: Eight step session strike order with the protective steps in red
File name: Session_Strike_Order.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Use_and_Care/Session_Strike_Order.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Studio Care: Worked Example: Striking a Session, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide banner. Make it a richly rendered dimensional diagram in three quarter view: eight glossy square tiles joined by one glowing path. The top row holds four tiles running left to right; the path drops down at the right end; the bottom row holds four tiles running right to left. Top row, left to right: tile one, charcoal (#212121), a small external backup drive with a glowing activity light beside a computer with a dark screen; tile two, red (#B71C1C), a studio monitor and a power amplifier with their power lights off; tile three, red, a console channel with its fader pulled fully down, its gain knob turned to minimum and its phantom power button unlit; tile four, red, a microphone cable's XLR plug drawn a short way out of a wall box jack. Bottom row, right to left: tile five, charcoal, a microphone cable coiled over under and hung on a hook; tile six, charcoal, a microphone resting in the foam cutout of an open case; tile seven, charcoal, collapsed mic stands lying together with headphones hung on a hook; tile eight, charcoal, a tidy empty room corner with chairs pushed in and the lights dimmed. The three red tiles glow a little brighter than the rest.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2010 Image 49. Vocal chain above, singer, pop filter and microphone spacing below

Now: A row of text boxes above a dot, a bar and a triangle with printed inch distances.

```
DAPR 2010 - Core Recording
Image: Vocal chain above, singer, pop filter and microphone spacing below
File name: Recording_Chain.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Vocal_Recording/Recording_Chain.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Vocals assignment (vocals-assignment.html), Figure 1; Vocals: The Chain & the Physical Setup, Figure 1
Fix: None, same content, richer rendering; the three to four inch distances move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape, in two horizontal bands. Upper band: a richly rendered dimensional row of five pieces of generic unbranded gear on glossy tiles, reading left to right and joined by a glowing blue (#0D47A1) cable: a large diaphragm condenser microphone, a preamp unit, a compressor unit rendered as semi transparent frosted glass to show it is optional, a converter box, and a computer with a dark, softly defocused screen. Lower band: a photorealistic side view on a seamless white sweep of a singer's head and shoulders in soft silhouette facing right, face not in focus, a round mesh pop filter on a gooseneck in front of the mouth, and a large diaphragm condenser microphone in a shock mount beyond the pop filter. The gap from the singer's mouth to the pop filter and the gap from the pop filter to the microphone are equal, each about the width of a hand. Two glowing green (#1B5E20) dimension bars of exactly equal length float just below, marking those two gaps.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. One singer only, in soft silhouette, no face in focus, no hands.
```

#### DAPR 2010 Image 50. The same vocal setup placed badly and placed well

Now: Two flat panels with a cartoon figure, an oval and a stick microphone, plus several printed notes.

```
DAPR 2010 - Core Recording
Image: The same vocal setup placed badly and placed well
File name: Vocal_Booth_Setup_Wrong_and_Right.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Vocal_Recording/Vocal_Booth_Setup_Wrong_and_Right.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Vocals: Common Mistakes on a Vocal Session, Figure 1
Fix: None, same content, richer rendering; the distances move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic, two equal side view panels of a small vocal booth corner, soft studio light, shallow depth of field, a thin red (#B71C1C) glow along the floor of the left panel and a thin green (#1B5E20) glow along the floor of the right panel. Each panel holds the same four things: a singer in soft silhouette facing right with no face in focus, a round mesh pop filter on a gooseneck, a large diaphragm condenser microphone in a shock mount on a stand, and the wall behind the microphone. Left panel, common setup: the pop filter is pressed flat against the microphone grille, the singer leans in so close the mouth nearly touches the filter, and the wall behind the microphone is bare, hard, painted drywall. Right panel, better setup: the singer stands farther back so the mouth is about a hand and a half from the microphone, the pop filter sits in the gap a few inches in front of the microphone, clearly not touching it, and a thick fabric covered absorber panel in blue (#0D47A1) hangs on the wall directly behind the microphone.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. One singer per panel only, in soft silhouette, no face in focus, no hands.
```

### DAPR 2020 Core Mixing

#### DAPR 2020 Image 14. Overhead listening triangle with toed in monitors

Now: A flat line drawing of an equal sided triangle between two speaker boxes and a head, with text labels on every part.

```
DAPR 2020 - Core Mixing
Image: Overhead listening triangle with toed in monitors
File name: Listening_Triangle_Overhead.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Acoustics__Mix_Acoustics/Listening_Triangle_Overhead.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mix Acoustics: Room Acoustics and Monitoring (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic overhead product photograph, shot straight down from directly above so distances are not distorted. On a matte light gray floor sit two identical small generic studio monitors (dark charcoal #212121 cabinets, visible woofer and tweeter from above only as the top of the cabinet and front baffle edge) and, centered below them, an empty studio chair seen from above with its headrest toward the bottom of the frame. Mark the ear position just in front of the headrest with a small glowing white sphere. Three glowing green (#1B5E20) tubes connect the two monitor fronts and the sphere to form an exactly equilateral triangle: all three sides the same length, the angle at the sphere exactly 60 degrees. Each monitor is rotated so its front baffle points straight at the sphere along its side of the triangle. Put a small raised tick mark at the midpoint of each of the three sides to show they are equal, and a thin curved green arc inside the angle at the sphere. Place the label "L" beside the left monitor and "R" beside the right monitor in clean charcoal lettering. Soft studio lighting, soft contact shadows. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 15. Absorber, diffuser and corner bass trap side by side

Now: Three flat boxed panels with arrows and hatching standing in for acoustic treatment, plus text labels in the third panel.

```
DAPR 2020 - Core Mixing
Image: Absorber, diffuser and corner bass trap side by side
File name: Treatment_Types_Comparison.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Acoustics__Mix_Acoustics/Treatment_Types_Comparison.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mix Acoustics: What the Room Does to What You Hear (Figure 2)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Three photorealistic product style vignettes side by side with equal spacing, each a small section of pale plaster wall seen from a three quarter angle with soft studio light. Left: a thick fabric wrapped porous absorber panel in deep green fabric (#1B5E20) mounted on the wall; a glowing green beam of sound travels in from the left and enters the panel face, fading into a faint warm glow inside the panel and never coming back out. Center: a wooden diffuser on the wall made of a grid of square wells of many different depths, warm natural wood; a glowing blue (#0D47A1) beam arrives and breaks into many thin blue rays spraying back out in a wide fan in all directions. Right: a room corner where two walls meet, with a tall thick triangular foam bass trap filling the vertical corner from floor to ceiling in charcoal (#212121) fabric; a broad, slow, long wavelength brown orange (#993300) wave, drawn as a thick glowing ribbon with only one or two gentle undulations, rolls into the corner and dies inside the trap. Keep all three vignettes at the same scale and lighting. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 16. Four spaces from small room to cathedral with growing pre delay and decay

Now: Four outline rectangles with dots and a plain blue bar under each, plus text labels for room names and settings.

```
DAPR 2020 - Core Mixing
Image: Four spaces from small room to cathedral with growing pre delay and decay
File name: Space_Scale_Comparison.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Effects__Balancing_and_Reverb/Space_Scale_Comparison.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Balancing and Reverb: Placing a Source in a Space (Figure 2)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Four photorealistic architectural cutaway scale models standing in a row on white, left to right, each clearly larger than the one before, all seen from the same three quarter angle with soft studio light: a tiny dry room with low ceiling and padded walls; a medium live room with wood floor and hard walls; a large concert hall with raked seating and a high ceiling; a very large stone cathedral interior with a tall vaulted nave. Inside each, a small glowing green (#1B5E20) sphere for the sound source near one end and a small white sphere for the listener near the other, the distance between them growing with the room. Directly beneath each model, a glossy dimensional bar made of three parts reading left to right: a small charcoal (#212121) cube for the direct sound, then an empty gap for the pre delay, then a glowing blue (#0D47A1) tail that tapers and fades for the decay. Both the gap and the tail get clearly longer from the small room to the cathedral, so the cathedral bar has the widest gap and the longest tail. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 17. Opposite polarity stereo summed to mono and cancelling

Now: Flat sine lines beside speaker icons and an arrow with text; the idea is right but the rendering is thin.

```
DAPR 2020 - Core Mixing
Image: Opposite polarity stereo summed to mono and cancelling
File name: Mono_Collapse_Check.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Effects__Delay_and_Stereo_Enhancements/Mono_Collapse_Check.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Quick Mix 4 (Figure 1); Delay & Stereo Enhancements: Common Mistakes and How to Hear Them (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram reading left to right, glossy 3D ribbons and blocks with soft shading. On the left, two small generic speaker cabinets stacked one above the other, each emitting a thick glowing ribbon waveform to the right: the upper ribbon blue (#0D47A1), the lower ribbon red (#B71C1C), both the same smooth wave with four full cycles and the same height, but exactly mirror images of each other, so wherever the blue ribbon rises the red one falls. Label the upper speaker "L" and the lower speaker "R". Both ribbons flow into a glossy brown orange (#993300) summing block shaped like a funnel in the middle of the image. Out of the right side of the block comes a single ribbon that is almost perfectly flat, a thin charcoal (#212121) line with only the faintest ripple, running into one single speaker cabinet on the far right. The contrast between the two tall waves going in and the nearly flat line coming out is the whole point. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 18. Four fields of a bounce specification feeding one file

Now: Four flat outlined boxes with clip art icons and titles joined by thin lines to a document icon.

```
DAPR 2020 - Core Mixing
Image: Four fields of a bounce specification feeding one file
File name: Professional_Practice_Bounce_Specification.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Final__Final_Mix_and_Final_Exam/Professional_Practice_Bounce_Specification.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Final Mix: "A Horse Is Not a Home" (Figure 1); Final Mix: Delivery and Verification Procedure (Figure 1); Final Mix and Final Exam: Study Guide (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: four glossy 3D tiles in a row across the upper half, seen from a slight three quarter angle, each with a raised dimensional symbol and a short label. Tile one, green (#1B5E20): a thick audio file card with a folded corner and a waveform stamped on it, labeled "FILE TYPE". Tile two, blue (#0D47A1): a smooth wave with evenly spaced glowing dots sitting along it like samples, labeled "SAMPLE RATE". Tile three, red (#B71C1C): a staircase of fine even steps rising left to right, like quantization levels, labeled "BIT DEPTH". Tile four, brown orange (#993300): one small speaker on the left of the tile and a pair of speakers on the right of the tile, labeled "MONO OR STEREO". From the bottom of each tile a glowing cable in the tile's color runs down and all four cables merge into one thick glossy charcoal (#212121) finished audio file block centered in the lower half of the image. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 19. Complete bounce against one cut off mid tail

Now: Two flat bar style waveforms, one ending early at a red dashed line and an X.

```
DAPR 2020 - Core Mixing
Image: Complete bounce against one cut off mid tail
File name: Professional_Practice_Bounce_Truncation.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Final__Final_Mix_and_Final_Exam/Professional_Practice_Bounce_Truncation.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Final Mix, Jeff Hirata "Sunshine" (Figure 1); Final: Final Mix & Final Exam: Module Overview (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: two long glossy 3D waveform sculptures lying on thin frosted glass lanes, one above the other, seen from a slight three quarter angle, both starting at the same left edge. Upper lane: a green (#1B5E20) waveform with a strong attack near the left, a few smaller swells, then a long smooth tail that tapers gradually to a thread and reaches true silence near the right edge. Lower lane: the identical blue (#0D47A1) waveform, matching the upper one peak for peak, but it stops dead a little past the middle of the lane, while the tail is still clearly audible, with a clean vertical sliced face like a cut block. At that cut stands a thin glowing red (#B71C1C) vertical blade of light, and the rest of the lower lane to the right is empty. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 20. Seven step delivery checklist with the listen step highlighted

Now: Seven empty checkboxes beside flat clip art icons, one with "0 dBFS" text and one with letters in circles.

```
DAPR 2020 - Core Mixing
Image: Seven step delivery checklist with the listen step highlighted
File name: Professional_Practice_Delivery_Verification_Checklist.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Final__Final_Mix_and_Final_Exam/Professional_Practice_Delivery_Verification_Checklist.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: In Class Mix 02 (Figure 1); Final Mix and Final Exam: Verifying Before You Submit (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: a tall glossy charcoal (#212121) checklist board standing upright in the center, seen from a slight three quarter angle, holding seven rows from top to bottom. Each row has an empty raised square checkbox on the left and a raised glossy symbol to its right. Row one: a small speaker and a small microphone, each crossed by a red (#B71C1C) slash. Row two: a short level meter whose tallest bar stops just under a thin red ceiling bar. Row three: an audio file card with a blue (#0D47A1) arrow leaving it to the right. Row four: a green (#1B5E20) play button followed by a full length waveform; this row alone glows softly and sits slightly forward of the board, to show it is the step most often skipped. Row five: two overlapping blue rings with an arrow into a single green ring. Row six: a brown orange (#993300) document with a pencil. Row seven: a blue cloud with an upward arrow. Keep the rows evenly spaced and the symbols the same scale. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 21. Edit through the transient against an edit in the quiet with a crossfade

Now: Two flat gray boxes with zigzag waveforms, a red line with a star on the left and a green line with a loop on the right.

```
DAPR 2020 - Core Mixing
Image: Edit through the transient against an edit in the quiet with a crossfade
File name: Gray_Clips_with_Star_and_Crossfade.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Comping_and_Arrangement/Gray_Clips_with_Star_and_Crossfade.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Comping Lab (Figure 1); Comping & Arrangement: Common Mistakes and How to Hear Them (Figure 2)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram, two panels side by side separated by a thin vertical glass divider, seen from a slight three quarter angle. Each panel holds one identical glossy audio clip tile in a light tint of charcoal (#212121), and inside each tile a raised charcoal waveform: low, even, quiet ripples from the left, then one sharp tall transient spike about two thirds of the way across, then quiet ripples again. Left panel: a thin glowing red (#B71C1C) vertical blade slices through the clip exactly at the tip of the transient spike, and a small red spark bursts from the top of the blade where it meets the peak. Right panel: the same blade, now glowing green (#1B5E20), has moved left into the quiet ripples well before the transient, and at the blade two short glossy crossfade ramps cross in an X shape, one fading down and one fading up, sitting entirely in the quiet part while the transient stays whole. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 22. Splice on the transient against a splice with a crossfade before it

Now: Two flat line waveforms with dashed edit lines and large text titles above each panel.

```
DAPR 2020 - Core Mixing
Image: Splice on the transient against a splice with a crossfade before it
File name: Green_to_Blue_Waveform_Splice_Pair.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Comping_and_Arrangement/Green_to_Blue_Waveform_Splice_Pair.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Mix Comping and Arranging Assignment (Figure 1); Comping & Arrangement: Common Mistakes and How to Hear Them (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram with two panels side by side, each a thin frosted glass lane seen from a slight three quarter angle. In both panels a glossy 3D waveform ribbon runs left to right: the left part is a low, busy green (#1B5E20) ripple from the outgoing take, and the right part is a blue (#0D47A1) note from the incoming take that begins with one tall sharp transient and then decays. Left panel: the green ripple ends and the blue take begins exactly at the tip of the blue transient, with a glowing red (#B71C1C) vertical edit plane standing right at that spot and a small red burst of sparks at its top edge, showing a click. Right panel: the red edit plane sits in the quiet gap a short distance before the blue transient; around it two short glossy ramps overlap in an X, a brown orange (#993300) ramp fading the green take out and a blue ramp fading the blue take in, and the blue transient follows untouched and complete after the crossfade. No sparks in the right panel. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 23. Four take lanes assembled into one comp lane

Now: Five rows of flat waveforms with colored label tabs; the concept reads but the rendering is plain.

```
DAPR 2020 - Core Mixing
Image: Four take lanes assembled into one comp lane
File name: Playlist_Comp_Lanes.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Comping_and_Arrangement/Playlist_Comp_Lanes.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Comping and Arrangement: The Controls and the Decisions (Figure 1); Mixing: Comping & Arrangement: Module Overview (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: five long glossy horizontal lanes stacked top to bottom, seen from a gentle three quarter angle, like thin glass trays. Each of the top four lanes (the takes) holds the same phrase as a raised waveform divided into four equal sections by three faint vertical glass dividers that run through all five lanes. In lane one the first section glows green (#1B5E20); in lane two the second section glows blue (#0D47A1); in lane three the third section glows red (#B71C1C); in lane four the fourth section glows brown orange (#993300). All other sections in the top four lanes are dull matte gray. The fifth lane at the bottom (the comp) is slightly thicker, with a charcoal (#212121) base, and holds all four glowing sections placed end to end in order: green, blue, red, brown orange. Faint glowing drop lines fall from each selected section straight down into its slot in the comp lane. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 24. Gain staging chain with a healthy meter at every stage

Now: Seven flat clip art icons in a row with identical cartoon meters under each.

```
DAPR 2020 - Core Mixing
Image: Gain staging chain with a healthy meter at every stage
File name: Gain_Staging_Chain.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Essential_Groundwork/Gain_Staging_Chain.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Essential Groundwork Lab (Figure 1); Assignment: Mix Prep Assignment (Figure 1); Essential Groundwork: Common Mistakes and How to Hear Them (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram reading left to right: seven glossy 3D tiles on a light gray floor, seen from a slight three quarter angle, joined by one continuous glowing charcoal (#212121) cable with small arrow beads showing direction. Tile one, blue (#0D47A1): a round puck with a raised waveform (the source). Tile two, brown orange (#993300): a clip with a small gain handle on its top edge (clip gain). Tile three, red (#B71C1C): a single rotary trim knob. Tile four, blue, wider than the others: three small processor modules side by side with gentle curves on their faces (the plugin inserts). Tile five, green (#1B5E20): a channel fader. Tile six, brown orange: several thin lines merging into one (the bus). Tile seven, red: a large master output knob. Under every tile stands a small upright LED meter, all seven lit to the same healthy height: green segments lit, the amber segment above just touching, and the top red segment dark on every meter. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 25. Five playback systems in checking order

Now: Five flat outline icons (speakers, car, phone, headphones) with text labels above a green arrow.

```
DAPR 2020 - Core Mixing
Image: Five playback systems in checking order
File name: Multi_System_Playback_Check.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Focus_and_Balance/Multi_System_Playback_Check.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Focus and Balance: Mix Window Procedure Guide (Figure 2)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic product lineup on a seamless white sweep, soft studio lighting, gentle contact shadows, five items in a row from left to right, evenly spaced: a pair of small generic nearfield studio monitors side by side; a single larger generic midfield studio monitor with a bigger woofer; a small generic unbranded scale model sedan in deep blue (#0D47A1) seen from a front three quarter angle; a generic smartphone standing upright with its screen dark; a pair of generic over ear headphones resting on a small stand. Under the whole row runs a glossy green (#1B5E20) floor stripe with a raised arrowhead at the right end, showing the order to check them. Cabinets in matte charcoal (#212121). No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 26. One element heard alone against the same element in a dense mix

Now: A flat blue waveform burst on the left and a tangle of colored line waves over it on the right.

```
DAPR 2020 - Core Mixing
Image: One element heard alone against the same element in a dense mix
File name: Single_Blue_Burst_beside_Stacked_Tracks.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Focus_and_Balance/Single_Blue_Burst_beside_Stacked_Tracks.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mixing: Focus & Balance: Module Overview (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram with two panels side by side on a white floor, seen from a slight three quarter angle. Left panel: one glossy 3D blue (#0D47A1) waveform ribbon, a burst that swells from quiet to loud and back, floating alone with open space all around it and a soft shadow beneath. Right panel: the very same blue burst at the same size, but now layered inside a dense stack of five other glossy ribbons that weave over and under it: a slow wide green (#1B5E20) wave, a fast red (#B71C1C) wave, a brown orange (#993300) wave, a slow charcoal (#212121) wave and a fine rapid violet (#4A148C) ripple. Parts of the blue burst are hidden behind the other ribbons and its edges are hard to follow. Two thin vertical frosted glass planes stand at either side of the blue burst in the right panel to mark the same time window. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 27. One clip alone against the same clip among six equal tracks

Now: A flat gray box with a large zigzag on the left and six identical small boxes on the right, one of them blue.

```
DAPR 2020 - Core Mixing
Image: One clip alone against the same clip among six equal tracks
File name: Single_Clip_beside_Stacked_Track_Rows.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Focus_and_Balance/Single_Clip_beside_Stacked_Track_Rows.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Focus and Balance: Mix Balancing (Figure 3)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram with two panels divided by a thin vertical glass divider, seen from a slight three quarter angle. Left panel: one large glossy clip tile in a light tint of charcoal (#212121), holding a tall raised blue (#0D47A1) waveform that fills most of the tile height. Right panel: six equal glossy clip tiles stacked evenly from top to bottom, each the same size and each holding a smaller raised waveform of the same height; five of them are matte gray and the third from the top is the same blue waveform, now shrunk to the same small height as its neighbours. The six stacked tiles together occupy about the same total height as the single tile on the left. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 28. Stereo field map of pan, depth and size

Now: A flat grid with outline circles of three sizes and five text labels on the axes.

```
DAPR 2020 - Core Mixing
Image: Stereo field map of pan, depth and size
File name: Stereo_Field_Map.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Focus_and_Balance/Stereo_Field_Map.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Focus and Balance: Panning Diagrams (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: a wide shallow glossy floor tile in a light tint of blue (#0D47A1) with a faint engraved grid, seen from above with only a slight tilt and no perspective shrinking, so sizes are true. Left to right across the tile is pan; bottom (near) to top (far) is depth. A small charcoal (#212121) wedge at the bottom center edge points into the tile to mark the listener. Place eight glossy spheres standing on the tile: along the near edge, three large spheres at far left, center and far right; in the middle depth, two medium spheres halfway between center and each side; along the far edge, three small spheres at far left, center and far right. Colors: large spheres green (#1B5E20), medium spheres blue, small spheres violet (#4A148C). Each sphere casts a soft shadow. Put the label "L" at the left end of the near edge and "R" at the right end of the near edge. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 29. Five mix passes in order along one track

Now: Five flat outlined boxes on a colored line with five word labels.

```
DAPR 2020 - Core Mixing
Image: Five mix passes in order along one track
File name: Five_Pass_Mix_Order.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__In-Class_Mixing/Five_Pass_Mix_Order.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: In Class Mix 01 (Figure 1); In Class Mixing: Common Mistakes and How to Hear Them (Figure 1); In Class Mixing: Repeatable Workflow Guide (Figure 1); Mixing: In Class Mixing: Module Overview (Figure 1); In Class Mixing: A Repeatable Order of Operations (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: one long glowing track runs left to right across the middle of the image and ends in a raised arrowhead on the right. Five glossy 3D tiles sit on the track in order, evenly spaced, seen from a slight three quarter angle, each with a raised symbol. Tile one, charcoal (#212121): a pair of faders at different heights (balance). Tile two, green (#1B5E20): an EQ curve with one clear downward notch (subtractive EQ). Tile three, blue (#0D47A1): a waveform being squeezed flatter between two plates (dynamics). Tile four, red (#B71C1C): a pan knob with a soft reverb halo around it (placement). Tile five, brown orange (#993300): a curved automation line with three round nodes (automation). The track segment under each tile takes that tile's color, so the track shifts color from charcoal to brown orange. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 30. Distortion chain with filtering before and tone shaping after the drive

Now: A flat banner of five outlined text boxes with arrows, a title line and a caption line inside the image.

```
DAPR 2020 - Core Mixing
Image: Distortion chain with filtering before and tone shaping after the drive
File name: Distortion_Pre_and_Post_EQ_Chain.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Master-Buss_Processing_and_Endgame/Distortion_Pre_and_Post_EQ_Chain.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Distortion: Guitars, Pickups and Using Distortion in a Mix (Figure 2)
Fix: None, same content, richer rendering

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide banner (generate it as a wide landscape; it will be cropped to a banner). A richly rendered dimensional diagram reading left to right: five glossy 3D modules in a single row, seen from a slight three quarter angle, joined by a thick glowing cable with arrow beads. Module one, charcoal (#212121): a small generic DI box with a guitar cable plugged into it. Module two, green (#1B5E20): a raised filter curve that is low on the left and rises to flat on the right (a high pass filter). Module three, brown orange (#993300), glowing warmer and brighter than the rest: a raised waveform whose tops and bottoms are rounded and flattened by saturation (the drive). Module four, green: a gentle raised bell curve (tone EQ). Module five, blue (#0D47A1): a single output level knob. Keep all five modules the same size and centered vertically with generous white space above and below. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 31. Meter with headroom against a meter pinned at the ceiling

Now: Two flat cartoon LED bar meters, one with dark top segments and one with a red top segment and burst lines.

```
DAPR 2020 - Core Mixing
Image: Meter with headroom against a meter pinned at the ceiling
File name: Headroom_on_Delivery.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Master-Buss_Processing_and_Endgame/Headroom_on_Delivery.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Mix Master Buss Processing, Automation, & Endgame (Figure 1); Master Buss Processing & Endgame: Common Mistakes and How to Hear Them (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic close product photograph of two tall generic hardware LED bar meters standing side by side on a white sweep, matte charcoal (#212121) housings, shallow depth of field, soft studio light, each meter a single column of about twenty rectangular LED segments. Left meter: lit green from the bottom to about three quarters of the height, with one amber segment lit above that, and the top four segments clearly dark and unlit, leaving visible headroom. Right meter: lit all the way to the top, green, then amber, and the very top segment glowing bright red (#B71C1C) with a soft red bloom around it, pinned at the ceiling. Both meters identical in size and angle so only the level differs. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 32. Master buss chain in insert order with early and last timing

Now: Six flat outlined text boxes with long descriptions and two colored timing bars, all in text.

```
DAPR 2020 - Core Mixing
Image: Master buss chain in insert order with early and last timing
File name: Master_Chain_Order.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Master-Buss_Processing_and_Endgame/Master_Chain_Order.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Master Buss Processing and Endgame: The Master Chain and the Final Check (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram reading left to right: six glossy 3D modules in a row across the upper part of the image, seen from a slight three quarter angle, joined by a glowing charcoal cable with arrow beads. Module one, charcoal (#212121): a bundle of thin colored track strips merging into one (all tracks). Module two, green (#1B5E20): a compressor face with a small analog style needle gain reduction meter. Module three, blue (#0D47A1): a gentle broad shelf curve (broad EQ). Module four, red (#B71C1C): a limiter face with a flat ceiling line over a waveform; render this module as translucent frosted glass with a dashed glowing outline so it reads as optional. Module five, charcoal: a pair of meter bars (meters only, no numbers). Module six, charcoal: an audio file card with an arrow leaving it (the bounce). Below the row, a glossy timeline strip: a short green bar directly under module two labeled "EARLY", and a longer blue bar spanning under modules three and four labeled "LAST". No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 33. Three quantize strengths shown as hits drawn toward the grid

Now: Three rows of flat blob markers on gray grid lines, scattered, halfway and on the line.

```
DAPR 2020 - Core Mixing
Image: Three quantize strengths shown as hits drawn toward the grid
File name: Marker_Rows_at_Varying_Offsets.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Timing/Marker_Rows_at_Varying_Offsets.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Timing: The Controls and What They Cost (Figure 2)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: eight evenly spaced thin vertical glass rods in light charcoal (#212121) stand across the image as the grid, seen from a slight three quarter angle. Three horizontal rows of glossy rounded pucks, eight pucks per row, one puck near each rod. Top row, red (#B71C1C): each puck sits clearly off its rod, some early to the left and some late to the right by different amounts. Middle row, brown orange (#993300): each puck sits exactly halfway between where the red puck above it sits and its rod, so every offset is cut in half and in the same direction. Bottom row, green (#1B5E20): every puck sits centered exactly on its rod. Faint ghost outlines in the middle and bottom rows show where the original red position was, with a short soft trail from the ghost to the puck. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 34. The same drum performance at three quantize strengths

Now: Three rows of flat drum hit waveforms over dashed grid lines, original, partial and full.

```
DAPR 2020 - Core Mixing
Image: The same drum performance at three quantize strengths
File name: Waveform_Rows_against_Grid_Lines.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Timing/Waveform_Rows_against_Grid_Lines.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Timing: Common Mistakes and How to Hear Them (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: three long frosted glass lanes stacked top to bottom, seen from a slight three quarter angle, all crossed by the same eight evenly spaced thin vertical grid planes. Each lane holds eight identical glossy drum hit waveforms, each a sharp attack with a short decaying tail. Top lane, charcoal (#212121), the original: each attack sits a little early or a little late of its grid plane by varied, natural amounts. Middle lane, green (#1B5E20), partial strength: each attack has moved halfway toward its grid plane, still slightly off. Bottom lane, red (#B71C1C), full strength: every attack sits exactly on its grid plane in perfect rigid alignment, the lane rendered a touch colder and more uniform than the others. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 35. Pitch line against its target at no, partial and full correction

Now: Three flat gray boxes each holding a zigzag line over a flat target line, wide, reduced and flat.

```
DAPR 2020 - Core Mixing
Image: Pitch line against its target at no, partial and full correction
File name: Correction_Amount_Comparison_Boxed.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Tuning/Correction_Amount_Comparison_Boxed.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Mixing: Mix Tuning Assignment (Figure 1); Tuning: Pitch Correction Procedure Guide (Figure 2)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: three wide glossy trays stacked top to bottom, seen from a slight three quarter angle, each tray a light tint of charcoal (#212121) with a thin raised charcoal target rail running straight across its middle. In each tray lies a glossy tube representing the sung pitch, running left to right. Top tray, red (#B71C1C): the tube swings well above and below the rail in a regular vibrato with a slow drift on top of it. Middle tray, brown orange (#993300): the same shape, but the swings are reduced to about a third of the height, still clearly a living vibrato around the rail. Bottom tray, green (#1B5E20): the tube lies dead straight exactly on top of the rail with no movement at all. All three tubes the same thickness and length. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 36. Natural pitch curves at three correction amounts

Now: Three flat line plots with axes and a dashed target line, wandering, reduced and flat.

```
DAPR 2020 - Core Mixing
Image: Natural pitch curves at three correction amounts
File name: Correction_Amount_Comparison_Curves.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Tuning/Correction_Amount_Comparison_Curves.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Tuning Lab (Figure 1); Tuning: What to Correct and What to Leave (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: three shallow glossy plot planes stacked top to bottom, seen from a slight three quarter angle, each with a raised charcoal (#212121) vertical axis on the left and horizontal axis along the bottom, both ending in small arrowheads, and a dashed glowing green (#1B5E20) target line running across at the same height in each. Top plane: a glowing red (#B71C1C) curve wanders freely above and below the target, with small natural wobbles and a few larger drifts, like a real singer. Middle plane: a glowing blue (#0D47A1) curve with the same features, pulled close to the target so it only wobbles gently around it. Bottom plane: a glowing brown orange (#993300) line lies perfectly flat and straight exactly on the target, covering the dashed line completely. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 37. Slow correction keeps the scoop, fast correction removes it

Now: Two flat line plots, a smooth S shaped rise above a hard vertical step.

```
DAPR 2020 - Core Mixing
Image: Slow correction keeps the scoop, fast correction removes it
File name: Correction_Speed_Scoop.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Tuning/Correction_Speed_Scoop.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Tuning: A Horse Is Not a Home, the Semester Project (Figure 1); Mixing: Tuning: Module Overview (Figure 2)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: two shallow glossy plot planes stacked top and bottom, seen from a slight three quarter angle, each with a raised charcoal (#212121) vertical axis on the left (pitch) and horizontal axis along the bottom (time), both ending in small arrowheads. In both planes, a faint dashed charcoal target line runs across the upper part for the note being sung, and a lower faint dashed line marks the note before it. Top plane: a glowing green (#1B5E20) pitch tube holds the lower note, then scoops up into the target in a smooth, gradual S shaped curve and settles gently onto the target line. Bottom plane: a glowing blue (#0D47A1) pitch tube holds the same lower note, then jumps straight up to the target in an instant vertical step with sharp square corners, and sits rigidly on the target. The scoop is present in the top plane and completely gone in the bottom plane. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 38. Six gain stages from channel fader to speaker

Now: Six flat outlined text boxes joined by blue arrows.

```
DAPR 2020 - Core Mixing
Image: Six gain stages from channel fader to speaker
File name: Gain_Stages_Chain.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Monitoring__Calibration_and_Monitoring/Gain_Stages_Chain.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Assignment: Calibration: Mixing Space, Assignment (Figure 1); Calibration and Monitoring: Procedure Guide (Figure 2)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic product lineup on a seamless white sweep, soft studio light, six generic unbranded pieces of gear in a row left to right, connected in order by glossy blue (#0D47A1) cables: a single channel fader module with a gray cap; a second fader module with a larger red (#B71C1C) cap for the master; a small desktop audio interface with its output knob facing the camera; a desktop monitor controller with one large volume knob; a rack power amplifier with two level knobs on its front panel; a passive two way studio monitor. On each piece, the one control that sets its gain (the fader cap, the knob, or for the speaker its woofer cone) is circled by a thin soft blue glow ring. Matte charcoal (#212121) finishes, even scale so the items read as a chain. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 39. Sealed headphone cup against a broken seal leaking low end

Now: Flat line cutaways of an ear under a headphone cup with text captions, sealed and leaking.

```
DAPR 2020 - Core Mixing
Image: Sealed headphone cup against a broken seal leaking low end
File name: Headphone_Seal_Cross_Section.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Monitoring__Calibration_and_Monitoring/Headphone_Seal_Cross_Section.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Calibration: Reference Noise Files (Figure 1); Calibration: Speaker and Headphone Level Calibration (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Two richly rendered anatomical cutaway views side by side, soft shading and real material textures, each a cross section through an over ear headphone cup, its cushion, the outer ear and the ear canal leading to the eardrum, seen from the front. Left panel (sealed): the cup's cushion, outlined with a thin green (#1B5E20) glow, presses evenly against the side of the head all the way around the ear with no gap. Inside the closed cavity and down the ear canal, a soft green glow of long slow pressure waves fills the space and reaches the eardrum at full strength. Right panel (leaking): identical, except the cushion, outlined with a thin red (#B71C1C) glow, is lifted away from the head at the top by the thin arm of a pair of eyeglasses tucked under it, leaving a visible gap. Long slow red pressure waves stream out through the gap as curved arrows, and the glow reaching the eardrum is noticeably weaker. Cups in matte charcoal (#212121). No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 40. Mid side encode and decode matrix with half gain outputs

Now: A flat node diagram with circles, crossing lines, equations and many text labels; the routing is correct.

```
DAPR 2020 - Core Mixing
Image: Mid side encode and decode matrix with half gain outputs
File name: Ms_Matrix_Signal_Flow.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Monitoring__Calibration_and_Monitoring/Ms_Matrix_Signal_Flow.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Calibration and Monitoring: MS (Mid Side) Matrix (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram reading left to right, glossy spheres and glowing cables on a white floor, seen from a slight three quarter angle. The left half sits on a very light green (#1B5E20) floor tint (encode) and the right half on a very light blue (#0D47A1) floor tint (decode). Far left: a green input sphere labeled "L" on the upper row and a blue input sphere labeled "R" on the lower row. Each input splits into two cables that cross in an X. Upper row: a glossy summing sphere with a raised plus symbol receives both L and R and outputs a brown orange (#993300) sphere labeled "M". Lower row: the cable from R passes through a small red polarity inverter puck before joining a second summing sphere, which also receives L; it outputs a red (#B71C1C) sphere labeled "S". In the right half the same pattern repeats: M and S each split and cross; the upper summing sphere receives M and S; on the lower row the cable from S passes through a red polarity inverter puck before a summing sphere that also receives M. After each decode summing sphere sits a small attenuator knob turned exactly halfway down (the half gain stage), and then the outputs: a green sphere labeled "L" on the upper row and a blue sphere labeled "R" on the lower row, matching the inputs. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 41. Six course areas around a central Core Mixing hub

Now: Flat hexagons with tiny glyphs, numbers and all caps text around a central hexagon.

```
DAPR 2020 - Core Mixing
Image: Six course areas around a central Core Mixing hub
File name: Learning_Outcomes.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Learning_Outcomes.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Orientation: Course Description, Learning Outcomes, and Requirements (Figure 3)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram: seven thick glossy hexagonal tiles lying on a white floor, seen from a gentle high three quarter angle, like polished 3D game pieces. A larger charcoal (#212121) hexagon sits in the center with a raised row of small console faders on it. Six smaller hexagons surround it, each joined to the center by a short glowing rod, arranged clockwise starting at the top: top, green (#1B5E20), a raised pair of studio monitors in a small room (the room); upper right, blue (#0D47A1), a raised stack of waveform takes (the take); lower right, red (#B71C1C), a raised curved automation line with an arrowhead (the motion); bottom, brown orange (#993300), a raised waveform with a small wrench resting on it (the repair); lower left, green, a raised checklist with ticked boxes (the discipline); upper left, blue, a raised gear (the tools). Every symbol is white or a pale tint and embossed on the tile face. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 42. Worksheet to PDF in four steps

Now: Four flat clip art icons with large step numbers and text labels, in colors outside the course palette.

```
DAPR 2020 - Core Mixing
Image: Worksheet to PDF in four steps
File name: Worksheet_to_PDF_Flow.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Worksheet_to_PDF_Flow.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Orientation: Handing Work In (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram reading left to right: four glossy 3D objects on a white floor, evenly spaced, seen from a slight three quarter angle, joined by thick glowing charcoal (#212121) arrows. One: a floating dark application window with softly defocused colored waveform bars inside, framed by four glowing corner brackets like a screenshot capture. Two: a glossy red (#B71C1C) clipboard holding a small copy of that screenshot. Three: a tall brown orange (#993300) document page with the screenshot pasted onto it and soft abstract lines for text below it (no readable writing). Four: a blue (#0D47A1) document with a folded corner, labeled "PDF" on a raised badge, with a small round green (#1B5E20) upload badge showing an upward arrow at its lower corner. No text other than the quoted label, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 43. Downloaded multitrack becoming an open session

Now: Four flat solid icons (zip file, folder, session window, gear) joined by arrows.

```
DAPR 2020 - Core Mixing
Image: Downloaded multitrack becoming an open session
File name: Professional_Practice_Multitrack_Download_Flow.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Professional_Practice__Presentations_and_Sessions/Professional_Practice_Multitrack_Download_Flow.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Sessions: Free DAW Session Track Downloads (Figure 1); Auxiliary Resources (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram reading left to right: four glossy 3D objects evenly spaced on a white floor, seen from a slight three quarter angle, joined by thick glowing arrows. One, green (#1B5E20): a compressed archive file with a raised zipper down its face and a round download badge with a downward arrow. Two, blue (#0D47A1): an open folder with the archive unzipping above it and several small audio files spilling out into the folder. Three, red (#B71C1C): a dark session window with softly defocused colored track lanes holding waveforms, and the audio files sliding into the lanes along a curved import arrow. Four, brown orange (#993300): two waveform discs side by side, each with a ring of evenly spaced glowing sample dots, the dot spacing on both discs identical and lined up by a thin glowing bridge, meaning the sample rates match; the fourth object glows slightly brighter than the others, as the step to watch. No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 44. Computer to network share to the course folder

Now: Three flat solid icons (monitor, share symbol, folder tree) joined by green arrows.

```
DAPR 2020 - Core Mixing
Image: Computer to network share to the course folder
File name: Professional_Practice_Network_Drive_Path.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Professional_Practice__Presentations_and_Sessions/Professional_Practice_Network_Drive_Path.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Sessions: Accessing Course Files on the Network Drive (DGM Assets) (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram reading left to right, three stages on a white floor seen from a slight three quarter angle, joined by thick glowing green (#1B5E20) arrows. One: a generic unbranded desktop computer monitor in charcoal (#212121) with a dark, softly glowing screen. Two: a network share shown as three glossy blue (#0D47A1) spheres joined by glowing rods, floating above a small generic server block. Three: a folder tree, a vertical charcoal trunk with three branches, each ending in a glossy 3D folder: the top folder charcoal, the middle folder red (#B71C1C) glowing and lifted slightly forward with a soft red halo as the course folder you are looking for, the bottom folder brown orange (#993300). No text, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 45. Complete session delivery package in one project folder

Now: A flat folder tree of clip art icons with text labels for the project, session file, audio, bounces and PDF.

```
DAPR 2020 - Core Mixing
Image: Complete session delivery package in one project folder
File name: Professional_Practice_Session_Delivery_Package.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Professional_Practice__Presentations_and_Sessions/Professional_Practice_Session_Delivery_Package.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Presentations and Sessions: Common Mistakes and How to Hear Them (Figure 1); Presentations and Sessions: Delivering Work Other People Can Open (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram, hierarchy reading top to bottom, seen from a slight three quarter angle. At the top center, a large glossy 3D green (#1B5E20) project folder. From its base, a glowing charcoal (#212121) branch splits into four and drops to four glossy items in a row beneath it, evenly spaced: a red (#B71C1C) session document with a small raised track lane symbol, labeled "SESSION"; a blue (#0D47A1) folder bulging with many small audio files, labeled "AUDIO"; a brown orange (#993300) folder with a raised waveform on its face, labeled "BOUNCES"; a white document with a red folded corner and soft abstract lines, labeled "PDF". The four items sit visibly inside the project folder's shadow line so they read as its contents. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 46. Software on firmware on hardware as a three layer stack

Now: Three flat outlined text boxes stacked with long descriptions, a sideways arrow label and a product name.

```
DAPR 2020 - Core Mixing
Image: Software on firmware on hardware as a three layer stack
File name: Hardware_Software_Firmware_Stack.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Hardware_Software_Firmware_Stack.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: macOS: P4: Hardware, Software, and Firmware
Fix: None, same content, richer rendering

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), near 4:3 landscape. A richly rendered dimensional diagram: three thick glossy slabs stacked one on top of another with small gaps between them, seen from a high three quarter angle. Bottom slab, the widest and heaviest, charcoal (#212121): on its top face, a photorealistic generic circuit board with a processor chip, memory sticks, a storage module and a row of ports along the front edge. Middle slab, thinner, brown orange (#993300): a single small chip on its surface glowing from within, with faint abstract light traces flowing from it down into the board below (firmware, built into the chip). Top slab, blue (#0D47A1): several floating app windows and small plugin tiles hovering above its surface, all screens dark and softly defocused. Label the front edge of each slab: "SOFTWARE" on the top slab, "FIRMWARE" on the middle slab, "HARDWARE" on the bottom slab, in clean white lettering. No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2020 Image 47. Launch Agent against Launch Daemon

Now: Two columns of flat outlined text boxes listing properties and file paths.

```
DAPR 2020 - Core Mixing
Image: Launch Agent against Launch Daemon
File name: Launch_Agents_vs_Daemons.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Launch_Agents_vs_Daemons.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: macOS: P3: Login Items, Launch Agents, and Launch Daemons
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A richly rendered dimensional diagram in two columns on a white floor, seen from a slight three quarter angle, each column a glossy tray holding four raised symbols stacked top to bottom, the rows aligned across the two columns. Left column, blue (#0D47A1), labeled "AGENT" on a raised header block: row one, a user ID badge with a simple head and shoulders silhouette (runs as the logged in user); row two, a small floating app window with a dark screen (can show a window); row three, an open door with a key in its lock (starts after login); row four, a small bookshelf inside a house shaped frame (the user's own library). Right column, charcoal (#212121) with brown orange (#993300) accents, labeled "DAEMON" on a raised header block: row one, a heavy master key (runs as root); row two, an empty dashed window outline with nothing inside (no interface); row three, a glowing power button in front of a still closed door (starts at boot, before login); row four, a larger bookshelf inside a solid system cabinet (the system library). No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 2255 Audio Hardware I

#### DAPR 2255 Image 07. MIDI status byte and data byte as two rows of bit tiles

Now: Two flat rows of eight empty squares with a 1 or 0 in the first box and small text labels.

```
DAPR 2255 - Audio Hardware I
Image: MIDI status byte and data byte as two rows of bit tiles
File name: Byte_Structure.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__Foundation/Byte_Structure.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: MIDI: Message Architecture and Data Structure (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a three quarter view, like glossy 3D tiles on a table, soft studio shading and gentle shadows. Two rows, one above the other, each row exactly eight square tiles side by side reading left to right. Upper row (the status byte): the leftmost tile is raised higher than the rest, solid deep green (#1B5E20), with a bold white "1" on its top face. The four leftmost tiles (including the green one) rest on one shared pale green (#C8E6C9) base plate, and the four rightmost tiles rest on a separate pale blue (#BBDEFB) base plate with a small gap between the plates, showing the byte split into two halves of four. The seven unraised tiles in this row are glossy pale grey. Lower row (the data byte): the leftmost tile is raised, solid brown orange (#993300), with a bold white "0" on its top face, and the remaining seven tiles are glossy blue (#0D47A1) resting together on one long pale blue base plate, reading as seven bits of value. Keep the two rows clearly separated, same tile size in both. No text other than the quoted labels "1" and "0", no other numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 08. Sixteen MIDI channels with channel ten set apart for drums

Now: A flat row of sixteen empty squares with the tenth filled, plus bracket text.

```
DAPR 2255 - Audio Hardware I
Image: Sixteen MIDI channels with channel ten set apart for drums
File name: GM_Channel_10.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__MIDI_Evolution_and_Extended_Protocols/GM_Channel_10.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: MIDI: Timeline General MIDI and MMC (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a three quarter view: a single straight row of exactly sixteen glossy cube tiles, evenly spaced, running left to right across the frame, soft studio shading and contact shadows. Fifteen of the cubes are glossy blue (#0D47A1), each with a tiny embossed eighth note shape on its top face. The tenth cube from the left (nine blue cubes before it, six blue cubes after it) is raised noticeably higher, solid brown orange (#993300), and carries a small embossed drum shape on its top face instead of a note. Under the nine left blue cubes runs one pale blue (#BBDEFB) base plate and under the six right blue cubes runs a second pale blue base plate; the orange cube sits alone on its own pale orange (#FFE0CC) pedestal between them, so the row reads as melodic channels on both sides of one percussion channel. Count carefully: exactly sixteen cubes, the orange one tenth from the left. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 09. OSC message as three linked blocks: address, type tag, value

Now: Monospaced text of one OSC message with three flat brackets and labels under it.

```
DAPR 2255 - Audio Hardware I
Image: OSC message as three linked blocks: address, type tag, value
File name: OSC_Address_Anatomy.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__MIDI_Evolution_and_Extended_Protocols/OSC_Address_Anatomy.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: MIDI: Open Sound Control Compared to MIDI (Figure 1)
Fix: None, same content, richer rendering. This figure cannot teach without the message text, so it quotes three labels exactly.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a gentle three quarter view: three glossy 3D blocks sitting in a row from left to right on a white surface, joined end to end like train cars with small glowing couplings, soft studio shading and contact shadows. Block one, the longest, deep green (#1B5E20), with the exact label "/mixer/ch/4/fader" printed on its front face in a clean white monospaced font, all lowercase exactly as written. Block two, short, blue (#0D47A1), with the exact label ",f" in the same white monospaced font. Block three, medium, brown orange (#993300), with the exact label "0.75" in the same font; on its top face sits a small generic unbranded fader whose cap rests about three quarters of the way up its slot. A faint glowing green path runs from the far right end back toward a small generic unbranded mixing console softly defocused in the background, showing where the message goes. Spell every label exactly as given and nothing else. No text other than the quoted labels "/mixer/ch/4/fader", ",f" and "0.75", no other numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 10. Troubleshooting stack of six layers, worked top to bottom

Now: Six flat outlined boxes in a column with thin arrows and gray text beside each.

```
DAPR 2255 - Audio Hardware I
Image: Troubleshooting stack of six layers, worked top to bottom
File name: Cross_Protocol_Isolation.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__MIDI_Over_USB_and_Network_Systems/Cross_Protocol_Isolation.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: MIDI: Extended Protocols Troubleshooting Checklist (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in isometric view: a vertical stack of exactly six thick glossy slabs, one above the other with small gaps, centered in the frame, soft studio shading and gentle shadows. Color the slabs from top to bottom in a gradient from charcoal (#212121) through blue (#0D47A1) to green (#1B5E20). On the top face of each slab sits one small sculpted 3D icon, in order from top to bottom: 1) a coiled audio cable with a round connector and a small power plug; 2) three different generic connector ends side by side (a round multi pin plug, a flat rectangular plug, a network plug); 3) a small rotary selector knob between two stacked version cards; 4) a row of small mailbox slots with one slot glowing; 5) a short row of eight tiny bit tiles with the first tile a different color; 6) a small network of four nodes joined by lines with one larger node crowned by a small clock face without numbers. A glowing brown orange (#993300) arrow runs down the left side of the stack from the top slab to the bottom slab, showing the order of checks. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 11. RTP MIDI session opening between two devices

Now: A plain sequence diagram with two lifelines and thin arrows labeled in small gray text.

```
DAPR 2255 - Audio Hardware I
Image: RTP MIDI session opening between two devices
File name: RTP_Session_Handshake.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__MIDI_Over_USB_and_Network_Systems/RTP_Session_Handshake.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: MIDI: RTP MIDI and AppleMIDI (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a gentle three quarter view. On the left stands a tall glossy green (#1B5E20) pillar and on the right a tall glossy blue (#0D47A1) pillar, facing each other across the frame, each topped by a small generic unbranded network device with a dark front panel. Between them, reading top to bottom, run five horizontal glowing lanes like glass rails. Lane 1: a glossy charcoal (#212121) packet travels left to right. Lane 2: a matching charcoal packet returns right to left. Lane 3: a brown orange (#993300) packet travels left to right. Lane 4: a matching brown orange packet returns right to left. The first two lanes attach to a small port ring on each pillar, and lanes 3 and 4 attach to a second, lower port ring, showing two different ports. Lane 5, at the bottom, is a thick braided green and blue glowing band running both directions at once, with a small clock face without numbers set at its middle, showing clock sync and then MIDI flowing both ways. Place the label "INITIATOR" at the base of the left pillar and "RESPONDER" at the base of the right pillar, clear of all lanes. No text other than the quoted labels "INITIATOR" and "RESPONDER", no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 12. One network switch carrying two separated VLANs

Now: Two flat colored boxes inside one outlined box, with device names as text.

```
DAPR 2255 - Audio Hardware I
Image: One network switch carrying two separated VLANs
File name: VLAN_Segmentation.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__MIDI_Over_USB_and_Network_Systems/VLAN_Segmentation.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: MIDI: Network Based Show Control Systems (Figure 2)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic studio product shot in a three quarter view from slightly above: a single generic unbranded rack network switch in the center, matte charcoal (#212121) metal, a row of sixteen network ports along its front. The left eight ports have green (#1B5E20) patch cables plugged in and small green port lights; the right eight ports have brown orange (#993300) patch cables and small orange port lights. A faint translucent green glow tints the left half of the switch face and a faint orange glow tints the right half, split cleanly down the middle. The green cables curve out to the left and back to three small generic devices: a compact unbranded mixing console, a small unbranded media server box, and a small unbranded MIDI interface box. The orange cables curve out to the right to three small generic stage lighting fixtures. No cable crosses from one side to the other. Soft studio lighting, real materials, shallow depth of field, clean white seamless background. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 13. Ohm's Law triangle as three glossy pieces

Now: A flat outlined triangle split into V, I and R with an equation line under it.

```
DAPR 2255 - Audio Hardware I
Image: Ohm's Law triangle as three glossy pieces
File name: Overview_Hero.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Ohms_Law/Overview_Hero.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Ohm's Law: Overview (Figure 1)
Fix: None, same content, richer rendering. The equation line under the triangle moves to the caption.

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), landscape close to 4:3. Make it a richly rendered dimensional diagram: a thick equilateral triangle, point up, built from three separate glossy 3D pieces with thin clean gaps between them, seen from a gentle three quarter angle with soft studio shading and a soft shadow on the white surface. A horizontal cut divides the top piece from the bottom half, and a vertical cut divides the bottom half into a left piece and a right piece of equal size. Top piece deep blue (#0D47A1) with a large raised white letter "V". Bottom left piece green (#1B5E20) with a large raised white letter "I". Bottom right piece brown orange (#993300) with a large raised white letter "R". The top piece is lifted slightly above the others, as if a hand had just picked it off, showing the idea of covering one quantity to find it. No text other than the quoted labels "V", "I" and "R", no equation, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 14. Two identical bench circuits, one closed and lit, one broken and dark

Now: Two thin line schematics side by side, one with current arrows and one with a gap.

```
DAPR 2255 - Audio Hardware I
Image: Two identical bench circuits, one closed and lit, one broken and dark
File name: Complete_Path.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Voltage_and_Current/Complete_Path.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Voltage & Current: Read About Basic Current and Voltage and Resistance (Figure 3)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic bench shot from a three quarter view slightly above, clean white seamless surface, soft studio lighting, shallow depth of field. Two identical simple circuits sit side by side, left and right, each laid out as a rectangular loop: a generic unbranded battery holder with one cylindrical cell on the left side of the loop, a small incandescent bulb in a screw socket on the right side, and insulated hookup wire forming the top and bottom of the loop. Left circuit: every wire is connected, the bulb glows warm and bright, and a faint green (#1B5E20) glow runs along the wires in one direction around the loop. Right circuit: identical parts, but the top wire is cut, with its two bare copper ends clearly separated by a visible gap in the middle of the top run; the bulb is dark and cold, and the wires carry no glow anywhere. The gap is the only difference between the two circuits. No text of any kind, no numbers, no plus or minus markings, no logos, no brand marks, no model numbers, no printing on the cells, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 15. One loop with conventional current one way and electron drift the other

Now: A thin line schematic loop with two flat arrows and sentence labels.

```
DAPR 2255 - Audio Hardware I
Image: One loop with conventional current one way and electron drift the other
File name: Conventional_vs_Electron_Flow.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Voltage_and_Current/Conventional_vs_Electron_Flow.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Voltage & Current: Read About Basic Current and Voltage and Resistance (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a gentle three quarter view: a single rectangular circuit loop made of thick glossy copper tubing lying on a white surface, soft studio shading and shadows. On the left side of the loop stands a glossy cylindrical battery upright, its top terminal capped in red (#B71C1C) and marked with a raised "+", its bottom terminal capped in charcoal (#212121) with a raised minus sign. On the right side of the loop sits a glossy blue (#0D47A1) resistor block. Along the outside of the top copper run, a bright glowing brown orange (#993300) band of chevrons points to the right, leaving the red plus terminal and heading toward the resistor: conventional current. Just inside the same top run, a row of small glossy charcoal spheres drifts to the left, each with a faint trailing streak pointing back to the right, so the spheres clearly move the opposite way: electron drift. The same pattern continues around the loop, the orange chevrons going clockwise and the charcoal spheres going counterclockwise. No text other than the quoted label "+" and the raised minus sign on the battery, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 16. Reservoir, pipe and narrow section as a glass water model

Now: A flat outlined tank and pipe with thin arrows and sentence labels for voltage, current and resistance.

```
DAPR 2255 - Audio Hardware I
Image: Reservoir, pipe and narrow section as a glass water model
File name: Reservoir_Analogy_Alt.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Voltage_and_Current/Reservoir_Analogy_Alt.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Voltage & Current: Watch (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic tabletop science model, three quarter view, soft studio lighting, shallow depth of field, clean white seamless background. On the left, a tall clear glass tank filled most of the way with blue tinted water (#0D47A1 tint), water surface catching the light. Beside the tank stands a slim vertical measuring rod with a green (#1B5E20) marker ring set level with the water surface, a double ended green arrow running from the tank base up to the ring, showing the height of the water. From the bottom of the tank, a clear glass pipe runs horizontally to the right; halfway along, the pipe steps down sharply into a much narrower glass section, which is the resistance. Water visibly flows through the pipe with small bubbles streaming to the right, and a brown orange (#993300) glowing arrow floats inside the wide pipe pointing right. The narrow section ends in a small spout that pours a thin steady stream into a shallow glass dish on the right. No text of any kind, no numbers, no scale markings, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 2255 Image 17. Five cut copper conductors shrinking as the gauge number rises

Now: Five flat copper colored circles with gauge and inch labels and a text arrow.

```
DAPR 2255 - Audio Hardware I
Image: Five cut copper conductors shrinking as the gauge number rises
File name: AWG_Runs_Backwards.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Wiring_and_Safety/AWG_Runs_Backwards.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Wiring & Safety: Wire Types & Gauges (Figure 4)
Fix: None, same content, richer rendering. The gauge numbers and inch diameters (10 AWG 0.1019 in, 14 AWG 0.0641 in, 18 AWG 0.0403 in, 22 AWG 0.0253 in, 28 AWG 0.0126 in) move to the caption; update the alt text to match.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Photorealistic macro product shot, soft studio lighting, shallow depth of field. Five short lengths of solid copper wire stand upright in a single row from left to right, each freshly cut flat on top so the bright copper cross section faces the camera from a three quarter angle above, each with a thin band of charcoal (#212121) insulation stripped back a little from the top. Diameters must shrink in exact proportion from left to right: taking the leftmost wire as 1, the others are 0.63, 0.40, 0.25 and 0.12 of that diameter, so the rightmost wire is about one eighth the thickness of the leftmost. Space the wires evenly. Along the white surface in front of them, a soft glowing brown orange (#993300) arrow runs from left to right under the whole row. No text of any kind, no numbers, no labels, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 3255 Audio Hardware II

#### DAPR 3255 Image 12. Three Ascending Course Steps Into Audio Hardware II

Now: A code drawn row of three flat outlined boxes with tiny arrows and a loose red text note; readable but plain.

```
DAPR 3255 - Audio Hardware II
Image: Three Ascending Course Steps Into Audio Hardware II
File name: Course_Sequence_Prerequisites.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Course_Orientation/Course_Sequence_Prerequisites.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Orientation: Prerequisites, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), a wide landscape banner. Show a course sequence as three thick glossy stepping blocks rising left to right like a short staircase, seen in a three quarter view. The first and lowest block on the left is green #1B5E20, the second and taller block in the middle is blue #0D47A1, and the third and tallest block on the right is red #B71C1C. A glowing path of soft light climbs across the tops of the three blocks from left to right and ends on top of the red block. Beside the red block, on its own small pale gray plinth, stands a separate glossy violet #4A148C round medallion with a keyhole in its center, joined to the red block by a short glowing thread, to show one extra requirement that sits alongside the course steps. Keep generous white space above and below so the banner crops cleanly.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D tiles and blocks. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints of these for plinths and floors.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 13. Steady DC Ribbon Beside an Alternating AC Ribbon

Now: Two code drawn line graphs with thin axes and default fonts; correct but flat.

```
DAPR 3255 - Audio Hardware II
Image: Steady DC Ribbon Beside an Alternating AC Ribbon
File name: Flat_Line_and_Sine_Graphs.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Electronics/Flat_Line_and_Sine_Graphs.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Electronics: AC & DC Circuits, Figure 2
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two matching glossy graph panels side by side, each a thin pale gray glass plate standing upright in a slight three quarter view, with a charcoal #212121 vertical axis on the left edge (voltage) and a charcoal horizontal axis along the bottom (time), both ending in small solid arrowheads. Across the middle of each panel runs a faint dashed gray zero line.

Left panel: a thick glossy blue #0D47A1 ribbon runs perfectly level from left to right, well above the zero line, never moving up or down.

Right panel: a thick glossy green #1B5E20 ribbon forms a smooth sine wave centered on the zero line, two full cycles from left to right, rising the same distance above the line as it falls below it, crossing the zero line cleanly each half cycle.

Quote exactly two labels, each centered above its panel in bold charcoal lettering: "DC" above the left panel and "AC" above the right panel.

Style: a richly rendered dimensional diagram with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D ribbons set on glass plates. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for the plates.

No text other than the quoted labels, no numbers, no tick values, no axis words, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens. No real product you could name. No hands or people.
```

#### DAPR 3255 Image 14. Multimeter Connected Three Ways: Across, In Series, and Power Off

Now: Three bordered boxes of text with no picture of how the meter is actually connected.

```
DAPR 3255 - Audio Hardware II
Image: Multimeter Connected Three Ways: Across, In Series, and Power Off
File name: Meter_Voltage_Current_Resistance.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Electronics__Transistor_Biasing_and_Breadboarding/Meter_Voltage_Current_Resistance.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Electronics: Measuring a Circuit with a Multimeter, Figure 1
Fix: None, same content, richer rendering (the image now shows the three connections instead of describing them)

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), a wide landscape banner in three equal side by side bench scenes, each on its own soft tinted mat. Every scene uses the same generic handheld digital multimeter with a dark blank display, a plain rotary dial with no markings, one red probe lead and one black probe lead, and the same tiny circuit: a small battery holder, one resistor and one small LED on a short strip of breadboard.

Scene 1, on a pale blue #0D47A1 tint mat: the battery is connected and the LED is lit. The red and black probe tips touch the two leads of the resistor at the same time, one on each side, so the meter sits across the part in parallel. The circuit itself is unbroken.

Scene 2, on a pale brown orange #993300 tint mat: the battery is connected and the LED is lit. One wire of the circuit is lifted out and the meter is inserted in the gap, red probe to one open end and black probe to the other, so all the current must flow through the meter. The red lead is plugged into a separate small jack on the meter body, a different jack from scenes 1 and 3.

Scene 3, on a pale green #1B5E20 tint mat: the battery holder is unplugged and set clearly apart, its wires loose, and the LED is dark. The resistor has been lifted out of the circuit and lies alone on the mat, with the red and black probes clipped to its two leads with small alligator clips.

Style: photorealistic product photograph, studio lighting, real materials and surface texture, shallow depth of field, clean seamless white background around the three mats. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for the mats.

No text of any kind, no numbers, no symbols on the dial or jacks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible screens (the meter display is dark). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 15. Multicast Flooding Every Port Versus IGMP Snooping to Subscribers Only

Now: Two flat charcoal bars with arrows to six monitor icons; clear but code drawn, and no multicast source is shown.

```
DAPR 3255 - Audio Hardware II
Image: Multicast Flooding Every Port Versus IGMP Snooping to Subscribers Only
File name: Flooded_Versus_Selective_Port_Delivery.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Audio_Network_Architecture/Flooded_Versus_Selective_Port_Delivery.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Multicast and Internet Group Management Protocol (IGMP), Figure 2
Fix: None, same content, richer rendering (a multicast source feeding each switch is added so the stream has a starting point)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two stacked scenes, one above the other, each a generic unbranded charcoal #212121 network switch seen in a three quarter view with six ports along its front, and six small generic receiving devices lined up below it, one cable from each port down to one device. A single source cable enters the top of each switch from a small glossy source block above, carrying a glowing multicast stream.

Top scene: the stream leaves all six ports. All six cables glow red #B71C1C with streams of small glowing packets, and all six devices light up red, including the ones that never asked for it.

Bottom scene: the same switch, but only the first two ports send the stream. Those two cables glow green #1B5E20 with packets, and those two devices light up green. The other four cables are dark and empty, and their four devices stay dim and idle.

Quote exactly two labels, small and bold, placed on the front face of each switch: "SNOOPING OFF" on the top switch and "SNOOPING ON" on the bottom switch.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks with glowing cables. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 16. Four Unicast Copies on the Wire Versus One Multicast Copy

Now: Two flat box diagrams with red and green arrows; correct idea, but the four unicast copies are not shown sharing one wire.

```
DAPR 3255 - Audio Hardware II
Image: Four Unicast Copies on the Wire Versus One Multicast Copy
File name: Four_Copies_Versus_One_Branch.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Audio_Network_Architecture/Four_Copies_Versus_One_Branch.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Multicast and Internet Group Management Protocol (IGMP), Figure 1
Fix: None, same content, richer rendering (the source's single uplink is shown so the copy count on the wire is visible)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two side by side scenes on pale gray floor tiles, separated by clear white space. Each scene has one glossy source block at the top, one short thick cable running down from it into a small charcoal #212121 switch in the middle, and four identical receiving blocks in a row at the bottom, each connected to the switch by its own cable.

Left scene: on the single cable between the source and the switch, four identical glowing red #B71C1C packets travel in a tight row, one behind the other, crowding the cable. Below the switch, one red packet travels down each of the four cables to each receiver.

Right scene: on the single cable between the source and the switch, only one glowing green #1B5E20 packet travels, with open space around it. At the switch it visibly branches into four, and one green packet travels down each of the four cables to each receiver.

Quote exactly two labels, bold, centered under each scene: "UNICAST" under the left scene and "MULTICAST" under the right scene.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks and glowing cables. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 17. Tagged Frames Crossing a Trunk Between Two Switches

Now: Two flat switch boxes joined by a line with small numbered tag rectangles floating above it.

```
DAPR 3255 - Audio Hardware II
Image: Tagged Frames Crossing a Trunk Between Two Switches
File name: Tagged_Frames_on_Link_Between_Switches.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Audio_Network_Architecture/Tagged_Frames_on_Link_Between_Switches.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Assignment: VLAN, IGMP and QoS Plan, Figure 1; Networking: VLANs, Trunk Ports, and Audio/Video over IP, Figure 2
Fix: None, same content, richer rendering (VLAN numbers move to the caption; tag color carries the VLAN in the image)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two generic unbranded charcoal #212121 network switches, one at the left and one at the right, in a three quarter view, joined by one thick glossy cable running between them: the trunk. Under each switch hang two access cables down to two device blocks: a green #1B5E20 tinted device and a blue #0D47A1 tinted device.

On the access cables, frames are small plain glossy packet blocks with no tag, tinted to match their device. On the trunk cable, three packet blocks travel in a row, and each now wears a small bright tag clip on its leading end: the first a green tag, the middle a blue tag, the last a green tag. At the left switch's trunk port, show one tag in the act of clipping onto a plain packet as it enters the trunk. At the right switch's trunk port, show one tag lifting off a packet as it leaves the trunk and drops toward its matching device.

Quote exactly one label, bold, just above the middle of the trunk cable: "TRUNK".

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks, cables and packet tiles. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted label, no numbers on the tags, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 18. Grandmaster Clock Feeding Two Boundary Clocks and Six Devices

Now: A flat tree of labeled red, orange and white boxes with thin connector lines.

```
DAPR 3255 - Audio Hardware II
Image: Grandmaster Clock Feeding Two Boundary Clocks and Six Devices
File name: Three_Tier_Clock_Tree.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Audio_Network_Architecture/Three_Tier_Clock_Tree.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Assignment: Dante Certification Level 3, Figure 1; Networking: Clocking and Precision Time Protocol, Figure 1
Fix: None, same content, richer rendering (each boundary clock's branch sits on its own subnet tile, matching the Level 3 caption)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show a clock hierarchy read top to bottom. At the top center, one large glossy red #B71C1C block with a round clock face on its front showing only tick marks and two hands, glowing softly: the grandmaster. Two glowing cables run down from it to two medium glossy brown orange #993300 blocks, one on the left and one on the right, each with a smaller clock face: the boundary clocks. From each boundary clock, three cables run down to three small pale gray device blocks, each with a tiny clock face. That is exactly one grandmaster, two boundary clocks and six devices.

Each boundary clock and its three devices stand together on their own pale tinted floor tile, left tile pale blue and right tile pale green, to show two separate subnets. Small glowing pulses travel down every cable from top to bottom, and all nine clock faces show the same hand position, so every device follows the grandmaster.

Quote exactly one label, bold, beside the top block: "GRANDMASTER".

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks with glowing cables. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floor tiles.

No text other than the quoted label, no numbers or numerals on any clock face, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 19. Heavy Analog Snake Beside One Light Network Cable

Now: A traced drawing of a multicore fan beside a small cable sketch with arrows, plus text blocks.

```
DAPR 3255 - Audio Hardware II
Image: Heavy Analog Snake Beside One Light Network Cable
File name: Analog_Snake_vs_Network.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Foundations_of_Audio_Networking/Analog_Snake_vs_Network.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Introduction to Audio Networking, Figure 3; Networking: Assignment: Dante Certification Level 1, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A product photograph of two cables side by side on a seamless white sweep.

Left half: the end of a heavy, thick black analog multicore snake, its rubber jacket about as thick as a wrist, lying in a heavy curve. At its end the jacket is stripped back and it fans out into sixteen thinner black tails, each ending in a generic unbranded three pin round XLR style connector with a satin metal shell, all laid out in a neat fan.

Right half: one slim blue #0D47A1 network patch cable with a clear generic RJ45 plug at each end, lying in a light loose loop, visibly thin and light next to the snake. Its jacket is slightly translucent, and inside it faint streams of tiny glowing points travel in both directions at once, to suggest many channels moving both ways on one cable.

Leave a clear gap of white space between the two cables. Style: photorealistic product photograph, studio lighting, real rubber, metal and plastic texture, shallow depth of field, clean seamless white background. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C.

No text of any kind, no numbers, no channel markings, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens. No real product you could name. No hands or people.
```

#### DAPR 3255 Image 20. Console Cabled Straight to a Stage Box Versus Both Through a Shared Switch

Now: Two rows of flat labeled boxes joined by thick lines, with a title and notes as text.

```
DAPR 3255 - Audio Hardware II
Image: Console Cabled Straight to a Stage Box Versus Both Through a Shared Switch
File name: Layer_1_Point_to_Point_vs_Switched.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Foundations_of_Audio_Networking/Layer_1_Point_to_Point_vs_Switched.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Layer 1: Point to Point Protocols, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two rows, one above the other, each with the same two pieces of generic unbranded gear: a compact digital mixing console on the left (charcoal body, rows of faders, a dark screen) and a rack mounted stage box on the right (charcoal chassis with a grid of round input sockets on its front).

Top row: one thick glossy brown orange #993300 cable runs directly from the console to the stage box and nothing else touches it. The cable glows evenly along its whole length, owning the link.

Bottom row: the console and the stage box each run a blue #0D47A1 cable to a generic network switch placed between them. Three more small generic devices (a laptop with a dark screen, a small rack processor and a small amplifier) also plug into the same switch with their own blue cables, so the switch is visibly shared.

Each row sits on its own pale tinted floor tile, the top one pale brown orange and the bottom one pale blue.

Style: a richly rendered dimensional diagram in a three quarter view with realistic generic equipment models, real depth, soft shading, soft contact shadows and solid color fills. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 21. Seven Layer Stack With the Presentation Layer Pulled Out

Now: A column of seven gray outlined text boxes with the sixth outlined in violet and long text notes beside each.

```
DAPR 3255 - Audio Hardware II
Image: Seven Layer Stack With the Presentation Layer Pulled Out
File name: OSI_Stack_Layer_6_Presentation.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Foundations_of_Audio_Networking/OSI_Stack_Layer_6_Presentation.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Networking: Layer 6 Presentation, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), near 4:3 landscape. Show a tall stack of exactly seven thick glossy rectangular slabs, one on top of another, in a three quarter view, like a stack of polished tiles. The bottom slab is layer one and the top slab is layer seven. Six of the slabs are pale matte gray.

The sixth slab from the bottom (the second from the top) is a rich glossy violet #4A148C, glowing softly, and slid forward out of the stack like a drawer so it clearly stands out. Resting on top of the pulled out violet slab, a small sculpture shows encoding: a smooth green #1B5E20 audio waveform ribbon on the left that turns, partway across, into a neat row of evenly spaced glossy sample blocks of varying heights on the right, like the same wave cut into samples.

Keep the stack centered with white space around it.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D tiles. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for the gray slabs.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 22. Seven Layer Stack With the Application Layer Pulled Out

Now: A column of seven gray outlined text boxes with the top box outlined in violet and long text notes beside each.

```
DAPR 3255 - Audio Hardware II
Image: Seven Layer Stack With the Application Layer Pulled Out
File name: OSI_Stack_Layer_7_Application.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Foundations_of_Audio_Networking/OSI_Stack_Layer_7_Application.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Networking: Layer 7 Application, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), near 4:3 landscape. Show a tall stack of exactly seven thick glossy rectangular slabs, one on top of another, in a three quarter view, like a stack of polished tiles. The bottom slab is layer one and the top slab is layer seven. The lower six slabs are pale matte gray.

The top slab, the seventh, is a rich glossy violet #4A148C, glowing softly, and slid forward out of the stack like a drawer so it clearly stands out. Resting on top of it sits a small generic tablet with a dark, softly defocused screen that shows only a faint glowing grid of dots, like a routing matrix, next to a small row of glossy control knobs. This is where routing software and control tools live.

Keep the stack centered with white space around it.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D tiles. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for the gray slabs.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 23. Seven Layer Stack With the Top Three Layers Pulled Out Together

Now: A column of seven gray outlined text boxes with the top three outlined in violet and long text notes beside each.

```
DAPR 3255 - Audio Hardware II
Image: Seven Layer Stack With the Top Three Layers Pulled Out Together
File name: OSI_Stack_Layers_5_to_7.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Foundations_of_Audio_Networking/OSI_Stack_Layers_5_to_7.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Networking: Layer 5: Session, Presentation, and Application, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), near 4:3 landscape. Show a tall stack of exactly seven thick glossy rectangular slabs, one on top of another, in a three quarter view. The bottom slab is layer one and the top slab is layer seven. The lower four slabs are pale matte gray and stay in place.

The top three slabs (fifth, sixth and seventh from the bottom) are glossy violet, each a slightly different shade: the fifth a light violet tint, the sixth a medium violet, the seventh full violet #4A148C. All three slide forward together as one group, glowing softly, clearly separated from the gray slabs below. On each violet slab rests one small object:
1. On the fifth slab: two glossy interlocking chain links, one green and one blue, for a session being set up and kept alive.
2. On the sixth slab: a green #1B5E20 audio waveform ribbon that turns partway across into a neat row of glossy sample blocks, for how the audio is encoded.
3. On the seventh slab: a small generic tablet with a dark, softly defocused screen showing only a faint grid of dots, for routing and control software.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D tiles. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for the gray slabs and the lighter violets.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 24. Seven Colored Layer Slabs With the Lower Four Forward

Now: A flat stack of seven colored bars with a bracket and text, using a yellow outside the course palette.

```
DAPR 3255 - Audio Hardware II
Image: Seven Colored Layer Slabs With the Lower Four Forward
File name: Seven_Colored_Layers_Labeled_in_Order.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Foundations_of_Audio_Networking/Seven_Colored_Layers_Labeled_in_Order.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Introduction to Audio Networking, Figure 2
Fix: None, same content, richer rendering (layer names move to the caption)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show a tall stack of exactly seven thick glossy rectangular slabs, one on top of another, centered, in a three quarter view. Each slab is a different solid color, from the bottom up:
1. Bottom slab: charcoal #212121
2. Brown orange #993300
3. Red #B71C1C
4. Green #1B5E20
5. Blue #0D47A1
6. Violet #4A148C
7. Top slab: a light violet tint

The lower four slabs (charcoal, brown orange, red, green) are slid slightly forward together and lit a little brighter, resting on a faint glowing pale blue base plate that reaches up beside them like a low bracket, marking them as the part of the stack where audio networks live. The upper three slabs sit slightly back and a touch softer in tone.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D tiles. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for the base plate and the top slab.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 25. Straight Through and Crossover Plugs Showing Wire Order

Now: Two flat boxes joined by gray and blue lines with standard names as text; the pin swaps are right, but no real wire colors are shown.

```
DAPR 3255 - Audio Hardware II
Image: Straight Through and Crossover Plugs Showing Wire Order
File name: Straight_Through_vs_Crossover.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Foundations_of_Audio_Networking/Straight_Through_vs_Crossover.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Cable Construction (RJ45), Figure 2
Fix: None, same content, richer rendering (the swap is now shown by real conductor colors: pins 1 and 3 and pins 2 and 6 trade places)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A macro product photograph of two short network patch cables, one above the other, each laid straight across the frame with a clear plastic RJ45 plug at each end. Every plug is turned the same way: gold contacts facing the camera, latch clip underneath and pointing away, so pin one is on the left of each plug. Through the clear plug bodies, the eight individual conductors are sharply visible side by side.

Top cable (charcoal jacket), both plugs identical, left to right in each plug: white with orange stripe, solid orange, white with green stripe, solid blue, white with blue stripe, solid green, white with brown stripe, solid brown.

Bottom cable (blue #0D47A1 jacket): the left plug uses the same order as above. The right plug uses: white with green stripe, solid green, white with orange stripe, solid blue, white with blue stripe, solid orange, white with brown stripe, solid brown. So on the bottom cable the orange pair and the green pair have visibly traded places between the two ends, while blue and brown stay put.

Keep the four plugs large and in sharp focus, with the cable jackets softly falling out of focus between them. Style: photorealistic macro product photograph, studio lighting, real copper, plastic and PVC texture, shallow depth of field, clean seamless white background. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C.

No text of any kind, no printing on the cable jackets, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens. No real product you could name. No hands or people.
```

#### DAPR 3255 Image 26. Switch Address Table Sending a Frame to One Port Only

Now: A flat charcoal box holding a text table with a green arrow from A to C; clear but code drawn.

```
DAPR 3255 - Audio Hardware II
Image: Switch Address Table Sending a Frame to One Port Only
File name: Switch_Table_and_Forwarded_Path.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Foundations_of_Audio_Networking/Switch_Table_and_Forwarded_Path.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Layer 2: Switched Protocols, Figure 1; Networking: Assignment: Map a Dante System to the OSI Layers, Figure 1
Fix: None, same content, richer rendering (the table is shown as color chips instead of text)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show one generic unbranded charcoal #212121 network switch in a three quarter view with four ports along its front. Below it, in a row left to right, stand four glossy device blocks, each cabled to the port directly above it: the first green #1B5E20, the second blue #0D47A1, the third brown orange #993300, the fourth violet #4A148C.

Floating just above the top of the switch is a small glossy lookup table made of four rows of paired chips. In each row a small gray port chip sits beside a colored chip matching the device on that port, in the same left to right order as the ports: green, blue, brown orange, violet. The third row (brown orange) glows brighter than the others.

A glowing frame packet leaves the green device, travels up its cable into the first port, and a bright glowing path then leaves only the third port and runs down to the brown orange device. The second and fourth cables stay dark and empty, with a faint dashed look, to show nothing was sent there.

Quote exactly four labels, one bold letter on the front face of each device: "A" on green, "B" on blue, "C" on brown orange, "D" on violet.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks, chips and glowing cables. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 27. Router Joining Two Subnets, Each Its Own Broadcast Domain

Now: Two flat rounded boxes of monitor icons with IP addresses as text and an orange router circle between them.

```
DAPR 3255 - Audio Hardware II
Image: Router Joining Two Subnets, Each Its Own Broadcast Domain
File name: Two_Subnet_Groups_and_Central_Router.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Foundations_of_Audio_Networking/Two_Subnet_Groups_and_Central_Router.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Layer 3: Routable IP Protocols, Figure 1
Fix: None, same content, richer rendering (addresses move to the caption; each subnet gets its own switch so the router is clearly the only link between them)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two separate glossy floor platforms, one on the left tinted pale blue and one on the right tinted pale green, with open white space between them. On each platform stand three small generic device blocks, each cabled to a small charcoal #212121 switch on that same platform.

Over each platform rises a faint translucent glass dome, blue over the left and green over the right, that ends exactly at the platform edge, to show that a broadcast stays inside its own subnet. Inside the left dome, a soft ripple of light spreads from one device to the other two and stops at the dome wall.

In the gap between the platforms sits one glossy brown orange #993300 router block. One cable runs from the router to the left switch and one cable runs from the router to the right switch. A single glowing packet is shown passing through the router from the left platform to the right platform, the only way across.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks, platforms and glass domes. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for platforms and domes.

No text of any kind, no numbers, no addresses, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 28. Address Octets Under a Mask That Covers the Network Part

Now: Two flat rows of numbered colored boxes with curly braces and text.

```
DAPR 3255 - Audio Hardware II
Image: Address Octets Under a Mask That Covers the Network Part
File name: Octet_Boxes_With_Network_Host_Braces.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__IP_Addressing/Octet_Boxes_With_Network_Host_Braces.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Assignment: Address a Dante System, Figure 1; Networking: IP Addressing Fundamentals, Figure 1
Fix: None, same content, richer rendering (the octet values move to the caption)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show a row of exactly four thick glossy blocks lying side by side in a three quarter view, the four octets of an address, with a small even gap between each block.

Hovering just above them is a matching mask: three solid opaque glossy blue #0D47A1 lids lowered over the first three blocks, and over the fourth block only an empty open frame outline in green #1B5E20, so the fourth block stays exposed. The first three address blocks are blue and the fourth block is green.

Under the row, a long glossy blue bar spans exactly the first three blocks, and a short glossy green bar spans exactly the fourth block, with a clear break between the two bars.

Quote exactly two labels, bold, centered under each bar: "NETWORK" under the blue bar and "HOST" under the green bar.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no numbers on the blocks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 29. Three NDI Variants as Pipes of Falling Bandwidth

Now: Three flat colored bars of descending length with text beside each.

```
DAPR 3255 - Audio Hardware II
Image: Three NDI Variants as Pipes of Falling Bandwidth
File name: Descending_Labeled_Bandwidth_Bars.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Industry_Network_Audio_Protocols/Descending_Labeled_Bandwidth_Bars.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Network: NDI, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show three clear glass pipes lying horizontally, stacked top to bottom with even spacing, all starting at the same left edge, seen in a gentle three quarter view.

Top pipe: the widest and longest, tinted red #B71C1C, packed with a dense stream of large loose glossy cubes, full quality with little packing.
Middle pipe: about half as wide, tinted brown orange #993300, carrying a lighter stream of smaller cubes pressed closer together.
Bottom pipe: the narrowest, tinted green #1B5E20, carrying a thin stream of small, tightly compressed cubes squeezed into dense bricks.

Quote exactly three labels, bold charcoal lettering placed just left of each pipe's start: "NDI" beside the top pipe, "HX3" beside the middle pipe, "HX2" beside the bottom pipe.

Style: a richly rendered dimensional diagram with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D glass pipes and cubes. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for the glass.

No text other than the quoted labels, no numbers beyond those labels, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 30. One Source Splitting Into Separate Video, Audio and Data Streams

Now: A flat source box with arrows to three colored boxes carrying standard numbers as text and a bracket note.

```
DAPR 3255 - Audio Hardware II
Image: One Source Splitting Into Separate Video, Audio and Data Streams
File name: Source_Splitting_into_Three_Streams.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Industry_Network_Audio_Protocols/Source_Splitting_into_Three_Streams.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: SMPTE 2110, Figure 1
Fix: None, same content, richer rendering (the part numbers for video, audio and ancillary data move to the caption)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. On the left, a glossy pale gray source block. From its right face, three separate glowing tubes emerge and fan out slightly, then run in parallel to the right across one shared pale translucent network plate that fills the right two thirds of the frame.

Top tube, blue #0D47A1: carries large flat glossy tiles like small video frames.
Middle tube, green #1B5E20: carries small glossy beads shaped like short waveform segments, for audio.
Bottom tube, brown orange #993300: carries tiny glossy cubes, for ancillary data.

Crossing all three tubes at regular intervals, thin vertical rings of violet #4A148C light line up perfectly across the three tubes at the same positions, like shared clock ticks, to show all three streams keep common timing.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks, glowing tubes and packets. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for the network plate.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 31. AVB Reserving Three Quarters of the Link Across Every Switch

Now: A flat split bar with percentages as text above a row of simple switch icons with check marks.

```
DAPR 3255 - Audio Hardware II
Image: AVB Reserving Three Quarters of the Link Across Every Switch
File name: Split_Bandwidth_Bar_Above_Switch_Row.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Industry_Network_Audio_Protocols/Split_Bandwidth_Bar_Above_Switch_Row.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Network: AVB, Figure 1
Fix: None, same content, richer rendering (the 75 and 25 percent figures move to the caption)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show three generic unbranded charcoal #212121 network switches in a row left to right, seen in a three quarter view, joined by two thick links. Each link is drawn as a wide clear glass channel split lengthwise into two lanes: a wide green #1B5E20 lane taking three quarters of the channel's width, and a narrow gray lane taking the remaining quarter.

In the wide green lane, glossy audio packets travel in a perfectly even, evenly spaced line. In the narrow gray lane, assorted gray packets of mixed sizes travel irregularly, bunched and gapped.

On top of each switch glows a small round green indicator light, all three lit, to show that every switch on the path has agreed to the reservation. The green lane is already open and lit along the full path from the first switch to the last before the packets set off.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks and glass channels. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text of any kind, no numbers, no percentages, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 32. Dante Devices Wired in a Star With Subscriptions Floating Above

Now: Flat light blue boxes around a charcoal switch with green arcs and a text tag for the control software.

```
DAPR 3255 - Audio Hardware II
Image: Dante Devices Wired in a Star With Subscriptions Floating Above
File name: Star_Wired_Devices_With_Subscription_Arrows.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Industry_Network_Audio_Protocols/Star_Wired_Devices_With_Subscription_Arrows.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Network: Dante, Figure 1; Networking: Assignment: Dante Certification Level 2, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. On a pale floor tile, a generic unbranded charcoal #212121 network switch sits in the center. Around it in a star stand five generic devices, each connected to the switch by its own dark cable lying on the floor: a compact mixing console at top center, a rack stage box upper left, a rack amplifier upper right, a small audio interface lower left, and a laptop with a dark screen lower right.

Above the cables, floating in the air, glowing green #1B5E20 arcs connect devices directly to each other, not following the cables: one arc from the stage box to the console, one from the console to the amplifier, and one from the interface to the amplifier. Each arc has a soft arrowhead at its receiving end. The laptop sits inside a soft violet #4A148C halo ring, to mark it as the machine that sets up those arcs in software.

Style: a richly rendered dimensional diagram in a three quarter view with realistic generic equipment models, real depth, soft shading, soft contact shadows and solid color fills. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 33. Three Protocol Discs Overlapping in a Shared AES67 Center

Now: A flat three circle Venn outline with protocol names as text and a text note underneath.

```
DAPR 3255 - Audio Hardware II
Image: Three Protocol Discs Overlapping in a Shared AES67 Center
File name: Three_Circle_Venn_With_Shared_Center.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Industry_Network_Audio_Protocols/Three_Circle_Venn_With_Shared_Center.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Network: AES67, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show three thick translucent tinted glass discs lying nearly flat on a white surface, seen from a high three quarter angle, overlapping like a classic three way Venn arrangement: one disc at the top in blue #0D47A1, one at lower left in green #1B5E20, one at lower right in violet #4A148C. Where two discs overlap, their tints mix softly. In the single small region where all three discs overlap, a bright glossy white gem sits slightly raised and glowing, small compared with the discs, to show the shared common ground is only part of each disc.

Quote exactly four labels, bold charcoal lettering, each placed on white space just outside its disc so no label touches an edge: "DANTE" above the blue disc, "RAVENNA" to the left of the green disc, "LIVEWIRE+" to the right of the violet disc, and "AES67" on the white gem in the center.

Style: a richly rendered dimensional diagram with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D glass discs. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints where the discs overlap.

No text other than the quoted labels, no other numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 34. Four Step DHCP Exchange Between Client and Server

Now: A code drawn sequence diagram with two thin lifelines and four labeled arrows; correct but plain.

```
DAPR 3255 - Audio Hardware II
Image: Four Step DHCP Exchange Between Client and Server
File name: Client_and_Server_Four_Message_Exchange.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Network_Configuration_and_Control/Client_and_Server_Four_Message_Exchange.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Dynamic Host Configuration Protocol (DHCP), Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two tall glossy charcoal #212121 posts standing apart, one on the left and one on the right, with time flowing downward. On top of the left post sits a small generic device block (the client, with no address yet); on top of the right post sits a small generic server block.

Between the posts, four glossy tube shaped arrows cross in order from top to bottom, each sloping slightly downward, evenly spaced:
1. Green #1B5E20, left to right, starting with a soft ring of light around its tail to show it is sent to everyone.
2. Blue #0D47A1, right to left, carrying a small glossy address tag.
3. Green, left to right, carrying the same small tag back as a request.
4. Blue, right to left, ending in a small glowing check mark shape at the client post.

At the bottom of the left post the client block's twin now wears the address tag, to show it has an address.

Quote exactly four labels, bold charcoal, each placed just above its arrow in white space so no label touches a line: "DISCOVER" over arrow one, "OFFER" over arrow two, "REQUEST" over arrow three, "ACKNOWLEDGE" over arrow four.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D posts and tube arrows. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no numbers, no addresses, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 35. Addresses Set One by One Versus Issued From One Server

Now: Two flat groups of empty boxes with text tags and text notes.

```
DAPR 3255 - Audio Hardware II
Image: Addresses Set One by One Versus Issued From One Server
File name: Hand_Labeled_Devices_Versus_Central_Server.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Network_Configuration_and_Control/Hand_Labeled_Devices_Versus_Central_Server.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Address Configuration and Interface Priority, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two side by side scenes on pale floor tiles, separated by white space.

Left scene: four generic device blocks in a row. Each has its own small glossy brown orange #993300 tag hanging from it on a short string, and each tag is a slightly different shape, as if cut and tied on separately. Beside each device lies a tiny separate glossy setting dial, turned to a different position on each, to show every device was set up on its own.

Right scene: the same four device blocks in a row, and above them one larger glossy blue #0D47A1 server block. Four glowing blue tracks run down from the server, one to each device, and each track delivers a matching blue tag of identical shape that snaps onto its device.

Quote exactly two labels, bold charcoal, centered above each scene: "STATIC" above the left scene and "DHCP" above the right scene.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks, tags and glowing tracks. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no writing on the tags, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 36. Plain Unmanaged Switch Beside a Managed Switch and Its Controls

Now: Two flat switch bars with port icons, the managed one with four text callouts.

```
DAPR 3255 - Audio Hardware II
Image: Plain Unmanaged Switch Beside a Managed Switch and Its Controls
File name: Managed_vs_Unmanaged_Switch.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Network_Configuration_and_Control/Managed_vs_Unmanaged_Switch.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Switch Management Basics, Figure 1; Networking: Assignment: Configure a Laptop and a Managed Switch, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. A product photograph of two generic unbranded eight port network switches on a seamless white sweep, side by side with space between them, both seen from the front in a slight three quarter view.

Left: a small plain charcoal #212121 metal desktop switch with eight RJ45 ports in a row and one small green power light. Nothing else.

Right: a similar switch in a deep blue #0D47A1 metal finish with the same eight RJ45 ports, plus one separate extra port set apart at the end for management, with a short gray cable from it running to the edge of a laptop with a dark, closed looking screen at the far right. Floating above the blue switch, in a neat row, are four small glossy dimensional icon tiles connected down to the switch by thin glowing threads: a tile showing a block split into two colored halves (VLAN), a tile showing a fast lane beside a slow lane (priority), a tile showing a funnel letting through only some drops (multicast filtering), and a tile showing a small mirror reflecting a packet (port mirroring).

Quote exactly four labels, small bold charcoal lettering on the face of each tile: "VLAN", "QOS", "IGMP", "MIRROR", in that order left to right.

Style: photorealistic product photograph for the two switches, studio lighting, real metal and plastic texture, shallow depth of field, clean seamless white background, with the four icon tiles rendered as glossy dimensional objects in the same light. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C.

No text other than the quoted labels, no port numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 37. Ping Request Out, Reply Back, Round Trip Measured

Now: A code drawn two lifeline diagram with horizontal arrows and a text bracket.

```
DAPR 3255 - Audio Hardware II
Image: Ping Request Out, Reply Back, Round Trip Measured
File name: Echo_Request_and_Reply_Timing.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Network_Diagnostics/Echo_Request_and_Reply_Timing.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Ping, Figure 1
Fix: None, same content, richer rendering (the arrows now slope downward so travel time is visible)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two tall glossy charcoal #212121 posts, the source on the left and the target on the right, with time flowing downward. A small generic laptop with a dark screen sits on top of the left post, and a small generic device block sits on top of the right post.

A glossy green #1B5E20 tube arrow slopes downward from the left post to the right post, carrying a small packet: the request. Just below where it lands, a glossy blue #0D47A1 tube arrow slopes downward from the right post back to the left post, carrying a packet: the reply.

On the left post, a glowing red #B71C1C bracket spans from the exact point where the green arrow departs down to the exact point where the blue arrow arrives, covering the whole trip out and back.

Quote exactly one label, bold, beside the red bracket in white space to its left: "ROUND TRIP".

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D posts and tube arrows. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted label, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 38. Traceroute Probes Dying One Hop Further Each Time

Now: A row of flat boxes with three stepped arrows marked by TTL numbers, red crosses and dashed returns.

```
DAPR 3255 - Audio Hardware II
Image: Traceroute Probes Dying One Hop Further Each Time
File name: Expanding_Arrows_Halting_Along_Hop_Chain.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Network_Diagnostics/Expanding_Arrows_Halting_Along_Hop_Chain.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Traceroute, Figure 1
Fix: None, same content, richer rendering (the time to live values move to the caption)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Along the bottom, five glossy blocks stand in a row left to right, joined by short cables: a small laptop with a dark screen (the source), three identical charcoal #212121 router blocks, and a pale gray target block at the far right.

Above the row, three glowing green #1B5E20 probe tracks start at the source and run to the right at three heights. The lowest and shortest probe stops directly above the first router and bursts into a small red #B71C1C spark. The middle probe is longer and bursts above the second router. The highest and longest probe bursts above the third router. Each probe carries a row of small fading beads, one fewer bead left at each router it passes, to show its life running out.

From each red burst, a thin glowing blue #0D47A1 track curves back down to the source, so each router that stopped a probe reports back. The three blue returns stay clearly separated and do not cross the green probes.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks and glowing tracks. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 39. No Audio Decision Tree With Four Checks and Four Causes

Now: A flat flowchart of blue diamonds and white outcome boxes, all carried by text.

```
DAPR 3255 - Audio Hardware II
Image: No Audio Decision Tree With Four Checks and Four Causes
File name: Flowchart_of_Diamonds_and_Outcomes.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Network_Diagnostics/Flowchart_of_Diamonds_and_Outcomes.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Troubleshooting Decision Tree, Figure 1
Fix: None, same content, richer rendering (each check and cause is shown by an object; the page text names them)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show a decision tree read top to bottom, slightly left of center. At the top, a glossy red #B71C1C starting tile holding a small speaker with a muted, silent look. Below it, four glossy blue #0D47A1 diamond tiles descend in a single column, joined by short glowing green #1B5E20 connectors (the pass path). Each diamond carries one small raised object on its face:
1. A network port with a small glowing link light.
2. A small address tag.
3. Two small concentric echo rings bouncing back.
4. Two interlocking chain links.

From the right point of each diamond, a short glowing brown orange #993300 connector runs right to a pale gray outcome tile holding one small raised object:
1. Beside the first diamond: a cable end with a bent connector.
2. Beside the second: a small settings gear.
3. Beside the third: a network box split by a thin wall into two halves.
4. Beside the fourth: a small clock face with tick marks only, beside a small routing grid of dots.

Keep the column and the four outcome tiles evenly spaced and aligned, with no connector crossing another.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D tiles with raised icons. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text of any kind, no yes or no words, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 40. Capture Laptop Fed by an Inline Tap and a Mirror Port

Now: A flat switch with colored wires and text labels, where the tap output wire crosses the listener's cable.

```
DAPR 3255 - Audio Hardware II
Image: Capture Laptop Fed by an Inline Tap and a Mirror Port
File name: Inline_Tap_and_Mirror_Port_Wiring.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Network_Diagnostics/Inline_Tap_and_Mirror_Port_Wiring.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Wireshark Setup and Capture Basics, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. At the top center, one generic unbranded charcoal #212121 network switch with four ports on its front, in a three quarter view. Below it, left to right on a pale floor: a glossy blue #0D47A1 tinted talker device, a glossy green #1B5E20 tinted listener device, and a generic laptop with a dark screen on a brown orange #993300 tinted pad (the capture computer).

The talker's cable does not go straight to the switch: it passes through a small glossy red #B71C1C inline tap box sitting on the floor between the talker and the switch, then continues up to the first port. From the tap, a second red cable runs along the floor behind the listener (never crossing its cable) to the capture laptop, carrying copies of the glowing packets that pass through the tap.

The listener's cable runs up to the second port. From the fourth port, a brown orange cable runs down to the capture laptop, and inside the switch a faint glowing copy of the talker's traffic is shown flowing across to that fourth port, to show it is mirrored there. The third port is empty.

Quote exactly two labels, bold charcoal: "TAP" on the face of the red tap box and "MIRROR" beside the fourth port.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D blocks and glowing cables. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 41. Six Rung Diagnostic Ladder, Physical Link at the Bottom

Now: A flat stack of colored rounded bars beside an arrow, with tool names as text and a yellow outside the course palette.

```
DAPR 3255 - Audio Hardware II
Image: Six Rung Diagnostic Ladder, Physical Link at the Bottom
File name: Six_Rung_Ladder_With_Tool_Labels.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Networking__Network_Diagnostics/Six_Rung_Ladder_With_Tool_Labels.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Networking: Assignment: Work a Fault Down the Diagnostic Ladder, Figure 1; Networking: Diagnostic Ladder, Figure 1
Fix: None, same content, richer rendering (tool names move to the caption)

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show one upright glossy ladder, centered, in a three quarter view, with two charcoal #212121 side rails and exactly six wide rungs, each rung a thick glossy colored bar. From the bottom rung up: brown orange #993300, red #B71C1C, a light brown orange tint, violet #4A148C, green #1B5E20, blue #0D47A1.

On each rung rests one small raised object, bottom to top:
1. A network port with a small glowing link light.
2. A small address tag.
3. Two small concentric echo rings bouncing back.
4. A short chain of three stepping stones, for the path.
5. A thick pipe with a flow gauge, for bandwidth.
6. A small generic tablet with a dark, defocused screen, for the audio application.

Beside the ladder rises a tall glowing arrow pointing up, starting level with the bottom rung. The bottom rung glows slightly brighter, as the place to start.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D rungs and small objects. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 42. Two Capture Points: Mirrored Switch Port and Inline Tap

Now: Two rows of flat labeled boxes with product and port details written as text.

```
DAPR 3255 - Audio Hardware II
Image: Two Capture Points: Mirrored Switch Port and Inline Tap
File name: Capture_Points_Mirror_and_Tap.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Software_Tools/Capture_Points_Mirror_and_Tap.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Software: Network Capture and Analysis, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show two rows, one above the other, each on its own pale floor tile.

Top row, left to right: a generic rack audio device, a cable to a blue #0D47A1 managed switch with eight ports, and a generic laptop with a dark screen on a violet #4A148C tinted pad, cabled to the last port of the switch. Glowing packets travel from the audio device into the first port; inside the switch, a faint violet copy of each packet glides across to the last port and down the cable to the laptop.

Bottom row, left to right: the same audio device, a cable into a small glossy red #B71C1C inline tap box, and a cable out of the tap to a single switch port block on the right. Glowing packets pass straight through the tap. From the bottom of the tap, a short red cable drops down to a second laptop with a dark screen on a violet tinted pad, carrying copies of every packet.

Quote exactly two labels, bold charcoal, at the left end of each row: "MIRROR" beside the top row and "TAP" beside the bottom row.

Style: a richly rendered dimensional diagram in a three quarter view with realistic generic equipment models, real depth, soft shading, soft contact shadows and solid color fills. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text other than the quoted labels, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 43. Five Step Design Cycle With the Pull Back Step Highlighted

Now: Five flat outlined text boxes in a row with a gray return arc and a red text warning.

```
DAPR 3255 - Audio Hardware II
Image: Five Step Design Cycle With the Pull Back Step Highlighted
File name: Design_Online_Push_Adjust_Cycle.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Software_Tools/Design_Online_Push_Adjust_Cycle.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Software: DSP and System Configuration Platforms, Figure 1
Fix: None, same content, richer rendering

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Show five thick glossy tiles in a gentle arc from left to right, joined by short glowing arrows, each tile holding one small raised scene:
1. Green #1B5E20 tile: a laptop with a dark screen beside a blueprint sheet with only a faint grid, and an unplugged cable lying loose: the design built offline.
2. Green tile: the same laptop now cabled to a generic rack DSP unit whose small link light glows: going online and matching the real hardware.
3. Green tile: a glowing stream of blocks flowing from the laptop into the rack unit, with a small speaker beside it showing a muted, silent look: pushing the design, when audio may drop.
4. Green tile: the rack unit alone with one of its front knobs glowing and turned: adjusting live in the hardware.
5. Red #B71C1C tile, slightly larger and raised above the others: a glowing stream flowing back from the rack unit into a small document folder, which closes and glows.

From the red tile, a wide charcoal #212121 return arrow sweeps under the row back to the first tile, closing the cycle.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D tiles with small raised scenes. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for floors.

No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3255 Image 44. Four Jobs of Wireless Management: Inventory, Spectrum, Calculation, Monitoring

Now: Four flat teal outlined text boxes in a row with small arrows.

```
DAPR 3255 - Audio Hardware II
Image: Four Jobs of Wireless Management: Inventory, Spectrum, Calculation, Monitoring
File name: Wireless_Management_Four_Jobs.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Software_Tools/Wireless_Management_Four_Jobs.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Software: Wireless System Management, Figure 1
Fix: None, same content, richer rendering (the teal outside the course palette becomes course green)

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), a wide landscape banner. Show four thick glossy pale green tiles in a row left to right, joined by short glowing green #1B5E20 arrows, each tile holding one small raised scene:
1. Inventory: a neat row of generic unbranded wireless bodypack transmitters and a pair of small rack receivers, lined up like stock on a shelf.
2. Spectrum: a glossy 3D landscape of a frequency spectrum, a ribbon of peaks and valleys, with a few wide solid blue #0D47A1 blocks standing in it where the band is already occupied.
3. Calculation: the same spectrum ribbon with several slim green markers placed in the clear gaps, and a few tiny red #B71C1C spikes (intermodulation products) sitting between them, none touching a green marker.
4. Monitoring: a small cluster of three glowing vertical meter bars (signal, audio, battery), the battery bar shaped like a small battery.

Keep the four tiles evenly spaced with white space above and below for cropping.

Style: a richly rendered dimensional diagram in a three quarter view, with real depth, soft shading, soft contact shadows and solid color fills, like glossy 3D tiles with small raised scenes. Not flat vector, not line art, not clip art. Palette: charcoal #212121, green #1B5E20, blue #0D47A1, red #B71C1C, brown orange #993300, violet #4A148C, with lighter tints for the tiles.

No text of any kind, no numbers, no frequency scales, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 3340 Spatial Audio I

#### DAPR 3340 Image 15. Nine ear level speakers and four height speakers around one listener

Now: A code drawn top down plan with dashed lines, outline speaker shapes and a text legend; it reads as a flat square rather than a speaker shell around a listener.

```
DAPR 3340 - Spatial Audio I
Image: Nine ear level speakers and four height speakers around one listener
File name: Ambisonics_Nine_Zero_Four_Speaker_Layout.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonics_Nine_Zero_Four_Speaker_Layout.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Sessions: Ambisonics and 9.0.4
Fix: None, same content, richer rendering. The layout stays an upper hemisphere (ear level plus height, nothing below the listener), so the alt text "full sphere" should be changed to "upper hemisphere" on the page.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram seen from an elevated three quarter angle behind and above the listening position, with soft shading and depth, like glossy 3D objects on glass. At the center sits a smooth charcoal (#212121) mannequin head form with a small nose showing it faces away from the viewer toward the top of the frame. Around it, on a pale blue (#E3F2FD) translucent circular floor disc, stand exactly nine small glossy blue (#0D47A1) monitor speakers at ear height, all aimed at the head: one center straight ahead, one front left and one front right about 30 degrees off center, one wide left and one wide right about 60 degrees off center, one side left and one side right about 100 degrees off center, and one rear left and one rear right about 140 degrees off center. There is no speaker directly behind the head. Above the head, on a faint translucent ring, hang exactly four glossy brown orange (#993300) height speakers angled down at the head: top front left, top front right, top rear left and top rear right. A very faint translucent pale green (#E8F5E9) dome rises from the ear level ring over the height ring, showing an upper half shell only, with nothing below ear level and no subwoofer anywhere. Thin softly glowing lines run from every speaker to the head. Soft contact shadows. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 16. One Atmos master branching into every deliverable

Now: A flat box tree with text in every box; the structure is right but it is a plain code drawn chart.

```
DAPR 3340 - Spatial Audio I
Image: One Atmos master branching into every deliverable
File name: Deliverable_Tree.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Creating_Dolby_Atmos_Deliverables/Deliverable_Tree.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Deliverables: What Makes an Immersive Delivery; Creating Dolby Atmos Deliverables
Fix: None, same content, richer rendering. Deliverable names (ADM BWF, IMF IAB, binaural, re renders to 7.1, 5.1 and stereo) move to the page caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional tree diagram in a gentle three quarter view from above, with soft shading and depth, like glossy 3D blocks joined by glowing cables. Top center: one large glossy green (#1B5E20) master slab with a softly glowing wireframe sphere floating above it, dotted with small bright points to suggest sounds placed in 3D. Four glowing blue (#0D47A1) cables fan down from the master to a row of four glossy blue tiles, evenly spaced left to right. Tile one holds a thick audio file block made of many stacked thin colored lanes with a slim metadata ribbon along its top edge (the master file). Tile two holds a flat sealed package block with a small film reel emblem pressed into its face (the cinema and streaming package). Tile three holds a pair of generic closed back headphones (binaural). Tile four holds a small cluster of speakers (re renders). From tile four only, three brown orange (#993300) cables drop to three smaller brown orange tiles in a row beneath it: the first holds a miniature ring of seven small speakers plus one small subwoofer cube, the second holds a miniature ring of five small speakers plus one small subwoofer cube, the third holds a single pair of small speakers side by side. Soft contact shadows on white. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 17. Final exam topic weights as nine descending bars

Now: A flat horizontal bar chart with nine long text labels; it is a plain code drawn chart.

```
DAPR 3340 - Spatial Audio I
Image: Final exam topic weights as nine descending bars
File name: Final_Exam_Coverage_Map.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Final_Project_and_Final_Exam/Final_Exam_Coverage_Map.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Final Study Guide
Fix: None, same content, richer rendering. The topic names move to the page, listed top to bottom in bar order: Foundations of Spatial Audio; Surround Microphone Arrays; Speaker Layout and Playback; Localization and Spatial Hearing; Ambisonics; Immersive Audio Concepts; Surround Recording Principles; Capture and Gain Structure; Additional Concepts.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional bar chart in a gentle three quarter view, with soft shading and depth, like glossy 3D bars resting on a thin pale gray (#F1F3F1) plinth. Exactly nine thick rounded bars lie horizontally, stacked from top to bottom with equal gaps, all starting from the same left edge and extending to the right. Their lengths step down from top to bottom in these proportions of the longest: full length, nine tenths, eight tenths, seven tenths, just over half, just under half, about a third, about a quarter, about a fifth. The top four bars are glossy green (#1B5E20), the next three are glossy blue (#0D47A1), the bottom two are glossy brown orange (#993300). Each bar casts a soft shadow onto the plinth. Nothing else in the frame: no axis, no gridlines, no legend. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 18. Fixed 7.1.2 bed speakers with free floating objects in the room

Now: A flat numbered strip of ten bed cells with numbered circles on sticks above it; it shows counts but not the idea of fixed channels versus positions in a room.

```
DAPR 3340 - Spatial Audio I
Image: Fixed 7.1.2 bed speakers with free floating objects in the room
File name: Bed_and_Object_Structure.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Bed_and_Object_Structure.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mixing in Dolby Atmos: Beds vs Objects
Fix: None, same content, richer rendering. The bed keeps exactly ten channels (7.1.2) and there are eight objects.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram of a translucent room box seen from an elevated three quarter angle behind the listening position, with soft shading and depth. The room floor is a pale gray (#F1F3F1) glass slab and the walls and ceiling are faint clear glass edges. At the center of the floor sits a small charcoal (#212121) mannequin head facing the front wall. The bed is exactly ten fixed speakers, each a matte charcoal box locked into a visible wall or ceiling bracket: front left, center and front right on the front wall; side left and side right on the side walls; rear left and rear right on the back wall; one subwoofer cube on the floor near the front wall; and two ceiling speakers, top left and top right, above the middle of the room. Floating freely inside the room are exactly eight small glowing spheres at clearly different positions and heights, colored green (#1B5E20), blue (#0D47A1) and brown orange (#993300) in a mixed order; each sphere drops a thin dotted line to a small glowing dot on the floor to show where it sits, and two of the spheres trail faint curved motion paths. The contrast should be obvious: the ten speakers are bolted in place, the eight spheres drift anywhere in the space. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 19. Seven stage expanded mastering chain

Now: A banner of seven outlined boxes with text titles and simple line icons (a pentagon, a diamond, a star) that do not show what each process does.

```
DAPR 3340 - Spatial Audio I
Image: Seven stage expanded mastering chain
File name: Full_Chain_of_Boxed_Processor_Icons.jpg
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mastering_and_Surround_Encoding/Full_Chain_of_Boxed_Processor_Icons.jpg
Size: 1600 x 500 px
Format: JPEG, quality 88
Used on: Loudness (Figure 3)
Fix: None, same content, richer rendering. Stage order stays EQ, dynamics, post EQ, harmonic exciter, stereo imaging, reverb, loudness maximizer; names go in the caption.

Create a 1600 x 500 pixel JPEG, a very wide banner (generate wide landscape; it will be cropped to a banner). Make it a richly rendered dimensional diagram on a soft, evenly lit pale gray (#EEF0EE) seamless studio background, seen from a gentle three quarter angle, with soft shading and depth. Exactly seven glossy rounded processor modules sit in one straight row from left to right with equal spacing, alternating deep blue (#0D47A1) and deep green (#1B5E20) bodies, joined by one glowing brown orange (#993300) patch cable that runs left to right through all of them with small light pulses traveling right. Each module carries one raised glowing relief on its top face that shows its job: module one, a smooth bell shaped frequency curve (EQ); module two, a waveform squeezed flat between two pressing plates (dynamics); module three, a gentle shelf shaped frequency curve (post EQ); module four, a waveform sprouting small bright sparkling overtone ripples (harmonic exciter); module five, a sound field widening outward with a double ended arrow (stereo imaging); module six, concentric ripples fading as they spread (reverb); module seven, a dense waveform pressed up against a flat glowing ceiling (loudness maximizer). Soft contact shadows. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 20. Many channel faders for mixing beside one master section for mastering

Now: Cartoon faders and knobs under large text headings; the point is right but it is flat clip art.

```
DAPR 3340 - Spatial Audio I
Image: Many channel faders for mixing beside one master section for mastering
File name: Mixing_versus_Mastering.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mastering_and_Surround_Encoding/Mixing_versus_Mastering.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Mastering Overview
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a photorealistic product photograph with soft studio lighting, real brushed metal and matte plastic, and gentle shallow depth of field. Two pieces of generic, unbranded studio hardware sit side by side on the white seamless background with a clear gap between them. On the left, a section of a mixing console surface with exactly eight identical channel strips; each strip has one small deep blue (#0D47A1) knob near the top and a long fader with a brown orange (#993300) cap, and the eight fader caps sit at clearly different heights to show many separate balances. On the right, a compact mastering control unit with exactly three large precision stepped knobs in deep blue in a row across its top, and a single wide master fader below them with one brown orange cap set at the middle, showing one control for one finished program. Both panels are blank, with no printing and no scale markings. Soft contact shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 21. Four band multiband compressor with one band working hard

Now: Flat bars hanging between two blue rules with "Input" and "Output" text; it does not look like a frequency spectrum split at crossover points.

```
DAPR 3340 - Spatial Audio I
Image: Four band multiband compressor with one band working hard
File name: Multiband_Crossover_Bands.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mastering_and_Surround_Encoding/Multiband_Crossover_Bands.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Multiband Compression
Fix: None, same content, richer rendering. The image keeps four bands (low, low mid, high mid, high) as in the current file; the page alt text says low, mid and high, so update the alt to four bands.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a gentle three quarter view, with soft shading and depth. A long glossy spectrum slab lies across the frame, running from low frequencies at the left to high frequencies at the right, its top surface shaped like a smooth program spectrum. Three thin glowing blue (#0D47A1) glass walls stand upright across the slab at the crossover points, dividing it into exactly four bands of similar width. Above the slab runs one straight glowing blue rail marking the input level. From that rail, a translucent block hangs down into each band showing how much that band is being turned down: in the lowest band a short green (#1B5E20) block, in the low mid band a long brown orange (#993300) block reaching about four times deeper than the low one, and in the high mid and high bands only very thin green slivers. The low mid band surface sits visibly lower than its neighbors under its long block. Soft contact shadows. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 22. Four stage typical mastering chain

Now: A banner of four outlined boxes with text titles and line icons (a pentagon and a star) that do not show what the processes do.

```
DAPR 3340 - Spatial Audio I
Image: Four stage typical mastering chain
File name: Short_Chain_of_Boxed_Processor_Icons.jpg
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mastering_and_Surround_Encoding/Short_Chain_of_Boxed_Processor_Icons.jpg
Size: 1600 x 500 px
Format: JPEG, quality 88
Used on: Loudness (Figure 2)
Fix: None, same content, richer rendering. Stage order stays EQ, dynamics, post EQ, loudness; names go in the caption.

Create a 1600 x 500 pixel JPEG, a very wide banner (generate wide landscape; it will be cropped to a banner). Make it a richly rendered dimensional diagram on a soft, evenly lit pale gray (#EEF0EE) seamless studio background, seen from a gentle three quarter angle, with soft shading and depth. Exactly four glossy rounded processor modules sit in one straight row from left to right with wide, equal spacing, alternating deep blue (#0D47A1) and deep green (#1B5E20) bodies, joined by one glowing brown orange (#993300) patch cable running left to right with small light pulses traveling right. Each module carries one raised glowing relief on its top face: module one, a smooth bell shaped frequency curve (EQ); module two, a waveform squeezed flat between two pressing plates (dynamics); module three, a gentle shelf shaped frequency curve (post EQ); module four, a dense waveform pressed up against a flat glowing ceiling (loudness). Match the look of a seven module version of this same chain so the two banners read as a set. Soft contact shadows. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 23. DAW session flow from tracks through stems and submaster to surround output

Now: A tall stack of orange outlined text boxes topped by real software application icons, which breaks the no brand rule and teaches the flow only in words.

```
DAPR 3340 - Spatial Audio I
Image: DAW session flow from tracks through stems and submaster to surround output
File name: Production_Session_Flow_Chart.jpg
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Production_Session_Flow_Chart.jpg
Size: 1200 x 1800 px
Format: JPEG, quality 88
Used on: Final Mix Creation (Figure 2)
Fix: None, same content, richer rendering; the branded application icons are removed and the step text moves to the caption.

Create a 1200 x 1800 pixel JPEG, tall portrait. Make it a richly rendered dimensional flow diagram on a soft, evenly lit pale gray (#EEF0EE) seamless studio background, read from top to bottom, seen from a gentle three quarter angle, with soft shading and depth, like glossy 3D blocks joined by glowing cables. Step one, top: a thick glossy green (#1B5E20) session file block with a plain waveform emblem pressed into its face. Step two: exactly twelve thin glossy track strips side by side, each with a small waveform relief, in mixed green, blue (#0D47A1) and brown orange (#993300). Step three: the twelve strips feed down by glowing cables into exactly four thicker stem bus blocks, grouped by color. Step four: each of the four stem blocks passes through its own small fader module (the premix). Step five: all four merge into one single wide charcoal (#212121) submaster block with two small glowing insert modules sitting on top of it, above its fader. Step six: one tall master fader block. Step seven: a generic unbranded audio interface rack unit with a blank front and a row of output jacks. Step eight, bottom: glowing cables leave the jacks to a miniature surround speaker ring of five small speakers plus one small subwoofer cube around a tiny listener sphere, with a small stereo pair set just beside the ring. Each step sits on its own soft pale tile with a short glowing cable to the next, all centered in one column. Soft contact shadows. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 24. Static automation line against a dynamic automation curve

Now: Two flat boxed lanes with a gray waveform and thin automation lines under text labels; correct but plain.

```
DAPR 3340 - Spatial Audio I
Image: Static automation line against a dynamic automation curve
File name: Static_versus_Dynamic_Automation.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Static_versus_Dynamic_Automation.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Automation
Fix: None, same content, richer rendering.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram with soft shading and depth, seen from a gentle three quarter angle. Two long glossy frosted glass lanes lie stacked one above the other with a clear gap, time running left to right. Inside each lane, recessed into the glass, is the same soft pale gray audio waveform with eight bursts of sound spaced along it. Upper lane: a single glowing green (#1B5E20) rod runs perfectly straight and level along the upper part of the lane from the left edge to the right edge, with one glossy square node at its far left start and no other nodes (static automation). Lower lane: a smooth glowing brown orange (#993300) ribbon curve with exactly five glossy square nodes: it starts low at the far left, rises smoothly to a high plateau by about a quarter of the way, holds level until just past halfway, dips smoothly to a low point at about two thirds of the way, then rises smoothly to finish high at the far right edge (dynamic automation). Soft glows beneath each line and soft contact shadows on white. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 25. Six step surround mix workflow

Now: A row of flat numbered boxes with clip art icons (a printer for printing the mix) and text labels.

```
DAPR 3340 - Spatial Audio I
Image: Six step surround mix workflow
File name: Surround_Mix_Workflow.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Surround_Mix_Workflow.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Surround Mixing Overview
Fix: None, same content, richer rendering. Step order stays session prep, output configuration, static balance, panning and placement, automation, print the mix; names go in the caption. The paper printer icon is replaced by a recorded master file, since printing a mix means recording it.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional process diagram in a gentle three quarter view, with soft shading and depth, like glossy 3D tiles on a path. Exactly six glossy rounded tiles sit in one row from left to right, alternating green (#1B5E20) and blue (#0D47A1) rims, joined by a glowing blue path with small light pulses moving right. Each tile holds one small 3D object: tile one, a neat stack of color coded track slabs squared up beside a blank clipboard (session prep); tile two, a small patch block with cables running into a miniature ring of five speakers and one subwoofer cube (output configuration); tile three, a brass balance scale with its two pans level (static balance); tile four, a small joystick panner standing in the middle of a miniature speaker ring with a glowing dot placed between two speakers (panning and placement); tile five, a curved glowing brown orange (#993300) ribbon with round nodes rising and falling over a lane (automation); tile six, a thick multichannel master file block with a glowing red (#B71C1C) record dot on its face (print the mix). Soft contact shadows on white. Nothing else in the frame. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 26. Bass management sending main channel lows and the LFE to one subwoofer

Now: A flat block diagram with text channel labels and simple speaker icons; correct but plain.

```
DAPR 3340 - Spatial Audio I
Image: Bass management sending main channel lows and the LFE to one subwoofer
File name: Bass_Management_Signal_Path.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Monitoring/Bass_Management_Signal_Path.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Bass Management
Fix: None, same content, richer rendering. Channel names L, C, R, Ls, Rs go in the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional signal path diagram in a gentle three quarter view, read left to right, with soft shading and depth, like glossy 3D objects joined by glowing cables. On the left, exactly five glowing green (#1B5E20) cables enter from the left edge, stacked evenly, and plug into the left face of a tall glossy charcoal (#212121) crossover block in the center left of the frame. On the top face of the block is a raised glowing relief of one curve splitting into two: a high branch and a low branch. From the right face of the block, exactly five glowing blue (#0D47A1) cables run right to a column of exactly five small, identical, generic satellite speakers facing the viewer. From the bottom of the block, one thick glowing brown orange (#993300) cable carries the combined low end down and right to a large glossy subwoofer cabinet in the lower right, with a real looking woofer cone. Separately, from the lower left edge, one dashed brown orange cable travels right along the bottom of the frame without touching the crossover block and joins the thick cable just before the subwoofer, labeled "LFE" in clear white space just above its left end. The label touches nothing. No text other than the quoted label "LFE", no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 27. Five cardioid surround system seen from above

Now: Five flat cartoon cardioid shapes with no mounts and no scale, a plain code drawn figure.

```
DAPR 3340 - Spatial Audio I
Image: Five cardioid surround system seen from above
File name: Cardioid_Pattern_Array_Layout.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Cardioid_Pattern_Array_Layout.png
Size: 1200 x 1200 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 3)
Fix: None, same content, richer rendering. The spacing range (about 10 cm to 1.5 m) stays in the caption.

Create a 1200 x 1200 pixel PNG with a solid white background (#FFFFFF), square. Make it a photorealistic top down product photograph, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte metal. On the white seamless surface stand exactly five identical generic, unbranded small pencil condenser microphones with matte charcoal (#212121) bodies, each on its own short low stand, arranged like a five speaker surround layout with the front toward the top of the frame. One center microphone at top center points straight toward the top of the frame. A front left and a front right microphone sit lower and wider, level with each other, aimed outward about 45 degrees from straight ahead. A rear left and a rear right microphone sit near the bottom corners, wider apart than the front pair, aimed back and outward about 135 degrees from straight ahead. Under each microphone a soft translucent green (#1B5E20) heart shaped cardioid pickup lobe glows on the white surface, pointing the way the microphone points, with its rear notch toward the middle of the layout. The middle of the frame is empty white. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 28. Double mid side: front cardioid, rear cardioid and one side figure eight

Now: Four flat overlapping lobes with text headings and plus and minus marks; correct but a crude cartoon.

```
DAPR 3340 - Spatial Audio I
Image: Double mid side: front cardioid, rear cardioid and one side figure eight
File name: Facing_Bidirectional_Polar_Pattern_Diagram.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Facing_Bidirectional_Polar_Pattern_Diagram.png
Size: 1200 x 1200 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 11)
Fix: None, same content, richer rendering.

Create a 1200 x 1200 pixel PNG with a solid white background (#FFFFFF), square. Make it a photorealistic product photograph seen from above at a slight three quarter tilt, soft studio lighting, real matte metal. At the center of the white seamless surface, three generic, unbranded microphones are clamped together on one small mount as a tight coincident cluster, capsules nearly touching. One small pencil condenser points straight toward the top of the frame (the front cardioid). A second identical pencil condenser points straight toward the bottom of the frame (the rear cardioid). Between and just above their capsules sits one side address large diaphragm microphone whose two open faces point left and right (the figure eight). Beneath the cluster, soft translucent pickup lobes glow on the white surface: a green (#1B5E20) heart shaped cardioid lobe extending toward the top of the frame, a blue (#0D47A1) heart shaped cardioid lobe extending toward the bottom, and a figure eight of two round lobes extending left and right, the left lobe a clear bright violet (#4A148C) and the right lobe a darker, deeper shade of the same violet to show opposite polarity. The label "+" sits in clear white space just outside the left lobe. No text other than the quoted label "+", no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 29. OCT front array with optional rear cardioids

Now: Flat cartoon capsules with measurements written on the drawing; the geometry is right but it is a code drawn figure.

```
DAPR 3340 - Spatial Audio I
Image: OCT front array with optional rear cardioids
File name: Five_Microphone_Surround_Array_Diagram.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Five_Microphone_Surround_Array_Diagram.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 6)
Fix: None, same content, richer rendering. Distances go in the caption (C 8 cm, about 3 in, forward; L to R 40 to 100 cm, about 15 to 40 in).

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), wide landscape near 4:3. Make it a photorealistic top down product photograph, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte metal. The front (toward the sound source) is the top of the frame. On the white seamless surface lies a generic, unbranded straight horizontal microphone bar in the upper part of the frame. At its left end a small pencil microphone points straight left; at its right end an identical microphone points straight right; these two are supercardioids, so under each glows a translucent green (#1B5E20) narrow front lobe pointing outward plus a small separate rear lobe pointing back toward the bar center. At the exact middle of the bar a very short stub, only about one tenth of the bar length, holds a third small microphone pointing straight toward the top of the frame, with a translucent green heart shaped cardioid lobe under it. Lower in the frame, well behind the bar, stand two more small pencil microphones on their own short stands, spaced a little narrower than the front bar, aimed back and outward about 135 degrees from straight ahead, each with a translucent pale green (#E8F5E9) cardioid lobe drawn lighter than the front lobes to show they are optional. All microphone bodies are matte charcoal (#212121). No text of any kind, no numbers, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 30. Fukada Tree with omni outriggers and rear cardioids

Now: A flat cartoon array with many text labels and distances; the geometry is right but it is a code drawn figure.

```
DAPR 3340 - Spatial Audio I
Image: Fukada Tree with omni outriggers and rear cardioids
File name: Fukada_Tree.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Fukada_Tree.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 15)
Fix: None, same content, richer rendering. Distances go in the caption (L to R 1.8 m; C 1 m forward; omni outriggers 1 m outside L and R; Ls and Rs 0 to 2 m behind L and R).

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a photorealistic top down product photograph of a large generic, unbranded microphone tree rig, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte black metal booms. The front (toward the orchestra) is the top of the frame. A long straight horizontal boom crosses the upper middle of the frame. Two cardioid pencil microphones sit on it, well apart (L and R), aimed forward and outward about 60 degrees from straight ahead. A forward arm from the middle of the boom, a little over half as long as the L to R spacing, holds a third cardioid (C) pointing straight toward the top of the frame. Farther out on the same boom line, beyond L and beyond R by a little over half the L to R spacing, sit two omnidirectional microphones with rounded ball tips (the outriggers). Lower in the frame, directly behind L and behind R, two more cardioid microphones on short drop arms aim back and outward about 135 degrees from straight ahead (Ls and Rs). Under every cardioid a soft translucent green (#1B5E20) heart shaped lobe glows on the white surface pointing the way the microphone points, and under each omni a soft translucent blue (#0D47A1) circular disc. All microphone bodies are matte charcoal (#212121). No text of any kind, no numbers, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 31. Hamasaki Square of four figure eight microphones

Now: Four pairs of flat circles with text labels and distances; the idea is right but it is a code drawn figure.

```
DAPR 3340 - Spatial Audio I
Image: Hamasaki Square of four figure eight microphones
File name: Hamasaki_Square.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Hamasaki_Square.png
Size: 1600 x 1200 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 9)
Fix: None, same content, richer rendering. The square is about 2 m, about 6.5 ft, on a side; that goes in the caption.

Create a 1600 x 1200 pixel PNG with a solid white background (#FFFFFF), wide landscape near 4:3. Make it a photorealistic top down product photograph, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte metal. The front (toward the stage) is the top of the frame, marked only by a soft wide warm glow along the top edge. On the white seamless surface stand exactly four identical generic, unbranded side address large diaphragm microphones on short stands at the four corners of a perfect square. Each microphone is turned so its two open faces point straight left and straight right, which puts its dead side toward the front and back. Under each microphone a translucent green (#1B5E20) figure eight pickup pattern glows on the white surface: two round lobes side by side, one extending left and one extending right. The middle of the square is empty white. All microphone bodies are matte charcoal (#212121). No text of any kind, no numbers, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 32. OCT front array ahead of a Hamasaki Square

Now: Flat cartoon capsules and paired circles with text labels and distances; correct geometry in a code drawn figure.

```
DAPR 3340 - Spatial Audio I
Image: OCT front array ahead of a Hamasaki Square
File name: Microphone_Spacing_Diagram_With_Measurements.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Microphone_Spacing_Diagram_With_Measurements.png
Size: 1200 x 1200 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 10)
Fix: None, same content, richer rendering. Distances go in the caption (OCT L to R 40 to 100 cm; square 80 to 100 cm behind the OCT; square about 2 m on a side).

Create a 1200 x 1200 pixel PNG with a solid white background (#FFFFFF), square. Make it a photorealistic top down product photograph, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte metal. The front (toward the sound source) is the top of the frame. Near the top center, a generic, unbranded straight microphone bar holds an OCT front array: a small pencil microphone at each end pointing straight outward left and right (supercardioids, each with a translucent green (#1B5E20) narrow front lobe and a small rear lobe beneath it), and at the bar center a very short forward stub holding a third small microphone pointing straight forward with a translucent green heart shaped cardioid lobe. Behind the bar, by a distance about equal to the bar length, begins a much larger square of exactly four identical side address large diaphragm microphones on short stands at the corners, the square about twice as wide as the OCT bar and filling the lower two thirds of the frame. Each of the four is turned so its two open faces point straight left and right, with a translucent blue (#0D47A1) figure eight pattern of two round lobes side by side glowing beneath it. All microphone bodies are matte charcoal (#212121). No text of any kind, no numbers, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 33. Decca Tree of three omni microphones

Now: Three flat green circles on a thin T with text distances; correct but a crude code drawn figure.

```
DAPR 3340 - Spatial Audio I
Image: Decca Tree of three omni microphones
File name: Microphone_Spacing_Distance_Diagram.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Microphone_Spacing_Distance_Diagram.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 1)
Fix: None, same content, richer rendering. Distances go in the caption (L to R 2 m; C 1.5 m forward).

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a photorealistic top down product photograph of a generic, unbranded Decca style microphone tree, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte black metal booms, shallow depth of field at the edges. The front (toward the orchestra) is the top of the frame. A long straight horizontal crossbar spans the lower part of the frame, with one omnidirectional microphone with a rounded ball shaped tip at each end (L and R). From the middle of the crossbar a straight arm reaches forward, about three quarters as long as the L to R span, holding a third identical omni microphone (C) at its tip. All three microphones point forward, toward the top of the frame, with matte charcoal (#212121) bodies. Under each microphone a soft translucent green (#1B5E20) circular pickup disc glows evenly on the white surface to show an omni pattern. No text of any kind, no numbers, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 34. Modified Decca Tree with two rear facing omnis

Now: Five flat green circles with text distances; it does not show that the rear omnis face backward.

```
DAPR 3340 - Spatial Audio I
Image: Modified Decca Tree with two rear facing omnis
File name: Modified_Decca_Tree.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Modified_Decca_Tree.png
Size: 1200 x 1200 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 2)
Fix: None, same content, richer rendering. Distances go in the caption (L to R 2 m; C 1.5 m forward).

Create a 1200 x 1200 pixel PNG with a solid white background (#FFFFFF), square. Make it a photorealistic top down product photograph of a generic, unbranded microphone tree, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte black metal booms. The front (toward the orchestra) is the top of the frame. In the upper half, a classic Decca tree: a long horizontal crossbar with one omnidirectional microphone with a rounded ball tip at each end (L and R), and a forward arm from the crossbar center, about three quarters as long as the L to R span, holding a third omni (C); these three point toward the top of the frame. In the lower half, a straight rear arm runs back from the crossbar center by about half the L to R span to a shorter second crossbar holding two more identical omni microphones, spaced about two thirds of the L to R span apart, both pointing straight toward the bottom of the frame (rear facing). All bodies are matte charcoal (#212121). Under the three front microphones glow soft translucent green (#1B5E20) circular discs; under the two rear microphones glow soft translucent blue (#0D47A1) circular discs. No text of any kind, no numbers, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3340 Image 35. Optimized Cardioid Triangle front array

Now: Three flat cartoon capsules with text distances on thin lines; correct geometry in a code drawn figure.

```
DAPR 3340 - Spatial Audio I
Image: Optimized Cardioid Triangle front array
File name: Spaced_Cardioid_Array_Spacing_Diagram.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Recording/Spaced_Cardioid_Array_Spacing_Diagram.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Using Standard Microphones (Figure 5)
Fix: None, same content, richer rendering. Distances go in the caption (C 8 cm, about 3 in, forward; L to R 40 to 100 cm, about 15 to 40 in).

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), a wide banner (generate wide landscape; it will be cropped to a banner). Make it a photorealistic top down product photograph, camera almost straight overhead with a slight three quarter tilt, soft studio lighting, real matte metal. The front (toward the sound source) is the top of the frame. Across the middle of the white seamless surface lies one long, straight, generic, unbranded microphone bar. At its left end a small pencil microphone points straight left and at its right end an identical microphone points straight right; these are supercardioids, so under each glows a translucent green (#1B5E20) narrow front lobe pointing outward plus a small separate rear lobe pointing back toward the bar center. At the exact middle of the bar a very short stub, only about one tenth of the bar length, holds a third small microphone pointing straight toward the top of the frame, with a translucent green heart shaped cardioid lobe under it. All bodies matte charcoal (#212121). Keep generous white space above and below. No text of any kind, no numbers, no measurement marks, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

### DAPR 3345 Spatial Audio II

#### DAPR 3345 Image 03. Five asset states above a four column task board

Now: Five flat outlined boxes with arrows above four flat gray columns of empty cards, all text driven.

```
DAPR 3345 - Spatial Audio II
Image: Five asset states above a four column task board
File name: Asset_States_and_Task_Board.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Asset_Pipeline__Asset_Tracking_Task_Tracking_and_Source_Control/Asset_States_and_Task_Board.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Asset Pipeline: Asset Tracking and Task Tracking (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram in a gentle three quarter view, soft studio shading and gentle shadows, two tiers. Upper tier: exactly five glossy red (#B71C1C) tiles in a row from left to right, linked by short glowing red arrows pointing right, each tile carrying one small sculpted icon on its top face, in order: a clipboard with a checklist; a studio microphone; a waveform with a pair of scissors trimming its tail; a small node block with a plug, standing for an event in a game; a small mixing fader with a check mark beside it. Lower tier: a physical task board seen at a slight angle, a pale grey (#EEEEEE) panel divided into exactly four columns by thin raised charcoal (#212121) dividers. Blank cards pinned in each column from left to right: three cards, one card, one card, two cards. The cards are plain white with a thin colored top edge and carry no writing. The two tiers are clearly separated by white space. No text of any kind, no numbers, no writing on the cards, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 04. Main line of commits with one branch that splits off and merges back

Now: Flat outlined circles on thin lines with small text labels.

```
DAPR 3345 - Spatial Audio II
Image: Main line of commits with one branch that splits off and merges back
File name: Branch_and_Merge.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Asset_Pipeline__Asset_Tracking_Task_Tracking_and_Source_Control/Branch_and_Merge.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Asset Pipeline: Git and Git LFS in Practice (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram in a gentle three quarter view, like glossy beads threaded on rods, soft studio shading and soft shadows. Along the lower part of the frame runs one straight horizontal charcoal (#212121) rod carrying exactly seven glossy charcoal spheres, evenly spaced from left to right: the main line of commits. From the second sphere, a glossy red (#B71C1C) rod angles up and to the right, levels off above the main line, and carries exactly three glossy red spheres, then angles back down and joins the main line exactly at the sixth charcoal sphere. The branch and main line never cross except at those two joining spheres. A faint glow marks the two joining spheres. Place the single label "main" at the far left end of the charcoal rod, clear of all spheres. No text other than the quoted label "main", no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 05. Tiny pointer in the commit, heavy audio in the LFS store

Now: Flat boxes and arrows from a commit to a pointer file to an LFS store with small waveform strips.

```
DAPR 3345 - Spatial Audio II
Image: Tiny pointer in the commit, heavy audio in the LFS store
File name: Git_LFS_Pointer.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Asset_Pipeline__Asset_Tracking_Task_Tracking_and_Source_Control/Git_LFS_Pointer.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Asset Pipeline: Source Control for Audio (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram in a gentle three quarter view, soft studio shading and gentle shadows, reading left to right. On the left, a small light glossy green (#1B5E20) box stands for the commit; resting on top of it is a single tiny thin white card, like an index card, with a few faint grey lines and no legible writing, the pointer. From that card a thin glowing blue (#0D47A1) thread runs to the right into a large heavy blue storage vault in the middle of the frame, solid and weighty, with a dark front and a few small status lights. From the vault, a second glowing thread leads to the right to a tall stack of six thick heavy slabs, each slab with a glossy blue face showing an embossed audio waveform. Make the size contrast dramatic: the pointer card is tiny and weightless, the audio slabs are massive. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 06. Pull, work, commit, push cycle with a second pull before the push

Now: Four flat outlined boxes on a thin circular arrow with a text note in the center.

```
DAPR 3345 - Spatial Audio II
Image: Pull, work, commit, push cycle with a second pull before the push
File name: Pull_Work_Commit_Push.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Asset_Pipeline__Asset_Tracking_Task_Tracking_and_Source_Control/Pull_Work_Commit_Push.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Asset Pipeline: Working on a Shared Repository (Figure 1)
Fix: None to the content. The center text note "Pull again before you push" is replaced by a small unlabeled pull marker between Commit and Push, so the rule shows in the picture itself.

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram in a gentle three quarter view: a glossy circular track like a raised glass ring lying flat on a white surface, centered in the frame, with glowing red (#B71C1C) chevrons moving clockwise around it. Four glossy tiles sit on the ring at the four compass points. Top: a red tile with a downward arrow falling into a tray icon, labeled "PULL". Right: a red tile with a small pencil and waveform icon, labeled "WORK". Bottom: a red tile with a small stamped seal icon, labeled "COMMIT". Left: a red tile with an upward arrow rising out of a tray icon, labeled "PUSH". On the ring between the bottom tile and the left tile, sitting on the track, add one smaller tile in a lighter red tint (#EF9A9A) carrying the same downward arrow into a tray icon as the top tile but no label, showing a second pull before the push. The order clockwise is: PULL, WORK, COMMIT, small pull, PUSH, back to PULL. Labels are bold white capitals on the tile faces. No text other than the quoted labels "PULL", "WORK", "COMMIT" and "PUSH", no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 07. Three prerequisites converging on Spatial Audio II

Now: Three flat outlined boxes with thin lines converging on a fourth box, all text.

```
DAPR 3345 - Spatial Audio II
Image: Three prerequisites converging on Spatial Audio II
File name: Prerequisite_Path.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Course_Orientation/Prerequisite_Path.png
Size: 1600 x 500 px
Format: PNG, solid white background
Used on: Orientation: Prerequisites (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 500 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram in a gentle three quarter view, soft studio shading and gentle shadows. On the left, three glossy blue (#0D47A1) tiles stacked one above another with small gaps, labeled from top to bottom "DAPR 2300", "DAPR 3340" and "ADVANCED STANDING" in bold white capitals on their faces. From each tile a glowing path runs to the right and all three paths converge into one larger glossy brown orange (#993300) tile on the right, labeled "DAPR 3345" in bold white. The path from the middle tile, "DAPR 3340", is noticeably thicker and brighter than the other two, showing the course this one builds on every week. The paths meet cleanly at the left face of the large tile without crossing each other. No text other than the quoted labels "DAPR 2300", "DAPR 3340", "ADVANCED STANDING" and "DAPR 3345", no other numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 08. FMOD project built into four banks that the game engine loads

Now: Flat outlined boxes from project to build to four banks to the game engine, all text.

```
DAPR 3345 - Spatial Audio II
Image: FMOD project built into four banks that the game engine loads
File name: FMOD_Bank_Build_Flow.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/FMOD__Implementation_in_FMOD_Studio/FMOD_Bank_Build_Flow.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: FMOD: Banks, Building, and Engine Integration (Figure 1)
Fix: None, same content, richer rendering

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram in a gentle three quarter view, soft studio shading and gentle shadows, reading left to right. Far left: a glossy brown orange (#993300) project folder, slightly open, with small waveform tiles peeking out. Next, linked by a glowing arrow: a compact glossy press or forge block with a soft glow at its mouth, standing for the build step. From the press, four glossy cartridge shaped banks fan out in a vertical column, each a rounded block with a label on its face: top "MASTER", largest, solid brown orange, with a small padlock icon showing it stays loaded; second "STRINGS", thinner, in a lighter orange tint (#FFCCBC); third "LEVEL 1" and fourth "LEVEL 2", white with brown orange edges. Thin glowing grey lines run from all four banks to the right into one generic unbranded game console shaped box, matte charcoal (#212121) with a dark front, softly lit. The lines from the two level banks are dashed with light, showing they load and unload. No text other than the quoted labels "MASTER", "STRINGS", "LEVEL 1" and "LEVEL 2", no other numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 09. Game mixer bus tree from Master down to SFX children

Now: Flat outlined boxes in a tree joined by thin grey lines, with a text note under UI.

```
DAPR 3345 - Spatial Audio II
Image: Game mixer bus tree from Master down to SFX children
File name: FMOD_Bus_Structure.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/FMOD__Implementation_in_FMOD_Studio/FMOD_Bus_Structure.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: FMOD: Buses, Snapshots, and the Mixer (Figure 1)
Fix: None, same content, richer rendering. The bus names and the UI reverb note move to the caption.

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram in a gentle three quarter view, a tree read top to bottom, like glossy 3D tiles joined by glowing cables, soft studio shading and gentle shadows. Top center: one large glossy brown orange (#993300) tile carrying a small sculpted bank of master faders. Middle row: exactly five smaller tiles in a row, each linked up to the top tile by its own glowing cable, each with one small sculpted icon, left to right: a music note; a leaf with a wind swirl; a starburst impact; a speech bubble; a cursor arrow over a round button. The first four middle tiles are glossy white with brown orange edges; the fifth tile (the cursor) is a cool pale grey (#ECEFF1), and its cable to the top tile runs on a separate clear path that passes around, not through, a soft translucent reverb cloud floating between the middle row and the top tile, while the other four cables pass through that cloud. Bottom row: exactly three tiles under the starburst tile only, each linked up to it by a cable, with icons left to right: a small generic character silhouette; a globe; a crosshair. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 10. Timeline sheet beside a parameter sheet of crossfading engine loops

Now: Two flat chart panels with axis numbers and text labels, one of time bars and one of overlapping triangles.

```
DAPR 3345 - Spatial Audio II
Image: Timeline sheet beside a parameter sheet of crossfading engine loops
File name: FMOD_Timeline_vs_Parameter_Sheet.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/FMOD__Implementation_in_FMOD_Studio/FMOD_Timeline_vs_Parameter_Sheet.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: FMOD: Events, Instruments, and the Timeline (Figure 1)
Fix: None, same content, richer rendering. Axis values (0 to 4 seconds, 0 to 8000 RPM) and region names move to the caption.

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram, two glossy 3D trays side by side seen from a gentle three quarter angle, soft studio shading and gentle shadows. Left tray, the timeline: a flat tray with a horizontal track and a small clock face without numbers standing at its left end. On the track lie three glossy brown orange (#993300) bars at staggered heights and start points: a short bar at the very start; a medium bar that begins just after the first starts and overlaps it; a long bar that begins about a quarter of the way along and runs past the halfway point. A thin glowing vertical playhead line stands across the tray, sweeping left to right. Right tray, the parameter sheet: a matching tray with four translucent triangular glass fins standing upright in a row, each peaking at a different point along the tray, neighbours overlapping at their bases so they crossfade, tinted from light to dark brown orange (#FFCCBC, #FFAB91, #E64A19, #993300) from left to right. A small generic tachometer dial without numbers stands at the right tray's left end, and a glowing vertical cursor line stands across the fins, set by the dial rather than the clock. No text of any kind, no numbers, no axis labels, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 11. Four stage lifecycle of an audio script

Now: Four flat outlined boxes in a row with arrows and small descriptive text in each.

```
DAPR 3345 - Spatial Audio II
Image: Four stage lifecycle of an audio script
File name: Audio_Script_Lifecycle.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Implementation__Level_Implementation_and_Engine_Scripting/Audio_Script_Lifecycle.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Implementation: Basic Scripting for Audio (Figure 1)
Fix: None, same content, richer rendering. The step names and audio calls move to the caption.

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram in a gentle three quarter view, soft studio shading and gentle shadows: exactly four glossy violet (#4A148C) tiles in a row from left to right, linked by short glowing violet arrows pointing right, each carrying one small sculpted icon on its top face, in this order. Tile one: a play symbol wrapped by a circular loop arrow, with a small tag on a string attached, standing for starting a looping sound and keeping its handle. Tile two: a short strip of film frames with a small rotary dial beside it, standing for reading a game value every frame and setting a parameter. Tile three: a translucent box shaped trigger volume with a small glossy sphere passing into it and a short burst of sound rings at that spot, standing for a one shot at a position. Tile four: a waveform fading down to nothing with the small tag from tile one now cut loose from its string, standing for stopping with a fade and releasing the handle. Make tile four white with a strong violet edge and a gentle glow so it stands out as the step people forget. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 12. Eight silent sound checks in order, stopping at the first failure

Now: Eight flat outlined boxes in two columns with numbers and question text and a thin curved arrow.

```
DAPR 3345 - Spatial Audio II
Image: Eight silent sound checks in order, stopping at the first failure
File name: Silent_Sound_Sequence.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Implementation__Level_Implementation_and_Engine_Scripting/Silent_Sound_Sequence.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Implementation: Debugging and Remote Profiling (Figure 1)
Fix: None, same content, richer rendering. The eight numbered questions move to the caption or page list, in the same order.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a gentle three quarter view, soft studio shading and gentle shadows. Exactly eight glossy tiles in two columns of four, left column first, each carrying one small sculpted icon, in this order. Left column top to bottom: 1) a tripwire lever snapping; 2) two matching tag shapes side by side; 3) a bank cartridge seated in a slot; 4) the same cartridge with a circular refresh arrow around it. Right column top to bottom: 5) a small cube with a location pin above it; 6) a single ear shape on a small cube; 7) a loudspeaker fading into a pale translucent ghost of itself; 8) a mixer fader pulled all the way down beside a mute button. A glowing violet (#4A148C) path runs down the left column from tile 1 to tile 4, then crosses to the top of the right column and runs down it, showing the order. Tiles 1 and 2 are glossy violet with a small green (#1B5E20) check light. Tile 3 glows solid red (#B71C1C) as the first failure, and the glowing path stops at it; tiles 4 to 8 are dimmed pale grey and unlit, since checking stops at the first failure. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 13. Five game buses, each paired with the decision it makes possible

Now: Five flat grey boxes with arrows pointing to lines of text.

```
DAPR 3345 - Spatial Audio II
Image: Five game buses, each paired with the decision it makes possible
File name: Bus_Decisions.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Interactive_Mix__The_Immersive_Interactive_Mix/Bus_Decisions.png
Size: 1600 x 900 px
Format: PNG, solid white background
Used on: Interactive Mix: Bus Structure and Submixing (Figure 1)
Fix: None, same content, richer rendering. The bus names and decisions move to the caption.

Create a 1600 x 900 pixel PNG with a solid white background (#FFFFFF), wide landscape. Make it a richly rendered dimensional diagram in a gentle three quarter view, soft studio shading and gentle shadows. On the left, exactly five glossy charcoal (#212121) tiles stacked in a column with even gaps, each with a small sculpted icon matching the bus: a music note; a leaf with a wind swirl; a starburst impact; a speech bubble; a cursor arrow over a round button. From each tile a short glowing arrow points right to a small sculpted scene showing the decision that bus allows. Music: a fader dipping low beneath a raised speech bubble, next to a small slider. Ambience: a small house shape with a soft low pass filter curve over it and a pair of crossed swords with a fader dipped beside them. SFX: the arrow splits into three small tiles showing a character silhouette, a globe and a crosshair. Voice: a speech bubble lifted on a pedestal above everything else, next to a small slider. UI: a cursor tile whose path curves cleanly around a soft translucent reverb cloud without touching it, with a fader locked in place by a small padlock. Use blue (#0D47A1), green (#1B5E20) and brown orange (#993300) accents on the scenes. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 14. How often a sound plays sets how much variation it earns

Now: A flat four bar chart in green tints with text labels over and under every bar.

```
DAPR 3345 - Spatial Audio II
Image: How often a sound plays sets how much variation it earns
File name: Variation_by_Frequency.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Variation__Nonrepetitive_Design_Strategies/Variation_by_Frequency.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Variation: How Much Variation Is Enough (Figure 1)
Fix: None, same content, richer rendering. The frequency bands and variation strategies move to the caption.

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram in a gentle three quarter view, soft studio shading and gentle shadows: exactly four glossy green columns standing in a row from left to right on a white surface, each taller and darker than the one before, from a pale green tint (#C8E6C9) through mid tints to deep green (#1B5E20). The heights rise roughly as one, two, three and four units. On top of each column sits a small sculpted scene. Column one: a single glossy sound tile. Column two: a short fan of four sound tiles with small pitch and volume dials. Column three: a heap of many sound tiles with a pair of dice resting on them. Column four: a full grid of sound tiles on a small platform with three floor swatches beneath it, stone, wood and grass. In front of each column base, a small sculpted icon for the kind of sound: an open book with a star; a door; a crosshair; a pair of footprints. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

#### DAPR 3345 Image 15. Two authoring hierarchies feeding the bus hierarchy in Wwise

Now: Three flat outlined boxes, two on the left with arrows into one on the right, all text.

```
DAPR 3345 - Spatial Audio II
Image: Two authoring hierarchies feeding the bus hierarchy in Wwise
File name: Wwise_Three_Hierarchies.png
Save to (overwrite): /Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Wwise__Implementation_and_Certification_in_Wwise/Wwise_Three_Hierarchies.png
Size: 1600 x 600 px
Format: PNG, solid white background
Used on: Wwise: The Project Hierarchy (Figure 1)
Fix: None, same content, richer rendering. The hierarchy names move to the caption.

Create a 1600 x 600 pixel PNG with a solid white background (#FFFFFF), wide landscape banner. Make it a richly rendered dimensional diagram in a gentle three quarter view, soft studio shading and gentle shadows. On the left, two low glossy platforms, one above the other. Upper left platform, brown orange (#993300): a small tree of rounded blocks branching downward, each leaf block showing an embossed waveform, standing for sounds and their containers. Lower left platform, violet (#4A148C): a small tree of blocks whose leaves are music segment tiles with embossed note heads and a short loop arrow, standing for interactive music. From the root of each left tree, a glowing cable in that tree's color runs to the right, and the two cables arrive side by side at one larger charcoal (#212121) platform on the right. On the right platform stands a tree of fader modules that branch downward from one master fader at the top, standing for the bus structure where signal is summed; the two incoming cables plug into its lower branches. The cables never cross each other. No text of any kind, no numbers, no logos, no brand marks, no model numbers, no watermark, no signature, no borders, no frames, no title bars, no caption text, no legible software screens (any screen is dark or softly defocused). No real product you could name. No hands or people.
```

# Part 3. Not line drawings, but wrong

These are photos, renders or exact charts, so they are not in Parts 1 and 2. Each one states something false or cannot be read. Say go on any row and Claude handles the ones marked "Claude".

| File (full path) | What is wrong | Fix route |
|---|---|---|
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/MIDI_5_Pin_DIN_Pin_Layout.png` | Pins are drawn in a ring with pin 3 at the top and pins 2 and 5 down by the key. A 5 pin 180 degree DIN has all five pins on one half circle arc, numbered 1, 4, 2, 5, 3 around the arc, with pin 2 in the middle opposite the key. | Real part photo or the MIDI Association pinout drawing; pin numbers go in the caption. Claude can find a licensed source. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Firewire_400_4_Pin.png` | The plug body is the larger 6 pin shape. A 4 pin FireWire plug is a small flat rectangle with a dimple on each side. The label is also baked into the image. | Real photo (Wikimedia Commons has 4 pin and 6 pin FireWire plugs). |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Monitoring__Psychoacoustics/Equal_Loudness.png` | The curves are smooth U shapes. Real equal loudness contours dip around 3 to 4 kHz (the ear's most sensitive region) and flatten as the phon level rises. | Claude redraws it as an exact chart from ISO 226:2003 data (Standards 0, choice 2). |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Gain_Staging/Decibel_Scales_Aligned_at_Nominal.png` | Nominal lines up (+4 dBu, minus 18 dBFS, 0 VU), but the uneven tick spacing puts 0 dBFS opposite +24 dBu. With +4 dBu at minus 18 dBFS, full scale is +22 dBu. | Decision needed (next row), then Claude redraws both to one alignment. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Gain_Staging/Meter_Alignment_Scales.png` | Uses 0 dBFS = +18 dBu, so +4 dBu lands at minus 14 dBFS. The figure above in the same module uses minus 18 dBFS. Both are real standards, but students see two answers in one module. | Tell Claude which alignment the Studio B interface is calibrated to. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Digital_Audio__The_Digital_Domain/Bit_Depth_Ladder.png` | The 32 bit float bar has no value and is drawn only about a third taller than 24 bit. Its theoretical range is about 1,500 dB. | Claude redraws with a broken axis and a label. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Voltage_and_Current/Orders_of_Magnitude.png` | The bars are meant to show orders of magnitude, but their heights grow by far less than ten times per step. No labels. | Claude redraws as an exact chart (log scale, one bar per power of ten). |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Microphones/Proximity_Effect.png` | The 2 in, 6 in and 12 in labels stack at the right edge where the curves merge, so no one can tell which is which. The vertical axis has no unit (dB). | Claude relabels at the left end of each curve. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Microphones__Characteristics_Selection_and_Stereo_Techniques/Mic_Pattern_Polar_Chart_Cardioid_Labeled.png` | The "Most sensitive at the front" leader line runs over the 30 degree label. | Claude nudges the label. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Processing__Compression/Gain_Reduction_Graph_Choice_A.png` | The Threshold label is tiny and sits on the curve. The other quiz choices share the style. | Claude enlarges and moves the label on all four. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Wireless_Systems/Third_Order_Intermodulation.png` | The IM3 products are drawn about half as tall as the carriers, which overstates them. | Optional. Say so in the caption, or regenerate with the IM3 bars much shorter. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__Foundation/Note_on_Note_Off_Timeline.png` | Two colored bars on a rail with no labels, and the right bar is cut off. It does not show a note on and a note off. | Regenerate (Claude can write the prompt). |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/MIDI__MIDI_Evolution_and_Extended_Protocols/OSC_DIN_Beside_Ethernet.jpg` | The black connector shows no pins, so it does not read as a 5 pin DIN. | Real photo of a MIDI DIN beside an RJ45. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Schematics/Opamp_Symbol.jpg` | Shows the op amp equivalent model (Rin, Rout, Gvin), not the plain op amp symbol the name says. | Check the page. If it teaches the symbol, swap in the plain triangle symbol. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2255--Audio_Hardware_I/Switches/Rotary_Switch.jpg` | A low quality top view of a red plastic housing. It does not read as a rotary switch. | Real photo of a rotary switch. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Send_Assignment_Context_Menu_On_Strip.jpg` | Shows the VCA assignment menu, not a send assignment menu. | Recapture in Pro Tools. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Binaural_Renderer_Channel_Strip.png` | So narrow it cannot be read at page size. | Recapture at Retina resolution. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3340--Spatial_Audio_I/Mixing_in_Dolby_Atmos/Pan_Curve_Shape_Icons.png` | A tiny, low resolution strip of icons. | Recapture larger. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Focus_and_Balance/Channel_Strip_Anatomy.png` | A tiny, narrow screenshot. Nothing is legible. | Recapture at Retina resolution. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/Mixing__Focus_and_Balance/Technical_Ear_Trainer_Settings.png` | A Word window covers the Monitor Selection and response controls, and callout 3 points at a blurred box. | Recapture clean. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Launchctl_List_Terminal.png` | A narrow Terminal capture; the text is unreadable. | Recapture wider with a larger font. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Sharing_Permissions.png` | A very narrow capture; the text is unreadable. | Recapture wider. |

Already on the older lists and not repeated here: Talkback_Box_Assembled.jpg, Time_Machine_Restore.jpg, Screenshot_Options_Menu_over_System_Settings.jpg, Terminal_Pwd_Ls_Cd.png, Vocal_EQ_Frequency_Band_Chart.jpg, Compression_Switch.png, Channel_Strip_with_Centered_Pan_Knobs.png (see `Image Fixes For Later - DAPR All Courses.md`).

# Part 4. Capture or source these, do not generate

These are drawings of real gear or real software screens. ChatGPT would invent controls, so each needs a photo, a manual scan or a screenshot. Same file name and path.

| File (full path) | What it needs |
|---|---|
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Operation/ASP4816_Block_Diagram_Full.png` | The block diagram page from the Audient ASP4816 manual, cropped. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Signal_Flow/ASP4816_Block_Diagram.png` | Same manual page, the single channel section. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Signal_Flow/ASP4816_Full_Panel.png` | Photo of the whole Studio B console from above, or the Audient press photo. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Signal_Flow/ASP4816_Strip_Input.png` and `ASP4816_Strip_Input_Classic.png` in the same folder | Close photo of the input section of one channel. The code drawn strips are cut off at the top and bottom. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Signal_Flow/ASP4816_Strip_Equalizers.png` and `ASP4816_Strip_Equalizers_Classic.png` | Close photo of the EQ section. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Signal_Flow/ASP4816_Strip_Auxiliaries.png` and `ASP4816_Strip_Auxiliaries_Classic.png` | Close photo of the six aux sends and cue A and B. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Signal_Flow/ASP4816_Strip_Routing.png` and `ASP4816_Strip_Routing_Classic.png` | Close photo of the routing buttons. The Classic version is gray on gray and unreadable. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Signal_Flow/ASP4816_Strip_Short_Fader.png` and `ASP4816_Strip_Short_Fader_Classic.png` | Close photo of the short fader section. The drawing shows 6 strips where the others show 7, and its top labels are clipped. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Console_Signal_Flow/ASP4816_Strip_Long_Fader.png` and `ASP4816_Strip_Long_Fader_Classic.png` | Close photo of the long faders. The drawn fader scale is cut off below 5. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Session_Delivery_and_Archiving/Session_Folder.png` (also used from `The_Digital_Recording_Process/`) | A real Finder screenshot of a session folder. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Dark_Toolbar_with_Labeled_Capture_Buttons.png` | Screenshot of the macOS capture toolbar (Shift Command 5). |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2020--Core_Mixing/macOS__Foundations/Privacy_Security_Pane.png` | Screenshot of System Settings, Privacy & Security. The current file is a mockup marked "(illustrative)". |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Software_Tools/Dante_Routing_Grid_Concept.png` | Screenshot of the Dante Controller routing grid. |
| `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Studio_Use_and_Care/Studio_Floor_Plan.png` | Already parked: send room names and a rough layout, and Claude writes the prompt. |

# Part 5. Files pages already link that do not exist yet (27)

These pages show a broken image right now.

DAPR 2000 Spring 2027 template v1 (18 files). Their prompts are already written, in the "Image briefs" section of:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/Miscellaneous/4-Work/UVU/UVU Courses/DAPR 2000 - Digital Audio Essentials/Claude outputs/Notes and Briefs/2026-09-25 DAPR 2000 Spring 2027 Template v1 Overnight Build Notes.md
```

Folders `Studio__The_Recording_Studio_and_Control_Room`: Studio_Floor_Plan.png, Module_Banner.jpg, Tracking_Session_Live_Room.jpg, Monitor_Controller_Desk.jpg. `Acoustics__Rooms_and_Sound_Control`: Module_Banner.jpg, Room_Reflection_Paths.png, Treated_Room_Corner.jpg, Decoupled_Wall_Section.png. `DAW__Editing_and_Comping`: Module_Banner.jpg, Multitrack_Edit_Alignment.png, Crossfade_Overlap.png, Comp_From_Takes.png. `Processing__Gates_and_Expanders`: Module_Banner.jpg, Gate_Envelope.png, Snare_And_Hi_Hat_Bleed.jpg, Expander_Transfer_Curve.png. `Project__Edit_and_Comp`: Edit_and_Comp_Desk.jpg. `Course_Orientation`: Spring_Term_Timeline.png (exact dates, so Claude draws this one as a chart).

DAPR 3340 v57 (9 files), already in `ChatGPT Image Prompts - ALL COURSES TO DO.md` or `Image Fixes For Later - DAPR All Courses.md`: Channel_Strip_With_Binaural_Insert.png, Ambisonics_Basics.png, Exercise_Post.png, Using_Surround_Microphones.gif (GIF is not allowed; needs a new PNG name and a relink), Introduction_to_Surround_Recording.png, Room_Design_and_Acoustics.png, Exercise_Music.png, Exercise_Music.jpg, Pro_Limiter_Plugin_Window.png.

Also found: one cartridge links `All/DAPR_Canvas_Icon_Reference/Callout_Note.png&quot;` with an escaped quote stuck to the end of the file name. That is an HTML bug, not a missing image. Claude can find and fix the page.

# Part 6. Page text to update once the new images land

The new images follow the fix. These captions and alt texts then need to match.

| Course | File | Change |
|---|---|---|
| ALL COURSES | SI_Prefix_Ladder.png | Caption: typical mic cable is about 30 pF per foot, not 100. |
| DAPR 2000 | Mix_Arc.png | Three pages describe a song energy arc and one (Mix 2 Revision) describes the Mix 1A, 1B, 2 sequence. Only overwrite the copy the energy arc pages use. The Mix 2 page keeps its own file. |
| DAPR 2000 | Microphones Module_Banner.png | Alt says three patterns; the banner showed six. Match the alt to the new image. |
| DAPR 2000 | Game_Audio_Pipeline.png | Role wording: implementation usually happens inside the middleware. Check the caption. |
| DAPR 2010 | Drum_Kit_Panels_with_Overhead_Options.png | Alt says two overhead placements; there are three panels. |
| DAPR 2010 | Perspective_Kit_with_Numbered_Blue_Markers.png | The caption says "numbered" and overheads first, but the old numbers put kick and snare first. The new image shows the order as three color tiers. Update the caption and the table order. |
| DAPR 2010 | Speaker_Cone_with_Numbered_Blue_Callouts.png | Alt says four mic positions; the image shows three. |
| DAPR 2010 | Array_Panels_with_Drawn_Microphones.png | Caption says two spaced arrays; the image has three (AB, ORTF, NOS). The new prompt uses omnis for AB. |
| DAPR 2020 | Grade_Breakdown.png | Confirm the real weights from the syllabus before generating. The old bars were nearly equal. |
| DAPR 3255 | Layer_Bars_With_Protocol_Pills.png | AES50 moves to Layer 1. The caption should name the six Layer 3 protocols (Dante, AES67, Ravenna, Livewire+, SMPTE ST 2110, NDI). |
| DAPR 3340 | Multiband_Crossover_Bands.png | Alt says three bands; the image shows four. |
| DAPR 3340 | Ambisonics_Nine_Zero_Four_Speaker_Layout.png | Alt says full sphere; 9.0.4 is the upper hemisphere only. |
| DAPR 3340 | Cardioid_Array_With_Labeled_Distances.png | The Figure 14 caption has a stray "Fukada Tree" line that belongs to Figure 15. |
| DAPR 3340 | Post_Production_Mix_Workflow_Chart.jpg | The film delivery list includes DTS HD 7.1, which is a home disc format. |
| DAPR 3345 | Credit_Hour_Rule.png | The update needs five labels, one over the four label limit. Either accept it or move the lab panel's words to the caption. |

# Part 7. Left alone on purpose

- Code drawn exact charts and schematics (EQ and filter curves, polar plots, transfer curves, envelopes, term Gantt charts, circuit schematics, pin order charts) were checked and left as they are unless listed in Part 3. Exact values matter there, and ChatGPT would bend them.
- Real photos, manufacturer images, screenshots and earlier ChatGPT renders passed unless listed above.
- 94 more code drawn line drawings sit in the repo but no current page links them. They were not briefed. Claude can list them for cleanup.
- Cleanup: `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2000--Digital_Audio_Essentials/Sound__Wave_Properties_Hearing_and_Frequency/Photo_Hero_Utah_Valley_Dawn (Adam Olson's conflicted copy 2026-09-23).jpg` is a Dropbox conflicted copy. No page uses it.
- Leave as they are, per earlier decisions: Common_Audio_Meters.png, Legacy_Dolby_Hardware_Milestones.png, Dolby_Pro_Logic_History_Overview.png.
