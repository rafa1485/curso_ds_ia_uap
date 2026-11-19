# Parcial 2: Ciencia de Datos 2026 — Banco de preguntas

Total: 71 preguntas. Fuente: Clase 6 (Ingeniería de atributos y clustering) y Libro, Cap. 10 §10.1–10.4 y Cap. 13 §13.1–13.4 como respaldo.

**1.** La codificación indicadora de una variable categórica:

a) Asigna enteros consecutivos a los niveles según su orden alfabético.  
b) Reemplaza cada categoría por la cantidad de veces que aparece.  
c) Crea una columna binaria por cada nivel.  

**2.** Las categorías nominales, como la isla de origen de un pingüino:

a) Poseen un orden natural entre sus niveles.  
b) Carecen de orden y de distancia intrínsecos.  
c) Admiten promediar sus códigos numéricos.  

**3.** Representar la condición «masa > 4500 g» como un atributo es un ejemplo de:

a) Binarización.  
b) Codificación indicadora.  
c) Estandarización.  

**4.** Discretizar un atributo consiste en:

a) Crear una columna binaria por cada nivel de una categoría.  
b) Convertir una escala continua en intervalos.  
c) Restar la media y dividir por la desviación estándar.  

**5.** Para representar una posición temporal cíclica, como la hora del día, se usan:

a) El seno y el coseno de 2πt/P.  
b) El número entero de la hora como valor lineal.  
c) El logaritmo de la hora.  

**6.** Según la clase, el logaritmo se usa para:

a) Comprimir colas.  
b) Normalizar por exposición.  
c) Codificar categorías nominales.  

**7.** Al construir una razón para normalizar por exposición, el riesgo señalado es:

a) Ocultar eventos reales al recortar extremos.  
b) Un denominador pequeño o nulo.  
c) Comprimir en exceso las colas de la distribución.  

**8.** Antes de recortar o eliminar un valor extremo, se recomienda:

a) Reemplazarlo por la media de la variable.  
b) Revisar fuente, unidad, cobertura y contexto.  
c) Eliminarlo para estabilizar el análisis.  

**9.** Una interacción entre atributos expresa que:

a) El efecto de una variable depende de otra.  
b) Dos variables están perfectamente correlacionadas.  
c) Una variable se registra en dos unidades distintas.  

**11.** La selección de atributos:

a) Conserva un subconjunto de las columnas originales.  
b) Construye nuevas coordenadas combinando columnas.  
c) Crea una columna binaria por cada nivel de una categoría.  

**12.** La reducción dimensional, como PCA:

a) Conserva un subconjunto de las columnas originales.  
b) Construye nuevas coordenadas combinando columnas originales.  
c) Elimina las observaciones atípicas.  

**13.** Los métodos de selección de tipo filtro:

a) Comparan subconjuntos de atributos entrenando el modelo.  
b) Seleccionan atributos durante el ajuste del modelo.  
c) Puntúan los atributos antes de ajustar el modelo.  

**14.** Los métodos de selección envolventes (wrappers):

a) Puntúan los atributos antes de ajustar el modelo.  
b) Comparan subconjuntos de atributos entrenando el modelo.  
c) Seleccionan atributos durante el ajuste del modelo.  

**15.** Los métodos de selección embebidos:

a) Puntúan los atributos antes de ajustar el modelo.  
b) Seleccionan atributos durante el ajuste del modelo.  
c) Comparan subconjuntos de atributos entrenando el modelo.  

**16.** Una limitación de los métodos de filtro es que:

a) Pueden ignorar interacciones entre atributos.  
b) Tienen un alto costo de búsqueda entre subconjuntos.  
c) Dependen del modelo y de su escala.  

**17.** Que un atributo resulte relevante en un procedimiento de selección:

a) Es distinto de demostrar que causa la respuesta.  
b) Demuestra que causa la respuesta.  
c) Garantiza que será elegido en cualquier muestra.  

**18.** En alta dimensión, las distancias entre vecinos:

a) Ganan contraste.  
b) Se vuelven todas iguales a cero.  
c) Pierden contraste.  

**19.** PCA busca:

a) Grupos compactos de observaciones.  
b) Direcciones ortogonales de máxima varianza.  
c) Las variables más asociadas con una etiqueta.  

**20.** El primer paso de PCA es:

a) Centrar las variables.  
b) Asignar cada observación a un centroide.  
c) Discretizar las variables continuas.  

**21.** En PCA, las cargas:

a) Ubican cada observación en la nueva representación.  
b) Indican la contribución de cada variable a un componente.  
c) Miden la varianza total de los datos.  

**22.** En PCA, las puntuaciones:

a) Indican la contribución de cada variable a un componente.  
b) Miden la varianza total de los datos.  
c) Ubican cada observación en la nueva representación.  

**23.** Una alta proporción de varianza explicada por los primeros componentes:

a) Garantiza que esos componentes son los más relevantes para cualquier tarea.  
b) Prueba que en los datos existen grupos claramente separados.  
c) Indica cuánta dispersión resumen, lo cual difiere de su relevancia para una tarea.  

**24.** Un gráfico de las dos primeras componentes de PCA:

a) Prueba que los grupos observados están separados.  
b) Sirve para explorar visualmente los datos.  
c) Reemplaza la evaluación de estabilidad de los grupos.  

**25.** Una señal rara pero importante puede:

a) Quedar siempre en el primer componente.  
b) Desaparecer al centrar las variables.  
c) Quedar en componentes de baja varianza.  

**26.** En el aprendizaje no supervisado:

a) Se ajusta un modelo para predecir una etiqueta conocida en casos nuevos.  
b) Se combinan pocos casos etiquetados con muchos casos carentes de etiqueta.  
c) Se trabaja con datos carentes de una etiqueta que indique la respuesta correcta.  

**27.** Uno de los objetivos del análisis no supervisado es:

a) Resumir perfiles y generar hipótesis.  
b) Estimar la accuracy de un clasificador.  
c) Confirmar relaciones causales.  

**28.** La distancia euclídea:

a) Suma las diferencias absolutas.  
b) Eleva al cuadrado las diferencias, por lo que las diferencias grandes pesan más.  
c) Compara la orientación de los vectores.  

**29.** La distancia Manhattan:

a) Eleva al cuadrado las diferencias.  
b) Suma las diferencias absolutas y reduce el peso relativo de los extremos.  
c) Compara la orientación de los vectores.  

**30.** La similitud coseno:

a) Suma las diferencias absolutas.  
b) Compara la forma relativa de los perfiles y puede ignorar su magnitud.  
c) Penaliza más las diferencias grandes.  

**31.** Los perfiles (2, 4, 2) y (20, 40, 20) tienen similitud coseno:

a) Igual a 1, porque son proporcionales.  
b) Cercana a 0, porque sus magnitudes difieren.  
c) Igual a −1, porque sus normas difieren.  

**32.** Si la masa se mide en gramos y la longitud de aleta en milímetros, antes de calcular distancias:

a) Debe decidirse cómo escalar las variables.  
b) Conviene excluir del análisis la variable de mayor magnitud.  
c) Conviene redondear ambas variables a valores enteros.  

**35.** K-means busca minimizar:

a) El número de grupos.  
b) La distancia entre centroides.  
c) La suma de distancias cuadráticas de cada observación a su centroide.  

**36.** El centroide de un grupo en K-means:

a) Es siempre una de las observaciones reales que pertenecen al grupo.  
b) Es la observación del grupo más alejada de los demás grupos.  
c) Es la media del grupo: un perfil promedio que puede diferir de toda observación real.  

**37.** Después de asignar cada observación al centroide más cercano, K-means:

a) Fusiona los dos grupos más cercanos.  
b) Marca como ruido los puntos alejados.  
c) Recalcula cada centroide como la media de su grupo.  

**38.** K-means++ y los reinicios múltiples se usan para:

a) Reducir el riesgo de resultados locales deficientes.  
b) Elegir automáticamente el valor de K.  
c) Detectar observaciones de ruido.  

**39.** K-means es adecuado cuando:

a) Los grupos son curvos o alargados, con fronteras irregulares.  
b) Los grupos son compactos, de dispersión semejante y con variables numéricas escaladas.  
c) Los grupos tienen densidades muy diferentes entre sí.  

**40.** Una situación problemática para K-means es la presencia de:

a) Grupos compactos, de dispersión y tamaño semejantes.  
b) Grupos curvos o de densidades diferentes.  
c) Variables numéricas escaladas a una misma escala.  

**41.** Respecto de las observaciones alejadas, K-means:

a) Asigna siempre cada observación a algún grupo.  
b) Las etiqueta como ruido.  
c) Las elimina del análisis.  

**42.** Al aumentar K, la inercia:

a) Disminuye siempre.  
b) Aumenta siempre.  
c) Se mantiene constante.  

**43.** El método del codo:

a) Determina de forma inequívoca un único valor óptimo de K.  
b) Busca rendimientos decrecientes de la inercia y se combina con otros criterios para elegir K.  
c) Elige el valor de K que maximiza la silhouette promedio.  

**44.** Para elegir K se recomienda combinar:

a) Únicamente el valor mínimo de la inercia.  
b) El número de variables y el número de observaciones.  
c) Inercia, métricas, tamaños, estabilidad, simplicidad y utilidad de los perfiles.  

**45.** El clustering jerárquico aglomerativo:

a) Comienza con un único conjunto y lo divide sucesivamente.  
b) Fija K centroides y reasigna observaciones.  
c) Comienza con una observación por grupo y fusiona grupos cercanos.  

**46.** El clustering jerárquico divisivo:

a) Comienza con una observación por grupo y fusiona grupos cercanos.  
b) Comienza con un único conjunto y lo divide sucesivamente.  
c) Fija K centroides y reasigna observaciones.  

**47.** En el clustering aglomerativo, una fusión temprana:

a) Se deshace si mejora la inercia.  
b) Se revisa en cada iteración posterior.  
c) Permanece en el resto de la jerarquía.  

**48.** El enlace simple:

a) Usa el par más lejano y favorece grupos compactos.  
b) Usa el par más cercano y puede encadenar regiones mediante puntos puente.  
c) Minimiza el aumento de dispersión dentro de los grupos.  

**49.** El enlace completo:

a) Usa el par más cercano y puede encadenar regiones.  
b) Usa el par más lejano, favorece la compactación y es sensible a extremos.  
c) Promedia todas las distancias entre pares.  

**50.** El enlace de Ward:

a) Fusiona los grupos que producen el menor aumento de dispersión.  
b) Usa el par más cercano entre grupos.  
c) Usa el par más lejano entre grupos.  

**51.** En un dendrograma, el orden horizontal de las hojas:

a) Representa la distancia entre observaciones.  
b) Indica el orden en que se registraron los datos.  
c) Carece de significado como distancia.  

**52.** El dendrograma permite:

a) Calcular la silhouette de cada observación.  
b) Identificar los puntos de ruido.  
c) Examinar varias granularidades de agrupamiento.  

**53.** DBSCAN usa como parámetros:

a) El número de grupos K.  
b) El tipo de enlace entre grupos.  
c) El radio ε y min_samples.  

**54.** En DBSCAN, un punto núcleo:

a) Está cerca de un núcleo, pero no es núcleo.  
b) Tiene suficientes vecinos dentro del radio ε.  
c) Está fuera de las regiones densas.  

**55.** En DBSCAN, un punto frontera:

a) Está cerca de un núcleo, pero no es núcleo.  
b) Tiene suficientes vecinos dentro del radio ε.  
c) Está fuera de las regiones densas.  

**56.** Que DBSCAN marque un punto como ruido significa que:

a) Es un error de medición que conviene eliminar.  
b) Es irrelevante para el análisis y puede descartarse.  
c) Quedó fuera de las regiones densas bajo esa configuración de parámetros.  

**57.** Una característica de DBSCAN frente a K-means es que:

a) Asigna siempre todas las observaciones a un grupo.  
b) Representa cada grupo mediante un centroide.  
c) Puede encontrar formas arbitrarias y prescinde de fijar K.  

**58.** En DBSCAN, un radio ε grande tiende a:

a) Fusionar regiones.  
b) Fragmentar regiones.  
c) Aumentar la cantidad de ruido.  

**59.** En DBSCAN, cambiar el escalado de las variables:

a) Deja intactas las vecindades.  
b) Modifica únicamente min_samples.  
c) Cambia el significado de ε.  

**60.** Para elegir los parámetros de DBSCAN se recomienda:

a) Explorar una grilla y buscar configuraciones estables.  
b) Elegir la configuración con la mejor cifra aislada.  
c) Fijar ε igual al número de grupos deseado.  

**61.** Una silhouette cercana a 1 indica:

a) Un caso fronterizo.  
b) Cohesión y separación altas.  
c) Una observación más cercana a otro grupo.  

**62.** Una silhouette negativa indica que la observación:

a) Está, en promedio, más cerca de otro grupo.  
b) Tiene cohesión y separación altas.  
c) Es el centroide de su grupo.  

**63.** ¿Qué métrica interna es preferible con valores menores?

a) Davies–Bouldin.  
b) Silhouette.  
c) Calinski–Harabasz.  

**64.** El índice de Calinski–Harabasz:

a) Compara cada grupo con su rival; valores menores son preferibles.  
b) Cuenta coincidencias con una clasificación externa.  
c) Compara la dispersión entre grupos con la interna; valores mayores indican mayor separación relativa.  

**65.** El índice de Davies–Bouldin:

a) Compara la dispersión entre grupos con la interna; valores mayores son preferibles.  
b) Compara cada grupo con su grupo rival; valores menores son preferibles.  
c) Cuenta coincidencias con una clasificación externa.  

**66.** Las métricas internas de clustering:

a) Identifican por sí solas la segmentación útil.  
b) Son independientes de la escala de las variables.  
c) Dependen de la representación y la geometría, y por sí solas resultan insuficientes para identificar una segmentación útil.  

**67.** Repetir el clustering sobre submuestras permite evaluar:

a) La accuracy de los grupos.  
b) Si los perfiles sobreviven a cambios de muestra.  
c) La cantidad óptima de variables.  

**68.** Comparar los resultados de varios reinicios permite evaluar:

a) Si la optimización llega a particiones parecidas.  
b) La accuracy de los grupos.  
c) La cantidad óptima de variables.  

**69.** Al describir los grupos obtenidos se recomienda:

a) Usar etiquetas valorativas.  
b) Informar los perfiles solo en unidades estandarizadas.  
c) Usar nombres descriptivos y perfiles en unidades originales.  

**70.** Encontrar un grupo mediante clustering:

a) Demuestra la existencia de una clase natural.  
b) Resulta insuficiente para demostrar una clase natural o una causa.  
c) Demuestra una relación causal.  

**71.** Después de agrupar pingüinos con las cuatro medidas, cruzar los grupos con species es legítimo para:

a) Describir coincidencias y desacuerdos con una referencia externa.  
b) Afirmar que el algoritmo predijo la especie.  
c) Elegir retrospectivamente la mejor configuración.  

**72.** ¿Cuál es un uso incorrecto de la variable species en el caso Palmer Penguins?

a) Describir coincidencias y desacuerdos con los grupos.  
b) Evaluar los grupos frente a una referencia externa.  
c) Usarla para elegir retrospectivamente la mejor configuración.  

**73.** En el caso Palmer Penguins, las variables species, island y sex:

a) Se reservan y quedan fuera de la formación de los grupos.  
b) Se usan para formar los grupos.  
c) Se estandarizan junto con las medidas morfológicas.  

**74.** La inercia resume:

a) La dispersión interna de los grupos de K-means.  
b) La cohesión y la separación de cada observación.  
c) La coincidencia con una referencia externa.  


## Clave del banco

| N.º | Respuesta | Bloque | Sección de origen |
|---|---|---|---|
| 1 | c | Atributos | Clase 6 – Categorías, discretización y binarización (Cap. 10 §10.1.4) |
| 2 | b | Atributos | Clase 6 – Categorías, discretización y binarización (Cap. 10 §10.1.4) |
| 3 | a | Atributos | Clase 6 – Categorías, discretización y binarización |
| 4 | b | Atributos | Clase 6 – Categorías, discretización y binarización |
| 5 | a | Atributos | Clase 6 – Tiempo, espacio e interacciones (Cap. 10 §10.1.5) |
| 6 | a | Atributos | Clase 6 – Transformaciones numéricas |
| 7 | b | Atributos | Clase 6 – Transformaciones numéricas |
| 8 | b | Atributos | Clase 6 – Outliers: error, evento o población distinta |
| 9 | a | Atributos | Clase 6 – Tiempo, espacio e interacciones (Cap. 10 §10.1.3) |
| 11 | a | Selección, reducción y PCA | Clase 6 – Selección y reducción son distintas |
| 12 | b | Selección, reducción y PCA | Clase 6 – Selección y reducción son distintas |
| 13 | c | Selección, reducción y PCA | Clase 6 – Familias de selección de atributos (Cap. 10 §10.2.2) |
| 14 | b | Selección, reducción y PCA | Clase 6 – Familias de selección de atributos (Cap. 10 §10.2.3) |
| 15 | b | Selección, reducción y PCA | Clase 6 – Familias de selección de atributos (Cap. 10 §10.2.4) |
| 16 | a | Selección, reducción y PCA | Clase 6 – Familias de selección de atributos |
| 17 | a | Selección, reducción y PCA | Clase 6 – Familias de selección de atributos |
| 18 | c | Selección, reducción y PCA | Clase 6 – Reducir dimensión: por qué (Cap. 10 §10.3.1) |
| 19 | b | Selección, reducción y PCA | Clase 6 – PCA: componentes principales (Cap. 10 §10.3.3) |
| 20 | a | Selección, reducción y PCA | Clase 6 – PCA: componentes principales (Cap. 10 §10.3.3) |
| 21 | b | Selección, reducción y PCA | Clase 6 – PCA: componentes principales |
| 22 | c | Selección, reducción y PCA | Clase 6 – PCA: componentes principales |
| 23 | c | Selección, reducción y PCA | Clase 6 – Varianza explicada y límites de PCA (Cap. 10 §10.3.4) |
| 24 | b | Selección, reducción y PCA | Clase 6 – Varianza explicada y límites de PCA |
| 25 | c | Selección, reducción y PCA | Clase 6 – Varianza explicada y límites de PCA |
| 26 | c | Semejanza y distancias | Clase 6 – Aprendizaje no supervisado (Cap. 13 §13.1.1) |
| 27 | a | Semejanza y distancias | Clase 6 – Aprendizaje no supervisado (Cap. 13 §13.1.1) |
| 28 | b | Semejanza y distancias | Clase 6 – Distancia euclídea (Cap. 13 §13.1.2) |
| 29 | b | Semejanza y distancias | Clase 6 – Manhattan y coseno (Cap. 13 §13.1.3) |
| 30 | b | Semejanza y distancias | Clase 6 – Manhattan y coseno (Cap. 13 §13.1.4) |
| 31 | a | Semejanza y distancias | Cap. 13 §13.1.4 – Similitud coseno |
| 32 | a | Semejanza y distancias | Clase 6 – Transformaciones numéricas / Escalado |
| 35 | c | K-means | Clase 6 – K-means: objetivo (Cap. 13 §13.2.1) |
| 36 | c | K-means | Clase 6 – K-means: objetivo (Cap. 13 §13.2.1) |
| 37 | c | K-means | Clase 6 – K-means: procedimiento |
| 38 | a | K-means | Clase 6 – K-means: procedimiento (Cap. 13 §13.2.2) |
| 39 | b | K-means | Clase 6 – Cuándo sirve K-means |
| 40 | b | K-means | Clase 6 – Cuándo sirve K-means |
| 41 | a | K-means | Clase 6 – Cuándo sirve K-means |
| 42 | a | K-means | Clase 6 – Elegir K (Cap. 13 §13.4.1) |
| 43 | b | K-means | Clase 6 – Elegir K (Cap. 13 §13.2.3) |
| 44 | c | K-means | Clase 6 – Elegir K |
| 45 | c | Clustering jerárquico | Clase 6 – Clustering jerárquico (Cap. 13 §13.2.5) |
| 46 | b | Clustering jerárquico | Clase 6 – Clustering jerárquico (Cap. 13 §13.2.5) |
| 47 | c | Clustering jerárquico | Clase 6 – Clustering jerárquico (Cap. 13 §13.2.4) |
| 48 | b | Clustering jerárquico | Clase 6 – Enlaces y dendrogramas (Cap. 13 §13.2.6) |
| 49 | b | Clustering jerárquico | Clase 6 – Enlaces y dendrogramas (Cap. 13 §13.2.6) |
| 50 | a | Clustering jerárquico | Clase 6 – Enlaces y dendrogramas (Cap. 13 §13.2.6) |
| 51 | c | Clustering jerárquico | Clase 6 – Enlaces y dendrogramas (Cap. 13 §13.2.7) |
| 52 | c | Clustering jerárquico | Clase 6 – Clustering jerárquico |
| 53 | c | DBSCAN | Clase 6 – DBSCAN: densidad y ruido (Cap. 13 §13.3.2) |
| 54 | b | DBSCAN | Clase 6 – DBSCAN: densidad y ruido (Cap. 13 §13.3.2) |
| 55 | a | DBSCAN | Clase 6 – DBSCAN: densidad y ruido (Cap. 13 §13.3.2) |
| 56 | c | DBSCAN | Clase 6 – Sensibilidad de DBSCAN (Cap. 13 §13.3.3) |
| 57 | c | DBSCAN | Clase 6 – DBSCAN: densidad y ruido |
| 58 | a | DBSCAN | Clase 6 – Sensibilidad de DBSCAN (Cap. 13 §13.3.4) |
| 59 | c | DBSCAN | Clase 6 – Sensibilidad de DBSCAN (Cap. 13 §13.3.4) |
| 60 | a | DBSCAN | Clase 6 – Sensibilidad de DBSCAN |
| 61 | b | Evaluación e interpretación | Clase 6 – Silhouette (Cap. 13 §13.4.2) |
| 62 | a | Evaluación e interpretación | Clase 6 – Silhouette (Cap. 13 §13.4.2) |
| 63 | a | Evaluación e interpretación | Clase 6 – Métricas internas |
| 64 | c | Evaluación e interpretación | Clase 6 – Calinski–Harabasz y Davies–Bouldin |
| 65 | b | Evaluación e interpretación | Clase 6 – Calinski–Harabasz y Davies–Bouldin (Cap. 13 §13.4.3) |
| 66 | c | Evaluación e interpretación | Clase 6 – Métricas internas |
| 67 | b | Evaluación e interpretación | Clase 6 – Estabilidad y casos frontera |
| 68 | a | Evaluación e interpretación | Clase 6 – Estabilidad y casos frontera |
| 69 | c | Evaluación e interpretación | Clase 6 – Describir grupos con prudencia |
| 70 | b | Evaluación e interpretación | Clase 6 – Describir grupos con prudencia (Cap. 13 §13.4.4) |
| 71 | a | Evaluación e interpretación | Clase 6 – Comparación externa posterior |
| 72 | c | Evaluación e interpretación | Clase 6 – Comparación externa posterior |
| 73 | a | Evaluación e interpretación | Clase 6 – Caso conductor: Palmer Penguins |
| 74 | a | Evaluación e interpretación | Clase 6 – Métricas internas (Cap. 13 §13.4.1) |
