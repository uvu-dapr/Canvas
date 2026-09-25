import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

fig, ax = plt.subplots(figsize=(16, 7.2), dpi=100)
fig.patch.set_facecolor("white")
ax.set_xlim(0, 16)
ax.set_ylim(0.4, 7.6)
ax.axis("off")

def box(x, y, w, h, title, body, color, dashed=False):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                       fc="white", ec=color, lw=3.5, ls="--" if dashed else "-")
    ax.add_patch(p)
    ax.text(x + w / 2, y + h - 0.35, title, ha="center", va="top", fontsize=19, color=color, fontweight="bold")
    ax.text(x + w / 2, y + h - 1.25, body, ha="center", va="top", fontsize=18, color=DARK, linespacing=1.35)

def arrow(x1, x2, y):
    ax.add_patch(FancyArrowPatch((x1, y), (x2, y), arrowstyle="-|>", mutation_scale=28, color=DARK, lw=2.5))

y, h, w = 2.7, 3.6, 2.5
xs = [0.05 + i * 2.66 for i in range(6)]
box(xs[0], y, w, h, "All tracks", "and auxes,\nbalanced,\nautomated", DARK)
box(xs[1], y, w, h, "1. Buss\ncompressor", "\non early,\nmix into it;\n1 to 2 dB GR\nis a lot", GREEN)
box(xs[2], y, w, h, "2. Broad EQ", "added last,\nsmall and\nlevel-matched", BLUE)
box(xs[3], y, w, h, "3. Limiter", "only if the\nassignment\nasks; always\nthe last\nprocessor", ORANGE, dashed=True)
box(xs[4], y, w, h, "Meters", "peak and\nloudness;\nchanges\nnothing\nyou hear", DARK)
box(xs[5], y, w, h, "Bounce", "exact\nselection,\nre-import,\nlisten", DARK)
for i in range(5):
    arrow(xs[i] + w + 0.03, xs[i + 1] - 0.03, y + h / 2)

ax.text(8.0, 7.0, "Master buss insert order, top slot first, master fader at unity",
        ha="center", va="center", fontsize=24, color=DARK)

# When each piece goes on
ty = 1.55
ax.plot([xs[1], xs[1] + w], [ty, ty], color=GREEN, lw=34, solid_capstyle="butt")
ax.text(xs[1] + w / 2, ty, "EARLY", ha="center", va="center", fontsize=20, color="white", fontweight="bold")
ax.plot([xs[2], xs[3] + w], [ty, ty], color=BLUE, lw=34, solid_capstyle="butt")
ax.text((xs[2] + xs[3] + w) / 2, ty, "LAST", ha="center", va="center", fontsize=20, color="white", fontweight="bold")
ax.text(xs[4] + 0.1, ty, "after the mix\nalready works", ha="left", va="center", fontsize=20, color=BLUE)
ax.text(xs[0] + w / 2, ty, "When it\ngoes on:", ha="center", va="center", fontsize=20, color=DARK)

plt.savefig("/home/claude/q40/fig/Mixing__Master-Buss_Processing_and_Endgame/Master_Chain_Order.png", dpi=100, facecolor="white")
