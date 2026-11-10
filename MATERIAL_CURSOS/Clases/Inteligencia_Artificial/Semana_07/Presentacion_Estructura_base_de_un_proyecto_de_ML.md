---
title: "Estructura base de un proyecto de Machine Learning"
subtitle: "Selección interna, evaluación externa y ajuste definitivo"
author: "Curso de Inteligencia Artificial"
course: "Inteligencia Artificial"
week: 7
lang: es
---

# Estructura base de un proyecto de Machine Learning

## Selección interna, evaluación externa y ajuste definitivo

**Semana 7 · Presentación complementaria**

**Recorrido conceptual:** `protocolo → selección → evaluación → ajuste final`

---

# El objeto evaluado es el procedimiento

Un proyecto de ML no evalúa solamente un algoritmo. Evalúa un procedimiento completo:

$$
\text{datos}
\rightarrow \text{transformaciones}
\rightarrow \text{representación}
\rightarrow \text{modelo}
\rightarrow \text{regla de decisión}.
$$

La imputación, codificación, escala, selección de variables, hiperparámetros y umbral pueden aprender de los datos. Por eso forman parte del pipeline que debe aislarse y evaluarse.

---

# Protocolo antes de ajustar

Antes de observar resultados comparativos se define:

- problema, población, unidad e instante de predicción;
- alternativas y espacio de configuraciones;
- métrica principal y regla de selección;
- partición compatible con independencia, grupos y tiempo;
- disponibilidad de una prueba independiente;
- semillas, presupuesto y criterios de desempate.

La anidación separa selección y evaluación, pero no corrige una formulación o partición inadecuada.

---

# Diagrama general de validación anidada

La metodología contiene dos ciclos:

- **Ciclo interno:** compara configuraciones y elige una para cada entrenamiento externo.
- **Ciclo externo:** evalúa el procedimiento completo de selección sobre datos no usados por ese procedimiento.

La prueba independiente es opcional y permanece reservada hasta que el procedimiento queda fijado.

El gráfico se lee de izquierda a derecha en la fila de ajuste y de derecha a izquierda en la de evaluación. El retorno hacia la siguiente partición tiene un carril inferior exclusivo. Entrenamiento y validación externos se renuevan juntos en cada partición; la prueba opcional se desarrolla en la diapositiva 9.

Convenciones del diagrama:

- paralelogramos: datos;
- rectángulos: procesos;
- rombos: decisiones de repetición;
- marco azul: evaluación externa;
- marco verde: selección interna;
- línea discontinua: prueba independiente opcional.

---

# Ciclo externo: estimar el procedimiento

Para cada partición externa:

1. separar entrenamiento externo y validación externa;
2. ejecutar toda la selección únicamente dentro del entrenamiento externo;
3. reajustar la configuración elegida con ese entrenamiento completo;
4. predecir la validación externa una sola vez;
5. conservar las predicciones fuera de muestra.

“Externa” describe su posición respecto del ciclo de selección. No implica necesariamente otra población o institución.

---

# Ciclo interno: elegir la configuración

Dentro de cada entrenamiento externo:

1. generar particiones internas respetando grupos o tiempo;
2. ajustar cada pipeline candidato con entrenamiento interno;
3. aplicar lo aprendido a validación interna;
4. agregar resultados de todos los folds internos;
5. elegir según la regla definida previamente.

No se selecciona por el mejor resultado de un fold aislado.

---

# El pipeline vive dentro de cada fold

Para una configuración candidata:

`entrenamiento interno → ajustar transformaciones → ajustar modelo`

`validación interna → aplicar transformaciones congeladas → predecir → medir`

Pueden formar parte del ajuste:

- imputación y tratamiento de categorías;
- escalado, vocabulario o componentes;
- selección de variables o balanceo;
- hiperparámetros del estimador;
- calibración y umbral de decisión.

---

# Predicciones externas y agregación

Después de elegir una configuración dentro de cada fold externo:

$$
\text{entrenamiento externo completo}
\rightarrow \text{reajuste}
\rightarrow \text{predicción externa}.
$$

Las predicciones externas se integran para calcular métricas fuera de muestra.

- Conservar resultados y soporte por fold.
- Revisar variación, grupos y calibración cuando corresponda.
- No multiplicar artificialmente la cantidad de observaciones independientes en CV repetida.
- No usar resultados externos para iniciar otra selección sin reconocer su reutilización.

---

# Modelo definitivo y prueba opcional

La evaluación externa estima el procedimiento, pero no entrega automáticamente el modelo definitivo.

1. Aplicar nuevamente la búsqueda interna sobre todos los datos de desarrollo.
2. Elegir la configuración con la regla predefinida.
3. Reajustar el pipeline completo con los datos permitidos.
4. Persistir transformaciones, estimador, umbral y metadatos.
5. Si existe prueba independiente, evaluarla una sola vez.

No se elige como modelo final el ajuste del fold externo con mejor puntuación.

---

# Ejemplo: anticipar demora crítica

**Tarea:** predecir si un trayecto tendrá más de 10 minutos de demora.

| Nivel | Decisión ilustrativa |
|---|---|
| Partición externa | vehículos completos, sin compartir vehículo entre folds |
| Partición interna | folds por vehículo dentro del entrenamiento externo |
| Pipelines | logística escalada, SVM con RBF y árbol controlado |
| Configuraciones | regularización, $C$, $\gamma$, profundidad y umbral |
| Selección interna | recall mínimo y menor cantidad de falsas alarmas |
| Evaluación externa | predicciones fuera de muestra por vehículo |
| Resultado final | nueva búsqueda interna y reajuste con desarrollo completo |

---

# Errores que rompen la separación

| Error | Consecuencia |
|---|---|
| preprocesar antes de crear folds | validación influye en la representación |
| seleccionar con resultados externos | estimación externa se vuelve optimista |
| abrir prueba repetidamente | prueba pasa a cumplir función de validación |
| mezclar grupos o periodos | se evalúa una tarea más fácil que el uso real |
| reportar el ganador interno | se ignora el sesgo de selección |
| conservar el mejor fold externo | se elige por azar de esa partición |

La anidación organiza el uso de la información; no vuelve válida cualquier decisión experimental.

---

# Síntesis

- El pipeline completo es la unidad evaluada.
- El ciclo interno selecciona configuraciones.
- El ciclo externo estima el procedimiento de selección.
- Cada transformación se ajusta únicamente con el entrenamiento correspondiente.
- Las predicciones externas se agregan sin volver a seleccionar.
- El modelo definitivo se reajusta después de evaluar el procedimiento.
- La prueba independiente es opcional, pero debe permanecer intacta si existe.
- Si no existe selección adaptativa, puede omitirse el ciclo interno, pero no el ajuste local de transformaciones.

**Lecturas:** capítulo 9, §9.3; capítulo 3, §3.4; capítulo 10, §10.2.7.
