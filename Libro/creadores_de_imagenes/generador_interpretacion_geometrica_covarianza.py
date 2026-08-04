"""Genera nubes que ilustran la interpretación geométrica de la covarianza."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


SALIDA = (
    Path(__file__).resolve().parents[1]
    / "imagenes"
    / "interpretacion_geometrica_covarianza.png"
)
RNG = np.random.default_rng(42)
N = 300

# Relación lineal positiva: las desviaciones de X e Y suelen tener el mismo signo.
x_lineal = RNG.normal(0, 1, N)
y_lineal = 1.5 * x_lineal + RNG.normal(0, 0.55, N)

# Nube circular: no existe una dirección lineal preferente.
angulo = RNG.uniform(0, 2 * np.pi, N)
radio = np.sqrt(RNG.uniform(0, 1, N))
x_circular = radio * np.cos(angulo)
y_circular = radio * np.sin(angulo)

# Relación en U: pares simétricos comparten Y para que la covarianza se anule.
x_positivo = RNG.uniform(0, 2, N // 2)
ruido_u = RNG.normal(0, 0.28, N // 2)
x_u = np.concatenate((-x_positivo, x_positivo))
y_u = np.concatenate((x_positivo**2 + ruido_u, x_positivo**2 + ruido_u))

casos = [
    (x_lineal, y_lineal, "Relación lineal positiva"),
    (x_circular, y_circular, "Nube circular"),
    (x_u, y_u, "Relación no lineal en U"),
]

fig, ejes = plt.subplots(1, 3, figsize=(13.5, 4.5))
for ax, (x, y, titulo) in zip(ejes, casos):
    covarianza = np.cov(x, y, ddof=1)[0, 1]
    correlacion = np.corrcoef(x, y)[0, 1]
    ax.scatter(x, y, s=18, alpha=0.58, color="#2171b5", edgecolors="none")
    ax.axhline(np.mean(y), color="#777777", linewidth=0.9, linestyle="--")
    ax.axvline(np.mean(x), color="#777777", linewidth=0.9, linestyle="--")
    ax.set_title(titulo, fontsize=12, fontweight="bold")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.text(
        0.04,
        0.96,
        f"Cov(X,Y) = {covarianza:.2f}\nr = {correlacion:.2f}",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "alpha": 0.86},
    )
    ax.grid(alpha=0.16)

fig.suptitle(
    "La covarianza resume asociación lineal, no toda forma de dependencia",
    fontsize=15,
    fontweight="bold",
    color="#173f55",
)
fig.tight_layout(rect=(0, 0, 1, 0.92))
fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
