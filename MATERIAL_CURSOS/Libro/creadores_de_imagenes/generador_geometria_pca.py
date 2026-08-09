"""Genera una figura didáctica sobre proyección y reconstrucción con PCA."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "geometria_pca.png"
RNG = np.random.default_rng(1010)

direccion_1 = np.array([0.84, 0.54])
direccion_2 = np.array([-direccion_1[1], direccion_1[0]])
coordenada_1 = RNG.normal(0, 2.2, 170)
coordenada_2 = RNG.normal(0, 0.48, 170)
datos = np.outer(coordenada_1, direccion_1) + np.outer(coordenada_2, direccion_2)

covarianza = np.cov(datos, rowvar=False)
valores, vectores = np.linalg.eigh(covarianza)
orden = np.argsort(valores)[::-1]
valores = valores[orden]
vectores = vectores[:, orden]
if vectores[0, 0] < 0:
    vectores[:, 0] *= -1
if vectores[1, 1] < 0:
    vectores[:, 1] *= -1

proyeccion = np.outer(datos @ vectores[:, 0], vectores[:, 0])
indices = np.linspace(0, len(datos) - 1, 18, dtype=int)
limite = 5.2

fig, ejes = plt.subplots(1, 2, figsize=(12.8, 5.2))

ejes[0].scatter(datos[:, 0], datos[:, 1], s=20, alpha=0.55, color="#2878a5")
colores = ["#d95f02", "#2b8c4b"]
for j, (color, etiqueta) in enumerate(zip(colores, ["PC1", "PC2"])):
    extremo = vectores[:, j] * np.sqrt(valores[j]) * 2.25
    ejes[0].annotate(
        "",
        xy=extremo,
        xytext=-extremo,
        arrowprops={"arrowstyle": "<->", "color": color, "lw": 2.6},
    )
    ejes[0].text(*(extremo * 1.08), etiqueta, color=color, fontweight="bold")
ejes[0].set_title("Direcciones de máxima varianza", fontweight="bold")

ejes[1].scatter(datos[:, 0], datos[:, 1], s=18, alpha=0.28, color="#2878a5", label="Datos")
ejes[1].scatter(
    proyeccion[:, 0],
    proyeccion[:, 1],
    s=18,
    alpha=0.62,
    color="#d95f02",
    label="Reconstrucción con PC1",
)
for i in indices:
    ejes[1].plot(
        [datos[i, 0], proyeccion[i, 0]],
        [datos[i, 1], proyeccion[i, 1]],
        color="#555555",
        linewidth=0.75,
        alpha=0.65,
    )
ejes[1].set_title("Proyección y error residual", fontweight="bold")
ejes[1].legend(loc="upper left", frameon=True)

for eje in ejes:
    eje.axhline(0, color="#999999", linewidth=0.7)
    eje.axvline(0, color="#999999", linewidth=0.7)
    eje.set_xlim(-limite, limite)
    eje.set_ylim(-3.7, 3.7)
    eje.set_aspect("equal")
    eje.set_xlabel("Variable centrada 1")
    eje.set_ylabel("Variable centrada 2")
    eje.grid(alpha=0.13)

porcentajes = 100 * valores / valores.sum()
fig.suptitle(
    f"Geometría de PCA: PC1 explica {porcentajes[0]:.1f}% y PC2 {porcentajes[1]:.1f}%",
    fontsize=15,
    fontweight="bold",
    color="#173f55",
)
fig.tight_layout(rect=(0, 0, 1, 0.92))
fig.savefig(SALIDA, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
