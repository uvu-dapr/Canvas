#!/usr/bin/env python3
"""taken_renames.py: work students already took under an old name, and the package's renamed copy of it (Adam, 2026-10-05).

live_import.py leaves out what students have taken when the package has it under the same title. When the package
renamed it since ("Mixing Space" became "Calibration & Monitoring: Assignment - Mixing Space"), the title no longer
matches, the package brings a second copy, and students see the work twice (found by hand for DAPR 2020 v82: 9 items).

A live item is taken when students can reach it: a published assignment or discussion that is open or past due, a quiz
that is available or past due. For each taken item no package item matches by title, the package item of the same kind
that shares the most words (title and body) is its renamed copy, when it shares enough.

    python3 taken_renames.py plan  <package.imscc> <live export.imscc> [--json out.json]
    python3 taken_renames.py apply <package.imscc> <live export.imscc> <out.imscc> [--only "title"]...

apply never overwrites and removes the copies (resource, files, module items); the live item stays where it is, and
Adam moves it into its module by hand (Standards 16a).
"""
import sys, os, re, html, json, zipfile, datetime

TITLE_W, BODY_W, MATCH = 0.4, 0.6, 0.45


def U(s):
    return " ".join(html.unescape(s or "").split())


def words(t):
    t = re.sub(r"(?s)<head.*?</head>", "", t or "")
    return set(re.findall(r"[a-z][a-z']{3,}", html.unescape(re.sub(r"<[^>]+>", " ", html.unescape(t))).lower()))


def tw(t):
    stop = {"assignment", "quiz", "exercise", "the", "and", "for"}
    return {w for w in re.findall(r"[a-z0-9]+", t.lower()) if len(w) > 2 and w not in stop}


def graded(path):
    """identifier -> dict(kind, title, words, reachable, files) for assignments, quizzes and discussions"""
    z = zipfile.ZipFile(path)
    names = set(z.namelist())
    rd = lambda n: z.read(n).decode("utf8", "ignore") if n in names else ""
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M")
    g = lambda x, k: (re.search(r"<%s>([^<]*)</%s>" % (k, k), x) or [None, ""])[1]
    out = {}
    for n in names:
        if n.endswith("/assignment_settings.xml"):
            rid = n.split("/")[0]
            x = rd(n)
            if "<quiz_identifierref>" in x:
                continue     # a quiz's gradebook side: the quiz itself is read below
            body = "".join(rd(m) for m in names if m.startswith(rid + "/") and m.endswith(".html"))
            due, un = g(x, "due_at"), g(x, "unlock_at")
            reach = g(x, "workflow_state") == "published" and (not un or un < now or (due and due < now))
            out[rid] = dict(kind="assignment", title=U(g(x, "title")), words=words(body), reachable=reach)
        elif n.endswith("/assessment_meta.xml"):
            rid = n.split("/")[0]
            x = rd(n)
            due = g(x, "due_at")
            qti = rd("non_cc_assessments/%s.xml.qti" % rid) or rd(rid + "/assessment_qti.xml")
            # published (Canvas exports "available" false for most published quizzes; workflow_state says it), and open
            # or past due; an unpublished quiz past its date was never seen
            reach = "<available>true</available>" in x or g(x, "workflow_state") == "published"
            out[rid] = dict(kind="quiz", title=U(g(x, "title")), words=words(qti), reachable=reach)
    man = rd("imsmanifest.xml")
    for m in re.finditer(r'<resource identifier="([^"]+)" type="imsdt_xmlv1p1"[^>]*>(.*?)</resource>', man, re.S):
        rid = m.group(1)
        f = re.search(r'<file href="([^"]+)"', m.group(2))
        x = rd(f.group(1)) if f else ""
        dep = re.search(r'<dependency identifierref="([^"]+)"', m.group(2))
        meta = rd(dep.group(1) + ".xml") if dep else ""
        if not meta and dep:
            meta = "".join(rd(k) for k in names if k.startswith(dep.group(1)))
        reach = "<workflow_state>active</workflow_state>" in meta
        out[rid] = dict(kind="discussion", title=U(g(x, "title")), words=words(g(x, "text")), reachable=reach)
    return out


def plan(pkg, export):
    P, L = graded(pkg), graded(export)
    ptitles = {(v["kind"], v["title"].lower()) for v in P.values()}
    # a package item whose title live already has is the update of that item, unless that live item is only an
    # unpublished leftover nobody took (then it is still the renamed copy of the taken one)
    ltitles = {(v["kind"], v["title"].lower()) for v in L.values() if v["reachable"]}
    pairs, used = [], set()
    for lid, lv in sorted(L.items(), key=lambda x: x[1]["title"]):
        if not lv["reachable"] or (lv["kind"], lv["title"].lower()) in ptitles:
            continue
        best, bid = 0.0, None
        for pid, pv in P.items():
            if pv["kind"] != lv["kind"] or pid in used or (pv["kind"], pv["title"].lower()) in ltitles:
                continue
            a, b = tw(lv["title"]), tw(pv["title"])
            t = len(a & b) / max(1, len(a | b))
            body = len(lv["words"] & pv["words"]) / max(1, len(lv["words"] | pv["words"])) if lv["words"] and pv["words"] else 0
            s = TITLE_W * t + BODY_W * body
            if lv["kind"] != "quiz" and t >= 0.7 and body >= 0.1:
                s = max(s, MATCH)   # the same name with the topic added ("Mixing Space"): a short page shares few words
            if s > best:
                best, bid = s, pid
        if bid and best >= MATCH:
            used.add(bid)
            pairs.append(dict(kind=lv["kind"], live=lv["title"], live_id=lid, package=P[bid]["title"], rid=bid, share=round(best, 2)))
    return pairs


if __name__ == "__main__":
    cmd, pkg, export = sys.argv[1], sys.argv[2], sys.argv[3]
    ps = plan(pkg, export)
    if cmd == "plan":
        for p in ps:
            print("%-10s %.2f  live %-48s  package copy %s" % (p["kind"], p["share"], p["live"][:48], p["package"]))
        print("%d taken item(s) the package brings again under a new name" % len(ps))
        if "--json" in sys.argv:
            json.dump(ps, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1)
    elif cmd == "apply":
        only = [sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--only"]
        if only:
            ps = [p for p in ps if p["package"] in only or p["live"] in only]
        sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
        import blueprint_copies as bc
        copies = [dict(kind=p["kind"], title=p["package"], file="", slug=None, rid=p["rid"], copies_slug=None) for p in ps]
        bc.apply(pkg, export, sys.argv[4], copies)
        print(json.dumps(dict(out=sys.argv[4], removed=[p["package"] for p in ps]), indent=1))
