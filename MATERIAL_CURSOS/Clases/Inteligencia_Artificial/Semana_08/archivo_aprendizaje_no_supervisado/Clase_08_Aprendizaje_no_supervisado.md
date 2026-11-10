---
title: "Aprendizaje no supervisado"
subtitle: "De la semejanza a segmentos e hipótesis"
author: "Curso de Inteligencia Artificial"
course: "Inteligencia Artificial"
week: 8
class: 8
lang: es
---

# Aprendizaje no supervisado

## De la semejanza a segmentos e hipótesis

**Semana 8 · Clase 8**

**Recorrido conceptual:** `representación → semejanza → estructura → interpretación`

---

# Propósito de la clase

Comprender cómo los métodos no supervisados organizan observaciones sin una etiqueta objetivo y cómo evaluar si esa organización es útil.

Al finalizar podremos:

- formular una pregunta no supervisada;
- justificar una distancia y una representación;
- explicar K-means, jerárquico, DBSCAN y SOM;
- usar PCA para resumir y visualizar datos;
- evaluar e interpretar segmentos sin convertirlos en categorías esenciales.

---

# Punto de partida

En aprendizaje supervisado disponíamos de pares con respuesta observada:

$$
(x_i,y_i) \rightarrow \widehat f \rightarrow \widehat y.
$$

Ahora solo observamos perfiles:

$$
x_1,\ldots,x_n \rightarrow \text{representación} \rightarrow \text{estructura candidata}.
$$

**Pregunta clave:** ¿qué significa que dos observaciones sean semejantes para nuestro problema?

---

# Caso conductor: movilidad

Una ciudad quiere resumir perfiles de zonas para planificar observación y servicio.

| Elemento | Ejemplo |
|---|---|
| Unidad | zona de movilidad durante una semana |
| Variables de formación | proporciones de viajes por franja, duración típica, variabilidad, congestión |
| Sin etiqueta | no existe un tipo verdadero de zona |
| Uso posterior | describir perfiles, revisar cobertura, proponer acciones exploratorias |

Un grupo no descubre una categoría natural: resume una estructura bajo decisiones explícitas.

---

# ¿Qué cambia sin etiquetas?

| Supervisado | No supervisado |
|---|---|
| objetivo $y$ observado | no hay respuesta correcta conocida |
| error frente a $y$ | cohesión, separación, estabilidad y utilidad |
| predicción para casos nuevos | representación, segmentos o vecindades |
| validación con etiquetas | evidencia interna, externa y contextual |

Muchas particiones pueden ser matemáticamente válidas. Ninguna métrica única decide cuál sirve mejor.

---

# Cuatro objetivos posibles

- **Descubrimiento de grupos:** observaciones semejantes dentro de cada segmento.
- **Representación:** resumir con prototipos, componentes o mapas.
- **Estructura local:** identificar vecindades, regiones densas y puntos aislados.
- **Generación de hipótesis:** proponer preguntas para contrastar después.

**Control:** elegir un algoritmo sin declarar el objetivo confunde una figura atractiva con un resultado útil.

---

# Formular antes de agrupar

Antes del ajuste debemos responder:

1. ¿Cuál es la unidad de análisis?
2. ¿Qué periodo y población cubren los datos?
3. ¿Qué diferencias importan para el dominio?
4. ¿Se admite ruido sin asignar a un grupo?
5. ¿Cómo se usará y revisará el resultado?

**Idea:** la distancia es una hipótesis de dominio expresada matemáticamente.

---

# Distancia euclídea

Para perfiles numéricos $\mathbf{x}$ y $\mathbf{z}$:

$$
d_2(\mathbf{x},\mathbf{z})=
\sqrt{\sum_{j=1}^{p}(x_j-z_j)^2}.
$$

Para $A=(2,3)$ y $B=(5,7)$:

$$
d_2(A,B)=\sqrt{3^2+4^2}=5.
$$

- Las diferencias grandes pesan más al elevarse al cuadrado.
- Es coherente con K-means y centroides definidos por medias.
- Supone variables cuantitativas y escalas comparables.

---

# Distancia Manhattan

La distancia Manhattan suma diferencias absolutas:

$$
d_1(\mathbf{x},\mathbf{z})=
\sum_{j=1}^{p}|x_j-z_j|.
$$

Para los mismos perfiles:

$$
d_1(A,B)=|2-5|+|3-7|=7.
$$

No elimina la necesidad de escalar variables, pero reduce el peso relativo de diferencias extremas frente a $d_2$.

---

# La métrica puede cambiar el vecino

Para $O=(0,0)$, $P=(3,0)$ y $Q=(2,2)$:

| Métrica | $d(O,P)$ | $d(O,Q)$ | Vecino más cercano |
|---|---:|---:|---|
| Euclídea | $3$ | $\sqrt{8}\approx2{,}83$ | $Q$ |
| Manhattan | $3$ | $4$ | $P$ |

No hay una métrica universalmente correcta: cada una expresa una noción distinta de diferencia.

---

# Similitud coseno: forma y nivel

La similitud coseno compara orientación:

$$
s_{\cos}(\mathbf{x},\mathbf{z})=
\frac{\mathbf{x}^{\mathsf T}\mathbf{z}}
{\|\mathbf{x}\|_2\|\mathbf{z}\|_2}.
$$

Los perfiles $A=(2,4,2)$ y $B=(20,40,20)$ tienen coseno $1$: misma composición relativa, distinta magnitud.

**Decisión:** usar proporciones para la forma y conservar el volumen como una variable adicional si importa operacionalmente.

---

# Escalar también es decidir

Una duración entre 0 y 120 puede dominar a una proporción entre 0 y 1. Dos opciones frecuentes son:

$$
z_{ij}=\frac{x_{ij}-\bar x_j}{s_j},
\qquad
r_{ij}=\frac{x_{ij}-\operatorname{mediana}(X_j)}
{Q_{0.75}(X_j)-Q_{0.25}(X_j)}.
$$

- $z$: centra y asigna varianza unitaria.
- $r$: alternativa robusta basada en mediana y rango intercuartílico.
- Logaritmos pueden comprimir colas derechas.

---

# Ponderar bloques de variables

Una distancia ponderada explicita prioridades:

$$
d_w(\mathbf{x},\mathbf{z})=
\sqrt{\sum_{j=1}^{p}w_j(x_j-z_j)^2},\qquad w_j\geq0.
$$

En movilidad, doce proporciones horarias pueden dominar por cantidad de columnas a dos variables de diversidad, incluso estandarizadas.

**Criterio:** asignar pesos por confiabilidad, relevancia operativa o equilibrio entre bloques; no para producir grupos más vistosos.

---

# Datos mixtos y variables reservadas

- K-means requiere variables numéricas y una media interpretable.
- Las categorías necesitan una codificación y una disimilitud coherentes.
- Las variables de **formación** determinan los grupos.
- Las variables de **caracterización** se reservan para comprenderlos después.

Separar ambos conjuntos evita introducir previamente la conclusión que se busca describir.

---

# K-means: idea y objetivo

K-means divide observaciones numéricas en $K$ grupos $C_1,\ldots,C_K$ minimizando:

$$
J=\sum_{k=1}^{K}\sum_{\mathbf{x}_i\in C_k}
\|\mathbf{x}_i-\boldsymbol{\mu}_k\|_2^2,
\qquad
\boldsymbol{\mu}_k=\frac{1}{|C_k|}\sum_{\mathbf{x}_i\in C_k}\mathbf{x}_i.
$$

El centroide es un perfil promedio; no tiene por qué coincidir con una zona real.

---

# K-means: dos pasos alternados

```text
Inicializar K centroides
Repetir:
    asignar cada observación al centroide más cercano
    recalcular cada centroide como media de su grupo
Hasta que no cambien las asignaciones o la mejora sea pequeña
```

- Cada paso no aumenta $J$.
- Converge a una solución local, no garantiza el óptimo global.
- Un grupo vacío requiere una regla documentada.

---

# Qué estructura busca K-means

K-means funciona mejor cuando los grupos son:

- compactos y aproximadamente esféricos;
- de dispersión y tamaño no demasiado distintos;
- representables mediante una media y distancia euclídea.

Siempre asigna todos los casos. Puede dividir grupos alargados o fusionar regiones con densidades diferentes.

**Límite:** su eficiencia no corrige una geometría inadecuada.

---

# Inicialización, reinicios y estabilidad

- Distintas semillas pueden producir soluciones diferentes.
- K-means++ favorece centros iniciales separados.
- Ejecutar varios reinicios reduce el riesgo de una mala solución local.
- Comparar solo la menor inercia puede ocultar asignaciones muy distintas.

**Control:** además de cambiar semillas, repetir con submuestras, periodos y transformaciones plausibles.

---

# Elegir el número de grupos

La inercia disminuye siempre al aumentar $K$. El método del codo busca un punto de rendimientos decrecientes, pero puede no ser claro.

Un protocolo razonable:

1. definir un rango de $K$ útil para el problema;
2. ejecutar varios reinicios por cada $K$;
3. comparar inercia, silhouette, Davies--Bouldin y tamaños;
4. revisar estabilidad y perfiles;
5. elegir la solución más simple que sea estable y accionable.

---

# Clustering jerárquico

Construye relaciones anidadas entre observaciones.

| Estrategia | Inicio | Operación |
|---|---|---|
| Aglomerativa | una observación por grupo | fusiona los grupos más próximos |
| Divisiva | todas las observaciones juntas | divide grupos sucesivamente |

El resultado suele visualizarse con un **dendrograma**. No exige fijar $K$ antes, pero una fusión temprana aglomerativa no se deshace.

---

# Reglas de enlace

La distancia entre grupos $A$ y $B$ depende del enlace:

$$
D_{\text{simple}}=\min d(i,l),\qquad
D_{\text{completo}}=\max d(i,l),
$$

$$
D_{\text{promedio}}=\frac{1}{|A||B|}\sum_{i\in A}\sum_{l\in B}d(i,l).
$$

- Simple: descubre cadenas, pero puede unir regiones por puntos puente.
- Completo: favorece grupos compactos; es sensible a extremos.
- Promedio: usa toda la información entre pares.
- Ward: minimiza aumento de dispersión y requiere geometría euclídea coherente.

---

# Leer un dendrograma

- Cada hoja es una observación o grupo inicial.
- La altura de unión indica la disimilitud de enlace.
- Un corte horizontal induce una partición.

**Tres errores frecuentes:** leer la posición horizontal como distancia, elegir un corte solo por cantidad deseada y tratar ramas como categorías reales sin perfiles ni estabilidad.

**Idea:** el dendrograma explora granularidades; no cuenta grupos automáticamente.

---

# Densidad y vecindades

Una vecindad de radio $\varepsilon$ alrededor de $\mathbf{x}$ es:

$$
N_{\varepsilon}(\mathbf{x})=
\{\mathbf{z}:d(\mathbf{x},\mathbf{z})\leq\varepsilon\}.
$$

El tamaño $|N_{\varepsilon}(\mathbf{x})|$ aproxima densidad local.

Los métodos por densidad encuentran regiones conectadas y densas, pueden describir formas no convexas y dejar casos sin grupo.

---

# DBSCAN: núcleo, frontera y ruido

DBSCAN usa radio $\varepsilon$ y `minPts`:

| Tipo de punto | Condición |
|---|---|
| Núcleo | su vecindad contiene al menos `minPts` casos |
| Frontera | no es núcleo, pero está cerca de uno |
| Ruido | no cumple ninguna de las condiciones anteriores |

No exige $K$: expande grupos mediante cadenas de puntos núcleo conectados por densidad.

---

# DBSCAN frente a K-means

| K-means | DBSCAN |
|---|---|
| exige $K$ | usa $\varepsilon$ y `minPts` |
| asigna todos los casos | puede dejar ruido |
| favorece grupos convexos | encuentra formas arbitrarias |
| centroide promedio | regiones densas conectadas |

Un punto etiquetado como ruido es geométricamente aislado bajo una configuración. No equivale a error, fraude ni evento irrelevante.

---

# Sensibilidad de DBSCAN

- `minPts` pequeño acepta cadenas frágiles; uno grande convierte más casos en ruido.
- El gráfico de distancia al vecino $k$ puede sugerir un rango para $\varepsilon$, no decidirlo por sí solo.
- El escalado cambia el significado efectivo de $\varepsilon$.

**Control:** explorar una rejilla de parámetros y buscar mesetas donde cantidad, tamaño y composición de grupos cambien poco.

---

# Mapas autoorganizados (SOM)

Un SOM es una rejilla de prototipos. Cada nodo $m$ tiene pesos $\mathbf{w}_m$.

Para una observación $\mathbf{x}$, la unidad de mejor coincidencia es:

$$
c=\arg\min_m\|\mathbf{x}-\mathbf{w}_m\|_2.
$$

Durante el ajuste se acercan a $\mathbf{x}$ la unidad ganadora y sus vecinas de rejilla.

---

# Qué muestra un SOM

- **Mapa de componentes:** valor de una variable en cada prototipo.
- **Matriz U:** distancia entre prototipos vecinos; sugiere fronteras o continuidad.
- **Mapa de conteos:** cantidad de observaciones por nodo.

Un SOM preserva vecindades de forma aproximada; no produce grupos automáticamente. Si se agrupan prototipos, esa etapa se evalúa por separado.

---

# Reducir dimensión: por qué

Con muchas variables, las distancias tienden a parecerse y las vecindades pierden contraste.

La reducción busca una representación:

$$
Z=g(X),\qquad q<p.
$$

Puede comprimir, disminuir ruido o facilitar visualización. También puede ocultar señales raras o distorsionar proximidades.

**Control:** no agrupar solo una proyección 2D sin revisar la estructura en el espacio de formación.

---

# PCA: componentes principales

PCA construye nuevas coordenadas lineales que resumen variación de $X$.

1. centrar las variables;
2. decidir si estandarizar según las unidades;
3. buscar direcciones ortogonales de máxima varianza;
4. proyectar cada observación en esas direcciones.

La primera componente explica la mayor varianza disponible; las siguientes explican varianza restante y son ortogonales a las anteriores.

---

# Varianza explicada e interpretación

Si $\lambda_j$ es la varianza de la componente $j$:

$$
\text{varianza explicada}_j=
\frac{\lambda_j}{\sum_r\lambda_r}.
$$

- Una componente combina variables originales mediante cargas.
- Alta varianza no implica utilidad para todas las decisiones.
- PCA optimiza reconstrucción lineal, no clasificación, causalidad ni calidad de grupos.

**Resultado:** elegir $q$ combina pérdida aceptable, estabilidad e interpretación.

---

# Inercia: compactación de K-means

La inercia es la función objetivo:

$$
W_K=\sum_{k=1}^{K}\sum_{i\in C_k}
\|\mathbf{x}_i-\boldsymbol{\mu}_k\|_2^2.
$$

- Menor valor: menor dispersión dentro de grupos bajo esa representación.
- Solo compara soluciones sobre los mismos datos y preprocesamiento.
- Siempre disminuye al crecer $K$; no basta para elegirlo.

---

# Silhouette: cohesión y separación

Para la observación $i$, $a(i)$ es la distancia media a su grupo y $b(i)$ la menor distancia media a otro grupo:

$$
s(i)=\frac{b(i)-a(i)}{\max\{a(i),b(i)\}}.
$$

| Valor | Lectura |
|---|---|
| cercano a 1 | buena cohesión y separación |
| cercano a 0 | punto de frontera |
| negativo | más cercano, en promedio, a otro grupo |

Revisar la distribución por grupo, no solo su promedio.

---

# Davies--Bouldin: grupos rivales

Compara dispersión interna y distancia entre centroides:

$$
DB=\frac{1}{K}\sum_{k=1}^{K}
\max_{l\neq k}\frac{S_k+S_l}{M_{kl}}.
$$

Valores menores indican grupos compactos respecto de su rival más cercano.

**Límite:** supone grupos descritos por centroides; puede valorar mal formas arbitrarias y resultados de DBSCAN.

---

# Caracterizar sin esencializar

Una ficha de segmento debe indicar:

- tamaño, perfiles centrales y dispersión;
- variables que lo distinguen y casos fronterizos;
- estabilidad ante muestras, periodos y decisiones de representación;
- qué casos no representa;
- para qué pregunta o acción exploratoria podría servir.

Usar nombres descriptivos, como “actividad nocturna alta y variabilidad baja”, en lugar de etiquetas valorativas.

---

# Anomalías y sobreinterpretación

Una observación atípica puede ser global, contextual o colectiva. Primero se revisan integridad, cobertura, unidades y periodo.

No debemos concluir que:

- un cluster es una clase natural;
- una separación visual prueba causalidad;
- ruido de DBSCAN es error;
- una métrica alta vuelve estable o útil la segmentación.

**Control:** triangular métricas internas, estabilidad, evidencia externa y utilidad contextual.

---

# Del segmento a la decisión

En movilidad, los segmentos pueden guiar preguntas como:

| Hallazgo descriptivo | Pregunta posterior |
|---|---|
| patrón nocturno concentrado | ¿la cobertura de observación es suficiente? |
| zona frontera entre segmentos | ¿cambia por periodo o por medición? |
| perfil aislado | ¿es un evento raro, una falla o una zona subobservada? |

El grupo informa una investigación o una regla revisable; no reemplaza el juicio ni demuestra por qué ocurre el patrón.

---

# Síntesis

- El aprendizaje no supervisado organiza perfiles sin una respuesta conocida.
- La representación, distancia y escalado definen qué estructura puede aparecer.
- K-means, jerárquico, DBSCAN y SOM responden a geometrías diferentes.
- PCA resume variación, pero no certifica utilidad ni conserva toda la estructura.
- La evaluación combina compactación, separación, estabilidad, evidencia externa y propósito.
- Un segmento es una descripción condicionada por método y datos, no una identidad fija.

---

# Lecturas

**Lectura principal**

- Capítulo 13, §§13.1–13.4: distancias, clustering, DBSCAN, SOM y evaluación.

**Para ampliar**

- Capítulo 10, §10.3: reducción de dimensionalidad, PCA y visualización.

**Actividad sugerida**

- Capítulo 13, actividad EMO [MOV-03]: segmentar zonas por patrón de movilidad.
