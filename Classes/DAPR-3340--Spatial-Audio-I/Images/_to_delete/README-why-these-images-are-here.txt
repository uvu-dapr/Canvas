This folder holds images that were on disk but NOT referenced by any page in v8 (DAPR-3340-Course-Turnkey-v8.imscc).

Per-topic subfolders match the topic folders one level up in Images/.

Why an image may end up here:
1) Auto-renamed leftover from Phase 1 image extraction (e.g. multichannel-formats-emerge-01.png).
   Adam's rebuilt pages use different image naming, so the auto-renamed version is a stale duplicate of a properly-named image in the parent topic folder.
2) Chapter-numbered figure (e.g. 1-23ITU51SpeakerLayout.png) that hasn't been referenced by a page yet.
   Adam may add references in a future page update.
3) An image whose reformat pass stripped its reference during the initial rebuild.
   The reformat agent dropped the img tag when reformatting; the image survived on disk.

To restore an image: move it back to Images/<topic>/ and reference it from the appropriate page.
To delete permanently: use Finder to trash whatever you don't want.
