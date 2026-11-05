---
title: "Ingeniería de atributos y clustering"
subtitle: "De la representación de datos a segmentos interpretables"
author: "Curso de Data Science"
course: "Data Science"
week: 6
class: 6
lang: es
---

# Ingeniería de atributos y clustering

## De la representación de datos a segmentos interpretables

**Semana 6 · Clase 6**

**Recorrido conceptual:** `datos brutos → atributos → semejanza → grupos → interpretación`

---

# Propósito de la clase

Construir representaciones útiles para analizar datos y formar grupos sin una etiqueta objetivo conocida.

Al finalizar podremos:

- transformar atributos numéricos, categóricos, temporales y espaciales;
- distinguir selección de atributos y reducción dimensional;
- explicar K-means, jerárquico y DBSCAN;
- elegir y calcular métricas de agrupamiento;
- describir grupos sin atribuirles significado que los datos no sostienen.

---

# Punto de partida

La Semana 05 estableció cómo formular una tarea y evaluar procedimientos de aprendizaje.

Ahora el foco es anterior al modelo:

$$
\text{datos brutos} \rightarrow \text{representación} \rightarrow \text{estructura analizable}.
$$

Las decisiones de representación determinan qué diferencias, semejanzas y patrones pueden aparecer.

---

# Caso conductor: Palmer Penguins

Trabajaremos con 344 registros de pingüinos de las islas Palmer.

| Elemento | Decisión |
|---|---|
| Unidad | un pingüino registrado |
| Formación | cuatro medidas morfológicas |
| Variables reservadas | `species`, `island`, `sex` |
| Pregunta | ¿qué perfiles morfológicos aparecen sin usar especie? |
| Uso posterior | describir patrones y contrastarlos con información externa |

---

# Atributos: representación con propósito

Un atributo es una magnitud usada para representar una observación.

| Dato disponible | Representación posible | Supuesto |
|---|---|---|
| masa corporal | valor, logaritmo o nivel | importa escala absoluta o relativa |
| isla | categoría indicadora | no existe orden entre islas |
| fecha | año, estación o ciclo | hay estructura temporal relevante |
| ubicación | zona, distancia o conectividad | la cercanía está bien definida |

Una representación útil conserva significado y responde a la pregunta de análisis.

---

# Outliers: error, evento o población distinta

Un valor extremo puede ser:

- error de captura o unidad;
- medición válida pero inusual;
- señal de una población diferente;
- resultado de una transformación o unión incorrecta.

**Criterio:** antes de recortar, revisar fuente, unidad, cobertura y contexto. Eliminar extremos sin investigar puede borrar justamente el patrón relevante.

---

# Transformaciones numéricas

| Operación | Uso | Riesgo |
|---|---|---|
| estandarizar | poner escalas en relación | tratar desviaciones como comparables sin justificación |
| logaritmo | comprimir colas derechas | aplicarlo a ceros o negativos |
| razón | normalizar por exposición | denominador pequeño o nulo |
| recorte | limitar influencia extrema | ocultar eventos reales |

**Ejemplo:** la masa se mide en gramos y la longitud de aleta en milímetros; una distancia directa estaría dominada por la masa.

---

# Categorías, discretización y binarización

- Las categorías nominales no poseen orden ni distancia intrínsecos.
- La codificación indicadora representa cada nivel con una columna binaria.
- Discretizar convierte una escala continua en intervalos; pierde detalle, pero puede facilitar una regla explícita.
- Binarizar expresa una condición, por ejemplo `masa > 4500 g`.

**Control:** una codificación debe preservar el significado de las diferencias y declarar cómo trata niveles nuevos.

---

# Tiempo, espacio e interacciones

Para fenómenos cíclicos, una posición $t$ en un periodo $P$ puede representarse como:

$$
x_{\sin}=\sin(2\pi t/P),\qquad x_{\cos}=\cos(2\pi t/P).
$$

Las interacciones expresan que el efecto de una variable depende de otra. Las distancias espaciales deben representar el mecanismo relevante: kilómetros, conectividad o tiempo de viaje no son equivalentes.

---

# Selección y reducción no son lo mismo

| Operación | Resultado |
|---|---|
| Selección de atributos | conserva un subconjunto de columnas originales |
| Reducción dimensional | construye nuevas coordenadas combinando columnas |

La selección puede conservar una medida corporal directa. PCA puede reemplazar varias medidas correlacionadas por componentes menos interpretables.

---

# Familias de selección de atributos

| Familia | Estrategia | Límite |
|---|---|---|
| Filtro | puntuar antes del modelo | puede ignorar interacciones |
| Envolvente | comparar subconjuntos | costo y sobreajuste de búsqueda |
| Embebida | seleccionar durante el ajuste | depende de modelo y escala |

Relevancia no equivale a causalidad. Atributos correlacionados pueden sustituirse entre muestras.

---

# Reducir dimensión: por qué

La reducción construye una representación:

$$
Z=g(X),\qquad q<p.
$$

Puede comprimir, disminuir ruido o facilitar visualización. En muchas dimensiones, las distancias entre vecinos tienden a perder contraste y las variables irrelevantes degradan la semejanza.

---

# PCA: componentes principales

PCA busca direcciones ortogonales de máxima varianza.

1. centrar las variables;
2. decidir si las unidades justifican estandarizar;
3. proyectar observaciones en componentes ordenadas por varianza.

Las cargas indican la contribución de cada variable; las puntuaciones ubican observaciones en la nueva representación.

---

# Varianza explicada y límites de PCA

Si $\lambda_j$ es la varianza de la componente $j$:

$$
\operatorname{PVE}_j=\frac{\lambda_j}{\sum_r\lambda_r}.
$$

- Alta varianza explicada no garantiza relevancia para una tarea.
- Una señal rara puede quedar en componentes de baja varianza.
- Un plano PCA sirve para explorar; no prueba que existan grupos separados.

---

# Aprendizaje no supervisado

No hay una variable objetivo que indique la respuesta correcta. El análisis busca:

- resumir perfiles semejantes;
- explorar estructura local o regiones densas;
- detectar observaciones que requieren revisión;
- generar hipótesis para contrastar después.

**Pregunta central:** ¿qué significa semejanza para las variables y el uso previsto?

---

# Distancia euclídea

Para perfiles numéricos $\mathbf{x}$ y $\mathbf{z}$:

$$
d_2(\mathbf{x},\mathbf{z})=
\sqrt{\sum_{j=1}^{p}(x_j-z_j)^2}.
$$

Es coherente con K-means y con centroides definidos por la media. Las diferencias grandes pesan más y las escalas deben ser comparables.

---

# Manhattan y coseno

$$
d_1(\mathbf{x},\mathbf{z})=\sum_{j=1}^{p}|x_j-z_j|.
$$

$$
s_{\cos}(\mathbf{x},\mathbf{z})=
\frac{\mathbf{x}^{\mathsf T}\mathbf{z}}
{\|\mathbf{x}\|_2\|\mathbf{z}\|_2}.
$$

Manhattan reduce el peso relativo de extremos. El coseno compara forma relativa y puede ignorar magnitud. La métrica es una decisión de modelado, no un detalle técnico neutro.

---

# Escalado y ponderación

La estandarización frecuente es:

$$
z_{ij}=\frac{x_{ij}-\bar{x}_j}{s_j}.
$$

Una distancia ponderada expresa prioridades entre atributos o bloques:

$$
d_w(\mathbf{x},\mathbf{z})=
\sqrt{\sum_{j=1}^{p}w_j(x_j-z_j)^2}.
$$

Ponderar debe responder a confiabilidad o significado, no a producir grupos visualmente atractivos.

---

# K-means: objetivo

K-means divide observaciones numéricas en $K$ grupos minimizando:

$$
J=\sum_{k=1}^{K}\sum_{\mathbf{x}_i\in C_k}
\|\mathbf{x}_i-\boldsymbol{\mu}_k\|_2^2.
$$

El centroide $\boldsymbol{\mu}_k$ es la media del grupo. Es un perfil promedio, no necesariamente una observación real.

---

# K-means: procedimiento

1. Inicializar $K$ centroides.
2. Asignar cada observación al centroide más cercano.
3. Recalcular cada centroide como media del grupo.
4. Repetir hasta que las asignaciones o el objetivo cambien muy poco.

La solución puede depender de la inicialización. K-means++ y varios reinicios reducen el riesgo de resultados locales deficientes.

---

# Cuándo sirve K-means

| Adecuado | Problemático |
|---|---|
| grupos compactos | grupos alargados o curvos |
| dispersión semejante | densidades muy diferentes |
| variables numéricas escaladas | categorías sin representación justificada |
| todos los casos deben agruparse | algunos casos deberían permanecer aislados |

K-means siempre asigna cada observación a un grupo.

---

# Elegir K

La inercia disminuye siempre al crecer $K$:

$$
W_K=\sum_{k=1}^{K}\sum_{i\in C_k}
\|\mathbf{x}_i-\boldsymbol{\mu}_k\|_2^2.
$$

El codo busca rendimientos decrecientes, pero no determina una respuesta única. Se combinan inercia, métricas, tamaños, estabilidad, simplicidad y utilidad de los perfiles.

---

# Clustering jerárquico

| Estrategia | Inicio | Operación |
|---|---|---|
| Aglomerativa | una observación por grupo | fusiona grupos cercanos |
| Divisiva | un único conjunto | divide grupos sucesivamente |

El dendrograma muestra fusiones a distintas alturas y permite examinar varias granularidades. Una fusión aglomerativa temprana no se deshace.

---

# Enlaces y dendrogramas

- **Simple:** une grupos por el par más cercano; puede encadenar regiones mediante puntos puente.
- **Completo:** usa el par más lejano; favorece compactación, es sensible a extremos.
- **Promedio:** resume todas las distancias entre pares.
- **Ward:** minimiza aumento de dispersión y requiere geometría euclídea coherente.

El orden horizontal de las hojas no representa una distancia adicional. El corte se justifica con perfiles, estabilidad y propósito.

---

# Alternativas de enlace: una lectura visual

Consideremos dos grupos candidatos, $A$ y $B$.

| Enlace | Qué compara entre $A$ y $B$ |
|---|---|
| Simple | el par de puntos más cercano |
| Completo | el par de puntos más lejano |
| Promedio | todas las distancias entre pares |
| Ward | el aumento de dispersión al fusionar centroides |

Cada regla puede producir un dendrograma y un corte distintos sobre los mismos datos.

---

# DBSCAN: densidad y ruido

DBSCAN usa radio $\varepsilon$ y `min_samples`.

| Tipo | Condición |
|---|---|
| núcleo | tiene suficientes vecinos en radio $\varepsilon$ |
| frontera | está cerca de un núcleo, pero no es núcleo |
| ruido | no pertenece a una región densa bajo esa configuración |

Puede encontrar formas arbitrarias y no requiere fijar $K$.

---

# Sensibilidad de DBSCAN

- Un radio grande fusiona regiones; uno pequeño las fragmenta.
- Un `min_samples` grande exige mayor evidencia local.
- El escalado cambia el significado efectivo de $\varepsilon$.
- La etiqueta de ruido no significa error ni irrelevancia.

Se explora una grilla de parámetros y se buscan configuraciones estables, no una cifra aislada favorable.

---

# Métricas internas

| Métrica | Qué resume | Dirección |
|---|---|---|
| Inercia | dispersión de K-means | menor |
| Silhouette | cohesión y separación | mayor |
| Calinski--Harabasz | separación relativa a dispersión | mayor |
| Davies--Bouldin | dispersión respecto de grupos rivales | menor |

Ninguna métrica identifica por sí sola una segmentación útil. Todas dependen de la representación y la geometría usada.

---

# Silhouette

Para una observación $i$, $a(i)$ es la distancia media a su grupo y $b(i)$ la menor distancia media a otro grupo:

$$
s(i)=\frac{b(i)-a(i)}{\max\{a(i),b(i)\}}.
$$

- Cercano a 1: cohesión y separación altas.
- Cercano a 0: caso fronterizo.
- Negativo: está más cerca, en promedio, de otro grupo.

Conviene revisar la distribución por grupo y no solo un promedio global.

---

# Calinski--Harabasz y Davies--Bouldin

Calinski--Harabasz compara dispersión entre grupos con dispersión interna. Valores mayores suelen indicar separación relativa mayor.

Davies--Bouldin compara cada grupo con su rival más parecido:

$$
DB=\frac{1}{K}\sum_{k=1}^{K}\max_{l\neq k}\frac{S_k+S_l}{M_{kl}}.
$$

Valores menores son preferibles. Ambas métricas favorecen ciertas geometrías y deben interpretarse junto con perfiles y estabilidad.

---

# Estabilidad y casos frontera

Una solución útil no debería cambiar por completo al modificar una semilla, una submuestra o una decisión defendible de transformación.

| Diagnóstico | Pregunta |
|---|---|
| reinicios | ¿la optimización llega a particiones parecidas? |
| submuestras | ¿los perfiles sobreviven a cambios de muestra? |
| casos con silhouette baja | ¿son fronteras, errores o transiciones? |
| tamaños de grupos | ¿hay segmentos diminutos o dominantes? |

---

# Describir grupos con prudencia

Una ficha de grupo debe incluir:

- cantidad de observaciones;
- medianas, dispersión y perfiles en unidades originales;
- casos representativos y fronterizos;
- sensibilidad a decisiones de análisis;
- población y periodo que cubre.

Usar nombres descriptivos, no etiquetas valorativas. Un grupo encontrado no demuestra una clase natural ni una causa.

---

# Comparación externa posterior

Después de formar grupos con las cuatro medidas morfológicas, podemos cruzar `cluster` con `species`:

| Uso legítimo | Uso incorrecto |
|---|---|
| describir coincidencias y desacuerdos | declarar que el algoritmo predijo especie |
| evaluar una referencia externa | usar especie para elegir retrospectivamente el mejor resultado |

La especie no participó en el agrupamiento. Una coincidencia parcial puede revelar subestructura o una representación insuficiente.

---

# Notebook: qué exploraremos

El ejemplo de Palmer Penguins implementará:

1. imputación y estandarización de medidas morfológicas;
2. K-means, jerárquico y DBSCAN;
3. inercia, silhouette, Calinski--Harabasz, Davies--Bouldin y estabilidad;
4. PCA 2D solo para visualizar;
5. perfiles en unidades originales y tabla cruzada final con especie.

---

# Síntesis

- Atributos, escalas y agregaciones definen el espacio donde se buscan patrones.
- Selección conserva columnas; PCA crea representaciones nuevas.
- K-means, jerárquico y DBSCAN responden a geometrías distintas.
- Las métricas comparan estructura geométrica, no significado biológico automático.
- La estabilidad, los perfiles y la información externa completan la evaluación.
- Clustering genera hipótesis y descripciones revisables; no sustituye una explicación causal.

---

# Lecturas

**Ingeniería y reducción de atributos**

- Capítulo 10, §§10.1--10.4.

**Clustering y evaluación**

- Capítulo 13, §§13.1--13.4.

**Práctica**

- Guía de ejercicios de Diseño experimental de Machine Learning, ejercicio 10: Palmer Penguins.
