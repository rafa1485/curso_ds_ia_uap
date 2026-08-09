"""Genera un esquema conceptual de una red neuronal."""
from pathlib import Path
import matplotlib.pyplot as plt

SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "red_neuronal.png"
fig, ax = plt.subplots(figsize=(7, 4))
ax.axis("off")
capas = [[(0.15, y) for y in (0.25, 0.5, 0.75)], [(0.5, y) for y in (0.15, 0.35, 0.65, 0.85)], [(0.85, 0.5)]]
for izquierda, derecha in zip(capas, capas[1:]):
    for x1, y1 in izquierda:
        for x2, y2 in derecha:
            ax.plot((x1, x2), (y1, y2), color="#b7c9d6", lw=0.8)
for capa in capas:
    for x, y in capa:
        ax.scatter(x, y, s=500, color="#dcecf5", edgecolor="#245b78", zorder=3)
ax.text(0.15, 0.05, "entrada", ha="center")
ax.text(0.5, 0.05, "oculta", ha="center")
ax.text(0.85, 0.05, "salida", ha="center")
fig.savefig(SALIDA, dpi=160, bbox_inches="tight")
plt.close(fig)
