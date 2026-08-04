"""Genera un diagrama didáctico de calibración probabilística."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "calibracion_probabilidades.png"

predicha = np.linspace(0.05, 0.95, 10)
bien = np.array([0.04, 0.17, 0.24, 0.36, 0.43, 0.57, 0.64, 0.76, 0.84, 0.94])
sobreconfiada = np.array([0.16, 0.25, 0.31, 0.40, 0.47, 0.53, 0.60, 0.68, 0.75, 0.83])

fig, ax = plt.subplots(figsize=(7.8, 6.5))
ax.plot([0, 1], [0, 1], linestyle="--", color="#555555", label="Calibración perfecta")
ax.plot(predicha, bien, marker="o", color="#2171b5", linewidth=2, label="Modelo bien calibrado")
ax.plot(
    predicha,
    sobreconfiada,
    marker="s",
    color="#cb181d",
    linewidth=2,
    label="Modelo sobreconfiado",
)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("Probabilidad pronosticada")
ax.set_ylabel("Frecuencia observada")
ax.set_title("Diagrama de confiabilidad", fontsize=15, fontweight="bold", color="#173f55")
ax.grid(alpha=0.25)
ax.legend(loc="upper left")
ax.text(
    0.60,
    0.19,
    "Por debajo de la diagonal:\nel evento ocurre menos de lo pronosticado",
    fontsize=10,
    color="#8c2f2f",
)
fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
