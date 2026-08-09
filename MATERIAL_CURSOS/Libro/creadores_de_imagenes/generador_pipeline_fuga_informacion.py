"""Compara un pipeline con fuga y otro que separa antes de ajustar."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "pipeline_fuga_informacion.png"


def caja(ax, x, y, texto, color, borde):
    parche = FancyBboxPatch(
        (x, y),
        0.17,
        0.13,
        boxstyle="round,pad=0.015,rounding_size=0.02",
        facecolor=color,
        edgecolor=borde,
        linewidth=1.6,
    )
    ax.add_patch(parche)
    ax.text(x + 0.085, y + 0.065, texto, ha="center", va="center", fontsize=10)


def flecha(ax, x1, y1, x2, y2, color):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops={"arrowstyle": "->", "lw": 1.6, "color": color},
    )


fig, ax = plt.subplots(figsize=(12, 5.8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

ax.text(0.03, 0.87, "Incorrecto: la prueba influye en el ajuste", fontsize=14, fontweight="bold", color="#8c2f2f")
incorrecto = [
    (0.04, "Todos los\ndatos"),
    (0.27, "Imputar y\nescalar"),
    (0.50, "Separar"),
    (0.73, "Entrenar y\nevaluar"),
]
for x, texto in incorrecto:
    caja(ax, x, 0.66, texto, "#f7dada", "#a94442")
for x1, x2 in zip([0.21, 0.44, 0.67], [0.27, 0.50, 0.73]):
    flecha(ax, x1, 0.725, x2, 0.725, "#a94442")
ax.text(0.355, 0.60, "Parámetros calculados con información de prueba", ha="center", fontsize=10, color="#8c2f2f")

ax.text(0.03, 0.43, "Correcto: separar antes de aprender transformaciones", fontsize=14, fontweight="bold", color="#245b78")
correcto = [
    (0.04, "Datos\noriginales"),
    (0.27, "Separar por\ngrupo/tiempo"),
    (0.50, "Ajustar solo con\nentrenamiento"),
    (0.73, "Transformar y\nevaluar prueba"),
]
for x, texto in correcto:
    caja(ax, x, 0.22, texto, "#dcecf5", "#245b78")
for x1, x2 in zip([0.21, 0.44, 0.67], [0.27, 0.50, 0.73]):
    flecha(ax, x1, 0.285, x2, 0.285, "#245b78")
ax.text(0.73, 0.12, "La prueba recibe transformaciones; nunca reajusta parámetros", ha="center", fontsize=10, color="#173f55")

fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
