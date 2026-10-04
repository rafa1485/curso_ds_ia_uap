# Guía de ejercicios: diseño experimental de Machine Learning

## Formulación, evaluación y comparación confiable de modelos

**Alcance:** clasificación, regresión y clustering.  
**Fuera de alcance en esta guía:** series temporales, pronóstico y particiones temporales.  
**Conjunto de datos común:** Palmer Penguins.  
**Entorno de trabajo:** Jupyter Notebook con Python.  
**Modalidad sugerida:** resolución individual, discusión en pequeños grupos y entrega individual verificable.

---

## 1. Propósitos de aprendizaje

Al completar la guía, el estudiante deberá ser capaz de:

1. Distinguir paradigma, tarea, algoritmo, modelo, predicción y decisión.
2. Formular problemas de clasificación, regresión y clustering a partir de un mismo dominio.
3. Definir unidad de análisis, población objetivo, muestra, variables predictoras y resultado esperado.
4. Elegir una partición que represente el modo en que el modelo será utilizado.
5. Separar correctamente entrenamiento, validación y prueba.
6. Reconocer fugas de información producidas por variables, entidades, duplicados o transformaciones.
7. Construir baselines pertinentes para cada tarea.
8. Seleccionar métricas compatibles con el objetivo y los costos de error.
9. Aplicar validación cruzada sin contaminar la evaluación.
10. Comparar modelos en condiciones justas y reconocer subajuste y sobreajuste.
11. Documentar un protocolo experimental reproducible y auditable.

---

## 2. Datos y entorno de trabajo

### 2.1. Conjunto Palmer Penguins

El conjunto contiene observaciones de 344 pingüinos pertenecientes a tres especies y registrados en tres islas del archipiélago Palmer, en la Antártida.

**Descarga directa en CSV:**  
<https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv>

**Documentación:**  
<https://allisonhorst.github.io/palmerpenguins/>

**Licencia:** CC0.

| Variable | Tipo | Descripción |
|---|---|---|
| `species` | Categórica | Especie: Adelie, Chinstrap o Gentoo |
| `island` | Categórica | Isla de observación |
| `bill_length_mm` | Numérica | Longitud del pico en milímetros |
| `bill_depth_mm` | Numérica | Profundidad del pico en milímetros |
| `flipper_length_mm` | Numérica | Longitud de la aleta en milímetros |
| `body_mass_g` | Numérica | Masa corporal en gramos |
| `sex` | Categórica | Sexo registrado |
| `year` | Categórica u ordinal | Año de observación |

### 2.2. Entorno de trabajo obligatorio

Todos los ejercicios se resolverán en notebooks de Jupyter con Python.

Bibliotecas principales:

- `pandas` para carga, inspección y transformación de datos;
- `numpy` para operaciones numéricas;
- `matplotlib` y `seaborn` para visualización;
- `scikit-learn` para particiones, pipelines, modelos, validación y métricas.

Cuando el entorno no tenga instaladas las dependencias, puede utilizarse una celda inicial como:

```python
%pip install pandas numpy matplotlib seaborn scikit-learn
```

La instalación no debe repetirse en cada ejecución. Una vez preparado el entorno, la celda puede conservarse comentada o marcarse como configuración inicial.

### 2.3. Estructura estándar del notebook

Cada archivo `.ipynb` deberá organizarse mediante celdas Markdown y celdas de código en este orden:

1. **Título y metadatos:** estudiante, fecha, ejercicio y versión.
2. **Propósito:** pregunta que se responderá y evidencia que se producirá.
3. **Entorno:** importaciones, versiones y semilla.
4. **Carga de datos:** fuente, fecha de descarga y verificación básica.
5. **Formulación experimental:** unidad, población, variables, objetivo y partición.
6. **Desarrollo:** código dividido en pasos breves y explicados.
7. **Resultados:** tablas y visualizaciones con títulos, ejes y unidades.
8. **Interpretación:** explicación en celdas Markdown; no alcanza con mostrar la salida del código.
9. **Conclusiones y limitaciones:** respuesta a la consigna y alcance de la evidencia.
10. **Reproducibilidad:** decisiones, parámetros y archivos necesarios para repetir el análisis.

Convención sugerida para los bloques iniciales:

```python
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

RANDOM_STATE = 42
DATA_URL = (
    "https://raw.githubusercontent.com/allisonhorst/"
    "palmerpenguins/master/inst/extdata/penguins.csv"
)
```

### 2.4. Reglas experimentales comunes

Estas reglas se aplican a todos los ejercicios:

1. Fijar y registrar una semilla aleatoria.
2. Conservar una copia inalterada de los datos originales.
3. No eliminar observaciones ni imputar faltantes antes de definir la partición.
4. Mantener el conjunto de prueba fuera de toda selección de variables, modelos e hiperparámetros.
5. Ajustar imputación, codificación y escalado solamente con los datos de entrenamiento de cada iteración.
6. Informar decisiones, no solamente resultados numéricos.
7. Diferenciar claramente resultados de entrenamiento, validación y prueba.
8. Utilizar `Pipeline` y `ColumnTransformer` de `scikit-learn` cuando existan transformaciones aprendidas de los datos.
9. Evitar variables globales ocultas y ejecuciones fuera de orden.
10. Antes de entregar, reiniciar el kernel y ejecutar todas las celdas desde el comienzo.
11. El notebook debe finalizar sin errores y conservar las salidas necesarias para revisar los resultados.

### 2.5. Producto de entrega

Cada estudiante deberá entregar:

- Un archivo `.ipynb` ejecutable y comentado.
- El informe breve integrado en las celdas Markdown del notebook.
- Una ficha final de protocolo experimental.
- Las tablas y figuras solicitadas con títulos, unidades y explicación.
- Una declaración de qué decisiones se tomaron antes y después de observar resultados.
- El archivo debe abrirse con Jupyter Notebook o JupyterLab y ejecutarse de principio a fin con **Restart Kernel and Run All**.


---

# Bloque A. Formulación del problema

## Ejercicio 1. Paradigma, tarea, algoritmo, predicción y decisión

### Objetivo

Distinguir los niveles que intervienen en un sistema de Machine Learning.

### Consignas

Para cada situación, completar la tabla solicitada:

1. Estimar la especie de un pingüino a partir de sus medidas corporales.
2. Estimar la masa corporal de un pingüino.
3. Formar grupos de pingüinos con perfiles morfológicos semejantes.
4. Usar una pequeña cantidad de especies verificadas y muchas observaciones sin especie confirmada.

| Situación | Paradigma | Tarea | Salida esperada | Algoritmos posibles | Decisión apoyada |
|---|---|---|---|---|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| 4 |  |  |  |  |  |

Luego responder:

1. ¿Por qué elegir un árbol no define por sí solo el problema experimental?
2. ¿En qué se diferencian una predicción y una decisión?
3. ¿Puede un mismo algoritmo resolver más de una tarea? Proponer un ejemplo.
4. ¿Puede una misma tarea resolverse con distintos algoritmos? Proponer dos alternativas.
5. ¿Por qué codificar las especies como 0, 1 y 2 no convierte la clasificación en una regresión?

### Evidencia requerida

- Tabla completa.
- Respuestas justificadas en un máximo de 300 palabras.

---

## Ejercicio 2. Tres formulaciones sobre el mismo conjunto de datos

### Objetivo

Comprobar que un dominio no determina una única tarea.

### Consignas

Formular los siguientes problemas usando Palmer Penguins:

1. **Clasificación:** predecir `species`.
2. **Regresión:** predecir `body_mass_g`.
3. **Clustering:** descubrir perfiles morfológicos sin utilizar `species` durante el agrupamiento.

Completar una única tabla comparativa. Cada columna deberá contener la definición propuesta para el tipo de problema correspondiente:

| Elemento | Definición propuesta: clasificación | Definición propuesta: regresión | Definición propuesta: clustering |
|---|---|---|---|
| Uso o decisión que se desea apoyar |  |  |  |
| Unidad de análisis |  |  |  |
| Variables de entrada candidatas |  |  |  |
| Variable objetivo, si corresponde |  |  |  |
| Salida producida por el modelo |  |  |  |
| Error o fracaso relevante |  |  |  |

### Preguntas de análisis

1. ¿Qué cambia entre las tres formulaciones aunque las filas sean las mismas?
2. ¿Qué variable debe ocultarse durante el clustering? ¿Para qué podría utilizarse después?
3. En regresión, ¿por qué `body_mass_g` no puede permanecer entre los predictores?
4. ¿Qué limitaciones de alcance tendrían las conclusiones obtenidas con estos datos?

### Evidencia requerida

- Una tabla comparativa completa con las tres definiciones propuestas.
- Un párrafo que compare sus diferencias experimentales.

---

# Bloque B. Auditoría y partición de los datos

## Ejercicio 3. Auditoría inicial y disponibilidad de variables

### Objetivo

Examinar la calidad de los datos sin utilizar todavía información reservada para evaluar modelos.

### Consignas

1. Descargar el CSV y verificar dimensiones, nombres y tipos de variables.
2. Completar el siguiente diccionario de datos. Los nombres de las variables ya están precargados; el estudiante deberá completar las restantes columnas mediante la documentación, la inspección del archivo y el análisis con Python.

| Variable | Descripción | Tipo conceptual | Tipo en `pandas` | Unidad o categorías | Cantidad de faltantes | Valores o rango observados | Rol posible | Tratamiento, controles y riesgos |
|---|---|---|---|---|---:|---|---|---|
| `species` |  |  |  |  |  |  |  |  |
| `island` |  |  |  |  |  |  |  |  |
| `bill_length_mm` |  |  |  |  |  |  |  |  |
| `bill_depth_mm` |  |  |  |  |  |  |  |  |
| `flipper_length_mm` |  |  |  |  |  |  |  |  |
| `body_mass_g` |  |  |  |  |  |  |  |  |
| `sex` |  |  |  |  |  |  |  |  |
| `year` |  |  |  |  |  |  |  |  |

Para completar la tabla se deberá indicar:

- **Descripción:** significado de la variable.
- **Tipo conceptual:** numérica continua, numérica discreta, categórica nominal o categórica ordinal.
- **Tipo en `pandas`:** tipo detectado al cargar el CSV, por ejemplo `object`, `float64` o `int64`.
- **Unidad o categorías:** unidad de medición o conjunto de categorías observadas.
- **Cantidad de faltantes:** número de valores ausentes calculado desde el `DataFrame`.
- **Valores o rango observados:** categorías presentes o valores mínimo y máximo.
- **Rol posible:** predictor, variable objetivo, variable contextual o variable excluida, según la tarea.
- **Tratamiento, controles y riesgos:** imputación, codificación, escalado, controles de calidad y posibles fugas o atajos.

3. Contar faltantes por variable.
4. Buscar filas exactamente duplicadas.
5. Buscar posibles duplicados lógicos usando combinaciones de variables.
6. Describir la distribución de `species`, `island` y `sex`.
7. Obtener resúmenes de las cuatro medidas corporales.
8. Identificar unidades y valores físicamente improbables, sin eliminarlos automáticamente.

### Preguntas de análisis

1. ¿Qué tratamiento requieren los faltantes antes de entrenar?
2. ¿Por qué no debe calcularse todavía una media global para imputarlos?
3. ¿`island` podría actuar como atajo para predecir `species`? Investigar la relación mediante una tabla cruzada.
4. ¿El año debería tratarse como número continuo o categoría? Justificar según el uso propuesto.

### Evidencia requerida

- Diccionario de datos completo según la tabla proporcionada.
- Tabla de calidad.
- Tabla cruzada `island` por `species`.
- Lista razonada de variables candidatas y variables que requieren cautela.

---

## Ejercicio 4. Entrenamiento, validación y prueba

### Objetivo

Asignar a cada partición un único papel experimental.

### Consignas

Para la clasificación de `species`:

1. Reservar el 20 % de las observaciones como prueba final mediante una partición estratificada.
2. Conservar el 80 % restante como conjunto de desarrollo.
3. Dentro del conjunto de desarrollo, establecer cómo se realizará la validación.
4. Verificar y comparar la proporción de especies en:
   - datos completos;
   - desarrollo;
   - prueba.
5. Registrar los índices o identificadores de cada partición para poder reconstruirla.
6. Crear una tabla de usos permitidos y prohibidos:

| Partición | Usos permitidos | Usos prohibidos |
|---|---|---|
| Entrenamiento |  |  |
| Validación |  |  |
| Prueba |  |  |

### Preguntas de análisis

1. ¿Por qué la estratificación es apropiada para este objetivo?
2. ¿Qué ocurriría si una clase poco frecuente quedara casi ausente de validación?
3. ¿Por qué consultar la prueba después de cada modificación invalida su papel?
4. ¿Los porcentajes elegidos constituyen una regla universal? ¿Qué otros factores deberían considerarse?

### Evidencia requerida

- Código reproducible de la partición.
- Tabla con cantidades y proporciones.
- Tabla de usos permitidos y prohibidos.

---

# Bloque C. Fuga de información y pipelines

## Ejercicio 5. Detectives de fuga de información

### Objetivo

Identificar procedimientos que producen evaluaciones demasiado optimistas.

### Consignas

Clasificar cada situación como correcta o contaminada y explicar el motivo:

1. Imputar faltantes con la media de todas las filas y luego separar entrenamiento y prueba.
2. Separar primero y ajustar el imputador únicamente con entrenamiento.
3. Estandarizar las cuatro variables corporales usando todos los datos antes de validación cruzada.
4. Elegir las dos variables con mayor correlación con el objetivo usando entrenamiento y prueba juntos.
5. Probar veinte configuraciones y seleccionar la que logra mayor accuracy en prueba.
6. Mantener fotografías del mismo pingüino en una única partición.
7. Incluir una variable creada después de confirmar la especie.
8. Eliminar duplicados después de repartir sus copias entre entrenamiento y prueba.
9. Ajustar el escalador dentro de cada fold de validación cruzada.
10. Usar `island` sin analizar que puede actuar como atajo para `species`.

Para los casos contaminados:

- identificar qué información cruza la frontera;
- explicar por qué no estaría disponible en el uso real;
- proponer una corrección.

### Evidencia requerida

- Tabla con diagnóstico, explicación y corrección de los diez casos.

---

## Ejercicio 6. Imputación y escalado: procedimiento incorrecto y procedimiento válido

### Objetivo

Demostrar que las transformaciones también aprenden de los datos.

### Consignas

Utilizar como predictores:

- `bill_length_mm`;
- `bill_depth_mm`;
- `flipper_length_mm`;
- `body_mass_g`.

Utilizar `species` como variable objetivo. Para clasificar las tres especies se puede emplear una regresión logística multiclase. El objetivo del ejercicio no es optimizar el clasificador, sino observar dónde se ajustan la imputación y el escalado.

Importar como mínimo los siguientes módulos:

```python
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
```

Usar los mismos folds y la misma configuración de `LogisticRegression` en ambos diseños para que la comparación sea justa.

Realizar dos diseños:

**Diseño A, contaminado para fines de diagnóstico**

1. Imputar y escalar usando todos los datos.
2. Aplicar después validación cruzada.

**Diseño B, válido**

1. Construir un pipeline con imputación y escalado.
2. Ajustar esas transformaciones dentro de cada fold.
3. Aplicar exactamente los parámetros aprendidos al fold reservado.

Comparar ambos resultados, aunque la diferencia sea pequeña.

### Preguntas de análisis

1. ¿Por qué el Diseño A está conceptualmente invalidado aunque produzca una métrica similar?
2. ¿Qué parámetros aprende el imputador?
3. ¿Qué parámetros aprende el escalador?
4. ¿Qué objeto se evalúa realmente: el algoritmo final o el procedimiento completo?

### Evidencia requerida

- Diagrama o lista de pasos de ambos diseños.
- Código de un pipeline reproducible.
- Comparación y explicación conceptual.

---

# Bloque D. Baselines y métricas

## Ejercicio 7. Baselines pertinentes

### Objetivo

Establecer referencias mínimas antes de comparar modelos complejos.

### Consignas

Construir los siguientes baselines usando solo información de entrenamiento:

1. **Clasificación:** predecir siempre la especie mayoritaria.
2. **Clasificación probabilística:** utilizar las frecuencias de especies observadas en entrenamiento.
3. **Regresión:** predecir siempre la media de `body_mass_g`.
4. **Regresión robusta:** predecir siempre la mediana de `body_mass_g`.
5. **Clustering:** considerar una partición trivial de un único grupo como referencia conceptual y evaluar si soluciones con más grupos aportan estructura estable e interpretable.

Evaluar cada baseline sobre los mismos casos que se utilizarán para evaluar los modelos correspondientes.

### Preguntas de análisis

1. ¿Por qué el baseline debe usar la misma información disponible que el modelo?
2. ¿Por qué superar una referencia deliberadamente débil no demuestra utilidad?
3. ¿Qué regla humana sencilla podría utilizarse como baseline operativo para estimar la masa de un pingüino?
4. ¿Por qué un único grupo no puede evaluarse con silhouette de la misma manera que dos o más grupos?

### Evidencia requerida

- Tabla de baselines, reglas y métricas.
- Justificación de cuál será la referencia principal para cada tarea.

---

## Ejercicio 8. Matriz de confusión y métricas de clasificación

### Objetivo

Interpretar accuracy, precisión, recall y F1 según el error relevante.

### Parte A. Cálculo manual

En un problema binario se obtuvieron:

- VP = 16
- FP = 8
- FN = 4
- VN = 72

Calcular, mostrando las operaciones:

1. Accuracy.
2. Precisión.
3. Recall.
4. F1.
5. Proporción real de positivos.

Luego interpretar cada resultado en una oración.

### Parte B. Accuracy engañosa

En 100 casos existen 20 positivos y 80 negativos. Un sistema siempre predice la clase negativa.

1. Construir la matriz de confusión.
2. Calcular accuracy y recall.
3. Explicar por qué una accuracy del 80 % puede ser inútil.
4. Proponer una situación donde los falsos negativos sean más costosos.
5. Proponer otra donde los falsos positivos sean más costosos.

### Parte C. Clasificación multiclase con Palmer Penguins

1. Ajustar un modelo sencillo de clasificación.
2. Obtener la matriz de confusión de validación.
3. Calcular accuracy, precisión, recall y F1 por especie.
4. Calcular un promedio macro para evitar que la clase más numerosa domine la interpretación.
5. Identificar qué par de especies se confunde con mayor frecuencia.
6. Comparar contra el baseline de clase mayoritaria.

### Evidencia requerida

- Cálculos manuales.
- Matriz de confusión correctamente rotulada.
- Tabla de métricas por clase.
- Interpretación vinculada con tipos de error.

---

## Ejercicio 9. Métricas de regresión

### Objetivo

Comparar MAE, RMSE y R cuadrado fuera de muestra.

### Parte A. Cálculo manual

Valores reales: `[10, 12, 18, 20]`  
Predicciones: `[11, 10, 17, 26]`

1. Calcular los errores con signo.
2. Calcular los errores absolutos.
3. Calcular los errores cuadrados.
4. Obtener MAE y RMSE.
5. Explicar por qué RMSE aumenta más ante el error de 6 unidades.

### Parte B. Predicción de masa corporal

Predecir `body_mass_g` a partir de:

- `bill_length_mm`;
- `bill_depth_mm`;
- `flipper_length_mm`.

Realizar lo siguiente:

1. Evaluar los baselines de media y mediana.
2. Ajustar una regresión lineal mediante un pipeline.
3. Medir MAE, RMSE y R cuadrado en validación.
4. Comparar las métricas con las de los baselines.
5. Expresar MAE y RMSE en gramos.
6. Interpretar qué significa un R cuadrado negativo si apareciera fuera de muestra.
7. Decidir qué métrica sería principal si los errores grandes fueran especialmente costosos.

### Extensión

Incorporar `species` como predictor mediante codificación ajustada dentro del pipeline y comparar. Explicar qué pregunta distinta responde el nuevo modelo.

### Evidencia requerida

- Cálculos manuales.
- Tabla comparativa de modelos y baselines.
- Interpretación en unidades del problema.

---

## Ejercicio 10. Evaluación de clustering

### Objetivo

Evaluar grupos sin confundir calidad geométrica con utilidad sustantiva.

### Consignas

Usar únicamente las cuatro variables morfológicas:

- `bill_length_mm`;
- `bill_depth_mm`;
- `flipper_length_mm`;
- `body_mass_g`.

No utilizar `species`, `island` ni `sex` para construir los clusters.

1. Imputar faltantes y estandarizar las variables.
2. Aplicar K-means para valores de K entre 2 y 6.
3. Repetir cada configuración con varias inicializaciones o semillas.
4. Calcular silhouette para cada K.
5. Examinar la variabilidad de silhouette entre repeticiones.
6. Seleccionar una solución considerando:
   - cohesión;
   - separación;
   - estabilidad;
   - simplicidad;
   - interpretabilidad.
7. Describir cada cluster mediante valores centrales de las variables en sus unidades originales.
8. Después de finalizar el agrupamiento, comparar los clusters con `species` mediante una tabla cruzada. Esta comparación no convierte el clustering en clasificación.
9. Analizar casos con silhouette baja o negativa.
10. Explicar si los grupos podrían apoyar alguna decisión concreta.

### Preguntas de análisis

1. ¿Por qué es imprescindible escalar antes de usar distancias con estas variables?
2. ¿Un silhouette alto demuestra que los grupos tienen significado biológico?
3. ¿Por qué distintas semillas pueden producir soluciones diferentes?
4. ¿Qué significa que un cluster contenga varias especies?
5. ¿Qué información aporta la estabilidad que no aporta una única ejecución?

### Evidencia requerida

- Curva o tabla de silhouette para K = 2, ..., 6.
- Resumen de estabilidad entre repeticiones.
- Perfiles de clusters en unidades originales.
- Tabla cruzada final con `species`.
- Interpretación que separe evidencia geométrica de significado de dominio.

---

# Bloque E. Validación cruzada y comparación de modelos

## Ejercicio 11. Validación cruzada del procedimiento completo

### Objetivo

Estimar desempeño y variabilidad sin utilizar la prueba final.

### Consignas

Sobre el conjunto de desarrollo de la tarea de clasificación:

1. Definir una validación cruzada estratificada de K folds.
2. Construir un pipeline con:
   - imputación;
   - escalado, cuando el algoritmo lo requiera;
   - modelo.
3. Evaluar al menos:
   - regresión logística multinomial;
   - árbol de decisión.
4. Usar exactamente los mismos folds para ambos modelos.
5. Registrar accuracy y F1 macro en cada fold.
6. Informar promedio, desvío estándar, mínimo y máximo.
7. Evitar consultar el conjunto de prueba.

### Preguntas de análisis

1. ¿Por qué informar solamente el promedio oculta información?
2. ¿Qué indicaría una dispersión grande entre folds?
3. ¿Por qué los modelos deben utilizar los mismos folds?
4. ¿Dónde deben aprenderse imputación, escalado y cualquier selección de atributos?
5. ¿Qué parte del proceso permanece completamente fuera del ciclo?

### Evidencia requerida

- Descripción de folds, semilla y métricas.
- Tabla con resultados por fold.
- Tabla resumida de comparación.
- Selección provisional de un modelo, todavía sin abrir la prueba.

---

## Ejercicio 12. Subajuste, equilibrio y sobreajuste

### Objetivo

Relacionar capacidad del modelo con desempeño de entrenamiento y validación.

### Consignas

Entrenar árboles de clasificación con diferentes valores de profundidad máxima, por ejemplo:

`1, 2, 3, 5, 8, sin límite`

Para cada configuración:

1. Medir desempeño de entrenamiento.
2. Medir desempeño mediante los mismos folds de validación.
3. Registrar promedio y dispersión.
4. Construir una figura con complejidad en el eje horizontal y desempeño en el vertical.
5. Clasificar cada región como posible subajuste, equilibrio o sobreajuste.
6. Seleccionar una configuración considerando desempeño, estabilidad y simplicidad.

### Preguntas de análisis

1. ¿Qué patrón se espera bajo subajuste?
2. ¿Qué brecha entre entrenamiento y validación sugiere sobreajuste?
3. ¿Por qué no debe elegirse la configuración con mejor entrenamiento?
4. ¿Qué papel cumple la simplicidad cuando dos configuraciones rinden de forma semejante?

### Evidencia requerida

- Tabla por configuración.
- Curva de desempeño.
- Selección justificada sin utilizar la prueba.

---


