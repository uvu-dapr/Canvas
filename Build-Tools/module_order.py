#!/usr/bin/env python3
"""module_order.py: every module in the order Adam set on 2026-09-29, and graded items named to match.

    Readings first. Graded work at the very end of each module: assignments, then the quiz. One CONTENT AND
    RESOURCES and one QUIZZES AND ASSIGNMENTS heading per module (no lab sections in any class); a missing one is
    added, and every item under a divider is indented (2026-10-03). Graded items are
    "Topic: Assignment - Name" and "Topic: Quiz - Name", Topic being the prefix the module's own pages use.
    Repeated links in a module are removed. Work students took is never renamed by a package: it is listed for
    Adam to rename by hand. DAPR Canvas Standards 6.9 and 16a.

    python3 module_order.py plan  <package .imscc or folder> [--live <Canvas export .imscc>] [--report <.report.json>] [--out plan.json]
    python3 module_order.py apply <unzipped folder> <plan.json> [--live <Canvas export .imscc>] [--all]
    either one takes --dividers <set> to use another set of divider names (DIVIDER_SETS; the default is 6.9's)

plan prints (or writes) a JSON plan: per module its items now, the new order, removals and renames. Canvas Preview's
Workbench > Module Order shows it side by side and lets Adam adjust it. apply writes a plan into an unzipped package
(a working copy, never the package itself) and stops without writing if any module does not hold exactly the plan's
items. --all also renames work students took (for a full teaching copy, never a LIVE-Import).
"""
import sys, re, os, json, zipfile, html, collections

GRADED = ("Assignment", "Quizzes::Quiz", "DiscussionTopic")
SUB = "ContextModuleSubHeader"
MODULE = [""]

# The module dividers (Canvas text headers), Standards 6.9, in one table so a new set of names is one edit.
# Adam chose set C on 2026-10-03 (Notes and Briefs/2026-10-03 Module Dividers - Options Preview.html):
# STUDY over the readings, PRACTICE over procedure guides, worked examples and the Resources page, GRADED WORK over
# assignments, discussions and the quiz, BONUS (OPTIONAL) and IN CLASS: only where needed, plain part names. Items under
# a divider are indented one level and pages under a part divider two ("I always want to indent the content themselves").
DIVIDER_SETS = {
    "C": dict(content="STUDY", practice="PRACTICE", graded="GRADED WORK", bonus="BONUS (OPTIONAL)", in_class="IN CLASS: ", plain_parts=True),
    "6.9": dict(content="CONTENT AND RESOURCES", practice=None, graded="QUIZZES AND ASSIGNMENTS", bonus=None, in_class=None, plain_parts=False),
    "A": dict(content="CONTENT & RESOURCES", practice=None, graded="GRADED WORK", bonus="BONUS (OPTIONAL)", in_class="IN CLASS: ", plain_parts=True),
}
DIVIDERS = DIVIDER_SETS["C"]
# A PRACTICE page, read from the title after its topic: the student does something step by step (Standards 6.9)
PRACTICE_PAGE = re.compile(r"(?i)\b(procedure|guide|worked example|workflow|walkthrough|step[- ]by[- ]step|scenario|common mistakes|"
                           r"checklist|verifying|exercise|hands[- ]on|try it|practice|how to)\b")
STD = (DIVIDERS["content"], DIVIDERS["graded"])
# Names a divider has had, so a module that uses any of them is recognized and renamed rather than given a second one
KNOWN = dict(content={"content and resources", "content & resources", "study", "learn"}, practice={"practice"},
             graded={"quizzes and assignments", "quizzes & assignments", "graded work", "required"},
             bonus={"bonus", "bonus (optional)"})
IN_CLASS = re.compile(r"(?i)^(?:LECTURE TIME WILL BE USED FOR|IN CLASS:)\s*(.+)$")

def head_kind(t):
    """content, practice, graded, bonus, in_class or part (a custom divider inside the readings, kept with them)."""
    l = t.strip().lower()
    for k, names in KNOWN.items():
        if l in names: return k
    return "in_class" if IN_CLASS.match(t.strip()) else "part"

def head_name(kind, t):
    """The name a divider of this kind carries in the current set (None: keep its own)."""
    if kind in ("content", "graded", "practice"): return DIVIDERS[kind]
    if kind == "bonus": return DIVIDERS["bonus"]
    if kind == "in_class" and DIVIDERS["in_class"]:
        what = IN_CLASS.match(t.strip()).group(1)
        return DIVIDERS["in_class"] + (what.title().replace("'S", "'s") if what.isupper() else what)
    if kind == "part" and DIVIDERS["plain_parts"]:
        p = re.sub(r"^P\d+:\s*", "", t.strip())
        return re.sub(r"(?i)\bmacos\b", "macOS", p.upper().replace(" AND ", " & "))
    return None

def is_practice(x):
    """A page students work through step by step; a Study Guide is study."""
    if x["k"] != "WikiPage": return False
    t = x["t"].split(":", 1)[1] if ":" in x["t"] else x["t"]
    return bool(PRACTICE_PAGE.search(t)) and not re.search(r"(?i)study guide", t)

def is_resource(x):
    """The module's Resources page, or a link or file that is not the slides (it belongs on that page, Standards 6.9)."""
    if x["k"] == "WikiPage": return bool(re.search(r"(?i):\s*resources$", x["t"].strip()))
    return x["k"] in ("ExternalUrl", "Attachment", "ContextExternalTool")

def new_id(mid, kind):
    """A stable identifier for a divider the plan adds, so planning twice gives the same id."""
    import hashlib
    return "g" + hashlib.md5(("divider:%s:%s" % (mid, kind)).encode()).hexdigest()

def indents(order):
    """Indent level for each item in its final order: dividers of the set and the top at 0, everything under a
    divider 1, a part or in-class divider 1, and pages under a part divider 2. order: dicts with k and t."""
    out, under, part = {}, False, False
    for x in order:
        if x["k"] == SUB:
            k = head_kind(x["t"])
            if k in ("content", "practice", "graded", "bonus") or x["t"] in (DIVIDERS["content"], DIVIDERS["practice"], DIVIDERS["graded"], DIVIDERS["bonus"]):
                out[x["id"]] = 0; under, part = True, False
            else:
                out[x["id"]] = 1 if under else 0; part = under and k == "part"
        else:
            out[x["id"]] = (2 if part else 1) if under else 0
    return out

def e(s): return html.escape(s)

def object_titles(z):
    """Assignment, quiz and graded discussion titles by identifier, from their own files (a module item's title can differ)."""
    out = {}
    for n in z.namelist():
        if n.endswith(("/assignment_settings.xml", "/assessment_meta.xml")) or (n.startswith("discussions/") or re.match(r"^[^/]+\.xml$", n)):
            try: s = z.read(n).decode("utf-8", "ignore")
            except KeyError: continue
            m = re.search(r'<(?:assignment|quiz|topicMeta)\b[^>]*\bidentifier="([^"]+)"', s); t = re.search(r"<title>([^<]*)</title>", s)
            if m and t: out[m.group(1)] = html.unescape(t.group(1)); out["file:" + n] = out[m.group(1)]
    # a module item points at a manifest resource, whose files may sit in a folder with another name (3340)
    man = z.read("imsmanifest.xml").decode("utf-8", "ignore")
    for r in re.finditer(r'(?s)<resource identifier="([^"]+)"[^>]*>(.*?)</resource>', man):
        for f in re.findall(r'href="([^"]+)"', r.group(0)):
            if "file:" + f in out: out.setdefault(r.group(1), out["file:" + f])
    return out

def modules(p):
    z = zipfile.ZipFile(p); OT = object_titles(z)
    mm = z.read("course_settings/module_meta.xml").decode("utf-8", "ignore")
    out = []
    for m in re.finditer(r'(?s)<module identifier="([^"]+)">(.*?)</module>', mm):
        t = html.unescape(re.search(r"<title>([^<]*)", m.group(2)).group(1))
        items = []
        for i in re.finditer(r'(?s)<item identifier="([^"]+)">(.*?)</item>', m.group(2)):
            g = lambda k: html.unescape((re.search(r"<%s>([^<]*)" % k, i.group(2)) or [None, ""])[1])
            it = dict(id=i.group(1), k=g("content_type"), t=g("title"), ref=g("identifierref"), url=g("url"), ind=int(g("indent") or 0))
            if it["k"] in GRADED and it["ref"] in OT: it["t"] = OT[it["ref"]]; it["own"] = True
            items.append(it)
        out.append((m.group(1), t, items))
    return out

def _n(s): return re.sub(r"[^a-z0-9]+", " ", s.lower().replace("&", " and ")).strip()

def prefix_of(mt, items):
    """The module's topic prefix. Its own items' prefixes decide; spelled as the module title spells it (with &)."""
    short = mt.split(":", 1)[1].strip() if ":" in mt else mt
    # A graded item already in the right form names the prefix ("Sound: Assignment - The Decibel in the Real World")
    good = collections.Counter(m.group(1).strip() for x in items if x["k"] in GRADED for m in [re.match(r"^([^:]{2,60}): (?:Assignment|Quiz)( - |$)", x["t"])] if m)
    c = collections.Counter()
    for x in items:
        if x["k"] != "WikiPage": continue          # readings decide; slide link titles use the short module name
        m = re.match(r"^([^:]{2,60}):\s", x["t"])
        if m:
            k = m.group(1).strip()
            fam = mt.split(":", 1)[0].strip() if ":" in mt else ""
            if fam and _n(fam).startswith(_n(k)): k = fam          # 3255's "Network:" pages in the "Networking:" family
            c[k] += 1
    if any(_n(k) == _n(short) for k in c): return short, False
    near = [k for k in c if (_n(short) in _n(k) or _n(k) in _n(short)) and len(_n(k)) >= 0.6 * len(_n(short))]
    if near: return max(near, key=lambda k: (c[k], len(k))), False
    if c and c.most_common(1)[0][1] >= 2: return c.most_common(1)[0][0], False
    if good: return good.most_common(1)[0][0], False     # no reading prefixes: a graded item already in the right form
    return short, True

def new_name(x, pre):
    t = x["t"]
    if x["k"] == "Assignment" and re.search(r"^%s: Assignment( - |$)" % re.escape(pre), t): return None
    if x["k"] == "Quizzes::Quiz" and (re.search(r"^%s: Quiz( - |$)" % re.escape(pre), t) or "Final Exam" in t): return None
    if x["k"] == "DiscussionTopic": return None
    # Attendance and Bonus work keep their own forms (Standards 6: "[Normal Name] (Bonus)")
    if re.search(r"(?i)attendance|roll call|\(Bonus\)|^Bonus:", t) or pre.lower().startswith(("optional builds", "bonus")): return None
    kind = "Assignment" if x["k"] == "Assignment" else "Quiz"
    name = t
    if name.startswith(pre + ":"): name = name[len(pre) + 1:].strip()
    fam = re.match(r"^([^:]{2,40}):\s+(.+)$", name)
    if fam and re.match(r"^(Assignment|Quiz)\b", fam.group(2)): name = fam.group(2); fam = None
    name = re.sub(r"^(Assignment|Quiz)\s*-\s*", "", name)
    if fam and not re.match(r"^P\d", fam.group(1)) and (_n(fam.group(1)) in _n(MODULE[0]) or _n(fam.group(1)) in _n(pre)): name = fam.group(2)
    name = re.sub(r"^(Assignment|Quiz)\s*-\s*", "", name)
    name = re.sub(r"^Exercise\s*-\s*(.+)$", r"\1 Exercise", name)      # 3340's "Exercise - Surround Monitoring"
    name = re.sub(r"\s*(Assignment|Quiz)$", "", name).strip(" -:")
    if kind == "Quiz" and name.lower() in ("", pre.lower()): return "%s: Quiz" % pre
    return "%s: %s - %s" % (pre, kind, name) if name else "%s: %s" % (pre, kind)

def plan_module(mt, items, taken, mid=""):
    real = [x for x in items]
    # 1. repeated links (same url or same target) in one module: keep the first
    seen, drop = set(), []
    for x in real:
        key = x["url"] or x["ref"]
        if x["k"] != SUB and key:
            if key in seen: drop.append(x); continue
            seen.add(key)
    keep = [x for x in real if x not in drop]
    # 2. split: the top (items before the first heading, not graded), readings with any custom headings, graded work
    first_h = next((i for i, x in enumerate(keep) if x["k"] == SUB), len(keep))
    slides = lambda x: x["k"] == "ExternalUrl" and re.search(r"Slides\b.*\(PDF\)", x["t"])
    # the overview page ("Topic: Overview", "Topic: Module Overview", "Section Overview"), not a reading whose title
    # ends in Overview ("Dolby Atmos Renderer Interface Overview")
    overview = lambda x: x["k"] == "WikiPage" and re.search(r"(?i)(^|:\s*)((module|section)\s+)?overview$", x["t"].strip())
    top = []                                  # the leading overview and slides, above the first heading if there is one
    if "orientation" not in mt.lower():       # Orientation's pages are all its content
        for x in keep[:first_h]:
            # the first page is the overview only when it is named for the module (3340's "Surround Monitoring" page)
            named_for = x["k"] == "WikiPage" and _n(x["t"]) in (_n(mt), _n(mt.split(":", 1)[-1]))
            if x["k"] in GRADED or not (slides(x) or overview(x) or not top and named_for): break
            top.append(x)
    # every slide deck link belongs at the top with the first one (2255 had its second deck after the quiz)
    top += [x for x in keep if slides(x) and x not in top]
    rest = [x for x in keep if x not in top]
    heads = {k: [x for x in rest if x["k"] == SUB and head_kind(x["t"]) == k] for k in ("content", "practice", "graded", "bonus", "in_class")}
    graded = [x for x in rest if x["k"] in GRADED]
    bonus = [x for x in graded if re.search(r"\(Bonus\)", x["t"])]
    reg = [x for x in graded if x not in bonus]
    readings = [x for x in rest if x["k"] not in GRADED and not (x["k"] == SUB and head_kind(x["t"]) != "part")]
    # a custom heading that only introduced graded work ("P6: Project and Quiz") goes down with it
    tail_heads = []
    while readings and readings[-1]["k"] == SUB:
        tail_heads.insert(0, readings.pop())
    # 3. the dividers (Standards 6.9): reuse the module's own, add what is missing, drop extras
    added, head_ren, extra_heads = [], {}, []
    def one(kind, needed):
        """The module's divider of this kind: its first one (renamed to the set's name), or a new one; extras go."""
        have = heads[kind]
        if kind == "graded":   # "Required" counts only when no real graded divider is there
            have = sorted(have, key=lambda x: x["t"].strip().lower() == "required")
        extra_heads.extend(have[1:])
        if not needed: extra_heads.extend(have[:1]); return None
        name = head_name(kind, have[0]["t"] if have else "")
        if have:
            h = have[0]
            if name and name != h["t"]: head_ren[h["id"]] = name
            return h
        if not name: return None
        h = dict(id=new_id(mid, kind), k=SUB, t=name, ref="", url="", ind=0, new=True)
        added.append(h); return h
    # PRACTICE (set C): procedure guides, worked examples and the like, then the Resources page and any loose links;
    # STUDY keeps the rest with its part dividers. A part divider left with nothing under it goes.
    practice = []
    if DIVIDERS.get("practice"):
        practice = [x for x in readings if is_practice(x)]
        res = [x for x in readings if is_resource(x) and x not in practice]
        if practice: practice += res
        readings = [x for x in readings if x not in practice]
        empty = [h for i, h in enumerate(readings) if h["k"] == SUB and (i + 1 == len(readings) or readings[i + 1]["k"] == SUB)]
        readings = [x for x in readings if x not in empty]; drop += empty
    has_readings = any(x["k"] != SUB for x in readings)
    c_head = one("content", has_readings)
    p_head = one("practice", bool(practice))
    i_head = one("in_class", bool(heads["in_class"]))
    b_needed = bool(bonus) and (bool(DIVIDERS["bonus"]) or bool(heads["bonus"]) and bool(reg))
    b_head = one("bonus", b_needed)
    g_head = one("graded", bool(reg) or (bool(bonus) and not b_head))
    if not b_head: reg, bonus = reg + bonus, []           # no bonus divider: bonus work sits with the rest
    for h in readings:
        if h["k"] == SUB:
            n = head_name("part", h["t"])
            if n and n != h["t"]: head_ren[h["id"]] = n
    def ordered(xs):
        assign = [x for x in xs if x["k"] != "Quizzes::Quiz"]
        quizzes = sorted([x for x in xs if x["k"] == "Quizzes::Quiz"], key=lambda x: "Final Exam" in x["t"])
        return assign + quizzes
    opt = lambda h: [h] if h else []
    if not c_head and i_head and p_head: after_p = [p_head, i_head]     # no STUDY pages: the in-class line leads PRACTICE
    else: after_p = opt(p_head)
    after = top + opt(c_head) + (opt(i_head) if c_head or not p_head else []) + readings + after_p + practice + tail_heads + opt(g_head) + ordered(reg) + opt(b_head) + ordered(bonus)
    drop += extra_heads
    pre, guessed = prefix_of(mt, items); MODULE[0] = mt
    renames = {}
    for x in graded:
        n = new_name(x, pre)
        if n and n != x["t"]: renames[x["id"]] = n
    # moved = the fewest items that really change place: everything outside the longest run kept in the same order
    b = [x["id"] for x in keep if x not in extra_heads]; a = [x["id"] for x in after if not x.get("new")]
    rank = [b.index(i) for i in a]; best = [1] * len(rank); prev = [-1] * len(rank)
    for i in range(len(rank)):
        for j in range(i):
            if rank[j] < rank[i] and best[j] + 1 > best[i]: best[i], prev[i] = best[j] + 1, j
    stay = set(); i = max(range(len(rank)), key=lambda k: best[k]) if rank else -1
    while i >= 0: stay.add(a[i]); i = prev[i]
    moved = set(a) - stay
    named = [dict(x, t=head_ren.get(x["id"], x["t"])) for x in after]
    ind = indents(named)
    reindent = sorted(x["id"] for x in after if not x.get("new") and ind[x["id"]] != x.get("ind", 0))
    return dict(after=after, drop=drop, renames=renames, moved=moved, prefix=pre, guessed=guessed,
                added=added, head_renames=head_ren, indent=ind, reindent=reindent)


def plan_package(pkg, live=None, report=None):
    """The plan for one package (an .imscc or an unzipped folder). report: the LIVE-Import's .report.json, which names
    the work students took (a working folder has none of its own)."""
    src = zip_or_dir(pkg)
    taken = set(); rep = report or pkg + ".report.json"
    if os.path.exists(rep):
        taken = {t.get("title") for t in json.load(open(rep)).get("taken_items", [])}
    liveids = {x["id"] for _, _, its in modules(live) for x in its} if live else set()
    OTL = object_titles(zipfile.ZipFile(live)) if live else {}
    out = {"package": pkg, "live": live, "modules": {}}
    for mid, mt, items in modules(src):
        if "Instructor Use Only" in mt: continue
        p = plan_module(mt, items, taken, mid)
        hand = {x["id"] for x in items if x["id"] in p["renames"] and (x["t"] in taken or OTL.get(x["ref"]) in taken)}
        fromexport = {x["id"] for x in items if x["id"] in p["renames"] and x["id"] not in hand and live and not x.get("own")}
        out["modules"][mid] = dict(
            title=mt, prefix=p["prefix"], guessed=p["guessed"],
            now=[dict(id=x["id"], kind=x["k"], title=x["t"], live=x["id"] in liveids, taken=x["id"] in hand or x["t"] in taken) for x in items],
            order=[x["id"] for x in p["after"]], drop=[x["id"] for x in p["drop"]],
            drop_live=[x["id"] for x in p["drop"] if x["id"] in liveids], moved=sorted(p["moved"]),
            renames={k: v for k, v in p["renames"].items() if k not in hand},
            by_hand={k: v for k, v in p["renames"].items() if k in hand}, from_export=sorted(fromexport),
            added=[dict(id=x["id"], kind=SUB, title=x["t"], live=False, taken=False) for x in p["added"]],
            head_renames=p["head_renames"], indent=p["indent"], reindent=p["reindent"])
    return out

def zip_or_dir(pkg):
    """modules() and object_titles() read a zip; a folder is read through a zip made in memory."""
    if not os.path.isdir(pkg): return pkg
    import io
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for root, _, fs in os.walk(pkg):
            for f in fs:
                if f.endswith((".xml", ".qti")): z.write(os.path.join(root, f), os.path.relpath(os.path.join(root, f), pkg))
    buf.seek(0); return buf


def apply_plan(W, plan, LIVE=None, ALL=False):
    """Writes a plan's order, removals and renames into the unzipped package W. Returns what it did."""
    def rd(p): return open(os.path.join(W, p), encoding="utf-8").read()
    def wr(p, s): open(os.path.join(W, p), "w", encoding="utf-8").write(s)
    def xesc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    def aesc(t): return xesc(t).replace('"', "&quot;")

    mm, man = rd("course_settings/module_meta.xml"), rd("imsmanifest.xml")
    report = {"renamed": [], "removed": [], "copied_from_export": [], "moved_modules": 0, "text_links": 0,
              "dividers_added": [], "dividers_renamed": [], "indented": 0}

    def block_end(s, start, tag="item"):
        """Index just past the </item> matching the <item ...> that opens at start (items nest in the manifest)."""
        depth, i = 0, start
        for m in re.compile(r"<%s\b[^>]*?(/?)>|</%s>" % (tag, tag)).finditer(s, start):
            if m.group(0).startswith("</"): depth -= 1
            elif not m.group(1): depth += 1
            if depth == 0: return m.end()
        raise ValueError("unclosed item")

    renames_all, refs = {}, {}
    RESFILES = {r.group(1): re.findall(r'href="([^"]+)"', r.group(0)) for r in re.finditer(r'(?s)<resource identifier="([^"]+)"[^>]*>.*?</resource>', man)}
    def settings_for(ref, name):
        """The settings file of the object a module item points at: <ref>/<name>, or wherever the manifest puts it."""
        if os.path.exists(os.path.join(W, ref, name)): return ref + "/" + name
        for f in RESFILES.get(ref, []):
            if f.endswith("/" + name) and os.path.exists(os.path.join(W, f)): return f
        return None
    export = zipfile.ZipFile(LIVE) if LIVE else None
    export_man = export.read("imsmanifest.xml").decode("utf-8", "ignore") if export else ""

    for mid, p in plan.items():
        # a module the plan leaves as it is is not touched (its manifest entry may list things differently, harmlessly)
        if not p.get("drop") and not p.get("renames") and not (ALL and p.get("by_hand")) and p["order"] == [x["id"] for x in p.get("now", [])] \
                and not p.get("added") and not p.get("head_renames") and not p.get("reindent"):
            continue
        # ---- module_meta.xml
        m = re.search(r'(?s)<module identifier="%s">.*?</module>' % re.escape(mid), mm)
        assert m, "module %s not in module_meta" % mid
        mod = m.group(0)
        its = {i.group(1): i.group(0) for i in re.finditer(r'(?s)<item identifier="([^"]+)">.*?</item>', mod)}
        want, drop = p["order"], set(p["drop"])
        new_heads = {x["id"]: x["title"] for x in p.get("added", []) if x["id"] not in its}
        assert set(its) == (set(want) - set(new_heads)) | drop and not (set(want) & drop), "module %s items differ from the plan (%s)" % (p["title"], sorted(set(its) ^ ((set(want) - set(new_heads)) | drop))[:4])
        assert set(new_heads) <= set(want), "module %s: a divider the plan adds is not in its order" % p["title"]
        sp = re.search(r"\n([ \t]*)<item identifier", mod); sp = sp.group(1) if sp else "      "
        for iid, t in new_heads.items():      # a divider the plan adds; new items arrive unpublished (Standards 16a, gate 12m)
            its[iid] = ('<item identifier="%s">\n%s  <content_type>%s</content_type>\n%s  <workflow_state>unpublished</workflow_state>\n'
                        '%s  <title>%s</title>\n%s  <position>0</position>\n%s  <new_tab>false</new_tab>\n%s  <indent>0</indent>\n'
                        '%s  <link_settings_json>null</link_settings_json>\n%s</item>') % ((iid, sp, SUB, sp, sp, xesc(t)) + (sp,) * 5)
            report["dividers_added"].append((p["title"], t))
        for iid, t in p.get("head_renames", {}).items():
            if iid in its and iid not in drop:
                its[iid] = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % xesc(t), its[iid], count=1)
                report["dividers_renamed"].append((p["title"], t))
        # indents from the final order and names (Adam may have moved items on the Module Order page)
        final = [dict(id=i, k=re.search(r"<content_type>([^<]*)", its[i]).group(1), t=html.unescape(re.search(r"<title>([^<]*)", its[i]).group(1))) for i in want]
        for iid, n in indents(final).items():
            b = its[iid]
            b2 = re.sub(r"<indent>\d+</indent>", "<indent>%d</indent>" % n, b) if "<indent>" in b else b.replace("</item>", "  <indent>%d</indent>\n%s</item>" % (n, sp))
            if b2 != b: its[iid] = b2; report["indented"] += 1
        ren = dict(p["renames"])                     # by_hand items (students took them) are never renamed by a LIVE-Import
        if ALL: ren.update(p.get("by_hand", {}))      # a full teaching copy carries every new name
        items_xml = []
        for n, iid in enumerate(want, 1):
            b = its[iid]
            b = re.sub(r"<position>\d+</position>", "<position>%d</position>" % n, b)
            if iid in ren:
                b = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % xesc(ren[iid]), b, count=1)
            r = re.search(r"<identifierref>([^<]*)</identifierref>", b)
            if r: refs[iid] = r.group(1)
            items_xml.append(b)
        body = mod[mod.index("<items>") + len("<items>"):mod.index("</items>")]
        indent = re.match(r"\s*", body).group(0) or "\n      "
        new_mod = mod[:mod.index("<items>") + len("<items>")] + indent + indent.join(items_xml) + re.sub(r"^.*?(\s*)$", r"\1", body, flags=re.S) + mod[mod.index("</items>"):]
        mm = mm.replace(mod, new_mod)
        report["moved_modules"] += 1
        for iid in drop: report["removed"].append((p["title"], re.search(r"<title>([^<]*)</title>", its[iid]).group(1)))
        for iid, t in ren.items(): renames_all[iid] = (t, html.unescape(re.search(r"<title>([^<]*)</title>", its[iid]).group(1)))
        # ---- imsmanifest.xml organization: the module's children in the same order
        s = man.find('<item identifier="%s">' % mid)
        if s >= 0:
            e = block_end(man, s); org = man[s:e]
            first = re.search(r"<item identifier=", org[1:])
            if first:
                head_end = first.start() + 1                          # where the first child starts
                sep = re.search(r"(\s*)<item identifier=", org[1:]).group(1)   # the spacing before each child
                kids, k = {}, head_end
                while True:
                    mk = re.compile(r'<item identifier="([^"]+)"').search(org, k)
                    if not mk: break
                    ke = block_end(org, mk.start()); kids[mk.group(1)] = org[mk.start():ke]; k = ke
                closing = org[k:]                                     # spacing and </item> after the last child
                # the manifest's own item ids can differ from module_meta's (2255): match by target, then by title
                byref, bytitle = {}, {}
                for iid in (set(want) - set(new_heads)) | drop:
                    r = re.search(r"<identifierref>([^<]*)</identifierref>", its[iid]); t = re.search(r"<title>([^<]*)</title>", its[iid]).group(1)
                    if r: byref.setdefault(r.group(1), []).append(iid)
                    else: bytitle.setdefault(t, []).append(iid)
                kid_for = {}
                for kid, kb in kids.items():
                    if kid in its: kid_for[kid] = kid; continue
                    r = re.search(r'identifierref="([^"]+)"', kb[:300]); t = re.search(r"<title>([^<]*)</title>", kb).group(1)
                    pool = byref.get(r.group(1), []) if r else bytitle.get(t, [])
                    pool = [x for x in pool if x not in kid_for.values()]
                    assert pool, "manifest item %s matches nothing in the module (%s)" % (kid, t)
                    kid_for[kid] = pool[0]
                kids = {kid_for[k]: v for k, v in kids.items()}
                out = []
                for iid in want:
                    if iid not in kids: continue
                    b = kids[iid]
                    if iid in ren: b = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % xesc(ren[iid]), b, count=1)
                    out.append(b)
                new_org = org[:head_end] + sep.join(out) + closing if out else org[:head_end - len(sep)] + closing
            else:
                new_org = org
            man = man[:s] + new_org + man[e:]
        # ---- removed repeats: a web link used only by the removed item goes too
        for iid in drop:
            r = re.search(r"<identifierref>([^<]*)</identifierref>", its[iid])
            if not r: continue
            ref = r.group(1)
            if mm.count(ref) == 0 and man.count('identifierref="%s"' % ref) == 0:
                rm = re.search(r'(?s)\n?[ \t]*<resource identifier="%s"[^>]*>.*?</resource>' % re.escape(ref), man)
                if rm and "imswl" in rm.group(0):
                    f = re.search(r'href="([^"]+)"', rm.group(0)).group(1)
                    man = man.replace(rm.group(0), "")
                    if os.path.exists(os.path.join(W, f)): os.remove(os.path.join(W, f))

    # ---- live items the package left out unchanged: copy them from the Canvas export so the import can rename them
    for mid, p in plan.items():
        for iid in p.get("from_export", []):
            if iid not in renames_all: continue
            ref = refs.get(iid)
            if not ref or os.path.exists(os.path.join(W, ref)) or ref in RESFILES: continue
            assert export, "a Canvas export is needed to copy %s" % ref
            rm = re.search(r'(?s)<resource identifier="%s"[^>]*>.*?</resource>' % re.escape(ref), export_man)
            assert rm, "%s is not in the Canvas export" % ref
            files = re.findall(r'<file href="([^"]+)"', rm.group(0))
            for f in files + ["non_cc_assessments/%s.xml.qti" % ref]:
                if f in export.namelist():
                    os.makedirs(os.path.dirname(os.path.join(W, f)) or W, exist_ok=True)
                    open(os.path.join(W, f), "wb").write(export.read(f))
            man = man.replace("</resources>", "  " + rm.group(0) + "\n  </resources>", 1)
            report["copied_from_export"].append(renames_all[iid][1])

    # ---- the objects themselves, their page heading, and link text elsewhere
    def replace_text_nodes(s, old, new):
        n = 0
        for o in {old, xesc(old)}:
            pat = ">" + o + "<"
            if pat in s: n += s.count(pat); s = s.replace(pat, ">" + xesc(new) + "<")
        return s, n

    olds = {}
    for iid, (new, old_item) in renames_all.items():
        ref = refs.get(iid)
        old_obj = None
        fa, fq = (settings_for(ref, "assignment_settings.xml"), settings_for(ref, "assessment_meta.xml")) if ref else (None, None)
        if fa:
            f = fa; s = rd(f); ref = os.path.dirname(fa)
            old_obj = html.unescape(re.search(r"<title>([^<]*)</title>", s).group(1))
            wr(f, re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % xesc(new), s, count=1))
            for h in os.listdir(os.path.join(W, ref)):
                if h.endswith(".html"):
                    t = rd(ref + "/" + h); t2, n = replace_text_nodes(t, old_obj, new)
                    t2 = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % xesc(new), t2, count=1)
                    if t2 != t: wr(ref + "/" + h, t2)
        elif fq:
            f = fq; s = rd(f); ref = os.path.dirname(fq)
            old_obj = html.unescape(re.search(r"<title>([^<]*)</title>", s).group(1))
            wr(f, s.replace("<title>%s</title>" % xesc(old_obj), "<title>%s</title>" % xesc(new)))
            for q in (ref + "/assessment_qti.xml", "non_cc_assessments/%s.xml.qti" % ref):
                if os.path.exists(os.path.join(W, q)):
                    s = rd(q); wr(q, re.sub(r'(<assessment [^>]*?\btitle=")[^"]*(")', lambda m: m.group(1) + aesc(new) + m.group(2), s, count=1))
        report["renamed"].append((old_obj or old_item, new))
        for o in {old_obj, old_item} - {None, ""}: olds[o] = new

    # link text on every page: a text node that is exactly an old name
    for root, _, fs in os.walk(W):
        for f in fs:
            if not f.endswith(".html"): continue
            p = os.path.relpath(os.path.join(root, f), W); s = rd(p); s0 = s
            for o, n in olds.items():
                s, k = replace_text_nodes(s, o, n); report["text_links"] += k
            if s != s0: wr(p, s)

    wr("course_settings/module_meta.xml", mm); wr("imsmanifest.xml", man)
    return report


def main():
    a = sys.argv[1:]
    opt = lambda k: a[a.index(k) + 1] if k in a else None
    if opt("--dividers"):                  # try another set of divider names (Adam's choice, 2026-10-03)
        global DIVIDERS, STD
        assert opt("--dividers") in DIVIDER_SETS, "--dividers is one of " + ", ".join(DIVIDER_SETS)
        DIVIDERS = DIVIDER_SETS[opt("--dividers")]; STD = (DIVIDERS["content"], DIVIDERS["graded"])
    if a[:1] == ["plan"] and len(a) > 1:
        p = plan_package(a[1], opt("--live"), opt("--report"))
        js = json.dumps(p, indent=1)
        if opt("--out"): open(opt("--out"), "w").write(js)
        else: print(js)
    elif a[:1] == ["apply"] and len(a) > 2:
        plan = json.load(open(a[2]))
        r = apply_plan(a[1], plan["modules"] if "modules" in plan else plan, opt("--live"), "--all" in a)
        print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in r.items()}))
    else:
        print(__doc__); sys.exit(2)

if __name__ == "__main__":
    main()
