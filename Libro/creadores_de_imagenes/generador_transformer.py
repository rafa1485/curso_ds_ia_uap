"""Genera un esquema simplificado del flujo de un Transformer."""
from pathlib import Path
import matplotlib.pyplot as plt

SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "transformer.png"
fig, ax = plt.subplots(figsize=(9, 2.5))
ax.axis("off")
items = ["tokens", "embeddings", "atencion\nQ,K,V", "red\nfeed-forward", "salida"]
for i, item in enumerate(items):
    x = i / (len(items) - 1)
    ax.text(x, 0.5, item, ha="center", va="center", bbox={"boxstyle": "round,pad=0.65", "fc": "#e8e1f2", "ec": "#60458a"}, transform=ax.transAxes)
    if i < len(items) - 1:
        ax.annotate("", ((i + 0.82) / (len(items) - 1), 0.5), ((i + 0.18) / (len(items) - 1), 0.5), xycoords=ax.transAxes, arrowprops={"arrowstyle": "->"})
fig.savefig(SALIDA, dpi=160, bbox_inches="tight")
plt.close(fig)
