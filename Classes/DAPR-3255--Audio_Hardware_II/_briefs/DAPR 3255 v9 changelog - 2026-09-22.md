# DAPR 3255 v9 changelog

2026-09-22

```
/mnt/user-data/outputs/DAPR-3255-Course-Turnkey-v9.imscc
```

1,778,643 bytes. Both gates green on the built tree and again on a fresh unzip of
the shipped file. Hard fails empty, warnings empty.

## 1. Student Essentials came out of the cartridge

You told me the Student Essentials module is maintained live in Canvas and that
none of those pages need to be in the .imscc. The cartridge's Course Orientation
module was carrying its own copy of almost all of it. Ten items are gone.

| Removed from the cartridge | Duplicated |
|---|---|
| MOO: c) Universal Class Policies & Expectations | Essentials: 1A |
| MOO: d) Instructor Information & Office Hours | Essentials: 1C |
| Course Orientation: Quiz - Course Overview, 10 pts | Essentials: 1) Quiz |
| MOO: a) Introduce Yourself, discussion, 5 pts | Essentials: 2A |
| MOO: b) Canvas Student Orientation | Essentials: 2B |
| MOO: c) Update Profile & Notifications | Essentials: 3C |
| Course Orientation: Quiz - Canvas Student Setup, 10 pts | Essentials: 2) Quiz |
| MOO: a) Resources & Links | Essentials: 3A |
| MOO: c) How to Make a PDF | Essentials: 3C |
| MOO: d) Questions, What's Working, and Adjustments | Essentials: 4A and 4B |

Three subheaders went with them: two would have been left empty, and the third
made no sense over a single remaining page.

Course Orientation is now three items, all specific to DAPR 3255 and none of
them available from a shared module:

1. MOO: a) Prerequisites
2. MOO: b) Course Description, Learning Outcomes, and Requirements
3. MOO: c) Build Projects Parts List and Budget

The parts list was lettered b), the same letter as the course description. It is
now c). That is the only rename.

### The 25 points, and why the weights did not move

The two quizzes and the discussion were 10, 10 and 5 points, in the Assignments
group. That group went from 33 items and 825 points to 30 items and 800 points.

Your groups are **weighted**, not point-summed: Attendance 25, Assignments 75,
Diagnostic Quizzes 0, plus the two bonus groups at 5 and 0.5. A weighted group
converts its own points to a percentage before the weight is applied, so the
denominator inside Assignments changing from 825 to 800 does not move anyone's
grade. Assignments is still 75 percent of the course.

So `assignment_groups.xml` is untouched, deliberately. I checked rather than
assumed, and the numbers are in the table above if you want to confirm it.

One observation while I was in there: the Diagnostic Quizzes group has zero items
and zero weight. Harmless, but it is an empty group in your gradebook.

## 2. A 25-point assignment was invisible in its module, in v6, v7 and v8

I found this while verifying the strip, not because a gate caught it.

The module item **Networking: Assignment - Terminate a Working Network Cable**
carried `identifierref` `g92120b5ce39fc9ec68651afea8fac602`. That identifier
appears nowhere in the manifest. The assignment itself is fine and lives in
`g28942079cad3b61b59a18e7263e8f0bc`. On import Canvas cannot resolve the item, so
a 25 point assignment goes missing from the Networking module.

This is not something the strip caused. The same dangling reference is in the v6
build, which means it shipped inside **v6, v7 and v8**. Both gates passed all
three. The real defect is that neither gate had a rule that a module item has to
resolve to a resource the manifest declares. Rule 6 checked the manifest's own
organizations tree; nothing checked `module_meta.xml`, which is what Canvas
actually builds modules from.

Repointed, and preflight now has **rule 6b**. Proved by putting the bad reference
back: the rule fires and hard fails.

## 3. Figure numbers were wrong on 28 pages

Also found during this build, also systemic.

Captions were written from the global image brief, so a picture that was seventh
in the brief got captioned "Figure 7." on a page that holds one picture. A
student reading that page sees Figure 7 beside the only figure on it.

| Page | Was | Now |
|---|---|---|
| electronics-ac-dc-circuits | 2, 3, 2 | 1, 2, 3 |
| electronics-soldering-technique | 4, 1, 2 | 1, 2, 3 |
| electronics-transistor-biasing | 5, 2 | 1, 2 |
| networking-subnet-masks-and-cidr | 4, 3 | 1, 2 |
| networking-protocol-comparison | 1, 8 | 1, 2 |
| networking-cable-construction-rj45 | 3, 4 | 1, 2 |
| networking-multicast-and-igmp | 3, 4 | 1, 2 |
| network-ndi | 7 | 1 |
| networking-layer-4-transport-protocols | 7 | 1 |
| electronics-breadboarding | 6 | 1 |
| networking-clocking-and-ptp | 6 | 1 |
| networking-ipv6-basics-overview | 6 | 1 |
| networking-layer-3-routable-ip-protocols | 6 | 1 |
| networking-smpte-2110 | 6 | 1 |
| plus 14 more single-figure pages | 2 to 5 | 1 |

`electronics-ac-dc-circuits` is the worst of them: it had **two figures both
labelled Figure 2** on the same page.

The wireshark capture page was a twenty ninth case, one figure labelled Figure 6,
which I renumbered to 1 before adding the second figure as 2.

I fixed exactly this defect on the op-amp page in v6 and only there. It was
systemic and I treated it as a one-off. Preflight now has **rule 11b**: every
page's captions must run 1..n. Proved by bumping one caption and watching it fail.

## 4. Alt text over the accessibility cap on six figures

Standards 2 caps alt text at 120 characters. Six `img` tags were over, the worst
at 235. They arrived with the Talkback Box photographs in v6.

I caught one over-long alt then, shortened it, and put an assert in the tool that
placed those figures. That is why the rest went by: the assert guarded only the
figures that one tool wrote. A cap belongs in the gate, not in one writer.

All six rewritten by hand rather than truncated, because a sentence cut off
mid-clause is worse for a screen reader than a short one. Longest is now 99
characters. Preflight has **rule 11c**. Proved by planting a 130 character alt.

## 5. Rule 6.8 narrowed, because Course Orientation is legitimately three pages

6.8 hard fails a student-visible module with fewer than four pages. With
Essentials gone, Course Orientation has three and tripped it.

The wrong fix is to exempt Course Orientation by name. 6.8 exists to catch a
module whose reading is too thin to support the quiz sitting on top of it, so the
real statement is: **a module carrying no graded object at all cannot have
reading too thin to support a quiz, because there is no quiz.** That is a shape
test, not a name test, so the next orientation-shaped module needs no new patch.

Proved both ways: passes now, and fires again the moment a quiz is planted back
into Course Orientation.

## 6. The image recount, 51 prompts down to 11

You asked whether the briefed images were still needed. You were right that they
mostly were not, and the reason was bigger than I expected: **you had already run
47 of the 51 prompts**, in three batches between 00:55 and 01:18 this morning.
Every filename the brief asked for was on disk except the four `wireless/` ones.

I reviewed all 47 by eye before using any of them: four full-resolution reads for
the Group A defect fixes, six for the Group B new subjects, and nine four-up
contact sheets for the 36 Group C restyles. The sheets are in the repo at
`Images/_briefs/_review/`.

**40 approved. 7 sent back. 4 never ran.** The new brief is the 11:

```
/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Classes/DAPR-3255--Audio_Hardware_II/Images/_briefs/ChatGPT Image Creation - DAPR 3255 v8.md
```

### The seven I sent back

| File | What is wrong |
|---|---|
| `electronics-opamp-inverting-vs-noninverting-02.png` | The non-inverting half runs the feedback resistor to the **plus** input, alongside the signal, and leaves the minus input tied only to ground. Positive feedback, no negative feedback. As drawn it latches |
| `electronics-ac-vs-dc-waveform-02.png` | The AC ribbon never crosses below the baseline. It is a unipolar ripple sitting on the plinth. Polarity reversal is the one thing the figure exists to show |
| `electronics-bjt-voltage-divider-bias-02.png` | The lower divider resistor ends on a floating ball terminal instead of ground. The divider has no return path |
| `electronics-filter-alignments-01.png` | In the stopband the slopes are in reverse order: the gentlest alignment falls fastest, the peaking one slowest |
| `ip-addressing-subnet-mask-bit-boundary-02.png` | The third row alternates network, host, network, host. A non-contiguous mask is the exact misconception a boundary figure exists to kill |
| `network-diagnostics-arp-resolution-sequence-02.png` | Geometry right, the mid-air arrow from the `-01` is gone, but red and cyan speckle is scattered across the frame from a botched matte |
| `audio-protocols-protocol-comparison-matrix-02.png` | A grey grid with seven balls on it and two arrows off to the side. No rows, no columns, nothing compared. The `-01` it replaced was more useful |

Their pages keep the `-01` they have today. A wrong new figure is worse than an
old correct one.

### Two things I called wrong and corrected

- I flagged `audio-protocols-aes50-point-to-point-chain-02.png` as broken at the
  last link. At full resolution all three cables are there. **I was wrong.**
  Approved.
- I flagged the bias transistor as a PNP dropped into an NPN circuit. At full
  resolution the emitter arrow points away from the base, so it is an NPN and it
  matches the wiring. **I was wrong about that too.** Only the floating divider
  leg in that figure is real.

Both misreads came off the four-up contact sheets, which downsample to roughly
750 px a cell. Good enough for structure, not good enough for topology. Anything
I claim about wiring or a component symbol now gets a full-resolution read first.

## 7. The 40 approved figures are placed

**32 src moves** from `-01` to the reviewed `-02`, across 32 pages. The `-01`
files stay on disk untouched, per Standards 20.4.

One alt text had to widen with its figure: `electrical-safety-current-path-01`
drew one current path, the `-02` draws two, so the alt now says two.

**Seven new placements**, on pages that had no figure at all:

| Figure | Page |
|---|---|
| `electronics-filter-q-against-bandwidth-01.png` | Electronics: Active Filters, Order, and Q |
| `electronics-parametric-eq-boost-and-cut-01.png` | Electronics: Parametric EQ |
| `electronics-constant-q-against-proportional-q-01.png` | Electronics: Parametric EQ |
| `electronics-frequency-scaling-01.png` | Electronics: Frequency and Component Scaling |
| `ip-addressing-nat-translation-flow-02.png` | Networking: Network Address Translation |
| `network-architecture-qos-dscp-priority-queue-02.png` | Networking: Quality of Service |
| `network-diagnostics-mirror-against-tap-01.png` | Networking: Wireshark Setup and Capture Basics |

NAT and QoS are the two that were pulled from their pages back in v5 and never
put back. They are back.

The cartridge now references 61 distinct images, up from 54, and 35 of those are
the new generation.

### One approved file I did not place

`electronics-solder-joint-macro-01.jpg` is the best single image in the whole
set, a genuinely good photoreal macro of a correct joint. But the soldering page
already carries the DAPR 2255 good-against-cold macro, which shows the same joint
plus the failure it gets judged against. A second joint photograph in that one
section adds nothing. It is also 1,853,216 bytes against a 512,000 cap. Kept on
disk, referenced by nothing. Say the word if you want it on the page and I will
re-encode it and swap the comparison out.

## 8. Four over-budget PNGs fixed losslessly

Standards 20.3 caps a PNG at 1 MB. Four were over. I re-deflated each one at
maximum compression with metadata stripped, and verified with an exact pixel
comparison that nothing changed before replacing anything.

| File | Was | Now | Pixel diff |
|---|---|---|---|
| `electronics-semiconductor-pn-junction-02.png` | 1,216,555 | 1,013,049 | 0 |
| `audio-protocols-ndi-bandwidth-tiers-02.png` | 1,150,781 | 850,612 | 0 |
| `audio-protocols-avb-milan-reserved-bandwidth-02.png` | 1,058,777 | 887,605 | 0 |
| `electronics-breadboard-internal-connections-01.png` | 1,072,054 | 890,709 | 0 |

Same dimensions, same pixels, so these are the same images and keep their
filenames. Nothing was upscaled and nothing was re-rendered.

## 9. Two things I did not change, for you to rule on

- **`networking-wireshark-setup-and-capture-basics`** teaches a capture-naming
  convention with the example `2024-11-FOH-dante-dropout-mDNS-missing.pcap`. The
  date is part of the convention being taught, so it is not the kind of date your
  rule is aimed at, but a 2024 stamp will read as stale to a Spring 2027 student.
  Changing a teaching example is your call, not mine.
- **`audio-protocols-protocol-osi-layer-map-02.png`** is approved and placed, but
  it is four unlabelled slabs for a figure called a layer map, and it is the
  weakest approved image in the set. It is not wrong, so I did not send it back.
  If you want it reworked, say so and I will add a twelfth prompt.

## 10. What is left

1. Run the eleven prompts in brief v8. Four are the `wireless/` folder, which
   does not exist yet and has to be created. Seven are retries.
2. `git add`, `commit`, `push` the image repo. Nothing in the cartridge resolves
   until the `-02` files are pushed, so **the 32 moved figures will show a broken
   box in Canvas until you push.** That is the one thing in this release that
   depends on you.
3. Tell me when the eleven land and I will place them and ship v10.

Still open from before: the catalog description of Dante Level 3 is out of date,
two Bonus-group assignments have no rubric, the Small Bear kit SKU
`KIT-AudHW2-PTB` price is unconfirmed, and the `Final/Final_Exam_-_Study_Guide/`
folder of 32 scraped reference images is still awaiting your disposal decision.
