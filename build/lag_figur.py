"""Setter de fem kurvefigurene (results/kurve_NOx.png) sammen til manus/fig_kurver.png (3 × 2-rutenett)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

Z = ["NO1", "NO2", "NO3", "NO4", "NO5"]
fig, ax = plt.subplots(3, 2, figsize=(12, 7.2))
for a, z in zip(ax.flat, Z + [None]):
    a.axis("off")
    if z:
        a.imshow(mpimg.imread(f"results/kurve_{z}.png"))
fig.tight_layout(pad=0.2)
fig.savefig("manus/fig_kurver.png", dpi=200, metadata={"Software": None})
