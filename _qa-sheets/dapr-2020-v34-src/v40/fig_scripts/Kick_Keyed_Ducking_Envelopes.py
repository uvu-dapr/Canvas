import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

fs = 8000
T = 2.0
t = np.arange(int(fs * (T + 0.05))) / fs - 0.05
bpm = 120
beat = 60.0 / bpm                      # 0.5 s between kicks
hits = np.arange(0, T - 1e-9, beat)

# Kick key signal: pitch drops 110 Hz -> 55 Hz, amplitude decays with an 80 ms time constant
key = np.zeros_like(t)
env = np.zeros_like(t)
for h in hits:
    m = t >= h
    tt = t[m] - h
    a = 10 ** (-6 / 20.0) * np.exp(-tt / 0.08)     # peak -6 dBFS
    freq = 55 + 55 * np.exp(-tt / 0.03)
    phase = 2 * np.pi * np.cumsum(freq) / fs
    key[m] += a * np.sin(phase)
    env[m] = np.maximum(env[m], a)
level_db = 20 * np.log10(np.maximum(env, 1e-6))

def compress(level_db, thresh, ratio, attack_ms, release_ms):
    target = np.where(level_db > thresh, (level_db - thresh) * (1 - 1.0 / ratio), 0.0)
    a_att = np.exp(-1.0 / (fs * attack_ms / 1000.0))
    a_rel = np.exp(-1.0 / (fs * release_ms / 1000.0))
    gr = np.zeros_like(target)
    g = 0.0
    for i, x in enumerate(target):
        coef = a_att if x > g else a_rel
        g = coef * g + (1 - coef) * x
        gr[i] = g
    return -gr

# Thresholds solved so the deepest reduction is 3.0 dB (bass) and 8.0 dB (pad)
def solve(target, ratio, rel):
    lo, hi = -40.0, -6.0
    for _ in range(40):
        mid = (lo + hi) / 2
        d = -compress(level_db, mid, ratio, 1.0, rel).min()
        lo, hi = (lo, mid) if d < target else (mid, hi)
    return (lo + hi) / 2
BASS_T = solve(3.0, 4.0, 100.0)
PAD_T = solve(8.0, 10.0, 150.0)
# Bass: 4:1, threshold 4 dB under the key peak -> 3 dB of reduction, fast attack, 100 ms release
bass = compress(level_db, BASS_T, 4.0, 1.0, 100.0)
# Pad: 10:1, threshold 9 dB under the key peak -> about 8 dB, 150 ms release (audible pump)
pad = compress(level_db, PAD_T, 10.0, 1.0, 150.0)

fig, axes = plt.subplots(3, 1, figsize=(16, 13), dpi=100, sharex=True,
                         gridspec_kw={"height_ratios": [1, 1, 1.25]})
fig.patch.set_facecolor("white")
for ax in axes:
    ax.set_facecolor("white")
    for h in hits:
        ax.axvline(h * 1000, color=GUIDE, lw=1.5, zorder=0)
    for sp in ["top", "right"]:
        ax.spines[sp].set_visible(False)
    ax.tick_params(labelsize=18, colors=DARK)

ax = axes[0]
ax.plot(t * 1000, key, color=DARK, lw=1.2)
ax.set_ylim(-0.6, 0.75)
ax.set_yticks([])
ax.set_ylabel("Kick key", fontsize=20, color=DARK)
ax.set_title("Kick-keyed ducking at 120 BPM: a kick every 500 ms", fontsize=24, color=DARK, pad=12)

ax = axes[1]
ax.plot(t * 1000, bass, color=BLUE, lw=4)
ax.axhline(-3, color=BLUE, lw=1.2, ls=":")
ax.set_ylim(-4.5, 0.8)
ax.set_yticks([0, -1, -2, -3, -4])
ax.set_ylabel("Bass gain (dB)", fontsize=20, color=DARK)
ax.text(520, -3.9, "3 dB dip on each kick, back to 0 dB well before the next kick", fontsize=18, color=BLUE, ha="left", va="center")

ax = axes[2]
ax.plot(t * 1000, pad, color=ORANGE, lw=4)
ax.set_ylim(-10.5, 1.2)
ax.set_yticks([0, -2, -4, -6, -8, -10])
ax.set_ylabel("Pad gain (dB)", fontsize=20, color=DARK)
ax.text(520, -9.6, "8 dB dip, longer release: the pad swells back across the beat", fontsize=18, color=ORANGE, ha="left", va="center")
ax.set_xlabel("Time (ms)", fontsize=20, color=DARK)
ax.set_xlim(-20, 2000)

plt.tight_layout(h_pad=1.5)
plt.savefig("Kick_Keyed_Ducking_Envelopes.png", facecolor="white")
i = int((0.49 + 0.05) * fs)
print("thresholds", BASS_T, PAD_T); print("bass min", bass.min(), "bass at 490ms", bass[i], "pad min", pad.min(), "pad at 490ms", pad[i])
