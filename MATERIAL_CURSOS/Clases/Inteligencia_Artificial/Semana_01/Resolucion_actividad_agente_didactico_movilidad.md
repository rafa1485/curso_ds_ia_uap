# Resolución de la actividad: agente didáctico de movilidad

## Alcance y necesidad

Esta resolución especifica un **asistente operativo didáctico** para una zona-hora simulada de Nueva York. El agente combina la actividad histórica de *pickups* de Yellow Taxi reportados por TLC, la zona, la hora y el clima disponible para recomendar `OBSERVAR`, `MONITOREAR` o `RECOMENDAR_REFUERZO`. Si la evidencia es insuficiente o inválida, conserva `ABSTENERSE` como salida excepcional de seguridad. Su finalidad es practicar los conceptos de agente, racionalidad, PEAS, percepción, acción y propiedades del ambiente; no demostrar una mejora operativa real.

El sistema es **solo recomendador**: comunica una acción sugerida, su evidencia, su explicación y sus limitaciones a una persona responsable. La prioridad se conserva internamente para decidir y auditar. El agente no traslada vehículos, no asigna conductores, no modifica rutas y no controla una flota.

> **Límite de interpretación indispensable**
>
> **TLC registra viajes realizados y reportados. No registra la demanda total, las solicitudes no atendidas, el tiempo de espera ni los vehículos libres.** Un conteo de *pickups* es actividad observada, no demanda completa ni necesidad insatisfecha. **NOAA aporta observaciones de una estación meteorológica; no representa el clima espacial completo de todas las zonas de la ciudad.** Por ello, este prototipo no puede afirmar que conoce la demanda real, que una zona tiene pasajeros esperando o que un refuerzo reducirá la espera.

> **Límite de oportunidad de los datos**
>
> **Los archivos de viajes NYC TLC empleados en el curso son publicaciones históricas, no un flujo de eventos disponible en tiempo real.** En una aplicación real, el agente no podría leer estos archivos para reevaluar hora por hora la ciudad ni reaccionar inmediatamente a los viajes que acaban de ocurrir. Para practicar el ciclo percepción-acción se adopta una suposición exclusivamente didáctica: una reproducción histórica o *replay* revela al agente los registros al cierre de cada hora simulada. La información acumulada hasta la hora $h$ se usa para recomendar una acción para la hora siguiente, $h+1$.

$$
\text{datos revelados hasta el cierre de }h
\longrightarrow
\text{recomendación simulada para }h+1.
$$

Esta suposición no transforma la fuente TLC en un sensor en vivo ni demuestra que el prototipo pueda desplegarse operacionalmente. Un sistema real requeriría fuentes con latencia conocida y suficiente, además de datos sobre solicitudes, flota, espera, tráfico y ejecución.

### Cuatro tiempos que no deben confundirse

| Tiempo | Significado | Tratamiento en el ejercicio |
|---|---|---|
| **Tiempo del evento** | Momento reportado en que comenzó o terminó el viaje | Ordena los viajes dentro de la reproducción histórica |
| **Tiempo de publicación real** | Momento posterior en que TLC pone el archivo histórico a disposición | Impide afirmar que la fuente sirve para decisiones horarias reales |
| **Tiempo de disponibilidad simulada** | Momento artificial en que el *replay* revela el registro al agente | Por convención didáctica, el registro se habilita al cierre de su hora |
| **Tiempo objetivo de la recomendación** | Franja para la cual se emite la acción | Es la hora $h+1$, no la hora $h$ ya observada |

### Estado real, percepción y estado interno

| Concepto | En este caso | Consecuencia |
|---|---|---|
| **Estado real del entorno** | Pasajeros que desean viajar, solicitudes atendidas y no atendidas, vehículos ocupados o libres, posiciones, tráfico y clima en cada lugar | Existe aunque el agente no pueda observarlo por completo |
| **Percepción** | Valor derivado que el *replay* habilita antes de la decisión simulada: zona-hora objetivo, resumen de *pickups* históricos hasta $h$, clima admisible de la estación y capacidad simulada | Es evidencia histórica parcial, posiblemente ruidosa o faltante; no es una observación operativa en vivo ni el fenómeno completo |
| **Estado interno** | Representación usada por la política: validez de datos, categoría de actividad histórica, categoría climática pertinente, prioridad calculada y capacidad restante simulada | Resume lo percibido para elegir una acción; no debe confundirse con el estado real |

Las columnas de un archivo **no son sensores físicos**. En la arquitectura de agentes, un *sensor* es aquí un **mecanismo lógico de adquisición simulado**: el reproductor histórico controla qué filas del archivo TLC quedan visibles en cada paso, las une con el catálogo de zonas, incorpora NOAA, aplica el corte temporal y recibe el parámetro de capacidad simulada. La *percepción* es el valor que ese mecanismo entrega después de validar, filtrar y derivar variables. No existe una conexión en tiempo real con TLC. Por ejemplo, el mecanismo revela marcas de tiempo históricas hasta el cierre de $h$ y la percepción puede ser una categoría de actividad para recomendar sobre $h+1$.

### Supuestos didácticos

- La unidad de decisión es una zona-hora simulada. En cada paso, $h$ es la última hora cerrada y $h+1$ es la hora objetivo de la recomendación.
- La política y los umbrales de `BAJA`, `MEDIA` y `ALTA` deben fijarse antes de evaluar el caso; esta resolución no inventa umbrales ni resultados numéricos.
- El archivo completo puede estar físicamente cargado durante el experimento, pero el *replay* enmascara el futuro. El historial admisible contiene únicamente registros revelados hasta el cierre de $h$. **Nunca se usan viajes, clima, umbrales ni resúmenes de $h+1$ o posteriores para recomendar sobre $h+1$.**
- Por convención didáctica se supone que los viajes de $h$ quedan disponibles inmediatamente al cerrarse esa hora. Esta convención es falsa respecto del mecanismo real de publicación de los archivos TLC y debe acompañar toda demostración.
- Si el clima se resume por hora, solo pueden entrar observaciones habilitadas hasta el cierre de $h$. El clima de $h+1$ solo podría utilizarse si una fuente de pronóstico disponible al corte lo proporcionara; las observaciones futuras no pueden tratarse como pronóstico.
- La zona de TLC se toma como unidad geográfica administrativa. El valor NOAA se interpreta como contexto de la estación, no como medición local de cada zona.
- La “capacidad simulada” es un parámetro externo del ejercicio que indica si todavía se permite emitir una recomendación de refuerzo. No prueba que exista un vehículo libre y no procede del dataset de movilidad.
- La salida se conserva con versión de política, hora cerrada $h$, hora objetivo $h+1$, evidencia revelada, motivos y marca explícita de `modo_replay`, de modo que pueda auditarse.

## 1. Propósito y usuario

**Propósito.** Bajo la suposición didáctica de disponibilidad horaria, analizar la evidencia histórica revelada hasta el cierre de la hora $h$ para una zona y recomendar al responsable `OBSERVAR`, `MONITOREAR` o `RECOMENDAR_REFUERZO` para la hora $h+1$, respetando la calidad de los datos, el corte temporal y la capacidad operativa simulada. Si no puede justificar una de esas acciones, debe `ABSTENERSE`. El agente busca producir recomendaciones coherentes y trazables dentro del *replay*; no monitorea la ciudad en tiempo real ni estima directamente pasajeros en espera.

La prioridad `BAJA`, `MEDIA` o `ALTA` se conserva como **estado interno de decisión**. Ayuda a evaluar la evidencia y a separar necesidad estimada de factibilidad.

**Usuario directo.** Una persona que representa al responsable de operaciones en la simulación. Recibe la salida, revisa su justificación y decide si la acepta, la posterga o la rechaza.

**Usuarios indirectos y personas afectadas.** Conductores, pasajeros potenciales, operadores de otras zonas y responsables institucionales. Aunque el agente no actúa físicamente, una persona podría basarse en su recomendación; por eso una mala recomendación puede concentrar atención en ciertas zonas, desatender otras o inducir traslados ineficientes si se usa fuera del alcance declarado.

**Decisión de diseño.** Se adopta asistencia humana y no autonomía. Esta elección es racional porque faltan variables operativas esenciales: demanda no atendida, espera, vehículos libres, origen posible del refuerzo, ruta, tráfico completo y costo real del traslado.

## 2. Medida de desempeño con al menos tres criterios

La evaluación se realiza sobre salidas del recomendador y restricciones de la simulación, no sobre una reducción real de espera que estos datos no permiten medir.

| Criterio | Pregunta auditable | Error que revela |
|---|---|---|
| **Coherencia entre estado interno y acción** | ¿Cada acción respeta la prioridad interna, la suficiencia de datos y la política declarada? | Recomendar refuerzo con prioridad interna media o evidencia insuficiente |
| **Cumplimiento de capacidad simulada** | ¿Nunca se recomienda un refuerzo cuando la capacidad simulada está agotada? | Violar una restricción dura del ejercicio |
| **Refuerzos innecesarios según la política** | ¿Cuántos `RECOMENDAR_REFUERZO` se emiten sin prioridad interna alta o sin las precondiciones establecidas? | Sobreintervención y consumo injustificado de capacidad simulada |
| **Abstención correcta** | ¿El agente se abstiene cuando faltan datos críticos, zona inválida o evidencia incompatible? | Confianza aparente sin soporte |
| **Consistencia entre zonas** | ¿Casos equivalentes bajo la representación reciben igual tratamiento y se revisan diferencias persistentes de cobertura? | Reglas arbitrarias o sesgo operativo no explicado |

Una forma conceptual de expresar el desempeño es:

$$
U = w_1 C_{\text{coherencia}}
    + w_2 C_{\text{abstención}}
    + w_3 C_{\text{consistencia entre zonas}}
    - w_4 E_{\text{refuerzo innecesario}},
$$

sujeto a la restricción dura de no exceder la capacidad simulada. Los pesos no se fijan aquí: deben ser una decisión explícita del ejercicio y someterse a revisión humana.

Los criterios entran en conflicto. Abstenerse más protege frente a datos deficientes, pero reduce la cantidad de recomendaciones; penalizar demasiado los refuerzos innecesarios puede hacer que el agente monitoree incluso cuando la política permitiría recomendar; reservar capacidad para decisiones posteriores puede impedir actuar sobre el caso actual. Por ello no basta maximizar una sola cifra y tampoco corresponde ocultar restricciones dentro de un promedio.

Una función de desempeño mal definida puede ejecutarse perfectamente y ser dañina. Por ejemplo, premiar solo la cantidad de refuerzos haría racional, respecto de esa métrica, recomendar siempre un refuerzo, consumir la capacidad simulada y concentrar atención donde hubo más viajes realizados, aunque esa actividad refleje oferta histórica y no necesidad insatisfecha.

## 3. Entorno y actores afectados

El entorno real incluye zonas urbanas, vías, pasajeros, conductores, vehículos, otros servicios de transporte, tráfico, clima, regulación y el proceso humano de operaciones. El entorno informacional didáctico incluye los registros históricos TLC, el reproductor que los revela por hora simulada, el catálogo y geometría de zonas, las observaciones NOAA, la configuración de la simulación, la política de prioridad y el registro de decisiones. El archivo histórico no constituye por sí mismo una percepción en tiempo real.

| Actor | Relación con la decisión | Posible efecto |
|---|---|---|
| Responsable de operaciones simulado | Revisa la recomendación y conserva autoridad | Carga de revisión, apoyo o falsa confianza |
| Conductores y operadores | Podrían recibir una instrucción humana posterior, fuera del agente | Traslado, oportunidad de servicio o recorrido vacío |
| Pasajeros atendidos | Sus viajes realizados contribuyen al historial TLC | Su patrón puede quedar sobrerrepresentado respecto de quienes no lograron viajar |
| Solicitantes no atendidos | Forman parte del fenómeno, pero no aparecen como tales en TLC | Invisibilidad en la métrica y posible perpetuación de brechas |
| Otras zonas | Compiten por atención y por la capacidad simulada | Costo de oportunidad si una zona es priorizada |
| TLC y NOAA | Proveen registros con alcances y procesos de captura propios | Calidad, demora, cobertura y representatividad condicionan la percepción |
| Docente y estudiantes | Diseñan, ejecutan y auditan la simulación | Responsables de no convertir el prototipo en una afirmación operacional |

La frontera del agente termina en el mensaje de recomendación. Si una organización decidiera actuar, esa decisión pertenecería a otro sistema sociotécnico que necesitaría datos de flota, seguridad, costos, autoridad, retroalimentación y evaluación causal.

## 4. Acciones permitidas y abstención

La salida completa tiene la forma:

```text
zona + hora_cerrada_h + hora_objetivo_h_mas_1 + acción + evidencia
+ restricciones + explicación + limitaciones + modo_replay
```

La prioridad es una clasificación interna y no un campo obligatorio de la respuesta visible. Las únicas acciones operativas son `OBSERVAR`, `MONITOREAR` y `RECOMENDAR_REFUERZO`; `ABSTENERSE` se mantiene como salida excepcional de seguridad. Las definiciones son operacionales y no deben sustituirse por interpretaciones coloquiales.

### `OBSERVAR`

| Elemento | Definición operacional |
|---|---|
| **Precondición** | Evidencia suficiente y válida; prioridad interna `BAJA`; no existe una condición de falla que obligue a abstenerse |
| **Salida observable** | Registro de la acción para $h+1$, evidencia disponible al cierre de $h$, limitaciones y regla; sin alerta prioritaria y sin recomendación de cambio |
| **Efecto real** | Solo crea una entrada informativa y auditable para la persona usuaria; no altera la calle ni la distribución de vehículos |
| **Qué NO significa** | No significa ignorar el caso, cerrar su seguimiento, captar nuevos datos por sí mismo, vigilar continuamente, confirmar baja demanda total ni asegurar que no haya pasajeros esperando |

### `MONITOREAR`

| Elemento | Definición operacional |
|---|---|
| **Precondición** | Evidencia suficiente y prioridad interna `MEDIA`; o prioridad interna `ALTA` cuando no existe capacidad simulada para recomendar refuerzo; o condición explícita de revisión definida por la política |
| **Salida observable** | Alerta informativa que eleva el caso para revisión en el siguiente paso del *replay*, con evidencia, limitaciones y, cuando corresponda, la explicación de que la capacidad agotada impidió recomendar refuerzo |
| **Efecto real** | Cambia la visibilidad y el orden de revisión dentro de la interfaz o bitácora didáctica |
| **Qué NO significa** | No mueve vehículos, no reserva capacidad, no garantiza observación en tiempo real, no inicia una captura nueva y no prueba que la situación vaya a empeorar. “Monitorear” significa volver a evaluar en el siguiente paso histórico simulado, no vigilar una fuente TLC en vivo |

### `RECOMENDAR_REFUERZO`

| Elemento | Definición operacional |
|---|---|
| **Precondición** | Prioridad interna `ALTA`, datos suficientes y válidos, y capacidad simulada disponible; todas las restricciones deben cumplirse simultáneamente |
| **Salida observable** | Propuesta destacada para que el humano considere priorizar capacidad adicional en la zona durante $h+1$, junto con evidencia histórica hasta $h$, límites, capacidad consumible y regla aplicada |
| **Efecto real** | Solo incorpora una propuesta a la decisión humana y, en la simulación, puede reservar o descontar una unidad de capacidad según las reglas del ejercicio después de su aceptación explícita |
| **Qué NO significa** | No ordena ni ejecuta un traslado; no elige vehículo, conductor, origen ni ruta; no confirma que haya un recurso libre; no garantiza beneficio ni reducción de espera. Tampoco es una recomendación calculada con viajes en vivo: procede de una reproducción histórica bajo disponibilidad supuesta |

### `ABSTENERSE`

| Elemento | Definición operacional |
|---|---|
| **Precondición** | Evidencia insuficiente o inválida: zona desconocida, tiempo inconsistente, datos críticos faltantes, referencia histórica con información posterior a $h$, indisponibilidad en el paso simulado, clima no disponible cuando la política lo requiere, capacidad desconocida para una posible acción alta, valores fuera del dominio o conflicto no resuelto entre fuentes |
| **Salida observable** | Mensaje de “sin recomendación”, motivo específico, datos faltantes o inválidos y solicitud de revisión humana; no se fuerza una prioridad operativa confiable |
| **Efecto real** | Detiene la recomendación automática para ese caso y conserva la evidencia para diagnóstico |
| **Qué NO significa** | No significa prioridad baja, ausencia de actividad, caso resuelto, autorización tácita para actuar ni eliminación del registro |

### Política ilustrativa

La tabla muestra coherencia entre condiciones y acción; no fija los umbrales que producen la prioridad.

| Evidencia | Prioridad interna derivada | Capacidad simulada | Acción visible | Justificación |
|---|---|---|---|---|
| Insuficiente o inválida | No confiable | Cualquiera | `ABSTENERSE` | La seguridad epistemológica precede a la optimización |
| Suficiente | `BAJA` | Cualquiera | `OBSERVAR` | Se registra sin escalar ni sugerir cambio |
| Suficiente | `MEDIA` | Cualquiera | `MONITOREAR` | Se eleva la revisión, no la intervención |
| Suficiente | `ALTA` | Disponible | `RECOMENDAR_REFUERZO` | Cumple prioridad, datos y restricción de capacidad |
| Suficiente | `ALTA` | No disponible | `MONITOREAR` | Mantiene visibilidad y explica la restricción sin crear otra acción ni infringir capacidad |
| Suficiente | `ALTA` | Desconocida | `ABSTENERSE` | No se puede comprobar una precondición crítica |

## 5. Percepciones disponibles antes de decidir

En la realidad, los archivos TLC no proporcionan estas percepciones con periodicidad horaria. Dentro del *replay*, para recomendar sobre $h+1$, el agente solo puede adquirir y derivar información cuya **disponibilidad simulada** no sea posterior al cierre de $h$:

- identificador y nombre válidos de la zona TLC;
- hora local cerrada $h$ y hora objetivo $h+1$, con zona horaria definida;
- conteos o resúmenes históricos de *pickups* Yellow Taxi **realizados y reportados** para referencias comparables reveladas hasta $h$;
- categorías derivadas de esa actividad histórica mediante umbrales previamente definidos;
- observaciones NOAA de la estación y resúmenes calculados solo con muestras habilitadas hasta $h$;
- indicadores de faltantes, antigüedad, cobertura, compatibilidad temporal y validez de uniones;
- capacidad simulada disponible o agotada, suministrada por el escenario;
- historial anterior de recomendaciones y consumo de capacidad, cuando la reproducción es secuencial;
- versión de la política, parámetros y reglas vigentes.

La historia de referencia debe construirse respetando causalidad temporal. Si $H_h$ es el historial revelado al cierre de $h$, debe cumplirse:

$$
H_h = \{r_i : \operatorname{disponible\_sim}(r_i) \leq \operatorname{cierre}(h)\}.
$$

La función `disponible_sim` es una convención del experimento, no la fecha real de publicación TLC. Que el viaje haya ocurrido en una hora no significa que estuviera disponible operacionalmente al terminarla; el *replay* finge esa disponibilidad para enseñar el ciclo del agente. Asimismo, normalizaciones, percentiles y umbrales ajustados con todo el mes incorporarían futuro respecto del paso simulado; deben calcularse solo con el historial ya revelado o con un período de entrenamiento anterior.

### Matriz de variables observadas y no observadas

| Variable o fenómeno | ¿Disponible? | Representación correcta |
|---|---:|---|
| *Pickups* Yellow Taxi realizados y reportados | Sí, con filtros de calidad y corte temporal | Actividad histórica observada |
| *Pickups* disponibles en tiempo real | No | El *replay* simula que los registros aparecen al cierre de cada hora |
| Zona de inicio TLC | Sí, si la unión es válida | Zona administrativa reportada para el *pickup* |
| Hora local del *pickup* | Sí, tras conversión temporal correcta | Momento reportado del inicio del viaje |
| Clima en la estación NOAA | Sí, si la observación ya estaba disponible | Contexto meteorológico puntual de una estación |
| Clima exacto de cada zona | No | No inferirlo como observación directa de NOAA |
| Demanda total de viajes | No | Variable latente fuera del dataset |
| Solicitudes no atendidas o canceladas | No | No pueden contarse desde los viajes completados/reportados |
| Tiempo de espera de pasajeros | No | No puede evaluarse ni declararse reducido |
| Vehículos libres y su ubicación | No | La capacidad simulada no sustituye un inventario real |
| Tráfico e incidentes en tiempo real | No | Parte no observada del entorno |
| Origen, recurso y ruta de un refuerzo | No | Requieren datos y decisiones adicionales |
| Capacidad simulada | Sí, si la provee el escenario | Restricción didáctica, no evidencia de flota real |
| Prioridad | Derivada | Estado interno producido por reglas, no columna física ni verdad del entorno |

## 6. Propiedades del ambiente

La clasificación depende del **nivel de abstracción**. El transporte urbano real y la simulación congelada no tienen exactamente las mismas propiedades; confundirlos conduce a atribuir al prototipo capacidades que no posee.

| Propiedad | Caracterización y justificación |
|---|---|
| **Observabilidad** | **Parcialmente observable.** Faltan demanda total, solicitudes no atendidas, espera, flota libre, tráfico completo, intenciones y clima espacial. Los registros observados son una proyección del estado real. |
| **Resultado/transición** | **Estocástico en la realidad**, porque una misma recomendación puede producir respuestas humanas, traslados y resultados distintos. Para el ejercicio, la **transición didáctica es determinista**: dada la misma representación, política y capacidad simulada, se obtiene la misma prioridad, acción y actualización de capacidad. Esto facilita auditoría, pero no vuelve determinista al transporte. |
| **Dependencia temporal** | **Secuencial** cuando una recomendación aceptada consume capacidad simulada o cuando recomendaciones previas condicionan las siguientes. El *replay* avanza de $h$ a $h+1$ y cada decisión modifica las opciones futuras. Solo sería episódico si cada zona-hora se evaluara de forma aislada y se reiniciara la capacidad. |
| **Cambio durante la decisión** | **Dinámico en la realidad**: viajes, vehículos y clima cambian mientras se calcula. Los archivos TLC no transmiten esos cambios en vivo. En el prototipo, el *replay* congela una instantánea al cierre de $h$, ejecuta la decisión para $h+1$ y luego avanza un paso; por eso el problema computacional es estático dentro de cada ciclo y dinámico solo por actualización simulada entre ciclos. |
| **Naturaleza del estado** | **Mixto continuo/discreto**: tiempo, temperatura, precipitación o viento pueden ser continuos; zona, prioridad, acción y disponibilidad son discretos. El prototipo **discretiza** hora, categorías climáticas y prioridad para obtener un espacio finito manejable. |
| **Participantes** | El ambiente real es **multiagente**: pasajeros, conductores, operadores y otros vehículos persiguen objetivos propios. La simulación los simplifica como contexto o efectos externos y modela explícitamente un solo recomendador y un humano supervisor. |
| **Conocimiento** | **Parcialmente conocido.** Se conocen el formato de datos, la regla artificial de disponibilidad, la política didáctica y la transición simulada, pero no se conoce por completo cómo los registros se relacionan con demanda latente ni cuáles serían las consecuencias reales de una recomendación. |

En consecuencia, una afirmación como “el ambiente es determinista” solo es defendible si se especifica “la transición interna de la simulación, con entrada congelada”. Sin ese nivel de abstracción, sería falsa para la movilidad urbana.

## 7. Riesgo de métrica inadecuada

El riesgo principal es usar el volumen histórico de *pickups* realizados como si fuera demanda total o necesidad insatisfecha y premiar la concentración de recomendaciones donde ese volumen es mayor. TLC observa el resultado conjunto de solicitudes, oferta disponible, reglas de servicio, geografía y prácticas de reporte. Una zona con pocos viajes registrados podría tener poca demanda, pero también poca oferta, solicitudes no atendidas o población que usa otros medios; el dataset no permite distinguir esas explicaciones.

Si la métrica recompensa únicamente “cubrir las zonas con más *pickups*”, el agente puede ejecutar sus reglas sin errores y aun así:

- reproducir patrones históricos de oferta en lugar de atender necesidad;
- favorecer zonas con mayor actividad Yellow Taxi reportada;
- consumir temprano la capacidad simulada;
- emitir demasiados refuerzos para mejorar una cifra interna;
- ocultar incertidumbre al tratar la abstención como fracaso;
- desplazar atención de zonas con baja cobertura observacional.

La mitigación consiste en separar indicador de evidencia y objetivo social, evaluar varios criterios, imponer capacidad como restricción, auditar cobertura por zona y período, conservar abstención y prohibir afirmaciones sobre espera o demanda no observada. Una evaluación operativa real requeriría nuevas fuentes y un diseño que mida consecuencias; no puede deducirse de esta simulación.

## 8. Supervisión o falla segura

Se adopta una arquitectura **human-in-the-loop** con abstención segura. El agente genera una propuesta; una persona conserva la autoridad y ve evidencia, limitaciones y regla aplicada antes de cualquier decisión externa.

Controles mínimos:

- validar esquema, tipos, zona, zona horaria, duplicados y faltantes antes de clasificar;
- aplicar un corte temporal estricto a datos, agregados, normalizaciones y umbrales, separando $h$ de la hora objetivo $h+1$;
- identificar toda ejecución como `modo_replay` y no mostrarla como monitoreo en tiempo real;
- impedir que el archivo mensual completo revele filas posteriores al cierre de $h$;
- comprobar que la observación NOAA corresponde a la estación declarada y no presentarla como clima zonal;
- verificar suficiencia de evidencia y dominio de entrada; ante incumplimiento, `ABSTENERSE`;
- impedir por regla dura `RECOMENDAR_REFUERZO` sin prioridad interna alta, evidencia suficiente y capacidad simulada;
- registrar entradas derivadas, fuentes, versión, prioridad interna, acción, motivo, capacidad antes/después y decisión humana; la prioridad queda en la bitácora de auditoría aunque no sea un campo obligatorio de la respuesta al usuario;
- permitir que el humano acepte, rechace o solicite revisión, dejando constancia de la razón;
- detener la emisión de recomendaciones ante anomalías masivas, desalineación temporal, cambio de esquema o resultados imposibles;
- revisar periódicamente tasas de acción y abstención por zona-hora para detectar cobertura desigual o deriva;
- no convertir automáticamente una alerta en una orden a conductores o sistemas de flota.

La falla segura es informativa: ante incertidumbre crítica, el sistema no inventa una prioridad ni degrada el caso a `BAJA`; emite `ABSTENERSE`, explica el dato faltante o inconsistente y remite a revisión humana. Si la prioridad interna es alta pero la capacidad está agotada, emite `MONITOREAR` y explica esa restricción sin violarla.

## PEAS consolidado

| Componente | Especificación del agente acotado |
|---|---|
| **P — Performance** | Coherencia entre estado interno y acción, cobertura de casos internamente altos y accionables, cumplimiento de capacidad, pocos refuerzos contrarios a política, abstención correcta, trazabilidad y revisión de consistencia entre zonas |
| **E — Environment** | Reproducción histórica por pasos horarios, zona objetivo en $h+1$, actividad Yellow Taxi reportada revelada hasta $h$, estación NOAA, catálogo de zonas, capacidad y política simuladas; como entorno real de referencia, pasajeros, conductores, flota, tráfico, clima y regulación parcialmente observados |
| **A — Actuators** | Mensajes y registros con las acciones operativas `OBSERVAR`, `MONITOREAR` y `RECOMENDAR_REFUERZO`; `ABSTENERSE` como salida excepcional de seguridad. Comunican evidencia, explicación y limitaciones. No existen actuadores físicos ni órdenes de traslado |
| **S — Sensors** | Mecanismos lógicos de *replay* para revelar progresivamente TLC histórico, leer zonas y NOAA, recibir $h$, zona y capacidad simuladas, aplicar el corte temporal y derivar percepciones con indicadores de calidad. No existe un sensor TLC en tiempo real y las columnas no son sensores físicos |

## Ciclo percepción-acción: ejemplo cualitativo

```text
Revelar en el replay los datos hasta el cierre de h
        ↓
Validar zona, tiempo, cobertura y procedencia
        ↓
Derivar actividad histórica y contexto climático admisibles
        ↓
Actualizar estado interno y asignar prioridad
        ↓
Comprobar suficiencia y capacidad simulada
        ↓
Seleccionar acción para la hora objetivo h+1
        ↓
Mostrar evidencia y limitaciones al humano
        ↓
Registrar revisión y preparar el siguiente ciclo
```

**Ejemplo sin cifras inventadas.** Al cerrarse la hora simulada $h$, el *replay* revela los registros históricos permitidos hasta ese corte. La política usa esa evidencia para construir internamente una prioridad sobre una zona durante $h+1$. Si la prioridad es alta y la capacidad simulada está disponible, el agente emite `RECOMENDAR_REFUERZO` para $h+1$ y explica que se basa en viajes históricos realizados, no en pasajeros esperando ni en un flujo vivo. El humano revisa la propuesta. Si la misma evidencia aparece cuando la capacidad está agotada, la salida visible es `MONITOREAR`. Si el cálculo utiliza viajes de $h+1$ para recomendar al inicio de $h+1$, la salida correcta es `ABSTENERSE` por fuga temporal.

## Invariantes y requisitos de coherencia

- Toda salida identifica una zona, la hora cerrada $h$, la hora objetivo $h+1$ y el `modo_replay`.
- Ningún dato, agregado, umbral aprendido o transformación usa registros revelados después del cierre de $h$ para decidir sobre $h+1$.
- El tiempo del viaje nunca se presenta como tiempo real de publicación o disponibilidad.
- `RECOMENDAR_REFUERZO` implica simultáneamente prioridad interna alta, evidencia suficiente y capacidad simulada disponible.
- Capacidad agotada implica que no se emite `RECOMENDAR_REFUERZO`.
- Evidencia insuficiente o inválida implica `ABSTENERSE`, no prioridad baja por defecto.
- Prioridad interna alta con evidencia suficiente y sin capacidad implica `MONITOREAR`, con explicación de la restricción.
- `OBSERVAR` no genera alerta prioritaria ni recomendación de cambio.
- `MONITOREAR` no produce movimiento físico ni promete observación continua.
- Toda recomendación incluye evidencia y limitaciones; la prioridad interna sin procedencia tampoco sería una base válida para decidir.
- La capacidad simulada nunca se describe como conteo de vehículos libres reales.
- El clima NOAA nunca se atribuye como medición exacta de todas las zonas.
- Una recomendación rechazada por el humano no se registra como ejecutada ni como resultado positivo.

## Afirmaciones permitidas y prohibidas

| Permitida | Prohibida | Motivo |
|---|---|---|
| “La bitácora interna clasificó la actividad histórica reportada como alta según la política.” | “La demanda total es alta.” | La prioridad es interna y TLC no observa toda la demanda |
| “Se registraron *pickups* Yellow Taxi realizados y reportados.” | “Ese fue el número de solicitudes.” | Faltan solicitudes no atendidas y otros servicios |
| “En el *replay*, los datos hasta $h$ se usaron para recomendar sobre $h+1$.” | “El agente monitorea los viajes TLC en tiempo real.” | Los archivos utilizados son publicaciones históricas |
| “La disponibilidad horaria fue simulada con fines didácticos.” | “TLC publica cada viaje al finalizar la hora.” | La regla de disponibilidad pertenece al experimento, no a la fuente real |
| “La estación NOAA reportó este contexto meteorológico.” | “Ese era el clima exacto en toda la zona.” | Una estación no da cobertura espacial completa |
| “El agente recomienda que una persona considere priorizar capacidad.” | “El agente envió un vehículo.” | El agente solo produce mensajes |
| “La capacidad simulada permite emitir la recomendación.” | “Hay un vehículo libre disponible.” | La capacidad es una restricción didáctica externa |
| “La evidencia fue suficiente bajo controles declarados.” | “El estado real se conoce por completo.” | El ambiente es parcialmente observable |
| “La política produjo una acción coherente.” | “La acción reducirá la espera.” | No se observan espera ni efecto causal |
| “El agente se abstuvo por fuga temporal.” | “La prioridad era baja.” | Ausencia de evidencia válida no equivale a baja prioridad |

## Preguntas de comprobación y respuestas esperadas

**¿Un *pickup* equivale a una solicitud de viaje?**

No. Es un viaje iniciado, realizado y reportado. No incluye necesariamente solicitudes no atendidas, cancelaciones ni intentos fuera de Yellow Taxi.

**¿Puede evaluarse la reducción real del tiempo de espera con este caso?**

No. El dataset descrito no contiene espera ni un contrafactual que permita atribuir cambios a la recomendación.

**¿Las columnas `temperature` o `PULocationID` son sensores?**

No por sí solas. Son campos registrados. El sensor del agente es el mecanismo lógico que adquiere y valida datos; la percepción es el valor derivado que entra a la decisión.

**¿Puede usarse el promedio NOAA de toda la hora si se decide a mitad de esa hora?**

No. Incluiría observaciones futuras respecto del instante simulado. Solo puede usarse información disponible hasta el corte.

**¿Los viajes TLC utilizados están disponibles realmente al finalizar cada hora?**

No. El curso utiliza archivos históricos publicados posteriormente. La disponibilidad al cierre de cada hora es una convención del *replay* para estudiar agentes y no una propiedad de la fuente real.

**¿Por qué se recomienda para $h+1$ y no para la misma hora $h$?**

Porque los conteos completos de $h$ solo quedan definidos después de cerrar esa hora en la simulación. Usarlos para decidir al comienzo de $h$ introduciría información futura. El esquema didáctico usa datos hasta $h$ para recomendar sobre $h+1$.

**¿Sería válido cargar el archivo mensual completo y dejar que los resúmenes usen todas sus filas?**

No. Aunque el archivo exista físicamente durante la ejecución, el *replay* debe enmascarar filas posteriores a $h$. De lo contrario, umbrales, agregados o decisiones incorporarían futuro y la simulación dejaría de representar una decisión secuencial.

**¿Qué acción corresponde a prioridad interna alta con evidencia suficiente y capacidad agotada?**

`MONITOREAR`, explicando que la evidencia justificó atención elevada, pero que la capacidad agotada impide recomendar un refuerzo. Así se mantienen solo tres acciones operativas.

**¿Qué acción corresponde si falta una percepción crítica?**

`ABSTENERSE`, indicando el motivo y solicitando revisión; no convertir el faltante en prioridad baja.

**¿Por qué el ambiente puede llamarse determinista y estocástico sin contradicción?**

La transición didáctica de reglas es determinista para una entrada congelada; las consecuencias de movilidad en el mundo real son estocásticas. La propiedad depende del nivel de abstracción.

**¿Puede `RECOMENDAR_REFUERZO` especificar el origen o la ruta?**

No. TLC y NOAA no contienen flota libre, origen operativo ni ruta. Hacerlo requeriría otro estado, otras percepciones y restricciones adicionales.

**¿Una ejecución sin errores garantiza una decisión aceptable?**

No. El agente puede optimizar perfectamente una función mal definida y causar sobreintervención, inequidad o consumo inadecuado de capacidad.

## Puente a Semana 2: representación como problema

La especificación de Semana 1 permite preparar, todavía sin elegir ni desarrollar un algoritmo de búsqueda, una formulación:

$$
P=(S,A,T,s_0,G,c).
$$

| Símbolo | Correspondencia preliminar |
|---|---|
| $S$ | Estados internos discretizados: hora cerrada $h$, zona objetivo en $h+1$, prioridades internas conocidas, evidencia histórica revelada, capacidad simulada restante e historial relevante de recomendaciones |
| $A$ | Acciones permitidas por la política; en una planificación posterior podrían representar qué caso atender o revisar a continuación |
| $T$ | Transición didáctica que registra la acción, actualiza capacidad y avanza el *replay* desde $h$ hacia $h+1$ de manera determinista |
| $s_0$ | Hora inicial cerrada, zonas objetivo del siguiente paso, evidencia histórica revelada al corte y capacidad simulada inicial definida por el escenario |
| $G$ | Condición explícita de cobertura o revisión de casos prioritarios respetando restricciones; debe definirse sin afirmar reducción de espera |
| $c$ | Costo didáctico de revisión, uso de capacidad, abstención o recomendación, definido de forma transparente y no confundido con costo real de movilidad |

La próxima semana deberá decidir qué diferencias del estado cambian acciones y costos, qué restricciones son duras y qué objetivo es verificable. La transición temporal deberá preservar el invariante `datos hasta h → recomendación para h+1`. No se desarrolla aquí BFS, costo uniforme ni otra estrategia: primero se mantiene separada la especificación del agente de la elección algorítmica.

## Fuentes internas del curso

- [Capítulo 1. Ciencia de Datos e Inteligencia Artificial](../../../Libro/Capitulo_01_Ciencia_de_Datos_e_IA.md), especialmente agente, racionalidad, datos como representación parcial y diferencia entre predicción y decisión.
- [Capítulo 6. Agentes inteligentes y representación de problemas](../../../Libro/Capitulo_06_Agentes_inteligentes_y_representacion_de_problemas.md), especialmente PEAS, propiedades del ambiente y formulación de problemas.
- [Semana 1. Fundamentos de IA, agentes y racionalidad](./Clase_01_Fundamentos_de_IA_agentes_y_racionalidad.md), presentación que contiene la actividad resuelta.
- [Semana 2. Representación y búsqueda en espacios de estados](../Semana_02/Clase_02_Representacion_y_busqueda_en_espacios_de_estados.md), continuidad mediante $P=(S,A,T,s_0,G,c)$.
- [Caso de datos MOVILIDAD](../../../LABORATORIOS/MOVILIDAD/), fuente interna para los registros TLC, las zonas y las observaciones NOAA utilizadas en el ejercicio.
