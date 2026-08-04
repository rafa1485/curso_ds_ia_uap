"""Genera una guía visual para elegir gráficos según la pregunta."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "seleccion_graficos.png"

fig, ax = plt.subplots(figsize=(12, 6.2))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

ax.text(
    0.5,
    0.94,
    "Elegir el gráfico a partir de la pregunta de comparación",
    ha="center",
    va="center",
    fontsize=16,
    fontweight="bold",
    color="#173f55",
)

elementos = [
    (0.07, 0.60, "Comparar\nmagnitudes", "Barras o puntos", "¿Comparten línea base?"),
    (0.38, 0.60, "Describir una\ndistribución", "Histograma, caja\no violín", "¿Se ve forma y tamaño?"),
    (0.69, 0.60, "Relacionar\nvariables", "Dispersión o\nhexágonos", "¿Hay sobreposición?"),
    (0.07, 0.20, "Mostrar\nevolución", "Línea o puntos\ntemporales", "¿La frecuencia es regular?"),
    (0.38, 0.20, "Mostrar\ncomposición", "Barras apiladas", "¿Importa volumen o proporción?"),
    (0.69, 0.20, "Mostrar\nespacio", "Puntos o mapa\ncoroplético", "¿El denominador es válido?"),
]

for x, y, objetivo, grafico, control in elementos:
    caja = FancyBboxPatch(
        (x, y),
        0.24,
        0.25,
        boxstyle="round,pad=0.02,rounding_size=0.025",
        facecolor="#e4f0f6",
        edgecolor="#245b78",
        linewidth=1.6,
    )
    ax.add_patch(caja)
    ax.text(x + 0.12, y + 0.19, objetivo, ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(x + 0.12, y + 0.115, grafico, ha="center", va="center", fontsize=11, color="#245b78")
    ax.text(x + 0.12, y + 0.045, control, ha="center", va="center", fontsize=9, style="italic")

fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
