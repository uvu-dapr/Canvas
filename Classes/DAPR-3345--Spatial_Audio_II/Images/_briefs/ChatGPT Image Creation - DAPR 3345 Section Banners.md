# DAPR 3345 Image Brief - Section Banners
Generated 2026-09-22, revision 2. Run each prompt separately in ChatGPT. Save each result
with the exact filename shown, into the exact folder shown. Do not rename.

---

## What changed in revision 2

Revision 1 was wrong in one way that matters and one that is easy to fix.

**Dimensions.** §20.3 sets a Canvas page figure at **1600 px wide**, and I wrote 1942. The four
images you already generated are 1942 x 809 because my brief said so. Every prompt below is
now **1600 x 667**, which holds the same 2.4:1 banner shape at the standard width. See
"The width problem" at the end: all twenty images in the repo are currently off this, not
just the new four, and there is a one-command fix.

**One violation I missed in the existing set.** `interactive-audio-workstation-banner.jpg`
shows a fabricated DAW timeline on one monitor and a fabricated engine viewport on the
other. §20.1 rule 3 names "DAW windows" specifically. I passed that image in the audit on
22 September and I should not have. It is now on the capture list.

---

## Verdict on the four you generated

| Image | Verdict |
|---|---|
| `dolby-certification-atmos-room-banner-01.jpg` | **Ship it.** Three fronts, two sides, four ceiling speakers angled down, no brand marks, no text. The overhead layer is unmistakable, which was the whole job. |
| `variation-randomization-dimensions-banner-01.jpg` | **Ship it.** Eight identical cubes, eight different forms. Reads instantly. Best of the four, and it sits beside the layered-recombination image as a matched pair. |
| `spatial-recording-concert-hall-rig-banner-01.jpg` | **One substance question.** See Image 01 below. |
| `final-project-playable-build-banner-01.jpg` | **Works, but it is very dark.** See Image 02 below. Your call. |

---

## Image 01 - Concert hall rig, regenerate for the tree geometry

| Field | Value |
|---|---|
| Filename | `spatial-recording-concert-hall-rig-banner-02.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 667 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Images/spatial-recording/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3345--Spatial_Audio_II/Images/spatial-recording/spatial-recording-concert-hall-rig-banner-02.jpg` |
| Used on | Canvas page `Spatial Recording: Section Overview` |
| Alt text | `Concert hall stage set for an orchestral recording with a Decca Tree and outrigger microphones` |
| Caption | `Figure 1. The capture this section is built on.` |

**Why regenerate.** The `-01` is a good photograph, but the three main microphones sit in a
straight line on a horizontal bar. A Decca Tree is a **triangle**: the centre microphone
stands roughly 1.5 m forward of the two outer ones, which are about 2 m apart. Shot head on,
a real tree still reads as a triangle because the centre mic is visibly nearer the camera.
This one does not. For a section that teaches the technique by name, that is a substance
defect under §20.4b, not a presentation one.

**The fix is the camera angle as much as the rig**, so this prompt moves to three-quarter.

**Better source, still:** a photograph from the February session. Students are mixing that
exact recording, and §20.6 puts real microphones outside what a generator should be drawing
at all. This prompt is the fallback.

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 667 pixel JPEG at quality 88.

Photorealistic photograph. Warm stage lighting from above, dark auditorium falling away at
the left edge, real wood stage floor and real matte black metal stands with visible surface
texture, shallow depth of field. Camera positioned to one side of the hall and slightly
elevated, looking across the stage at a three-quarter angle rather than straight on.

A concert hall stage set up for an orchestral recording, with no musicians present. The
main feature is a tall microphone boom carrying three small cylindrical condenser
microphones arranged as a clear triangle when seen from this angle: one microphone stands
well forward of the other two, and those two are spaced widely apart behind it. The
triangular arrangement is obvious and is the focal point of the image. Two further
microphones stand on tall stands at the far left and far right edges of the stage. Two
compact spherical microphone arrays sit on their own separate stands. Several short stands
carry single microphones among empty orchestra chairs and music stands.

Reading direction is left to right across the stage, with the three-microphone triangle
the clear subject.

No text anywhere in the image. No logo, brand mark, model number, or badge on any
microphone, stand, or case. No borders, frames, title bars, or caption text. No people, no
watermark, no signature.
```

---

## Image 02 - Final project build, optional brighten

| Field | Value |
|---|---|
| Filename | `final-project-playable-build-banner-02.jpg` |
| Format | JPEG, quality 88, its own background |
| Dimensions | 1600 x 667 px |
| Destination folder | `/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II/Images/final-project/` |
| Raw URL after push | `https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3345--Spatial_Audio_II/Images/final-project/final-project-playable-build-banner-02.jpg` |
| Used on | Canvas page `Final Project: Section Overview` |
| Alt text | `A dim untextured game corridor on a monitor with a controller held in silhouette` |
| Caption | `Figure 1. The build, running.` |

**Why this is optional.** The `-01` is correct: untextured grey geometry, warm light at the
end, controller in hand, no heads-up display, no text. Nothing in it is false. The problem
is presentation only. It is by far the darkest image in the course, the outer thirds are
close to pure black, and on a white Canvas page a 2.4:1 banner that is mostly black reads as
a bar with a small bright window in it. Every other banner carries light across the whole
frame.

Regenerate if you want the set to look even. Keep the `-01` if you like the mood.

**ChatGPT prompt (paste as-is):**

```text
Create a 1600 x 667 pixel JPEG at quality 88.

Photorealistic photograph of a desk at night. The monitor is the brightest thing in the
frame, but the room is not black: a soft warm lamp somewhere off frame to the left lifts the
desk surface, the wall behind, and the edges of the objects, so detail is visible right
across the picture. Real wood desk and real matte plastic with visible surface texture,
shallow depth of field.

A wide monitor fills the centre of the frame, in sharp focus, displaying a first-person view
down a dim industrial corridor built from plain untextured light grey geometric blocks, with
a single warm light source glowing at the far end and reflecting off the floor. In the
foreground, low in the frame and softly out of focus, a game controller held in two hands,
lit enough by the lamp to read clearly as a controller. A plant and a cup of pens sit at the
far left and far right edges, dim but visible, so the composition carries to both sides.

Reading direction is foreground to screen, and the mood is arrival rather than construction.

No text anywhere in the image. No heads-up display, no menus, no interface elements, no
crosshair, no icons. No logo, brand mark, or model number on the monitor or the controller.
No borders, frames, title bars, or caption text. No watermark, no signature.
```

---

## The four that are captures, not prompts

§20.1 rule 3 is explicit: front panels, plug-in GUIs, **DAW windows**, meters, Pro Tools
dialogs and Dolby Renderer screens are sourced, never generated. ChatGPT invents controls
and fabricates model numbers, and a photorealistic fake is more convincing and exactly as
wrong. Each of these is a screenshot or a screen-recording still from the real application,
cropped to 1600 x 667 and saved as JPEG quality 88.

| # | Filename and folder | What to capture | Why |
|---|---|---|---|
| 03 | `fmod/fmod-authoring-session-banner-01.jpg` | A real FMOD Studio session. Event editor open, timeline legible, a 3D panner or spatializer visible on an event. | Replaces `fmod-implementation-desk-banner.jpg`, which shows a fabricated DAW timeline and also opens the Wwise section. |
| 04 | `wwise/wwise-authoring-hierarchy-banner-01.jpg` | A real Wwise Authoring session, Project Explorer tree expanded down the left so the hierarchy is the subject. Voice Profiler or attenuation editor in frame is a bonus. | Wwise currently has no banner of its own. Create the folder `Images/wwise/`. |
| 05 | `implementation/implementation-engine-editor-banner-01.jpg` | A real engine editor, level open with audio emitters placed, and a code editor in the same frame showing a script that posts an event or sets a parameter. | Implementation has no banner. The section's argument is that placing and scripting are one activity, so both belong in one frame. |
| 06 | `interactive-audio/interactive-audio-workstation-banner-02.jpg` | A real DAW session and a real engine viewport, side by side, the same two-tool comparison the current image fakes. | **New in revision 2.** The current `-banner.jpg` fabricates both screens. My audit passed it and should not have. |

Captures 03 and 04 exist so FMOD and Wwise look like different tools. Right now both section
overviews open with the same borrowed photograph.

---

## Two repo defects that need no new art

**1. One image is over the weight cap.** §20.3 caps a JPEG at 500 KB.

| File | Size |
|---|---|
| `final-project/final-project-study-guide-banner.jpg` | 532,822 bytes, 520 KB |

Everything else is inside. One command fixes it, and I can run it on your say-so.

**2. The width problem, and it predates this brief.** §20.3 sets a full-width Canvas figure
at 1600 px. Not one of the twenty images in the repo is 1600 px wide:

| Shape | Count | Current width |
|---|---|---|
| Banners | 11 | 1942 px |
| Concept figures | 9 | 1536 px |

Nothing is broken, because the pages carry `max-width:100%`, so they scale. It is a standards
gap rather than a rendering fault, and mixing 1600 with 1942 would look worse than being
consistently off. Three options, and this is your call:

- **Down-sample all twenty to 1600 wide.** One pass, no regeneration, no re-prompting, and
  every filename and reference stays identical because only the pixels change. Banners become
  1600 x 667, concept figures 1600 x 1067.
- **Leave them and amend §20.3** to name a banner row at 1942 x 809, since the table has no
  banner entry today and that is arguably the real gap.
- **Leave them and record the exception** in the build notes.

---

## What I do once the files land

1. Add the `<img>` block to the section overviews that have no banner.
2. Repoint `wwise-section-overview.html` off `fmod-implementation-desk-banner.jpg`.
3. Retire `fmod-implementation-desk-banner.jpg` and `interactive-audio-workstation-banner.jpg`,
   neither of which conforms to §20.4 anyway, both lacking the `-nn` counter, and rewrite
   every reference.
4. Regenerate the §8.1 Image Reference page so the three new folders appear.
5. HTTP check every new raw URL and report any that does not return 200.

Then push, or Canvas keeps serving the old files:

```
cd ~/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3345--Spatial_Audio_II && git add -A && git status
```
