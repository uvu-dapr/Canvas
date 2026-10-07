"""J130: the student PDF of each restyled deck, the way Canvas Preview's Slides > Update makes it (LibreOffice headless from
the Embedded deck; one page per showing slide or the old PDF is kept). export_pdfs_j130.py plan.json"""
import sys, os, json, re, zipfile, subprocess, tempfile, shutil
SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
def counts(p):
    z = zipfile.ZipFile(p); s = [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)]
    hidden = sum(1 for n in s if re.search(r'<p:sld [^>]*show="0"', z.read(n).decode("utf8", "ignore")))
    return len(s), hidden
def pages(pdf):
    out = subprocess.run(["mdls", "-raw", "-name", "kMDItemNumberOfPages", pdf], capture_output=True, text=True).stdout.strip()
    if out.isdigit(): return int(out)
    return len(re.findall(rb"/Type\s*/Page[^s]", open(pdf, "rb").read()))
for e in json.load(open(sys.argv[1])):
    linked = e["deck"]; d, base = os.path.split(linked); emb = os.path.join(d, base.replace("-Linked.pptx", "-Embedded.pptx"))
    out = os.path.join(d, "PDF", base.replace("-Linked.pptx", ".pdf"))
    if not os.path.exists(emb): print("NO EMBEDDED", base, flush=True); continue
    tmp = tempfile.mkdtemp()
    subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", tmp, emb], capture_output=True, timeout=600)
    made = os.path.join(tmp, os.path.basename(emb)[:-5] + ".pdf")
    if not os.path.exists(made): print("FAILED", base, flush=True); shutil.rmtree(tmp); continue
    all_, hid = counts(emb); got = pages(made)
    if got not in (all_, all_ - hid): print("PAGE MISMATCH kept old", base, got, all_, hid, flush=True); shutil.rmtree(tmp); continue
    os.makedirs(os.path.dirname(out), exist_ok=True); shutil.move(made, out); shutil.rmtree(tmp)
    print("ok", base, got, flush=True)
