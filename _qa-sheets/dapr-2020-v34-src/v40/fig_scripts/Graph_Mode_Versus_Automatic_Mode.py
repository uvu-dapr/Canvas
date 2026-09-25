import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#424242"; GREEN = "#1B5E20"; ORANGE = "#BF360C"; BLUE = "#0D47A1"; GUIDE = "#BDBDBD"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

# Phrase in G major, pitch as MIDI note number (60 = C4). B4 = 71, D5 = 74, E5 = 76.
sr = 2000
t = np.arange(0, 2.6, 1 / sr)
raw = np.full_like(t, np.nan)
vib = lambda tt, d: d * np.sin(2 * np.pi * 5.5 * tt)
# B4 held, in tune, light vibrato
m = (t >= 0.0) & (t < 0.6); raw[m] = 71 + 0.10 * np.sin(2 * np.pi * 5.0 * t[m])  # 3 whole cycles, ends at 0
# deliberate slide from B4 up to D5
m = (t >= 0.6) & (t < 0.9); raw[m] = 71 + 3 * (t[m] - 0.6) / 0.3
# D5 held, in tune, vibrato +/-25 cents
m = (t >= 0.9) & (t < 1.8); raw[m] = 74 + vib(t[m] - 0.9, 0.25)
# gap, then E5 sung 40 cents flat
m = (t >= 1.9) & (t < 2.6); raw[m] = 76 - 0.40 + vib(t[m] - 1.9, 0.12)

# Automatic mode: fast correction toward the nearest note of G major
scale = {7, 9, 11, 0, 2, 4, 6}
def nearest(x):
    best = None
    for n in range(int(np.floor(x)) - 2, int(np.floor(x)) + 3):
        if n % 12 in scale and (best is None or abs(n - x) < abs(best - x)):
            best = n
    return best
tau = 0.005  # 5 ms: a fast retune speed
a = 1 - np.exp(-1 / (sr * tau))
auto = np.full_like(t, np.nan)
corr = 0.0
for i, x in enumerate(raw):
    if np.isnan(x):
        continue
    corr += a * ((nearest(x) - x) - corr)
    auto[i] = x + corr

# Graph mode: only the flat E5 moves, its center up 35 cents, shape unchanged
graph = raw.copy()
m = t >= 1.9; graph[m] = raw[m] + 0.35

fig, axes = plt.subplots(3, 1, figsize=(16, 13), dpi=100, sharex=True)
fig.patch.set_facecolor("white")
names = {71: "B4", 72: "C5", 73: "C#5", 74: "D5", 75: "D#5", 76: "E5"}
panels = [(raw, "Original: in tune B, slide up, D with vibrato, E sung 40 cents flat", DARK),
          (auto, "Automatic mode, key of G, fast speed: slide becomes steps, vibrato frozen", ORANGE),
          (graph, "Graph mode: only the flat E was moved, everything else untouched", GREEN)]
for ax, (y, title, col) in zip(axes, panels):
    ax.set_facecolor("white")
    for n in names:
        ax.axhline(n, color=GUIDE, lw=1, zorder=0)
    ax.set_yticks(list(names)); ax.set_yticklabels(list(names.values()), fontsize=18, color=DARK)
    ax.set_ylim(70.4, 76.6)
    if y is not raw:
        ax.plot(t, raw, color=GUIDE, lw=2.5, zorder=1, label="original")
    ax.plot(t, y, color=col, lw=3.2, zorder=3)
    ax.set_title(title, fontsize=21, color=col, loc="left")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axes[1].annotate("C5 step inside the slide", xy=(0.76, 72), xytext=(1.0, 71.0), fontsize=18, color=ORANGE,
                 arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2.2))
axes[1].legend(loc="upper left", fontsize=17, frameon=False)
axes[2].annotate("E moved up 35 cents,\nvibrato kept", xy=(2.2, 75.95), xytext=(1.25, 71.3), fontsize=18, color=GREEN,
                 arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.2))
axes[2].set_xlabel("Time (seconds)", fontsize=20, color=DARK)
axes[2].tick_params(axis="x", labelsize=18, colors=DARK)
plt.tight_layout()
plt.savefig("/home/claude/q40/fig/Mixing__Tuning/Graph_Mode_Versus_Automatic_Mode.png", facecolor="white")
