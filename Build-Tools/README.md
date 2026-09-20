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
| `british_spelling_check.py` | US spelling sweep. Takes a path, walks html, xml, md, txt and csv |
| `fall_2026_spine.py` | Fall 2026 term dates. Exports `W`, `due_fridays()` and `zulu()` |
| `spring_2027_spine.py` | Spring 2027 term dates, same interface. Daylight saving runs the other way |

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

## When you add a check

Add it here, and add a row to the table in Platform Reference 21.1d in the same session.
A defect that lives only in a chat transcript comes back in the next course.

**Never count, always resolve.** A check that counts tokens, files or attributes proves
nothing. Resolve every reference against the thing it names, and after you change the
shape of the data, confirm the checker still sees it. A check that fails loudly is doing
its job. One that passes quietly may not be looking.
