# Parcial 2 – Inteligencia Artificial
## Preguntas de opción múltiple – Grupos A y B

Fecha: 17/11/2026
Fuentes: presentaciones de material-para-parcial-IA-2; contexto del libro (capítulos 9, 10, 11 y 12).

Consigna: seleccione la única alternativa correcta en cada pregunta.

---

## Grupo A

**1.** En el marco de la clase, aprender consiste en:

a) almacenar los ejemplos de entrenamiento para responder con ellos.
b) ajustar, a partir de ejemplos, una función que transforma información disponible en una salida útil.
c) definir manualmente una regla condición-acción para cada caso.

**2.** En un sistema de decisión basado en Machine Learning, la regla de decisión:

a) estima una clase, un valor o un puntaje a partir de las señales.
b) registra el estado real confirmado después del horizonte.
c) convierte la salida del modelo y los costos en una acción.

**3.** El aprendizaje supervisado se caracteriza por:

a) disponer de ejemplos con entrada y respuesta conocida (x, y).
b) disponer solo de variables x, para buscar estructura en los datos.
c) aprender por interacción, a partir de acciones y recompensas.

**4.** En el caso conductor de movilidad, la unidad de análisis es:

a) el tramo, considerando todos sus registros como uno solo.
b) la flota completa de vehículos.
c) un par (tramo, instante de decisión).

**5.** Existe fuga de información cuando:

a) el modelo obtiene un error alto en el conjunto de entrenamiento.
b) el conjunto de datos contiene valores faltantes.
c) el entrenamiento o la evaluación reciben información que todavía es desconocida en el momento de la predicción real.

**6.** El conjunto de prueba se utiliza para:

a) medir una única vez el procedimiento congelado.
b) ajustar los parámetros y las transformaciones del modelo.
c) elegir variables, configuraciones y umbral.

**7.** La partición estratificada:

a) usa el pasado para entrenar y el futuro para evaluar.
b) asigna todos los registros de un mismo grupo a una sola partición.
c) conserva aproximadamente la proporción de clases en cada partición.

**8.** En la matriz de confusión del caso de bloqueo (positivo = bloqueado), un falso negativo es:

a) una falsa alarma: se predice bloqueado y el tramo estaba libre.
b) un acierto sobre un tramo libre.
c) un bloqueo omitido: se predice libre y el tramo estaba bloqueado.

**9.** En la matriz de confusión, los FP y los FN corresponden a:

a) aciertos del modelo.
b) errores del modelo.
c) la cantidad total de casos evaluados.

**10.** En cada iteración de la validación cruzada, la imputación, el escalado y la codificación se ajustan:

a) con los folds de entrenamiento de esa iteración.
b) con todos los datos, antes de crear los folds.
c) con el fold de validación de esa iteración.

**11.** El sobreajuste se reconoce por:

a) errores altos en entrenamiento y en validación.
b) error de entrenamiento bajo y error de validación peor.
c) error de validación mínimo con una brecha controlada.

**12.** Una característica útil:

a) tiene significado, está disponible al predecir y se calcula igual en entrenamiento e inferencia.
b) se calcula con datos posteriores al instante de predicción.
c) es la que presenta la mayor cantidad de valores distintos.

**13.** Codificar las zonas norte, centro y sur como 1, 2 y 3:

a) crea una geometría artificial entre categorías nominales.
b) conserva la ausencia de orden entre las categorías.
c) equivale a la codificación indicadora.

**14.** Los métodos de selección de atributos de tipo filtro:

a) comparan subconjuntos entrenando el modelo final.
b) seleccionan atributos durante el ajuste del modelo.
c) puntúan los atributos antes de ajustar el modelo final.

**15.** La diferencia entre selección de atributos y reducción dimensional es que:

a) la selección conserva columnas originales y la reducción construye nuevas coordenadas.
b) ambas conservan las columnas originales.
c) la selección construye nuevas coordenadas y la reducción conserva columnas originales.

**16.** En un proyecto de Machine Learning, la unidad evaluada es:

a) el pipeline completo.
b) el conjunto de prueba.
c) el estimador aislado.

**17.** En la validación anidada, el ciclo interno:

a) ajusta el modelo definitivo con todos los datos de desarrollo.
b) selecciona la configuración.
c) estima el desempeño del procedimiento de selección.

**18.** Seleccionar la configuración usando los resultados de la evaluación externa provoca que:

a) la estimación externa se vuelva más conservadora.
b) el ciclo interno deje de ser necesario.
c) la estimación externa se vuelva optimista.

**19.** En regresión lineal, el coeficiente βj representa:

a) el valor de referencia cuando todas las entradas valen cero.
b) el cambio asociado con una unidad de xj, manteniendo fijas las demás entradas.
c) la probabilidad de que y tome el valor 1.

**20.** Para estimar probabilidades cuando Y ∈ {0, 1}, una recta resulta inadecuada porque:

a) puede producir valores menores que 0 o mayores que 1.
b) siempre produce valores entre 0 y 1.
c) admite una sola variable de entrada.

**21.** En la regresión logística, si xj aumenta una unidad y las demás entradas quedan fijas:

a) la probabilidad aumenta βj puntos.
b) el puntaje η se multiplica por βj.
c) los odds se multiplican por e^βj.

**22.** Una salida p̂ = 0,8 de un modelo significa:

a) que el modelo acierta 80 % en cualquier población.
b) 80 % de probabilidad bajo los datos y supuestos del modelo.
c) que el evento ocurrirá con certeza.

**23.** El método de mínimos cuadrados elige los parámetros que minimizan:

a) la suma de los valores absolutos de las predicciones.
b) la suma de los residuos al cuadrado.
c) la log-loss.

**24.** En la regresión logística, la función sigmoide transforma el puntaje lineal en:

a) un valor numérico de cualquier magnitud.
b) una probabilidad entre 0 y 1.
c) un conjunto de grupos de observaciones similares.

**25.** Para estimar la demora en minutos de un trayecto se utiliza un modelo de:

a) regresión.
b) clasificación binaria.
c) agrupamiento (clustering).

---

## Grupo B

**1.** En la notación ŷ = f(x), el símbolo ŷ representa:

a) la estimación producida por la función aprendida.
b) las variables observadas antes de decidir.
c) el resultado real definido por el problema.

**2.** En un sistema de decisión basado en Machine Learning, el modelo:

a) convierte la predicción y los costos en una acción.
b) estima una clase, un valor o un puntaje a partir de las señales x.
c) observa el entorno, actúa y recibe las consecuencias de la acción.

**3.** En el aprendizaje por refuerzo, la evidencia disponible es:

a) la interacción, las acciones y las recompensas.
b) pocos ejemplos etiquetados y muchos ejemplos que solo contienen x.
c) un conjunto de pares (x, y) con respuesta conocida.

**4.** Dos registros de la misma unidad de análisis:

a) constituyen evidencia dependiente entre sí.
b) aportan evidencia independiente y duplican la información útil.
c) representan dos poblaciones distintas.

**5.** Usar la duración final de un bloqueo como variable para predecir ese bloqueo es un ejemplo de fuga:

a) de preprocesamiento.
b) por duplicados o entidad.
c) temporal.

**6.** El conjunto de validación se utiliza para:

a) medir una única vez el procedimiento congelado.
b) elegir variables, configuraciones y umbral.
c) ajustar los parámetros y las transformaciones del modelo.

**7.** La partición aleatoria corresponde cuando las unidades:

a) tienen un orden temporal relevante para el uso.
b) pertenecen a grupos con patrones propios.
c) son intercambiables e independientes.

**8.** En la matriz de confusión del caso de bloqueo (positivo = bloqueado), un falso positivo es:

a) un acierto sobre un tramo bloqueado.
b) una falsa alarma: se predice bloqueado y el tramo estaba libre.
c) un bloqueo omitido: se predice libre y el tramo estaba bloqueado.

**9.** En la matriz de confusión, los VP y los VN corresponden a:

a) aciertos del modelo.
b) falsas alarmas.
c) bloqueos omitidos.

**10.** Ajustar el preprocesamiento con todos los datos antes de crear los folds:

a) mejora la independencia de la validación.
b) filtra información entre folds.
c) garantiza la reproducibilidad del experimento.

**11.** El subajuste se reconoce por:

a) error de validación mínimo con una brecha controlada.
b) error de entrenamiento bajo y error de validación peor.
c) errores altos en entrenamiento y en validación.

**12.** En ingeniería de características, una característica o atributo es:

a) un parámetro aprendido durante el ajuste.
b) la salida que el modelo debe estimar.
c) una magnitud utilizada como entrada de un modelo.

**13.** La codificación indicadora (one-hot) de una variable categórica:

a) reemplaza cada nivel por su frecuencia.
b) crea una columna binaria por nivel.
c) asigna un número entero ordenado a cada nivel.

**14.** Los métodos de selección de atributos envolventes:

a) seleccionan atributos durante el ajuste mediante una penalización.
b) puntúan los atributos antes de ajustar el modelo final.
c) evalúan subconjuntos entrenando el modelo que finalmente se utilizará.

**15.** En PCA, los componentes principales son:

a) direcciones ortogonales ordenadas por varianza.
b) las variables originales con mayor correlación con y.
c) grupos de observaciones similares.

**16.** Forman parte del procedimiento que debe aislarse durante la evaluación:

a) únicamente los parámetros del modelo.
b) únicamente los datos del conjunto de prueba.
c) la imputación, la selección de variables, los hiperparámetros y el umbral.

**17.** En la validación anidada, el ciclo externo:

a) selecciona la configuración.
b) estima el desempeño del procedimiento de selección.
c) persiste el modelo definitivo.

**18.** Mezclar grupos o períodos entre entrenamiento y evaluación provoca que:

a) se evalúe una tarea más fácil que el uso real.
b) se evalúe una tarea más difícil que el uso real.
c) se elimine la fuga de información.

**19.** En regresión lineal, el término "lineal" se refiere a:

a) la relación causal entre las entradas y la salida.
b) los parámetros; pueden incluirse transformaciones e interacciones de las entradas.
c) las entradas, que deben usarse siempre en su escala original.

**20.** La regresión logística transforma el puntaje lineal η mediante:

a) el índice de Gini.
b) la función logaritmo.
c) la función sigmoide.

**21.** La regresión logística es lineal en:

a) el índice de Gini.
b) la probabilidad p̂.
c) los log-odds.

**22.** En la secuencia puntaje → probabilidad → clase → acción, la clase se obtiene:

a) aplicando un umbral a la probabilidad.
b) incorporando costos y restricciones operativas.
c) combinando linealmente las entradas.

**23.** En mínimos cuadrados, los errores grandes pesan más porque:

a) se elevan al cuadrado.
b) se dividen por la cantidad de observaciones.
c) se multiplican por la pendiente.

**24.** La regresión logística se utiliza para estimar:

a) grupos de observaciones similares.
b) una probabilidad entre 0 y 1.
c) un valor numérico de cualquier magnitud, como los minutos de demora.

**25.** Para estimar si la demora de un trayecto superará los 10 minutos se utiliza un modelo de:

a) clasificación binaria.
b) agrupamiento (clustering).
c) regresión.

---

## Clave de respuestas – Grupo A

| N.º | Respuesta | N.º en el banco | Fuente |
|---|---|---|---|
| 1 | b | 1 | Clase 5: ¿Qué significa aprender? / Libro 9.1.1 |
| 2 | c | 3 | Clase 5: Modelo, regla de decisión y agente |
| 3 | a | 5 | Clase 5: Aprendizaje supervisado / Libro 9.1.1 |
| 4 | c | 13 | Clase 5: Unidad y población |
| 5 | c | 17 | Clase 5: Fuga de información |
| 6 | a | 24 | Clase 5: Entrenamiento, validación y prueba / Libro 9.3.1 |
| 7 | c | 27 | Clase 5: Partición aleatoria y estratificada / Libro 9.3.2 |
| 8 | c | 35 | Clase 5: Matriz de confusión / Libro 9.4.3 |
| 9 | b | 119 | Clase 5: Matriz de confusión / Libro 9.4.3 |
| 10 | a | 45 | Clase 5: Transformaciones dentro de cada fold |
| 11 | b | 47 | Clase 5: Subajuste y sobreajuste / Libro 9.2.4 |
| 12 | a | 53 | Clase 6: La representación define qué puede aprenderse / Libro 10.1 |
| 13 | a | 57 | Clase 6: Características categóricas / Libro 10.1.4 |
| 14 | c | 63 | Clase 6: Selección de atributos / Libro 10.2.2 |
| 15 | a | 69 | Clase 6: Reducción dimensional y PCA / Libro 10.3.2 |
| 16 | a | 73 | Estructura base: El objeto evaluado es el procedimiento |
| 17 | b | 75 | Estructura base: Ciclo interno / Libro 9.3.6 |
| 18 | c | 79 | Estructura base: Errores que rompen la separación |
| 19 | b | 83 | Clase 7: Regresión lineal: hipótesis / Libro 11.1.5 |
| 20 | a | 89 | Clase 7: ¿Por qué no usar una recta para probabilidades? / Libro 11.4.1 |
| 21 | c | 93 | Clase 7: Odds y coeficientes / Libro 11.4.3 |
| 22 | b | 97 | Clase 7: Probabilidad no significa certeza / Libro 11.4.7 |
| 23 | b | 85 | Clase 7: ¿Qué significa ajustar la recta? / Libro 11.1.4 |
| 24 | b | 121 | Clase 7: Regresión logística / Libro 11.4.2 |
| 25 | a | 117 | Clase 7: Caso conductor / Regresión o clasificación / Libro 11.1.1 |

---

## Clave de respuestas – Grupo B

| N.º | Respuesta | N.º en el banco | Fuente |
|---|---|---|---|
| 1 | a | 2 | Clase 5: ¿Qué significa aprender? / Libro 9.1.6 |
| 2 | b | 4 | Clase 5: Modelo, regla de decisión y agente |
| 3 | a | 6 | Clase 5: Comparación de paradigmas |
| 4 | a | 14 | Clase 5: Unidad y población / Libro 9.3.2 |
| 5 | c | 18 | Clase 5: Tres fugas frecuentes |
| 6 | b | 23 | Clase 5: Entrenamiento, validación y prueba / Libro 9.3.1 |
| 7 | c | 28 | Clase 5: Partición aleatoria y estratificada / Libro 9.3.2 |
| 8 | b | 36 | Clase 5: Matriz de confusión / Libro 9.4.3 |
| 9 | a | 120 | Clase 5: Matriz de confusión / Libro 9.4.3 |
| 10 | b | 46 | Clase 5: Transformaciones dentro de cada fold |
| 11 | c | 48 | Clase 5: Subajuste y sobreajuste / Libro 9.2.4 |
| 12 | c | 54 | Clase 6: La representación define qué puede aprenderse / Libro 10.1.1 |
| 13 | b | 58 | Clase 6: Características categóricas / Libro 10.1.4 |
| 14 | c | 64 | Clase 6: Métodos envolventes / Libro 10.2.3 |
| 15 | a | 70 | Clase 6: Reducción dimensional y PCA / Libro 10.3.3 |
| 16 | c | 74 | Estructura base: El objeto evaluado es el procedimiento |
| 17 | b | 76 | Estructura base: Ciclo externo / Libro 9.3.6 |
| 18 | a | 80 | Estructura base: Errores que rompen la separación / Libro 9.3.4 |
| 19 | b | 84 | Clase 7: Regresión lineal: hipótesis / Libro 11.1.3 |
| 20 | c | 90 | Clase 7: Regresión logística / Libro 11.4.2 |
| 21 | c | 94 | Clase 7: Odds y coeficientes / Libro 11.4.3 |
| 22 | a | 98 | Clase 7: Puntaje, probabilidad, clase y acción |
| 23 | a | 86 | Clase 7: ¿Qué significa ajustar la recta? / Libro 11.1.4 |
| 24 | b | 122 | Clase 7: Regresión o clasificación / Regresión logística / Libro 11.4.1 |
| 25 | a | 118 | Clase 7: Caso conductor / Regresión o clasificación / Libro 11.4.1 |
