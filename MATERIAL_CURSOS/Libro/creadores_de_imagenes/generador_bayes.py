"""Genera un esquema de actualizacion bayesiana."""
from pathlib import Path
import matplotlib.pyplot as plt

SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "actualizacion_bayesiana.png"
fig, ax = plt.subplots(figsize=(8, 3))
ax.axis("off")
items = [(0.18, "Prior\nP(H)"), (0.5, "Evidencia\nP(E|H)"), (0.82, "Posterior\nP(H|E)")]
for x, text in items:
    ax.text(x, 0.55, text, ha="center", va="center", bbox={"boxstyle": "round,pad=0.8", "fc": "#f7e6c4", "ec": "#9a6415"})
ax.annotate("actualizar", (0.4, 0.55), (0.27, 0.55), arrowprops={"arrowstyle": "->", "lw": 1.5})
ax.annotate("normalizar", (0.72, 0.55), (0.59, 0.55), arrowprops={"arrowstyle": "->", "lw": 1.5})
fig.savefig(SALIDA, dpi=160, bbox_inches="tight")
plt.close(fig)
