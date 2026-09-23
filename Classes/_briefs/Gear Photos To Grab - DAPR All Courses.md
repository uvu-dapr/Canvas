# Gear Photos: DAPR All Courses

Updated 2026-09-23 evening. Real products come from the manufacturer or an open license, never from ChatGPT (Canvas Standards 20.1 rule 3).

## Already downloaded and in place (19 files, not committed)

Claude downloaded these, checked each one by eye, and saved them over the existing file names, so the pages need no change. Open license photos need the credit in the image caption; manufacturer shots get "Image courtesy (maker)".

| File | Source | Credit |
|---|---|---|
| Tt_Bantam_Plug.png | Hosa TTS-102 | Image courtesy Hosa Technology |
| Db25_Male.png | Hosa DTP-800 snake | Image courtesy Hosa Technology |
| Db25_Female.png | American Radio Supply, right angle DB25 female port (found by Adam) | Image courtesy American Radio Supply |
| Firewire_400_6_Pin.png | StarTech 1394_6 | Image courtesy StarTech.com |
| Adam_Audio_Monitors.jpg | ADAM Audio T5V | Image courtesy ADAM Audio |
| Electrolytic_Large_Bank.jpg | Flickr, NAD 310 interior | "NAD 310 Capacitors" by Turntable Guy, CC BY 2.0 |
| Electrolytic_on_PCB.jpg | SparkFun Capacitors tutorial | SparkFun Electronics, CC BY-SA 4.0 |
| Ceramic.jpg | SparkFun Capacitors tutorial | SparkFun Electronics, CC BY-SA 4.0 |
| Oscilloscope.jpg | Rigol DS1054Z product photo | Image courtesy RIGOL Technologies |
| 3pdt_Toggle_Photo.jpg | SparkFun Proto Pedal guide | SparkFun Electronics, CC BY-SA 3.0 |
| DMX_Fixture.jpg | Chauvet Ovation P-56FC rear panel (3 and 5 pin DMX in and out) | Image courtesy CHAUVET Professional |
| DMX_Terminator.jpg | LEX DMX5P-TERM, 5 pin, 120 ohm | Image courtesy LEX Products |
| PAR_Fixture_DIP_Switch_Bank.jpg (**new file**, the DAPR 2255 page must link it) | The DMX Wiki, 10 switch DMX address bank | Public domain (The DMX Wiki) |
| Schematic_Full.png | SparkFun RedBoard v06, the same revision as the old file, now 2200 x 1700 | SparkFun Electronics, CC BY-SA 3.0 |
| Sennheiser_HD_490_Pro.jpg | Sennheiser press image | Image courtesy Sennheiser |
| PreSonus_Eris_E3.5.jpg | PreSonus product image (first gen pair) | Image courtesy PreSonus |
| JBL_305P_MkII.png | JBL product image, no badges | Image courtesy JBL Professional |
| Audio_Technica_ATH_R30x.png | Audio-Technica product image | Image courtesy Audio-Technica |
| Philips_SHP9500.png | Philips product image | Image courtesy Philips |

## Still needs you

| Save as (under Classes/) | Why Claude could not do it | Easiest fix |
|---|---|---|
| `DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/TA5_Mini_XLR.png` | Switchcraft's site blocked the download | Save [ta5m.jpg](https://www.switchcraft.com/assets/1/24/DimLarge/ta5m.jpg) and [ta5flx.jpg](https://www.switchcraft.com/assets/1/24/DimLarge/ta5flx.jpg) anywhere in the repo and tell Claude, who will set them side by side |
| `DAPR-2255--Audio_Hardware_I/Power/Wattmeter.jpg` | Good photos are on Wikimedia; the maker's image is only 450 px | Download [this Commons file](https://commons.wikimedia.org/wiki/File:P3-Kill-a-watt.jpg), or a phone photo of any plug in power meter |
| `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround_and_Multichannel_Audio/Legacy_Dolby_Hardware_Milestones.png` and `Dolby_Pro_Logic_History_Overview.png` | No openly licensed photos of 1980s Pro Logic gear exist | Photo of an old receiver, or drop the images |

---

# Earlier research notes (reference)


Written 2026-09-23. These are real products, so they come from the manufacturer or an open license, never from ChatGPT (Canvas Standards 20.1 rule 3).

**How to use this file**

1. Open the **Page** link and look at the picture. Check the **Check** column before you keep it.
2. Download the full size image (the **Grab** link, or the largest size on the page).
3. Save it over the **Save as** path, with that exact name and extension. The pages already point there.
4. If the download is a different format from the Save as name, convert it in Terminal. Replace the two paths, and it's done when the `%` prompt comes back:

```
sips -s format png "PASTE_DOWNLOADED_FILE" --out "PASTE_SAVE_AS_PATH"
```

(Use `format jpeg` when the Save as name ends in `.jpg`.)

5. For open license photos, put the **Credit** line in the image caption on the page.

Wikimedia Commons tip: any Commons file downloads full size from `https://commons.wikimedia.org/wiki/Special:FilePath/FILE_NAME`.

Base folder for every path below:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/
```

---

## DAPR 2000: cables and connectors

| Save as | Page | Grab | Check | Credit |
|---|---|---|---|---|
| `DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Tt_Bantam_Plug.png` | [Hosa TTS-102](https://hosatech.com/products/analog-audio/interconnect-cables/single-interconnects/tts-102/) | [TTS-102-Connector.jpg](https://hosatech.com/wp-content/uploads/2014/03/TTS-102-Connector.jpg) | Three conductors: tip, ring, sleeve. Backup: [Bittree TT cords](https://www.bittree.com/collections/patchcords/products/tt-bantam-110-ohm-audio-patch-cables) | Image courtesy Hosa Technology |
| `DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Db25_Male.png` | [Hosa DTP-800 snake](https://hosatech.com/products/analog-audio/snakes/dtp-800/) | [DTP-800-Connector.jpg](https://hosatech.com/wp-content/uploads/2014/03/DTP-800-Connector.jpg) | 25 pins, 13 over 12. Backup: [DBD-300-Connector.jpg](https://hosatech.com/wp-content/uploads/2014/03/DBD-300-Connector.jpg) | Image courtesy Hosa Technology |
| `DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/TA5_Mini_XLR.png` | [Switchcraft TA5MX](https://www.switchcraft.com/tini-qg-mini-xlr-5-pin-male-cable-mount-silver-pins-nickel/ta5mx/) and [TA5FLX](https://www.switchcraft.com/tini-qg-mini-xlr-5-pin-female-cable-mount-no-flex-relief-large-cable-opening-silver-pins-nickel/ta5flx/) | [ta5m.jpg](https://www.switchcraft.com/assets/1/24/DimLarge/ta5m.jpg), [ta5flx.jpg](https://www.switchcraft.com/assets/1/24/DimLarge/ta5flx.jpg), or the [group shot](https://www.switchcraft.com/assets/1/24/DimLarge/mini_xlr_connectors_group.png) | Five pins. Two separate photos: send both to me and I'll set them side by side | Image courtesy Switchcraft Inc. |
| `DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Firewire_400_6_Pin.png` | [Commons: Firewire6-pin.jpg](https://commons.wikimedia.org/wiki/File:Firewire6-pin.jpg) | Special:FilePath link on that page | Rounded 6 pin end, not the square 9 pin FireWire 800. Backup: [StarTech 1394_6](https://www.startech.com/en-us/cables/1394_6) | From the Commons page |
| `DAPR-2000--Digital_Audio_Essentials/Signal_Flow__Cables_and_Connections/Adam_Audio_Monitors.jpg` | [ADAM T5V](https://www.adam-audio.com/en/t-series/t5v/) | [T5V featured image](https://www.adam-audio.com/content/uploads/2023/04/adam-audio-t5v-studio-monitor-featured-image.png) | At least 1200 wide. Backup: [T7V](https://www.adam-audio.com/content/uploads/2023/04/adam-audio-t7v-studio-monitor-featured-image.png) (1500 x 1000) | Image courtesy ADAM Audio |

## DAPR 2255: electronics and lighting

| Save as | Page | Grab | Check | Credit |
|---|---|---|---|---|
| `DAPR-2255--Audio_Hardware_I/Capacitors/Electrolytic_Large_Bank.jpg` | [Flickr: NAD 310 Capacitors](https://www.flickr.com/photos/alternativeroute/5194242792) | [Original, 2048 x 1536](https://live.staticflickr.com/5001/5194242792_aa2528d4fa_o.jpg) | Big filter cans inside an amp | "NAD 310 Capacitors" by Turntable Guy, CC BY 2.0 |
| `DAPR-2255--Audio_Hardware_I/Capacitors/Electrolytic_on_PCB.jpg` | [Commons: Electrolytic capacitors mounted on a circuit board](https://commons.wikimedia.org/wiki/File:Electrolytic_capacitors_mounted_on_a_circuit_board.jpg) | Special:FilePath link on that page | At least 1200 wide | From the Commons page |
| `DAPR-2255--Audio_Hardware_I/Capacitors/Ceramic.jpg` | [Commons: Ceramic capacitors](https://commons.wikimedia.org/wiki/File:Ceramic_capacitors.jpg) | Special:FilePath link on that page | Disc caps with readable codes like 104. Backup: [SparkFun photo](https://cdn.sparkfun.com/assets/6/5/f/8/e/51968eb0ce395f432c000001.jpg) (smaller) | From the Commons page, or SparkFun Electronics, CC BY-SA 4.0 |
| `DAPR-2255--Audio_Hardware_I/Multimeters/Oscilloscope.jpg` | [Flickr: Adafruit Rigol DS1054Z](https://www.flickr.com/photos/adafruit/48092521332) | [Original, 6250 x 4807](https://live.staticflickr.com/65535/48092521332_dd43bf6448_o.jpg) | A waveform on the screen is a plus | "Rigol DS1054Z" by Adafruit Industries, CC BY-NC-SA 2.0 |
| `DAPR-2255--Audio_Hardware_I/Power/Wattmeter.jpg` | [Commons: P3 Kill A Watt](https://commons.wikimedia.org/wiki/File:P3-Kill-a-watt.jpg) | Special:FilePath link on that page | Readable display. Backup: [Flickr kill-a-watt, 1600 x 1200](https://live.staticflickr.com/23/29362266_8532314c74_o.jpg) | From the Commons page, or "kill-a-watt" by ninjabong, CC BY-NC-SA 2.0 |
| `DAPR-2255--Audio_Hardware_I/Switches/3pdt_Toggle_Photo.jpg` | [Commons: Toggle Switch 3PDT](https://commons.wikimedia.org/wiki/File:Toggle_Switch_-_3PDT.jpg) | Special:FilePath link on that page | All nine lugs visible. Backup: [SparkFun 3PDT stomp switch](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/5/detail-stomp-switch.jpg) | From the Commons page, or SparkFun Electronics, CC BY-SA 3.0 |
| `DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/DMX_Fixture.jpg` | [Chauvet Ovation P-56FC](https://chauvetprofessional.com/product/ovation-p-56fc/) | [OVATION-P-56-BACK.png](https://chauvetprofessional.com/wp-content/uploads/2025/10/OVATION-P-56-BACK.png) | Rear panel with 5 pin DMX in and out readable (it also has 3 pin, which is a good teaching point) | Image courtesy CHAUVET Professional |
| `DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/DMX_Terminator.jpg` | [LEX DMX5P-TERM](https://lexproducts.com/powerflex_detail?part=DMX5P-TERM) | [DMX5P-TERM_1_web.jpg](https://lexproducts.com/admin/storage/uploads/2020/02/08/5e3e218234b3eDMX5P-TERM_1_web.jpg) | 5 pin XLR male, 120 ohm. Probably small, so your own photo would beat it. Backup: [ADJ DMX5T](https://www.adj.com/products/dmx5t10pack) (110 ohm) | Image courtesy LEX Products |
| `DAPR-2255--Audio_Hardware_I/MIDI__Systems_and_Implementation/PAR_Fixture_DIP_Switch_Bank.jpg` | [The DMX Wiki: Dip Switches](https://www.thedmxwiki.com/dmx_definitions/dip_switches) | [snv12415.jpg, 1024 x 768](https://www.thedmxwiki.com/_media/dmx_definitions/snv12415.jpg) | Public domain but small, and the switch count isn't confirmed. **Best option: photograph a PAR's DIP bank from your lighting kit** | Public domain (The DMX Wiki) |

## DAPR 3255: schematics

| Save as | Page | Grab | Check | Credit |
|---|---|---|---|---|
| `DAPR-3255--Audio_Hardware_II/Final_Exam/Schematic_Full.png` | [SparkFun RedBoard](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) | [RedBoard V22 schematic PDF](https://cdn.sparkfun.com/datasheets/Dev/Arduino/Boards/RedBoard-V22.pdf), or the [RedBoard Qwiic PDF](https://cdn.sparkfun.com/assets/c/5/7/e/f/RedBoard-Qwiic.pdf) | Pick the board your students use. Drop the PDF in the folder and I'll export it to a sharp PNG | SparkFun Electronics, CC BY-SA 4.0 |
| `DAPR-3255--Audio_Hardware_II/Final_Exam/Schematic_Symbols.png` | [SparkFun: How to Read a Schematic](https://learn.sparkfun.com/tutorials/how-to-read-a-schematic) | Nothing to grab | I'll build one labeled chart from SparkFun's open symbols | SparkFun Electronics, CC BY-SA 4.0 |

## Current headphones and monitors (All/DAPR_Monitor)

| Save as | Page | Grab | Check | Credit |
|---|---|---|---|---|
| `All/DAPR_Monitor/Sennheiser_HD_490_Pro.jpg` | [Sennheiser newsroom](https://newsroom.sennheiser.com/built-to-handle-the-complexities-of-todays-music-production-zc8y6e) | The "HD_490_PRO_Product_Shot_Cutout_Iso_View" original | Whole headphone in frame; skip the TEC Winner badge version | Image courtesy Sennheiser |
| `All/DAPR_Monitor/PreSonus_Eris_E3.5.jpg` | [PreSonus Eris E3.5](https://www.presonus.com/products/eris-e35-studio-monitor) | [Front view, 3000 x 2137](https://cdn.shopify.com/s/files/1/0705/5772/9001/files/2777500101_pre_mon_frt_1_nr.png) | First gen E3.5. If you teach the 2nd Gen: [pair, 3000 x 1775](https://www.presonus.com/products/eris-35-2nd-gen-pair) | Image courtesy PreSonus |
| `All/DAPR_Monitor/JBL_305P_MkII.png` | [JBL 305P MkII](https://www.jbl.com/305PMKII-.html) | [JBL_305PMKII_Hero.png](https://www.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dwc859c659/JBL_305PMKII_Hero.png) | No award badges | Image courtesy JBL Professional |
| `All/DAPR_Monitor/Audio_Technica_ATH_R30x.png` | [Audio-Technica ATH-R30x](https://www.audio-technica.com/en-us/ath-r30x) | [ath-r30x_04.png](https://www.audio-technica.com/media/catalog/product/a/t/ath-r30x_04.png) | Confirmed R30x, not R70x | Image courtesy Audio-Technica |
| `All/DAPR_Monitor/Philips_SHP9500.png` | [Philips SHP9500](https://www.usa.philips.com/c-p/SHP9500_00/hifi-stereo-headphones) | [Main image, 2248 x 3000](https://images.philips.com/is/image/philipsconsumer/d9c5751249db420b88b5b0c2004b8870?$png$&wid=2248&hei=3000) | Open grilles visible. Philips lists it as discontinued | Image courtesy Philips |

## DAPR 3340: Dolby history

| Save as | Page | Grab | Check | Credit |
|---|---|---|---|---|
| `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround_and_Multichannel_Audio/Legacy_Dolby_Hardware_Milestones.png` | [Science Museum: Dolby CP50](https://collection.sciencemuseumgroup.org.uk/objects/co8338252/cp50-dolby-stereo-processor-projection-equipment) | [CP50 photo](https://coimages.sciencemuseumgroup.org.uk/531/244/large_smg00222363.jpg) | Real CP50 cinema processor. Check the license line on the page. Also [Commons Dolby 361](https://commons.wikimedia.org/wiki/File:Dolby361.jpg) and [Dolby SR breadboard](https://commons.wikimedia.org/wiki/File:Dolby_SR_breadboard.jpg). Grab two or three and I'll make the collage | © Science Museum Group; others from their Commons pages |
| `DAPR-3340--Spatial_Audio_I/Introduction_to_Surround_and_Multichannel_Audio/Dolby_Pro_Logic_History_Overview.png` | [Commons: Yamaha RX-V359 logos](https://commons.wikimedia.org/wiki/File:DTS_Surround_and_Dolby_Digital_Pro_Logic_II_logos_on_Yamaha_RX-V359_AV_receiver.jpg) | Special:FilePath link on that page | Weak: shows Pro Logic II, not 1987 Pro Logic. Nothing better is openly licensed. **Best option: photograph an old Pro Logic receiver**, or drop this image | From the Commons page |

---

## Only you can capture these

| Save as | What |
|---|---|
| `DAPR-3255--Audio_Hardware_II/Electronics/Talkback_Box_Assembled.jpg` | Photo of the finished talkback box |
| `DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/Track_Input_Selector.png` | Pro Tools screenshot of the track input selector |
| `DAPR-3340--Spatial_Audio_I/Surround_Mastering_and_Surround_Encoding/Common_Audio_Meters.png` | Screenshots of real meter plugins |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Time_Machine_Restore.jpg` | Screenshot (Shift Command 4) |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Screenshot_Options_Menu_over_System_Settings.jpg` | Screenshot |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Terminal_Pwd_Ls_Cd.png` | Narrow Terminal window running pwd, ls, cd |
| `DAPR-2020--Core_Mixing/macOS__Foundations/Function_Keys_Panel.png` | System Settings, Keyboard, Function Keys |
| `DAPR-2010--Core_Recording/Studio_Use_and_Care/Studio_Floor_Plan.png` | Send me the room names and rough layout and I'll draw it |

## Claude builds these (diagrams, no real products)

TRS_MIDI_Cables_3.5mm Type A vs Type B wiring, Schematic_Symbols chart, Transformer symbols, Speaker_Placement (ITU 5.1), Theatrical_Listening_Environment, Analog_Digital_Delivery_Evolution, Vocal_EQ_Frequency_Band_Chart.
