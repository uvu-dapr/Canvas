# DAPR 2010 Image Brief - v12 Corrections
Generated 2026-09-22. Run each prompt separately in ChatGPT. Save each result
with the exact filename shown, into the exact folder shown. Do not rename.

Written against `DAPR-2010-Course-Turnkey-v12.imscc`. All 54 figures the cartridge
references were opened and looked at, composited on white first per 20.4b. Nothing
below was judged from a filename or from alt text.

House style for this brief, per 20.5 and 20.5a:

| Rule | Value |
|---|---|
| Style | Photorealistic, unless the field table says dimensional diagram |
| Text inside the image | **None.** The page carries the heading, the caption and the prose |
| Palette for diagrams | `#212121` body dark, `#1B5E20` green, `#0D47A1` blue, `#B71C1C` red, `#993300` orange |
| Photorealistic format | JPEG, quality 88, its own background |
| Diagram format | PNG-24, transparent background |
| Never generated | Real hardware panels, real software windows, named products, silkscreen, model numbers (20.1 rule 3) |

---

## Image 01 - Punch and playlists, the misspelling fix

| Field | Value |
|---|---|
| Filename | `tracking-punch-and-playlists-03.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/tracking/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2010--Core_Recording/Pro_Tools_for_Tracking/Punch_and_Playlists.png` |
| Used on | Canvas page `tracking-read-02` |
| Alt text | `Four take lanes with a punch range replacing part of the top lane while the lower lanes stay intact` |
| Caption | `Figure 2. The punch replaces audio only inside the range, and only on the active playlist.` |
| Why | The shipping `-02` prints "Kept, not ovewrritten" three times. 20.5 says never accept a misspelled label. Fixed here by removing the labels entirely |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, viewed slightly from above at a three quarter
angle, with soft depth and drop-free solid color fills.

Four horizontal audio take lanes stacked vertically, evenly spaced, each lane a long
rounded rectangular slab with visible thickness so it reads as a solid object rather
than a flat outline. Each lane is filled with a dense audio waveform drawn as a
symmetric envelope about the lane center line, so every lane clearly contains audio.

The top lane is the active one. Make it visually forward: slightly larger, brighter,
and sitting above the plane of the other three. Fill its waveform in dark green
#1B5E20.

Inside the top lane only, a rectangular region spanning about one quarter of the lane
width, positioned left of center, is filled in red #B71C1C instead of green, and its
waveform inside that region is visibly different in shape from the green waveform on
either side. Two thin vertical red #B71C1C planes stand at the left and right edges of
that region, rising above and below the lane, marking where the region starts and ends.

The three lower lanes are receded, slightly dimmer, and filled in blue #0D47A1. Their
waveforms run unbroken from end to end with no red region and no gap anywhere.

Reading direction is left to right for time, and top to bottom for lane order.

No text anywhere in the image. No numbers, no letters, no labels, no ruler markings,
no tick marks. No logo, brand mark, model number, or software interface. No borders,
frames, title bars, or caption text. No people, no watermark, no signature.
```

---

## Image 02 - Phase against polarity, the constant offset fix

| Field | Value |
|---|---|
| Filename | `miking-techniques-phase-versus-polarity-03.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 800 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/miking-techniques/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2010--Core_Recording/Miking_Techniques/Phase_versus_Polarity.png` |
| Used on | Canvas page `miking-techniques-read-02` |
| Alt text | `Left, two identical waves offset by a constant delay. Right, two waves that are exact mirror images` |
| Caption | `Figure 1. Phase is the same wave arriving later. Polarity is the same wave turned upside down. Left panel, phase. Right panel, polarity.` |
| Why | Measured on the shipping `-02`: in the phase panel the two waves have different periods, so the peak offset runs 0, 9, 11, 21, 21, 31, 25 pixels across the frame. The first peaks coincide exactly, so at the left edge there is no delay at all, which contradicts the panel |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 800 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram. Two panels of equal width side by side,
separated by a single thin vertical divider in gray. Solid color fills, soft depth,
no gradients across the whole frame.

LEFT PANEL. Two smooth continuous sine waves stacked one above the other, each drawn
as a thick rounded tube with visible thickness. The upper wave is blue #0D47A1. The
lower wave is dark green #1B5E20.

CRITICAL for the left panel: the two waves must have EXACTLY the same period and
EXACTLY the same amplitude. Count the cycles: both waves show exactly four complete
cycles across the panel. The lower green wave is shifted to the right relative to the
blue wave by a constant amount equal to about one fifth of one cycle, and that shift
is IDENTICAL at every peak across the whole panel. Measure the horizontal distance
from the first blue peak to the first green peak, then from the fourth blue peak to
the fourth green peak. Those two distances must be the same. The waves must never
drift closer together or further apart from left to right.

RIGHT PANEL. Two smooth continuous sine waves stacked one above the other, same tube
rendering. The upper wave is blue #0D47A1. The lower wave is red #B71C1C.

CRITICAL for the right panel: the two waves are exact mirror images about a horizontal
axis. Every peak of the blue wave sits at the same horizontal position as a trough of
the red wave, and every trough of the blue wave sits at the same horizontal position
as a peak of the red wave. There is no horizontal shift at all between them. Both show
exactly four complete cycles.

Reading direction is left to right for time.

No text anywhere in the image. No numbers, no letters, no labels, no axis marks, no
arrows, no callouts, no dashed measuring lines. No borders, frames, title bars, or
caption text. No watermark, no signature.
```

---

## Image 03 - Headroom and noise floor, the clipping band fix

| Field | Value |
|---|---|
| Filename | `gain-staging-headroom-noise-floor-03.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/gain-staging/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2010--Core_Recording/Gain_Staging/Headroom_Noise_Floor.png` |
| Used on | Canvas page `gain-staging-read-01` |
| Alt text | `A vertical level scale with a thin clipping band at the top, a wide usable range below it, and a noise floor at the bottom` |
| Caption | `Figure 2. Headroom is the room between nominal and the clipping band. It is not the clipping band itself.` |
| Why | On the shipping `-02` the red band labeled Clipping is the same band the Headroom arrow spans, so the picture says headroom equals the clip zone. Flagged on 2026-09-20 and never corrected |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram. One tall vertical bar standing upright in the
center of the frame, drawn at a slight three quarter angle so it reads as a solid
column with real thickness and a visible top face, like an architectural model rather
than a flat rectangle.

The column is divided top to bottom into four stacked bands of very different heights:

1. TOP band, red #B71C1C. This band is THIN, occupying only about the top one twelfth
of the column height. It is the clipping region. It must be obviously the shortest
band in the column.

2. SECOND band, plain light gray, occupying about one quarter of the column height.
This is the headroom region and it is clearly a different color from the red band
above it. A blue #0D47A1 dimensional arrow with arrowheads at both ends stands beside
the column, spanning exactly this gray band, from the line where it meets the red band
down to the line where it meets the band below. The arrow must not extend into the red
band at any point.

3. THIRD band, dark green #1B5E20, occupying about half the column height. This is the
usable range and it is the tallest band.

4. BOTTOM band, dark gray, occupying about one eighth of the column height. This is
the noise floor.

A thin horizontal orange #993300 plane cuts across the column exactly where the gray
headroom band meets the green usable band, extending a little beyond the column on
both sides. This marks nominal level.

Reading direction is top to bottom, loudest to quietest.

No text anywhere in the image. No numbers, no letters, no decibel values, no labels,
no scale markings, no tick marks. No borders, frames, title bars, or caption text. No
watermark, no signature.
```

---

## Image 04 - Session roles, the assistant size fix

| Field | Value |
|---|---|
| Filename | `studio-etiquette-session-roles-03.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 800 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/studio-etiquette/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2010--Core_Recording/Studio_Etiquette/Session_Roles.png` |
| Used on | Canvas page `studio-etiquette-read-02` |
| Alt text | `Five equal role blocks arranged in a ring around a central session block, all the same size` |
| Caption | `Figure 1. Client, producer, artist, engineer, assistant. Five roles, five jobs, one session. No role here is smaller than another.` |
| Why | Two defects on the shipping `-02`, both flagged on 2026-09-20 and still present. The boxes taper top to bottom, so ASSISTANT renders at about half the type size of CLIENT, in a course whose whole point is training the assistant. And the artist or talent role is missing entirely. The purple fill is also off palette (3) |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 800 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, viewed at a three quarter angle from slightly
above. Solid color fills, soft depth, real thickness on every block.

One hexagonal slab sits at the center of the composition in dark charcoal #212121.

Five identical hexagonal slabs are arranged evenly around it, one at each of five
positions on a circle, each one touching the central slab edge to edge so the six
together read as a single honeycomb with no gaps between the pieces.

CRITICAL: all five outer slabs are EXACTLY the same size as each other, exactly the
same thickness, and exactly the same height above the ground plane. Not one of them is
larger, smaller, taller, shorter, closer or further away than the others. Measure them.
If any one of the five is a different size from the other four, redraw it.

Fill the five outer slabs in these five colors, one each, in order going clockwise from
the top: dark green #1B5E20, blue #0D47A1, red #B71C1C, orange #993300, dark green
#1B5E20 again.

A thin ring of gray connecting bars runs between adjacent outer slabs, so the five are
visibly joined to one another as well as to the center.

Reading direction is a ring, with no beginning and no end. Nothing in the composition
may suggest a top to bottom ladder or a hierarchy.

No text anywhere in the image. No numbers, no letters, no labels, no icons of people,
no job titles. No borders, frames, title bars, or caption text. No people, no
watermark, no signature.
```

---

## Image 05 - Speaker cone positions

| Field | Value |
|---|---|
| Filename | `guitar-bass-speaker-cone-positions-02.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/guitar-bass/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2010--Core_Recording/Images/guitar-bass/guitar-bass-speaker-cone-positions-02.jpg` |
| Used on | Canvas page `guitar-bass-read-01` |
| Alt text | `A guitar speaker seen face on with four colored markers running from the dust cap out to the cone edge` |
| Caption | `Figure 2. Four positions, dust cap to cone edge. Red is brightest, blue is balanced, green is warmest, orange is the off axis position.` |
| Why | The shipping `-01` has four leader lines converging into a tangle, two of them crossing, two labels printed on top of the cone outline, one marker drawn as a star while the others are triangles, and the right 40 percent of the frame empty. The content is right, the drawing is unusable |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft even lighting from above and slightly to the
left, shallow depth of field so the cone surface falls off gently toward the edges of
the frame, on a clean seamless dark gray background.

A single generic 12 inch guitar loudspeaker, seen straight on, face toward the camera,
filling most of the frame. Real paper cone texture with visible fiber, a fabric dust
cap at the center, a ribbed surround at the outer edge, and a stamped steel basket. The
speaker is anonymous: plain black basket, plain unbranded cone, no gasket printing.

Four small solid colored spheres rest on the cone surface, evenly spaced along one
straight radius that runs from the center of the dust cap out to the edge of the cone,
all four on the same side of the speaker. They are small, about one twelfth of the cone
diameter each, and they cast a soft contact shadow on the cone so they read as objects
sitting on it.

From the dust cap outward, the four spheres are: red #B71C1C directly on the dust cap,
blue #0D47A1 about a third of the way out, dark green #1B5E20 about two thirds of the
way out, orange #993300 at the outer edge of the cone just inside the surround.

Reading direction is center to edge along that one radius.

No text anywhere in the image. No numbers, no letters, no labels, no leader lines, no
arrows, no callouts, no measurement marks. No logo, brand mark, model number, or
printed cone legend. No microphones, no stands, no cables, no amplifier cabinet. No
borders, frames, or caption text. No hands, no people, no watermark, no signature.
```

---

## Image 06 - Course card

| Field | Value |
|---|---|
| Filename | `course-orientation-course-card-02.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/course-orientation/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2010--Core_Recording/Images/course-orientation/course-orientation-course-card-02.jpg` |
| Used on | Canvas page `orientation-1b-outcomes` |
| Alt text | `A professional recording studio control room seen from behind the console toward the live room glass` |
| Caption | `Figure 1. Core Recording. This is the room you are learning to work in.` |
| Why | The shipping `-01` is the thin sparse line art that 20.5a was written to remove: two gray squares for monitors, a stick figure for a person, and a gray trapezoid for a console. It carries the course title baked into the image, which 20.5 prohibits |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic architectural interior photograph. Warm practical lighting from
recessed ceiling fixtures and the glow of the console meters, long exposure so the
room is evenly lit, shallow depth of field with the console surface sharp and the far
wall softly out of focus.

A professional recording studio control room, photographed from just behind and above
the engineer position, looking forward. In the near foreground, the rear third of a
large analog mixing console: rows of faders, knobs and small illuminated buttons, real
brushed metal and matte plastic surfaces, dust and fingerprints visible on the armrest.
A pair of large nearfield monitors sits on stands beyond the console, angled inward
toward the engineer position.

Beyond the monitors, a wide window of studio glass looks through into a live room where
a drum kit and two microphone stands are visible, softly out of focus.

The side walls carry real acoustic treatment: fabric wrapped broadband absorber panels
and a wooden slat diffuser. There is a rack of outboard gear to one side, its front
panels dark with small status lights.

The console, the monitors, the outboard and the microphones are all anonymous: no
visible brand marks, no product names, no model numbers, no silkscreen legends readable
at any size.

Reading direction is foreground to background, engineer position toward the live room.

No text anywhere in the image. No numbers, no letters, no labels, no course title. No
logo, brand mark, model number, or readable silkscreen on any panel. No borders,
frames, title bars, or caption text. No people, no watermark, no signature.
```

---

## Image 07 - Drum microphone placement

| Field | Value |
|---|---|
| Filename | `drums-microphone-placement-02.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 1200 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/drums/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2010--Core_Recording/Images/drums/drums-microphone-placement-02.jpg` |
| Used on | Canvas page `drums-read-02` |
| Alt text | `A five piece drum kit miked up, seen from above and slightly behind the drummer position` |
| Caption | `Figure 2. A full kit miked up. Kick in, snare top, hi-hat, each tom, two overheads, one room mic back in the corner.` |
| Why | The shipping `-01` is a flat overhead outline that cannot show what it claims. It marks Snare top and Snare bottom as two different spots on the same overhead circle, which in a plan view is meaningless. The Room mic marker floats at the far right with no spatial relation to the kit, there is an unlabeled tom with no mic on it, and one overhead leader line passes through the rack tom |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 1200 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft even overhead lighting with a warm fill from
the left, moderate depth of field so the whole kit stays readable, shot from a high
three quarter angle above and behind the drummer position looking down and forward
across the kit, on a wooden studio floor with a treated wall behind.

A five piece drum kit fully miked for a session: kick drum, snare, two rack toms, one
floor tom, hi-hat, one crash and one ride cymbal. Real lacquered wood shells, real
coated drum heads with visible stick marks, chrome hardware with fingerprints, felt
washers on the cymbal stands.

Microphones on stands in these positions, each clearly a different distance and angle
so the arrangement reads as deliberate rather than crowded:

One small microphone inside the kick drum port, its stand low and short.
One microphone above the snare drum, angled down across the head away from the hi-hat.
One microphone under the snare drum, pointing up at the bottom head, visible through
the gap in the stand.
One microphone above the hi-hat, angled down at the edge of the top cymbal.
One microphone above each tom, angled down at each head.
Two identical microphones on tall boom stands high above the kit, spaced apart and
both aimed down toward the snare.
One large microphone on a tall stand well back from the kit, near the far corner of
the room, clearly further away than everything else.

Every microphone, stand, drum and cymbal is anonymous: no visible brand marks, no
product names, no model numbers, no readable grille badges.

Reading direction is from the drummer position outward across the kit.

No text anywhere in the image. No numbers, no letters, no labels, no leader lines, no
arrows, no callouts, no measurement marks. No logo, brand mark, or model number on any
drum, cymbal, microphone or stand. No borders, frames, or caption text. No drummer, no
hands, no people, no watermark, no signature.
```

---

## Image 08 - Early reflections

| Field | Value |
|---|---|
| Filename | `acoustics-early-reflections-02.png` |
| Format | PNG-24, transparent background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/acoustics/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2010--Core_Recording/_unplaced/Acoustics/Room_Paths_with_Arrival_Time_Graph.png` |
| Used on | Canvas page `acoustics-read-01` |
| Alt text | `A control room seen from above with the direct path from each monitor to the listener and the first reflection off each side wall` |
| Caption | `Figure 1. The direct sound in green, the first side wall reflection in red. The red path is longer, so it arrives later, and that is what smears the image.` |
| Why | The shipping `-01` prints Direct sound across the green path so the label sits on the line, and the bottom 40 percent of the frame is empty. The content is right. The layout wastes almost half the figure |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel PNG with a fully transparent background.

A richly rendered dimensional diagram, isometric, viewed from above and in front at
about thirty degrees, with real depth and solid color fills. Nothing flat or wireframe.

A rectangular control room drawn as a floor slab with three low walls standing up along
the back and both sides, so the room reads as an open topped box seen from above. The
floor is light warm gray. The walls have visible thickness.

Two loudspeaker cabinets sit on the floor near the back wall, angled inward toward a
point at the front center of the room. A small solid sphere sits at that point,
representing the listening position. The three together form a clear triangle that
fills the width of the room.

From each loudspeaker, one thick dark green #1B5E20 tube runs straight to the sphere.
These are the direct paths. They are the shortest routes.

From each loudspeaker, one thick red #B71C1C tube runs outward to a point on the
nearer side wall, and from that point continues to the sphere. Each red path bounces
exactly once, at one point on one wall, and the angle leaving the wall visibly mirrors
the angle arriving at it. Mark each bounce point with a small flat red #B71C1C square
lying against the wall surface.

CRITICAL: each red two segment path must be visibly LONGER than the green path from the
same loudspeaker. The difference in length should be obvious at a glance.

The room outline fills the frame edge to edge with only a small even margin on all four
sides. There is no large empty band anywhere in the composition.

Reading direction is loudspeaker to listener.

No text anywhere in the image. No numbers, no letters, no labels, no arrows, no
callouts, no dimension lines. No borders, frames, title bars, or caption text. No
people, no watermark, no signature.
```

---

## Image 09 - Vocal microphone and pop filter geometry

| Field | Value |
|---|---|
| Filename | `vocals-pop-filter-distance-01.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 900 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-2010--Core_Recording/Images/vocals/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-2010--Core_Recording/Images/vocals/vocals-pop-filter-distance-01.jpg` |
| Used on | Canvas page `vocals-read-01` |
| Alt text | `A vocal microphone on a stand with a pop filter set between it and the singer position, seen from the side` |
| Caption | `Figure 2. About 3 to 4 inches from the singer to the filter, and the same again from the filter to the capsule. The filter sits halfway, not against the grille.` |
| Why | This is the half of `vocals-recording-chain-01` that is genuinely visual. That file also carries a box and arrow signal chain in which COMPRESSOR overflows its box on both sides. Per 8.1 the chain belongs in page prose, not in a picture, so it is being removed from the figure rather than regenerated. See the page edits section of the cover note |

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 900 pixel JPEG at quality 88.

Photorealistic studio photograph. Soft key light from the upper left with a gentle fill
from the right, shallow depth of field with the microphone capsule and the pop filter
mesh both sharp, on a clean seamless dark background with a hint of acoustic panel
texture far behind.

Seen from the side, in profile, filling the frame left to right: a large diaphragm
studio condenser microphone hanging in an elastic shockmount on a heavy boom stand,
positioned on the right of the frame with the capsule facing left.

In front of it, a circular fabric mesh pop filter on its own gooseneck clamp, standing
vertically, its face parallel to the microphone grille.

On the left of the frame, a foam windshield of the kind a vocalist stands behind,
mounted on a short stand at the same height as the microphone, standing in for the
singer position.

CRITICAL geometry: the gap between the singer position on the left and the pop filter
in the middle must be the SAME distance as the gap between the pop filter and the
microphone capsule on the right. Measure both gaps. They are equal. The pop filter sits
exactly halfway between the two, not pressed against the microphone grille and not
pressed against the singer position.

All three items are anonymous: plain matte black and brushed metal, no visible brand
marks, no product names, no model numbers, no badges.

Reading direction is left to right, singer toward microphone.

No text anywhere in the image. No numbers, no letters, no labels, no arrows, no
dimension lines, no measurement callouts. No logo, brand mark, or model number on the
microphone, the shockmount, the filter or the stands. No borders, frames, or caption
text. No singer, no hands, no people, no watermark, no signature.
```

---

# Not a ChatGPT job

20.1 rule 3 governs the subject, not the style. Anything below is either a real panel,
a real software window, a real room, or a list that should not be a picture at all.

## Adam captures or supplies these

| Item | What is needed | Why |
|---|---|---|
| `digital-recording-pro-tools-playback-engine-01.png` | A real screenshot of the Playback Engine dialog on a studio machine | The shipping file is a very convincing drawn imitation. It has no Cancel button, and it carries a caption baked into the image |
| `tracking-pro-tools-record-arm-controls-01.png` | A real screenshot of a record armed mono track at medium height | The shipping file is a page lifted from the Avid reference guide. Two leader lines are cut off at the left edge and point at nothing, and TrackInput Monitor is missing a space |
| `tracking-pro-tools-edit-window-01.png` | A real screenshot of your own Edit window | Also a lifted reference guide page. Every callout carries a cross reference such as "(page 675)" to a manual students do not have, and the interface is several Pro Tools versions old |
| `tracking-pro-tools-mix-window-01.png` | A real screenshot of your own Mix window | Same class as above. Same page references, same old interface, plus a caption baked in |
| `studio-care-studio-floor-plan-01.png` | Studio A and B layout, a phone photo of a sketch or just the wall dimensions | The shipping file is four empty boxes with no console, no monitors, no doors and no scale. There is a stray unterminated diagonal in Studio B, two unlabeled rooms, and the Studio B Control Room label floats outside its own room |
| `patch-bays-studio-b-bay-map-01.png` | The higher resolution original of the bay map, or the source document | The content is genuine and correct. At 1069 by 670 the smallest labels are about 5 px cap height and unreadable. This needs the original, not a regeneration |

## I do these from the manual

Source for all of them is `Instructor Stuff/Manuals/Audient_ASP-4816_Console.pdf`.

| Item | What is wrong now |
|---|---|
| `console-signal-flow-asp4816-strip-input-01.png` | Still 1006 by 2350. Every other strip section was re-cropped to landscape on 2026-09-22 and this one was missed, so it renders about 2100 px tall on the page |
| `console-signal-flow-asp4816-strip-equalizers-02.png` | My crop cuts through the LMF knob row at the bottom edge |
| `console-signal-flow-asp4816-strip-auxiliaries-02.png` | My crop cuts through the bottom SF button row |
| `console-signal-flow-asp4816-strip-long-fader-02.png` | My crop slices the fader caps in half and loses the whole lower half of the scale. On a figure whose subject is the long fader, the fader is the part that got cut |
| `console-signal-flow-asp4816-strip-short-fader-02.png` | Top edge clips a knob. Least bad of the five |
| All five above | Seven identical channel strips side by side. One or two at larger scale would teach the same thing and read better |
| `console-signal-flow-asp4816-full-panel-01.png` | Still the full desk squeezed into 1600 px. Every legend is about 2 px tall and the whole thing reads as gray texture. Flagged 2026-09-20, never cropped |
| `console-operation-asp4816-connector-panel-01.png` | Now landscape at 1600 by 548, but the port labels are still too small to read. Needs splitting into two or three zoomed crops, which is what the 2026-09-20 audit asked for |

## These should stop being pictures

8.1 says an image with no reason to exist does not get briefed. Each of these is a
two column list rendered as a graphic, so it belongs in an HTML table on the page.

| Item | Replace with |
|---|---|
| `microphones-spec-sheet-anatomy-02.png` | A table of the six spec lines with real values and units. The figure also carries a substance error flagged on 2026-09-20 and never fixed: "Output impedance: what it needs to be plugged into" describes the preamp input impedance, not the microphone output impedance |
| `studio-business-cost-breakdown-01.png` | A two column table, one time against every month. The picture has no visual content at all |
| `studio-business-rate-structures-01.png` | A table, or keep the bar idea only if the three rows get labeled. As it stands there is nothing saying what the three bars are, and the purple fill is off palette |

## Stop sending these two to ChatGPT

| Item | Why |
|---|---|
| `microphones-polar-patterns` | Three generations now. `-01` was a valentine heart, `-03` brought the rear cusp back and also detached the super and hyper rear lobes and drew the hypercardioid rear lobe nearly as large as the front, which makes it a figure of eight. `-02` is correct: decibel radius on a 30 dB grid, rear lobes joined at the null, nulls at 126, 109 and 90 degrees. Keep `-02` |
| `miking-techniques-three-to-one-rule` | `-03` dropped the title and the caption and left the top third empty. `-02` is the better of the two. Keep `-02` |

## Fix on the page, not in the image

| Item | Page edit |
|---|---|
| `microphones-proximity-effect-02.png` | The curves are accurate and the distances are in inches, which is right. There are no axis units on either axis. Rather than regenerate a graph, which is exactly the text heavy subject that 20.5 says fails, put the axis units and the directional pattern caveat in the caption: frequency in hertz across, decibels up, and this applies to directional patterns only, never to an omni |
| `microphones-transducer-types-02.png` | Good figure. The dynamic panel labels its magnet and the ribbon panel does not label its two. Say so in the caption rather than regenerating |
| `console-operation-troubleshooting-order-02.png` | The decision diamonds still have no YES and NO on the branches, so the right branch to "Fix the source" could be read either way. Add the branch words to the caption, or accept a regeneration knowing it needs twelve labels and will probably come back with a text defect |
| `miking-techniques-spaced-arrays-02.png` | Correct figure. ORTF 17 cm and 110 degrees, NOS 30 cm and 90 degrees, both right. It gives centimeters with no inches, and your standard wants US units present. Put 6.7 in and 11.8 in in the caption |
| `impedance-five-connection-cases-01.png` | Correct figure. The NEEDS A BOX chip is white text on yellow, which fails contrast under 2. All five verdicts are NEEDS A BOX or WRONG, so a student never sees a case that is simply fine. Either regenerate with dark text on the chips, or note in the prose that case 1 is fine once the box is in the path |
