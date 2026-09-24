# Image Fixes For Later: DAPR All Courses

Parked 2026-09-23 so the course builds can move. Nothing here blocks a rebuild; the current files work, they are just weaker than they should be. Paths are under:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/
```

## Claude can finish these (just say go)

| File | What is wrong | Plan |
|---|---|---|
| `DAPR-3255--Audio_Hardware_II/Electronics/Rendered_Triangles_With_Banded_Resistors.png` and `..._Tan_Resistors.png` | Ground resistor drawn on top of the input wire | Redraw both op amp circuits cleanly (Image 21 in the ChatGPT file also covers it) |
| `DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/DMX_Universe_Addressing.png` | Caption says ranges overlap; none do in the drawing | Redraw with two overlapping fixture ranges |
| `DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/TRS_MIDI_Cables_3.5mm.jpg` | Nothing shows Type A vs Type B | Draw a Type A vs Type B wiring diagram |
| `DAPR-2255--Audio_Hardware_I/Schematics/Logic_Gates.png` | OR, NOR, XOR, XNOR input leads stop short | Touch up the leads |
| `DAPR-3255--Audio_Hardware_II/Final_Exam/Schematic_Symbols.png` and `Transformer_Symbols.jpg` | Low resolution, labels unreadable | Rebuild from SparkFun open symbols (CC BY-SA 4.0) |
| `DAPR-3340--Spatial_Audio_I/Surround_Monitoring/Speaker_Placement.jpg`, `Theatrical_Listening_Environment.jpg` | Small third party figures, notes unreadable | Redraw as clean diagrams |
| `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround_and_Multichannel_Audio/Analog_Digital_Delivery_Evolution.png` | 639 px wide, text too small | Rebuild at 1600 wide |
| `DAPR-2020--Core_Mixing/Effects__Spectral_Effects_and_EQ/Vocal_EQ_Frequency_Band_Chart.jpg` | Washed out third party chart | Rebuild as a clean chart |
| Denon AVR-5803 rear photo (held, not placed) | Serial number visible | Blur the serial before any page uses it |
| `DAPR-2020--Core_Mixing/Effects__Dynamic_Effects/Compression_Switch.png` | Five numbered callouts with no legend, so the numbers mean nothing. Purple and cyan, off the section 3 palette. The picture is a side-chain trigger, not a compression switch, so the filename and the folder are both wrong | Redraw on palette with a legend, rename to what it shows, and move it to `Effects__Frequency_Dynamics_and_Side-Chains/` |
| `DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Please_Complete_Your_Course_Evaluations.png` | Another student's name is readable in the second browser tab. Section 4 rule 4 says blur other people's names | Blur the tab title, then it can go on the Course Evaluations page beside the other two screenshots |
| `DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Course_Outline_Banner_Alt.png` | Square at 1024 by 1024, so it crops badly wherever a banner is wide. The wide `Course_Outline.png` is the one in use | Re-render wide, or retire it |
| `DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Dark_Purple_Course_Title_Card.jpg` | Reads "Course Outline & Industry Roadmap", which is a different artifact from this course's outline. 655 by 550 | Re-render with the right words, or retire it |

## Needs Adam (photo, screenshot, or a decision)

| File | What to do |
|---|---|
| `DAPR-3255--Audio_Hardware_II/Electronics/Talkback_Box_Assembled.jpg` | Phone photo of a finished talkback box (current file is a hand and a cable) |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Time_Machine_Restore.jpg` | Real screenshot (current is a phone photo of a screen) |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Screenshot_Options_Menu_over_System_Settings.jpg` | Real screenshot |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Terminal_Pwd_Ls_Cd.png` | Narrow Terminal window running pwd, ls, cd |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Function_Keys_Panel.png` | System Settings, Keyboard, Function Keys |
| `DAPR-2010--Core_Recording/Studio_Use_and_Care/Studio_Floor_Plan.png` | Send room names and rough layout; Claude draws it |
| `DAPR-2010--Core_Recording/Studio_Use_and_Care/Power_Up_Sequence_Alt.png` | Decide which power up order is right (it disagrees with Power_Up_Sequence.png) |
| `DAPR-2000--Digital_Audio_Essentials/Monitoring__Psychoacoustics/Sound_Field_Speaker_Placement.png` | Re-export larger from its source |
| `DAPR-3255--Audio_Hardware_II/Electronics/Symbol_Inductor.png` | Re-export the full strip from its source |
| `All/DAPR_Introduce_Yourself/Example_Headshot.jpg` | Confirm consent or AI origin, or swap in your own |
| `DAPR-3345--Spatial_Audio_II/Interactive_Audio__Foundations_of_Interactive_Spatial_Audio/Workstation_Banner.jpg` and `_Alt` | Made up DAW screens; replace with real FMOD or Wwise captures when you have them |
| `DAPR-2255--Audio_Hardware_I/Power/Wattmeter.jpg` | Optional: page link for the plug in meter photo, for the credit line |
| `DAPR-2020--Core_Mixing/Orientation__Course_Orientation_and_Feedback/Core_Recording_DAPR_2010_002.png` | A DAPR 2010 title card sitting in the DAPR 2020 folder. Moving it is on the v31 approval table; say yes there and it goes to `DAPR-2010--Core_Recording/Course_Orientation/` |

Added 2026-09-23 during the DAPR 2020 v31 build, under section 4 rule 3 of Decisions Already Made: keep the weak image, log it, do not stop the build.


## DAPR 3340 figures whose file no longer exists (found 2026-09-23 during the v50 rebuild)

Ten pages carry an `<img>` whose GitHub URL returns 404. The original files are not in the
repo under any name, including `_unused` and every `Archive`. The prose around each one says
"see Figure N", so the page reads wrong without it. None of these blocks the v50 import; the
course imports unpublished.

| Page | Missing file | Old alt text, which names the original | Proposed fix |
|---|---|---|---|
| `ambisonics-basics` | `DAPR-3340--Spatial_Audio_I/Ambisonics_and_Binaural/Ambisonics_Basics.png` | `Fig06_01-AmbisonicsLogo.png` | Point at `Ambisonic_Logo.png`, already in that folder and clearly the same picture |
| `working-with-binaural-in-pro-tools` | `Ambisonics_and_Binaural/Channel_Strip_With_Binaural_Insert.png` | `Fig06_20a-Select-IRCAMHEAR-StereoOut.png` | Point at `Binaural_Renderer_Channel_Strip.png`, already in that folder |
| `exercise-ambisonics-and-binaural-post` | `Ambisonics_and_Binaural/Exercise_Post.png` | `2024-08-23_11-12-38.png` | Recapture: the Quad clip in the Pro Tools clip list |
| `multichannel-formats-emerge` | `Introduction_to_Surround_and_Multichannel_Audio/Star_Wars_Dolby_Stereo.png` | `Historical Star Wars and Dolby Stereo image` | Source a licensable 1977 Dolby Stereo print image, or drop the figure and keep the prose |
| `exercise-surround-mastering-music` | `Surround_Mastering_and_Surround_Encoding/Exercise_Music.png` | `Fig5.31-ImportAudioDialog.png` | Recapture: the Import Audio dialog with Copy showing |
| `exercise-surround-mastering-post` | `Surround_Mastering_and_Surround_Encoding/Pro_Limiter_Plugin_Window.png` | `2024-08-21_12-45-57.png` | Recapture, or point at `Surround_Limiter_Plugin_Window.jpg` in that folder if it shows the ceiling at zero |
| `exercise-surround-mixing-and-surround-plugins-music` | `Surround_Mixing_and_Surround_Plugins/Exercise_Music.jpg` | `4-X Automation-cropped.jpg` | Recapture: a track header with automation lanes shown |
| `room-design-and-acoustics` | `Surround_Monitoring/Room_Design_and_Acoustics.png` | `image.png` | Recapture or redraw: the room treatment tool the paragraph describes |
| `introduction-to-surround-recording` | `Surround_Recording/Introduction_to_Surround_Recording.png` | `Spacial Impression.png` | Redraw: localization against envelopment, the two ideas the paragraph sets up |
| `using-surround-microphones` | `Surround_Recording/Using_Surround_Microphones.gif` | `Ambisonics.gif` | Redraw as a still: decoding to an arbitrary speaker layout. It was an animated GIF; a labelled diagram carries the same point |

Separately, 34 URLs in the DAPR 3340 cartridge pointed at real files under the wrong spelling
(`Dts_Neo_6` for `DTS_Neo_6`, `bounce-mix.jpg` for `Bounce_Mix.jpg`, `.png` where the file is
`.jpg`). Those were corrected in the cartridge in v50. macOS hid them because it is case
insensitive; raw.githubusercontent.com is not.
