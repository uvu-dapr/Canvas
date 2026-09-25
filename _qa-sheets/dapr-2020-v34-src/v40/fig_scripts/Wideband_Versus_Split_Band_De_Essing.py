import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

f = np.logspace(np.log10(50), np.log10(20000), 2000)
GR = 6.0                      # dB of reduction while an S is present
g = 10 ** (-GR / 20.0)

# Wideband: the whole signal is turned down
wide = np.full_like(f, -GR)
# Split band: Linkwitz-Riley 4th order split at 5 kHz, only the high side is reduced
fc = 5000.0
x = (f / fc) ** 4
lp = 1.0 / (1.0 + x); hp = x / (1.0 + x)
split = 20 * np.log10(lp + g * hp)

fig, axes = plt.subplots(1, 2, figsize=(16, 7.5), dpi=100, sharey=True)
fig.patch.set_facecolor("white")
ticks = [50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
tl = ["50", "100", "200", "500", "1k", "2k", "5k", "10k", "20k"]
for ax, curve, col, title in [(axes[0], wide, ORANGE, "Wideband: the whole word dips"),
                              (axes[1], split, GREEN, "Split band: only the highs dip")]:
    ax.set_facecolor("white")
    ax.set_xscale("log"); ax.set_xlim(50, 20000); ax.set_ylim(-9, 2)
    ax.set_xticks(ticks); ax.set_xticklabels(tl, fontsize=16, color=DARK); ax.minorticks_off()
    ax.set_yticks(range(-8, 3, 2)); ax.tick_params(axis="y", labelsize=18, colors=DARK)
    for v in range(-8, 3, 2):
        ax.axhline(v, color=GUIDE, lw=0.8, zorder=0)
    for t in ticks:
        ax.axvline(t, color=GUIDE, lw=0.6, zorder=0)
    ax.axhline(0, color=DARK, lw=1.5, ls=":", zorder=1)
    ax.plot(f, curve, color=col, lw=4, zorder=3)
    ax.set_title(title, fontsize=22, color=DARK, pad=12)
    ax.set_xlabel("Frequency (Hz)", fontsize=20, color=DARK)
    for sp in ["top", "right"]:
        ax.spines[sp].set_visible(False)
axes[0].set_ylabel("Gain during an S (dB)", fontsize=20, color=DARK)
axes[0].text(300, -4.3, "6 dB off every frequency,\nincluding the vowel body", fontsize=18, color=ORANGE, ha="center", va="center")
axes[1].axvline(fc, color=DARK, lw=2, ls="--", zorder=2)
axes[1].text(fc * 0.9, -7.6, "split point\n5 kHz", fontsize=18, color=DARK, ha="right", va="center")
axes[1].text(300, -2.2, "Vowel body keeps\nits level", fontsize=18, color=GREEN, ha="center", va="center")
axes[1].text(10500, -7.4, "Highs down\n6 dB", fontsize=18, color=GREEN, ha="center", va="center")
plt.tight_layout(w_pad=2)
plt.savefig("Wideband_Versus_Split_Band_De_Essing.png", facecolor="white")
print("split at 1k", split[np.argmin(abs(f-1000))], "at 5k", split[np.argmin(abs(f-5000))], "at 20k", split[-1])
