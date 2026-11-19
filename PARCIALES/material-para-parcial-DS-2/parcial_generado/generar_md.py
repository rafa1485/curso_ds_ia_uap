import random, sys
sys.dont_write_bytecode = True
from banco_datos import BANCO, PARES, TITULO, NOMBRE, FUENTE, BLOQUES
B = {q[0]: q for q in BANCO}
L = "abc"
def opciones(q, letra):
    ops = [q[5], q[6]]; ops.insert(L.index(letra), q[4]); return ops
def secuencia(n, seed):
    base = [L[i % 3] for i in range(n)]; r = random.Random(seed)
    while True:
        r.shuffle(base)
        if all(len(set(base[i:i+4])) > 1 for i in range(n-3)): return base
out = [f"# {TITULO} — Banco de preguntas\n", f"Total: {len(BANCO)} preguntas. Fuente: {FUENTE}\n"]; clave = []
for q, le in zip(BANCO, secuencia(len(BANCO), 7)):
    out.append(f"**{q[0]}.** {q[3]}\n")
    out += [f"{l}) {o}  " for l, o in zip(L, opciones(q, le))] + [""]
    clave.append(f"| {q[0]} | {le} | {BLOQUES[q[1]]} | {q[2]} |")
out += ["\n## Clave del banco\n", "| N.º | Respuesta | Bloque | Sección de origen |", "|---|---|---|---|"] + clave
open(f"{NOMBRE}_banco_preguntas.md", "w").write("\n".join(out) + "\n")
g = [f"# {TITULO} — Grupos\n"]
for gi, nombre in enumerate(["A", "B"]):
    ids = [p[gi] for p in PARES]; letras = secuencia(len(ids), 200 + gi)
    g.append(f"## Grupo {nombre}\n"); filas = []
    for k, (n, le) in enumerate(zip(ids, letras), 1):
        q = B[n]; g.append(f"**{k}.** {q[3]}\n")
        g += [f"{l}) {o}  " for l, o in zip(L, opciones(q, le))] + [""]
        filas.append(f"| {k} | {le} | {n} | {BLOQUES[q[1]]} | {q[2]} |")
    g += [f"### Clave Grupo {nombre}\n", "| N.º | Respuesta | N.º banco | Bloque | Sección de origen |", "|---|---|---|---|---|"] + filas + [""]
    print(nombre, {l: letras.count(l) for l in L}, {BLOQUES[b]: sum(B[i][1]==b for i in ids) for b in BLOQUES})
open(f"{NOMBRE}_grupos.md", "w").write("\n".join(g) + "\n")
