"""Genera ejemplos de distribuciones discretas y continuas frecuentes."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial
from scipy.stats import gamma, norm, weibull_min


SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "distribuciones_probabilidad.png"

fig, ejes = plt.subplots(2, 2, figsize=(11, 7.2))

k = np.arange(0, 13)
for tasa, color in [(1.5, "#9ecae1"), (4.0, "#3182bd")]:
    masa = np.exp(-tasa) * tasa**k / factorial(k)
    ejes[0, 0].plot(k, masa, marker="o", label=fr"Poisson $\lambda={tasa}$", color=color)
ejes[0, 0].set_title("Conteos: Poisson")
ejes[0, 0].set_xlabel("Número de eventos")
ejes[0, 0].set_ylabel("Probabilidad")
ejes[0, 0].legend()

x = np.linspace(-4, 4, 500)
ejes[0, 1].plot(x, norm.pdf(x, 0, 1), color="#756bb1", label="Normal estándar")
ejes[0, 1].plot(x, norm.pdf(x, 0, 1.7), color="#bcbddc", label="Mayor dispersión")
ejes[0, 1].set_title("Magnitudes simétricas: Normal")
ejes[0, 1].set_xlabel("Valor")
ejes[0, 1].set_ylabel("Densidad")
ejes[0, 1].legend()

t = np.linspace(0.001, 8, 500)
ejes[1, 0].plot(t, gamma.pdf(t, a=2, scale=1), color="#31a354", label="Gamma")
ejes[1, 0].plot(t, weibull_min.pdf(t, c=1.8, scale=2.5), color="#addd8e", label="Weibull")
ejes[1, 0].set_title("Tiempos positivos")
ejes[1, 0].set_xlabel("Tiempo")
ejes[1, 0].set_ylabel("Densidad")
ejes[1, 0].legend()

p = np.linspace(0.001, 0.999, 500)
from scipy.stats import beta

ejes[1, 1].plot(p, beta.pdf(p, 2, 2), color="#e6550d", label="Beta(2,2)")
ejes[1, 1].plot(p, beta.pdf(p, 2, 6), color="#fdae6b", label="Beta(2,6)")
ejes[1, 1].set_title("Probabilidades y proporciones: Beta")
ejes[1, 1].set_xlabel("Probabilidad")
ejes[1, 1].set_ylabel("Densidad")
ejes[1, 1].legend()

for ax in ejes.flat:
    ax.grid(alpha=0.2)

fig.suptitle(
    "La forma apropiada depende del soporte y del mecanismo generador",
    fontsize=15,
    fontweight="bold",
    color="#173f55",
)
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
