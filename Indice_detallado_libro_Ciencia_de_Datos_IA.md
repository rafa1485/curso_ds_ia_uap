# Ciencia de Datos e Inteligencia Artificial

## Fundamentos, métodos y aplicaciones con Python y R

## Índice temático detallado para el desarrollo del libro

Este documento define la estructura propuesta del material teórico común a los cursos de **Ciencia de Datos** e **Inteligencia Artificial**. La obra se organiza en 16 capítulos, ordenados de manera progresiva para que cada uno se apoye en conocimientos desarrollados previamente.

Cada sección contiene las subsecciones teóricas que deberán desarrollarse durante la redacción. Al final de toda sección teórica se incorpora una subsección de **Ejemplo práctico guiado**, destinada a presentar paso a paso una aplicación acotada de los conocimientos correspondientes.

La práctica del libro se organiza en tres niveles:

1. **Ejemplo práctico guiado:** introduce y ejercita una técnica puntual. Puede resolverse durante la lectura o la clase y no necesariamente forma parte de la evaluación obligatoria.
2. **Actividad EMO (Experiencia Mínima Obligatoria):** exige que cada estudiante demuestre individualmente una capacidad esencial sobre uno de los cuatro datasets, aunque su desarrollo pueda incluir instancias de colaboración.
3. **Laboratorio integrador:** reúne las cuatro actividades EMO de un dataset en una tarea de mayor alcance, conectando contenidos de varios capítulos.

Los cuatro datasets funcionan como casos transversales:

1. Movilidad urbana y transporte.
2. Calidad, consumo y gestión del agua.
3. Reclamos financieros y procesamiento de texto.
4. Diagnóstico visual de enfermedades vegetales.

Cada estudiante deberá completar las 16 actividades EMO —cuatro por dataset— y participar en los cuatro laboratorios. Los equipos podrán además profundizar uno de los casos como proyecto integrador final.

## Convenciones para las actividades prácticas

- `[GUIADO]`: ejemplo resuelto o parcialmente resuelto para aprender una técnica.
- `[EMO · AGUA-nn]`: experiencia obligatoria con datos de agua.
- `[EMO · MOV-nn]`: experiencia obligatoria con datos de movilidad.
- `[EMO · REC-nn]`: experiencia obligatoria con reclamos financieros.
- `[EMO · VEG-nn]`: experiencia obligatoria con imágenes de sanidad vegetal.
- `[LAB · dataset]`: laboratorio integrador que combina las EMO del caso.

En toda actividad EMO se indicarán la capacidad mínima, la consigna, la evidencia individual y los criterios de aprobación. Aprobar una actividad implica demostrar la capacidad requerida; no exige obtener el mejor modelo ni una métrica predeterminada.

---

# Parte I. Fundamentos y trabajo con datos

# Capítulo 1. Ciencia de Datos e Inteligencia Artificial: conceptos, historia y aplicaciones

## 1.1. Ciencia de Datos, Inteligencia Artificial y aprendizaje automático

### 1.1.1. Definición y objetivos de la Ciencia de Datos

### 1.1.2. Definición y objetivos de la Inteligencia Artificial

### 1.1.3. Aprendizaje automático y aprendizaje profundo

### 1.1.4. Relación con la estadística, la optimización y la ingeniería de software

### 1.1.5. Diferencias entre modelos descriptivos, predictivos y prescriptivos

### 1.1.6. Ejemplo práctico guiado: identificación de componentes de Ciencia de Datos e IA en un problema real

Desarrollar un caso en el que se diferencien la captura de datos, el análisis descriptivo, la predicción y la toma automatizada de decisiones.

## 1.2. Enfoques y fundamentos de la Inteligencia Artificial

### 1.2.1. Sistemas que actúan como seres humanos

### 1.2.2. Sistemas que piensan como seres humanos

### 1.2.3. Sistemas que piensan racionalmente

### 1.2.4. Sistemas que actúan racionalmente

### 1.2.5. Test de Turing y modelado cognitivo

### 1.2.6. Fundamentos filosóficos, matemáticos y computacionales

### 1.2.7. Ejemplo práctico guiado: análisis de un asistente inteligente desde los cuatro enfoques de la IA

Evaluar un sistema conocido e identificar qué capacidades exhibe, qué información utiliza y bajo qué criterio puede considerarse inteligente.

## 1.3. Evolución histórica de la Ciencia de Datos y la IA

### 1.3.1. Antecedentes lógicos y matemáticos

### 1.3.2. Nacimiento formal de la Inteligencia Artificial

### 1.3.3. Sistemas expertos y representación simbólica

### 1.3.4. Invierno de la IA y resurgimiento estadístico

### 1.3.5. Big Data, aprendizaje profundo e IA generativa

### 1.3.6. Ejemplo práctico guiado: construcción de una línea de tiempo tecnológica

Relacionar hitos históricos con la disponibilidad de datos, la capacidad de cómputo y los cambios metodológicos.

## 1.4. Aplicaciones, alcances y riesgos

### 1.4.1. Aplicaciones en ingeniería e industria

### 1.4.2. Aplicaciones en salud, ambiente y agricultura

### 1.4.3. Aplicaciones en finanzas y sistemas de información

### 1.4.4. Automatización, asistencia y apoyo a decisiones

### 1.4.5. Limitaciones técnicas y organizacionales

### 1.4.6. Sesgos, privacidad, seguridad y uso responsable

### 1.4.7. Ejemplo práctico guiado: evaluación inicial de oportunidades y riesgos

Elaborar una ficha de análisis para una aplicación real, incluyendo beneficios esperados, actores afectados, riesgos y límites de automatización.

---

# Capítulo 2. Ciclo de vida de un proyecto basado en datos

## 2.1. Formulación del problema

### 2.1.1. Problema real, pregunta analítica y tarea computacional

### 2.1.2. Objetivos técnicos y objetivos de negocio

### 2.1.3. Unidad de análisis, población y alcance

### 2.1.4. Variables de entrada, resultados y restricciones

### 2.1.5. Criterios de éxito y línea de base

### 2.1.6. Ejemplo práctico guiado: formulación de un problema de mantenimiento ferroviario

Transformar una necesidad operativa en preguntas descriptivas, predictivas y prescriptivas medibles.

### Actividad EMO [AGUA-01]: formular el problema y la decisión operativa

**Capacidad mínima:** convertir una necesidad de gestión del agua en una tarea analítica verificable.

**Consigna:** definir la unidad de análisis, el usuario, la decisión que se desea apoyar, la variable objetivo, las variables disponibles, las restricciones y un baseline razonable para el dataset de calidad o gestión del agua.

**Modalidad de trabajo:** preparación individual con una instancia breve de contraste entre pares.

**Evidencia individual:** ficha de una página con el problema, las preguntas descriptiva, predictiva y prescriptiva, la métrica de valor y los supuestos.

**Criterios de aprobación:**

- Existe correspondencia entre la necesidad, la tarea computacional y la decisión.
- La unidad de análisis y el resultado esperado son observables o medibles.
- Los límites, actores afectados y supuestos quedan explícitos.

**Aporte al laboratorio:** define el alcance y los criterios de éxito del laboratorio de agua.

## 2.2. Metodologías para proyectos de datos

### 2.2.1. Proceso KDD

### 2.2.2. Metodología CRISP-DM

### 2.2.3. Ciclos iterativos y enfoques ágiles

### 2.2.4. Hipótesis, experimentación y retroalimentación

### 2.2.5. Roles dentro de un equipo de datos

### 2.2.6. Ejemplo práctico guiado: diseño de un ciclo CRISP-DM

Organizar las etapas, actividades y entregables de uno de los proyectos integradores.

## 2.3. Fuentes, tipos y arquitectura básica de datos

### 2.3.1. Datos estructurados

### 2.3.2. Datos semiestructurados

### 2.3.3. Datos no estructurados

### 2.3.4. Datos observacionales, experimentales y simulados

### 2.3.5. Datasets abiertos y fuentes privadas

### 2.3.6. Bases de datos, archivos, APIs y flujos de sensores

### 2.3.7. Introducción a las características de Big Data

### 2.3.8. Ejemplo práctico guiado: inventario de fuentes para movilidad urbana

Identificar fuentes abiertas, formatos, frecuencias de actualización y posibles claves de integración.

## 2.4. Entornos, herramientas y reproducibilidad

### 2.4.1. Python y R como entornos de análisis

### 2.4.2. Cuadernos Jupyter y documentos reproducibles

### 2.4.3. Bibliotecas esenciales de Python

### 2.4.4. Ecosistema tidyverse en R

### 2.4.5. Organización de código, datos y resultados

### 2.4.6. Versionado de código, datos y modelos

### 2.4.7. Semillas aleatorias y registro de experimentos

### 2.4.8. Ejemplo práctico guiado: creación de la estructura reproducible de un proyecto

Preparar carpetas, cuaderno inicial, archivo de dependencias y registro básico de experimentos.

---

# Capítulo 3. Preparación, calidad y transformación de datos

## 3.1. Comprensión y evaluación de la calidad de los datos

### 3.1.1. Estructura de una tabla de datos

### 3.1.2. Tipos de variables

### 3.1.3. Escalas de medición

### 3.1.4. Exactitud, completitud, consistencia y actualidad

### 3.1.5. Perfiles y diccionarios de datos

### 3.1.6. Reglas de validación

### 3.1.7. Ejemplo práctico guiado: auditoría inicial de un dataset abierto

Construir un perfil de calidad que identifique tipos, rangos, faltantes, duplicados e inconsistencias.

## 3.2. Limpieza de datos

### 3.2.1. Datos faltantes y mecanismos de ausencia

### 3.2.2. Eliminación e imputación de observaciones

### 3.2.3. Registros duplicados

### 3.2.4. Errores de codificación y unidades

### 3.2.5. Valores imposibles e inconsistencias lógicas

### 3.2.6. Detección y tratamiento de valores atípicos

### 3.2.7. Ejemplo práctico guiado: limpieza de mediciones de temperatura y vibración

Diseñar y aplicar reglas que preserven eventos reales mientras se corrigen errores de medición o registro.

### Actividad EMO [AGUA-02]: auditar y limpiar mediciones de agua

**Capacidad mínima:** distinguir datos faltantes, registros erróneos y posibles eventos físicos reales.

**Consigna:** perfilar un subconjunto de mediciones, identificar faltantes, duplicados, cambios de unidad, valores imposibles y atípicos; luego aplicar una estrategia de limpieza e imputación justificada.

**Modalidad de trabajo:** análisis colaborativo; implementación y conclusiones individuales.

**Evidencia individual:** notebook reproducible con tabla de reglas, comparación antes/después y justificación de cada decisión.

**Criterios de aprobación:**

- Las reglas se derivan del diccionario de datos o de límites físicos documentados.
- La imputación o exclusión se aplica sin utilizar información futura o de prueba.
- Los posibles eventos reales no se eliminan automáticamente como errores.

**Aporte al laboratorio:** genera el dataset depurado y documentado.

## 3.3. Integración y transformación

### 3.3.1. Selección y filtrado de observaciones

### 3.3.2. Combinación de tablas y tipos de unión

### 3.3.3. Agregación y cambio de granularidad

### 3.3.4. Reformateo entre estructuras anchas y largas

### 3.3.5. Codificación de variables categóricas

### 3.3.6. Normalización y estandarización

### 3.3.7. Transformaciones matemáticas

### 3.3.8. Discretización y binarización

### 3.3.9. Ejemplo práctico guiado: integración de reclamos y datos contextuales

Unir fuentes heterogéneas y obtener una tabla analítica consistente para modelado.

### Actividad EMO [REC-01]: construir el corpus analítico de reclamos

**Capacidad mínima:** transformar registros de reclamos y variables contextuales en un corpus reproducible sin contaminar la variable objetivo.

**Consigna:** seleccionar el texto relevante, armonizar categorías, resolver duplicados, documentar faltantes y construir una tabla con identificador, texto, etiqueta y variables contextuales permitidas.

**Modalidad de trabajo:** criterios comunes por equipo; preparación y verificación individual.

**Evidencia individual:** notebook de preparación, diccionario del corpus y diagrama breve de procedencia de las variables.

**Criterios de aprobación:**

- Cada observación y etiqueta tienen una interpretación inequívoca.
- Se identifican campos que revelarían directa o indirectamente la respuesta.
- El procedimiento permite reconstruir el mismo corpus desde los datos originales.

**Aporte al laboratorio:** produce la entrada común del laboratorio de reclamos.

## 3.4. Pipelines y prevención de fugas de información

### 3.4.1. Concepto de pipeline

### 3.4.2. Ajuste y aplicación de transformaciones

### 3.4.3. Fuga de información o data leakage

### 3.4.4. Transformaciones dependientes del conjunto de entrenamiento

### 3.4.5. Tratamiento conjunto del preprocesamiento y el modelo

### 3.4.6. Pruebas y documentación del proceso

### 3.4.7. Ejemplo práctico guiado: construcción de un pipeline sin fuga de información

Comparar un procedimiento incorrecto con otro que ajuste todas las transformaciones únicamente sobre datos de entrenamiento.

---

# Capítulo 4. Estadística descriptiva, exploración y visualización

## 4.1. Descripción de una variable

### 4.1.1. Población, muestra, parámetro y estadístico

### 4.1.2. Distribuciones de frecuencias

### 4.1.3. Media, mediana y moda

### 4.1.4. Cuantiles y medidas de posición

### 4.1.5. Rango, varianza y desviación estándar

### 4.1.6. Rango intercuartílico

### 4.1.7. Asimetría y curtosis

### 4.1.8. Ejemplo práctico guiado: perfil estadístico del consumo eléctrico

Calcular e interpretar medidas descriptivas y reconocer distribuciones asimétricas y observaciones extremas.

### Actividad EMO [AGUA-03]: explorar patrones y anomalías en datos de agua

**Capacidad mínima:** describir la distribución de las variables y separar hallazgos estadísticos de conclusiones operativas no demostradas.

**Consigna:** calcular medidas robustas, comparar grupos o períodos, representar las distribuciones y seleccionar tres hallazgos que puedan orientar una hipótesis de riesgo o un muestreo posterior.

**Modalidad de trabajo:** exploración en parejas; interpretación y entrega individuales.

**Evidencia individual:** notebook o informe reproducible con al menos tres visualizaciones, sus interpretaciones y una advertencia sobre causalidad o sesgo.

**Criterios de aprobación:**

- Las medidas y gráficos son adecuados a la escala y distribución de las variables.
- Cada hallazgo está respaldado por evidencia visible o cuantificada.
- Se distinguen observaciones atípicas, errores y eventos que requieren investigación.

**Aporte al laboratorio:** establece el diagnóstico exploratorio y las hipótesis de riesgo.

## 4.2. Relaciones entre variables

### 4.2.1. Tablas de contingencia

### 4.2.2. Covarianza

### 4.2.3. Correlación lineal

### 4.2.4. Correlaciones no paramétricas

### 4.2.5. Asociación frente a causalidad

### 4.2.6. Variables de confusión

### 4.2.7. Análisis multivariado exploratorio

### 4.2.8. Ejemplo práctico guiado: análisis de factores asociados con retrasos de transporte

Explorar relaciones entre horario, clima, recorrido, demanda y tiempo de viaje sin confundir asociación con causalidad.

## 4.3. Visualización exploratoria

### 4.3.1. Principios de percepción visual

### 4.3.2. Histogramas y gráficos de densidad

### 4.3.3. Diagramas de caja y violín

### 4.3.4. Gráficos de barras y proporciones

### 4.3.5. Diagramas de dispersión

### 4.3.6. Mapas de calor

### 4.3.7. Visualización temporal y geográfica

### 4.3.8. Errores y manipulaciones frecuentes

### 4.3.9. Ejemplo práctico guiado: panel exploratorio de movilidad

Construir un conjunto coherente de visualizaciones que permita detectar patrones temporales, espaciales y operativos.

### Actividad EMO [MOV-01]: construir un diagnóstico geotemporal de movilidad

**Capacidad mínima:** preparar y representar correctamente datos con componentes espacial y temporal.

**Consigna:** obtener zonas y franjas horarias comparables, mapear la intensidad de viajes o demanda y detectar al menos dos patrones y una observación atípica.

**Modalidad de trabajo:** preparación de datos en equipo; visualizaciones e interpretación individuales.

**Evidencia individual:** notebook con mapa, gráfico temporal, descripción de la granularidad y tres conclusiones justificadas.

**Criterios de aprobación:**

- La agregación espacial y temporal conserva una unidad de análisis clara.
- Los gráficos permiten comparar zonas o períodos sin escalas engañosas.
- Las conclusiones reconocen cobertura, estacionalidad y posibles sesgos de registro.

**Aporte al laboratorio:** proporciona el diagnóstico geotemporal sobre el que se construyen segmentación y pronóstico.

## 4.4. Comunicación de resultados

### 4.4.1. Pregunta, evidencia y mensaje principal

### 4.4.2. Selección del gráfico según el objetivo

### 4.4.3. Storytelling con datos

### 4.4.4. Visualizaciones interactivas

### 4.4.5. Dashboards y aplicaciones web

### 4.4.6. Comunicación para públicos técnicos y no técnicos

### 4.4.7. Accesibilidad y documentación

### 4.4.8. Ejemplo práctico guiado: presentación ejecutiva de un hallazgo

Transformar un análisis exploratorio en una visualización y una explicación breve orientadas a la toma de decisiones.

---

# Parte II. Probabilidad, agentes y resolución de problemas

# Capítulo 5. Probabilidad, incertidumbre e inferencia bayesiana

## 5.1. Fundamentos de probabilidad

### 5.1.1. Experimento aleatorio y espacio muestral

### 5.1.2. Eventos y operaciones entre eventos

### 5.1.3. Axiomas de probabilidad

### 5.1.4. Reglas de suma y producto

### 5.1.5. Probabilidad condicional

### 5.1.6. Independencia

### 5.1.7. Ejemplo práctico guiado: probabilidad de incidentes en una red de transporte

Calcular probabilidades simples, conjuntas y condicionales a partir de datos observados.

## 5.2. Variables aleatorias y distribuciones

### 5.2.1. Variables aleatorias discretas y continuas

### 5.2.2. Función de probabilidad y función de densidad

### 5.2.3. Función de distribución acumulada

### 5.2.4. Esperanza, varianza y covarianza

### 5.2.5. Distribuciones discretas frecuentes

### 5.2.6. Distribuciones continuas frecuentes

### 5.2.7. Distribuciones conjuntas, marginales y condicionales

### 5.2.8. Ejemplo práctico guiado: modelado probabilístico de fallas y tiempos de espera

Seleccionar distribuciones plausibles y contrastar sus propiedades con observaciones reales.

## 5.3. Teorema de Bayes e inferencia probabilística

### 5.3.1. Probabilidad previa

### 5.3.2. Verosimilitud

### 5.3.3. Probabilidad posterior

### 5.3.4. Evidencia y normalización

### 5.3.5. Actualización secuencial de creencias

### 5.3.6. Inferencia mediante distribuciones conjuntas

### 5.3.7. Ejemplo práctico guiado: diagnóstico probabilístico de una transacción fraudulenta

Actualizar la probabilidad de fraude a partir de sucesivas evidencias sobre importe, dispositivo y localización.

### Actividad EMO [AGUA-04]: estimar riesgo y priorizar una acción

**Capacidad mínima:** actualizar una probabilidad con evidencia y convertirla en una decisión explícita.

**Consigna:** construir un modelo probabilístico base para una condición anómala, actualizar el riesgo con al menos dos evidencias y definir una regla de priorización que considere los costos de falsos positivos y falsos negativos.

**Modalidad de trabajo:** discusión de supuestos en grupo; cálculos, sensibilidad y decisión individuales.

**Evidencia individual:** notebook o planilla reproducible con probabilidades previas y posteriores, matriz de costos y análisis de sensibilidad.

**Criterios de aprobación:**

- Se diferencian probabilidad previa, verosimilitud y posterior.
- La decisión se deriva de probabilidades y costos declarados.
- Se analiza cómo cambia la prioridad cuando varían los supuestos.

**Aporte al laboratorio:** produce el indicador de riesgo y la regla de priorización.

## 5.4. Incertidumbre y comunicación probabilística

### 5.4.1. Incertidumbre aleatoria

### 5.4.2. Incertidumbre epistémica

### 5.4.3. Estimaciones puntuales e intervalos

### 5.4.4. Calibración de probabilidades

### 5.4.5. Riesgos de interpretación

### 5.4.6. Comunicación de resultados inciertos

### 5.4.7. Ejemplo práctico guiado: elaboración de un reporte de riesgo

Expresar probabilidades, incertidumbres y supuestos de manera comprensible para una decisión operativa.

---

# Laboratorio integrador 1. Diagnóstico y priorización en calidad del agua

**Etiqueta:** `[LAB · AGUA]`

**Actividades EMO integradas:** `AGUA-01`, `AGUA-02`, `AGUA-03` y `AGUA-04`.

**Propósito:** construir una cadena reproducible que vaya desde la formulación del problema y la depuración de mediciones hasta la estimación de riesgo y la priorización de muestreos, inspecciones o intervenciones.

**Consigna integradora:**

1. Delimitar la unidad de análisis, el usuario y la decisión.
2. Auditar, limpiar y documentar las variables seleccionadas.
3. Describir patrones, grupos y anomalías relevantes.
4. Estimar un riesgo probabilístico con supuestos explícitos.
5. Proponer una prioridad de acción y justificarla mediante costos y sensibilidad.
6. Comunicar qué puede concluirse, qué no puede concluirse y qué dato adicional sería más valioso.

**Producto grupal:** informe técnico breve con notebook reproducible, tabla o mapa de prioridades y recomendación operativa.

**Evidencia individual:** anexo de decisiones metodológicas y defensa corta de una observación, una probabilidad y una prioridad elegidas por el estudiante.

**Criterios de aprobación:**

- Se pueden reconstruir los datos y resultados.
- La depuración no oculta anomalías relevantes.
- El indicador de riesgo y la decisión son coherentes con los supuestos.
- La incertidumbre y las limitaciones se comunican de forma explícita.

**Perspectiva de Ciencia de Datos:** calidad, trazabilidad, análisis exploratorio y comunicación.

**Perspectiva de Inteligencia Artificial:** representación de evidencia, incertidumbre, utilidad y selección de acciones.

---

# Capítulo 6. Agentes inteligentes y representación de problemas

## 6.1. Agentes y racionalidad

### 6.1.1. Concepto de agente

### 6.1.2. Percepciones, sensores, acciones y actuadores

### 6.1.3. Función y programa de agente

### 6.1.4. Medidas de desempeño

### 6.1.5. Racionalidad y autonomía

### 6.1.6. Agentes omniscientes frente a agentes racionales

### 6.1.7. Ejemplo práctico guiado: definición de un agente para supervisión de una cadena de frío

Especificar las percepciones, acciones, objetivos, información disponible y criterios de desempeño.

## 6.2. Entornos de tarea

### 6.2.1. Descripción PEAS

### 6.2.2. Entornos observables y parcialmente observables

### 6.2.3. Entornos deterministas y estocásticos

### 6.2.4. Entornos episódicos y secuenciales

### 6.2.5. Entornos estáticos y dinámicos

### 6.2.6. Entornos discretos y continuos

### 6.2.7. Entornos monoagente y multiagente

### 6.2.8. Ejemplo práctico guiado: caracterización PEAS de un sistema de movilidad

Describir formalmente un agente que recomiende rutas o gestione una flota.

## 6.3. Arquitecturas de agentes

### 6.3.1. Agentes reactivos simples

### 6.3.2. Agentes reactivos basados en modelos

### 6.3.3. Agentes orientados a objetivos

### 6.3.4. Agentes basados en utilidad

### 6.3.5. Agentes que aprenden

### 6.3.6. Componentes de aprendizaje, crítica y exploración

### 6.3.7. Ejemplo práctico guiado: comparación de arquitecturas

Diseñar distintas versiones de un agente para un mismo problema y analizar sus ventajas y limitaciones.

## 6.4. Representación computacional de problemas

### 6.4.1. Estados y variables de estado

### 6.4.2. Acciones y modelos de transición

### 6.4.3. Estado inicial y estados objetivo

### 6.4.4. Costos, restricciones y utilidad

### 6.4.5. Nivel de abstracción

### 6.4.6. Introducción a la representación del conocimiento

### 6.4.7. Ejemplo práctico guiado: formulación de un problema de asignación de recursos

Traducir una situación real a estados, acciones, restricciones, costos y condición de objetivo.

---

# Capítulo 7. Búsqueda y resolución algorítmica de problemas

## 7.1. Espacios de estados y procesos de búsqueda

### 7.1.1. Árboles y grafos

### 7.1.2. Nodos, estados y caminos

### 7.1.3. Frontera y conjunto explorado

### 7.1.4. Búsqueda en árbol y búsqueda en grafo

### 7.1.5. Ciclos y estados repetidos

### 7.1.6. Complejidad temporal y espacial

### 7.1.7. Ejemplo práctico guiado: representación de una red vial como grafo

Construir el espacio de estados y definir costos para un problema de rutas.

## 7.2. Búsqueda no informada

### 7.2.1. Búsqueda en anchura

### 7.2.2. Búsqueda en profundidad

### 7.2.3. Búsqueda con profundidad limitada

### 7.2.4. Profundización iterativa

### 7.2.5. Búsqueda de costo uniforme

### 7.2.6. Completitud y optimalidad

### 7.2.7. Comparación de estrategias

### 7.2.8. Ejemplo práctico guiado: comparación experimental de algoritmos no informados

Resolver el mismo grafo con varias estrategias y comparar solución, tiempo y memoria.

## 7.3. Búsqueda informada y heurísticas

### 7.3.1. Funciones heurísticas

### 7.3.2. Búsqueda voraz

### 7.3.3. Algoritmo A*

### 7.3.4. Heurísticas admisibles

### 7.3.5. Heurísticas consistentes

### 7.3.6. Diseño y evaluación de heurísticas

### 7.3.7. Ejemplo práctico guiado: búsqueda de rutas con A*

Diseñar una heurística geográfica y verificar su efecto sobre la cantidad de nodos explorados.

### Actividad EMO [MOV-02]: comparar rutas y heurísticas sobre una red

**Capacidad mínima:** representar una red de movilidad como grafo y justificar una estrategia de búsqueda.

**Consigna:** seleccionar orígenes y destinos del dataset, construir un grafo simplificado, comparar costo uniforme y A* y evaluar una heurística en términos de solución, nodos explorados y costo computacional.

**Modalidad de trabajo:** construcción del grafo en equipo; experimentos y análisis individuales.

**Evidencia individual:** notebook con representación del grafo, definición de costos, resultados comparativos y discusión de admisibilidad o limitaciones de la heurística.

**Criterios de aprobación:**

- Estados, acciones, costos y objetivo quedan definidos sin ambigüedad.
- Los algoritmos se comparan sobre las mismas instancias.
- La heurística utiliza información disponible y sus propiedades se justifican.

**Aporte al laboratorio:** incorpora la dimensión de decisión o desplazamiento sobre la estructura espacial.

## 7.4. Búsqueda local y problemas con restricciones

### 7.4.1. Búsqueda por ascenso de colinas

### 7.4.2. Máximos locales, mesetas y crestas

### 7.4.3. Recocido simulado

### 7.4.4. Introducción a algoritmos evolutivos

### 7.4.5. Variables, dominios y restricciones

### 7.4.6. Satisfacción de restricciones

### 7.4.7. Ejemplo práctico guiado: planificación de recorridos de inspección

Optimizar un recorrido sujeto a límites de tiempo, prioridades y disponibilidad de recursos.

---

# Capítulo 8. Decisiones secuenciales y aprendizaje por refuerzo

## 8.1. Decisiones bajo incertidumbre

### 8.1.1. Alternativas, estados y consecuencias

### 8.1.2. Preferencias y teoría de utilidad

### 8.1.3. Utilidad esperada

### 8.1.4. Actitudes frente al riesgo

### 8.1.5. Árboles de decisión

### 8.1.6. Valor de la información

### 8.1.7. Ejemplo práctico guiado: decisión de inspección y reemplazo de un transformador

Comparar alternativas según probabilidad de avería, costos, beneficios y tolerancia al riesgo.

## 8.2. Procesos de decisión de Markov

### 8.2.1. Propiedad de Markov

### 8.2.2. Estados, acciones y transiciones

### 8.2.3. Recompensas

### 8.2.4. Políticas

### 8.2.5. Horizonte y factor de descuento

### 8.2.6. Funciones de valor

### 8.2.7. Ecuaciones de Bellman

### 8.2.8. Ejemplo práctico guiado: control secuencial de un sistema simplificado

Formular un proceso de decisión de Markov y calcular valores para una política dada.

## 8.3. Resolución de procesos de decisión

### 8.3.1. Evaluación de políticas

### 8.3.2. Mejora de políticas

### 8.3.3. Iteración de políticas

### 8.3.4. Iteración de valores

### 8.3.5. Convergencia y costo computacional

### 8.3.6. Ejemplo práctico guiado: selección de una política operativa

Implementar iteración de valores y analizar cómo cambia la política ante distintos costos y recompensas.

## 8.4. Aprendizaje por refuerzo

### 8.4.1. Aprendizaje basado en modelos y libre de modelos

### 8.4.2. Exploración frente a explotación

### 8.4.3. Métodos Monte Carlo

### 8.4.4. Aprendizaje por diferencias temporales

### 8.4.5. Q-learning

### 8.4.6. SARSA

### 8.4.7. Diseño de recompensas

### 8.4.8. Seguridad, estabilidad y límites de aplicación

### 8.4.9. Ejemplo práctico guiado: entrenamiento de un agente en un entorno discreto

Entrenar y comparar políticas mediante Q-learning y SARSA, observando convergencia y exploración.

---

# Parte III. Fundamentos del aprendizaje automático

# Capítulo 9. Formulación y evaluación de problemas de aprendizaje automático

## 9.1. Paradigmas de aprendizaje

### 9.1.1. Aprendizaje supervisado

### 9.1.2. Aprendizaje no supervisado

### 9.1.3. Aprendizaje semisupervisado

### 9.1.4. Aprendizaje autosupervisado

### 9.1.5. Regresión, clasificación y agrupamiento

### 9.1.6. Variables de entrada, objetivos y etiquetas

### 9.1.7. Ejemplo práctico guiado: formulación de cuatro tareas de aprendizaje

Clasificar problemas de movilidad, agua, reclamos e imágenes según paradigma, entradas, salidas y tipo de tarea.

## 9.2. Ajuste, error y generalización

### 9.2.1. Funciones de pérdida

### 9.2.2. Riesgo empírico

### 9.2.3. Error de entrenamiento y error de generalización

### 9.2.4. Sobreajuste y subajuste

### 9.2.5. Compromiso entre sesgo y varianza

### 9.2.6. Complejidad del modelo

### 9.2.7. Modelos de referencia o baselines

### 9.2.8. Ejemplo práctico guiado: curvas de aprendizaje

Diagnosticar sobreajuste o subajuste a partir del desempeño en entrenamiento y validación.

## 9.3. Diseño de la evaluación

### 9.3.1. Conjuntos de entrenamiento, validación y prueba

### 9.3.2. Muestreo aleatorio y estratificado

### 9.3.3. Validación cruzada

### 9.3.4. Validación para datos agrupados

### 9.3.5. Validación temporal

### 9.3.6. Selección de modelos e hiperparámetros

### 9.3.7. Reproducibilidad y comparación justa

### 9.3.8. Ejemplo práctico guiado: protocolo de evaluación sin contaminación

Diseñar un protocolo adecuado para datos con clases desbalanceadas, grupos o dependencia temporal.

## 9.4. Métricas de desempeño

### 9.4.1. MAE, MSE y RMSE

### 9.4.2. Coeficiente de determinación

### 9.4.3. Matriz de confusión

### 9.4.4. Exactitud, precisión y sensibilidad

### 9.4.5. Especificidad y puntuación F1

### 9.4.6. Curvas ROC y área ROC-AUC

### 9.4.7. Curvas precisión-recall y PR-AUC

### 9.4.8. Umbrales, costos y datos desbalanceados

### 9.4.9. Ejemplo práctico guiado: evaluación de un clasificador de incidentes

Comparar métricas y elegir un umbral considerando los costos de falsos positivos y falsos negativos.

### Actividad EMO [REC-02]: diseñar la evaluación de un clasificador de reclamos

**Capacidad mínima:** definir un protocolo de evaluación apropiado antes de entrenar el modelo de texto.

**Consigna:** analizar el balance de clases y posibles grupos o dependencias, establecer particiones, baseline, métrica principal, métricas auxiliares y costos de error para una tarea de clasificación o priorización de reclamos.

**Modalidad de trabajo:** discusión grupal del caso; protocolo y justificación individuales.

**Evidencia individual:** ficha experimental con particiones, baseline, métricas, regla de selección y prueba de que no existe fuga evidente entre entrenamiento y evaluación.

**Criterios de aprobación:**

- La partición respeta duplicados, grupos y orden temporal cuando corresponda.
- La métrica principal responde al objetivo operativo y al desbalance.
- El conjunto de prueba queda reservado para la evaluación final.

**Aporte al laboratorio:** fija el protocolo común con el que se compararán representaciones y modelos de texto.

---

# Capítulo 10. Ingeniería, selección y reducción de atributos

## 10.1. Ingeniería de características

### 10.1.1. Representación numérica de observaciones

### 10.1.2. Transformaciones lineales y no lineales

### 10.1.3. Interacciones entre variables

### 10.1.4. Variables categóricas

### 10.1.5. Características temporales

### 10.1.6. Características espaciales

### 10.1.7. Conocimiento del dominio

### 10.1.8. Ejemplo práctico guiado: atributos para predecir demanda de transporte

Crear variables temporales, espaciales y contextuales y justificar su relación con el fenómeno.

## 10.2. Selección de atributos

### 10.2.1. Relevancia y redundancia

### 10.2.2. Métodos de filtro

### 10.2.3. Métodos envolventes

### 10.2.4. Métodos embebidos

### 10.2.5. Importancia de variables

### 10.2.6. Regularización L1 y L2

### 10.2.7. Selección dentro de la validación cruzada

### 10.2.8. Ejemplo práctico guiado: selección de variables de calidad del agua

Comparar varios métodos y evaluar estabilidad, desempeño e interpretabilidad.

## 10.3. Reducción de dimensionalidad

### 10.3.1. Maldición de la dimensionalidad

### 10.3.2. Proyecciones y representaciones latentes

### 10.3.3. Análisis de componentes principales

### 10.3.4. Varianza explicada

### 10.3.5. Interpretación de componentes

### 10.3.6. Introducción a métodos no lineales

### 10.3.7. Visualización de datos de alta dimensión

### 10.3.8. Ejemplo práctico guiado: proyección de un dataset multivariado

Aplicar PCA, elegir la cantidad de componentes e interpretar la representación obtenida.

## 10.4. Pipelines de representación y modelado

### 10.4.1. Transformaciones encadenadas

### 10.4.2. Columnas numéricas, categóricas y textuales

### 10.4.3. Ajuste conjunto con el modelo

### 10.4.4. Búsqueda de hiperparámetros

### 10.4.5. Interpretabilidad frente a capacidad predictiva

### 10.4.6. Persistencia de transformaciones

### 10.4.7. Ejemplo práctico guiado: pipeline completo para datos heterogéneos

Integrar imputación, codificación, escalado, selección de atributos y estimación en un único proceso reproducible.

---

# Capítulo 11. Regresión y clasificación: modelos fundamentales

## 11.1. Regresión lineal

### 11.1.1. Formulación del problema de regresión

### 11.1.2. Regresión lineal simple

### 11.1.3. Regresión lineal múltiple

### 11.1.4. Estimación por mínimos cuadrados

### 11.1.5. Interpretación de coeficientes

### 11.1.6. Variables categóricas e interacciones

### 11.1.7. Ejemplo práctico guiado: predicción de consumo o demanda

Construir e interpretar un modelo lineal, comparándolo con una predicción de referencia.

## 11.2. Supuestos y diagnóstico del modelo lineal

### 11.2.1. Linealidad

### 11.2.2. Independencia

### 11.2.3. Homocedasticidad

### 11.2.4. Distribución de residuos

### 11.2.5. Multicolinealidad

### 11.2.6. Observaciones influyentes

### 11.2.7. Análisis gráfico de residuos

### 11.2.8. Ejemplo práctico guiado: diagnóstico y mejora de una regresión

Detectar incumplimientos de supuestos y evaluar transformaciones o cambios en la especificación.

## 11.3. Modelos lineales regularizados

### 11.3.1. Complejidad y sobreajuste

### 11.3.2. Regresión Ridge

### 11.3.3. Regresión Lasso

### 11.3.4. Elastic Net

### 11.3.5. Estandarización y regularización

### 11.3.6. Selección del parámetro de penalización

### 11.3.7. Ejemplo práctico guiado: comparación de regresiones regularizadas

Analizar el efecto de la penalización sobre coeficientes, error de validación y selección de variables.

## 11.4. Regresión logística y clasificación

### 11.4.1. Formulación de la clasificación binaria

### 11.4.2. Función logística

### 11.4.3. Odds y log-odds

### 11.4.4. Estimación e interpretación de coeficientes

### 11.4.5. Probabilidades y umbrales de decisión

### 11.4.6. Clasificación multiclase

### 11.4.7. Calibración de probabilidades

### 11.4.8. Ejemplo práctico guiado: clasificación de reclamos prioritarios

Estimar probabilidades, seleccionar un umbral operativo y explicar las variables más relevantes.

---

# Capítulo 12. Métodos supervisados avanzados y ensambles

## 12.1. Árboles de decisión

### 12.1.1. Particiones recursivas

### 12.1.2. Entropía y ganancia de información

### 12.1.3. Índice de Gini

### 12.1.4. Árboles de clasificación y regresión

### 12.1.5. Profundidad y complejidad

### 12.1.6. Poda

### 12.1.7. Interpretación de reglas

### 12.1.8. Ejemplo práctico guiado: árbol para priorización de incidentes

Entrenar, visualizar y podar un árbol, evaluando su claridad y capacidad de generalización.

## 12.2. Máquinas de soporte vectorial

### 12.2.1. Hiperplanos y fronteras de decisión

### 12.2.2. Margen máximo

### 12.2.3. Vectores de soporte

### 12.2.4. Margen blando

### 12.2.5. Funciones kernel

### 12.2.6. Parámetros de regularización y kernel

### 12.2.7. Escalado y costo computacional

### 12.2.8. Ejemplo práctico guiado: clasificación no lineal con SVM

Comparar kernels y analizar el efecto de sus hiperparámetros sobre la frontera de decisión.

## 12.3. Métodos de ensamble

### 12.3.1. Combinación de modelos

### 12.3.2. Bagging

### 12.3.3. Random Forest

### 12.3.4. Boosting

### 12.3.5. Gradient Boosting

### 12.3.6. Stacking

### 12.3.7. Ajuste de hiperparámetros

### 12.3.8. Ejemplo práctico guiado: competencia controlada de modelos

Comparar árboles, Random Forest y boosting mediante un protocolo común de validación.

## 12.4. Explicabilidad y aprendizaje distribuido

### 12.4.1. Interpretabilidad global y local

### 12.4.2. Importancia por permutación

### 12.4.3. Gráficos de dependencia parcial

### 12.4.4. Valores SHAP

### 12.4.5. Motivación del aprendizaje federado

### 12.4.6. Arquitecturas federadas

### 12.4.7. Privacidad, comunicación y limitaciones

### 12.4.8. Ejemplo práctico guiado: explicación de una predicción individual

Explicar la predicción de un ensamble y contrastarla con la importancia global de las variables.

---

# Capítulo 13. Aprendizaje no supervisado y descubrimiento de estructuras

## 13.1. Distancias, similitudes y representación

### 13.1.1. Objetivos del aprendizaje no supervisado

### 13.1.2. Distancia euclídea

### 13.1.3. Distancia Manhattan

### 13.1.4. Similitud coseno

### 13.1.5. Escalas y ponderación de variables

### 13.1.6. Datos mixtos

### 13.1.7. Ejemplo práctico guiado: comparación de similitudes entre observaciones

Analizar cómo cambian los vecinos y agrupamientos al modificar escalas o métricas.

## 13.2. Agrupamiento particional y jerárquico

### 13.2.1. Algoritmo K-means

### 13.2.2. Inicialización y convergencia

### 13.2.3. Selección del número de grupos

### 13.2.4. Clustering jerárquico

### 13.2.5. Métodos aglomerativos y divisivos

### 13.2.6. Tipos de enlace

### 13.2.7. Dendrogramas

### 13.2.8. Ejemplo práctico guiado: segmentación de patrones de consumo

Construir perfiles de grupos y comparar resultados de K-means y clustering jerárquico.

## 13.3. Métodos basados en densidad y representaciones neuronales

### 13.3.1. Concepto de densidad

### 13.3.2. DBSCAN

### 13.3.3. Ruido y formas arbitrarias

### 13.3.4. Sensibilidad a parámetros

### 13.3.5. Mapas autoorganizados

### 13.3.6. Proyección y visualización de prototipos

### 13.3.7. Ejemplo práctico guiado: detección de zonas de movilidad atípicas

Aplicar un método basado en densidad y distinguir grupos densos de observaciones aisladas.

### Actividad EMO [MOV-03]: segmentar zonas por patrón de movilidad

**Capacidad mínima:** construir y validar segmentos útiles a partir de variables geotemporales.

**Consigna:** definir características comparables por zona, aplicar al menos dos estrategias de agrupamiento y caracterizar los segmentos según demanda, temporalidad, conectividad u otra dimensión operativa.

**Modalidad de trabajo:** definición común de variables; ajuste, validación e interpretación individuales.

**Evidencia individual:** notebook con preprocesamiento, selección razonada de hiperparámetros, visualización de grupos y ficha interpretativa de cada segmento.

**Criterios de aprobación:**

- Las escalas y métricas son coherentes con las variables.
- La selección de grupos combina métricas, estabilidad y utilidad.
- La interpretación no confunde separación algorítmica con categorías reales.

**Aporte al laboratorio:** define perfiles de zonas que podrán utilizarse en el pronóstico y la recomendación.

## 13.4. Evaluación, interpretación y anomalías

### 13.4.1. Inercia

### 13.4.2. Coeficiente Silhouette

### 13.4.3. Índice Davies-Bouldin

### 13.4.4. Evaluación externa

### 13.4.5. Caracterización de clusters

### 13.4.6. Detección no supervisada de anomalías

### 13.4.7. Riesgos de sobreinterpretación

### 13.4.8. Ejemplo práctico guiado: validación de una segmentación

Combinar métricas, visualización y conocimiento del dominio para juzgar la utilidad de los grupos.

---

# Capítulo 14. Análisis y pronóstico de series temporales

## 14.1. Estructura de las series temporales

### 14.1.1. Índice temporal y frecuencia

### 14.1.2. Tendencia

### 14.1.3. Estacionalidad

### 14.1.4. Ciclos

### 14.1.5. Ruido

### 14.1.6. Valores faltantes y atípicos temporales

### 14.1.7. Descomposición

### 14.1.8. Ejemplo práctico guiado: descomposición de una serie de demanda

Identificar componentes y discutir qué patrones podrían ser predecibles.

## 14.2. Dependencia temporal y estacionariedad

### 14.2.1. Dependencia serial

### 14.2.2. Estacionariedad

### 14.2.3. Autocorrelación

### 14.2.4. Autocorrelación parcial

### 14.2.5. Transformaciones de varianza

### 14.2.6. Diferenciación regular y estacional

### 14.2.7. Ejemplo práctico guiado: transformación de una serie no estacionaria

Aplicar transformaciones y diferenciaciones y evaluar el resultado con gráficos y diagnósticos.

## 14.3. Modelos ARIMA

### 14.3.1. Modelos autorregresivos

### 14.3.2. Modelos de medias móviles

### 14.3.3. Modelos ARMA

### 14.3.4. Modelos ARIMA

### 14.3.5. Componentes estacionales

### 14.3.6. Selección de órdenes

### 14.3.7. Variables exógenas

### 14.3.8. Diagnóstico de residuos

### 14.3.9. Ejemplo práctico guiado: pronóstico de consumo de agua

Ajustar un modelo ARIMA o SARIMA, comprobar sus residuos y producir pronósticos con intervalos.

## 14.4. Evaluación de pronósticos

### 14.4.1. Horizonte de predicción

### 14.4.2. Pronósticos puntuales e intervalos

### 14.4.3. MAE, RMSE, MAPE y métricas escaladas

### 14.4.4. Validación walk-forward

### 14.4.5. Prevención de fuga temporal

### 14.4.6. Comparación con modelos de machine learning

### 14.4.7. Incertidumbre y actualización del modelo

### 14.4.8. Ejemplo práctico guiado: comparación de métodos de pronóstico

Comparar un baseline estacional, ARIMA y un modelo de aprendizaje automático mediante validación temporal.

### Actividad EMO [MOV-04]: pronosticar demanda por zona y franja horaria

**Capacidad mínima:** evaluar un pronóstico respetando el orden temporal y comparándolo con un baseline.

**Consigna:** seleccionar una zona o segmento, construir una serie regular, definir un horizonte operativo y comparar un baseline con un modelo ARIMA, SARIMA u otra alternativa pertinente mediante validación *walk-forward*.

**Modalidad de trabajo:** selección de casos en equipo; modelado, diagnóstico y conclusiones individuales.

**Evidencia individual:** notebook con particiones temporales, pronósticos, intervalos, métricas por horizonte y análisis de residuos o errores.

**Criterios de aprobación:**

- Ninguna transformación utiliza observaciones posteriores al instante pronosticado.
- El modelo se compara con un baseline adecuado a la frecuencia y estacionalidad.
- Se interpreta la incertidumbre y su efecto sobre una decisión de movilidad.

**Aporte al laboratorio:** aporta la estimación futura requerida para recomendar posicionamiento, capacidad o inspección.

---

# Laboratorio integrador 2. Análisis geotemporal y decisión en movilidad

**Etiqueta:** `[LAB · MOVILIDAD]`

**Actividades EMO integradas:** `MOV-01`, `MOV-02`, `MOV-03` y `MOV-04`.

**Propósito:** integrar exploración espacial, búsqueda sobre redes, segmentación y pronóstico para apoyar una decisión operativa de movilidad.

**Consigna integradora:**

1. Definir la granularidad espacial y temporal del problema.
2. Construir un diagnóstico de demanda o viajes con mapas y perfiles temporales.
3. Representar una parte de la red como grafo y comparar rutas o costos.
4. Agrupar zonas con patrones semejantes y justificar los segmentos.
5. Pronosticar demanda para al menos una zona o segmento.
6. Proponer una regla de posicionamiento, asignación o recorrido basada en la evidencia.

**Producto grupal:** notebook o aplicación reproducible con mapa, perfiles de zonas, pronóstico y recomendación.

**Evidencia individual:** análisis de una zona diferente, comparación de un algoritmo o modelo y explicación del impacto de la incertidumbre sobre la recomendación.

**Criterios de aprobación:**

- Se conserva una unidad geotemporal consistente en toda la cadena.
- Búsqueda, clustering y pronóstico responden a una misma decisión.
- Las comparaciones utilizan baselines y protocolos reproducibles.
- La recomendación reconoce límites de cobertura y sesgos de movilidad.

**Perspectiva de Ciencia de Datos:** integración, exploración, segmentación, validación temporal y visualización.

**Perspectiva de Inteligencia Artificial:** representación de grafos, heurísticas, predicción y selección de acciones.

---

# Parte IV. Aprendizaje profundo y datos no estructurados

# Capítulo 15. Redes neuronales, aprendizaje profundo y visión artificial

## 15.1. Fundamentos de redes neuronales

### 15.1.1. Neurona artificial

### 15.1.2. Perceptrón

### 15.1.3. Capas de entrada, ocultas y de salida

### 15.1.4. Pesos y sesgos

### 15.1.5. Funciones de activación

### 15.1.6. Propagación hacia adelante

### 15.1.7. Capacidad de representación

### 15.1.8. Ejemplo práctico guiado: construcción de una red neuronal mínima

Implementar una red pequeña y visualizar cómo aprende una frontera de decisión.

### Actividad EMO [VEG-01]: preparar un dataset de imágenes vegetales

**Capacidad mínima:** organizar imágenes, clases y particiones de forma reproducible y sin contaminación.

**Consigna:** inspeccionar las clases y metadatos, detectar duplicados o imágenes problemáticas, definir transformaciones básicas y construir particiones de entrenamiento, validación y prueba que respeten planta, captura o procedencia cuando esa información exista.

**Modalidad de trabajo:** auditoría inicial en equipo; partición, controles y documentación individuales.

**Evidencia individual:** notebook con distribución de clases, galería de control, reglas de inclusión y archivo reproducible de particiones.

**Criterios de aprobación:**

- Las imágenes similares o relacionadas no quedan repartidas indebidamente entre particiones.
- Las transformaciones preservan la señal visual relevante.
- El desbalance y las limitaciones de procedencia quedan documentados.

**Aporte al laboratorio:** establece el conjunto de imágenes y el protocolo de evaluación.

## 15.2. Entrenamiento de redes profundas

### 15.2.1. Funciones de pérdida

### 15.2.2. Descenso del gradiente

### 15.2.3. Retropropagación

### 15.2.4. Mini-batches, épocas y tasa de aprendizaje

### 15.2.5. Inicialización y normalización

### 15.2.6. Regularización y dropout

### 15.2.7. Early stopping

### 15.2.8. Aceleración mediante GPU

### 15.2.9. Ejemplo práctico guiado: diagnóstico del entrenamiento

Analizar curvas de pérdida y desempeño para detectar inestabilidad, sobreajuste o capacidad insuficiente.

### Actividad EMO [VEG-02]: entrenar y diagnosticar un baseline neuronal

**Capacidad mínima:** interpretar el proceso de entrenamiento y aplicar controles básicos de generalización.

**Consigna:** entrenar una red pequeña o un baseline equivalente, registrar pérdida y métricas por época y comparar al menos dos configuraciones de regularización, tasa de aprendizaje o *early stopping*.

**Modalidad de trabajo:** ejecución individual con puesta en común de diagnósticos.

**Evidencia individual:** historial de entrenamiento, curvas comparativas, configuración reproducible y diagnóstico escrito.

**Criterios de aprobación:**

- Las conclusiones se basan en curvas de entrenamiento y validación.
- Las configuraciones se comparan manteniendo constantes los demás factores relevantes.
- Se identifica sobreajuste, subajuste o inestabilidad y se propone una corrección plausible.

**Aporte al laboratorio:** crea el baseline y los criterios para decidir si un modelo más complejo aporta valor.

## 15.3. Imágenes digitales y redes convolucionales

### 15.3.1. Píxeles, canales y resolución

### 15.3.2. Tensores de imágenes

### 15.3.3. Convolución y filtros

### 15.3.4. Mapas de características

### 15.3.5. Padding y stride

### 15.3.6. Pooling

### 15.3.7. Arquitecturas convolucionales

### 15.3.8. Ejemplo práctico guiado: clasificación de imágenes vegetales

Entrenar una red convolucional sencilla y analizar errores por clase.

### Actividad EMO [VEG-03]: construir y evaluar una CNN

**Capacidad mínima:** implementar una red convolucional y analizar su comportamiento por clase.

**Consigna:** entrenar una CNN sencilla sobre las particiones definidas, compararla con el baseline y examinar matriz de confusión, métricas por clase y una galería de aciertos y errores.

**Modalidad de trabajo:** arquitectura base compartida; entrenamiento y análisis individuales.

**Evidencia individual:** notebook con arquitectura, parámetros principales, resultados comparativos y galería comentada de errores.

**Criterios de aprobación:**

- La evaluación utiliza exclusivamente las particiones establecidas.
- Se informan métricas por clase y no solo exactitud global.
- Los errores se relacionan con calidad de imagen, similitud visual o cobertura del dataset.

**Aporte al laboratorio:** aporta el primer clasificador visual específico del dominio.

## 15.4. Transferencia, evaluación y tareas avanzadas de visión

### 15.4.1. Aumento de datos

### 15.4.2. Transfer learning

### 15.4.3. Ajuste fino

### 15.4.4. Métricas para clasificación visual

### 15.4.5. Interpretación de modelos visuales

### 15.4.6. Introducción a detección de objetos

### 15.4.7. Introducción a segmentación

### 15.4.8. TensorFlow, Keras y PyTorch

### 15.4.9. Ejemplo práctico guiado: transferencia para diagnóstico de enfermedades

Adaptar una red preentrenada, comparar estrategias de congelamiento y evaluar su generalización.

### Actividad EMO [VEG-04]: aplicar transferencia y definir condiciones de uso

**Capacidad mínima:** adaptar un modelo preentrenado y decidir cuándo su predicción requiere revisión humana.

**Consigna:** comparar extracción de características y ajuste fino, incorporar aumento de datos solo en entrenamiento, evaluar calibración o confianza y proponer una regla de abstención o derivación.

**Modalidad de trabajo:** selección de arquitectura por equipo; experimentos, evaluación y regla de uso individuales.

**Evidencia individual:** notebook comparativo, matriz de confusión final, análisis de confianza y ficha breve del modelo.

**Criterios de aprobación:**

- El aumento de datos no modifica validación ni prueba.
- La comparación considera desempeño, costo y estabilidad.
- La regla de abstención se relaciona con errores observados y no con un umbral arbitrario.

**Aporte al laboratorio:** produce el modelo candidato y sus límites de uso.

---

# Laboratorio integrador 3. Diagnóstico visual de enfermedades vegetales

**Etiqueta:** `[LAB · SANIDAD VEGETAL]`

**Actividades EMO integradas:** `VEG-01`, `VEG-02`, `VEG-03` y `VEG-04`.

**Propósito:** construir y documentar un sistema de clasificación visual que compare un baseline, una CNN y transferencia de aprendizaje, con análisis explícito de errores y condiciones de uso.

**Consigna integradora:**

1. Auditar imágenes, etiquetas, duplicados y procedencia.
2. Fijar particiones y un protocolo reproducible.
3. Entrenar y diagnosticar un baseline.
4. Construir una CNN y analizar resultados por clase.
5. Aplicar transferencia de aprendizaje y comparar estrategias.
6. Diseñar una regla de abstención o revisión humana.
7. Preparar una ficha del modelo con población objetivo, límites y riesgos.

**Producto grupal:** prototipo de clasificación con galería de errores, comparación de modelos y ficha de uso.

**Evidencia individual:** análisis de una clase o subconjunto asignado, reproducción de un experimento y defensa de la regla de abstención.

**Criterios de aprobación:**

- Particiones, transformaciones y entrenamiento son reproducibles.
- La comparación incluye un baseline y métricas por clase.
- El análisis visual de errores respalda las decisiones metodológicas.
- Se explicitan los límites de generalización a imágenes de campo.

**Perspectiva de Ciencia de Datos:** calidad, partición, evaluación, visualización de errores y documentación.

**Perspectiva de Inteligencia Artificial:** arquitectura, entrenamiento, transferencia, confianza y comportamiento del sistema.

---

# Capítulo 16. Procesamiento del lenguaje natural y grandes modelos de lenguaje

## 16.1. Preparación y representación clásica de textos

### 16.1.1. Corpus, documentos, oraciones y tokens

### 16.1.2. Limpieza y normalización

### 16.1.3. Tokenización

### 16.1.4. Palabras vacías

### 16.1.5. Stemming y lematización

### 16.1.6. N-gramas

### 16.1.7. Bag of Words

### 16.1.8. TF-IDF

### 16.1.9. Ejemplo práctico guiado: representación de reclamos financieros

Preparar un corpus y comparar matrices Bag of Words y TF-IDF para una tarea de clasificación.

### Actividad EMO [REC-03]: representar textos con TF-IDF

**Capacidad mínima:** transformar textos en atributos numéricos sin utilizar información del conjunto de evaluación.

**Consigna:** construir un pipeline de normalización y TF-IDF, comparar al menos dos decisiones de tokenización o n-gramas y examinar términos relevantes y dimensionalidad resultante.

**Modalidad de trabajo:** vocabulario y variantes discutidos en equipo; ajuste y análisis individuales.

**Evidencia individual:** notebook con pipeline, comparación de representaciones, ejemplos de términos y verificación de que el vocabulario se ajusta solo con entrenamiento.

**Criterios de aprobación:**

- La normalización se justifica según el idioma y el objetivo.
- El vocabulario y los pesos se aprenden exclusivamente con entrenamiento.
- Se interpretan ventajas y pérdidas de información de las variantes.

**Aporte al laboratorio:** aporta la representación clásica y el baseline de texto.

## 16.2. Modelado y evaluación de textos

### 16.2.1. Similitud entre documentos

### 16.2.2. Clasificación de textos

### 16.2.3. Análisis de sentimiento

### 16.2.4. Extracción de información

### 16.2.5. Clases desbalanceadas en NLP

### 16.2.6. Métricas de clasificación

### 16.2.7. Evaluación cualitativa de errores

### 16.2.8. Ejemplo práctico guiado: clasificación automática de reclamos

Entrenar un modelo clásico, evaluar sus errores y proponer reglas de uso operativo.

### Actividad EMO [REC-04]: clasificar, priorizar y analizar errores

**Capacidad mínima:** entrenar un clasificador de texto, evaluarlo con el protocolo fijado y traducir sus errores a una regla de uso.

**Consigna:** comparar un baseline con al menos un modelo de clasificación, seleccionar un umbral o regla de priorización y realizar un análisis cualitativo de falsos positivos, falsos negativos y subgrupos relevantes.

**Modalidad de trabajo:** tabla comparativa grupal; modelo, errores y conclusiones individuales.

**Evidencia individual:** notebook con métricas, matriz de confusión, ejemplos anonimizados de errores, decisión de umbral y recomendación de supervisión.

**Criterios de aprobación:**

- Se respeta el protocolo definido en `REC-02`.
- Las métricas se acompañan con ejemplos y análisis por clase o subgrupo.
- La regla operativa refleja los costos de error y reconoce casos de baja confianza.

**Aporte al laboratorio:** produce el clasificador, la priorización y el análisis de errores final.

## 16.3. Embeddings, atención y Transformers

### 16.3.1. Limitaciones de las representaciones dispersas

### 16.3.2. Embeddings distribucionales

### 16.3.3. Representaciones contextuales

### 16.3.4. Modelos secuenciales

### 16.3.5. Mecanismos de atención

### 16.3.6. Arquitectura Transformer

### 16.3.7. Preentrenamiento y ajuste fino

### 16.3.8. Ejemplo práctico guiado: comparación de representaciones de texto

Comparar TF-IDF y embeddings contextuales en similitud o clasificación de reclamos.

## 16.4. Grandes modelos de lenguaje y aplicaciones generativas

### 16.4.1. Grandes modelos de lenguaje

### 16.4.2. Generación autoregresiva

### 16.4.3. Diseño de instrucciones o prompting

### 16.4.4. Aprendizaje en contexto

### 16.4.5. Generación aumentada con recuperación

### 16.4.6. Integración mediante APIs y aplicaciones

### 16.4.7. Alucinaciones y evaluación de respuestas

### 16.4.8. Sesgos, privacidad y propiedad intelectual

### 16.4.9. Documentación de limitaciones y supervisión humana

### 16.4.10. Ejemplo práctico guiado: asistente para consulta de reclamos

Diseñar un prototipo que recupere antecedentes, genere una respuesta trazable y aplique controles de seguridad y revisión humana.

---

# Laboratorio integrador 4. Clasificación y priorización de reclamos financieros

**Etiqueta:** `[LAB · RECLAMOS]`

**Actividades EMO integradas:** `REC-01`, `REC-02`, `REC-03` y `REC-04`.

**Propósito:** desarrollar una cadena de procesamiento de texto que convierta reclamos abiertos en categorías o prioridades útiles, con evaluación reproducible y revisión crítica de errores.

**Consigna integradora:**

1. Construir y documentar el corpus analítico.
2. Definir objetivo, particiones, baseline, métricas y costos de error.
3. Preparar una representación TF-IDF reproducible.
4. Entrenar y comparar modelos de clasificación.
5. Analizar errores por clase, subgrupo y tipo de redacción.
6. Proponer una regla de priorización, abstención o revisión humana.
7. Comparar, como extensión, TF-IDF con embeddings contextuales o un modelo preentrenado.

**Producto grupal:** notebook o prototipo de clasificación y exploración de reclamos con reporte de desempeño y errores.

**Evidencia individual:** análisis de un conjunto de errores asignado, reproducción de una comparación y defensa del umbral o regla de uso.

**Criterios de aprobación:**

- El corpus y las particiones son trazables y no contienen fugas evidentes.
- El modelo se compara con un baseline mediante métricas adecuadas.
- El análisis cualitativo complementa la evaluación cuantitativa.
- La priorización conserva supervisión en situaciones ambiguas o sensibles.

**Perspectiva de Ciencia de Datos:** calidad del corpus, diseño experimental, evaluación y comunicación.

**Perspectiva de Inteligencia Artificial:** representación del lenguaje, clasificación, confianza y asistencia a decisiones.

---

# Apéndices sugeridos

## Apéndice A. Fundamentos matemáticos

### A.1. Álgebra lineal

### A.2. Cálculo diferencial

### A.3. Optimización

### A.4. Notación probabilística y estadística

### A.5. Ejemplo práctico guiado: operaciones matemáticas empleadas en un modelo

Resolver un ejercicio integrador de vectores, matrices, derivadas y optimización.

## Apéndice B. Guía de programación científica

### B.1. Tipos y estructuras de datos

### B.2. Funciones y módulos

### B.3. Operaciones vectorizadas

### B.4. Manejo de errores

### B.5. Pruebas y documentación

### B.6. Ejemplo práctico guiado: implementación reproducible de un análisis

Transformar un cuaderno exploratorio en funciones reutilizables y verificables.

## Apéndice C. Ética, gobernanza y documentación de modelos

### C.1. Ciclo de vida responsable

### C.2. Privacidad y protección de datos

### C.3. Equidad y análisis de sesgos

### C.4. Transparencia y explicabilidad

### C.5. Supervisión y rendición de cuentas

### C.6. Fichas de datos y tarjetas de modelos

### C.7. Ejemplo práctico guiado: auditoría de un sistema de IA

Completar una ficha de riesgos, controles, limitaciones y responsables para uno de los proyectos integradores.

## Apéndice D. Proyectos integradores

### D.1. Movilidad urbana y transporte

#### D.1.1. Fuente abierta, licencia y versión del dataset

#### D.1.2. Unidad espacial y temporal

#### D.1.3. Diccionario de variables

#### D.1.4. Actividades `MOV-01` a `MOV-04`

#### D.1.5. Guía del laboratorio de movilidad

### D.2. Calidad, consumo y gestión del agua

#### D.2.1. Fuente abierta, licencia y versión del dataset

#### D.2.2. Unidad de análisis y contexto operativo

#### D.2.3. Diccionario de variables y límites físicos

#### D.2.4. Actividades `AGUA-01` a `AGUA-04`

#### D.2.5. Guía del laboratorio de agua

### D.3. Reclamos financieros y procesamiento de texto

#### D.3.1. Fuente abierta, licencia y versión del corpus

#### D.3.2. Unidad de análisis, etiquetas y anonimización

#### D.3.3. Diccionario de campos y criterios de exclusión

#### D.3.4. Actividades `REC-01` a `REC-04`

#### D.3.5. Guía del laboratorio de reclamos

### D.4. Diagnóstico visual de enfermedades vegetales

#### D.4.1. Fuente abierta, licencia y versión del dataset

#### D.4.2. Clases, procedencia y condiciones de captura

#### D.4.3. Particiones, duplicados y transformaciones permitidas

#### D.4.4. Actividades `VEG-01` a `VEG-04`

#### D.4.5. Guía del laboratorio de sanidad vegetal

### D.5. Rúbrica común de evaluación

#### D.5.1. Reproducibilidad y trazabilidad

#### D.5.2. Corrección metodológica

#### D.5.3. Interpretación y relación con la decisión

#### D.5.4. Análisis de incertidumbre, sesgos y limitaciones

#### D.5.5. Comunicación y defensa individual

### D.6. Ejemplo práctico guiado: defensa integral de un proyecto

Preparar una entrega que incluya formulación, calidad de datos, análisis, modelado, validación, interpretación, riesgos y comunicación.

---

# Matriz general de experiencias obligatorias

| Código | Dataset | Capítulo y sección | Capacidad demostrada | Aporte al laboratorio |
|---|---|---|---|---|
| `AGUA-01` | Agua | 2.1 | Formulación del problema y la decisión | Alcance y criterio de éxito |
| `AGUA-02` | Agua | 3.2 | Auditoría, limpieza e imputación | Dataset depurado |
| `AGUA-03` | Agua | 4.1 | Exploración e interpretación de anomalías | Diagnóstico e hipótesis |
| `AGUA-04` | Agua | 5.3 | Actualización de riesgo y priorización | Indicador y regla de acción |
| `MOV-01` | Movilidad | 4.3 | Visualización geotemporal | Diagnóstico de zonas y períodos |
| `MOV-02` | Movilidad | 7.3 | Grafos, costos y heurísticas | Rutas o desplazamientos |
| `MOV-03` | Movilidad | 13.3 | Segmentación de zonas | Perfiles operativos |
| `MOV-04` | Movilidad | 14.4 | Pronóstico y validación temporal | Demanda futura |
| `REC-01` | Reclamos | 3.3 | Construcción reproducible del corpus | Datos y etiquetas |
| `REC-02` | Reclamos | 9.4 | Protocolo y métricas de evaluación | Diseño experimental |
| `REC-03` | Reclamos | 16.1 | Representación TF-IDF | Atributos y baseline |
| `REC-04` | Reclamos | 16.2 | Clasificación, umbral y errores | Priorización operativa |
| `VEG-01` | Sanidad vegetal | 15.1 | Auditoría y partición de imágenes | Dataset y evaluación |
| `VEG-02` | Sanidad vegetal | 15.2 | Entrenamiento y diagnóstico | Baseline neuronal |
| `VEG-03` | Sanidad vegetal | 15.3 | CNN y análisis por clase | Clasificador específico |
| `VEG-04` | Sanidad vegetal | 15.4 | Transferencia y abstención | Modelo candidato y límites |

# Secuencia de integración

| Nivel | Función pedagógica | Alcance | Evidencia |
|---|---|---|---|
| Ejemplo práctico guiado | Aprender una técnica inmediatamente después de la teoría | Una sección | Resultado breve, resuelto o parcialmente resuelto |
| Actividad EMO | Demostrar una capacidad mínima sobre un dataset real | Una o dos capacidades relacionadas | Evidencia individual reproducible |
| Laboratorio integrador | Combinar cuatro EMO en una decisión de mayor alcance | Varios capítulos | Producto grupal más evidencia y defensa individuales |
| Proyecto de profundización | Construir una solución más abierta sobre un caso elegido | Curso completo | Prototipo, repositorio, informe y defensa |

La secuencia recomendada es:

> teoría → ejemplo guiado → actividad EMO → retroalimentación → laboratorio integrador → proyecto de profundización

# Criterios de uso de los ejemplos prácticos guiados

Los ejemplos prácticos guiados deberán:

1. Retomar exclusivamente conocimientos desarrollados hasta la sección correspondiente.
2. Utilizar datos reales o una versión didáctica fiel a un problema real.
3. Incluir una pregunta concreta, un procedimiento reproducible y una interpretación.
4. Evitar ejercicios puramente mecánicos sin relación con una decisión o problema.
5. Señalar supuestos, limitaciones y posibles fuentes de error.
6. Producir una evidencia verificable: cálculo, tabla, gráfico, modelo, algoritmo o decisión justificada.
7. Contribuir, cuando sea posible, a uno de los cuatro proyectos integradores del libro.

# Criterios comunes para las actividades EMO

1. Cada código representa una capacidad obligatoria y una evidencia individual.
2. El trabajo puede comenzar en grupo, pero cada estudiante debe ejecutar, interpretar o defender una variante propia.
3. Las consignas y datos mínimos son comunes para permitir comparaciones justas.
4. Los criterios de aprobación evalúan corrección y comprensión, no una métrica competitiva.
5. Una EMO puede recuperarse de manera independiente sin repetir todo el laboratorio.
6. Los notebooks deben registrar versión de datos, semillas, dependencias y decisiones relevantes.
7. Toda actividad debe incluir al menos una limitación, un posible sesgo o una condición de uso.
8. La aprobación de las 16 EMO es requisito para acreditar la experiencia con los cuatro tipos de datos.

# Criterios comunes para los laboratorios integradores

1. Cada laboratorio debe reutilizar las evidencias generadas por sus cuatro EMO.
2. El producto grupal debe mostrar la cadena `datos → evidencia → modelo o algoritmo → decisión → comunicación`.
3. La evaluación debe diferenciar los aportes de Ciencia de Datos y de Inteligencia Artificial sin duplicar entregas.
4. Cada estudiante debe presentar una evidencia individual y responder preguntas sobre el producto completo.
5. El laboratorio no obliga a aplicar técnicas que no sean pertinentes al tipo de dato.
6. Las extensiones avanzadas se consideran profundización y no sustituyen las capacidades mínimas.

