"""Ilustra cómo un eje truncado exagera diferencias entre barras."""
from pathlib import Path

import matplotlib.pyplot as plt


SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "escalas_enganosas.png"
categorias = ["Zona A", "Zona B"]
valores = [96, 100]
colores = ["#6baed6", "#2171b5"]

fig, ejes = plt.subplots(1, 2, figsize=(10.5, 4.8))

for ax, limite, titulo in zip(
    ejes,
    [(0, 110), (94, 101)],
    ["Escala completa", "Escala truncada"],
):
    barras = ax.bar(categorias, valores, color=colores, width=0.58)
    ax.set_ylim(*limite)
    ax.set_title(titulo, fontsize=13, fontweight="bold")
    ax.set_ylabel("Índice observado")
    ax.grid(axis="y", alpha=0.25)
    for barra, valor in zip(barras, valores):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            valor + (limite[1] - limite[0]) * 0.015,
            str(valor),
            ha="center",
            va="bottom",
            fontsize=11,
        )

fig.suptitle(
    "Los mismos valores producen impresiones visuales diferentes",
    fontsize=15,
    fontweight="bold",
    color="#173f55",
)
fig.text(
    0.5,
    0.01,
    "La diferencia absoluta es 4 en ambos paneles; el segundo exagera su magnitud relativa.",
    ha="center",
    fontsize=10,
)
fig.tight_layout(rect=(0, 0.05, 1, 0.92))
fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
