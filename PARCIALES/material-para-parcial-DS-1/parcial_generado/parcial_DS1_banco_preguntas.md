# Parcial 1: Ciencia de Datos 2026 — Banco de preguntas

Total: 106 preguntas. Fuente: Clases 01–05 (PDF) y capítulos 5 y 9 como respaldo.

**1.** ¿Cuál de las siguientes afirmaciones describe la Ciencia de Datos según lo visto en clase?

a) Una disciplina centrada exclusivamente en programar y entrenar modelos predictivos.  
b) Una técnica de almacenamiento masivo de datos para su consulta posterior.  
c) Un campo interdisciplinario que obtiene conocimiento a partir de datos, comunica evidencia y apoya decisiones.  

**2.** En la taxonomía de preguntas analíticas, la pregunta «¿Qué acción conviene?» corresponde al objetivo de:

a) Describir.  
b) Diagnosticar.  
c) Prescribir.  

**3.** En la taxonomía de preguntas analíticas, la pregunta «¿Qué está cambiando? ¿Se degradó la cobertura o el modelo?» corresponde al objetivo de:

a) Predecir.  
b) Monitorear.  
c) Describir.  

**4.** En el proceso KDD (Knowledge Discovery in Databases), la minería de datos es:

a) Un sinónimo del proceso KDD completo.  
b) La etapa final de despliegue del modelo.  
c) Una etapa dentro del proceso completo.  

**5.** El ciclo CRISP-DM comienza por:

a) La comprensión del problema.  
b) El modelado.  
c) La preparación de los datos.  

**6.** La unidad de análisis (U) de un problema es:

a) La entidad elemental descrita, predicha o decidida, que define el significado de una fila.  
b) El conjunto de unidades sobre las que se desea generalizar o actuar.  
c) El periodo temporal que abarca el proyecto.  

**7.** ¿Cuál es un ejemplo de datos semiestructurados?

a) Una tabla SQL de viajes con esquema explícito.  
b) Grabaciones de audio de llamadas de reclamo.  
c) Eventos en formato JSON con claves y esquema flexible.  

**8.** En la especificación compacta P = (U, R, O, X, Y, A, H, C), la letra H representa:

a) El horizonte temporal.  
b) La hipótesis del modelo.  
c) El historial de datos disponible.  

**9.** Entre las seis V de Big Data, la Veracidad se pregunta por:

a) La confiabilidad de los datos.  
b) La latencia con que llegan los datos.  
c) La cantidad de datos disponibles.  

**10.** Respecto de la reproducibilidad, el uso de una semilla aleatoria:

a) Ayuda, pero requiere además datos, entorno y partición versionados.  
b) Garantiza por sí sola la reproducibilidad completa.  
c) Reemplaza la necesidad de versionar el código.  

**11.** El linaje de un dato responde a la pregunta:

a) ¿De dónde viene?  
b) ¿Qué transformaciones se le aplicaron?  
c) ¿Qué formato de archivo tiene?  

**12.** La granularidad de una tabla indica:

a) La proporción de valores faltantes.  
b) El número de columnas.  
c) El nivel de detalle temporal, espacial y de entidad.  

**13.** El valor «00123», almacenado como texto y usado como código postal, tiene tipo semántico de:

a) Cantidad de razón.  
b) Identificador nominal.  
c) Categoría ordinal.  

**14.** La dimensión de calidad «Oportunidad» pregunta si el dato:

a) Llega antes de usarlo.  
b) Cumple dominio, formato y rango.  
c) Tiene una clave que identifica una única fila.  

**15.** La dimensión de calidad «Unicidad» controla que:

a) Los campos concuerden entre fuentes.  
b) El dato represente la población, el lugar y el periodo.  
c) La clave identifique una única fila.  

**16.** Un duplicado de clave consiste en registros que:

a) Coinciden en la clave y difieren en otros atributos.  
b) Coinciden en todas sus columnas.  
c) Representan el mismo objeto y carecen de una clave común.  

**17.** Si muchas ventas pertenecen a una misma tienda, la unión ventas → tiendas es:

a) one-to-many.  
b) many-to-one.  
c) many-to-many.  

**18.** Una unión many-to-many accidental puede:

a) Reducir el número de columnas.  
b) Ordenar las filas por clave.  
c) Multiplicar filas y totales.  

**19.** Al agregar viajes individuales en una tabla zona-hora se gana comparabilidad y se pierde:

a) El detalle individual y el orden dentro de cada grupo.  
b) La unidad útil para la pregunta.  
c) La posibilidad de contar viajes por zona.  

**20.** Antes de imputar valores faltantes, se recomienda:

a) Reemplazarlos por cero.  
b) Explicar el mecanismo que los produjo y el costo de equivocarse.  
c) Eliminar las variables que los contienen.  

**21.** Las marcas horarias «10:00 UTC» y «10:00 America/New_York»:

a) Representan el mismo instante.  
b) Representan instantes distintos.  
c) Difieren solo en el formato de escritura.  

**22.** ¿Cuál de las siguientes es una función del análisis exploratorio de datos (EDA)?

a) Generar hipótesis y controles.  
b) Confirmar relaciones causales.  
c) Reparar automáticamente los datos.  

**23.** Una celda vacía en la precipitación registrada por NOAA debe interpretarse como:

a) Una medición faltante.  
b) Precipitación igual a cero.  
c) Una unidad ausente del marco.  

**24.** Frente a valores extremos, la mediana es:

a) Más sensible que la media.  
b) Menos sensible que la media.  
c) Igual de sensible que la media.  

**25.** El rango intercuartílico (IQR) resume:

a) La diferencia entre el máximo y el mínimo.  
b) La extensión del 50 % central de los datos.  
c) La distancia típica respecto de la media.  

**26.** La varianza se expresa en:

a) Las mismas unidades de la variable.  
b) Porcentaje respecto de la media.  
c) Unidades al cuadrado de la variable.  

**27.** Un valor marcado como atípico por la regla de Tukey:

a) Es un error y debe eliminarse.  
b) Requiere investigación o contexto antes de decidir qué hacer con él.  
c) Indica una falla del instrumento de medición.  

**28.** El coeficiente de correlación de Pearson mide:

a) La asociación lineal estandarizada, entre −1 y 1.  
b) La asociación de orden monotónica, basada en rangos.  
c) La variación lineal conjunta, en producto de unidades.  

**29.** Una correlación de Pearson cercana a cero:

a) Es compatible con una dependencia fuerte de tipo curvo.  
b) Demuestra que las variables son independientes.  
c) Indica un error de medición.  

**30.** La paradoja de Simpson ocurre cuando:

a) Un punto influyente domina el coeficiente de correlación.  
b) Dos variables presentan correlación cercana a cero.  
c) El patrón agregado cambia o se invierte dentro de los estratos.  

**32.** La apariencia de un histograma depende de:

a) El orden en que se registraron las observaciones.  
b) El ancho, el origen y los límites de los intervalos (bins).  
c) El nombre asignado a la variable.  

**33.** Replicar una observación de una estación meteorológica en todas las zonas:

a) Crea nuevas observaciones meteorológicas independientes.  
b) Aumenta el tamaño aparente, pero mantiene la misma información independiente.  
c) Mejora la representatividad espacial del clima.  

**34.** En una tabla de contingencia normalizada por fila, las proporciones suman 100 %:

a) Dentro de cada columna.  
b) Sobre el total de la tabla.  
c) Dentro de cada fila.  

**35.** Una tasa se calcula como:

a) Eventos sobre exposición.  
b) Casos de interés sobre el total definido.  
c) Cantidad de eventos registrados.  

**36.** La afirmación «El 3 % de las muestras registradas tuvo detección» es:

a) Predictiva.  
b) Descriptiva.  
c) Prescriptiva.  

**37.** La afirmación «Conviene revisar este sitio» es:

a) Prescriptiva.  
b) Descriptiva.  
c) Predictiva.  

**38.** La afirmación «Una nueva muestra tiene 3 % de probabilidad de detección» es:

a) Predictiva.  
b) Descriptiva.  
c) Prescriptiva.  

**39.** Un parámetro es:

a) Una cantidad fija pero desconocida de la población.  
b) Una función calculable a partir de los datos observados.  
c) El tamaño de la muestra.  

**40.** El estadístico p̂ = x/n:

a) Coincide siempre con el parámetro p.  
b) Se calcula sobre la población completa.  
c) Se calcula con la muestra y se usa como estimación del parámetro p.  

**41.** Si se repite el mismo diseño de muestreo sobre una población estable y la estimación cambia entre muestras, esa dispersión expresa:

a) Un error de programación.  
b) Variabilidad muestral.  
c) Sesgo de selección.  

**42.** Visitar únicamente los sitios de acceso sencillo es un ejemplo de:

a) Sesgo: el procedimiento apunta sistemáticamente fuera del objetivo.  
b) Variabilidad muestral.  
c) Error estándar.  

**43.** Una muestra muy grande obtenida con un mecanismo de selección sesgado produce:

a) Una estimación libre de sesgo.  
b) Una estimación con alta variabilidad.  
c) Una estimación estable que puede seguir sesgada.  

**44.** La representatividad de una muestra depende principalmente de:

a) El formato de almacenamiento de los datos.  
b) El proceso que produjo los datos.  
c) El número de columnas de la tabla.  

**45.** En un muestreo aleatorio simple de tamaño n:

a) La población se divide en estratos y se sortea dentro de cada uno.  
b) Cada conjunto posible de n unidades tiene la misma probabilidad de ser elegido.  
c) Se eligen las unidades de acceso más sencillo.  

**46.** El muestreo estratificado:

a) Realiza un único sorteo sobre toda la población.  
b) Selecciona las unidades por orden de llegada.  
c) Divide la población en grupos mutuamente excluyentes y sortea dentro de cada uno.  

**47.** Si una unidad está ausente del marco de muestreo, el sorteo aleatorio:

a) Corrige esa ausencia automáticamente.  
b) Le asigna mayor probabilidad de inclusión.  
c) Mantiene esa exclusión, porque el marco es anterior al sorteo.  

**48.** Un evento es:

a) El conjunto de todos los resultados posibles.  
b) La frecuencia relativa de un resultado.  
c) Un subconjunto del espacio muestral.  

**49.** La probabilidad del complemento de un evento D se obtiene como:

a) P(D) / 2.  
b) 1 − P(D).  
c) P(D) · P(D).  

**50.** P(A ∩ B) representa la probabilidad de que:

a) Ocurra A dado que ocurrió B.  
b) Ocurra al menos uno de los dos eventos.  
c) Ocurran ambos eventos.  

**51.** Al calcular P(A | B):

a) El universo se restringe a los casos donde ocurrió B.  
b) El denominador es el total de casos observados.  
c) Se multiplica P(A) por P(B).  

**53.** Dos eventos mutuamente excluyentes, ambos con probabilidad positiva:

a) Son dependientes, porque si ocurre uno el otro es imposible.  
b) Son independientes.  
c) Tienen probabilidad conjunta igual al producto de sus marginales.  

**54.** Las probabilidades P(alerta | detección) y P(detección | alerta):

a) Usan denominadores distintos y, en general, difieren.  
b) Son siempre iguales.  
c) Suman siempre 1.  

**55.** Una alerta muy sensible ante un evento raro puede:

a) Eliminar los falsos positivos.  
b) Producir muchas falsas alarmas.  
c) Garantizar que cada alerta sea una detección real.  

**56.** El sitio A tiene 1 detección en 2 muestras (50 %) y el sitio B, 40 en 100 (40 %). ¿Qué afirmación es correcta?

a) El sitio A tiene con certeza mayor riesgo que el sitio B.  
b) Ambas proporciones son igualmente estables.  
c) La proporción de A es menos estable porque se basa en dos observaciones.  

**57.** El error estándar de una proporción disminuye con el tamaño de muestra n según:

a) Una relación lineal: duplicar la muestra lo reduce a la mitad.  
b) La raíz cuadrada de n: cuadruplicar la muestra lo reduce aproximadamente a la mitad.  
c) Una relación constante: se mantiene igual para cualquier n.  

**58.** Respecto de la desviación estándar s y el error estándar de la media:

a) Ambos describen la dispersión de los datos individuales.  
b) s describe la dispersión de los datos individuales; el error estándar, la estabilidad del estimador.  
c) El error estándar describe los datos individuales y s, la estabilidad del estimador.  

**59.** El bootstrap aproxima la variabilidad de un estadístico mediante:

a) La división de los datos en entrenamiento y prueba.  
b) Remuestreo con reemplazo del mismo tamaño que la muestra original.  
c) Una fórmula cerrada del error estándar.  

**60.** Al aplicar bootstrap a datos agrupados o con dependencia temporal:

a) El remuestreo debe respetar los grupos, el tiempo o la dependencia.  
b) Se remuestrean filas individuales en cualquier caso.  
c) Se ordenan los datos por valor antes de remuestrear.  

**61.** Aumentar el tamaño de una muestra mal seleccionada:

a) Reduce la variabilidad, pero mantiene el sesgo.  
b) Elimina el sesgo.  
c) Aumenta la variabilidad.  

**62.** En un problema de decisión, las acciones son:

a) Condiciones desconocidas al momento de decidir.  
b) Alternativas bajo control del decisor.  
c) Resultados de combinar una acción con un estado.  

**63.** En un problema de decisión, los estados son:

a) Alternativas bajo control del decisor.  
b) Condiciones desconocidas al momento de decidir.  
c) La evidencia disponible antes de elegir.  

**64.** Un falso positivo y un falso negativo que ocurren con la misma frecuencia:

a) Tienen siempre el mismo costo.  
b) Se compensan entre sí en el costo esperado.  
c) Pueden tener importancias muy distintas.  

**65.** El costo esperado de una acción se obtiene:

a) Ponderando el costo de cada estado por su probabilidad y sumando.  
b) Tomando el mayor costo posible de la acción.  
c) Promediando los costos de todas las celdas con igual peso.  

**66.** El cálculo del costo esperado de cada acción:

a) Predice qué ocurrirá en un caso concreto.  
b) Determina la probabilidad de cada estado.  
c) Compara consecuencias promedio bajo probabilidades y costos explícitos.  

**67.** Dos organizaciones con la misma probabilidad estimada pueden elegir acciones distintas porque:

a) Enfrentan costos, capacidades o responsabilidades diferentes.  
b) La probabilidad cambia según quién la calcule.  
c) La probabilidad determina por sí sola la acción.  

**71.** La incertidumbre epistémica:

a) Proviene de conocimiento limitado y puede reducirse con más datos pertinentes o mejores mediciones.  
b) Es la variabilidad inherente al fenómeno, que persiste aun con parámetros conocidos.  
c) Corresponde al costo de una decisión equivocada.  

**72.** La incertidumbre aleatoria:

a) Proviene de contar con pocos datos.  
b) Representa variabilidad inherente al fenómeno y persiste aun con parámetros conocidos.  
c) Se elimina al ampliar la muestra histórica.  

**73.** La frecuencia relativa de un evento en repeticiones comparables:

a) Es la probabilidad exacta en cualquier muestra.  
b) Mide el costo del evento.  
c) Puede aproximar su probabilidad.  

**74.** En Machine Learning, aprender de los datos significa:

a) Ajustar una función f: X → Y a partir de ejemplos.  
b) Memorizar los casos históricos.  
c) Almacenar los datos en una tabla.  

**75.** ¿Qué nivel responde a la pregunta «¿Qué salida necesitamos?»?

a) Paradigma.  
b) Algoritmo.  
c) Tarea.  

**76.** ¿Qué nivel responde a la pregunta «¿De dónde proviene la señal de aprendizaje?»?

a) Tarea.  
b) Paradigma.  
c) Algoritmo.  

**77.** En aprendizaje supervisado, el conjunto de entrenamiento contiene:

a) Únicamente entradas x para agrupar por similitud.  
b) Pares (x, y) con respuesta conocida.  
c) Predicciones ŷ de un modelo previo.  

**78.** El aprendizaje semisupervisado:

a) Trabaja únicamente con casos etiquetados.  
b) Prescinde de etiquetas incluso para la evaluación final.  
c) Combina pocos casos etiquetados con muchos casos carentes de etiqueta.  

**79.** Estimar la concentración de un contaminante en mg/L corresponde a una tarea de:

a) Clasificación.  
b) Clustering.  
c) Regresión.  

**80.** Determinar si una medición supera un límite para activar una inspección corresponde a una tarea de:

a) Regresión.  
b) Clustering.  
c) Clasificación.  

**81.** Codificar numéricamente una categoría (por ejemplo, 0, 1 y 2):

a) Mantiene la tarea como clasificación.  
b) Convierte la tarea en regresión.  
c) Convierte la tarea en clustering.  

**82.** En la definición de un problema predictivo, t0 representa:

a) El periodo futuro donde se define el resultado.  
b) El instante en que debe emitirse la predicción.  
c) El momento en que se confirma la etiqueta.  

**83.** Generalizar significa:

a) Obtener error cero en entrenamiento.  
b) Aplicar el modelo a cualquier población futura.  
c) Mantener un desempeño útil en casos nuevos de la población objetivo.  

**84.** El conjunto de validación se usa para:

a) Elegir variables, configuración y umbral.  
b) Ajustar los parámetros del modelo.  
c) Medir una única vez el procedimiento congelado.  

**85.** El conjunto de prueba se usa para:

a) Elegir los hiperparámetros.  
b) Ajustar las transformaciones de los datos.  
c) Medir una única vez el procedimiento congelado.  

**86.** Consultar repetidamente el conjunto de prueba y modificar el procedimiento según el resultado:

a) Convierte la prueba en validación.  
b) Mejora la estimación de generalización.  
c) Equivale a aplicar validación cruzada.  

**88.** Si el modelo deberá predecir un periodo futuro, la partición recomendada es:

a) Aleatoria.  
b) Temporal.  
c) Estratificada por clase.  

**89.** La partición estratificada:

a) Mantiene juntos los registros de un mismo grupo.  
b) Ordena los datos según el tiempo.  
c) Conserva aproximadamente la proporción de clases.  

**90.** Existe fuga de información cuando el ajuste o la evaluación:

a) Obtienen bajo desempeño en entrenamiento.  
b) Se comparan contra un baseline simple.  
c) Utilizan información que estaría indisponible al producir una predicción real.  

**91.** Para imputar faltantes con la media, el procedimiento correcto es:

a) Separar primero y ajustar el imputador solo con entrenamiento.  
b) Calcular la media con todos los datos antes de separar.  
c) Calcular la media con el conjunto de prueba.  

**92.** Si un mismo evento aparece duplicado en entrenamiento y en prueba, un acierto sobre la copia:

a) Exagera la capacidad de generalización del modelo.  
b) Demuestra que el modelo generaliza a muestras nuevas.  
c) Mejora la validez de la evaluación.  

**93.** La selección de atributos basada en datos debe realizarse:

a) Usando el conjunto de prueba.  
b) Con todos los datos antes de particionar.  
c) Dentro de entrenamiento o de cada fold.  

**94.** Un baseline es:

a) El mejor modelo obtenido en validación.  
b) El modelo final que se despliega.  
c) Una referencia simple y reproducible, disponible con la misma información que el modelo.  

**95.** Un baseline posible para una serie temporal es:

a) Repetir el último valor o el del mismo periodo anterior.  
b) Predecir la clase mayoritaria.  
c) Asignar todas las observaciones a un único grupo.  

**96.** Con 20 excedencias en 100 mediciones, un baseline que siempre predice «normal» obtiene:

a) Accuracy baja y recall alto.  
b) Accuracy alta y recall nulo.  
c) Accuracy y recall altos.  

**97.** En clasificación, la métrica precisión (precision) responde a la pregunta:

a) De los eventos reales, ¿cuántos se detectaron?  
b) Del total de casos, ¿qué fracción fue acertada?  
c) De las alertas emitidas, ¿cuántas eran correctas?  

**98.** En clasificación, la métrica recall (sensibilidad) responde a la pregunta:

a) De las alertas emitidas, ¿cuántas eran correctas?  
b) De los eventos reales, ¿cuántos se detectaron?  
c) Del total de casos, ¿qué fracción fue acertada?  

**99.** En la matriz de confusión, un falso negativo es:

a) Una falsa alarma.  
b) Un acierto sobre la clase negativa.  
c) Un positivo omitido.  

**100.** La métrica F1:

a) Incorpora los verdaderos negativos.  
b) Equilibra precisión y recall.  
c) Equivale a la accuracy.  

**101.** Si omitir una excedencia es más costoso que realizar una inspección innecesaria, merece especial atención:

a) La precisión.  
b) El recall.  
c) La accuracy.  

**102.** En comparación con MAE, la métrica RMSE:

a) Pondera linealmente la magnitud del error.  
b) Penaliza más los errores grandes.  
c) Se expresa en unidades al cuadrado del objetivo.  

**103.** El coeficiente R²:

a) Se expresa en la unidad del objetivo.  
b) Toma siempre valores entre 0 y 1.  
c) Compara el error del modelo con el de predecir la media.  

**104.** El índice silhouette:

a) Mide la accuracy predictiva de los grupos.  
b) Combina cohesión y separación en una escala aproximada de −1 a 1.  
c) Indica el número de observaciones de cada grupo.  

**105.** Al evaluar series temporales se recomienda:

a) Barajar las observaciones antes de dividirlas.  
b) Entrenar con el pasado, validar en periodos posteriores y comparar contra persistencia.  
c) Usar un único corte temporal elegido por conveniencia.  

**106.** En validación cruzada K-fold:

a) La prueba final se incluye como uno de los K bloques.  
b) Cada bloque actúa una vez como validación y la prueba final permanece fuera del ciclo.  
c) Un único bloque actúa como validación en todas las iteraciones.  

**107.** En cada iteración de la validación cruzada, la imputación y el escalado se ajustan con:

a) Los folds de entrenamiento.  
b) Todos los datos disponibles, una sola vez.  
c) El fold de validación.  

**108.** En las curvas de pérdida, el sobreajuste se reconoce cuando:

a) La pérdida de entrenamiento sigue bajando, la de validación deja de mejorar y la separación aumenta.  
b) Ambas pérdidas, de entrenamiento y de validación, son altas.  
c) La pérdida de validación alcanza su mínimo.  

**109.** En las curvas de pérdida, el subajuste se reconoce cuando:

a) Ambas pérdidas, de entrenamiento y de validación, son altas.  
b) La pérdida de entrenamiento baja y la de validación aumenta.  
c) La pérdida de validación alcanza su mínimo.  

**110.** Superar un baseline débil:

a) Demuestra la utilidad del modelo.  
b) Garantiza la generalización del modelo.  
c) Resulta insuficiente para demostrar utilidad.  

**111.** Si el modelo se usará para predecir otra fila independiente de la misma población, la partición recomendada es:

a) Temporal dentro de cada grupo.  
b) Por grupos.  
c) Aleatoria o estratificada.  

**112.** Si la evaluación debe medir la transferencia del modelo hacia sitios distintos de los usados en el entrenamiento, la partición recomendada es:

a) Por grupos.  
b) Temporal dentro de cada grupo.  
c) Aleatoria o estratificada.  


## Clave del banco

| N.º | Respuesta | Semana | Sección de origen |
|---|---|---|---|
| 1 | c | Semana 1 | Clase 1 – ¿Qué es la Ciencia de Datos? |
| 2 | c | Semana 1 | Clase 1 – Taxonomía de preguntas analíticas |
| 3 | b | Semana 1 | Clase 1 – Taxonomía de preguntas analíticas |
| 4 | c | Semana 1 | Clase 1 – KDD |
| 5 | a | Semana 1 | Clase 1 – CRISP-DM |
| 6 | a | Semana 1 | Clase 1 – Unidad, población y alcance |
| 7 | c | Semana 1 | Clase 1 – Estructura de los datos |
| 8 | a | Semana 1 | Clase 1 – Especificación del problema |
| 9 | a | Semana 1 | Clase 1 – Big Data |
| 10 | a | Semana 1 | Clase 1 – Herramientas y reproducibilidad |
| 11 | b | Semana 2 | Clase 2 – Procedencia y linaje |
| 12 | c | Semana 2 | Clase 2 – Unidad y granularidad |
| 13 | b | Semana 2 | Clase 2 – Tipos físicos y semánticos |
| 14 | a | Semana 2 | Clase 2 – Calidad apta al propósito |
| 15 | c | Semana 2 | Clase 2 – Calidad apta al propósito |
| 16 | a | Semana 2 | Clase 2 – Duplicados |
| 17 | b | Semana 2 | Clase 2 – Claves y cardinalidad |
| 18 | c | Semana 2 | Clase 2 – Claves y cardinalidad |
| 19 | a | Semana 2 | Clase 2 – Agregación y pérdida de información |
| 20 | b | Semana 2 | Clase 2 – Faltantes |
| 21 | b | Semana 2 | Clase 2 – Integración temporal |
| 22 | a | Semana 3 | Clase 3 – Alcance del EDA |
| 23 | a | Semana 3 | Clase 3 – Cero, faltante y ausencia de fila |
| 24 | b | Semana 3 | Clase 3 – Media, mediana y moda |
| 25 | b | Semana 3 | Clase 3 – IQR, MAD y robustez |
| 26 | c | Semana 3 | Clase 3 – Rango, varianza y desviación estándar |
| 27 | b | Semana 3 | Clase 3 – Atípico y error |
| 28 | a | Semana 3 | Clase 3 – Covarianza y correlación |
| 29 | a | Semana 3 | Clase 3 – Covarianza y correlación |
| 30 | c | Semana 3 | Clase 3 – Asociación, causalidad y Simpson |
| 32 | b | Semana 3 | Clase 3 – Histogramas |
| 33 | b | Semana 3 | Clase 3 – Trampas de correlación |
| 34 | c | Semana 3 | Clase 3 – Proporciones condicionadas |
| 35 | a | Semana 3 | Clase 3 – Conteos, proporciones y tasas |
| 36 | b | Semana 4 | Clase 4 – Describir, predecir, prescribir |
| 37 | a | Semana 4 | Clase 4 – Describir, predecir, prescribir |
| 38 | a | Semana 4 | Clase 4 – Describir, predecir, prescribir |
| 39 | a | Semana 4 | Clase 4 – Parámetro, estadístico y estimación |
| 40 | c | Semana 4 | Clase 4 – Parámetro, estadístico y estimación |
| 41 | b | Semana 4 | Clase 4 – Variabilidad muestral |
| 42 | a | Semana 4 | Clase 4 – Sesgo y variabilidad |
| 43 | c | Semana 4 | Clase 4 – Sesgo y variabilidad |
| 44 | b | Semana 4 | Clase 4 – Cobertura, selección y representatividad |
| 45 | b | Semana 4 | Clase 4 – Tipos de muestreo |
| 46 | c | Semana 4 | Clase 4 – Tipos de muestreo |
| 47 | c | Semana 4 | Clase 4 – Muestreo aleatorio simple |
| 48 | c | Semana 4 | Clase 4 – Evento y espacio muestral |
| 49 | b | Semana 4 | Clase 4 – Probabilidad marginal y complemento |
| 50 | c | Semana 4 | Clase 4 – Probabilidad conjunta |
| 51 | a | Semana 4 | Clase 4 – Probabilidad condicional |
| 53 | a | Semana 4 | Cap. 5 – 5.1.6 Independencia |
| 54 | a | Semana 4 | Clase 4 – Invertir la condición |
| 55 | b | Semana 4 | Clase 4 – Invertir la condición |
| 56 | c | Semana 4 | Clase 4 – Estimaciones y tamaño de muestra |
| 57 | b | Semana 4 | Clase 4 – Variabilidad muestral de una proporción |
| 58 | b | Semana 4 | Clase 4 – Variabilidad muestral de una media |
| 59 | b | Semana 4 | Clase 4 – Bootstrap |
| 60 | a | Semana 4 | Clase 4 – Bootstrap |
| 61 | a | Semana 4 | Clase 4 – Precisión y sesgo |
| 62 | b | Semana 4 | Clase 4 – Estados inciertos y acciones |
| 63 | b | Semana 4 | Clase 4 – Estados inciertos y acciones |
| 64 | c | Semana 4 | Clase 4 – Costos de aciertos y errores |
| 65 | a | Semana 4 | Clase 4 – Valor esperado de una acción |
| 66 | c | Semana 4 | Clase 4 – Valor esperado de una acción |
| 67 | a | Semana 4 | Clase 4 – Del análisis predictivo al prescriptivo |
| 71 | a | Semana 4 | Cap. 5 – 5.4.2 Incertidumbre epistémica |
| 72 | b | Semana 4 | Cap. 5 – 5.4.1 Incertidumbre aleatoria |
| 73 | c | Semana 4 | Clase 4 – Probabilidad como proporción de largo plazo |
| 74 | a | Semana 5 | Clase 5 – Qué significa aprender |
| 75 | c | Semana 5 | Clase 5 – Paradigma, tarea y algoritmo |
| 76 | b | Semana 5 | Clase 5 – Paradigma, tarea y algoritmo |
| 77 | b | Semana 5 | Clase 5 – Aprendizaje supervisado |
| 78 | c | Semana 5 | Clase 5 – Aprendizaje semisupervisado |
| 79 | c | Semana 5 | Clase 5 – Un dominio, cuatro formulaciones |
| 80 | c | Semana 5 | Clase 5 – Un dominio, cuatro formulaciones |
| 81 | a | Semana 5 | Clase 5 – Cuatro tareas de análisis |
| 82 | b | Semana 5 | Clase 5 – Instante y horizonte |
| 83 | c | Semana 5 | Clase 5 – Generalización |
| 84 | a | Semana 5 | Clase 5 – Entrenamiento, validación y prueba |
| 85 | c | Semana 5 | Clase 5 – Entrenamiento, validación y prueba |
| 86 | a | Semana 5 | Clase 5 – Entrenamiento, validación y prueba |
| 88 | b | Semana 5 | Clase 5 – Qué partición reproduce el uso real |
| 89 | c | Semana 5 | Clase 5 – Partición aleatoria y estratificada |
| 90 | c | Semana 5 | Clase 5 – Fuga de información |
| 91 | a | Semana 5 | Clase 5 – Imputación: separar antes de calcular |
| 92 | a | Semana 5 | Clase 5 – Ejemplo: el mismo evento a ambos lados |
| 93 | c | Semana 5 | Clase 5 – Duplicados y selección de atributos |
| 94 | c | Semana 5 | Clase 5 – Baseline |
| 95 | a | Semana 5 | Clase 5 – Baselines por tipo de tarea |
| 96 | b | Semana 5 | Clase 5 – Accuracy engañosa |
| 97 | c | Semana 5 | Clase 5 – Métricas de clasificación |
| 98 | b | Semana 5 | Clase 5 – Métricas de clasificación |
| 99 | c | Semana 5 | Clase 5 – Matriz de confusión |
| 100 | b | Semana 5 | Clase 5 – Métrica, prevalencia y costo |
| 101 | b | Semana 5 | Clase 5 – Métrica, prevalencia y costo |
| 102 | b | Semana 5 | Clase 5 – Métricas de regresión |
| 103 | c | Semana 5 | Clase 5 – R² y sus límites |
| 104 | b | Semana 5 | Clase 5 – Evaluar clustering |
| 105 | b | Semana 5 | Clase 5 – Evaluar series temporales |
| 106 | b | Semana 5 | Clase 5 – Validación cruzada |
| 107 | a | Semana 5 | Clase 5 – El pipeline dentro de cada fold |
| 108 | a | Semana 5 | Clase 5 – Curvas de pérdida |
| 109 | a | Semana 5 | Clase 5 – Curvas de pérdida |
| 110 | c | Semana 5 | Clase 5 – Baseline |
| 111 | c | Semana 5 | Clase 5 – Qué partición reproduce el uso real |
| 112 | a | Semana 5 | Clase 5 – Partición por grupos |
