"""export_tagged for decks with alt text on groups: same profile rules (own profile), same font list, same filter."""
import sys, os, json, subprocess, shutil
BT = "/Users/adamwolson/Library/CloudStorage/Dropbox/apps/GitHub/Canvas/Build-Tools"; sys.path.insert(0, BT); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a11y_files as A
from altlist import altlist
def export_with_group_alt(pptx, outdir):
    prof = os.path.join(A.CACHE, "lo-profile-groupalt"); sd = os.path.join(prof, "user", "Scripts", "python"); os.makedirs(sd, exist_ok=True)
    shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cpvgroupalt.py"), os.path.join(sd, "cpvgroupalt.py"))
    pdf = os.path.join(outdir, os.path.splitext(os.path.basename(pptx))[0] + ".pdf")
    job = dict(deck=os.path.abspath(pptx), pdf=os.path.abspath(pdf), alts=altlist(pptx), result=os.path.join(outdir, "groupalt-result.json"))
    jf = os.path.join(outdir, "groupalt-job.json"); json.dump(job, open(jf, "w"))
    if os.path.exists(job["result"]): os.remove(job["result"])
    env = dict(os.environ, FONTCONFIG_FILE=A.lo_fonts_conf(), CPV_GROUPALT_JOB=jf)
    subprocess.run([A.LO_SOFFICE, "-env:UserInstallation=file://" + prof, "--headless", "--norestore",
                    "vnd.sun.star.script:cpvgroupalt.py$run?language=Python&location=user"], capture_output=True, timeout=900, env=env)
    r = json.load(open(job["result"])) if os.path.exists(job["result"]) else dict(error="no result")
    r["wanted"] = len(job["alts"])
    return (pdf if os.path.exists(pdf) and r.get("ok") else None), r
if __name__ == "__main__":
    print(export_with_group_alt(sys.argv[1], sys.argv[2]))
