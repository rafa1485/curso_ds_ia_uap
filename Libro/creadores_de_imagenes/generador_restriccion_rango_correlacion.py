"""Ilustra restricción de rango y correlación inducida al mezclar grupos."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


SALIDA = (
    Path(__file__).resolve().parents[1]
    / "imagenes"
    / "restriccion_rango_correlacion.png"
)
RNG = np.random.default_rng(73)

# Una misma relación observada sobre el rango completo y sobre una franja estrecha.
x_completo = RNG.uniform(-4, 4, 900)
y_completo = 0.9 * x_completo + RNG.normal(0, 1.0, x_completo.size)
mascara = np.abs(x_completo) <= 0.8
x_restringido = x_completo[mascara]
y_restringido = y_completo[mascara]

# Dos grupos sin relación interna apreciable, pero con centros diferentes.
n_grupo = 220
x_a = RNG.normal(-2.2, 0.65, n_grupo)
y_a = RNG.normal(-2.0, 0.75, n_grupo)
x_b = RNG.normal(2.2, 0.65, n_grupo)
y_b = RNG.normal(2.0, 0.75, n_grupo)
x_mezcla = np.concatenate((x_a, x_b))
y_mezcla = np.concatenate((y_a, y_b))


def correlacion(x, y):
    return np.corrcoef(x, y)[0, 1]


fig, ejes = plt.subplots(1, 3, figsize=(14, 4.7))

ejes[0].scatter(x_completo, y_completo, s=14, alpha=0.42, color="#2171b5", edgecolors="none")
ejes[0].set_title("Rango completo", fontsize=12, fontweight="bold")
ejes[0].text(
    0.05,
    0.94,
    f"r = {correlacion(x_completo, y_completo):.2f}\nn = {x_completo.size}",
    transform=ejes[0].transAxes,
    va="top",
    bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "alpha": 0.88},
)

ejes[1].scatter(x_restringido, y_restringido, s=20, alpha=0.56, color="#6baed6", edgecolors="none")
ejes[1].set_title(r"Misma relación, $|X| \leq 0.8$", fontsize=12, fontweight="bold")
ejes[1].text(
    0.05,
    0.94,
    f"r = {correlacion(x_restringido, y_restringido):.2f}\nn = {x_restringido.size}",
    transform=ejes[1].transAxes,
    va="top",
    bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "alpha": 0.88},
)

ejes[2].scatter(x_a, y_a, s=19, alpha=0.58, color="#31a354", label=f"Grupo A: r={correlacion(x_a, y_a):.2f}", edgecolors="none")
ejes[2].scatter(x_b, y_b, s=19, alpha=0.58, color="#e6550d", label=f"Grupo B: r={correlacion(x_b, y_b):.2f}", edgecolors="none")
ejes[2].set_title("Mezcla de grupos", fontsize=12, fontweight="bold")
ejes[2].text(
    0.05,
    0.94,
    f"r global = {correlacion(x_mezcla, y_mezcla):.2f}",
    transform=ejes[2].transAxes,
    va="top",
    bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "alpha": 0.88},
)
ejes[2].legend(loc="lower right", fontsize=9)

for ax in ejes:
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(alpha=0.16)

fig.suptitle(
    "La correlación depende del rango observado y de la composición de la población",
    fontsize=15,
    fontweight="bold",
    color="#173f55",
)
fig.tight_layout(rect=(0, 0, 1, 0.91))
fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
