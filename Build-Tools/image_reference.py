#!/usr/bin/env python3
"""
image_reference.py - regenerate a course's Image Reference page from its Images folder.

    python3 image_reference.py /path/to/Classes/DAPR-2255--Audio_Hardware_I

Standards 8.1: the Image Reference is a mandatory build artifact and no cartridge
ships without it. It mirrors Images/ exactly, so it is generated from disk, never
edited by hand. Folders whose name starts with an underscore are working folders
(_briefs, _review, _superseded, _duplicates) and are left out on purpose.
"""
import os, sys, datetime

RAW = "https://raw.githubusercontent.com/uvu-dapr/Canvas/main/Classes/%s/Images/%s/%s"
EXT = (".png", ".jpg", ".jpeg", ".svg", ".webp")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(pretty)s - Image Reference</title>
<style>
body{font-family:Arial,Helvetica,sans-serif;color:#212121;background:#f5f5f5;margin:0;padding:32px 24px 80px}
.wrap{max-width:1250px;margin:0 auto}h1{font-size:1.7em;margin:0 0 4px}
.sub{color:#616161;margin:0 0 24px}
h2{color:#993300;border-bottom:3px solid #993300;padding-bottom:6px;margin:34px 0 14px;font-size:1.2em}
.grid{display:flex;flex-wrap:wrap;gap:14px}
.img-item{background:#fff;border:1px solid #cfd8dc;border-radius:5px;padding:8px;width:216px}
.img-item img{width:200px;height:160px;object-fit:contain;background:#fff;display:block}
.img-item .cap{font-family:"Courier New",Courier,monospace;font-size:11px;color:#424242;
word-break:break-all;margin-top:6px;user-select:all}
</style>
</head>
<body>
<div class="wrap">
<h1>%(pretty)s - Image Reference</h1>
<p class="sub">Generated %(date)s. %(count)d images across %(folders)d topic folders. Mirrors <span style="font-family:monospace">Images/</span> exactly.</p>
"""


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    course_dir = os.path.abspath(sys.argv[1].rstrip("/"))
    course = os.path.basename(course_dir)
    images = os.path.join(course_dir, "Images")
    if not os.path.isdir(images):
        print("no Images folder under " + course_dir)
        return 2

    topics = sorted(d for d in os.listdir(images)
                    if os.path.isdir(os.path.join(images, d)) and not d.startswith("_"))
    body, total = [], 0
    for topic in topics:
        files = sorted(f for f in os.listdir(os.path.join(images, topic))
                       if f.lower().endswith(EXT) and not f.startswith("."))
        if not files:
            continue
        total += len(files)
        body.append('<h2>%s <span style="color:#616161;font-weight:normal;font-size:.8em">(%d)</span></h2>'
                    % (topic, len(files)))
        body.append('<div class="grid">')
        for f in files:
            body.append('<div class="img-item"><img src="%s" alt="%s" loading="lazy">'
                        '<div class="cap">%s</div></div>'
                        % (RAW % (course, topic, f), f, f))
        body.append("</div>")

    pretty = course.replace("--", " ").replace("_", " ").replace("-", " ")
    pretty = " ".join(pretty.split())
    head = HEAD % {"pretty": pretty,
                   "date": datetime.date.today().isoformat(),
                   "count": total,
                   "folders": len(topics)}
    out = os.path.join(course_dir, course + "--Image-Reference.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(head + "\n".join(body) + "\n</div>\n</body>\n</html>\n")
    print("%d images, %d folders -> %s" % (total, len(topics), out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
