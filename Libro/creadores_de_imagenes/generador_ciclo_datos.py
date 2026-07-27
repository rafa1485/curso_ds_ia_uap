"""Genera un diagrama del ciclo de vida de un proyecto de datos."""
from pathlib import Path
import matplotlib.pyplot as plt

SALIDA = Path(__file__).resolve().parents[1] / "imagenes" / "ciclo_vida_datos.png"
etapas = ["Problema", "Datos", "Preparacion", "Modelo", "Evaluacion", "Decision"]
fig, ax = plt.subplots(figsize=(10, 2.4))
ax.axis("off")
for i, etapa in enumerate(etapas):
    ax.text(i, 0.5, etapa, ha="center", va="center", bbox={"boxstyle": "round,pad=0.6", "fc": "#d9eaf7", "ec": "#245b78"})
    if i < len(etapas) - 1:
        ax.annotate("", (i + 0.72, 0.5), (i + 0.28, 0.5), arrowprops={"arrowstyle": "->", "lw": 1.5})
ax.text(2.5, 0.05, "retroalimentacion y monitoreo", ha="center", fontsize=10, color="#245b78")
fig.savefig(SALIDA, dpi=160, bbox_inches="tight")
plt.close(fig)
