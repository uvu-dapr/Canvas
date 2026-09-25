import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

t = np.linspace(0, 2.0, 4000)
def voice(start, center, vdepth, vrate, phase):
    y = np.full_like(t, np.nan)
    m = t >= start
    tt = t[m] - start
    y[m] = center + (-120 - center) * np.exp(-tt / 0.05) + vdepth * np.clip((tt - 0.4) / 0.3, 0, 1) * np.sin(2 * np.pi * vrate * tt + phase)
    return y

lead = voice(0.10, 10, 20, 5.5, 0.0)
dbl_before = voice(0.22, 35, 15, 5.0, 1.3)   # 120 ms late, 25 cents sharp of the lead
dbl_after = voice(0.12, 13, 15, 5.0, 1.3)    # aligned within 20 ms, 3 cents from the lead center, own vibrato kept

fig, axes = plt.subplots(1, 2, figsize=(16, 8), dpi=100, sharey=True)
fig.patch.set_facecolor("white")
for ax, dbl, title, col in [(axes[0], dbl_before, "Before: double late and 25 cents sharp of the lead", ORANGE),
                            (axes[1], dbl_after, "After: double tuned and timed to the lead", GREEN)]:
    ax.set_facecolor("white")
    ax.axhline(0, color=DARK, lw=1.6)
    ax.text(0.55, -14, "Grid line (A4)", ha="left", va="top", fontsize=17, color=DARK)
    ax.axhline(10, color=BLUE, lw=1.6, ls=":")
    ax.text(1.98, 64, "Lead center +10 cents", ha="right", va="bottom", fontsize=17, color=BLUE)
    ax.annotate("", xy=(1.9, 11), xytext=(1.9, 62), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.8))
    ax.plot(t, lead, color=BLUE, lw=3.2, label="Lead")
    ax.plot(t, dbl, color=col, lw=3.2, label="Double")
    ax.set_xlim(0, 2.0); ax.set_ylim(-130, 90)
    ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
    ax.set_title(title, fontsize=20, color=col, loc="left")
    ax.set_xlabel("Time (seconds)", fontsize=19, color=DARK)
    ax.tick_params(labelsize=17, colors=DARK)
    ax.legend(loc="lower right", fontsize=18, frameon=False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axes[0].set_ylabel("Cents from A4", fontsize=19, color=DARK)
axes[0].annotate("120 ms late", xy=(0.22, -110), xytext=(0.42, -95), fontsize=18, color=ORANGE,
                 arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2))
plt.tight_layout()
plt.savefig("/home/claude/q40/fig/Mixing__Tuning/Lead_And_Double_Tuning_Before_And_After.png", facecolor="white")
