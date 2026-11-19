# Parcial 2: Ciencia de Datos 2026 — Grupos

## Grupo A

**1.** La codificación indicadora de una variable categórica:

a) Asigna enteros consecutivos a los niveles según su orden alfabético.  
b) Reemplaza cada categoría por la cantidad de veces que aparece.  
c) Crea una columna binaria por cada nivel.  

**2.** Según la clase, el logaritmo se usa para:

a) Comprimir colas.  
b) Normalizar por exposición.  
c) Codificar categorías nominales.  

**3.** Para representar una posición temporal cíclica, como la hora del día, se usan:

a) El seno y el coseno de 2πt/P.  
b) El número entero de la hora como valor lineal.  
c) El logaritmo de la hora.  

**4.** La selección de atributos:

a) Conserva un subconjunto de las columnas originales.  
b) Construye nuevas coordenadas combinando columnas.  
c) Crea una columna binaria por cada nivel de una categoría.  

**5.** Los métodos de selección de tipo filtro:

a) Comparan subconjuntos de atributos entrenando el modelo.  
b) Puntúan los atributos antes de ajustar el modelo.  
c) Seleccionan atributos durante el ajuste del modelo.  

**6.** PCA busca:

a) Grupos compactos de observaciones.  
b) Las variables más asociadas con una etiqueta.  
c) Direcciones ortogonales de máxima varianza.  

**7.** Una alta proporción de varianza explicada por los primeros componentes:

a) Garantiza que esos componentes son los más relevantes para cualquier tarea.  
b) Prueba que en los datos existen grupos claramente separados.  
c) Indica cuánta dispersión resumen, lo cual difiere de su relevancia para una tarea.  

**8.** En el aprendizaje no supervisado:

a) Se trabaja con datos carentes de una etiqueta que indique la respuesta correcta.  
b) Se ajusta un modelo para predecir una etiqueta conocida en casos nuevos.  
c) Se combinan pocos casos etiquetados con muchos casos carentes de etiqueta.  

**9.** La distancia euclídea:

a) Suma las diferencias absolutas.  
b) Eleva al cuadrado las diferencias, por lo que las diferencias grandes pesan más.  
c) Compara la orientación de los vectores.  

**10.** Si la masa se mide en gramos y la longitud de aleta en milímetros, antes de calcular distancias:

a) Debe decidirse cómo escalar las variables.  
b) Conviene excluir del análisis la variable de mayor magnitud.  
c) Conviene redondear ambas variables a valores enteros.  

**11.** K-means busca minimizar:

a) El número de grupos.  
b) La suma de distancias cuadráticas de cada observación a su centroide.  
c) La distancia entre centroides.  

**12.** K-means es adecuado cuando:

a) Los grupos son curvos o alargados, con fronteras irregulares.  
b) Los grupos son compactos, de dispersión semejante y con variables numéricas escaladas.  
c) Los grupos tienen densidades muy diferentes entre sí.  

**13.** Al aumentar K, la inercia:

a) Aumenta siempre.  
b) Se mantiene constante.  
c) Disminuye siempre.  

**14.** El clustering jerárquico aglomerativo:

a) Comienza con un único conjunto y lo divide sucesivamente.  
b) Comienza con una observación por grupo y fusiona grupos cercanos.  
c) Fija K centroides y reasigna observaciones.  

**15.** El enlace simple:

a) Usa el par más cercano y puede encadenar regiones mediante puntos puente.  
b) Usa el par más lejano y favorece grupos compactos.  
c) Minimiza el aumento de dispersión dentro de los grupos.  

**16.** En DBSCAN, un punto núcleo:

a) Está cerca de un núcleo, pero no es núcleo.  
b) Está fuera de las regiones densas.  
c) Tiene suficientes vecinos dentro del radio ε.  

**17.** En DBSCAN, un radio ε grande tiende a:

a) Fusionar regiones.  
b) Fragmentar regiones.  
c) Aumentar la cantidad de ruido.  

**18.** Una silhouette cercana a 1 indica:

a) Un caso fronterizo.  
b) Cohesión y separación altas.  
c) Una observación más cercana a otro grupo.  

**19.** El índice de Calinski–Harabasz:

a) Compara cada grupo con su rival; valores menores son preferibles.  
b) Cuenta coincidencias con una clasificación externa.  
c) Compara la dispersión entre grupos con la interna; valores mayores indican mayor separación relativa.  

**20.** Después de agrupar pingüinos con las cuatro medidas, cruzar los grupos con species es legítimo para:

a) Afirmar que el algoritmo predijo la especie.  
b) Describir coincidencias y desacuerdos con una referencia externa.  
c) Elegir retrospectivamente la mejor configuración.  

### Clave Grupo A

| N.º | Respuesta | N.º banco | Bloque | Sección de origen |
|---|---|---|---|---|
| 1 | c | 1 | Atributos | Clase 6 – Categorías, discretización y binarización (Cap. 10 §10.1.4) |
| 2 | a | 6 | Atributos | Clase 6 – Transformaciones numéricas |
| 3 | a | 5 | Atributos | Clase 6 – Tiempo, espacio e interacciones (Cap. 10 §10.1.5) |
| 4 | a | 11 | Selección, reducción y PCA | Clase 6 – Selección y reducción son distintas |
| 5 | b | 13 | Selección, reducción y PCA | Clase 6 – Familias de selección de atributos (Cap. 10 §10.2.2) |
| 6 | c | 19 | Selección, reducción y PCA | Clase 6 – PCA: componentes principales (Cap. 10 §10.3.3) |
| 7 | c | 23 | Selección, reducción y PCA | Clase 6 – Varianza explicada y límites de PCA (Cap. 10 §10.3.4) |
| 8 | a | 26 | Semejanza y distancias | Clase 6 – Aprendizaje no supervisado (Cap. 13 §13.1.1) |
| 9 | b | 28 | Semejanza y distancias | Clase 6 – Distancia euclídea (Cap. 13 §13.1.2) |
| 10 | a | 32 | Semejanza y distancias | Clase 6 – Transformaciones numéricas / Escalado |
| 11 | b | 35 | K-means | Clase 6 – K-means: objetivo (Cap. 13 §13.2.1) |
| 12 | b | 39 | K-means | Clase 6 – Cuándo sirve K-means |
| 13 | c | 42 | K-means | Clase 6 – Elegir K (Cap. 13 §13.4.1) |
| 14 | b | 45 | Clustering jerárquico | Clase 6 – Clustering jerárquico (Cap. 13 §13.2.5) |
| 15 | a | 48 | Clustering jerárquico | Clase 6 – Enlaces y dendrogramas (Cap. 13 §13.2.6) |
| 16 | c | 54 | DBSCAN | Clase 6 – DBSCAN: densidad y ruido (Cap. 13 §13.3.2) |
| 17 | a | 58 | DBSCAN | Clase 6 – Sensibilidad de DBSCAN (Cap. 13 §13.3.4) |
| 18 | b | 61 | Evaluación e interpretación | Clase 6 – Silhouette (Cap. 13 §13.4.2) |
| 19 | c | 64 | Evaluación e interpretación | Clase 6 – Calinski–Harabasz y Davies–Bouldin |
| 20 | b | 71 | Evaluación e interpretación | Clase 6 – Comparación externa posterior |

## Grupo B

**1.** Las categorías nominales, como la isla de origen de un pingüino:

a) Poseen un orden natural entre sus niveles.  
b) Carecen de orden y de distancia intrínsecos.  
c) Admiten promediar sus códigos numéricos.  

**2.** Al construir una razón para normalizar por exposición, el riesgo señalado es:

a) Ocultar eventos reales al recortar extremos.  
b) Un denominador pequeño o nulo.  
c) Comprimir en exceso las colas de la distribución.  

**3.** Al representar la cercanía espacial, kilómetros, conectividad y tiempo de viaje:

a) Son equivalentes y pueden intercambiarse.  
b) Son nociones distintas, y la elegida debe representar el mecanismo relevante.  
c) Se combinan siempre en una única distancia promedio.  

**4.** La reducción dimensional, como PCA:

a) Construye nuevas coordenadas combinando columnas originales.  
b) Conserva un subconjunto de las columnas originales.  
c) Elimina las observaciones atípicas.  

**5.** Los métodos de selección envolventes (wrappers):

a) Puntúan los atributos antes de ajustar el modelo.  
b) Seleccionan atributos durante el ajuste del modelo.  
c) Comparan subconjuntos de atributos entrenando el modelo.  

**6.** El primer paso de PCA es:

a) Asignar cada observación a un centroide.  
b) Discretizar las variables continuas.  
c) Centrar las variables.  

**7.** Un gráfico de las dos primeras componentes de PCA:

a) Sirve para explorar visualmente los datos.  
b) Prueba que los grupos observados están separados.  
c) Reemplaza la evaluación de estabilidad de los grupos.  

**8.** Uno de los objetivos del análisis no supervisado es:

a) Resumir perfiles y generar hipótesis.  
b) Estimar la accuracy de un clasificador.  
c) Confirmar relaciones causales.  

**9.** La distancia Manhattan:

a) Eleva al cuadrado las diferencias.  
b) Suma las diferencias absolutas y reduce el peso relativo de los extremos.  
c) Compara la orientación de los vectores.  

**10.** Al ponderar variables en una distancia, los pesos deben responder a:

a) La obtención de grupos visualmente atractivos.  
b) La confiabilidad o el significado de las variables.  
c) El orden de las columnas en la tabla.  

**11.** El centroide de un grupo en K-means:

a) Es la media del grupo: un perfil promedio que puede diferir de toda observación real.  
b) Es siempre una de las observaciones reales que pertenecen al grupo.  
c) Es la observación del grupo más alejada de los demás grupos.  

**12.** Una situación problemática para K-means es la presencia de:

a) Grupos compactos, de dispersión y tamaño semejantes.  
b) Variables numéricas escaladas a una misma escala.  
c) Grupos curvos o de densidades diferentes.  

**13.** El método del codo:

a) Determina de forma inequívoca un único valor óptimo de K.  
b) Elige el valor de K que maximiza la silhouette promedio.  
c) Busca rendimientos decrecientes de la inercia y se combina con otros criterios para elegir K.  

**14.** El clustering jerárquico divisivo:

a) Comienza con un único conjunto y lo divide sucesivamente.  
b) Comienza con una observación por grupo y fusiona grupos cercanos.  
c) Fija K centroides y reasigna observaciones.  

**15.** El enlace completo:

a) Usa el par más cercano y puede encadenar regiones.  
b) Promedia todas las distancias entre pares.  
c) Usa el par más lejano, favorece la compactación y es sensible a extremos.  

**16.** Que DBSCAN marque un punto como ruido significa que:

a) Quedó fuera de las regiones densas bajo esa configuración de parámetros.  
b) Es un error de medición que conviene eliminar.  
c) Es irrelevante para el análisis y puede descartarse.  

**17.** En DBSCAN, cambiar el escalado de las variables:

a) Cambia el significado de ε.  
b) Deja intactas las vecindades.  
c) Modifica únicamente min_samples.  

**18.** Una silhouette negativa indica que la observación:

a) Tiene cohesión y separación altas.  
b) Está, en promedio, más cerca de otro grupo.  
c) Es el centroide de su grupo.  

**19.** El índice de Davies–Bouldin:

a) Compara la dispersión entre grupos con la interna; valores mayores son preferibles.  
b) Compara cada grupo con su grupo rival; valores menores son preferibles.  
c) Cuenta coincidencias con una clasificación externa.  

**20.** ¿Cuál es un uso incorrecto de la variable species en el caso Palmer Penguins?

a) Describir coincidencias y desacuerdos con los grupos.  
b) Evaluar los grupos frente a una referencia externa.  
c) Usarla para elegir retrospectivamente la mejor configuración.  

### Clave Grupo B

| N.º | Respuesta | N.º banco | Bloque | Sección de origen |
|---|---|---|---|---|
| 1 | b | 2 | Atributos | Clase 6 – Categorías, discretización y binarización (Cap. 10 §10.1.4) |
| 2 | b | 7 | Atributos | Clase 6 – Transformaciones numéricas |
| 3 | b | 10 | Atributos | Clase 6 – Tiempo, espacio e interacciones (Cap. 10 §10.1.6) |
| 4 | a | 12 | Selección, reducción y PCA | Clase 6 – Selección y reducción son distintas |
| 5 | c | 14 | Selección, reducción y PCA | Clase 6 – Familias de selección de atributos (Cap. 10 §10.2.3) |
| 6 | c | 20 | Selección, reducción y PCA | Clase 6 – PCA: componentes principales (Cap. 10 §10.3.3) |
| 7 | a | 24 | Selección, reducción y PCA | Clase 6 – Varianza explicada y límites de PCA |
| 8 | a | 27 | Semejanza y distancias | Clase 6 – Aprendizaje no supervisado (Cap. 13 §13.1.1) |
| 9 | b | 29 | Semejanza y distancias | Clase 6 – Manhattan y coseno (Cap. 13 §13.1.3) |
| 10 | b | 34 | Semejanza y distancias | Clase 6 – Escalado y ponderación (Cap. 13 §13.1.5) |
| 11 | a | 36 | K-means | Clase 6 – K-means: objetivo (Cap. 13 §13.2.1) |
| 12 | c | 40 | K-means | Clase 6 – Cuándo sirve K-means |
| 13 | c | 43 | K-means | Clase 6 – Elegir K (Cap. 13 §13.2.3) |
| 14 | a | 46 | Clustering jerárquico | Clase 6 – Clustering jerárquico (Cap. 13 §13.2.5) |
| 15 | c | 49 | Clustering jerárquico | Clase 6 – Enlaces y dendrogramas (Cap. 13 §13.2.6) |
| 16 | a | 56 | DBSCAN | Clase 6 – Sensibilidad de DBSCAN (Cap. 13 §13.3.3) |
| 17 | a | 59 | DBSCAN | Clase 6 – Sensibilidad de DBSCAN (Cap. 13 §13.3.4) |
| 18 | b | 62 | Evaluación e interpretación | Clase 6 – Silhouette (Cap. 13 §13.4.2) |
| 19 | b | 65 | Evaluación e interpretación | Clase 6 – Calinski–Harabasz y Davies–Bouldin (Cap. 13 §13.4.3) |
| 20 | c | 72 | Evaluación e interpretación | Clase 6 – Comparación externa posterior |

