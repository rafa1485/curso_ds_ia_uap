import random, sys
sys.dont_write_bytecode = True
from banco_datos import BANCO, PARES
B = {q[0]: q for q in BANCO}
L = "abc"

def opciones(q, letra):
    """Ubica la correcta en 'letra' y conserva el orden relativo de los distractores."""
    _, _, _, _, c, d1, d2 = q
    ops = [d1, d2]; i = L.index(letra); ops.insert(i, c); return ops

def secuencia(n, seed):
    base = [L[i % 3] for i in range(n)]
    r = random.Random(seed)
    while True:
        r.shuffle(base)
        if all(len(set(base[i:i+4])) > 1 for i in range(n-3)):
            return base

TITULO = "Parcial 1: Ciencia de Datos 2026"
# Banco
letras_banco = secuencia(len(BANCO), 7)
out = [f"# {TITULO} — Banco de preguntas\n",
       f"Total: {len(BANCO)} preguntas. Fuente: Clases 01–05 (PDF) y capítulos 5 y 9 como respaldo.\n"]
clave = []
for q, le in zip(BANCO, letras_banco):
    n, sem, sec, st = q[:4]
    out.append(f"**{n}.** {st}\n")
    for l, o in zip(L, opciones(q, le)):
        out.append(f"{l}) {o}  ")
    out.append("")
    clave.append(f"| {n} | {le} | Semana {sem} | {sec} |")
out += ["\n## Clave del banco\n", "| N.º | Respuesta | Semana | Sección de origen |", "|---|---|---|---|"] + clave
open("parcial_DS1_banco_preguntas.md", "w").write("\n".join(out) + "\n")

# Grupos
g = [f"# {TITULO} — Grupos\n"]
for gi, nombre in enumerate(["A", "B"]):
    ids = [p[gi] for p in PARES]
    letras = secuencia(len(ids), 100 + gi)
    g.append(f"## Grupo {nombre}\n")
    filas = []
    for k, (n, le) in enumerate(zip(ids, letras), 1):
        q = B[n]
        g.append(f"**{k}.** {q[3]}\n")
        for l, o in zip(L, opciones(q, le)):
            g.append(f"{l}) {o}  ")
        g.append("")
        filas.append(f"| {k} | {le} | {n} | Semana {q[1]} | {q[2]} |")
    g += [f"### Clave Grupo {nombre}\n", "| N.º | Respuesta | N.º banco | Semana | Sección de origen |", "|---|---|---|---|---|"] + filas + [""]
    cnt = {l: letras.count(l) for l in L}
    print(nombre, cnt, "semanas:", {s: sum(B[i][1]==s for i in ids) for s in range(1,6)})
open("parcial_DS1_grupos.md", "w").write("\n".join(g) + "\n")
