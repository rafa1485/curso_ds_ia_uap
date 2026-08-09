---
title: "Introducción a la Ciencia de Datos"
subtitle: "De una necesidad a evidencia útil para decidir"
course: "Data Science"
week: 1
class: 1
language: es
---

# Introducción a la Ciencia de Datos

## De una necesidad a evidencia útil para decidir

**Semana 1 · Clase 1**

<!-- Notas docentes: La clase comienza por decisiones, representaciones y evidencia, no por algoritmos o herramientas. -->

---

# Propósito de la clase

Comprender la Ciencia de Datos como un proceso interdisciplinario que transforma observaciones en evidencia para apoyar decisiones responsables.

Al finalizar, podremos:

- distinguir dato, representación, modelo, evidencia y decisión;
- diferenciar descripción, predicción y prescripción;
- formular unidad, población, alcance y horizonte antes de modelar;
- explicar workflow, KDD, CRISP-DM, procedencia y reproducibilidad;
- especificar un problema de movilidad con unidad **zona-franja**.

---

# Pregunta de apertura

> Una empresa de movilidad quiere “mejorar el servicio”.

¿Qué debemos precisar antes de abrir un dataset?

- ¿Qué situación se desea modificar?
- ¿Quién utilizará el resultado?
- ¿Sobre qué unidad se decidirá?
- ¿Qué acción está disponible?
- ¿Qué datos existirán a tiempo?
- ¿Cómo se medirá el valor?

---

# ¿Qué es la Ciencia de Datos?

Campo interdisciplinario que desarrolla métodos para:

1. obtener conocimiento a partir de datos;
2. comunicar evidencia sobre un fenómeno;
3. apoyar decisiones bajo objetivos y restricciones.

No se reduce a programar, graficar, entrenar modelos o acumular datos. Su producto puede ser un inventario, auditoría, análisis, estimación, visualización o recomendación.

**La pregunta y la decisión determinan el producto apropiado.**

---

# Los datos representan, no reproducen

Un dato es un registro producido por un proceso de observación situado.

**Diagrama:** `fenómeno → proceso de observación → registro`, con una salida lateral que muestra lo que puede quedar fuera: contexto, silencios, error y selección.

Ejemplo:

`demoras en la ciudad → sensor / regla / canal → hora / GPS / reclamo`

Preguntas mínimas:

- ¿Qué representa?
- ¿Cómo se obtuvo?
- ¿Qué no observa?
- ¿Cuándo estuvo disponible?

---

# De datos a conocimiento

**Diagrama:** `datos → información → conocimiento → decisión`.

| Nivel | Significado | Operación principal |
|---|---|---|
| Datos | Observaciones codificadas | Registrar |
| Información | Datos organizados en contexto | Organizar |
| Conocimiento | Patrones y reglas de uso | Interpretar |
| Decisión | Selección de una acción | Deliberar |

Cada transición agrega contexto, pero también supuestos, pérdidas y posibles sesgos. La **trazabilidad** permite reconstruirla.

---

# De la necesidad a la decisión

**Diagrama:** `necesidad → pregunta → datos → análisis → evidencia → decisión humana → impacto`.

## Correspondencia hacia adelante

La tarea debe producir evidencia utilizable por una acción real.

## Correspondencia hacia atrás

La decisión define unidad, oportunidad, evaluación y datos necesarios.

**Un modelo es un componente de la cadena, no la decisión.**

---

# El ciclo aprende y vuelve atrás

**Diagrama circular:** `formular → obtener y representar → analizar y evaluar → revisar y decidir → observar impacto → formular`, con retornos desde evaluación hacia formulación y datos.

- Explorar puede revelar que la pregunta no es medible.
- Evaluar puede mostrar que no se supera el baseline.
- Usar puede cambiar el proceso que genera datos.

> La organización define quién aprueba, ejecuta, revisa y puede detener el sistema.

---

# Taxonomía de preguntas analíticas

| Objetivo | Pregunta | Ejemplo en movilidad |
|---|---|---|
| Describir | ¿Qué ocurrió? | ¿Dónde y cuándo hubo demoras? |
| Diagnosticar | ¿Qué se asocia? | ¿Qué acompaña demoras mayores? |
| Predecir | ¿Qué valor no conocemos? | ¿Qué demanda tendrá cada zona-franja? |
| Prescribir | ¿Qué acción conviene? | ¿Cómo reasignar vehículos factibles? |
| Monitorear | ¿Qué está cambiando? | ¿Se degradó la cobertura o el modelo? |

Pueden conectarse, pero requieren evidencia y evaluación diferentes.

---

# Describir: resumir lo observado

Una descripción estima propiedades de observaciones y grupos:

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\qquad
\widehat{p}=\frac{1}{n}\sum_{i=1}^{n}\mathbb{1}(y_i=1)
$$

- **Productos:** frecuencias, medias, cuantiles, distribuciones, segmentos y visualizaciones.
- **Movilidad:** viajes, demora mediana y espera extrema por zona y franja observada.

**Una asociación descriptiva no demuestra causa ni anticipa por sí sola.**

---

# Predecir: estimar lo no observado

Una predicción estima un resultado desconocido, futuro o costoso de medir:

$$
\widehat{P}(Y\mid X)
\qquad\text{o}\qquad
\widehat{\mathbb{E}}[Y\mid X]
$$

- Las entradas deben existir en el momento real de uso.
- La evaluación utiliza casos no usados para ajustar.
- La partición debe respetar tiempo, grupos y duplicados.
- El desempeño se compara con un baseline pertinente.

> ¿Qué demanda tendrá cada zona durante la próxima franja?

---

# Describir no es predecir

**Diagrama comparativo:** una tarjeta de descripción, que resume casos observados, conduce solo como hipótesis a una tarjeta de predicción, que estima casos no observados.

| Descripción | Predicción |
|---|---|
| Resume casos observados | Estima casos no observados |
| Media, cuantiles, distribución | Probabilidad condicional, error futuro |
| ¿Dónde ocurrieron demoras? | ¿Qué zona-franja tendrá demanda alta? |

Una buena explicación del pasado no implica bajo error sobre periodos posteriores.

---

# Predecir no es decidir

**Diagrama:** `predicción e incertidumbre → comparación de acciones, costos y restricciones → responsable humano`.

$$
a^*=\arg\max_{a\in\mathcal A}\mathbb E[U(a,S)\mid X]
$$

- El modelo informa.
- La política compara.
- La persona autorizada aprueba, modifica o rechaza.

> La autoridad humana efectiva requiere tiempo, información y poder real para contradecir o detener la recomendación.

---

# Una disciplina interdisciplinaria

**Diagrama radial:** estadística, matemática, computación, ingeniería, conocimiento del dominio y comunicación convergen en evidencia útil y confiable.

| Perspectiva | Contribución |
|---|---|
| Estadística | Variabilidad e inferencia |
| Matemática | Objetivos y restricciones |
| Computación | Representación y escala |
| Ingeniería | Pruebas y operación |
| Dominio | Significado y plausibilidad |
| Comunicación | Comprensión y uso |

Una perspectiva aislada puede optimizar la parte equivocada.

---

# Formular antes de modelar

**Diagrama:** `necesidad real → pregunta analítica → tarea computacional`, con una flecha de retorno: “¿sirve para decidir?”.

Ejemplo:

`reducir esperas → demanda por zona-franja → agregar o predecir`

> Si no podemos explicar quién decide, sobre qué unidad, con qué información, para cuándo y con qué propósito, la formulación aún no está completa.

---

# Especificación compacta del problema

$$
\mathcal P=(U,\mathcal R,O,X,Y,A,H,C)
$$

- $U$: unidad de análisis.
- $\mathcal R$: población objetivo.
- $O$: objetivo del proyecto.
- $X$: entradas disponibles.
- $Y$: resultado de interés.
- $A$: acciones posibles.
- $H$: horizonte temporal.
- $C$: restricciones.
- Usuario, valor y responsables completan la ficha.

Cuatro pruebas: **observabilidad, accionabilidad, disponibilidad temporal y contrafactual**: “¿qué haríamos si la respuesta fuera distinta?”.

---

# Unidad, población y alcance

- **Unidad $U$:** entidad elemental descrita, predicha o decidida; define el significado de una fila.
- **Población $\mathcal R$:** unidades sobre las que se desea generalizar o actuar; no equivale a la muestra observada.
- **Alcance:** periodos, lugares, casos, usuarios, acciones y exclusiones autorizadas.

Si la acción reasigna recursos entre zonas por franja, la evidencia final debe conservar la unidad **zona-franja**. Las predicciones por viaje requieren una agregación explícita.

`población objetivo ≠ muestra disponible ≠ población futura de uso`

---

# Horizonte y disponibilidad: reconstruir el reloj

**Diagrama temporal:** histórico y entradas conocidas conducen al corte $t_0$; allí ocurre la decisión. La franja objetivo y el resultado se encuentran después del corte y no pueden usarse como entradas.

`histórico → corte t₀ → franja objetivo → resultado`

- $X$: conocido y recibido antes de $t_0$.
- Decisión: tomada en $t_0$.
- $Y$: observado después de $t_0$.

Evaluar con la información disponible retrospectivamente puede sobrestimar lo que el sistema sabía al decidir.

---

# Workflow de un proyecto de datos

**Diagrama iterativo:**

1. Formular decisión y éxito.
2. Obtener e inventariar.
3. Preparar la representación.
4. Analizar o modelar.
5. Evaluar y contrastar.
6. Comunicar o integrar con autoridad y monitoreo.
7. Volver a formular con la evidencia de uso.

Baseline, criterios de éxito y protocolo de evaluación se fijan antes de comparar resultados finales.

---

# Puertas y artefactos: aprender antes de escalar

| Puerta | Evidencia mínima | Artefacto vivo |
|---|---|---|
| Formular → datos | Unidad, alcance, autoridad y valor acordados | Ficha del problema |
| Datos → análisis | Cobertura, licencia, calidad y tiempo conocidos | Inventario + diccionario |
| Análisis → uso | Baseline superado y riesgos aceptables | Registro de experimento |
| Uso → escala | Utilidad, carga y fallos observados | Plan de monitoreo y retirada |

Un **producto mínimo evaluable** es el artefacto más pequeño que permite probar la incertidumbre capaz de invalidar el proyecto.

**Continuar, modificar, escalar o detener son resultados legítimos.**

---

# KDD: del dato al conocimiento validado

**Diagrama iterativo:** `selección → preprocesamiento → transformación → minería de datos → interpretación y evaluación`, con retorno hacia preprocesamiento.

- La minería es una etapa dentro de KDD, no un sinónimo del proceso completo.
- El preprocesamiento estudia calidad, faltantes, errores, duplicados y consistencia.
- La transformación cambia la representación con supuestos explícitos.
- La interpretación determina validez, novedad, comprensión y utilidad.

Evitar el salto: `resultado → patrón → hallazgo validado → regla aprobada`.

---

# CRISP-DM: organizar el proyecto completo

**Diagrama circular:** `comprensión del problema → comprensión de datos → preparación → modelado → evaluación → despliegue o entrega → comprensión del problema`.

- Comienza por el problema, no por el modelo.
- Evalúa desempeño técnico y correspondencia con el objetivo.
- Despliegue puede ser informe, tablero, API o regla operativa.
- Operación, monitoreo, incidentes y retirada retroalimentan el ciclo.

**CRISP-DM no termina al publicar un modelo.**

---

# Estructura de los datos

| Tipo | Organización | Ejemplo y decisión de representación |
|---|---|---|
| Estructurados | Esquema explícito, filas, columnas y claves | Viajes SQL; validar unidad, tipos y cardinalidad |
| Semiestructurados | Claves o marcas con esquema flexible | Eventos JSON; distinguir ausente, nulo y lista vacía |
| No estructurados | Sin variables tabulares inmediatas | Texto, audio o imagen; construir una representación |

Un esquema válido no garantiza significado correcto; y “no estructurado” no significa carente de estructura interna.

---

# De fuentes heterogéneas a una tabla analítica

**Diagrama:** viajes con unidad viaje, clima con unidad estación-hora y zonas con unidad polígono-versión pasan por reglas explícitas de agregación, unión, filtrado y corte para producir una tabla analítica cuya fila es zona-franja.

`fuentes → reglas explícitas → tabla analítica zona-franja`

- La tabla analítica deriva de fuentes: no las reemplaza.
- Cada unión declara claves, cardinalidad, cobertura y fecha de corte.
- Cambiar la cantidad de filas puede cambiar la población o la unidad.
- La tabla conserva claves y procedencia.

---

# Fuentes: inventariar antes de integrar

| Fuente | Unidad original | Acceso | Riesgo principal |
|---|---|---|---|
| Viajes | viaje | base o archivo | operadores no cubiertos |
| GPS | dispositivo-evento | flujo o API | latencia, deriva y pérdida |
| Clima | estación-hora | API | desfase horario y distancia |
| Zonas | polígono-versión | archivo geográfico | límites modificados |
| Calendario | día | archivo o tabla | definición local |

Ficha mínima:

`propietario · propósito original · unidad · cobertura · captura · formato · frecuencia · licencia · sensibilidad · calidad · cambios`

---

# Procedencia: ejes distintos, preguntas distintas

**Diagrama de cuatro ejes independientes:**

1. **Mecanismo de generación:** observacional / experimental / simulado.
2. **Propósito de recolección:** primario para el proyecto / secundario, creado con otro propósito.
3. **Acceso y gobernanza:** abierto / privado / restringido.
4. **Linaje:** origen → extracción → transformación → producto.

No son categorías excluyentes entre ejes. Un dato puede ser **observacional, secundario y privado** a la vez. Cada eje implica límites de inferencia, uso y auditoría diferentes.

---

# Big Data: seis V, seis diagnósticos

**Diagrama radial:** seis dimensiones convergen en el desafío de datos.

| Dimensión | Pregunta de diagnóstico |
|---|---|
| Volumen | ¿Cuánto se almacena y procesa? |
| Velocidad | ¿Con qué ritmo y latencia llega? |
| Variedad | ¿Qué formatos, fuentes y estructuras se integran? |
| Veracidad | ¿Qué confiabilidad e incertidumbre posee? |
| Valor | ¿Mejora una decisión? |
| Variabilidad | ¿Cómo cambian significado y distribución? |

**Escala no corrige semántica: más datos del concepto equivocado siguen siendo equivocados.**

---

# Herramientas y reproducibilidad

| Entornos | Artefactos | Controles |
|---|---|---|
| Python, R, SQL, Jupyter, Quarto | Código, datos, configuración, resultados, documentación | Versiones, checksums, pruebas, semillas, decisiones |

Cadena reproducible:

`fuente identificada → transformación versionada → experimento registrado → resultado reconstruible`

- Una semilla ayuda, pero no sustituye datos, entorno y partición versionados.
- Un notebook debe ejecutarse de principio a fin en un entorno limpio.
- La herramienta se elige por el ciclo de vida y el equipo, no por preferencia personal.

---

# Caso movilidad: formulación coherente

## Decisión operativa

Antes de cada franja, el responsable decide si reasigna vehículos entre zonas.

- **Unidad:** zona-franja.
- **Población:** zonas operadas en condiciones normales.
- **Horizonte:** próxima franja de 30 minutos.
- **Resultado:** demanda y espera por zona-franja.
- **Acciones:** mantener o proponer traslados factibles.
- **Restricciones:** capacidad, distancia, seguridad y cobertura.
- **Valor:** reducir espera extrema sin aumentar cancelaciones.
- **Autoridad:** responsable de operaciones.

**La unidad coincide con el nivel de predicción y de reasignación.**

---

# Movilidad: evidencia, recomendación y autoridad

**Diagrama:** `viajes, GPS, clima y zonas → construir zona-franja → demanda esperada e incertidumbre → opciones factibles y consecuencias → responsable decide → acción en la flota o mantener estado`. El impacto observado retroalimenta la construcción y evaluación.

## Límite de automatización

El sistema:

- recomienda opciones;
- comunica incertidumbre;
- puede abstenerse ante datos insuficientes o riesgo alto;
- no ejecuta traslados;
- no reemplaza protocolos de seguridad.

La autoridad final permanece en el responsable de operaciones.

---

# Del caso amplio a tareas concretas

| Objetivo | Tarea sobre zona-franja | Producto y evaluación |
|---|---|---|
| Describir | Agregar viajes, espera y oferta observada | Perfil por zona-franja |
| Predecir | Estimar demanda o espera de la próxima franja | Pronóstico vs. baseline temporal |
| Prescribir | Comparar reasignaciones factibles | Opciones, utilidad y restricciones |
| Monitorear | Detectar cambio en datos, error e impacto | Alertas, revisión o retirada |

Los eventos de viaje se agregan a zona-franja; el resultado no se presenta como una decisión por viaje individual.

---

# Fuga temporal: saber hoy lo que mañana ocurrió

**Diagrama temporal:** para decidir a las 09:00 sobre la franja 09:00–09:30, son válidos el GPS recibido hasta las 08:55, calendario y flota disponible. Son fuga los viajes completados a las 09:20 y la demanda total de la franja.

| Disponible al decidir | Conocido después: fuga |
|---|---|
| GPS recibido hasta 08:55 | Viajes completados a las 09:20 |
| Calendario | Demanda total 09:00–09:30 |
| Flota disponible | Espera final de la franja |

Reconstruir qué eventos habían sido **recibidos**, no solo cuáles ocurrieron antes. Tiempo de evento, recepción y decisión son relojes distintos.

---

# Actividad guiada: ficha del problema

En equipos, completar para movilidad:

1. necesidad, usuario, responsable y personas afectadas;
2. unidad zona-franja, población, alcance y exclusiones;
3. decisión, acciones permitidas y autoridad final;
4. fecha de corte, horizonte, entradas disponibles y resultado;
5. pregunta descriptiva, predictiva y prescriptiva;
6. fuentes, procedencia y regla de integración;
7. baseline, valor, restricciones y condición de detención;
8. un riesgo de fuga temporal y su control.

**Tiempo sugerido:** 30 minutos de trabajo + 10 minutos de contraste.

---

# Criterios de revisión

La ficha es adecuada si:

- la unidad **zona-franja** coincide con pregunta, tabla y acción;
- población, alcance, horizonte y exclusiones son verificables;
- cada entrada existe y puede recibirse antes de decidir;
- descripción, predicción y prescripción no se confunden;
- las fuentes conservan procedencia y reglas de integración;
- el baseline representa una alternativa realista;
- valor, riesgos y criterios de detención están explícitos;
- una persona con autoridad aprueba, modifica o rechaza la acción.

**Entregable:** ficha de una página + diagrama `necesidad → evidencia → decisión → impacto`.

---

# Puesta en común

Cada equipo presenta en un minuto:

1. la decisión y quién conserva autoridad;
2. la unidad, el corte temporal y el horizonte;
3. el baseline y la métrica de valor;
4. el supuesto que podría invalidar el proyecto.

Preguntas para contrastar:

- ¿La evidencia llega antes y a la misma granularidad que la decisión?
- ¿Qué representa la muestra y qué zonas quedan fuera?
- ¿Qué resultado justificaría modificar o detener el proyecto?

---

# Síntesis: siete ideas para conservar

1. Los datos son representaciones parciales producidas por procesos.
2. La Ciencia de Datos construye evidencia, no solo modelos.
3. Describir, predecir y decidir son problemas distintos.
4. Unidad, población, alcance y horizonte preceden al algoritmo.
5. Workflow, KDD y CRISP-DM son iterativos y trazables.
6. Procedencia y reproducibilidad sostienen lo que podemos afirmar.
7. La autoridad y responsabilidad pertenecen a personas y organizaciones.

> Primero se diseña la decisión y la evidencia necesaria; después se eligen datos, métodos y herramientas.

---

# Síntesis visual: la cadena completa

**Diagrama:**

`necesidad y alcance → unidad, población y horizonte → fuentes y procedencia → representación analítica → evidencia evaluada → decisión autorizada`

La decisión conduce a `impacto → monitoreo → aprendizaje`, que vuelve a la necesidad. Tres controles acompañan la cadena:

- pregunta y valor;
- calidad y licencia;
- baseline y riesgos.

**Cada flecha es una decisión documentable; cada retorno es una oportunidad de aprender.**

---

# Lecturas y recursos

## Lectura principal

- [Capítulo 1. Ciencia de Datos e Inteligencia Artificial](../../../Libro/Capitulo_01_Ciencia_de_Datos_e_IA.md): secciones 1.1.1, 1.1.4, 1.1.5 y 1.1.6.
- [Capítulo 2. Ciclo de vida de un proyecto basado en datos](../../../Libro/Capitulo_02_Ciclo_de_vida_de_un_proyecto_de_datos.md): secciones 2.1 a 2.4, con énfasis en 2.1.3, 2.2.1, 2.2.2, 2.3 y 2.4.

## Para continuar

- Revisar los glosarios de ambos capítulos.
- Completar la ficha inicial del caso de movilidad.
- Dibujar el linaje de una fuente hasta la unidad zona-franja.
