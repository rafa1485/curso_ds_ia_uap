---
title: "Panorama de métodos de Inteligencia Artificial"
subtitle: "Modelos, interacción, lenguaje y aprendizaje distribuido"
author: "Curso de Inteligencia Artificial"
course: "Inteligencia Artificial"
week: 8
class: 8
lang: es
---

# Panorama de métodos de Inteligencia Artificial

## Modelos, interacción, lenguaje y aprendizaje distribuido

**Semana 8 · Clase 8**

**Recorrido conceptual:** `señal → representación → aprendizaje → salida → evaluación`

---

# Propósito de la clase

Comprender los principios que distinguen varias familias centrales de Inteligencia Artificial y reconocer qué aprende cada una.

Al finalizar podremos:

- explicar SVM, redes neuronales y ensambles;
- describir el ciclo de aprendizaje por refuerzo;
- seguir el recorrido desde texto hasta un modelo de lenguaje;
- explicar el aprendizaje federado;
- comparar señales, salidas, fortalezas y límites.

---

# SVM: separar con margen

Una máquina de soporte vectorial busca una frontera que separe clases y deje el mayor margen posible.

Para un clasificador lineal:

$$
f(\mathbf{x})=\mathbf{w}^{\mathsf T}\mathbf{x}+b,
\qquad
\widehat y=\operatorname{sign}(f(\mathbf{x})).
$$

La frontera está dada por $f(\mathbf{x})=0$. El vector $\mathbf{w}$ determina su orientación y $b$ su desplazamiento.

---

# Margen máximo

Si varias fronteras clasifican correctamente los datos, SVM prefiere la que maximiza la distancia a los ejemplos más cercanos.

$$
\text{ancho del margen}=\frac{2}{\|\mathbf{w}\|_2}.
$$

Un margen amplio busca una separación menos dependiente de pequeñas variaciones de la muestra.

## Vectores de soporte

Los **vectores de soporte** son los ejemplos situados sobre el margen o que lo violan.

- Determinan la posición de la frontera.
- Casos alejados suelen no cambiar la solución.
- El método se concentra en los ejemplos geométricamente críticos.

La frontera depende de los casos cercanos, no de un promedio global de cada clase.

---

# Margen blando y kernels

En datos reales puede ser imposible separar sin errores. El parámetro $C$ regula el equilibrio entre margen amplio y penalización de violaciones.

Un kernel calcula semejanza en una representación implícita:

$$
K(\mathbf{x},\mathbf{z})=\phi(\mathbf{x})^{\mathsf T}\phi(\mathbf{z}).
$$

- Kernel lineal: frontera lineal en las variables disponibles.
- Kernel RBF: fronteras curvas según distancias locales.
- Escalado y selección de hiperparámetros son parte del pipeline.

---

# Ejemplo SVM: riesgo operativo

Se representan eventos mediante demora estimada y congestión.

1. Un SVM lineal busca una recta de separación entre riesgo bajo y alto.
2. Los eventos cercanos a la frontera se convierten en vectores de soporte.
3. Si la separación es curva, un kernel RBF puede representarla.
4. La puntuación respecto de la frontera no es automáticamente una probabilidad calibrada.

La acción posterior todavía requiere costos, capacidad y supervisión.

---

# Red neuronal: una unidad básica

Una neurona artificial combina entradas y aplica una activación:

$$
z=\mathbf{w}^{\mathsf T}\mathbf{x}+b,
\qquad a=\phi(z).
$$

- Los pesos controlan cuánto influye cada entrada.
- El sesgo desplaza el umbral.
- La activación introduce una transformación, generalmente no lineal.

Sin activaciones no lineales, apilar capas seguiría produciendo una transformación lineal.

---

# Funciones de activación

| Activación | Expresión o rango | Uso frecuente |
|---|---|---|
| Sigmoide | $(0,1)$ | salida binaria |
| Tanh | $(-1,1)$ | estados centrados |
| ReLU | $\max(0,z)$ | capas ocultas |
| Softmax | probabilidades que suman 1 | salida multiclase |

La activación de salida debe ser coherente con la tarea y la función de pérdida.

---

# Capas y representaciones

Una red multicapa compone transformaciones:

$$
\mathbf{h}^{(\ell)}=
\phi\!\left(W^{(\ell)}\mathbf{h}^{(\ell-1)}+\mathbf{b}^{(\ell)}\right).
$$

- Entrada: variables observadas.
- Capas ocultas: representaciones intermedias aprendidas.
- Salida: cantidad, clase, probabilidad u otra estructura.

La profundidad permite construir relaciones complejas mediante composiciones sucesivas.

## Propagación hacia adelante

Durante la inferencia, la información avanza desde la entrada hasta la salida:

`entrada → transformación → activación → ... → predicción`

Cada capa recibe la representación anterior. La predicción final depende de todos los pesos y sesgos recorridos.

La propagación hacia adelante calcula una salida; todavía no modifica el modelo.

---

# Pérdida y retropropagación

El entrenamiento repite cuatro pasos:

1. calcular una predicción;
2. medir el desacuerdo con una función de pérdida;
3. propagar gradientes desde la salida hacia las capas anteriores;
4. actualizar parámetros con un optimizador.

$$
\theta \leftarrow \theta-\eta\nabla_{\theta}L.
$$

La retropropagación calcula gradientes; el descenso del gradiente usa esos gradientes para ajustar parámetros.

La validación orienta arquitectura, regularización y parada; la prueba estima desempeño final bajo el protocolo fijado.

---

# Ejemplo neuronal: relación XOR

XOR devuelve 1 cuando dos entradas binarias son diferentes.

| $x_1$ | $x_2$ | $y$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Una sola frontera lineal no separa estos casos. Una capa oculta puede construir regiones intermedias y combinarlas en una salida no lineal.

---

# Ensemble Learning: combinar modelos

Un ensamble agrega predicciones de varios modelos:

$$
\widehat f(\mathbf{x})=
\sum_{m=1}^{M}\alpha_m f_m(\mathbf{x}).
$$

La mejora aparece cuando los modelos son razonablemente competentes y sus errores no coinciden por completo.

Combinar copias idénticas con los mismos errores aporta poco.

---

# Bagging y Random Forest

**Bagging** entrena modelos en paralelo sobre muestras bootstrap y luego promedia o vota.

**Random Forest** añade diversidad al permitir que cada división considere solo una selección aleatoria de variables.

`muestras diferentes → árboles diferentes → promedio o voto`

El objetivo principal es reducir la variabilidad de un árbol individual.

---

# Boosting

Boosting construye un modelo aditivo de forma secuencial:

$$
F_M(x)=F_0(x)+\sum_{m=1}^{M}\nu h_m(x).
$$

Cada nuevo modelo busca corregir parte del error actual. La tasa $\nu$ controla el tamaño de cada corrección.

No es una votación independiente: los modelos posteriores dependen de los anteriores.

---

# Ejemplo de ensamble

Para estimar riesgo de demora:

- un árbol puede cambiar mucho ante pequeñas variaciones;
- Random Forest promedia muchos árboles decorrelacionados;
- boosting añade árboles pequeños que corrigen residuos;
- stacking puede aprender cómo combinar familias diferentes.

La evaluación debe usar la misma partición, información y métrica para todos los modelos.

---

# Aprendizaje por refuerzo

En aprendizaje supervisado, una etiqueta indica la respuesta esperada. En RL, un agente actúa, observa consecuencias y aprende una política.

$$
S_t \rightarrow A_t \rightarrow R_{t+1},S_{t+1}.
$$

La señal puede llegar con demora y cada acción puede cambiar las experiencias futuras.

---

# Ciclo agente-entorno

- El **estado** resume la información relevante.
- La **acción** es una alternativa disponible.
- La **transición** describe cómo evoluciona el entorno.
- La **recompensa** aporta una señal inmediata.
- La **política** asigna acciones a estados.

`estado → agente → acción → entorno → recompensa y nuevo estado`

---

# Retorno y descuento

El objetivo no suele ser maximizar solo la recompensa inmediata, sino el retorno:

$$
G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots,
\qquad 0\leq\gamma<1.
$$

$\gamma$ regula cuánto pesan consecuencias futuras. Una acción costosa ahora puede ser conveniente si evita pérdidas posteriores.

## Funciones de valor

El valor de un estado resume el retorno esperado desde ese estado:

$$
V^{\pi}(s)=\mathbb{E}_{\pi}[G_t\mid S_t=s].
$$

El valor de una acción permite comparar alternativas:

$$
Q^{\pi}(s,a)=\mathbb{E}_{\pi}[G_t\mid S_t=s,A_t=a].
$$

Una política puede elegir la acción con mayor valor estimado, respetando restricciones de exploración y seguridad.

---

# Exploración y explotación

- **Explotar:** elegir la acción que actualmente parece mejor.
- **Explorar:** probar alternativas para obtener información.

Solo explotar puede fijar una política prematura. Explorar sin control puede ser costoso o inseguro.

La estrategia $\varepsilon$-greedy elige una acción aleatoria con probabilidad $\varepsilon$ y la mejor conocida en el resto de los casos.

---

# Q-learning como ejemplo

Q-learning actualiza una estimación a partir de la transición observada:

$$
Q(s,a)\leftarrow Q(s,a)+\alpha
\left[r+\gamma\max_{a'}Q(s',a')-Q(s,a)\right].
$$

El término entre corchetes compara la estimación actual con recompensa inmediata más mejor valor futuro estimado.

---

# Ejemplo RL: asignación secuencial

Un agente decide dónde posicionar un recurso móvil.

| Elemento | Ejemplo |
|---|---|
| Estado | zona, hora, congestión y disponibilidad |
| Acción | mantener, mover o esperar |
| Recompensa | servicio logrado menos traslado y demora |
| Política | regla aprendida para seleccionar acciones |

Una recompensa incompleta puede producir conductas indeseadas aunque el algoritmo la optimice correctamente.

---

# NLP: del texto a una tarea

El procesamiento del lenguaje natural transforma lenguaje en representaciones computables:

`texto → tokens → representación numérica → modelo → salida`

Las salidas pueden ser una clase, entidades, una respuesta, un resumen o una distribución sobre próximos tokens.

## Corpus y tokenización

- Corpus: colección de documentos usada para análisis o aprendizaje.
- Token: unidad procesada por el modelo.
- Vocabulario: conjunto de tokens disponibles.

Los tokens pueden ser palabras, subpalabras, caracteres o símbolos especiales. La tokenización determina qué unidades puede observar directamente el modelo.

---

# Representaciones dispersas

Bag of Words representa un documento mediante conteos. TF-IDF reduce el peso de términos frecuentes en muchos documentos:

$$
\operatorname{tfidf}(t,d)=\operatorname{tf}(t,d)
\log\frac{N}{\operatorname{df}(t)}.
$$

Son baselines útiles e interpretables, pero pierden gran parte del orden y del contexto.

---

# Embeddings

Un embedding asigna a cada unidad un vector denso:

$$
\text{token}\longrightarrow \mathbf{e}\in\mathbb{R}^{d}.
$$

Los embeddings distribucionales aproximan semejanzas de uso. Los embeddings contextuales cambian según la oración.

“Banco” necesita representaciones distintas en “banco financiero” y “banco de la plaza”.

---

# Atención

La atención pondera qué elementos son relevantes para cada posición:

$$
\operatorname{Attention}(Q,K,V)=
\operatorname{softmax}\left(\frac{QK^{\mathsf T}}{\sqrt{d_k}}\right)V.
$$

- Consulta $Q$: qué información busca la posición actual.
- Claves $K$: cómo se describe cada posición disponible.
- Valores $V$: información que se combina.

---

# Transformer simplificado

Un Transformer combina:

1. embeddings de tokens y posición;
2. atención para intercambiar información entre posiciones;
3. redes feed-forward por posición;
4. conexiones residuales y normalización;
5. varias capas apiladas.

La arquitectura permite procesar dependencias contextuales sin recurrencia paso a paso durante el entrenamiento.

---

# Modelos de lenguaje

Un modelo de lenguaje asigna probabilidades a secuencias. En generación autorregresiva:

$$
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t}).
$$

Un LLM es un modelo de lenguaje con gran escala de parámetros, datos y cómputo. El modelo produce distribuciones de tokens; una aplicación conversacional añade interfaz, instrucciones y herramientas.

---

# Ejemplo de generación

Contexto: “La capital de Argentina es”

| Token candidato | Probabilidad ilustrativa |
|---|---:|
| Buenos | 0,72 |
| Córdoba | 0,08 |
| una | 0,05 |
| grande | 0,02 |

Se selecciona un token, se añade al contexto y se repite el proceso. La temperatura y la estrategia de decodificación modifican diversidad y determinismo.

---

# Fluidez no equivale a verdad

El objetivo de predecir tokens no verifica automáticamente afirmaciones.

- Una salida probable puede ser falsa.
- El contexto puede ser insuficiente o ambiguo.
- Datos de entrenamiento pueden contener sesgos.
- Recuperar fuentes ayuda, pero no elimina la necesidad de validación.

La evaluación debe corresponder al uso: exactitud factual, cobertura, robustez, seguridad y trazabilidad.

---

# Aprendizaje federado

El aprendizaje federado entrena un modelo compartido sin reunir todos los datos brutos en un único repositorio.

`modelo global → entrenamiento local → actualizaciones → agregación → nuevo modelo global`

Es una organización del entrenamiento, no una familia de predicción: el modelo local puede ser una red, un modelo lineal u otra arquitectura compatible.

---

# Una ronda de FedAvg

En una ronda típica:

1. el servidor distribuye parámetros $\theta_t$;
2. cada cliente ajusta localmente y obtiene $\theta_t^{(k)}$;
3. los clientes envían actualizaciones;
4. el servidor calcula un promedio ponderado:

$$
\theta_{t+1}=\sum_{k=1}^{K}\frac{n_k}{\sum_j n_j}\theta_t^{(k)}.
$$

El proceso se repite durante varias rondas.

---

# Ejemplo federado

Varios hospitales desean mejorar un clasificador sin centralizar historias clínicas.

- Cada institución conserva sus registros.
- Entrena localmente una copia del modelo.
- Comparte actualizaciones con un coordinador.
- El coordinador agrega y redistribuye el modelo.

El resultado puede fallar si poblaciones, mediciones o tamaños difieren mucho entre instituciones.

---

# Federado no significa privado por sí solo

Las actualizaciones pueden revelar información y el servidor puede ser un punto de ataque.

Controles posibles:

- agregación segura;
- privacidad diferencial;
- autenticación y validación de clientes;
- evaluación global y por cliente;
- límites frente a actualizaciones maliciosas.

También deben considerarse comunicación, clientes intermitentes y datos no idénticamente distribuidos.

---

# Comparación final

| Método | Señal principal | Qué aprende | Salida típica |
|---|---|---|---|
| SVM | etiquetas | frontera de margen | clase o puntuación |
| Red neuronal | pérdida | transformaciones compuestas | predicción o representación |
| Ensamble | errores etiquetados | combinación de modelos | predicción agregada |
| RL | recompensas | política o valores | acción |
| NLP / LLM | texto, etiquetas o próximos tokens | representación y distribución lingüística | clase, extracción o texto |
| Federado | actualizaciones locales | parámetros compartidos | modelo global |

---

# Síntesis

- SVM selecciona una frontera mediante margen y ejemplos críticos.
- Las redes aprenden composiciones no lineales mediante gradientes.
- Los ensambles aprovechan diversidad entre predictores.
- RL aprende decisiones secuenciales a partir de recompensas.
- NLP convierte lenguaje en representaciones; los LLM generan token a token.
- El aprendizaje federado distribuye el ajuste, pero no garantiza privacidad.
- Elegir un método exige alinear señal, salida, evaluación y condiciones de uso.

---

# Lecturas

**Modelos supervisados y distribuidos**

- Capítulo 12, §§12.2–12.4: SVM, ensambles y aprendizaje federado.
- Capítulo 15, §§15.1–15.2: redes neuronales y entrenamiento.

**Decisiones y lenguaje**

- Capítulo 8, §§8.2 y 8.4: decisiones secuenciales y aprendizaje por refuerzo.
- Capítulo 16, §§16.1, 16.3 y 16.4: NLP, Transformer y modelos de lenguaje.
