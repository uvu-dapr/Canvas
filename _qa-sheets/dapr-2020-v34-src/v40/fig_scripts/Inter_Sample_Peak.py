import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

# A sine at one quarter of the sample rate, sampled 45 degrees away from its peaks.
# Every sample lands at +/- sin(45 deg) of the true peak. Scale so the samples sit exactly at full scale (1.0).
A = np.sqrt(2.0)          # true peak amplitude when samples read 1.0
n = np.arange(0, 13)      # sample numbers
phase = np.pi / 4
samples = A * np.sin(2 * np.pi * n / 4 + phase)
t = np.linspace(0, 12, 2000)
wave = A * np.sin(2 * np.pi * t / 4 + phase)
true_peak_db = 20 * np.log10(A)   # +3.01 dB
assert abs(np.max(np.abs(samples)) - 1.0) < 1e-9

fig, ax = plt.subplots(figsize=(16, 8), dpi=100)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

ax.axhline(0, color=GUIDE, lw=1)
ax.axhline(1, color=ORANGE, lw=2.5, ls="--")
ax.axhline(-1, color=ORANGE, lw=2.5, ls="--")
ax.fill_between(t, 1, wave, where=wave > 1, color=ORANGE, alpha=0.30)
ax.fill_between(t, -1, wave, where=wave < -1, color=ORANGE, alpha=0.30)

ax.plot(t, wave, color=BLUE, lw=3, label="Waveform the converter rebuilds")
ax.vlines(n, 0, samples, color=DARK, lw=1.5)
ax.plot(n, samples, "o", color=DARK, ms=13, label="Stored samples (all read 0.0 dBFS)")

ax.text(12.15, 1.0, "0 dBFS", va="center", ha="left", fontsize=20, color=ORANGE)
ax.text(12.15, -1.0, "0 dBFS", va="center", ha="left", fontsize=20, color=ORANGE)
ax.annotate("true peak +%.1f dBTP" % true_peak_db, xy=(0.5, A), xytext=(2.1, 1.72),
            fontsize=20, color=GREEN, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.5))

ax.set_xlim(-0.3, 13.6)
ax.set_ylim(-1.95, 2.05)
ax.set_xticks(range(0, 13))
ax.tick_params(axis="both", labelsize=18, colors=DARK)
ax.set_yticks([-1.414, -1, 0, 1, 1.414])
ax.set_yticklabels(["-1.41", "-1.00", "0", "1.00", "1.41"])
ax.set_xlabel("Sample number", fontsize=20, color=DARK)
ax.set_ylabel("Amplitude (1.00 = full scale)", fontsize=20, color=DARK)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=18, frameon=False)
plt.tight_layout()
plt.savefig("/home/claude/q40/fig/Mixing__Master-Buss_Processing_and_Endgame/Inter_Sample_Peak.png", dpi=100, facecolor="white")
