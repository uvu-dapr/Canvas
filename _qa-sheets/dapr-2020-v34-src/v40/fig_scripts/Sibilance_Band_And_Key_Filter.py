import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

f = np.logspace(np.log10(50), np.log10(20000), 2000)
lf = np.log10(f)

# Simplified long-term spectra (illustrative shapes, relative dB)
# Vowel: energy peaks near 600 Hz and falls about 7 dB per octave above it
oct_ = np.log2(f / 600.0)
vowel = np.where(f < 600, -6 - 5 * oct_ ** 2, -6 - 7 * oct_)
vowel = np.maximum(vowel, -60)
# S sound: noise band centred near 7 kHz
ssound = -8 - 16 * ((lf - np.log10(7000)) / 0.28) ** 2
ssound = np.maximum(ssound, -60)

# Key filter: 2nd order band-pass, centre 7 kHz, Q 1.2 (real magnitude)
f0, Q = 7000.0, 1.2
s = 1j * f / f0
bp = np.abs((s / Q) / (s ** 2 + s / Q + 1))
bp_db = 20 * np.log10(bp)

fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xscale("log")
ax.set_xlim(50, 20000)
ax.set_ylim(-48, 4)
ticks = [50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
ax.set_xticks(ticks)
ax.set_xticklabels(["50", "100", "200", "500", "1k", "2k", "5k", "10k", "20k"], fontsize=18, color=DARK)
ax.minorticks_off()
ax.set_yticks(range(-48, 1, 6))
ax.tick_params(axis="y", labelsize=18, colors=DARK)
for v in range(-48, 1, 6):
    ax.axhline(v, color=GUIDE, lw=0.8, zorder=0)
for t in ticks:
    ax.axvline(t, color=GUIDE, lw=0.6, zorder=0)
for sp in ["top", "right"]:
    ax.spines[sp].set_visible(False)

ax.axvspan(4000, 10000, color=ORANGE, alpha=0.08, zorder=0)
ax.text(6300, 2.2, "Typical sibilant range, about 4 to 10 kHz", fontsize=18, color=ORANGE, ha="center")

ax.plot(f, vowel, color=BLUE, lw=4, label="Vowel (ah)")
ax.plot(f, ssound, color=ORANGE, lw=4, label="S sound")
ax.plot(f, bp_db, color=GREEN, lw=4, ls="--", label="Key filter: band-pass at 7 kHz")

ax.text(900, -2.8, "Vowel: most energy is low", fontsize=19, color=BLUE, ha="left")
ax.text(1000, -40, "The key filter rejects\nthe vowel, so a loud vowel\nstays under threshold", fontsize=19, color=GREEN, ha="center", va="center")
ax.text(6700, -41, "S energy passes\nthe key filter and\ntriggers the de-esser", fontsize=19, color=ORANGE, ha="center", va="center")

ax.set_xlabel("Frequency (Hz)", fontsize=20, color=DARK)
ax.set_ylabel("Relative level (dB)", fontsize=20, color=DARK)
ax.legend(loc="upper left", fontsize=18, frameon=False)
ax.set_title("What the de-esser's detector hears: a filtered copy of the vocal", fontsize=24, color=DARK, pad=34)
plt.tight_layout()
plt.savefig("Sibilance_Band_And_Key_Filter.png", facecolor="white")
i = np.argmin(np.abs(f - 500)); j = np.argmin(np.abs(f - 7000))
print("BP at 500 Hz", bp_db[i], "at 7k", bp_db[j], "at 4k", bp_db[np.argmin(np.abs(f-4000))])
