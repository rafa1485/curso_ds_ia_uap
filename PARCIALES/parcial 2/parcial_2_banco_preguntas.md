# Parcial 2 – Inteligencia Artificial
## Banco de preguntas de opción múltiple

Fecha: 17/11/2026
Fuentes: presentaciones de material-para-parcial-IA-2; contexto del libro (capítulos 9, 10, 11 y 12).

**1.** En el marco de la clase, aprender consiste en:

a) almacenar los ejemplos de entrenamiento para responder con ellos.
b) ajustar, a partir de ejemplos, una función que transforma información disponible en una salida útil.
c) definir manualmente una regla condición-acción para cada caso.

**2.** En la notación ŷ = f(x), el símbolo ŷ representa:

a) la estimación producida por la función aprendida.
b) las variables observadas antes de decidir.
c) el resultado real definido por el problema.

**3.** En un sistema de decisión basado en Machine Learning, la regla de decisión:

a) estima una clase, un valor o un puntaje a partir de las señales.
b) registra el estado real confirmado después del horizonte.
c) convierte la salida del modelo y los costos en una acción.

**4.** En un sistema de decisión basado en Machine Learning, el modelo:

a) convierte la predicción y los costos en una acción.
b) estima una clase, un valor o un puntaje a partir de las señales x.
c) observa el entorno, actúa y recibe las consecuencias de la acción.

**5.** El aprendizaje supervisado se caracteriza por:

a) disponer de ejemplos con entrada y respuesta conocida (x, y).
b) disponer solo de variables x, para buscar estructura en los datos.
c) aprender por interacción, a partir de acciones y recompensas.

**6.** En el aprendizaje por refuerzo, la evidencia disponible es:

a) la interacción, las acciones y las recompensas.
b) pocos ejemplos etiquetados y muchos ejemplos que solo contienen x.
c) un conjunto de pares (x, y) con respuesta conocida.

**7.** El aprendizaje semisupervisado resulta útil cuando:

a) el agente aprende por interacción mediante recompensas.
b) medir las señales es barato y confirmar el resultado es costoso.
c) todas las observaciones tienen una etiqueta verificada.

**8.** El aprendizaje no supervisado:

a) ajusta una función a partir de pares (x, y) con respuesta conocida.
b) busca estructura, similitudes o representaciones en datos que carecen de etiqueta objetivo.
c) aprende qué acciones acumulan mejores recompensas mediante interacción.

**9.** Estimar los minutos que tardará en resolverse un reclamo es una tarea de:

a) clasificación.
b) regresión.
c) agrupamiento (clustering).

**10.** Determinar si un tramo quedará bloqueado o libre es una tarea de:

a) clasificación.
b) regresión.
c) agrupamiento (clustering).

**11.** Según la clase, el diseño de un experimento de Machine Learning comienza por:

a) el archivo de datos disponible.
b) la decisión que debe tomar el sistema.
c) el algoritmo con mejor desempeño reportado.

**12.** Cambiar el instante de decisión t0 o el horizonte H:

a) mantiene la misma etiqueta y cambia únicamente el modelo.
b) modifica solo la presentación de los resultados.
c) cambia la tarea, la etiqueta y la utilidad operativa.

**13.** En el caso conductor de movilidad, la unidad de análisis es:

a) el tramo, considerando todos sus registros como uno solo.
b) la flota completa de vehículos.
c) un par (tramo, instante de decisión).

**14.** Dos registros de la misma unidad de análisis:

a) constituyen evidencia dependiente entre sí.
b) aportan evidencia independiente y duplican la información útil.
c) representan dos poblaciones distintas.

**15.** Una columna de la tabla histórica es válida como variable de entrada cuando:

a) tiene la mayor cantidad de valores distintos.
b) aparece registrada en la tabla histórica.
c) su valor existe en el instante de decisión t0.

**16.** Para anticipar el bloqueo de un tramo antes de ingresar, ¿qué variable puede usarse como entrada?

a) la duración total del incidente.
b) la lluvia acumulada hasta t0.
c) la velocidad medida tras ingresar al tramo.

**17.** Existe fuga de información cuando:

a) el modelo obtiene un error alto en el conjunto de entrenamiento.
b) el conjunto de datos contiene valores faltantes.
c) el entrenamiento o la evaluación reciben información que todavía es desconocida en el momento de la predicción real.

**18.** Usar la duración final de un bloqueo como variable para predecir ese bloqueo es un ejemplo de fuga:

a) de preprocesamiento.
b) por duplicados o entidad.
c) temporal.

**19.** Normalizar las variables con la media de todo el conjunto de datos, antes de separar entrenamiento y evaluación, produce:

a) fuga de información por preprocesamiento.
b) fuga temporal por usar la duración final del evento.
c) subajuste por falta de capacidad del modelo.

**20.** Que un mismo vehículo aporte registros casi idénticos a entrenamiento y a evaluación genera fuga:

a) de preprocesamiento.
b) por duplicados o entidad.
c) temporal.

**21.** Generalizar significa:

a) obtener el error mínimo en el conjunto de entrenamiento.
b) garantizar el mismo desempeño en cualquier población.
c) mantener el desempeño en unidades nuevas de la población objetivo.

**22.** Un valor de desempeño medido fuera de muestra es:

a) una medida del ajuste al conjunto de entrenamiento.
b) una garantía universal de desempeño.
c) evidencia bajo un escenario de uso definido.

**23.** El conjunto de validación se utiliza para:

a) medir una única vez el procedimiento congelado.
b) elegir variables, configuraciones y umbral.
c) ajustar los parámetros y las transformaciones del modelo.

**24.** El conjunto de prueba se utiliza para:

a) medir una única vez el procedimiento congelado.
b) ajustar los parámetros y las transformaciones del modelo.
c) elegir variables, configuraciones y umbral.

**25.** Consultar repetidamente el conjunto de prueba para tomar decisiones:

a) reduce el riesgo de fuga temporal.
b) lo convierte en un conjunto de validación.
c) mejora la estimación del desempeño futuro.

**26.** Si un cambio en el procedimiento está motivado por el resultado de la prueba:

a) alcanza con repetir la medición sobre la misma prueba.
b) se requiere una nueva prueba independiente.
c) el resultado de la prueba anterior sigue siendo válido.

**27.** La partición estratificada:

a) usa el pasado para entrenar y el futuro para evaluar.
b) asigna todos los registros de un mismo grupo a una sola partición.
c) conserva aproximadamente la proporción de clases en cada partición.

**28.** La partición aleatoria corresponde cuando las unidades:

a) tienen un orden temporal relevante para el uso.
b) pertenecen a grupos con patrones propios.
c) son intercambiables e independientes.

**29.** En una partición por grupos:

a) los registros de cada grupo se reparten entre todas las particiones.
b) se conserva la proporción de clases en cada partición.
c) todos los registros de un mismo grupo quedan en una sola partición.

**30.** En una partición temporal:

a) los registros se asignan al azar, independientemente de su fecha.
b) el pasado entrena y el futuro evalúa.
c) el futuro entrena y el pasado evalúa.

**31.** Un baseline es:

a) el modelo más complejo evaluado en el proyecto.
b) una referencia simple y reproducible, disponible con la misma información que el modelo.
c) el conjunto de datos reservado para la prueba final.

**32.** Un baseline adecuado para una tarea de regresión es:

a) el valor máximo del conjunto de prueba.
b) la clase mayoritaria del entrenamiento.
c) la media o la mediana del entrenamiento.

**33.** En un conjunto con 80 % de tramos libres, un baseline que siempre predice "libre" obtiene accuracy de 80 % y recall de 0 %. Esto muestra que:

a) el baseline es adecuado para el uso real.
b) la accuracy sola puede representar mal el objetivo de detectar bloqueos.
c) el recall pierde importancia cuando la accuracy es alta.

**34.** Si un clasificador obtiene accuracy alta en datos donde la mayoría de los tramos están libres, conviene revisar además:

a) el error en el conjunto de entrenamiento únicamente.
b) la cantidad de variables de entrada.
c) el recall, para saber qué fracción de los bloqueos reales detecta.

**35.** En la matriz de confusión del caso de bloqueo (positivo = bloqueado), un falso negativo es:

a) una falsa alarma: se predice bloqueado y el tramo estaba libre.
b) un acierto sobre un tramo libre.
c) un bloqueo omitido: se predice libre y el tramo estaba bloqueado.

**36.** En la matriz de confusión del caso de bloqueo (positivo = bloqueado), un falso positivo es:

a) un acierto sobre un tramo bloqueado.
b) una falsa alarma: se predice bloqueado y el tramo estaba libre.
c) un bloqueo omitido: se predice libre y el tramo estaba bloqueado.

**37.** La precisión mide:

a) la proporción total de aciertos sobre todos los casos.
b) de los bloqueos reales, qué fracción fue detectada.
c) de las alertas emitidas, qué fracción correspondía a bloqueos reales.

**38.** El recall mide:

a) de los bloqueos reales, qué fracción fue detectada.
b) de las alertas emitidas, qué fracción correspondía a bloqueos reales.
c) la proporción total de aciertos sobre todos los casos.

**39.** La métrica F1:

a) es el promedio aritmético de accuracy y recall.
b) incorpora los verdaderos negativos en su cálculo.
c) es la media armónica de precisión y recall.

**40.** Respecto de las métricas de regresión MAE y RMSE:

a) RMSE penaliza con mayor fuerza los errores grandes.
b) ambas se expresan en unidades al cuadrado de y.
c) MAE penaliza con mayor fuerza los errores grandes.

**41.** En el caso de bloqueo, ingresar a un tramo bloqueado (falso negativo) es más costoso que desviarse innecesariamente (falso positivo). Por eso, la métrica elegida debe:

a) hacer visible el error costoso.
b) priorizar la cantidad total de aciertos.
c) tratar ambos errores con el mismo peso.

**42.** Modificar el umbral de decisión de un clasificador:

a) cambia el equilibrio entre falsos positivos y falsos negativos.
b) modifica los parámetros aprendidos por el modelo.
c) cambia la clase positiva del problema.

**43.** En la validación cruzada K-fold:

a) todos los folds se usan a la vez para entrenar y validar.
b) el conjunto de prueba se incluye como uno de los folds.
c) cada fold actúa una vez como validación y los K−1 restantes como entrenamiento.

**44.** En la validación cruzada con datos temporales:

a) los folds se forman al azar, mezclando fechas.
b) el conjunto de prueba se reparte entre los folds.
c) se usan ventanas expansivas o deslizantes, donde el pasado entrena y el futuro valida.

**45.** En cada iteración de la validación cruzada, la imputación, el escalado y la codificación se ajustan:

a) con los folds de entrenamiento de esa iteración.
b) con todos los datos, antes de crear los folds.
c) con el fold de validación de esa iteración.

**46.** Ajustar el preprocesamiento con todos los datos antes de crear los folds:

a) mejora la independencia de la validación.
b) filtra información entre folds.
c) garantiza la reproducibilidad del experimento.

**47.** El sobreajuste se reconoce por:

a) errores altos en entrenamiento y en validación.
b) error de entrenamiento bajo y error de validación peor.
c) error de validación mínimo con una brecha controlada.

**48.** El subajuste se reconoce por:

a) error de validación mínimo con una brecha controlada.
b) error de entrenamiento bajo y error de validación peor.
c) errores altos en entrenamiento y en validación.

**49.** Para comparar dos alternativas de forma justa, deben mantenerse iguales:

a) la cantidad de hiperparámetros de cada modelo.
b) únicamente el algoritmo de aprendizaje.
c) las unidades, los folds, el período de prueba y la métrica.

**50.** Un protocolo congelado implica que:

a) código, datos, particiones, variables, configuración, umbral y métricas quedan fijados antes de abrir la prueba.
b) la prueba se repite hasta obtener el mejor resultado.
c) los hiperparámetros se ajustan después de ver la prueba.

**51.** Cualquier ranking o descarte de variables basado en datos debe:

a) realizarse con el conjunto de prueba.
b) realizarse una vez con todos los datos.
c) ajustarse dentro de cada fold.

**52.** Usar información de validación o de prueba para elegir variables produce:

a) una estimación más conservadora del desempeño.
b) una reducción del sobreajuste.
c) optimismo en la estimación del desempeño.

**53.** Una característica útil:

a) tiene significado, está disponible al predecir y se calcula igual en entrenamiento e inferencia.
b) se calcula con datos posteriores al instante de predicción.
c) es la que presenta la mayor cantidad de valores distintos.

**54.** En ingeniería de características, una característica o atributo es:

a) un parámetro aprendido durante el ajuste.
b) la salida que el modelo debe estimar.
c) una magnitud utilizada como entrada de un modelo.

**55.** Al estandarizar una variable numérica, el riesgo señalado en clase es:

a) ocultar eventos reales extremos.
b) aprender la media y la dispersión con todos los datos.
c) aplicar la transformación a valores cero o negativos.

**56.** La transformación logaritmo es útil para representar:

a) límites a los valores extremos.
b) cambios relativos.
c) categorías nominales.

**57.** Codificar las zonas norte, centro y sur como 1, 2 y 3:

a) crea una geometría artificial entre categorías nominales.
b) conserva la ausencia de orden entre las categorías.
c) equivale a la codificación indicadora.

**58.** La codificación indicadora (one-hot) de una variable categórica:

a) reemplaza cada nivel por su frecuencia.
b) crea una columna binaria por nivel.
c) asigna un número entero ordenado a cada nivel.

**59.** Si durante el uso aparece una categoría desconocida (por ejemplo, la zona "oeste"), un cuidado adecuado es:

a) representarla como "desconocida" u "otra" y registrar su frecuencia.
b) sustituirla por la categoría más frecuente.
c) asignarle el código numérico siguiente al último nivel conocido.

**60.** Representar la hora con el par seno/coseno de 2πt/P permite:

a) ordenar las horas de forma lineal de 0 a 23.
b) conservar que las 23:00 y las 00:00 son horas cercanas.
c) eliminar la periodicidad diaria.

**61.** Una interacción entre variables representa que:

a) el efecto de una variable depende del valor de otra.
b) dos variables tienen la misma escala.
c) una variable se calcula con datos futuros.

**62.** Generar todas las interacciones por pares entre muchas variables:

a) aumenta la capacidad del modelo y el riesgo de sobreajuste.
b) reduce el riesgo de sobreajuste.
c) garantiza un mejor desempeño fuera de muestra.

**63.** Los métodos de selección de atributos de tipo filtro:

a) comparan subconjuntos entrenando el modelo final.
b) seleccionan atributos durante el ajuste del modelo.
c) puntúan los atributos antes de ajustar el modelo final.

**64.** Los métodos de selección de atributos envolventes:

a) seleccionan atributos durante el ajuste mediante una penalización.
b) puntúan los atributos antes de ajustar el modelo final.
c) evalúan subconjuntos entrenando el modelo que finalmente se utilizará.

**65.** Lasso (regularización L1) se clasifica como un método de selección:

a) de filtro, porque ordena las variables por su correlación con y.
b) envolvente, porque agrega variables de a una.
c) embebido, porque produce coeficientes iguales a cero durante el ajuste.

**66.** Una limitación de los métodos de filtro univariados es que:

a) dependen de la penalización del modelo.
b) requieren entrenar el modelo final muchas veces.
c) pueden perder interacciones entre variables.

**67.** La selección hacia adelante:

a) comienza con todos los atributos y retira el menos útil.
b) comienza con un conjunto vacío y agrega el atributo que más mejora la validación.
c) selecciona atributos durante el ajuste mediante penalización L1.

**68.** La eliminación hacia atrás:

a) selecciona atributos durante el ajuste mediante penalización L1.
b) comienza con un conjunto vacío y agrega el atributo que más mejora la validación.
c) comienza con todos los atributos y retira el menos útil.

**69.** La diferencia entre selección de atributos y reducción dimensional es que:

a) la selección conserva columnas originales y la reducción construye nuevas coordenadas.
b) ambas conservan las columnas originales.
c) la selección construye nuevas coordenadas y la reducción conserva columnas originales.

**70.** En PCA, los componentes principales son:

a) direcciones ortogonales ordenadas por varianza.
b) las variables originales con mayor correlación con y.
c) grupos de observaciones similares.

**71.** Conservar 90 % de la varianza mediante PCA:

a) elimina el riesgo de sobreajuste.
b) puede perder señal predictiva ubicada en direcciones de baja varianza.
c) garantiza conservar 90 % de la capacidad predictiva.

**72.** Durante la inferencia, un pipeline ya ajustado:

a) recalcula los componentes de PCA en cada predicción.
b) vuelve a ajustar todas las transformaciones con los datos nuevos.
c) reutiliza las medias, categorías, columnas seleccionadas y componentes aprendidos.

**73.** En un proyecto de Machine Learning, la unidad evaluada es:

a) el pipeline completo.
b) el conjunto de prueba.
c) el estimador aislado.

**74.** Forman parte del procedimiento que debe aislarse durante la evaluación:

a) únicamente los parámetros del modelo.
b) únicamente los datos del conjunto de prueba.
c) la imputación, la selección de variables, los hiperparámetros y el umbral.

**75.** En la validación anidada, el ciclo interno:

a) ajusta el modelo definitivo con todos los datos de desarrollo.
b) selecciona la configuración.
c) estima el desempeño del procedimiento de selección.

**76.** En la validación anidada, el ciclo externo:

a) selecciona la configuración.
b) estima el desempeño del procedimiento de selección.
c) persiste el modelo definitivo.

**77.** Tras la evaluación externa, el modelo definitivo se obtiene:

a) tomando el modelo del primer fold externo.
b) conservando el ajuste del fold externo con mejor puntuación.
c) reajustando el pipeline elegido con todos los datos de desarrollo permitidos.

**78.** Conservar el ajuste del fold externo con mejor puntuación:

a) elimina el sesgo de selección.
b) elige por azar de esa partición.
c) produce el modelo definitivo correcto.

**79.** Seleccionar la configuración usando los resultados de la evaluación externa provoca que:

a) la estimación externa se vuelva más conservadora.
b) el ciclo interno deje de ser necesario.
c) la estimación externa se vuelva optimista.

**80.** Mezclar grupos o períodos entre entrenamiento y evaluación provoca que:

a) se evalúe una tarea más fácil que el uso real.
b) se evalúe una tarea más difícil que el uso real.
c) se elimine la fuga de información.

**81.** En la expresión f̂ = arg min₍f∈F₎ (1/n) Σ L(yᵢ, f(xᵢ)), L representa:

a) la familia de funciones que el modelo puede representar.
b) la cantidad de ejemplos de entrenamiento.
c) la penalización por una predicción incorrecta.

**82.** En la expresión f̂ = arg min₍f∈F₎ (1/n) Σ L(yᵢ, f(xᵢ)), F representa:

a) el conjunto de prueba.
b) la familia de funciones que el modelo puede representar.
c) la penalización por una predicción incorrecta.

**83.** En regresión lineal, el coeficiente βj representa:

a) el valor de referencia cuando todas las entradas valen cero.
b) el cambio asociado con una unidad de xj, manteniendo fijas las demás entradas.
c) la probabilidad de que y tome el valor 1.

**84.** En regresión lineal, el término "lineal" se refiere a:

a) la relación causal entre las entradas y la salida.
b) los parámetros; pueden incluirse transformaciones e interacciones de las entradas.
c) las entradas, que deben usarse siempre en su escala original.

**85.** El método de mínimos cuadrados elige los parámetros que minimizan:

a) la suma de los valores absolutos de las predicciones.
b) la suma de los residuos al cuadrado.
c) la log-loss.

**86.** En mínimos cuadrados, los errores grandes pesan más porque:

a) se elevan al cuadrado.
b) se dividen por la cantidad de observaciones.
c) se multiplican por la pendiente.

**87.** Un coeficiente de regresión lineal describe:

a) un efecto causal demostrado.
b) una relación válida en cualquier población o período.
c) una asociación condicionada al modelo.

**88.** Si los residuos de una regresión muestran curvatura, esto indica que:

a) la variabilidad del error es constante.
b) falta representar una relación curva entre las entradas y la salida.
c) los errores son independientes en el tiempo.

**89.** Para estimar probabilidades cuando Y ∈ {0, 1}, una recta resulta inadecuada porque:

a) puede producir valores menores que 0 o mayores que 1.
b) siempre produce valores entre 0 y 1.
c) admite una sola variable de entrada.

**90.** La regresión logística transforma el puntaje lineal η mediante:

a) el índice de Gini.
b) la función logaritmo.
c) la función sigmoide.

**91.** En la regresión logística, la probabilidad p̂ = σ(η):

a) puede tomar cualquier valor real.
b) vale 1 cuando η = 0.
c) siempre pertenece al intervalo (0, 1).

**92.** En la regresión logística, el valor de σ(0) es:

a) 1.
b) 0.
c) 0,5.

**93.** En la regresión logística, si xj aumenta una unidad y las demás entradas quedan fijas:

a) la probabilidad aumenta βj puntos.
b) el puntaje η se multiplica por βj.
c) los odds se multiplican por e^βj.

**94.** La regresión logística es lineal en:

a) el índice de Gini.
b) la probabilidad p̂.
c) los log-odds.

**95.** La regresión logística se ajusta minimizando:

a) el índice de Gini de las hojas.
b) la suma de residuos al cuadrado mediante una fórmula cerrada.
c) la log-loss.

**96.** En la log-loss, una probabilidad alta asignada a la clase equivocada:

a) recibe una penalización nula.
b) mejora el valor de la pérdida.
c) recibe una penalización grande.

**97.** Una salida p̂ = 0,8 de un modelo significa:

a) que el modelo acierta 80 % en cualquier población.
b) 80 % de probabilidad bajo los datos y supuestos del modelo.
c) que el evento ocurrirá con certeza.

**98.** En la secuencia puntaje → probabilidad → clase → acción, la clase se obtiene:

a) aplicando un umbral a la probabilidad.
b) incorporando costos y restricciones operativas.
c) combinando linealmente las entradas.

**99.** Si un falso negativo cuesta mucho más que un falso positivo, el umbral de decisión conveniente:

a) se mantiene en 0,5.
b) desciende por debajo de 0,5.
c) sube por encima de 0,5.

**100.** Según la clase, el umbral de decisión de un clasificador depende de:

a) la cantidad de variables de entrada.
b) las consecuencias de los errores, la capacidad y las restricciones.
c) únicamente el algoritmo elegido.

**101.** Una fortaleza de los modelos lineales (regresión lineal y logística) es:

a) la captura automática de interacciones.
b) la interpretación de sus coeficientes.
c) la representación automática de curvaturas.

**102.** Un límite compartido de la regresión lineal y la logística es que:

a) su frontera es lineal, y las curvaturas e interacciones deben incluirse explícitamente.
b) su cálculo es poco eficiente.
c) son inestables con pocos datos.

**103.** En un árbol de decisión, cada hoja contiene:

a) una pregunta sobre un atributo y un umbral.
b) una predicción basada en los ejemplos que llegan a ella.
c) el conjunto completo de entrenamiento.

**104.** El índice de Gini de un nodo vale 0 cuando:

a) las clases están equilibradas.
b) el nodo es puro (contiene una sola clase).
c) el nodo es la raíz del árbol.

**105.** Un árbol de decisión elige la división que:

a) más reduce la impureza respecto del nodo padre.
b) más aumenta la impureza de las hojas.
c) produce las hojas de mayor tamaño.

**106.** En un problema de dos clases, un índice de Gini igual a 0,5 indica:

a) clases equilibradas (máxima mezcla).
b) un nodo puro.
c) una hoja vacía.

**107.** Un árbol de decisión profundo puede:

a) aislar pocos ejemplos y memorizar ruido.
b) garantizar estabilidad ante pequeños cambios en los datos.
c) producir siempre probabilidades bien calibradas.

**108.** La complejidad de un árbol de decisión se regula mediante:

a) la función sigmoide.
b) la tasa de aprendizaje ν.
c) la profundidad, el tamaño mínimo de hoja y la poda.

**109.** El bagging construye árboles sobre remuestras con el objetivo principal de:

a) aumentar la profundidad de cada árbol.
b) corregir secuencialmente el error.
c) reducir la varianza.

**110.** Random Forest se diferencia de bagging porque:

a) entrena los árboles en forma secuencial.
b) además de usar remuestras, considera solo algunos atributos en cada división.
c) utiliza un único árbol profundo.

**111.** En boosting:

a) se ajusta un único árbol de profundidad máxima.
b) los árboles votan en forma independiente.
c) cada árbol nuevo intenta corregir parte del error actual.

**112.** En boosting, el parámetro ν representa:

a) la cantidad de atributos considerados en cada división.
b) la tasa de aprendizaje.
c) el índice de impureza del nodo.

**113.** Según la clase, ¿qué problema persiste aunque se agreguen más modelos a un ensamble?

a) la varianza de un único árbol.
b) las etiquetas incorrectas.
c) la inestabilidad de un árbol aislado.

**114.** Para datos tabulares con prioridad predictiva, la clase sugiere como punto de partida:

a) Random Forest o boosting.
b) regresión lineal simple.
c) agrupamiento (clustering).

**115.** En la comparación de familias de modelos, la extrapolación de árboles y ensambles es:

a) posible, con riesgo.
b) pobre.
c) superior a la de los modelos lineales.

**116.** En la comparación de familias de modelos, la estabilidad generalmente baja corresponde a:

a) la regresión lineal.
b) el ensamble de árboles.
c) el árbol de decisión individual.

**117.** Para estimar la demora en minutos de un trayecto se utiliza un modelo de:

a) regresión.
b) clasificación binaria.
c) agrupamiento (clustering).

**118.** Para estimar si la demora de un trayecto superará los 10 minutos se utiliza un modelo de:

a) clasificación binaria.
b) agrupamiento (clustering).
c) regresión.

**119.** En la matriz de confusión, los FP y los FN corresponden a:

a) aciertos del modelo.
b) errores del modelo.
c) la cantidad total de casos evaluados.

**120.** En la matriz de confusión, los VP y los VN corresponden a:

a) aciertos del modelo.
b) falsas alarmas.
c) bloqueos omitidos.

**121.** En la regresión logística, la función sigmoide transforma el puntaje lineal en:

a) un valor numérico de cualquier magnitud.
b) una probabilidad entre 0 y 1.
c) un conjunto de grupos de observaciones similares.

**122.** La regresión logística se utiliza para estimar:

a) grupos de observaciones similares.
b) una probabilidad entre 0 y 1.
c) un valor numérico de cualquier magnitud, como los minutos de demora.

---

## Clave de respuestas – Banco

| N.º | Respuesta | Par temático (uso interno) | Fuente |
|---|---|---|---|
| 1 | b | 1A | Clase 5: ¿Qué significa aprender? / Libro 9.1.1 |
| 2 | a | 1B | Clase 5: ¿Qué significa aprender? / Libro 9.1.6 |
| 3 | c | 2A | Clase 5: Modelo, regla de decisión y agente |
| 4 | b | 2B | Clase 5: Modelo, regla de decisión y agente |
| 5 | a | 3A | Clase 5: Aprendizaje supervisado / Libro 9.1.1 |
| 6 | a | 3B | Clase 5: Comparación de paradigmas |
| 7 | b | 4A | Clase 5: Aprendizaje semisupervisado / Libro 9.1.3 |
| 8 | b | 4B | Clase 5: Aprendizaje no supervisado / Libro 9.1.2 |
| 9 | b | 5A | Clase 5: Clasificación y regresión / Libro 9.1.5 |
| 10 | a | 5B | Clase 5: Clasificación y regresión / Libro 9.1.5 |
| 11 | b | 6A | Clase 5: Partir de la decisión |
| 12 | c | 6B | Clase 5: Instante y horizonte |
| 13 | c | 7A | Clase 5: Unidad y población |
| 14 | a | 7B | Clase 5: Unidad y población / Libro 9.3.2 |
| 15 | c | 8A | Clase 5: Variables disponibles al decidir |
| 16 | b | 8B | Clase 5: Variables disponibles al decidir |
| 17 | c | 9A | Clase 5: Fuga de información |
| 18 | c | 9B | Clase 5: Tres fugas frecuentes |
| 19 | a | 10A | Clase 5: Tres fugas frecuentes |
| 20 | b | 10B | Clase 5: Tres fugas frecuentes |
| 21 | c | 11A | Clase 5: Generalización / Libro 9.2.3 |
| 22 | c | 11B | Clase 5: Generalización |
| 23 | b | 12B | Clase 5: Entrenamiento, validación y prueba / Libro 9.3.1 |
| 24 | a | 12A | Clase 5: Entrenamiento, validación y prueba / Libro 9.3.1 |
| 25 | b | 13A | Clase 5: Entrenamiento, validación y prueba |
| 26 | b | 13B | Clase 5: Entrenamiento, validación y prueba |
| 27 | c | 14A | Clase 5: Partición aleatoria y estratificada / Libro 9.3.2 |
| 28 | c | 14B | Clase 5: Partición aleatoria y estratificada / Libro 9.3.2 |
| 29 | c | 15A | Clase 5: Partición por grupos / Libro 9.3.4 |
| 30 | b | 15B | Clase 5: Partición temporal / Libro 9.3.5 |
| 31 | b | 16A | Clase 5: Baseline / Libro 9.2.7 |
| 32 | c | 16B | Clase 5: Baseline / Libro 9.2.7 |
| 33 | b | 17A | Clase 5: Baseline de clasificación: accuracy engañosa |
| 34 | c | 17B | Clase 5: Baseline de clasificación: accuracy engañosa / Libro 9.4.8 |
| 35 | c | 18A | Clase 5: Matriz de confusión / Libro 9.4.3 |
| 36 | b | 18B | Clase 5: Matriz de confusión / Libro 9.4.3 |
| 37 | c | 19A | Clase 5: Accuracy, precisión, recall y F1 / Libro 9.4.4 |
| 38 | a | 19B | Clase 5: Accuracy, precisión, recall y F1 / Libro 9.4.4 |
| 39 | c | 20A | Clase 5: Accuracy, precisión, recall y F1 / Libro 9.4.5 |
| 40 | a | 20B | Clase 5: MAE y RMSE / Libro 9.4.1 |
| 41 | a | 21A | Clase 5: Métrica y costo / Libro 9.4.8 |
| 42 | a | 21B | Clase 5: Métrica y costo / Libro 9.4.8 |
| 43 | c | 22A | Clase 5: Validación cruzada K-fold / Libro 9.3.3 |
| 44 | c | 22B | Clase 5: Validación cruzada K-fold / Libro 9.3.5 |
| 45 | a | 23A | Clase 5: Transformaciones dentro de cada fold |
| 46 | b | 23B | Clase 5: Transformaciones dentro de cada fold |
| 47 | b | 24A | Clase 5: Subajuste y sobreajuste / Libro 9.2.4 |
| 48 | c | 24B | Clase 5: Subajuste y sobreajuste / Libro 9.2.4 |
| 49 | c | 25A | Clase 5: Comparación justa y protocolo congelado / Libro 9.3.7 |
| 50 | a | 25B | Clase 5: Comparación justa y protocolo congelado / Libro 9.3.7 |
| 51 | c | 26A | Clase 5: Selección de características / Libro 10.2.7 |
| 52 | c | 26B | Clase 5: Selección de características / Libro 10.2.7 |
| 53 | a | 27A | Clase 6: La representación define qué puede aprenderse / Libro 10.1 |
| 54 | c | 27B | Clase 6: La representación define qué puede aprenderse / Libro 10.1.1 |
| 55 | b | 28A | Clase 6: Características numéricas / Libro 10.1.2 |
| 56 | b | 28B | Clase 6: Características numéricas / Libro 10.1.2 |
| 57 | a | 29A | Clase 6: Características categóricas / Libro 10.1.4 |
| 58 | b | 29B | Clase 6: Características categóricas / Libro 10.1.4 |
| 59 | a | 30A | Clase 6: Categoría desconocida: ejemplo y cuidados |
| 60 | b | 30B | Clase 6: Tiempo y espacio / Libro 10.1.5 |
| 61 | a | 31A | Clase 6: Interacciones y conocimiento del dominio / Libro 10.1.3 |
| 62 | a | 31B | Clase 6: Interacciones y conocimiento del dominio / Libro 10.1.3 |
| 63 | c | 32A | Clase 6: Selección de atributos / Libro 10.2.2 |
| 64 | c | 32B | Clase 6: Métodos envolventes / Libro 10.2.3 |
| 65 | c | 33A | Clase 6: Métodos embebidos / Libro 10.2.4 |
| 66 | c | 33B | Clase 6: Métodos de filtro / Libro 10.2.2 |
| 67 | b | 34A | Clase 6: Métodos envolventes / Libro 10.2.3 |
| 68 | c | 34B | Clase 6: Métodos envolventes / Libro 10.2.3 |
| 69 | a | 35A | Clase 6: Reducción dimensional y PCA / Libro 10.3.2 |
| 70 | a | 35B | Clase 6: Reducción dimensional y PCA / Libro 10.3.3 |
| 71 | b | 36A | Clase 6: Reducción dimensional y PCA / Libro 10.3.4 |
| 72 | c | 36B | Clase 6: El pipeline completo es la unidad evaluada / Libro 10.4.6 |
| 73 | a | 37A | Estructura base: El objeto evaluado es el procedimiento |
| 74 | c | 37B | Estructura base: El objeto evaluado es el procedimiento |
| 75 | b | 38A | Estructura base: Ciclo interno / Libro 9.3.6 |
| 76 | b | 38B | Estructura base: Ciclo externo / Libro 9.3.6 |
| 77 | c | 39A | Estructura base: Modelo definitivo y prueba opcional |
| 78 | b | 39B | Estructura base: Errores que rompen la separación |
| 79 | c | 40A | Estructura base: Errores que rompen la separación |
| 80 | a | 40B | Estructura base: Errores que rompen la separación / Libro 9.3.4 |
| 81 | c | 41A | Clase 7: Aprendizaje supervisado / Libro 9.2.1 |
| 82 | b | 41B | Clase 7: Aprendizaje supervisado / Libro 9.2.2 |
| 83 | b | 42A | Clase 7: Regresión lineal: hipótesis / Libro 11.1.5 |
| 84 | b | 42B | Clase 7: Regresión lineal: hipótesis / Libro 11.1.3 |
| 85 | b | 43A | Clase 7: ¿Qué significa ajustar la recta? / Libro 11.1.4 |
| 86 | a | 43B | Clase 7: ¿Qué significa ajustar la recta? / Libro 11.1.4 |
| 87 | c | 44A | Clase 7: Interpretar sin exagerar / Libro 11.1.5 |
| 88 | b | 44B | Clase 7: Residuos / Libro 11.2.7 |
| 89 | a | 45A | Clase 7: ¿Por qué no usar una recta para probabilidades? / Libro 11.4.1 |
| 90 | c | 45B | Clase 7: Regresión logística / Libro 11.4.2 |
| 91 | c | 46A | Clase 7: Regresión logística / Libro 11.4.2 |
| 92 | c | 46B | Clase 7: Regresión logística / Libro 11.4.2 |
| 93 | c | 47A | Clase 7: Odds y coeficientes / Libro 11.4.3 |
| 94 | c | 47B | Clase 7: Odds y coeficientes / Libro 11.4.3 |
| 95 | c | 48A | Clase 7: ¿Cómo se ajusta la logística? / Libro 11.4.4 |
| 96 | c | 48B | Clase 7: ¿Cómo se ajusta la logística? / Libro 11.4.4 |
| 97 | b | 49A | Clase 7: Probabilidad no significa certeza / Libro 11.4.7 |
| 98 | a | 49B | Clase 7: Puntaje, probabilidad, clase y acción |
| 99 | b | 50A | Clase 7: De probabilidad a acción / Libro 11.4.5 |
| 100 | b | 50B | Clase 7: De probabilidad a acción / Libro 11.4.5 |
| 101 | b | 51A | Clase 7: Límite compartido de los modelos lineales |
| 102 | a | 51B | Clase 7: Límite compartido de los modelos lineales |
| 103 | b | 52A | Clase 7: Árbol de decisión / Libro 12.1.1 |
| 104 | b | 52B | Clase 7: ¿Cómo elige una división? / Libro 12.1.3 |
| 105 | a | 53A | Clase 7: ¿Cómo elige una división? / Libro 12.1.3 |
| 106 | a | 53B | Clase 7: ¿Cómo elige una división? / Libro 12.1.3 |
| 107 | a | 54A | Clase 7: Capacidad e inestabilidad del árbol / Libro 12.1.5 |
| 108 | c | 54B | Clase 7: Capacidad e inestabilidad del árbol / Libro 12.1.5-12.1.6 |
| 109 | c | 55A | Clase 7: Por qué combinar árboles / Libro 12.3.2 |
| 110 | b | 55B | Clase 7: Random Forest / Libro 12.3.3 |
| 111 | c | 56A | Clase 7: Boosting / Libro 12.3.4 |
| 112 | b | 56B | Clase 7: Boosting / Libro 12.3.5 |
| 113 | b | 57A | Clase 7: Por qué combinar árboles / Libro 12.3.3 |
| 114 | a | 57B | Clase 7: Cómo elegir un punto de partida |
| 115 | b | 58A | Clase 7: Comparación de familias |
| 116 | c | 58B | Clase 7: Comparación de familias |
| 117 | a | 59A | Clase 7: Caso conductor / Regresión o clasificación / Libro 11.1.1 |
| 118 | a | 59B | Clase 7: Caso conductor / Regresión o clasificación / Libro 11.4.1 |
| 119 | b | 60A | Clase 5: Matriz de confusión / Libro 9.4.3 |
| 120 | a | 60B | Clase 5: Matriz de confusión / Libro 9.4.3 |
| 121 | b | 61A | Clase 7: Regresión logística / Libro 11.4.2 |
| 122 | b | 61B | Clase 7: Regresión o clasificación / Regresión logística / Libro 11.4.1 |
