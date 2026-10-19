"""LibreOffice Python macro (runs inside soffice). LibreOffice 26.8's PPTX import drops descr on group shapes (p:grpSp),
so their PDF Figure tags come out without alt. Job file (env CPV_GROUPALT_JOB): {"deck", "pdf", "alts": [[slide index over
all slides, group name, alt], ...], "result"}. Gives each named top-level group its alt text, then exports the tagged PDF
with the same filter options as Build-Tools a11y_files.LO_TAGGED."""
import os, json, uno
from com.sun.star.beans import PropertyValue
def _pv(n, v):
    p = PropertyValue(); p.Name = n; p.Value = v; return p
def run(*args):
    job = json.load(open(os.environ["CPV_GROUPALT_JOB"])); res = dict(set=0, notes=[])
    try:
        desk = XSCRIPTCONTEXT.getDesktop()
        doc = desk.loadComponentFromURL(uno.systemPathToFileUrl(job["deck"]), "_blank", 0, (_pv("Hidden", True),))
        pages = doc.getDrawPages()
        for si, name, alt in job["alts"]:
            pg = pages.getByIndex(si); hits = [pg.getByIndex(i) for i in range(pg.getCount())]
            hits = [s for s in hits if s.getName() == name and s.getShapeType() == "com.sun.star.drawing.GroupShape"]
            if len(hits) != 1: res["notes"].append("slide %d %s: %d matches" % (si + 1, name, len(hits))); continue
            if hits[0].Description: res["notes"].append("slide %d %s had %r" % (si + 1, name, hits[0].Description))
            hits[0].Description = alt; res["set"] += 1
        fd = uno.Any("[]com.sun.star.beans.PropertyValue", tuple(_pv(k, v) for k, v in (("UseTaggedPDF", True), ("PDFUACompliance", True),
                     ("ExportBookmarks", True), ("ExportNotes", False), ("ExportNotesPages", False))))
        uno.invoke(doc, "storeToURL", (uno.systemPathToFileUrl(job["pdf"]), (_pv("FilterName", "impress_pdf_Export"), _pv("FilterData", fd))))
        doc.close(True); res["ok"] = True
    except Exception as e:
        res["error"] = "%s: %s" % (type(e).__name__, e)
    json.dump(res, open(job["result"], "w"))
g_exportedScripts = (run,)
