"""Genera el ciclo de evaluación y mejora de calidad de datos."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "ciclo_calidad_datos.png"

etapas = [
    (0.08, 0.58, "Definir propósito\ny unidad"),
    (0.31, 0.58, "Perfilar y\nvalidar"),
    (0.54, 0.58, "Investigar\ncausas"),
    (0.77, 0.58, "Corregir o\nmarcar"),
    (0.54, 0.16, "Comparar y\ndocumentar"),
    (0.31, 0.16, "Monitorear\ncambios"),
]

fig, ax = plt.subplots(figsize=(11, 4.4))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

for x, y, texto in etapas:
    caja = FancyBboxPatch(
        (x, y),
        0.16,
        0.18,
        boxstyle="round,pad=0.02,rounding_size=0.025",
        facecolor="#dcecf5",
        edgecolor="#245b78",
        linewidth=1.8,
    )
    ax.add_patch(caja)
    ax.text(x + 0.08, y + 0.09, texto, ha="center", va="center", fontsize=11)

flechas = [
    ((0.24, 0.67), (0.31, 0.67)),
    ((0.47, 0.67), (0.54, 0.67)),
    ((0.70, 0.67), (0.77, 0.67)),
    ((0.85, 0.58), (0.70, 0.34)),
    ((0.54, 0.25), (0.47, 0.25)),
    ((0.31, 0.25), (0.16, 0.58)),
]
for inicio, fin in flechas:
    ax.annotate(
        "",
        xy=fin,
        xytext=inicio,
        arrowprops={"arrowstyle": "->", "color": "#245b78", "lw": 1.8},
    )

ax.text(
    0.5,
    0.93,
    "La calidad se evalúa respecto del propósito y se controla de forma continua",
    ha="center",
    fontsize=14,
    fontweight="bold",
    color="#173f55",
)
fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
