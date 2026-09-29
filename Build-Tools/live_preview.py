#!/usr/bin/env python3
"""live_preview.py: what a LIVE-Import will do to the running course, module by module (Adam, 2026-09-29).

    python3 live_preview.py <LIVE-Import .imscc> <Canvas export .imscc of the live course> [--report <.report.json>]
                            [--json out.json] [--html out.html]

For every module: the live course now, the module after the import, and what stays in Canvas that the package does
not touch. It follows how Canvas imports (context_module_importer.rb): module items are numbered in the order they
appear in the package, an item already in Canvas is matched by its identifier and updated, an import never deletes
anything, and a module already published stays published. Work students took is left out of a LIVE-Import and only
placed, so it keeps its name, points and grades. DAPR Canvas Standards 16a.
"""
import sys, re, os, json, zipfile, html, hashlib

def zread(z, n):
    try: return z.read(n).decode("utf-8", "ignore")
    except KeyError: return None

def tag(s, t):
    m = re.search(r"<%s>([^<]*)</%s>" % (t, t), s or "")
    return html.unescape(m.group(1)).strip() if m else None

def load(path):
    z = zipfile.ZipFile(path)
    man = zread(z, "imsmanifest.xml") or ""
    res = {m.group(1): re.findall(r'href="([^"]+)"', m.group(0)) for m in re.finditer(r'(?s)<resource identifier="([^"]+)"[^>]*>.*?</resource>', man)}
    objs = {}
    for rid, files in res.items():
        o = {}
        for f in files:
            if f.endswith("assignment_settings.xml"):
                s = zread(z, f) or ""
                o = dict(kind="assignment", title=tag(s, "title"), points=tag(s, "points_possible"), due=(tag(s, "due_at") or "")[:10], state=tag(s, "workflow_state"))
            elif f.endswith("assessment_meta.xml"):
                s = zread(z, f) or ""
                o = dict(kind="quiz", title=tag(s, "title"), points=tag(s, "points_possible"), due=(tag(s, "due_at") or "")[:10], state=tag(s, "workflow_state") or ("published" if tag(s, "available") == "true" else "unpublished"))
            elif f.startswith("wiki_content/") and f.endswith(".html"):
                s = zread(z, f) or ""
                body = re.sub(r"(?s)^.*?<body[^>]*>|</body>.*$", "", s)
                o = dict(kind="page", title=html.unescape((re.search(r"<title>([^<]*)", s) or [0, ""])[1]).strip(),
                         state=(re.search(r'name="workflow_state" content="([^"]+)"', s) or [0, "active"])[1],
                         # the words, and the picture files, separately (Canvas rewrites HTML on export, so raw HTML always differs)
                         body=hashlib.md5(re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", body))).strip().encode()).hexdigest(),
                         imgs=sorted(set(x.split("?")[0] for x in re.findall(r'<img[^>]+src="([^"]+)"', body))))
        if o: objs[rid] = o
    mm = zread(z, "course_settings/module_meta.xml") or ""
    mods = []
    for m in re.finditer(r'(?s)<module identifier="([^"]+)">(.*?)</module>', mm):
        head = m.group(2).split("<items>")[0]
        items = []
        for i in re.finditer(r'(?s)<item identifier="([^"]+)">(.*?)</item>', m.group(2)):
            b = i.group(2)
            items.append(dict(id=i.group(1), title=tag(b, "title") or "", type=tag(b, "content_type") or "", ref=tag(b, "identifierref"), url=tag(b, "url")))
        mods.append(dict(id=m.group(1), title=tag(head, "title") or "", state=tag(head, "workflow_state") or "active",
                         position=int(tag(head, "position") or 0), unlock=(tag(head, "unlock_at") or "")[:10], items=items))
    return dict(mods=mods, objs=objs, res=res)

KIND = {"WikiPage": "Page", "Assignment": "Assignment", "Quizzes::Quiz": "Quiz", "DiscussionTopic": "Discussion",
        "ExternalUrl": "Link", "Attachment": "File", "ContextModuleSubHeader": "Heading", "ContextExternalTool": "Tool"}

def preview(pkg, export, report=None):
    P, L = load(pkg), load(export)
    taken = set()
    rep = report or pkg + ".report.json"
    if os.path.exists(rep):
        taken = {t.get("title") for t in json.load(open(rep)).get("taken_items", [])}
    live_mod = {m["id"]: m for m in L["mods"]}
    live_item = {i["id"]: (m, i) for m in L["mods"] for i in m["items"]}
    pkg_item_ids = {i["id"] for m in P["mods"] for i in m["items"]}
    out = {"package": os.path.basename(pkg), "export": os.path.basename(export), "modules": [], "stays": [],
           "counts": dict(new_modules=0, updated_modules=0, items_new=0, items_updated=0, renamed=0, points=0, dates=0, pages_text=0, placed=0, stay_items=0, stay_modules=0)}
    c = out["counts"]
    for m in sorted(P["mods"], key=lambda m: m["position"] or 999):
        lm = live_mod.get(m["id"])
        mod = dict(id=m["id"], title=m["title"], status="new" if not lm else "updated", live_title=lm["title"] if lm else None,
                   live_state=lm["state"] if lm else None, pkg_state=m["state"], unlock=m["unlock"], live=[], after=[], stays=[], notes=[])
        c["new_modules" if not lm else "updated_modules"] += 1
        if lm:
            mod["live"] = [dict(title=i["title"], kind=KIND.get(i["type"], i["type"])) for i in lm["items"]]
            if lm["title"] != m["title"]: mod["notes"].append("Module renamed from \"%s\"." % lm["title"])
            if lm["state"] == "active" and m["state"] == "unpublished":
                mod["notes"].append("Published in Canvas now, and it stays published: an import cannot unpublish a module.")
        for i in m["items"]:
            k = KIND.get(i["type"], i["type"]); po = P["objs"].get(i["ref"] or ""); was = live_item.get(i["id"])
            e = dict(title=i["title"], kind=k, marks=[])
            lo = L["objs"].get((was[1]["ref"] if was else i["ref"]) or "")
            if i["ref"] and not po and i["type"] in ("Assignment", "Quizzes::Quiz", "DiscussionTopic", "WikiPage") and (lo or i["title"] in taken):
                e["marks"].append("placed: students took it, so it is never replaced (name, points and grades stay)"); c["placed"] += 1
            elif not was:
                e["marks"].append("new"); c["items_new"] += 1
            else:
                if was[0]["id"] != m["id"]: e["marks"].append("moves here from \"%s\"" % was[0]["title"])
                if was[1]["title"] != i["title"]: e["marks"].append("renamed from \"%s\"" % was[1]["title"]); c["renamed"] += 1
                if po and lo:
                    if po.get("points") and lo.get("points") and float(po["points"]) != float(lo["points"]):
                        e["marks"].append("points %g to %g" % (float(lo["points"]), float(po["points"]))); c["points"] += 1
                    if po.get("due") != lo.get("due") and (po.get("due") or lo.get("due")):
                        e["marks"].append("due %s to %s" % (lo.get("due") or "none", po.get("due") or "none")); c["dates"] += 1
                    if po.get("body") and lo.get("body") and po["body"] != lo["body"]:
                        e["marks"].append("page text updated"); c["pages_text"] += 1
                    if po.get("kind") == "page" and lo.get("kind") == "page" and po.get("imgs") != lo.get("imgs"):
                        same = sorted(os.path.basename(x) for x in po.get("imgs", [])) == sorted(os.path.basename(x) for x in lo.get("imgs", []))
                        e["marks"].append("pictures now load from the module's own folder" if same else "pictures changed"); c["pictures"] = c.get("pictures", 0) + 1
                if e["marks"]: c["items_updated"] += 1
            mod["after"].append(e)
        if lm:
            here = {i["id"] for i in m["items"]}
            for i in lm["items"]:
                if i["id"] not in here and i["id"] not in pkg_item_ids:
                    mod["stays"].append(dict(title=i["title"], kind=KIND.get(i["type"], i["type"]))); c["stay_items"] += 1
        out["modules"].append(mod)
    pkg_mod_ids = {m["id"] for m in P["mods"]}
    for lm in L["mods"]:
        if lm["id"] not in pkg_mod_ids:
            out["stays"].append(dict(title=lm["title"], published=lm["state"] == "active", items=len(lm["items"]))); c["stay_modules"] += 1
    return out

def e(s): return html.escape(str(s).replace("–", "-").replace("—", "-"), quote=True)

def to_html(o, title):
    c = o["counts"]
    css = (":root{--bg:#f6f7f8;--card:#fff;--ink:#1f2328;--sub:#57606a;--line:#d0d7de;--acc:#0d47a1;--new:#1b5e20;--chg:#8a5a00;--warn:#b71c1c}"
           "@media (prefers-color-scheme: dark){:root:not([data-theme=\"light\"]){--bg:#161b22;--card:#1f242c;--ink:#e6edf3;--sub:#9da7b3;--line:#30363d;--acc:#79b8ff;--new:#7ee787;--chg:#e3b341;--warn:#ff7b72}}"
           "body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 -apple-system,system-ui,sans-serif}main{max-width:1280px;margin:0 auto;padding:22px 16px 60px}"
           "h1{margin:0 0 4px;font-size:1.5em}.sub{color:var(--sub)}.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:14px 0}"
           ".card h2{margin:0 0 2px;font-size:1.15em}.cols{display:grid;grid-template-columns:1fr 1.25fr 0.9fr;gap:14px}@media(max-width:800px){.cols{grid-template-columns:1fr}}"
           ".it{padding:3px 0;border-top:1px solid var(--line);font-size:14px}.k{color:var(--sub);font-size:11px;margin-right:6px;text-transform:uppercase;letter-spacing:.03em}"
           ".m{display:inline-block;font-size:11.5px;margin:1px 4px 1px 0;padding:1px 6px;border-radius:9px;background:rgba(127,127,127,.15)}.m.new{color:var(--new);font-weight:700}.m.chg{color:var(--chg);font-weight:700}.m.placed{color:var(--acc)}"
           ".badge{font-size:12px;padding:2px 8px;border-radius:9px;margin-left:8px}.b-new{background:rgba(46,160,67,.2)}.b-upd{background:rgba(13,71,161,.12)}"
           ".sum{display:flex;gap:16px;flex-wrap:wrap}.sum div{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:8px 12px}.sum b{font-size:1.3em;display:block}"
           "h3{font-size:.85em;margin:6px 0;color:var(--sub);text-transform:uppercase;letter-spacing:.04em}.note{color:var(--warn);font-weight:600;font-size:13.5px}")
    h = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{e(title)}</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>{css}</style></head><body><main>'
    h += f"<h1>{e(title)}</h1><p class='sub'>Live course now: <b>{e(o['export'])}</b> · what you import: <b>{e(o['package'])}</b>. Read only: nothing is changed by this page.</p>"
    h += "<div class='sum'>" + "".join(f"<div><b>{v}</b>{e(t)}</div>" for v, t in [
        (c["new_modules"], "new modules"), (c["updated_modules"], "modules updated"), (c["items_new"], "new items"), (c["items_updated"], "items updated"),
        (c["renamed"], "renamed"), (c["points"], "points change"), (c["dates"], "due dates change"), (c["pages_text"], "pages with new words"), (c.get("pictures", 0), "pages with new picture links"),
        (c["placed"], "placed, never replaced"), (c["stay_items"] + c["stay_modules"], "things that stay in Canvas")]) + "</div>"
    h += ("<div class='card'><h2>How to read this</h2><ul class='sub'><li><b>Live now</b>: the module in your latest Canvas export.</li>"
          "<li><b>After the import</b>: the module in the order Canvas will set, each item marked <span class='m new'>new</span> or with what changes "
          "(<span class='m chg'>renamed</span>, points, due date, page text); unmarked items are already in Canvas and unchanged.</li>"
          "<li><b>Stays in Canvas</b>: live items the package does not touch. An import never deletes, so these remain until you delete them (old copies, old headings).</li></ul></div>")
    for m in o["modules"]:
        b = "<span class='badge b-new'>new module</span>" if m["status"] == "new" else "<span class='badge b-upd'>updated</span>"
        h += f"<div class='card'><h2>{e(m['title'])}{b}</h2><p class='sub'>{'Opens ' + e(m['unlock']) + ' · ' if m['unlock'] else ''}{'arrives unpublished' if m['pkg_state'] == 'unpublished' and m['status'] == 'new' else ('published in Canvas' if m['live_state'] == 'active' else ('unpublished in Canvas' if m['live_state'] else 'published'))}</p>"
        h += "".join(f"<p class='note'>{e(n)}</p>" for n in m["notes"])
        live = "".join(f"<div class='it'><span class='k'>{e(i['kind'])}</span>{e(i['title'])}</div>" for i in m["live"]) or "<p class='sub'>Not in Canvas yet.</p>"
        def mark(x):
            cls = "new" if x == "new" else ("placed" if x.startswith("placed") else "chg")
            return f"<span class='m {cls}'>{e(x)}</span>"
        after = "".join(f"<div class='it'><span class='k'>{e(i['kind'])}</span>{e(i['title'])}<div>{''.join(mark(x) for x in i['marks'])}</div></div>" for i in m["after"])
        stays = "".join(f"<div class='it'><span class='k'>{e(i['kind'])}</span>{e(i['title'])}</div>" for i in m["stays"]) or "<p class='sub'>Nothing extra.</p>"
        h += f"<div class='cols'><div><h3>Live now</h3>{live}</div><div><h3>After the import</h3>{after}</div><div><h3>Stays in Canvas</h3>{stays}</div></div></div>"
    if o["stays"]:
        h += "<div class='card'><h2>Modules the package does not touch (they stay)</h2><p class='sub'>Blueprint modules stay on purpose; old course modules are on your delete list.</p>"
        h += "".join(f"<div class='it'>{e(s['title'])} <span class='sub'>({s['items']} items, {'published' if s['published'] else 'unpublished'})</span></div>" for s in o["stays"]) + "</div>"
    return h + "</main></body></html>"

def main():
    a = sys.argv[1:]
    if len(a) < 2: print(__doc__); sys.exit(2)
    opt = lambda k: a[a.index(k) + 1] if k in a else None
    o = preview(a[0], a[1], opt("--report"))
    if opt("--json"): json.dump(o, open(opt("--json"), "w"), indent=1)
    if opt("--html"):
        name = re.sub(r"-LIVE-Import.*$", "", o["package"]).replace(".imscc", "")
        open(opt("--html"), "w", encoding="utf-8").write(to_html(o, "Live course preview: " + name))
    if not opt("--json") and not opt("--html"): print(json.dumps(o, indent=1))
    else: print(json.dumps(o["counts"]))

if __name__ == "__main__":
    main()
