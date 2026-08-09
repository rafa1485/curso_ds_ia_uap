"""Ilustra una variable de confusión en un ejemplo de movilidad."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


SALIDA = (
    Path(__file__).resolve().parents[1]
    / "imagenes"
    / "variable_confusion_movilidad.png"
)
RNG = np.random.default_rng(121)
N = 220

# Dentro de cada franja, demanda y retraso son prácticamente independientes.
demanda_valle = RNG.normal(42, 9, N)
retraso_valle = RNG.normal(7, 3.2, N)
demanda_pico = RNG.normal(88, 10, N)
retraso_pico = RNG.normal(22, 3.8, N)

demanda = np.concatenate((demanda_valle, demanda_pico))
retraso = np.concatenate((retraso_valle, retraso_pico))


def correlacion(x, y):
    return np.corrcoef(x, y)[0, 1]


def recta(ax, x, y, color, estilo="-"):
    pendiente, intercepto = np.polyfit(x, y, 1)
    dominio = np.linspace(np.min(x), np.max(x), 100)
    ax.plot(dominio, pendiente * dominio + intercepto, color=color, lw=2.2, linestyle=estilo)


fig, ejes = plt.subplots(1, 3, figsize=(14.5, 4.9), gridspec_kw={"width_ratios": [0.8, 1.15, 1.3]})

# Panel 1: estructura causal simplificada.
ax = ejes[0]
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
nodos = {
    "Hora del día\nZ": (0.50, 0.80, "#fdae6b"),
    "Demanda\nX": (0.22, 0.25, "#9ecae1"),
    "Retraso\nY": (0.78, 0.25, "#a1d99b"),
}
for texto, (x, y, color) in nodos.items():
    ax.add_patch(Circle((x, y), 0.16, facecolor=color, edgecolor="#334455", linewidth=1.6))
    ax.text(x, y, texto, ha="center", va="center", fontsize=11, fontweight="bold")
for destino in [(0.27, 0.37), (0.73, 0.37)]:
    ax.annotate(
        "",
        xy=destino,
        xytext=(0.50, 0.64),
        arrowprops={"arrowstyle": "->", "lw": 2, "color": "#555555"},
    )
ax.set_title("Mecanismo de confusión", fontsize=12, fontweight="bold")

# Panel 2: análisis que ignora Z.
ax = ejes[1]
ax.scatter(demanda, retraso, s=18, alpha=0.42, color="#6b8fb3", edgecolors="none")
recta(ax, demanda, retraso, "#173f55")
ax.text(
    0.05,
    0.95,
    f"r global = {correlacion(demanda, retraso):.2f}",
    transform=ax.transAxes,
    va="top",
    bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "alpha": 0.9},
)
ax.set_title("Sin controlar la hora", fontsize=12, fontweight="bold")
ax.set_xlabel("Demanda")
ax.set_ylabel("Retraso")
ax.grid(alpha=0.16)

# Panel 3: se muestra y controla visualmente el estrato.
ax = ejes[2]
ax.scatter(
    demanda_valle,
    retraso_valle,
    s=19,
    alpha=0.55,
    color="#3182bd",
    label=f"Valle: r={correlacion(demanda_valle, retraso_valle):.2f}",
    edgecolors="none",
)
ax.scatter(
    demanda_pico,
    retraso_pico,
    s=19,
    alpha=0.55,
    color="#e6550d",
    label=f"Pico: r={correlacion(demanda_pico, retraso_pico):.2f}",
    edgecolors="none",
)
recta(ax, demanda_valle, retraso_valle, "#2171b5")
recta(ax, demanda_pico, retraso_pico, "#cb4b16")
ax.set_title("Estratificado por franja", fontsize=12, fontweight="bold")
ax.set_xlabel("Demanda")
ax.set_ylabel("Retraso")
ax.legend(loc="lower right", fontsize=9)
ax.grid(alpha=0.16)

fig.suptitle(
    "La hora del día puede crear una asociación global entre demanda y retraso",
    fontsize=15,
    fontweight="bold",
    color="#173f55",
)
fig.tight_layout(rect=(0, 0, 1, 0.91))
fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
