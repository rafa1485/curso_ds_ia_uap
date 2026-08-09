"""Genera un diagrama del ciclo de vida de un proyecto de datos."""
from pathlib import Path
import matplotlib.pyplot as plt

SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "ciclo_vida_datos.png"

etapas = [
    ("Problema", (1.5, 5.0)),
    ("Datos", (4.5, 5.0)),
    ("Representación", (7.5, 5.0)),
    ("Análisis", (10.5, 5.0)),
    ("Evidencia", (10.5, 2.0)),
    ("Decisión", (7.5, 2.0)),
    ("Evaluación", (4.5, 2.0)),
]

fig, ax = plt.subplots(figsize=(14, 7))
ax.axis("off")
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)

estilo_caja = {
    "boxstyle": "round,pad=0.75",
    "fc": "#d9eaf7",
    "ec": "#245b78",
    "lw": 2.2,
}
estilo_flecha = {
    "arrowstyle": "-|>",
    "color": "#245b78",
    "lw": 2.4,
    "mutation_scale": 18,
}

for etapa, (x, y) in etapas:
    ax.text(
        x,
        y,
        etapa,
        ha="center",
        va="center",
        fontsize=18,
        fontweight="bold",
        color="#173f54",
        bbox=estilo_caja,
        zorder=2,
    )

conexiones = [
    ((2.45, 5.0), (3.82, 5.0)),
    ((5.18, 5.0), (6.02, 5.0)),
    ((8.98, 5.0), (9.62, 5.0)),
    ((10.5, 4.48), (10.5, 2.52)),
    ((9.56, 2.0), (8.36, 2.0)),
    ((6.66, 2.0), (5.55, 2.0)),
]
for inicio, fin in conexiones:
    ax.annotate("", xy=fin, xytext=inicio, arrowprops=estilo_flecha, zorder=1)

ax.annotate(
    "",
    xy=(1.5, 4.48),
    xytext=(3.48, 2.0),
    arrowprops={**estilo_flecha, "connectionstyle": "arc3,rad=-0.75"},
    zorder=1,
)
ax.text(
    1.5,
    0.75,
    "Retroalimentación\ny monitoreo",
    ha="center",
    va="center",
    fontsize=15,
    color="#245b78",
    fontweight="bold",
)

fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
