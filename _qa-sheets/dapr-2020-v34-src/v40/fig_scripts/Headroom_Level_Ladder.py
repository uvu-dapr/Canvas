import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

YMIN, YMAX = -12.5, 2.0
ax.set_ylim(YMIN, YMAX)
ax.set_xlim(0, 16)

# dB guide lines every 1 dB, labelled every 2 dB
for db in range(-12, 1):
    ax.axhline(db, color=GUIDE, lw=0.8, zorder=0)
ax.set_yticks(list(range(-12, 1, 2)))
ax.set_yticklabels([str(v) if v != 0 else "0" for v in range(-12, 1, 2)], fontsize=20, color=DARK)
ax.set_ylabel("Peak level (dB relative to full scale)", fontsize=20, color=DARK)
ax.set_xticks([])
for s in ["top", "right", "bottom"]:
    ax.spines[s].set_visible(False)
ax.spines["left"].set_color(DARK)

# Full scale line and clipping zone
ax.axhline(0, color=ORANGE, lw=3, zorder=3)
ax.add_patch(Rectangle((0, 0), 16, YMAX, color=ORANGE, alpha=0.10, zorder=1))
ax.text(8.0, 1.0, "Above 0 dBFS: clipping", ha="center", va="center", fontsize=22, color=ORANGE, fontweight="bold")
ax.text(15.9, 0.15, "0 dBFS full scale", ha="right", va="bottom", fontsize=20, color=ORANGE)

# Bar 1: mix to mastering, peaks near -6 dBFS
x1, w = 0.6, 3.5
ax.add_patch(Rectangle((x1, YMIN), w, -6 - YMIN, color=BLUE, alpha=0.85, zorder=2))
ax.plot([x1 - 0.3, x1 + w + 0.3], [-6, -6], color=BLUE, lw=3, zorder=3)
ax.text(x1 + w / 2, -9.3, "Mix sent\nto mastering", ha="center", va="center", fontsize=22, color="white", fontweight="bold")
ax.text(x1 + w / 2, -6.3, "peaks near -6 dBFS", ha="center", va="top", fontsize=18, color="white")

# headroom bracket for the mix
bx = x1 + w + 0.5
ax.annotate("", xy=(bx, 0), xytext=(bx, -6), arrowprops=dict(arrowstyle="<->", color=GREEN, lw=3))
ax.text(bx + 0.25, -3, "about 6 dB of\npeak headroom:\nroom for\nmastering\nto work", ha="left", va="center", fontsize=20, color=GREEN)

# Bar 2: finished master, ceiling about -1 dBTP
x2 = 11.7
ax.add_patch(Rectangle((x2, YMIN), w, -1 - YMIN, color=GREEN, alpha=0.85, zorder=2))
ax.plot([x2 - 0.3, x2 + w + 0.3], [-1, -1], color=GREEN, lw=3, zorder=3)
ax.text(x2 + w / 2, -7.0, "Finished\nmaster", ha="center", va="center", fontsize=22, color="white", fontweight="bold")
ax.text(x2 + w / 2, -1.3, "ceiling about -1 dBTP", ha="center", va="top", fontsize=18, color="white")

# margin bracket for the master
mx = x2 - 0.45
ax.annotate("", xy=(mx, 0), xytext=(mx, -1), arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=3))
ax.text(mx - 0.25, -3.0, "about 1 dB of\nmargin for\ninter-sample\npeaks and\nlossy encoding", ha="right", va="center", fontsize=19, color=ORANGE)

ax.set_title("Two different targets: the mix you deliver and the finished master", fontsize=24, color=DARK, pad=16)
plt.tight_layout()
plt.savefig("/home/claude/q40/fig/Mixing__Master-Buss_Processing_and_Endgame/Headroom_Level_Ladder.png", dpi=100, facecolor="white")
