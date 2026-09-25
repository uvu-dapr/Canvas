import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

# G major phrase: short D4 (62), short E4 (64), long G4 (67) held two seconds. Pitch in MIDI note units.
t = np.linspace(0, 2.8, 5600)
before = np.full_like(t, np.nan)
m = (t >= 0.0) & (t < 0.35); before[m] = 62.0
m = (t >= 0.40) & (t < 0.75); before[m] = 64.15                       # E: 15 cents sharp
m = t >= 0.80
tt = t[m] - 0.80
G_center = 67 - 0.35                                                  # 35 cents flat
scoop = (-1.2 - (-0.35)) * np.exp(-tt / 0.05)                          # scoop up from 120 cents below G
vib = 0.25 * np.clip((tt - 0.4) / 0.3, 0, 1) * np.sin(2 * np.pi * 5.5 * tt)   # +/-25 cents
sag = -0.35 * np.clip((tt - 1.6) / 0.4, 0, 1)                          # last 0.4 s sags a further 35 cents (to 70 flat)
before[m] = G_center + scoop + vib + sag

after = before.copy()
after[m] = (67 - 0.05) + scoop + vib + sag * 0.5                        # center to 5 cents flat, sag halved

fig, ax = plt.subplots(figsize=(16, 8.5), dpi=100)
fig.patch.set_facecolor("white"); ax.set_facecolor("white")
names = {62: "D4", 63: "D#4", 64: "E4", 65: "F4", 66: "F#4", 67: "G4", 68: "G#4"}
for n in names:
    ax.axhline(n, color=GUIDE, lw=1, zorder=0)
ax.set_yticks(list(names)); ax.set_yticklabels(list(names.values()), fontsize=19, color=DARK)
ax.plot(t, before, color=GUIDE, lw=4, ls="--", label="Before", zorder=2)
ax.plot(t, after, color=GREEN, lw=3.2, label="After", zorder=3)
ax.set_xlim(0, 2.8); ax.set_ylim(61.5, 68.3)
ax.set_xlabel("Time (seconds)", fontsize=20, color=DARK)
ax.tick_params(axis="x", labelsize=18, colors=DARK)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.annotate("E: 15 cents sharp, left alone", xy=(0.57, 64.2), xytext=(0.2, 65.3), fontsize=19, color=DARK,
            arrowprops=dict(arrowstyle="->", color=DARK, lw=2))
ax.annotate("G center: 35 cents flat\nmoved to 5 cents flat,\nscoop and vibrato kept", xy=(1.6, 66.95), xytext=(1.0, 67.55), fontsize=19, color=GREEN,
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=2))
ax.annotate("End sag cut about in half", xy=(2.75, 66.55), xytext=(1.85, 65.5), fontsize=19, color=ORANGE,
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2))
ax.legend(loc="lower right", fontsize=19, frameon=False)
ax.set_title("Worked example: one note out of three changed", fontsize=23, color=DARK, pad=12)
plt.tight_layout()
plt.savefig("/home/claude/q40/fig/Mixing__Tuning/Worked_Example_Lead_Phrase_Tuning.png", facecolor="white")
