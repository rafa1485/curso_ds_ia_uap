---
title: "Modelos supervisados fundamentales"
subtitle: "De funciones aprendidas a decisiones"
author: "Curso de Inteligencia Artificial"
course: "Inteligencia Artificial"
week: 7
class: 7
lang: es
---

# Modelos supervisados fundamentales

## De funciones aprendidas a decisiones

**Semana 7 · Clase 7**

**Recorrido conceptual:** `ejemplos → función → predicción → decisión`

---

# Propósito de la clase

Comprender qué aprende un modelo supervisado y cómo su salida puede informar la acción de un agente.

Al finalizar podremos:

- formular regresión y clasificación;
- explicar el ajuste de una regresión lineal;
- interpretar la probabilidad producida por una regresión logística;
- distinguir probabilidad, clase y acción;
- explicar cómo aprende un árbol de decisión;
- comparar un modelo lineal, un árbol y un ensamble.

---

# Punto de partida

Ya estudiamos un agente que decide con una creencia conocida:

`evidencia → probabilidad del estado → costo esperado → acción`

Ahora la probabilidad o el valor esperado no vienen dados. Se estiman a partir de ejemplos:

`(x_i,y_i) → modelo ajustado → predicción para x nuevo`

**Pregunta nueva:** ¿qué relación aprende cada familia de modelos?

---

# Caso conductor: movilidad

Treinta minutos antes de una salida, un agente debe anticipar el estado de un trayecto.

| Elemento | Ejemplo |
|---|---|
| Entradas $x$ | duración planificada, congestión, lluvia, franja horaria |
| Objetivo continuo | minutos de demora |
| Objetivo binario | demora mayor que 10 minutos: sí/no |
| Acción posterior | mantener, reasignar o solicitar revisión |

El mismo dominio admite modelos distintos según la salida que necesitamos.

---

# Aprendizaje supervisado

Disponemos de ejemplos con entrada y respuesta observada:

$$
\mathcal D=\{(x_1,y_1),\ldots,(x_n,y_n)\}.
$$

El algoritmo selecciona una función dentro de una familia:

$$
\widehat f=\arg\min_{f\in\mathcal F}\frac{1}{n}\sum_{i=1}^{n}L(y_i,f(x_i)).
$$

- $\mathcal F$: funciones que el modelo puede representar.
- $L$: penalización por una predicción incorrecta.
- Aprender significa ajustar la función, no almacenar una tabla de respuestas.

---

# Tarea, modelo y decisión

| Nivel | Pregunta |
|---|---|
| Tarea | ¿Qué salida necesitamos estimar? |
| Modelo | ¿Qué familia de funciones utilizaremos? |
| Ajuste | ¿Qué criterio determina sus parámetros? |
| Decisión | ¿Cómo convertimos la salida en una acción? |

**Distinción central:** un modelo predice; la regla de decisión incorpora costos, capacidad y restricciones.

---

# Regresión o clasificación

| Tarea | $y$ | Salida del modelo | Caso de movilidad |
|---|---|---|---|
| Regresión | número real | $\widehat y$ | demora estimada: 14,2 min |
| Clasificación binaria | $0$ o $1$ | $\widehat p=P(Y=1\mid x)$ | probabilidad de demora crítica |

Una etiqueta final puede obtenerse con un umbral, pero el puntaje probabilístico contiene más información que la clase rígida.

---

# Regresión lineal: hipótesis

La regresión lineal aproxima la media del objetivo mediante una función afín:

$$
\widehat y=\beta_0+\beta_1x_1+\cdots+\beta_px_p.
$$

- $\beta_0$: valor de referencia.
- $\beta_j$: cambio asociado con una unidad de $x_j$, manteniendo las demás entradas fijas.
- “Lineal” se refiere a los parámetros; pueden incluirse transformaciones e interacciones.

---

# Ejemplo de una recta

Horas de operación:

$$x=(2,4,6,8,10)$$

Consumo energético en MWh:

$$y=(18,25,29,36,42)$$

La recta ajustada es:

$$
\widehat y=12{,}3+2{,}95x.
$$

Para $x=7$, predice $\widehat y=32{,}95$ MWh.

---

# ¿Qué significa ajustar la recta?

El residuo del caso $i$ es:

$$
e_i=y_i-\widehat y_i.
$$

Mínimos cuadrados elige los parámetros que minimizan:

$$
S(\beta)=\sum_{i=1}^{n}(y_i-\widehat y_i)^2.
$$

Los errores grandes pesan más porque se elevan al cuadrado. La función de pérdida define qué ajuste considera preferible el modelo.

---

# La solución en regresión simple

Para una sola entrada:

$$
\widehat\beta_1=
\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}
{\sum_i(x_i-\bar x)^2},
\qquad
\widehat\beta_0=\bar y-\widehat\beta_1\bar x.
$$

La pendiente es covarianza dividida por varianza de $x$.

**Lectura:** $2{,}95$ MWh adicionales por cada hora de operación dentro del rango estudiado.

---

# Interpretar sin exagerar

Un coeficiente permite describir una asociación condicionada al modelo.

No demuestra por sí solo que:

- modificar $x_j$ causará el cambio predicho;
- la relación continuará fuera del rango observado;
- las entradas omitidas son irrelevantes;
- el mismo coeficiente vale en otra población o período.

**Asociación predictiva no equivale a efecto causal.**

---

# Residuos: qué no explicó el modelo

Revisar residuos permite detectar límites de la forma elegida:

- curvatura: falta una relación no lineal;
- dispersión creciente: cambia la variabilidad del error;
- grupos separados: falta una diferencia relevante;
- observaciones extremas: pueden dominar el ajuste;
- patrón temporal: los errores no son independientes.

Un error sistemático no se corrige agregando decimales a la predicción.

---

# Regresión lineal en movilidad

Ejemplo ilustrativo:

$$
\widehat{demora}=
-4+0{,}18\,duración+6{,}2\,congestión+3{,}1\,lluvia.
$$

Para duración 40 min, congestión 0,7 y lluvia 1:

$$
\widehat{demora}=-4+0{,}18(40)+6{,}2(0{,}7)+3{,}1=10{,}64.
$$

La salida conserva la unidad: minutos de demora.

---

# ¿Por qué no usar una recta para probabilidades?

Si $Y\in\{0,1\}$, una recta puede producir valores menores que 0 o mayores que 1.

Necesitamos:

1. un puntaje que combine las entradas;
2. una transformación que lo lleve al intervalo $[0,1]$.

La regresión logística utiliza un puntaje lineal y una función sigmoide.

---

# Regresión logística

Primero calcula:

$$
\eta=\beta_0+\beta_1x_1+\cdots+\beta_px_p.
$$

Luego transforma el puntaje:

$$
\widehat p=\sigma(\eta)=\frac{1}{1+e^{-\eta}}.
$$

- $\eta$ puede tomar cualquier valor real.
- $\widehat p$ siempre pertenece a $(0,1)$.
- $\sigma(0)=0{,}5$.

---

# Puntaje, probabilidad, clase y acción

| Objeto | Ejemplo | Función |
|---|---:|---|
| Puntaje $\eta$ | 0,8 | evidencia combinada por el modelo |
| Probabilidad $\widehat p$ | 0,69 | riesgo estimado del evento |
| Clase | demora crítica | resultado de aplicar un umbral |
| Acción | reasignar vehículo | decisión según costo y restricciones |

Confundir estos cuatro objetos oculta dónde se producen los errores.

---

# Ejemplo numérico de la sigmoide

Supongamos:

$$
\eta=-3+0{,}8x.
$$

Para $x=4$:

$$
\eta=0{,}2,
\qquad
\widehat p=\frac{1}{1+e^{-0{,}2}}\approx0{,}55.
$$

Para $x=5$, $\eta=1$ y $\widehat p\approx0{,}731$.

El incremento de probabilidad no es constante: depende del punto de partida.

---

# Odds y coeficientes

La regresión logística es lineal en los log-odds:

$$
\log\frac{p}{1-p}=\beta_0+\sum_j\beta_jx_j.
$$

Si $x_j$ aumenta una unidad, los odds se multiplican por $e^{\beta_j}$, manteniendo las demás entradas fijas.

Si $\beta_j=0{,}40$, $e^{0{,}40}\approx1{,}49$: los odds aumentan 49%, no la probabilidad en 49 puntos.

---

# ¿Cómo se ajusta la logística?

Para cada caso observado:

$$
Y_i\sim Bernoulli(p_i).
$$

El ajuste minimiza la log-loss:

$$
-\ell(\beta)=-\sum_i\left[y_i\log p_i+(1-y_i)\log(1-p_i)\right].
$$

Una probabilidad alta asignada a la clase equivocada recibe una penalización grande. El ajuste es iterativo; no existe la fórmula cerrada de mínimos cuadrados.

---

# Probabilidad no significa certeza

Una salida $\widehat p=0{,}8$ significa que el modelo asigna 80% de probabilidad bajo sus datos y supuestos.

No significa que:

- el evento ocurrirá;
- el modelo acierta 80% en cualquier población;
- la probabilidad está bien calibrada;
- deba ejecutarse automáticamente una acción.

La calidad probabilística se comprueba con casos no usados para ajustar.

---

# De probabilidad a acción

Decidir si actuar tiene dos errores posibles:

- actuar y que el evento no ocurra (falso positivo): costo $C_{FP}$;
- no actuar y que el evento ocurra (falso negativo): costo $C_{FN}$.

Se actúa cuando el costo esperado de actuar es menor que el de no actuar:

$$
(1-\widehat p)\,C_{FP}<\widehat p\,C_{FN}
\qquad\Longleftrightarrow\qquad
\widehat p>\frac{C_{FP}}{C_{FP}+C_{FN}}.
$$

Con $C_{FP}=8$ y $C_{FN}=40$:

$$
t=\frac{8}{48}\approx0{,}167.
$$

Si un falso negativo cuesta más que un falso positivo ($40>8$), conviene actuar incluso con probabilidades bajas: el umbral desciende por debajo de $0{,}5$.

El umbral 0,5 no es universal: depende de consecuencias, capacidad y restricciones.

---

# Caso conductor: probabilidad de demora

Modelo ilustrativo:

$$
\eta=-3+0{,}04\,duración+2{,}2\,congestión+0{,}8\,lluvia.
$$

Para duración 40, congestión 0,7 y lluvia 1:

$$
\eta=-3+1{,}6+1{,}54+0{,}8=0{,}94,
$$

$$
\widehat p=\sigma(0{,}94)\approx0{,}719.
$$

La regla posterior decide si ese riesgo justifica intervenir.

---

# Límite compartido de los modelos lineales

Regresión lineal y logística combinan entradas mediante una suma ponderada.

Esto favorece:

- interpretación y cálculo eficiente;
- comportamiento estable con pocos datos;
- una frontera lineal en el espacio representado.

Pero exige incorporar explícitamente curvaturas e interacciones que sean importantes.

---

# Árbol de decisión

Un árbol aprende una secuencia de preguntas:

```text
¿congestión > 0,65?
├── sí: ¿llueve?
│   ├── sí  → riesgo alto
│   └── no  → riesgo medio
└── no      → riesgo bajo
```

Cada hoja contiene una predicción basada en los ejemplos que llegan a ella.

---

# ¿Cómo elige una división?

El árbol prueba atributos y umbrales y mide la impureza de cada nodo con el índice de Gini:

$$
G=1-p^2-(1-p)^2=2p(1-p),
$$

donde $p$ es la proporción de una de las clases en el nodo.

- $G=0$: nodo puro (una sola clase).
- $G=0{,}5$: clases equilibradas (máxima mezcla).

Se elige la división que más reduce la impureza, comparando la del padre con la suma ponderada de la de las hijas.

**Lectura:** $G$ es la probabilidad de que dos ejemplos tomados al azar del nodo tengan etiquetas distintas. Un padre $50/50$ ($G=0{,}5$) dividido en hijas $80/20$ y $20/80$ ($G=0{,}32$) deja la impureza ponderada en $0{,}32$, menor que la del padre.

---

# Capacidad e inestabilidad del árbol

Un árbol profundo puede:

- representar relaciones no lineales e interacciones;
- aislar pocos ejemplos y memorizar ruido;
- cambiar mucho ante pequeñas variaciones de los datos;
- producir probabilidades extremas en hojas pequeñas.

Profundidad, tamaño mínimo de hoja y poda controlan la complejidad.

---

# Por qué combinar árboles

Los ensambles aprovechan que modelos distintos cometen errores diferentes.

| Método | Mecanismo | Efecto buscado |
|---|---|---|
| Bagging | árboles sobre remuestras | reducir varianza |
| Random Forest | remuestras y atributos aleatorios | aumentar diversidad |
| Boosting | árboles secuenciales que corrigen errores | reducir error de forma progresiva |

Más modelos no reparan etiquetas incorrectas, fuga o cambio de población.

---

# Random Forest

Un bosque aleatorio:

1. obtiene varias remuestras de los ejemplos;
2. crece un árbol en cada remuestra;
3. considera solo algunos atributos en cada división;
4. promedia probabilidades o predicciones.

El promedio estabiliza árboles individuales; la selección aleatoria evita que todos repitan las mismas primeras divisiones.

---

# Boosting

Boosting construye un modelo aditivo:

$$
F_M(x)=F_0(x)+\sum_{m=1}^{M}\nu\,h_m(x).
$$

Cada árbol nuevo intenta corregir parte del error actual.

- $\nu$: tasa de aprendizaje.
- Árboles pequeños: correcciones acotadas.
- Muchas iteraciones: mayor capacidad y mayor necesidad de control.

No es votación independiente: el aprendizaje es secuencial.

---

# Comparación de familias

| Aspecto | Lineal / logística | Árbol | Ensamble de árboles |
|---|---|---|---|
| Relación aprendida | suma ponderada | reglas por regiones | combinación de regiones |
| Interacciones | deben declararse | automáticas | automáticas |
| Interpretación | coeficientes | reglas si es pequeño | más difícil |
| Extrapolación | posible, con riesgo | pobre | pobre |
| Estabilidad | generalmente alta | baja | mayor que un árbol |

Ninguna familia domina en todos los problemas.

---

# Cómo elegir un punto de partida

- Salida numérica y relación aproximadamente suave: regresión lineal.
- Probabilidad binaria interpretable: regresión logística.
- Reglas no lineales e interacciones: árbol controlado.
- Datos tabulares con prioridad predictiva: Random Forest o boosting.

La comparación debe mantener la misma tarea, información disponible y criterio de uso.

# Lecturas

## Lectura principal

- Capítulo 11, secciones 11.1.1--11.1.5: regresión lineal.
- Capítulo 11, secciones 11.4.1--11.4.5: regresión logística y clasificación.
- Capítulo 12, secciones 12.1.1--12.1.5: árboles de decisión.

## Para ampliar

- Capítulo 12, secciones 12.3.1--12.3.5: ensambles, Random Forest y boosting.
