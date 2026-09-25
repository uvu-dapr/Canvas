import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

# One sung note, pitch in cents relative to the target note.
sr = 2000
t = np.arange(0, 2.0, 1 / sr)
center = -20.0
raw = center + (-150 - center) * np.exp(-t / 0.05)                 # scoop from 150 cents below
raw += 30 * np.clip((t - 0.5) / 0.3, 0, 1) * np.sin(2 * np.pi * 5.5 * (t - 0.5))  # vibrato +/-30 cents

def correct(x, tau):
    # correction = (target - pitch) passed through a one-pole smoother with time constant tau
    a = 1 - np.exp(-1 / (sr * tau))
    out = np.empty_like(x); c = 0.0
    for i, v in enumerate(x):
        c += a * ((0.0 - v) - c)
        out[i] = v + c
    return out

fast = correct(raw, 0.002)   # 2 ms
slow = correct(raw, 0.400)   # 400 ms

fig, axes = plt.subplots(2, 1, figsize=(16, 11), dpi=100, sharex=True)
fig.patch.set_facecolor("white")
for ax, y, col, title in [(axes[0], fast, ORANGE, "Fast retune speed (2 ms): scoop removed, vibrato flattened, note snaps to the line"),
                          (axes[1], slow, GREEN, "Slow retune speed (400 ms): scoop and vibrato kept, center drawn onto the note")]:
    ax.set_facecolor("white")
    ax.axhline(0, color=DARK, lw=1.6, zorder=1)
    for c in (-150, -100, -50, 50):
        ax.axhline(c, color=GUIDE, lw=1, zorder=0)
    ax.plot(t, raw, color=GUIDE, lw=3, label="Sung pitch", zorder=2)
    ax.plot(t, y, color=col, lw=3.4, label="After correction", zorder=3)
    ax.set_ylim(-165, 60); ax.set_xlim(0, 2.0)
    ax.set_yticks([-150, -100, -50, 0, 50])
    ax.set_yticklabels(["-150", "-100", "-50", "0 = target", "+50"])
    ax.tick_params(labelsize=18, colors=DARK)
    ax.set_ylabel("Cents from target", fontsize=19, color=DARK)
    ax.set_title(title, fontsize=21, color=col, loc="left")
    ax.legend(loc="lower right", fontsize=18, frameon=False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axes[0].annotate("Scoop gone", xy=(0.02, -8), xytext=(0.15, -110), fontsize=19, color=ORANGE,
                 arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2.2))
axes[1].annotate("Scoop kept", xy=(0.05, -95), xytext=(0.2, -140), fontsize=19, color=GREEN,
                 arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.2))
axes[1].set_xlabel("Time (seconds)", fontsize=20, color=DARK)
plt.tight_layout()
plt.savefig("/home/claude/q40/fig/Mixing__Tuning/Fast_Versus_Slow_Retune_Speed.png", facecolor="white")
m = t > 1.5
print("slow: mean after 1.5 s %.1f, swing +/-%.1f" % (slow[m].mean(), (slow[m].max() - slow[m].min()) / 2))
