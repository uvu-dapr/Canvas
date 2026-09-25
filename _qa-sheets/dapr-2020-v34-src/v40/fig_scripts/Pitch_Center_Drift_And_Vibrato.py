import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

# One held A4, pitch in cents relative to A4. Two seconds long.
t = np.linspace(0, 2.0, 4000)
center = -10.0
# scoop: starts 90 cents flat and settles onto the center in about 0.2 s
scoop = (-90 - center) * np.exp(-t / 0.05)
# vibrato: 5.5 cycles per second, fades in from 0.6 s to 1.0 s, up to +/-30 cents
depth = 30 * np.clip((t - 0.6) / 0.4, 0, 1)
vib = depth * np.sin(2 * np.pi * 5.5 * (t - 0.6))
# drift: the last 0.5 s sags flat by up to 50 cents as the breath runs out
drift = -50 * np.clip((t - 1.5) / 0.5, 0, 1) ** 1.5
pitch = center + scoop + vib + drift

# pitch center = average pitch of the note after the scoop has settled
body = t >= 0.2
pc = pitch[body].mean()

fig, ax = plt.subplots(figsize=(16, 8), dpi=100)
fig.patch.set_facecolor("white"); ax.set_facecolor("white")
ax.set_xlim(0, 2.0); ax.set_ylim(-150, 150)

# semitone rows: row for A4 spans -50..+50 cents
ax.axhspan(-50, 50, color="#E8F5E9", zorder=0)
for b in (-150, -50, 50, 150):
    ax.axhline(b, color=GUIDE, lw=1.2, zorder=1)
for c in (-100, 0, 100):
    ax.axhline(c, color=GUIDE, lw=1, ls=":", zorder=1)
ax.set_yticks([-100, 0, 100])
ax.set_yticklabels(["G#4", "A4", "A#4"], fontsize=22, color=DARK)
ax.set_ylabel("Note grid (one row = one semitone = 100 cents)", fontsize=19, color=DARK)
ax.set_xlabel("Time (seconds)", fontsize=20, color=DARK)
ax.tick_params(axis="x", labelsize=18, colors=DARK)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)

ax.plot(t, pitch, color=BLUE, lw=3.2, zorder=3)
ax.axhline(pc, xmin=0.1, xmax=1.0, color=GREEN, lw=3, ls="--", zorder=4)
ax.text(0.22, pc - 6, "Pitch center: %d cents" % round(pc), ha="left", va="top", fontsize=20, color=GREEN, fontweight="bold")

ax.annotate("Scoop up from below", xy=(0.04, -60), xytext=(0.12, -125), fontsize=20, color=ORANGE,
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2.5))
ax.annotate("Vibrato: about 5.5 cycles\nper second around the center", xy=(1.14, 22), xytext=(0.62, 100), fontsize=20, color=BLUE,
            arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.5))
ax.annotate("Drift: the end sags flat\nas the breath runs out", xy=(1.9, -75), xytext=(1.38, -128), fontsize=20, color=ORANGE,
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2.5))
ax.text(0.01, 3, "A4 note line", fontsize=18, color=DARK, va="bottom")

ax.set_title("One held note: judge the pitch center, not the swing around it", fontsize=24, color=DARK, pad=14)
plt.tight_layout()
plt.savefig("/home/claude/q40/fig/Mixing__Tuning/Pitch_Center_Drift_And_Vibrato.png", facecolor="white")
print("pitch center", pc)
