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
