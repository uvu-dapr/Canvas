# DAPR Build Tools

Canonical home, as of 2026-09-20. **Edit these files here and commit. Nothing else.**

They used to live in Dropbox at
`Reference Files/Applications/AI Projects Standards/Work/Utah Valley University/Build Tools/`.
On 2026-09-20 that copy was overwritten twice inside one session by two machines editing it
at the same time, each time silently discarding half the checks. The gate went on printing
`RESULT: PASS` while it had stopped looking at quizzes entirely. A shared file with no
history and no merge is not something a build gate can sit on.

The Dropbox path still works: `preflight.py` there is now a four line shim that runs this
copy, so an old command line or an older prompt keeps working and automatically gets the
current checker. **The shim is not the checker. Editing it changes nothing.**

## The files

| File | What it does |
|---|---|
| `preflight.py` | The build gate. Run it from inside an unzipped `.imscc`. It must print `RESULT: PASS` before anything ships |
| `budget_check.py` | Gate 12j, the Standards §11e credit hour budget. States the course, its credits and lab (Folder Map §3.13) and its model (Standards §11e-1), resolves every graded object from the manifest, and ends with a block to paste to an AI. `preflight.py` imports it, so run either one |
| `british_spelling_check.py` | US spelling sweep. Takes a path, walks html, xml, md, txt and csv |
| `fall_2026_spine.py` | Fall 2026 term dates. Exports `W`, `due_fridays()` and `zulu()` |
| `spring_2027_spine.py` | Spring 2027 term dates, same interface. Daylight saving runs the other way |
| `module_order.py` | Every module in Adam's order (DAPR Canvas Standards 6.9): readings, then assignments, then the quiz; one heading pair; graded items named "Topic: Assignment - Name" and "Topic: Quiz - Name". `plan` writes a JSON plan (Canvas Preview ▸ Workbench ▸ Module Order shows it side by side and lets Adam adjust it); `apply` writes a plan into an unzipped working copy and stops without writing if a module does not match. Work students took is listed to rename by hand, never renamed by a package |
| `live_preview.py` | The live course after a LIVE-Import, before Adam imports it (DAPR Canvas Standards 16a): each module live now (the newest Canvas export), after the import, and what stays in Canvas, with new items, renames, moves, due date and point changes, new page words and picture links marked. Plays the import the Canvas way: file order, nothing deleted, work students took placed and never replaced. `--html` writes a web page, `--json` the data; Canvas Preview ▸ Compare ▸ Live Course: After the Import shows it |
| `match_ids.py` | The ids Canvas stored for each live item (DAPR Canvas Standards 16a, Platform Reference 23.1): an export labels items with a hash of their own database id, but an import matches only the id an item was created under. `plan <package> <export> <class folder>` reads the older packages (made before the export) for each live item's stored id; `apply` writes the next version with them, keeps live grading weights, leaves out modules whose taken work can't be linked, carries untaken originals from the export, and leaves unsure groups alone; `stored <export>` lists every stored id. Canvas Preview runs it (Report, Workbench ▸ Use the IDs Canvas Matches, Give Items Their Live IDs); preflight 12k and cartridge-gate use it |
| `deck_pair.py` | Every teaching deck as `<Base>-Linked.pptx` (teaching pictures linked by relative path from `Presentations/Images/<Base>-<Subject>.<ext>`, reference slides at the end) and `<Base>-Embedded.pptx` (built from it, pictures inside), DAPR Canvas Standards 8 "Linked and Embedded pair". `split`, `embed`, `status`, `verify`, `clean`. Design marks (icons, checkmarks, warnings, master pictures) stay inside both decks. Canvas Preview ▸ Slides runs it (Update, Update All ⇧⌃⌘E, Make Linked and Embedded ⇧⌃⌘L) |
| `deck_names.py` | The naming rules for decks and deck pictures: a deck keeps its name minus module numbers, lesson, part and week numbers, years, course codes, counters and run-together words; a picture is `<Base>-<Subject>` from its alt text or slide title, never generic or numbered |
| `deck_picture_text.json` | Alt text and file name subjects written by looking at each deck picture whose alt text was empty, a file name, PowerPoint's automatic text or a shop page title (242 on 2026-09-30), keyed by the picture's SHA-1; `deck_pair.py` puts them into the decks |
| `merge_decks.py` | Two decks of one lecture become one: the newer deck whole, plus the older slides a plan places, in the newer look (footer, title, Part dividers, page numbers; a slide from another design rebuilt as title, bullets and pictures in their arrangement), with fact fixes, American spelling and no dashes. Plans and reports: `Deck Merge Report <date>.md` in each course's Presentations folder |
| `relink_slides.py` | A package's slide PDF links brought up to the decks in Canvas Links: a renamed deck's link and title follow its new name, the older deck of a merged pair loses its item (and any page download link), and a deck nothing links gets a `<Topic>: Slides - <Title> (PDF)` item. Items keep their identifiers, so a LIVE-Import updates them; removed items stay in the live course until deleted by hand |
| `live_import.py` | Makes a LIVE-Import: a package for a course already running, in which every item Canvas already has carries its live identifier, so importing updates it instead of adding a second copy. See "Live imports" below |

## Running the gate

Build, zip, unzip the zip **somewhere else**, then run it there. Never in the folder you
built in: a stale or orphaned file there passes and still ships.

```
python3 "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Build-Tools/preflight.py"
```

Two environment variables change what it checks:

| Variable | Effect |
|---|---|
| `DAPR_COURSE_FOLDER` | The course's repo folder name, for example `DAPR-2255--Audio_Hardware_I`. Turns on the cross course image check and the filename prefix check |
| `DAPR_PREFLIGHT_NO_NET` | Skips the live link check. Use it for a fast pass; never for the run that ships |

## Live imports (2026-09-28)

A course that is already running is updated with a LIVE-Import, never with a fresh package, because Canvas matches
imported items by identifier (Platform Reference 23.1).

```
python3 live_import.py --pkg <full package> --export <today's Canvas export> --out <next free ...-LIVE-Import-...imscc> --work <empty scratch folder>
    [--tiebreak <an earlier LIVE-Import>] [--rename "package title=>live title"] [--rename "module:package=>live"]
    [--outline <full package>]   # when --pkg is an earlier LIVE-Import that already left items out
    [--no-restructure]           # the old behaviour: drop the module items of work left out
```

- **Restructure (the default):** the course is rebuilt to its outline as if from the first day. New modules for past
  weeks come in unpublished.
- **What is left out:** anything students have taken or can submit. That means a quiz they reached, a published
  assignment that is open or past due, and a published discussion.
- **Left out means never replaced:** grades and submissions are untouched. The module item stays, so Canvas finds the
  live item by its id and places it in the correct module (checked in Canvas's `context_module_importer.rb`).
- **The report:** `<out>.report.json` lists:
  - the work students took and where it now sits, with any point difference;
  - old modules (course, Blueprint or instructor, and whether each is safe to delete);
  - old pages the outline no longer uses.

Gate a LIVE-Import against the same export:

```
python3 cartridge-gate.py <zip> <fresh unzip> --live <export>      # (the gate lives in the standards Build Tools folder)
python3 preflight.py . --live <export>                              # run inside the fresh unzip
```

With `--live`, three things the template rules forbid pass, and only when the live course agrees:

- an item published in Canvas stays published;
- a module item or link may point at a live item that isn't in the package;
- the course total without the taken items is a warning, not a failure.

Gate 12k fails on any item that would arrive as a second copy. An old live module that only shares a title with a
module the package updates and renames is listed as "old copies to delete", a warning.

**Before calling a LIVE-Import ready,** open every outside link: Canvas Preview, Go, Check Web Links in Every Class
(Control Option Command E). The gates only check links inside the package.

## When you add a check

Add it here, and add a row to the table in Platform Reference 21.1d in the same session.
A defect that lives only in a chat transcript comes back in the next course.

**Never count, always resolve.** A check that counts tokens, files or attributes proves
nothing. Resolve every reference against the thing it names, and after you change the
shape of the data, confirm the checker still sees it. A check that fails loudly is doing
its job. One that passes quietly may not be looking.
