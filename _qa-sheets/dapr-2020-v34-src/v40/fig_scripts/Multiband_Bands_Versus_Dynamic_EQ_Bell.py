import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

f = np.logspace(np.log10(20), np.log10(20000), 2000)

# Linkwitz-Riley 4th order crossover magnitudes (LP + HP sum to 1, in phase)
def lr4_lp(f, fc):
    return 1.0 / (1.0 + (f / fc) ** 4)
def lr4_hp(f, fc):
    x = (f / fc) ** 4
    return x / (1.0 + x)

f1, f2 = 200.0, 2500.0
low = lr4_lp(f, f1)
mid = lr4_hp(f, f1) * lr4_lp(f, f2)
high = lr4_hp(f, f1) * lr4_hp(f, f2)
g_low = 10 ** (-4 / 20.0)             # 4 dB gain reduction in the low band
combined = g_low * low + mid + high   # mid and high untouched

# Analog peaking EQ (RBJ prototype) magnitude
def peak_db(f, f0, gain_db, q):
    A = 10 ** (gain_db / 40.0)
    s = 1j * f / f0
    H = (s ** 2 + s * (A / q) + 1) / (s ** 2 + s / (A * q) + 1)
    return 20 * np.log10(np.abs(H))

bell = peak_db(f, 3000.0, -5.0, 4.0)

def db(x):
    return 20 * np.log10(np.maximum(x, 1e-6))

fig, axes = plt.subplots(2, 1, figsize=(16, 12), dpi=100)
fig.patch.set_facecolor("white")
ticks = [20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
labels = ["20", "50", "100", "200", "500", "1k", "2k", "5k", "10k", "20k"]

for ax in axes:
    ax.set_facecolor("white")
    ax.set_xscale("log")
    ax.set_xlim(20, 20000)
    ax.set_ylim(-8, 2.5)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labels, fontsize=18, color=DARK)
    ax.minorticks_off()
    ax.set_yticks([-8, -6, -4, -2, 0, 2])
    ax.tick_params(axis="y", labelsize=18, colors=DARK)
    for v in [-8, -6, -4, -2, 0, 2]:
        ax.axhline(v, color=GUIDE, lw=0.8, zorder=0)
    for t in ticks:
        ax.axvline(t, color=GUIDE, lw=0.6, zorder=0)
    ax.set_ylabel("Gain (dB)", fontsize=20, color=DARK)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)

# Panel 1: multiband
ax = axes[0]
ax.axvspan(20, f1, color=BLUE, alpha=0.08, zorder=0)
ax.plot(f, db(low), color=GUIDE, lw=2, ls="--", zorder=1)
ax.plot(f, db(mid), color=GUIDE, lw=2, ls="--", zorder=1)
ax.plot(f, db(high), color=GUIDE, lw=2, ls="--", zorder=1)
ax.plot(f, db(combined), color=BLUE, lw=4, zorder=3)
for fc in (f1, f2):
    ax.axvline(fc, color=DARK, lw=2, ls=":", zorder=2)
ax.text(f1 * 1.05, 1.6, "crossover 200 Hz", fontsize=18, color=DARK, ha="left")
ax.text(f2 * 1.05, 1.6, "crossover 2.5 kHz", fontsize=18, color=DARK, ha="left")
ax.text(24, -4.5, "Low band: 4 dB of gain\nreduction turns down\neverything below the\ncrossover as one block", fontsize=18, color=BLUE, ha="left", va="top")
ax.text(700, -2.2, "Mid band untouched", fontsize=18, color=DARK, ha="center")
ax.text(7000, -2.2, "High band untouched", fontsize=18, color=DARK, ha="center")
ax.text(760, -5.2, "Dashed gray: the three\ncrossover bands\nBlue: the summed output", fontsize=17, color=DARK, ha="center", va="center")
ax.set_title("Multiband compression: a whole band moves", fontsize=24, color=DARK, pad=12)

# Panel 2: dynamic EQ
ax = axes[1]
ax.plot(f, np.zeros_like(f), color=GREEN, lw=4, zorder=2)
ax.plot(f, bell, color=ORANGE, lw=4, zorder=3)
ax.axvline(3000, color=DARK, lw=2, ls=":", zorder=1)
ax.text(3000 * 1.06, -6.4, "3 kHz band, Q 4,\ncutting 5 dB\nwhile above threshold", fontsize=18, color=ORANGE, ha="left", va="center")
ax.text(60, 0.9, "Below threshold: gain stays at 0 dB, the EQ is flat", fontsize=18, color=GREEN, ha="left")
ax.text(60, -2.6, "Everything outside the narrow\nband is left alone", fontsize=18, color=DARK, ha="left", va="center")
ax.set_title("Dynamic EQ: one narrow band moves", fontsize=24, color=DARK, pad=12)
ax.set_xlabel("Frequency (Hz)", fontsize=20, color=DARK)

plt.tight_layout(h_pad=2.5)
plt.savefig("Multiband_Bands_Versus_Dynamic_EQ_Bell.png", facecolor="white")
print("min combined dB", db(combined).min(), "at low end", db(combined)[0], "bell min", bell.min())
