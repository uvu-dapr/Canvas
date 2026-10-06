#!/usr/bin/env python3
"""DAPR 3340 J122 (Adam, 2026-10-06, "By due date + new readings"): the three-week Week 01 module becomes
Week 01 Introduction, Week 02 Surround Routing (two pages moved + two new), Week 03 Surround Panning (four new pages),
facts from the Pro Tools Reference Guide 2026.4 (chapters 52, 57, 58, 59). Text edits only (Platform Reference 22a).
    python3 split_3340.py <unzipped package folder>
"""
import sys, os, re, hashlib, html

W = sys.argv[1]
RAW = "https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/DAPR-3340--Spatial_Audio_I/Surround_Mixing_and_Surround_Plugins/"
ICON = "https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/All/DAPR_Canvas_Icon_Reference/"
def gid(*p): return "g" + hashlib.md5("|".join(("3340-j122",) + p).encode()).hexdigest()

def h2(t): return '<h2 style="color:#1b5e20; font-size:1.3em; border-bottom:2px solid #1b5e20; padding-bottom:4px;">%s</h2>' % t
def fig(f, alt, cap): return ('<p><img style="max-width: 100%%; height: auto;" src="%s%s" alt="%s"></p>\n<p><em><span style="color:#616161;">%s</span></em></p>' % (RAW, f, alt, cap))
def callout(kind, head, body):
    col = {"Note": ("#e3f2fd", "#0d47a1"), "Tip": ("#f3e5f5", "#4a148c"), "Warning": ("#fff8e1", "#BF360C"), "Required": ("#e8f5e9", "#1b5e20")}[kind]
    return ('<div style="background-color:%s; border-left:4px solid %s; margin:16px 0; padding:12px 14px;"><img src="%sCallout_%s.png" alt="%s" width="44" height="44" style="vertical-align:middle; margin-right:10px;"><strong style="vertical-align:middle;">%s</strong><div style="margin-left:54px; margin-top:4px;">%s</div></div>'
            % (col[0], col[1], ICON, kind, kind, head, body))
def ul(items): return "<ul>\n" + "\n".join("<li>%s</li>" % i for i in items) + "\n</ul>"
def page(title, body):
    return ('<div style="font-family:Arial, Helvetica, sans-serif; max-width:900px; margin:0 auto; color:#212121; line-height:1.6; background-color:#ffffff; padding:0 12px;">\n'
            '<h2 style="background-color:#1b5e20; color:#ffffff; padding:16px 20px; font-size:1.4em; border-radius:4px;">%s</h2>\n%s\n</div>' % (title, body))

PAGES = [
 ("Week 02", "Surround Routing: Sub-Paths for Dialog, Music, and Effects", "surround-routing-sub-paths-for-dialog-music-and-effects-f26",
  fig("Output_Path_Submenu_of_Subpaths.jpg", "An output selector showing a 5.1 path and its sub-paths", "A 5.1 path and the sub-paths inside it, as the output selector lists them") +
  "<p>A 5.1 path carries six channels. A <strong>sub-path</strong> is a smaller path inside it that reaches only some of those channels. When you route a track to a sub-path, the track lands in exactly the speakers that sub-path covers, and nowhere else. Sub-paths are made in the I/O Setup dialog (Setup &gt; I/O), on the Output and Bus pages, under the main path.</p>" +
  h2("The sub-paths a 5.1 mix uses") +
  ul(["<strong>LCR</strong>: the front three channels. Use it for dialog and other sounds that should stay forward.",
      "<strong>Stereo (front L and R)</strong>: music stems and effects that belong in the front left and right speakers.",
      "<strong>Center</strong>: a mono path to the center channel alone.",
      "<strong>Ls/Rs</strong>: the two surround channels, for surround effects and ambience.",
      "<strong>LFE</strong>: a mono path to the LFE channel alone.",
      "<strong>5.0</strong>: all five full-range channels without the LFE. It keeps tracks out of the LFE channel."]) +
  "<p>The default 5.1 settings give you one 5.1 main output bus with sub-paths for 5.0, left/right, LCR and center, plus a stereo main bus. Anything else (Ls/Rs, LFE) you add with New Sub-Path.</p>" +
  h2("Why use a sub-path instead of panning") +
  "<p>Panning a track on a 5.1 path can always reach all six channels, and a move of the panner can pull it somewhere you did not intend. A sub-path makes the destination fixed: dialog on an LCR sub-path can never leak into the surrounds, and a music stem on the front stereo sub-path never touches the center. Pro Tools also folds a wider track down (or fans a narrower one out) automatically when the widths differ, using the Routing Coefficients in the Mixing Preferences; the output selector shows &gt; for a fold down and &lt; for a fan out.</p>" +
  callout("Tip", "Make the sub-path before you need it", "Set up LCR, front stereo, Ls/Rs and LFE sub-paths once, export the I/O Settings file, and import it into the next surround session (I/O Setup, Import Settings). Every session then starts with the same routing.")),
 ("Week 02", "Surround Routing: Building a 5.1 Submix on an Aux Input", "surround-routing-building-a-5-1-submix-on-an-aux-input-f26",
  fig("Submix_Strips_Feeding_Main_Mix.png", "Submix Aux Input tracks feeding the main mix", "Submix tracks feeding the main mix") +
  "<p>A submix gathers several tracks onto one bus, then brings that bus back on an <strong>Aux Input track</strong> so one fader, one set of plugins and one mute control them all. In surround the idea is the same as in stereo; the bus and the Aux Input are simply 5.1 wide.</p>" +
  h2("A discrete submix (track outputs)") +
  "<p>Use track outputs when every bit of the signal should pass through the submix, for example a bus compressor on a group of effects:</p>" +
  "<ol>\n<li>Set the output of each contributing track to a 5.1 bus path (Effects, for example).</li>\n<li>Pan each track in the 5.1 panner.</li>\n<li>Choose Track &gt; New and make an Aux Input track, 5.1 format.</li>\n<li>Set the Aux Input's input to the same 5.1 bus.</li>\n<li>Set the Aux Input's output to the 5.1 main output path.</li>\n<li>Put any plugin on the Aux Input; its wet and dry settings decide how much effect is heard.</li>\n</ol>" +
  "<p>The track faders now balance the submix, and the Aux Input fader sets the level of the whole group. Volume, pan, mute and the send controls of the Aux Input can all be automated.</p>" +
  h2("A send and return submix (reverb and delay)") +
  "<p>For a shared reverb, keep each track's main output on the 5.1 main path and add a <strong>send</strong> to a bus instead. On the Aux Input that receives the bus, put the reverb at 100% wet and turn on Solo Safe, so soloing a track does not mute the reverb return. The track faders set the dry level; the send level (or the Aux Input fader) sets the wet level.</p>" +
  callout("Note", "Stems are submixes too", "A stem (dialog, music, effects) is a submix that is also printed on its own. Each stem gets its own bus path and Aux Input, and the stems together feed the main mix.")),
 ("Week 03", "Surround Panning: The Output Window and the X/Y Grid", "surround-panning-the-output-window-and-the-x-y-grid-f26",
  fig("Surround_Panner_Output_Window.jpg", "A track's Output window with the surround panner grid", "The Output window: the full-size surround panner") +
  "<p>A track can be panned in surround only after its output is assigned to a multichannel path (5.1, for example). Then a <strong>Panner Grid</strong> appears on the track in the Mix window, and in the Edit window when I/O View is shown (View &gt; Edit Window &gt; I/O).</p>" +
  h2("Opening the full-size panner") +
  "<p>Click the small fader button at the right edge of the track's Output selector. The <strong>Output window</strong> opens with a large X/Y Grid, the speakers drawn around it, the track fader, mute, and the panning controls. Several Output windows can be open at once.</p>" +
  h2("The Pan Location cursor") +
  "<p>The dot in the grid is the <strong>Pan Location cursor</strong>; where it sits is where the sound comes from. Its color shows the track's automation mode:</p>" +
  ul(["<strong>Green</strong>: Read.", "<strong>Red</strong>: Write, Touch, Latch or Touch/Latch.", "<strong>Yellow</strong>: automation Off (or suspended)."]) +
  h2("Moving it") +
  ul(["Drag anywhere in the grid: the cursor moves relative to your drag, so a click does not make it jump.",
      "Command-Shift-click a spot to snap the cursor there.",
      "Click a speaker icon to snap the pan to that speaker.",
      "Hold Command for fine adjustment; Shift-drag to move in X or Y only.",
      "Option-click the grid to reset every panner control."]) +
  callout("Warning", "Not moving? Check the output first", "If no Panner Grid appears, the track's output is stereo or mono. Assign it to the 5.1 path (or a 5.1 bus) and the grid appears.")),
 ("Week 03", "Surround Panning: Front, Rear, and Front/Rear Linking", "surround-panning-front-rear-and-front-rear-linking-f26",
  fig("Divergence_Front_Rear_Link.png", "The panner's Front, Rear and F/R position knobs with the link button", "The Position knobs: Front, Rear and F/R, with the Front/Rear link button below them") +
  "<p>Below the grid are three <strong>Position</strong> controls:</p>" +
  ul(["<strong>Front</strong>: left to right across the front speakers.",
      "<strong>Rear</strong>: left to right across the rear (surround) speakers.",
      "<strong>F/R</strong>: front to back."]) +
  h2("Front/Rear linking") +
  "<p>By default Front and Rear are <strong>linked</strong>: moving F/R carries the sound front to back along one left/right line. Unlink them and Front and Rear can sit in different places, so a front to back move travels diagonally (for example, from front left to rear right).</p>" +
  h2("Stereo tracks on a 5.1 path") +
  fig("Linked_Dual_Surround_Panner_Grids.jpg", "Two surround panner grids for a stereo track, linked", "A stereo track on a 5.1 path gets a left and a right panner") +
  "<p>A stereo track routed to a 5.1 path gets <strong>two panners</strong>, one for its left channel and one for its right. Three links are on by default: <strong>Link</strong> (the two move together), <strong>Front Inverse</strong> and <strong>Rear Inverse</strong> (left and right mirror each other across the front and the rear). Front/Rear Inverse is off by default. With the mirror links on, widening the left channel widens the right channel to match.</p>" +
  callout("Tip", "Keep the image steady", "Most of a surround mix should stay where you put it. Moving pans are for effects that really travel (a pass by, a fly over); too many moving elements make a surround mix hard to follow.")),
 ("Week 03", "Surround Panning: Center Percentage and Divergence", "surround-panning-center-percentage-and-divergence-f26",
  fig("Pt_Surround_Panner_Annotated.png", "The Output window's surround panner with its controls labeled", "The surround panner: the Divergence knobs and Center % sit below the Position knobs") +
  h2("Center %") +
  "<p><strong>Center %</strong> sets how much of the signal goes to the center speaker. At 0% a sound panned to the front center is a <strong>phantom center</strong>, made from the left and right speakers only. At 100% the front works as a true three-speaker LCR pan. Music often keeps a low Center % so the center speaker stays clear for dialog.</p>" +
  h2("Divergence") +
  "<p><strong>Divergence</strong> sets how wide a panned sound is, that is, how much it spreads into the speakers next to where it is panned. Full divergence keeps a sound pinned to the speakers nearest its pan position; lower divergence lets it bleed into neighboring speakers, so it sounds wider and less placed. There are three divergence controls:</p>" +
  ul(["<strong>Front</strong> divergence: across the front speakers.", "<strong>Rear</strong> divergence: across the rear speakers.", "<strong>F/R</strong> divergence: between front and rear."]) +
  "<p>All three, and Center %, can be automated. The <strong>Divergence Editing</strong> panning mode lets you drag the divergence boundaries right on the grid.</p>" +
  callout("Note", "Hear it before you trust it", "Pan a sound to front left, then lower Front divergence while listening: the sound spreads toward the center and right. Raise it again and the sound narrows back to the left speaker.")),
 ("Week 03", "Surround Panning: The LFE Fader and Panning Modes", "surround-panning-the-lfe-fader-and-panning-modes-f26",
  fig("Output_Window_With_Highlighted_LFE_Fader.jpg", "An Output window with its LFE fader highlighted", "The LFE fader in a track's Output window") +
  h2("The LFE fader") +
  "<p>The <strong>LFE fader</strong> appears only on &quot;.1&quot; formats (5.1, 6.1, 7.1). It sets how much of the track goes to the LFE channel, and that feed is <strong>post-fader</strong>. LFE faders can follow Mix and Edit groups. Pro Tools applies <strong>no filtering</strong> to the LFE: the channel is full bandwidth, so if a delivery spec asks for a filtered LFE, add the filter yourself. To send a track to the LFE alone, route it to an LFE sub-path instead of using the fader.</p>" +
  h2("The four panning modes") +
  "<p>The <strong>Panning Mode</strong> button below the grid switches between four modes, and every mode can be automated:</p>" +
  ul(["<strong>X/Y</strong> (the default): joystick panning anywhere in the grid. A diagonal move may be heard in some or all channels.",
      "<strong>3-Knob</strong>: set a Front and a Rear point, then move along the straight line between them with F/R. With full divergence, a pan from front left to rear right is heard in just those two speakers.",
      "<strong>Divergence Editing</strong>: drag the divergence boundaries on the grid.",
      "<strong>AutoGlide</strong>: moves from the current position to a new one over a set AutoGlide Time."]) +
  callout("Required", "Check the meters", "After panning, watch the Output window's multichannel meters during playback: they show which of the six channels the track is really reaching."))
]

# 1. pages and manifest resources
man_p = os.path.join(W, "imsmanifest.xml"); man = open(man_p, encoding="utf-8").read()
new_res = []
ids = {}
for wk, title, slug, body in PAGES:
    rid = gid("page", slug); ids[title] = rid
    f = "wiki_content/%s.html" % slug
    doc = ('<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n<title>%s</title>\n<meta name="identifier" content="%s"/>\n<meta name="editing_roles" content="teachers"/>\n<meta name="workflow_state" content="unpublished"/>\n</head>\n<body>\n%s\n</body>\n</html>\n'
           % (html.escape(title, quote=False), rid, page(html.escape(title, quote=False), body)))
    assert all(ord(c) < 128 for c in doc), title
    visible = re.sub(r"<[^>]+>", " ", doc)
    assert "--" not in visible and chr(0x2014) not in visible and chr(0x2013) not in visible, title
    open(os.path.join(W, f), "w", encoding="utf-8").write(doc)
    new_res.append('<resource identifier="%s" type="webcontent" href="%s"><file href="%s" /></resource>' % (rid, f, f))
assert man.count("<resources>") == 1
man = man.replace("<resources>", "<resources>" + "\n".join(new_res) + "\n", 1)
open(man_p, "w", encoding="utf-8").write(man)

# 2. modules
mm_p = os.path.join(W, "course_settings", "module_meta.xml"); s = open(mm_p, encoding="utf-8").read()
mods = re.findall(r'<module identifier="[^"]+">[\s\S]*?</module>', s)
w1 = [m for m in mods if "<title>Week 01: Introduction to Surround and Multichannel Audio</title>" in m]
assert len(w1) == 1, "Week 01 module not found once"
w1 = w1[0]
items = re.findall(r'<item identifier="[^"]+">[\s\S]*?</item>', w1)
def t(it): return html.unescape(re.search(r"<title>([^<]*)</title>", it).group(1))
move = ["Surround Sound and Hardware Basics", "Signal Routing: Multichannel Track Assignments and Output Routing"]
moved = [it for it in items if t(it) in move]
assert len(moved) == 2, [t(i) for i in items]
nw1 = w1
for it in moved: nw1 = nw1.replace(it, "", 1)
def ref_item(title, ref, indent):
    return ('<item identifier="%s">\n<content_type>WikiPage</content_type>\n<workflow_state>unpublished</workflow_state>\n<title>%s</title>\n<identifierref>%s</identifierref>\n<position>0</position>\n<new_tab/>\n<indent>%d</indent>\n<link_settings_json>null</link_settings_json>\n</item>'
            % (gid("item", title), html.escape(title, quote=False), ref, indent))
def divider(mid, name):
    return ('<item identifier="%s">\n<content_type>ContextModuleSubHeader</content_type>\n<workflow_state>unpublished</workflow_state>\n<title>%s</title>\n<position>0</position>\n<new_tab/>\n<indent>0</indent>\n<link_settings_json>null</link_settings_json>\n</item>' % (gid("div", mid, name), name))
def module(key, title, opens, its):
    its = [re.sub(r"<position>\d+</position>", "<position>%d</position>" % (i + 1), x) for i, x in enumerate(its)]
    return ('<module identifier="%s">\n    <title>%s</title><unlock_at>%s</unlock_at>\n    <workflow_state>unpublished</workflow_state>\n    <position>0</position>\n    <require_sequential_progress>false</require_sequential_progress>\n    <locked>false</locked>\n    <items>\n      %s\n    </items>\n  </module>'
            % (gid("module", key), html.escape(title, quote=False), opens, "\n      ".join(its)))
w2_items = [divider("w2", "Study")] + [re.sub(r"<indent>\d+</indent>", "<indent>1</indent>", m) for m in moved] + \
           [ref_item(tt, ids[tt], 1) for wk, tt, _, _ in PAGES if wk == "Week 02"]
w3_items = [divider("w3", "Study")] + [ref_item(tt, ids[tt], 1) for wk, tt, _, _ in PAGES if wk == "Week 03"]
m2 = module("w2", "Week 02: Surround Routing: Sub-Paths and Submixes", "2026-08-31T06:00:00Z", w2_items)
m3 = module("w3", "Week 03: Surround Panning: The 5.1 Panner", "2026-09-07T06:00:00Z", w3_items)
s = s.replace(w1, nw1 + "\n  " + m2 + "\n  " + m3, 1)
open(mm_p, "w", encoding="utf-8").write(s)
print("Week 01 keeps %d item(s); Week 02: %d; Week 03: %d; 6 new pages" % (len(items) - 2, len(w2_items), len(w3_items)))
