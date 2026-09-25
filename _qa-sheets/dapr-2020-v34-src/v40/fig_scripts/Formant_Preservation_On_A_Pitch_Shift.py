import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

# Illustrative vowel "ah": formant peaks near 700, 1220 and 2600 Hz
F = [(700, 130, 0.0), (1220, 150, -6.0), (2600, 220, -16.0)]
def env(f, scale=1.0):
    # spectral envelope in dB, optionally stretched by 'scale' (formants moved)
    lin = np.zeros_like(f, dtype=float)
    for fc, bw, g in F:
        lin += 10 ** (g / 20) / (1 + ((f - fc * scale) / (bw * scale / 2)) ** 2)
    return 20 * np.log10(lin + 10 ** (-40 / 20))

f0 = 220.0
ratio = 2 ** (4 / 12)          # four semitones up
f1 = f0 * ratio                 # about 277 Hz
fx = np.linspace(50, 4000, 3000)
floor = -42

cases = [("Original note: 220 Hz", f0, 1.0, DARK),
         ("Up four semitones WITH formant preservation: harmonics move, peaks stay", f1, 1.0, GREEN),
         ("Up four semitones WITHOUT formant preservation: peaks move up about 26 percent", f1, ratio, ORANGE)]
fig, axes = plt.subplots(3, 1, figsize=(16, 14), dpi=100, sharex=True)
fig.patch.set_facecolor("white")
for ax, (title, fund, sc, col) in zip(axes, cases):
    ax.set_facecolor("white")
    ax.plot(fx, env(fx, sc), color=col, lw=2.4, ls="--", zorder=2)
    h = np.arange(1, 40) * fund
    h = h[h < 4000]
    ax.vlines(h, floor, env(h, sc), color=BLUE, lw=3, zorder=3)
    for fc, _, _ in F:
        ax.axvline(fc * sc, color=col, lw=1.2, alpha=0.5, zorder=1)
        ax.text(fc * sc + 25, 3, "%d Hz" % round(fc * sc), fontsize=17, color=col, va="bottom")
    ax.set_ylim(floor, 12); ax.set_xlim(0, 4000)
    ax.set_yticks([-40, -20, 0])
    ax.tick_params(labelsize=17, colors=DARK)
    ax.set_ylabel("Level (dB)", fontsize=18, color=DARK)
    ax.set_title(title, fontsize=20, color=col, loc="left")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axes[0].text(3950, -12, "Blue lines: harmonics of the note\nDashed curve: formant envelope", ha="right", fontsize=17, color=DARK)
axes[2].set_xlabel("Frequency (Hz)", fontsize=20, color=DARK)
plt.tight_layout()
plt.savefig("/home/claude/q40/fig/Mixing__Tuning/Formant_Preservation_On_A_Pitch_Shift.png", facecolor="white")
print(f1, [round(fc * ratio) for fc, _, _ in F])
