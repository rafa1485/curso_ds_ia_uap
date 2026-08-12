---
title: "Representación de problemas y búsqueda"
subtitle: "Estados, grafos y estrategias no informadas"
course: "Inteligencia Artificial"
week: 2
class: 2
language: es
---

# Representación de problemas y búsqueda

## Estados, grafos y estrategias no informadas

**Semana 2 · Clase 2**

---

# Propósito de la clase

Transformar una necesidad operativa en un problema de búsqueda y justificar una estrategia para resolverlo.

Al finalizar, podremos:

- formular un problema mediante estados, acciones, transiciones, objetivo y costos;
- distinguir estado, nodo, camino, frontera y conjunto explorado;
- representar un espacio de estados como grafo;
- comparar búsqueda en anchura, profundidad, profundidad limitada, profundización iterativa y costo uniforme;
- formular una búsqueda sobre el caso transversal de movilidad.

---

# De PEAS a una solución

La clase 1 delimitó:

`desempeño · entorno · actuadores · sensores`

La clase 2 agrega:

`estado · acciones · transición · objetivo · costo · estrategia`

> PEAS define la tarea del agente; la formulación de búsqueda define qué puede explorar el algoritmo.

---

# Pregunta de apertura

> ¿Qué necesita conocer un algoritmo para encontrar una secuencia de decisiones?

- ¿Cómo describe cada situación posible?
- ¿Qué acciones son legales?
- ¿Qué cambia después de actuar?
- ¿Cómo reconoce una solución?
- ¿Qué significa que una solución sea mejor?

---

# Del agente al problema de búsqueda

Un agente deliberativo necesita convertir su decisión en una pregunta computable:

`situación actual → alternativas → consecuencias → objetivo`

La representación determina:

- qué soluciones existen;
- qué acciones parecen legales;
- qué costos se consideran;
- qué diferencias entre situaciones puede reconocer el algoritmo.

---

# Formulación general

$$P=(S,A,T,s_0,G,c)$$

- $S$: espacio de estados.
- $A(s)$: acciones aplicables en $s$.
- $T(s,a)$: estado resultante.
- $s_0$: estado inicial.
- $G(s)$: prueba de objetivo.
- $c(s,a,s')$: costo de transición.

---

# ¿Qué es un estado?

Un estado reúne la información necesaria para:

- decidir qué acciones son legales;
- predecir consecuencias relevantes;
- evaluar si se alcanzó el objetivo;
- calcular costos futuros.

No es una copia completa de la realidad: es una representación orientada a una decisión.

---

# Diseñar variables de estado

Caso de movilidad:

`s = (zona, hora, vehículos disponibles, demanda pendiente)`

Cada variable debe cambiar al menos una de estas respuestas:

- ¿qué puedo hacer?;
- ¿qué ocurrirá?;
- ¿cuánto costará?;
- ¿ya alcancé el objetivo?

---

# Estado, percepción y nodo

| Concepto | Función |
|---|---|
| Estado del mundo | Situación que existe, aunque no se observe por completo |
| Percepción | Evidencia recibida por sensores |
| Estado interno | Estimación mantenida por el agente |
| Nodo de búsqueda | Registro del algoritmo: estado, padre, acción y costo |

Dos nodos pueden contener el mismo estado y representar caminos distintos.

---

# Suficiencia del estado

Un estado es suficiente si conserva la información del pasado que cambia el futuro relevante:

$$P(S_{t+1}\mid S_{0:t},A_{0:t})=P(S_{t+1}\mid S_t,A_t)$$

Si una calle cierra a las 18:00, representar solo la zona no basta: la hora modifica acciones y transiciones.

---

# Acciones, precondiciones y efectos

```text
ACCIÓN trasladar(vehículo, origen, destino)
PRECONDICIONES:
    vehículo disponible en origen
    conexión habilitada
    capacidad y seguridad válidas
EFECTOS:
    disminuye disponibilidad en origen
    aumenta disponibilidad en destino
    avanzan tiempo y costo
```

---

# Modelo de transición

En un problema determinista:

$$s'=T(s,a)$$

La transición debe:

- aplicar los efectos de la acción;
- conservar invariantes;
- incluir consumo de tiempo y recursos;
- separar acciones del agente de eventos externos.

---

# Estado inicial y objetivo

- $s_0$ describe la situación al comenzar la búsqueda.
- $G(s)$ reconoce cualquier estado aceptable.

Ejemplo:

`G(s) = demanda crítica cubierta y restricciones satisfechas`

El objetivo declara el resultado, no el método para alcanzarlo.

---

# Longitud y costo

Para un camino de $k$ acciones:

$$g=\sum_{i=0}^{k-1}c(s_i,a_i,s_{i+1})$$

- Longitud: cantidad de acciones.
- Costo: suma de pesos de las transiciones.

Solo coinciden cuando todas las acciones cuestan una unidad.

---

# Costos y restricciones

| Concepto | Tratamiento | Ejemplo |
|---|---|---|
| Restricción dura | Excluir alternativa | Capacidad máxima |
| Restricción blanda | Penalizar | Evitar reasignaciones |
| Costo | Comparar caminos | Minutos o kilómetros |
| Utilidad | Valorar consecuencias | Riesgo y calidad |

Una ilegalidad no debe convertirse solamente en un costo alto.

---

# Nivel de abstracción

Una representación útil conserva diferencias que cambian decisiones y omite detalles irrelevantes.

- Muy poca abstracción: el espacio se vuelve intratable.
- Demasiada abstracción: aparecen planes imposibles o inseguros.

> El estado correcto depende de la pregunta, el horizonte y las restricciones.

---

# Ejemplo: una red vial

Objetivo: viajar de $A$ a $F$ minimizando minutos.

- Estado: intersección actual.
- Acción: recorrer una calle saliente.
- Transición: llegar al extremo de la calle.
- Objetivo: `estado = F`.
- Costo: tiempo de cada arista.

Si existen horarios o combustible limitado, la intersección deja de ser un estado suficiente.

---

# Grafo dirigido y ponderado

Un grafo $G=(V,E)$ representa:

- vértices como estados;
- aristas como transiciones legales;
- dirección como posibilidad de avance;
- pesos como tiempo, distancia, dinero o riesgo.

El significado de cada peso debe declararse y usar una unidad consistente.

---

# Grafo de estados y árbol de búsqueda

- El **grafo de estados** contiene cada estado y sus transiciones.
- El **árbol de búsqueda** contiene las distintas maneras de llegar a estados.

Un mismo estado puede aparecer varias veces en el árbol con distintos padres o costos.

---

# El nodo de búsqueda

$$n=(estado,padre,acción,g,profundidad)$$

El nodo permite:

- reconstruir el camino solución;
- comparar costos acumulados;
- medir profundidad;
- conservar alternativas que llegan al mismo estado.

---

# La frontera

La frontera reúne nodos generados pero aún no expandidos.

| Política de extracción | Estrategia |
|---|---|
| Cola FIFO | Anchura |
| Pila LIFO | Profundidad |
| Menor costo $g$ | Costo uniforme |

Cambiar la frontera cambia el orden de exploración.

---

# El conjunto explorado

Registra estados ya expandidos para:

- evitar ciclos;
- reducir trabajo repetido;
- reconocer convergencias;
- conservar el mejor costo conocido cuando corresponde.

La clave del estado debe representar igualdad semántica, no identidad del objeto en memoria.

---

# Ciclos y estados repetidos

Un ciclo vuelve a un estado anterior. Una convergencia llega al mismo estado desde caminos diferentes.

Controles posibles:

1. ancestros del camino actual;
2. conjunto de estados descubiertos;
3. mejor costo conocido y reapertura.

---

# Búsqueda en grafo

```text
insertar nodo inicial en frontera
mientras frontera no esté vacía:
    extraer un nodo
    si es objetivo: devolver camino
    registrar su estado como explorado
    para cada sucesor legal:
        calcular nuevo costo
        insertar si es nuevo o mejora el costo
devolver fracaso
```

---

# Tiempo y memoria

- $b$: factor de ramificación.
- $d$: profundidad de la solución menos profunda.
- $m$: profundidad máxima.
- $C^*$: costo óptimo.
- $\varepsilon$: costo mínimo positivo.

Hasta profundidad $d$ pueden aparecer $O(b^d)$ nodos. La mayoría se concentra en el último nivel.

---

# Búsqueda en anchura

La búsqueda en anchura (BFS) expande por niveles:

`profundidad 0 → profundidad 1 → profundidad 2 → ...`

- Frontera: cola FIFO.
- Marca estados al descubrirlos.
- Encuentra primero una solución de menor profundidad.

---

# BFS paso a paso

En cada iteración:

1. desencolar el nodo más antiguo;
2. comprobar el objetivo;
3. generar sucesores no descubiertos;
4. encolarlos al final.

La frontera conserva casi todo el nivel más reciente: la memoria es su principal limitación.

---

# Garantías de BFS

BFS es:

- completa si $b$ es finito y existe una solución a profundidad finita;
- óptima si todas las acciones tienen el mismo costo;
- no óptima con aristas de pesos diferentes;
- costosa en memoria: tiempo y espacio $O(b^d)$.

---

# Búsqueda en profundidad

La búsqueda en profundidad (DFS) expande el nodo más profundo disponible.

- Frontera: pila LIFO o recursión.
- Sigue una rama y luego retrocede.
- Usa menos memoria que BFS.
- Puede quedar atrapada en ramas profundas o ciclos.

---

# DFS paso a paso

El orden de sucesores determina qué rama se recorre primero.

DFS resulta útil cuando:

- la memoria es crítica;
- las soluciones pueden ser profundas;
- cualquier solución es aceptable.

No garantiza el camino más corto ni el de menor costo.

---

# Profundidad limitada

La búsqueda de profundidad limitada impide expandir más allá de $\ell$.

Debe distinguir:

- solución;
- fracaso verdadero;
- corte por alcanzar el límite.

Un límite operativo justificable es mejor que un número arbitrario.

---

# Profundización iterativa

Ejecuta profundidad limitada con límites crecientes:

`0, 1, 2, 3, ...`

Combina:

- completitud y optimalidad por profundidad de BFS;
- memoria lineal de DFS;
- repetición controlada de niveles poco profundos.

---

# Búsqueda de costo uniforme

La búsqueda de costo uniforme (UCS) extrae el nodo con menor $g$.

- Frontera: cola de prioridad.
- Expande por costo acumulado, no por profundidad.
- Conserva el menor costo conocido por estado.
- Es óptima con costos no negativos y condiciones de terminación apropiadas.

---

# Comparación de estrategias

| Estrategia | Frontera | Completa | Óptima | Riesgo principal |
|---|---|---|---|---|
| BFS | FIFO | Sí* | Costos iguales | Memoria |
| DFS | LIFO | No general | No | Rama infinita |
| Limitada | LIFO + límite | Si $\ell\ge d$* | No | Límite incorrecto |
| Iterativa | Límites crecientes | Sí* | Costos iguales | Repetición |
| UCS | Prioridad por $g$ | Sí* | Sí* | Memoria y prioridad |

`*` Bajo los supuestos declarados.

---

# Caso transversal: movilidad como grafo

- Estado: zona y configuración relevante de la flota.
- Acción: trasladar un vehículo a una zona conectada.
- Transición: actualizar ubicación, tiempo y disponibilidad.
- Objetivo: cubrir demanda crítica respetando capacidad.
- Costo: demora esperada más distancia vacía.

El grafo es una simplificación del sistema, no una copia de la ciudad.

---

# Actividad guiada

En equipos, construir una instancia con 5 a 7 estados:

1. definir $S,A,T,s_0,G,c$;
2. dibujar el grafo y asignar pesos;
3. ejecutar BFS y costo uniforme;
4. registrar orden de expansión, camino y costo;
5. explicar por qué coinciden o difieren;
6. identificar una variable omitida que cambiaría la solución.

**Tiempo:** 30 minutos + 10 minutos de contraste.

---

# Síntesis

- Representar es decidir qué diferencias cambian acciones y costos.
- Estado y nodo no son sinónimos.
- La frontera define el orden de exploración.
- El conjunto explorado controla repetidos y ciclos.
- Longitud y costo solo coinciden con costos unitarios.
- Ninguna estrategia domina bajo todos los criterios.
- Las garantías dependen de supuestos explícitos.

---

# Lecturas y continuidad

## Lectura principal

- Capítulo 6, sección 6.4: representación computacional de problemas.
- Capítulo 7, secciones 7.1 y 7.2: espacios de estados y búsqueda no informada.

## Próxima clase

- heurísticas;
- búsqueda voraz;
- algoritmo A*;
- admisibilidad y consistencia.
