# Capítulo 6. Agentes inteligentes y representación de problemas

## Propósito y objetivos de aprendizaje

Un sistema de inteligencia artificial no actúa en el vacío. Recibe información incompleta, interviene sobre un entorno y es evaluado por las consecuencias de sus decisiones. La noción de **agente** reúne estos elementos en una unidad de análisis: permite preguntar qué observa el sistema, qué puede hacer, qué pretende lograr y bajo qué condiciones una acción puede considerarse racional. Esta perspectiva evita reducir la inteligencia artificial a un algoritmo aislado.

El capítulo avanza desde el concepto general de agente hasta la formulación computacional de problemas. Primero distingue racionalidad, autonomía y omnisciencia. Luego caracteriza los entornos mediante PEAS y seis dimensiones que condicionan el diseño. A continuación compara arquitecturas de agentes, desde reglas reactivas hasta sistemas que aprenden. Por último traduce situaciones del mundo real a estados, acciones, transiciones, objetivos, costos y restricciones. Esa traducción será la entrada de los métodos de búsqueda del capítulo 7 y de las decisiones secuenciales del capítulo 8.

Al finalizar, el lector podrá:

- definir un agente por su relación perceptiva y activa con un entorno;
- diferenciar secuencia de percepciones, función de agente y programa de agente;
- diseñar medidas de desempeño alineadas con resultados y restricciones;
- explicar racionalidad limitada, autonomía y diferencia respecto de omnisciencia;
- construir una descripción PEAS y justificar cada uno de sus componentes;
- caracterizar observabilidad, incertidumbre, secuencialidad, dinamismo, continuidad e interacción entre agentes;
- comparar arquitecturas reactivas, deliberativas, basadas en utilidad y con aprendizaje;
- formular un problema mediante estados, acciones, transiciones, objetivos, costos y restricciones;
- seleccionar un nivel de abstracción adecuado y reconocer sus pérdidas de información;
- documentar supuestos, errores posibles y criterios de validación de una representación.

## 6.1. Agentes y racionalidad

La perspectiva de agentes desplaza la pregunta «¿qué algoritmo es inteligente?» hacia una pregunta operacional: «¿qué entidad selecciona acciones a partir de lo que percibe y cómo se evalúa esa selección?». El mismo algoritmo puede ser apropiado en un entorno e inadecuado en otro. Por ello, antes de escoger técnicas se debe delimitar el sistema, su frontera, su información y su responsabilidad.

### 6.1.1. Concepto de agente

Un **agente** es una entidad que percibe un entorno mediante sensores y actúa sobre él mediante actuadores. La definición es deliberadamente amplia: incluye un termostato, un robot, una persona, un sistema de recomendación o un servicio que asigna cuadrillas. Lo decisivo no es que tenga forma física ni que aprenda, sino que exista un ciclo entre percepción y acción.

Se denomina **entorno** a aquello que queda fuera de la frontera del agente y que resulta relevante para su tarea. Esa frontera es una decisión de modelado. En un sistema de movilidad, puede considerarse agente a cada vehículo, al coordinador de toda la flota o al conjunto vehículo-conductor. Cada elección modifica sensores, acciones y objetivos. Si el conductor queda dentro del agente, sus decisiones forman parte del mecanismo interno; si queda fuera, son eventos del entorno que deben observarse o anticiparse.

Formalmente, en el instante $t$ el entorno posee un estado $e_t$, genera una percepción $p_t$ y recibe una acción $a_t$. Una representación general es:

$$
p_t=O(e_t), \qquad a_t=\pi(p_1,\ldots,p_t), \qquad e_{t+1}\sim T(e_t,a_t),
$$

donde $O$ es el proceso de observación, $\pi$ la conducta del agente y $T$ la dinámica del entorno. El símbolo $\sim$ admite que la transición sea incierta. No se presupone que $p_t=e_t$: una percepción es información acerca del entorno, no necesariamente una copia completa de este.

Conviene distinguir agente de herramienta. Una calculadora produce un resultado cuando una persona la invoca, pero no suele seleccionar por sí misma cuándo actuar ni mantener un ciclo propio de interacción. En cambio, un sistema que supervisa caudales, detecta riesgo y decide emitir una orden participa en ese ciclo. La distinción no siempre es absoluta; depende del grado de iniciativa y de la frontera adoptada.

**Error frecuente.** Llamar «agente» a cualquier modelo predictivo. Un predictor que estima probabilidad de falla produce información; solo constituye por sí solo un agente si esa salida participa en una política que selecciona acciones. De otro modo, es un componente perceptivo o inferencial dentro de un agente más amplio.

### 6.1.2. Percepciones, sensores, acciones y actuadores

Una **percepción** es el contenido informativo recibido por el agente en un instante. La **secuencia de percepciones** $p_{1:t}=(p_1,\ldots,p_t)$ reúne toda su experiencia hasta $t$. Una observación puntual puede ser ambigua, mientras que la historia permite inferir tendencias: una presión baja aislada puede deberse a ruido; una caída persistente acompañada por aumento de caudal sugiere fuga.

Los **sensores** son mecanismos de adquisición. Pueden ser físicos, como manómetros y cámaras, o lógicos, como una interfaz de consulta, una cola de mensajes o un formulario. Sensor y variable observada no son sinónimos: un sensor posee rango, resolución, frecuencia, latencia, disponibilidad y error. Dos instrumentos que informan «presión» pueden ofrecer evidencias de calidad muy diferente.

Una **acción** es una decisión abstracta disponible para el agente; un **actuador** es el mecanismo que intenta ejecutarla. «Cerrar válvula V3» es una acción; el dispositivo motorizado y el canal de control son actuadores. La orden no garantiza el efecto: puede haber demora, rechazo o falla mecánica. Por eso se distingue entre acción emitida $a_t$ y transición efectiva del entorno.

| Elemento | Pregunta de diseño | Ejemplo en una red de agua | Riesgo habitual |
|---|---|---|---|
| Percepción | ¿Qué información recibe el agente? | Presión 2,1 bar a las 10:05 | Confundir dato con estado real |
| Sensor | ¿Cómo y con qué calidad se obtiene? | Manómetro digital cada minuto | Ignorar calibración o latencia |
| Acción | ¿Qué decisión puede seleccionar? | Reducir bombeo un 10 % | Definir acciones no ejecutables |
| Actuador | ¿Cómo se materializa la acción? | Variador de frecuencia | Suponer ejecución perfecta |
| Efecto | ¿Qué cambió realmente? | Caudal reducido tras 20 s | No verificar realimentación |

Diseñar el ciclo exige unidades, marcas temporales y semántica explícitas. También requiere manejar percepciones ausentes, contradictorias o fuera de rango. «Sin lectura» no equivale a «valor cero». En sistemas críticos, una acción debe incluir confirmación, límites operativos y una alternativa segura si el actuador no responde.

### 6.1.3. Función y programa de agente

La **función de agente** describe matemáticamente qué acción corresponde a cada secuencia posible de percepciones:

$$
f:P^*\rightarrow A,
$$

donde $P^*$ es el conjunto de secuencias finitas de percepciones y $A$ el conjunto de acciones. Es una especificación abstracta de conducta. Aunque una tabla pudiera enumerar todas las correspondencias, sería inmensa o infinita en entornos reales.

El **programa de agente** es el procedimiento concreto que implementa esa función sobre una arquitectura computacional. Recibe la percepción actual, consulta o actualiza memoria y devuelve una acción. La **arquitectura** aporta recursos de cómputo, almacenamiento, comunicación, sensores y actuadores. En forma sintética:

$$
Agente = Arquitectura + Programa.
$$

No deben confundirse estos niveles. Una misma función puede implementarse con programas distintos; un mismo programa puede comportarse de manera diferente si cambia la precisión de los sensores o el tiempo disponible. Además, el programa no recibe literalmente toda la historia: suele condensarla en un estado interno $m_t$:

$$
m_t=U(m_{t-1},p_t), \qquad a_t=D(m_t),
$$

donde $U$ actualiza memoria y $D$ decide. La calidad de $m_t$ depende de qué información retiene y cuál descarta.

Un esquema general, todavía independiente de lenguaje, es:

```text
PROCEDIMIENTO AGENTE(percepción)
    actualizar estado interno con percepción y acción anterior
    estimar alternativas legalmente disponibles
    evaluar alternativas según objetivo y conocimiento actual
    seleccionar una acción, o abstenerse si ninguna es segura
    registrar decisión y razones
    devolver acción
FIN PROCEDIMIENTO
```

La función de agente es útil para razonar sobre conducta; el programa permite estudiar límites reales. Memoria finita, presupuesto, demora máxima y precisión numérica forman parte del diseño. Una especificación que solo funciona con tiempo ilimitado no define un agente operativo.

### 6.1.4. Medidas de desempeño

Una **medida de desempeño** evalúa la secuencia de estados y consecuencias producida por el agente. Debe expresar el resultado deseado en el entorno, no una preferencia por el mecanismo interno. Para un servicio de agua, «minimizar interrupciones y pérdidas respetando seguridad» es mejor criterio que «emitir muchas alertas», porque una cantidad elevada de alertas puede lograrse sin resolver ningún problema.

Sea una trayectoria $\tau=(e_0,a_0,e_1,\ldots,e_H)$. Una medida general puede escribirse:

$$
J(\tau)=\sum_{t=0}^{H}w_t r(e_t,a_t)-\sum_{t=0}^{H}q(e_t,a_t),
$$

donde $r$ representa beneficios, $q$ costos o penalizaciones, y $w_t$ pondera el tiempo. Sin embargo, no todo debe convertirse en una suma. Una restricción de seguridad puede ser no negociable: primero se excluyen acciones inseguras y luego se optimiza entre las restantes.

Una medida bien construida declara:

- **unidad de evaluación:** evento, usuario, zona o trayectoria;
- **horizonte:** minutos, jornada, año o vida útil;
- **resultados positivos:** continuidad, cobertura, calidad o tiempo ahorrado;
- **costos:** energía, desgaste, demora, falsa alarma o intervención;
- **restricciones:** legalidad, seguridad, equidad y capacidad;
- **agregación:** promedio, peor caso, percentil o combinación;
- **fuente de verdad:** cómo y cuándo se verifica el resultado.

| Medida defectuosa | Conducta oportunista posible | Reformulación preferible |
|---|---|---|
| Maximizar alertas atendidas | Generar alertas triviales | Reducir daño confirmado por unidad de recurso |
| Minimizar tiempo medio de viaje | Perjudicar sistemáticamente zonas remotas | Combinar media, percentil alto y cobertura territorial |
| Minimizar consumo energético | Interrumpir un servicio necesario | Minimizar energía sujeto a nivel mínimo de servicio |
| Maximizar precisión | Ignorar casos raros y graves | Incorporar costos asimétricos y calibración |

La ley de Goodhart advierte que, cuando una medida se convierte en objetivo, puede dejar de ser una buena medida. Se requieren métricas complementarias, auditoría y revisión de efectos distributivos. El desempeño tampoco debe evaluarse solo con casos favorables: fallas de sensores, picos de demanda y cambios de régimen forman parte del entorno real.

### 6.1.5. Racionalidad y autonomía

Un agente es **racional** si selecciona la acción que maximiza el desempeño esperado dadas la secuencia de percepciones, el conocimiento previo, las acciones disponibles y sus recursos. En un instante $t$:

$$
a_t^*\in\arg\max_{a\in A_t}\mathbb{E}\left[J\mid p_{1:t},K,a\right],
$$

donde $K$ es el conocimiento disponible y $A_t$ el conjunto de acciones factibles. Si varias acciones alcanzan el mismo máximo, cualquiera puede ser racional. La racionalidad se juzga con la información disponible al decidir, no únicamente por el resultado observado después.

La expectativa es esencial: una decisión razonable puede terminar mal por azar. Reparar una tubería con alto riesgo estimado puede revelar que estaba intacta; ello no demuestra irracionalidad si el diagnóstico era válido y el costo esperado justificaba inspeccionar. Inversamente, una decisión temeraria puede salir bien sin volverse racional.

La **racionalidad limitada** reconoce que obtener la acción ideal puede requerir más cómputo, datos o tiempo de los disponibles. Un agente operativo busca una buena decisión dentro de sus recursos. El costo de deliberar también importa: una planificación perfecta que llega después de una inundación carece de valor. Esto conduce a algoritmos interrumpibles, umbrales y políticas de respaldo.

La **autonomía** es el grado en que la conducta depende de la experiencia propia y no solo de conocimiento incorporado por el diseñador. No equivale a ausencia de supervisión. Un agente puede aprender patrones locales y, a la vez, requerir aprobación humana para cerrar una válvula principal. La autonomía responsable necesita límites de acción, trazabilidad, detección de situaciones desconocidas y capacidad de abstención.

**Error frecuente.** Presentar racionalidad como obediencia ciega a una métrica. Si la métrica omite seguridad o derechos, maximizarla no convierte la conducta en aceptable. La especificación normativa precede a la optimización.

### 6.1.6. Agentes omniscientes frente a agentes racionales

Un agente **omnisciente** conoce el estado real, los efectos exactos de cada acción y todos los eventos futuros. Un agente racional no dispone de ese privilegio: decide bien a partir de evidencia limitada. Confundir ambos conceptos lleva a evaluar decisiones retrospectivamente con información que no existía en el momento.

Supóngase que hay 30 % de probabilidad de una falla grave. Inspeccionar cuesta 10 unidades y evita una pérdida de 100 si la falla existe. Sin inspección, el costo esperado es $0{,}30\times100=30$; inspeccionar cuesta 10, por lo que es racional hacerlo bajo este modelo. Si luego se descubre que no había falla, el costo realizado fue 10, pero la decisión continúa siendo racional. Un agente omnisciente habría sabido que ese caso no requería inspección.

La diferencia puede formalizarse mediante valor de información. Sea $I$ una observación perfecta antes de decidir. Su valor esperado es:

$$
VEIP=\mathbb{E}_I\left[\max_a\mathbb{E}(J\mid I,a)\right]-\max_a\mathbb{E}(J\mid a).
$$

La sigla **VEIP** significa **valor esperado de la información perfecta**. La fórmula compara el mejor desempeño esperado en dos situaciones: decidir después de conocer $I$ y decidir sin conocerlo. $J$ es la medida de desempeño que se desea maximizar; $a$ representa una acción factible; e $I$ es una observación que revela sin error la incertidumbre relevante antes de actuar. La distribución de $I$ representa lo que el agente cree posible con la información que posee en ese momento.

El primer término,

$$
\mathbb{E}_I\left[\max_a\mathbb{E}(J\mid I,a)\right],
$$

se evalúa de adentro hacia afuera. Primero se supone que la observación tomó un valor concreto $I=i$. Para cada acción se calcula $\mathbb{E}(J\mid I=i,a)$, porque aun con esa observación pueden quedar otras fuentes de azar. Luego se elige la acción con mayor desempeño esperado para ese valor observado. Finalmente se promedia el resultado óptimo sobre todos los valores que podría tomar $I$. Si $I$ es discreta, este término puede escribirse como

$$
\sum_i P(I=i)\max_a\mathbb{E}(J\mid I=i,a).
$$

Por tanto, la acción puede depender de la información recibida: ante $I=i_1$ se puede elegir $a_1$, y ante $I=i_2$, otra acción $a_2$. En términos de políticas, el primer término evalúa la mejor regla contingente $a(I)$.

El segundo término,

$$
\max_a\mathbb{E}(J\mid a),
$$

es el mejor desempeño esperado con la información actual. Primero se promedia la consecuencia de cada acción sobre los estados todavía desconocidos y después se selecciona una única acción. La ubicación del máximo es decisiva: en el primer término se observa y luego se elige; en el segundo se elige sin poder adaptar la acción al valor de $I$. En general,

$$
\mathbb{E}_I\left[\max_a\mathbb{E}(J\mid I,a)\right]
\geq
\max_a\mathbb{E}(J\mid a),
$$

porque un agente que recibe información siempre puede ignorarla y ejecutar la acción que habría elegido sin observar. La posibilidad de adaptar la decisión puede mejorar el desempeño y, si la misma acción es óptima para todos los valores de $I$, lo deja igual. Esta es la razón por la que el VEIP es no negativo cuando observar no tiene costo, no demora la decisión y no obliga a actuar.

El ejemplo de la falla permite calcular cada término. Para mantener la convención de maximizar, sea $J=-C$, donde $C$ es el costo. Sin información perfecta hay dos acciones:

| Acción | Costo si hay falla | Costo si no hay falla | Costo esperado | Desempeño esperado |
|---|---:|---:|---:|---:|
| Inspeccionar | 10 | 10 | $0{,}30(10)+0{,}70(10)=10$ | $-10$ |
| No inspeccionar | 100 | 0 | $0{,}30(100)+0{,}70(0)=30$ | $-30$ |

El segundo término vale entonces

$$
\max_a\mathbb{E}(J\mid a)=\max\{-10,-30\}=-10.
$$

Con información perfecta, el agente inspecciona cuando sabe que existe la falla y no inspecciona cuando sabe que no existe. El desempeño es $-10$ en el primer caso y $0$ en el segundo. Por ello,

$$
\mathbb{E}_I\left[\max_a\mathbb{E}(J\mid I,a)\right]
=0{,}30(-10)+0{,}70(0)=-3,
$$

y

$$
VEIP=(-3)-(-10)=7.
$$

Las 7 unidades representan la reducción máxima de costo esperado que podría aportar conocer con certeza si existe la falla antes de decidir. Equivalen a pasar de un costo esperado de 10 a uno de 3. En consecuencia, no sería racional pagar más de 7 unidades por esa información perfecta bajo los supuestos del ejemplo. Si obtenerla costara 4, su valor neto sería $7-4=3$; si costara 9, su valor neto sería negativo.

El VEIP es una cota superior, no el valor automático de cualquier sensor o prueba. La información real puede ser imperfecta, tardía o costosa. Una prueba con falsos positivos y falsos negativos cambia las probabilidades pero no revela el estado; su valor se calcula promediando las decisiones óptimas posteriores a cada resultado posible y suele ser menor que el VEIP. Además deben restarse el costo de adquisición, el costo de procesar el dato y las pérdidas ocasionadas por esperar. Obtener más datos solo es racional cuando la mejora esperada de la decisión supera esos costos.

También debe evitarse el sesgo de resultado: juzgar solo por éxito o fracaso. Una auditoría correcta reconstruye percepciones, modelo, alternativas y restricciones disponibles en el instante de decisión. Esta distinción prepara el análisis de utilidad y decisiones bajo incertidumbre del capítulo 8.

### 6.1.7. Ejemplo práctico guiado: definición de un agente para supervisión de una cadena de frío

Se diseñará un agente que supervise lotes sensibles durante almacenamiento y transporte refrigerado. Su propósito es recomendar respuestas ante indicios de pérdida de condiciones térmicas, sin sustituir la decisión sanitaria ni accionar por sí mismo sobre los productos.

**Paso 1. Delimitar frontera y autoridad.** El agente recibe telemetría de cámaras y vehículos, consulta datos del lote y puede recomendar una medición adicional, priorizar una inspección o proponer el aislamiento preventivo de un lote. El responsable de calidad autoriza el aislamiento y decide la liberación o descarte posterior. Esta frontera distingue la recomendación del agente de la intervención ejecutada por personal habilitado.

**Paso 2. Especificar PEAS.** La tarea se describe antes de elegir el algoritmo:

| Componente | Especificación |
|---|---|
| Desempeño | Reducir exposición térmica y tiempo de detección, evitar afectación de producto y limitar inspecciones, falsas alarmas y aislamientos innecesarios |
| Entorno | Cámaras refrigeradas, vehículos, lotes, turnos operativos, aperturas autorizadas, equipos de refrigeración y responsables de calidad |
| Actuadores | Emitir alertas; recomendar medición, inspección o aislamiento de lote; fijar prioridad e instante de reevaluación |
| Sensores | Temperatura, estado y duración de apertura de puerta, consumo y disponibilidad de energía, marcas temporales, autodiagnóstico del sensor e identificación del lote |

**Paso 3. Representar percepciones y calidad.** Cada observación incluye unidad, ubicación, lote asociado, marca temporal, latencia, calibración y validez. La serie térmica permite distinguir un valor aislado de una desviación persistente; la señal de puerta aporta una causa operativa posible; la telemetría de energía ayuda a reconocer una interrupción o un equipo que consume sin recuperar el rango esperado. Un dato ausente se representa como desconocido, no como una condición normal.

**Paso 4. Definir acciones y precondiciones.** El conjunto de recomendaciones es:

$$
A=\{\text{vigilar},\ \text{recomendar medici\'on},\ \text{recomendar inspecci\'on},\ \text{recomendar aislamiento de lote}\}.
$$

Recomendar una medición es apropiado cuando la evidencia es insuficiente o contradictoria. La inspección requiere una anomalía plausible que pueda confirmarse en el equipo, el recinto o el registro operativo. Recomendar aislamiento exige identificar los lotes potencialmente expuestos y superar un umbral de riesgo acordado; si la trazabilidad es incompleta, el agente debe abstenerse de afirmar qué unidades están afectadas y escalar el caso.

**Paso 5. Establecer desempeño.** Una medida ilustrativa, aplicada sobre magnitudes normalizadas, es:

$$
J=-(5E_T+4D_P+2T_D+C_I+3F+2A_I),
$$

donde $E_T$ es la exposición térmica acumulada, $D_P$ el daño esperado al producto, $T_D$ la demora de detección, $C_I$ el costo de inspección, $F$ las falsas alarmas y $A_I$ los aislamientos innecesarios. La inocuidad y los límites normativos son restricciones duras: no deben intercambiarse por ahorro operativo. Los coeficientes son hipótesis sujetas a validación con calidad, logística y mantenimiento.

**Paso 6. Explicitar conocimiento e incertidumbre.** El agente conoce rangos admisibles por tipo de producto, tolerancias temporales, historial de calibración, asociación entre lotes y ubicaciones, aperturas planificadas y comportamiento esperado del equipo. No observa directamente la temperatura interna de cada unidad ni puede asegurar una causa única. Mantiene, por tanto, una creencia sobre exposición y riesgo en vez de convertir toda alerta en certeza.

**Paso 7. Formular una política inicial auditable.** El siguiente pseudocódigo ilustra el ciclo percepción-decisión, no una implementación productiva:

```text
SI telemetría inválida, desactualizada O sin identificación confiable
    recomendar medición independiente y escalar la incertidumbre
SINO
    estimar exposición por lote con temperatura, puerta y energía
    SI desviación breve Y apertura autorizada Y recuperación normal
        vigilar y fijar instante de reevaluación
    SI desviación persistente O recuperación anómala
        recomendar inspección prioritaria
    SI riesgo del lote supera el umbral Y trazabilidad suficiente
        recomendar aislamiento para aprobación de calidad
```

**Paso 8. Probar escenarios.** Una lectura extrema aislada con autodiagnóstico defectuoso debe producir una solicitud de medición, no una conclusión sobre el producto. Una elevación sostenida tras una puerta abierta, acompañada de consumo energético alto y recuperación insuficiente, debe priorizar inspección. Una interrupción de energía con exposición prolongada y lotes bien identificados debe motivar la recomendación de aislamiento. Si no puede determinarse qué lotes estuvieron presentes, el agente debe comunicar esa incertidumbre y ampliar la revisión.

**Resultado de la especificación.** Se han declarado PEAS, percepciones, acciones, autoridad, conocimiento, restricciones, incertidumbre y desempeño. Quedan pendientes la calibración por producto, la validación retrospectiva con incidentes, las pruebas de sensores y trazabilidad, y los protocolos de ciberseguridad. La especificación define un agente racional respecto de información disponible; no promete diagnóstico omnisciente ni elimina la responsabilidad humana.

## 6.2. Entornos de tarea

El **entorno de tarea** es el problema externo para el cual se diseña el agente. Incluye condiciones físicas o informacionales, otros actores y reglas de evaluación. Caracterizarlo antes de elegir arquitectura evita, por ejemplo, aplicar reglas sin memoria cuando las observaciones son parciales o planificar sobre una dinámica que cambia más rápido que el cálculo.

### 6.2.1. Descripción PEAS

PEAS organiza la especificación en cuatro componentes: **medida de desempeño (P, performance)**, **entorno (E)**, **actuadores (A)** y **sensores (S)**. El orden comienza por desempeño para impedir que las capacidades tecnológicas definan por accidente el propósito.

| Componente | Contenido | Preguntas de control |
|---|---|---|
| Desempeño | Criterios de éxito, costos y restricciones | ¿Qué consecuencia se premia? ¿Para quién? ¿En qué horizonte? |
| Entorno | Objetos, procesos, actores y condiciones externas | ¿Qué puede cambiar sin control del agente? |
| Actuadores | Canales por los que el agente interviene | ¿Qué acciones son realmente ejecutables y reversibles? |
| Sensores | Fuentes de percepción y su calidad | ¿Qué se observa, con qué demora, error y cobertura? |

PEAS no es una lista de dispositivos. Debe capturar semántica y límites. «GPS» como sensor es insuficiente si no se especifican frecuencia, precisión y zonas sin cobertura. «Optimizar movilidad» como desempeño no indica si interesa tiempo total, regularidad, emisiones, accesibilidad o una combinación.

Un buen PEAS es consistente: cada criterio debe poder estimarse con alguna evidencia; cada acción debe corresponder a un actuador; cada supuesto sobre el entorno debe reflejarse en observaciones o incertidumbre. También debe señalar quién queda fuera de la frontera. En una flota, los pasajeros no son meros elementos físicos: poseen objetivos, reaccionan a recomendaciones y pueden alterar demanda.

PEAS es un documento vivo. Cambiar autoridad, incorporar un sensor o ampliar cobertura puede modificar la clase de entorno. Por ello se versiona junto con las políticas y pruebas del agente.

### 6.2.2. Entornos observables y parcialmente observables

Un entorno es **completamente observable** si la percepción contiene toda la información relevante para elegir racionalmente. Es **parcialmente observable** si sensores incompletos o ruidosos ocultan aspectos relevantes. La propiedad depende de la tarea y la representación, no de conocer cada detalle del universo.

En ajedrez, el tablero es observable: las piezas y posiciones están visibles, aunque no se conozca la futura jugada rival. En una red de agua subterránea, presión y caudal no revelan directamente ubicación y tamaño de una fuga. En movilidad, un mapa puede mostrar vehículos registrados, pero no intenciones de conductores ni demanda futura.

Cuando hay observabilidad parcial, el agente mantiene un **estado de creencia** $b_t(s)$, distribución sobre estados posibles:

$$
b_t(s)=P(S_t=s\mid p_{1:t},a_{1:t-1}).
$$

Tras ejecutar $a_t$ y observar $p_{t+1}$, combina modelo de transición y observación:

$$
b_{t+1}(s')\propto P(p_{t+1}\mid s')\sum_s P(s'\mid s,a_t)b_t(s).
$$

No siempre se requiere una distribución completa; pueden usarse intervalos, conjuntos de estados o resúmenes. Pero ocultar incertidumbre con una estimación puntual produce confianza falsa.

**Errores frecuentes.** Equiparar gran cantidad de datos con observabilidad completa; confundir variable no observada con inexistente; o usar información futura durante la evaluación. La observabilidad debe analizarse en el instante real de decisión y con sensores realmente disponibles.

### 6.2.3. Entornos deterministas y estocásticos

Un entorno es **determinista** si el estado siguiente queda fijado por estado actual y acción:

$$
s_{t+1}=T(s_t,a_t).
$$

Es **estocástico** si existen varios resultados con probabilidades:

$$
P(S_{t+1}=s'\mid S_t=s,A_t=a)=T(s'\mid s,a).
$$

La incertidumbre puede provenir de variabilidad física, actores externos o una representación que omite variables. Si un modelo de tráfico no incluye clima ni eventos, la transición parecerá aleatoria incluso si parte de la variación posee causas. Por eso «estocástico» describe el modelo al nivel adoptado, no una propiedad metafísica.

En entornos estratégicos, el resultado también depende de acciones de otros agentes. A veces se utiliza «no determinista» cuando se conocen resultados posibles pero no probabilidades. Esta distinción es práctica: con probabilidades se optimiza utilidad esperada; sin ellas puede emplearse robustez, peor caso o planificación contingente.

La verificación exige repetir o simular una misma condición y observar variación, pero nunca se reproducen exactamente todos los factores. Conviene separar incertidumbre **aleatoria**, asociada a variación irreducible del modelo, de incertidumbre **epistémica**, asociada a conocimiento insuficiente. Más datos pueden reducir la segunda, no necesariamente la primera.

Un error común es transformar una predicción más probable en transición segura. Si una ruta demora 20 minutos con probabilidad 0,6 y 45 con probabilidad 0,4, planificar siempre con 20 puede incumplir compromisos críticos. La distribución y la tolerancia al riesgo son parte de la decisión.

### 6.2.4. Entornos episódicos y secuenciales

En un entorno **episódico**, la experiencia se divide en episodios independientes: la acción de uno no afecta decisiones futuras. Clasificar imágenes independientes se aproxima a este caso si cada predicción no modifica datos ni usuarios. En un entorno **secuencial**, la acción actual cambia estados, información disponible u oportunidades posteriores.

La diferencia se expresa en el horizonte. Si el desempeño total es

$$
J=\sum_{t=0}^{H}r_t,
$$

una elección secuencial debe considerar efectos sobre términos futuros, no solo $r_t$. Asignar hoy la única cuadrilla a una tarea moderada puede impedir atender una emergencia dentro de una hora. Recomendar una ruta redistribuye tráfico y modifica demoras posteriores.

Las decisiones secuenciales introducen compromisos entre beneficio inmediato y futuro, acciones reversibles e irreversibles y valor de conservar opciones. También requieren memoria o una representación de estado suficiente. Un sistema que trata cada instante como episodio independiente puede oscilar: abrir y cerrar una válvula repetidamente porque ignora su acción anterior.

La episodicidad depende de la ventana. Una inspección aislada parece episodio, pero forma parte de un programa anual con presupuesto limitado. Antes de declarar independencia, se debe preguntar si la acción consume recursos, cambia el entorno, produce aprendizaje o afecta a otros casos.

### 6.2.5. Entornos estáticos y dinámicos

Un entorno es **estático** si no cambia mientras el agente delibera. Es **dinámico** si evoluciona durante ese intervalo. En un entorno **semidinámico**, el estado externo permanece, pero la medida de desempeño cambia con el tiempo, como en una prueba cronometrada.

La clasificación depende de la relación entre escalas temporales. Un problema puede considerarse estático si calcular toma milisegundos y el entorno cambia cada hora; la misma técnica deja de ser adecuada si deliberar requiere veinte minutos. La razón

$$
\rho=\frac{\text{tiempo de deliberaci\'on}}{\text{escala de cambio relevante}}
$$

ofrece una guía: cuanto mayor es $\rho$, más necesario resulta actualizar, interrumpir o actuar con una política de respaldo.

Los entornos dinámicos exigen marcas temporales, detección de datos obsoletos y ciclos de realimentación. Un plan debe incluir condiciones de invalidez: «esta ruta es válida durante cinco minutos si no se cierra el corredor». También puede ser necesario decidir mientras continúa la percepción, en vez de alternar fases rígidas de observar y actuar.

**Limitación.** Aumentar frecuencia no resuelve todo. Sensores más rápidos generan ruido y carga; actuadores tienen latencia; cambios excesivos producen inestabilidad. El diseño debe equilibrar capacidad de respuesta y persistencia, por ejemplo mediante histéresis o tiempos mínimos entre maniobras.

### 6.2.6. Entornos discretos y continuos

Un entorno es **discreto** cuando estados, percepciones, acciones o tiempo se representan mediante conjuntos contables. Es **continuo** cuando alguna dimensión relevante toma valores en intervalos. Un tablero de ajedrez es discreto; presión, velocidad y tiempo físico son continuos.

Las dimensiones pueden mezclarse. Un agente de bombeo observa presión continua, decide entre tres modos discretos y actúa en instantes cada cinco minutos. Por eso conviene caracterizar por separado:

| Dimensión | Posible representación |
|---|---|
| Estado | Nivel continuo o categorías bajo/normal/alto |
| Acción | Caudal continuo o encender/apagar |
| Tiempo | Continuo o intervalos de cinco minutos |
| Observación | Señal continua muestreada y cuantizada |

La discretización divide un continuo en regiones. Facilita búsqueda y verificación, pero introduce error. Si los intervalos son muy amplios, estados con riesgos distintos quedan unidos; si son muy finos, explota el número de combinaciones. Los umbrales cercanos a límites pueden causar cambios abruptos por ruido.

Una discretización defendible se basa en sensibilidad de la decisión: dos valores pueden compartir categoría si conducen a acciones equivalentes y cumplen las mismas restricciones. Deben documentarse resolución, tratamiento de fronteras y pérdida máxima tolerada. No basta con elegir intervalos «porque producen una tabla manejable».

### 6.2.7. Entornos monoagente y multiagente

En un entorno **monoagente**, el desempeño puede analizarse sin modelar decisiones de otras entidades como agentes. En uno **multiagente**, otros actores seleccionan acciones que afectan resultados. Pueden cooperar, competir o combinar ambas relaciones.

Una roca que bloquea una ruta pertenece al entorno, pero no es agente: no persigue una finalidad. Otro conductor sí puede serlo porque adapta su conducta. En movilidad, vehículos cooperan al respetar reglas y compiten por espacio. En mercados, participantes responden estratégicamente a precios. La política óptima depende entonces de expectativas sobre los demás.

Para agentes $i=1,\ldots,n$, la transición depende de una acción conjunta $\mathbf{a}=(a^1,\ldots,a^n)$ y cada uno puede tener utilidad $U_i(s,\mathbf{a})$. Si todos comparten utilidad, hay cooperación; si la ganancia de uno es pérdida de otro, aparece un caso competitivo de suma cero; la mayoría de aplicaciones no encaja por completo en ninguno.

Un reto central es la **no estacionariedad**: mientras un agente aprende, los demás también cambian, de modo que el entorno aparente deja de tener dinámica fija. Surgen además coordinación, comunicación, confianza y asignación de responsabilidad.

**Error frecuente.** Modelar personas como obstáculos pasivos. Usuarios y operadores interpretan recomendaciones, pueden rechazarlas y cambian de conducta ante incentivos. Ignorar esa adaptación produce políticas frágiles y, a veces, injustas.

### 6.2.8. Ejemplo práctico guiado: caracterización PEAS de un sistema de movilidad

Se especificará un agente que recomienda rutas a una flota de transporte a demanda. La recomendación no controla directamente a conductores ni garantiza tiempos.

**Paso 1. Definir desempeño.** Se propone minimizar tiempo de espera y retraso, kilómetros vacíos y emisiones, sujeto a seguridad, capacidad y cobertura mínima por zona. Se añaden percentil 90 de espera y diferencia máxima entre zonas para evitar que un buen promedio oculte servicio deficiente.

**Paso 2. Completar PEAS.**

| PEAS | Especificación del agente de movilidad |
|---|---|
| Desempeño | Espera media y P90, puntualidad, distancia vacía, cancelaciones, emisiones, cobertura territorial, cero violaciones de seguridad |
| Entorno | Red vial, vehículos, conductores, pasajeros, peatones, clima, obras, semáforos, regulación y eventos |
| Actuadores | Recomendar ruta, proponer reasignación, ajustar hora estimada, solicitar confirmación, abstenerse |
| Sensores | Posición y velocidad, solicitudes, ocupación, mapa, cierres, clima, aceptación del conductor y calidad de conexión |

**Paso 3. Clasificar con justificación.** Es parcialmente observable porque no se conocen demanda futura, intención de otros conductores ni todos los incidentes. Es estocástico: una misma ruta y salida producen demoras diferentes. Es secuencial: asignar un vehículo modifica cobertura posterior. Es dinámico porque el tráfico cambia durante el cálculo. Combina variables continuas y discretas. Es multiagente, pues conductores y pasajeros responden a recomendaciones.

**Paso 4. Identificar ambigüedades.** Si el agente solo informa rutas y cada conductor decide, «seguir ruta» no es un actuador directo; es una acción recomendada cuyo cumplimiento debe observarse. Si la evaluación usa tiempos finales, estos no pueden introducirse retrospectivamente como percepción inicial.

**Paso 5. Derivar requisitos.** La observabilidad parcial requiere estimar estado e incertidumbre. El dinamismo exige caducidad y replanificación. La secuencialidad obliga a considerar disponibilidad futura. La interacción exige modelar aceptación y evitar concentrar vehículos en la misma ruta. Las restricciones de seguridad deben imponerse antes de optimizar tiempo.

**Escenario de prueba.** Dos rutas tienen estimaciones: A, 15 minutos con alta variabilidad; B, 19 minutos estable. Para un traslado con compromiso crítico, recomendar A solo por menor media puede ser inadecuado. El agente debe considerar la variabilidad de la demora y el costo de llegar tarde. Si 30 vehículos reciben A simultáneamente, la recomendación modifica el entorno; una predicción que supone tráfico constante deja de ser válida.

El ejemplo muestra que PEAS y las seis dimensiones no son etiquetas decorativas. De ellas se desprenden memoria, actualización temporal, tratamiento probabilístico, coordinación y criterios de prueba.

## 6.3. Arquitecturas de agentes

Una arquitectura de agente organiza la transformación de percepciones en acciones. Las categorías siguientes no son productos excluyentes: un sistema real puede combinar reacción rápida, modelo interno, planificación, utilidad y aprendizaje. La elección depende del entorno, las garantías necesarias y el costo de construir y mantener cada componente.

### 6.3.1. Agentes reactivos simples

Un **agente reactivo simple** selecciona una acción a partir de la percepción actual mediante reglas condición-acción:

$$
a_t=g(p_t).
$$

Ejemplos son «si la temperatura supera el límite, apagar» o «si hay obstáculo inmediato, detener». No mantiene un modelo explícito del pasado. Su fortaleza es la respuesta rápida, trazable y de bajo costo computacional.

```text
PARA CADA regla EN reglas ordenadas
    SI regla.condición coincide con percepción actual
        devolver regla.acción
devolver acción segura por defecto
```

La prioridad entre reglas debe ser explícita. Si «continuar servicio» y «detener por seguridad» se activan juntas, la segunda debe prevalecer. También se requiere una acción por defecto para condiciones no cubiertas.

Esta arquitectura es adecuada en entornos suficientemente observables, con relaciones estables y decisiones locales. Falla cuando la misma percepción corresponde a estados distintos. Una lectura normal puede significar «todo funciona» o «el sensor quedó congelado»; sin historia no se distingue. También puede oscilar cerca de un umbral. La histéresis reduce oscilación, pero ya introduce memoria mínima.

**Error frecuente.** Creer que más reglas solucionan cualquier caso. Una base creciente desarrolla conflictos, huecos y combinaciones difíciles de verificar. Si la decisión depende sistemáticamente del pasado o de consecuencias futuras, corresponde cambiar de arquitectura, no acumular excepciones.

### 6.3.2. Agentes reactivos basados en modelos

Un **agente reactivo basado en modelos** mantiene un estado interno que resume aspectos no observados directamente. Actualiza ese estado con percepción, acción anterior y conocimiento de cómo evoluciona el entorno:

$$
m_t=U(m_{t-1},a_{t-1},p_t), \qquad a_t=g(m_t).
$$

El modelo posee al menos dos partes: un **modelo de transición**, que anticipa efectos de acciones y cambios externos, y un **modelo de observación**, que relaciona estados con percepciones. El estado interno puede ser simbólico («válvula probablemente cerrada»), numérico o probabilístico.

En inspección de tuberías, una caída gradual de presión y la acción previa de aumentar bombeo permiten inferir un estado distinto al sugerido por la lectura actual sola. Si falta una lectura, el modelo proyecta temporalmente el estado, pero su incertidumbre debe crecer.

La ventaja es operar bajo observabilidad parcial sin planificar extensamente. La limitación es que una reacción sobre estado estimado sigue siendo local: no compara necesariamente secuencias de acciones. Además, un modelo incorrecto acumula error. Por ello se necesitan sincronización temporal, detección de deriva y corrección con observaciones.

Conviene registrar no solo el valor estimado, sino su confianza y procedencia. Un estado interno opaco puede parecer conocimiento cierto cuando solo extrapola datos antiguos.

### 6.3.3. Agentes orientados a objetivos

Un **agente orientado a objetivos** selecciona acciones considerando estados deseados. Además de estimar el estado actual, pregunta qué secuencia puede alcanzar una condición objetivo $G$. Si $Goal(s)$ indica que $s$ satisface el objetivo, el agente busca una sucesión:

$$
s_0\xrightarrow{a_0}s_1\xrightarrow{a_1}\cdots\xrightarrow{a_{k-1}}s_k,
\qquad Goal(s_k)=verdadero.
$$

Esta arquitectura separa «qué se quiere» de «cómo lograrlo». Puede adaptarse a objetivos nuevos sin reescribir todas las reglas. En logística, el objetivo puede ser que tareas urgentes queden asignadas y todos los recursos regresen dentro del horario.

Sin embargo, alcanzar un objetivo no distingue caminos. Dos planes pueden ser factibles, pero uno consumir diez veces más recursos. Tampoco resuelve por sí solo objetivos incompatibles. «Llegar» y «llegar con seguridad» deben expresarse mediante restricciones y costos, no confiar en que el planificador los infiera.

La planificación requiere un modelo de acciones y puede ser costosa. En entornos dinámicos se combina con reacción: un plan proporciona dirección global y reglas de seguridad responden a eventos inmediatos. El capítulo 7 desarrollará algoritmos para explorar estos espacios y comparar estrategias de búsqueda.

### 6.3.4. Agentes basados en utilidad

Un **agente basado en utilidad** asigna valor a consecuencias y elige entre alternativas que alcanzan objetivos con diferente calidad. Una función $U(s)$ representa preferencia sobre estados; bajo incertidumbre se maximiza utilidad esperada:

$$
a^*=\arg\max_a\sum_{s'}P(s'\mid s,a)U(s').
$$

La utilidad permite intercambios entre tiempo, costo, riesgo y calidad. No es necesariamente dinero ni una medida objetiva. Debe reflejar preferencias coherentes de las partes responsables. Si hay múltiples criterios normalizados $x_j$, puede usarse provisionalmente:

$$
U(s)=\sum_{j=1}^{m}w_j u_j(x_j(s)),
$$

pero una suma ponderada admite compensaciones. Una gran mejora en tiempo podría compensar matemáticamente una violación de seguridad; por ello las restricciones duras se aplican fuera de la utilidad.

La forma de $u_j$ expresa actitud ante riesgo y rendimientos decrecientes. Los pesos no deben escogerse solo por conveniencia: requieren consulta, análisis de sensibilidad y documentación. Si pequeños cambios alteran la acción, la decisión es frágil.

Los agentes de utilidad son apropiados con incertidumbre y objetivos graduados, pero plantean riesgos normativos. Agregar bienestar puede ocultar distribución: mejorar mucho a un grupo y empeorar poco a muchos quizá produzca igual suma. Se necesitan métricas de equidad, límites y mecanismos de impugnación.

### 6.3.5. Agentes que aprenden

Un **agente que aprende** modifica algún componente de su conducta a partir de experiencia. Puede aprender el modelo de observación, la transición, reglas, función de evaluación o política. Aprender no constituye una arquitectura completa por sí solo: especifica cómo cambia el agente.

Sea $\theta_t$ el conjunto de parámetros o conocimiento. Una actualización general es:

$$
\theta_{t+1}=L(\theta_t,\text{experiencia}_t,\text{retroalimentaci\'on}_t).
$$

La experiencia puede ser supervisada, cuando existe una respuesta de referencia; no supervisada, cuando se descubren estructuras; o basada en recompensas, cuando las consecuencias llegan después de actuar. Este último caso se estudiará en el capítulo 8.

Aprender aporta adaptación a condiciones locales y cambios difíciles de codificar. No garantiza mejora: datos sesgados, objetivos mal definidos o retroalimentación tardía pueden degradar conducta. La distribución cambia además porque las acciones del agente alteran qué datos se observan. Si solo se inspeccionan zonas que el modelo marca como riesgosas, faltará evidencia sobre las demás.

La operación segura exige separar entrenamiento y evaluación, comparar con una línea base, detectar deriva, conservar versiones y permitir reversión controlada. En ámbitos críticos, el aprendizaje puede proponer ajustes mientras reglas verificadas limitan acciones. Autonomía no significa actualización irrestricta en producción.

### 6.3.6. Componentes de aprendizaje, crítica y exploración

Una descomposición clásica incluye cuatro componentes:

- el **elemento de desempeño** selecciona acciones con el conocimiento actual;
- el **elemento de aprendizaje** modifica ese conocimiento;
- el **crítico** compara resultados con la medida de desempeño y produce retroalimentación;
- el **generador de problemas** propone acciones exploratorias que aportan información.

El crítico no es simplemente el entorno. El entorno produce consecuencias; el crítico las interpreta según objetivos. Una demora de cinco minutos puede ser aceptable o grave según contexto. Si la señal del crítico premia una aproximación incorrecta, el aprendizaje optimizará el sustituto.

La **exploración** sacrifica potencialmente desempeño inmediato para conocer alternativas; la **explotación** usa la mejor alternativa conocida. Explorar sin límites puede causar daño; no explorar consolida errores y desconoce cambios. Se puede restringir exploración a simulación, rangos seguros, periodos de baja demanda o acciones reversibles.

| Componente | Pregunta de auditoría | Falla típica |
|---|---|---|
| Desempeño | ¿Cómo se elige la acción ahora? | Política no alineada con restricciones |
| Aprendizaje | ¿Qué se actualiza y con qué datos? | Aprender correlaciones espurias |
| Crítico | ¿Quién define éxito y cuándo se observa? | Recompensa incompleta o tardía |
| Exploración | ¿Qué incertidumbre intenta reducir? | Riesgo injustificado o exploración inútil |

La retroalimentación puede estar demorada y confundida: tras cambiar una ruta, clima y demanda también cambian. Atribuir todo resultado a la acción genera aprendizaje causal incorrecto. Deben registrarse contexto, política activa y probabilidad con que se eligió la acción.

### 6.3.7. Ejemplo práctico guiado: comparación de arquitecturas

Se comparan cinco versiones de un agente que recomienda mantenimiento para aerogeneradores. Todas reciben vibración, temperatura de rodamientos, potencia producida, velocidad del viento, alarmas del controlador, historial de intervenciones y disponibilidad de técnicos. La acción puede ser continuar vigilancia, solicitar una prueba, programar mantenimiento o recomendar una parada segura.

**Versión A, reactiva simple.** Aplica reglas a la percepción actual: si la vibración supera un umbral, eleva la prioridad; si alcanza un límite de seguridad, recomienda parada. Responde con poca latencia y sus reglas son fáciles de auditar, pero no distingue un sensor defectuoso de un deterioro real ni integra señales débiles acumuladas.

**Versión B, basada en modelo.** Mantiene un estado interno con tendencia de vibración, régimen de operación, calidad de sensores, intervenciones recientes y condición probable de componentes. Puede explicar una temperatura elevada por carga y ambiente, o considerar más preocupante una anomalía persistente en condiciones comparables. Tolera observación parcial, aunque introduce errores si el modelo de degradación está mal especificado.

**Versión C, orientada a objetivos.** Planifica acciones para alcanzar estados verificables, por ejemplo, diagnosticar todos los equipos de riesgo alto y completar el mantenimiento obligatorio antes de una fecha. Puede ordenar pruebas, ventanas de parada e intervenciones según precedencias y recursos. Satisface metas, pero dos planes que llegan al mismo objetivo parecen equivalentes si la representación no incorpora sus consecuencias económicas y operativas.

**Versión D, basada en utilidad.** Compara resultados graduados mediante su utilidad esperada. Pondera riesgo de falla, energía no producida, costo de movilización, demora y oportunidad de agrupar intervenciones, bajo restricciones no negociables de seguridad. Permite elegir entre mantenimiento inmediato y una prueba informativa, pero requiere probabilidades calibradas y acuerdos explícitos sobre intercambios entre criterios.

**Versión E, con aprendizaje.** Ajusta estimadores de degradación o políticas de prioridad usando inspecciones, reemplazos y fallas observadas. Puede reconocer patrones específicos de un modelo de aerogenerador y adaptarse al envejecimiento. Su calidad depende de etiquetas, cobertura y retroalimentación: si solo se inspeccionan los casos previamente priorizados, el conjunto de aprendizaje queda sesgado. Debe compararse con una línea base, vigilar deriva y conservar límites de seguridad no aprendidos.

| Criterio | Reactiva | Basada en modelo | Orientada a objetivos | Basada en utilidad | Con aprendizaje |
|---|---:|---:|---:|---:|---:|
| Respuesta inmediata | Alta | Alta | Media | Media | Depende de la política |
| Manejo de observación parcial | Bajo | Alto | Depende del estado | Alto si se modela | Alto con datos representativos |
| Planificación temporal | Nula | Baja | Alta | Alta | Depende del elemento de desempeño |
| Comparación de costos y riesgos | Implícita | Limitada | Limitada | Explícita | Aprendida o combinada |
| Adaptación a cambios | Baja | Media | Media | Media | Alta con control |
| Facilidad de auditoría | Alta | Media/alta | Media | Media | Variable |

**Prueba guiada.** El aerogenerador A presenta un pico extremo de vibración, pero el sensor informa baja confiabilidad y las variables restantes son normales. El B muestra un aumento moderado y sostenido de vibración y temperatura bajo cargas comparables, con una ventana de bajo viento prevista para el día siguiente. El agente reactivo prioriza A por umbral. El basado en modelo reduce la certeza sobre A y eleva el riesgo estimado de B. El orientado a objetivos programa una prueba inmediata de A y reserva la ventana para diagnosticar B. El basado en utilidad compara el valor de la información, el riesgo de esperar y la pérdida de producción. El agente con aprendizaje puede refinar la probabilidad de degradación de B a partir de casos históricos semejantes, sin sobrepasar las reglas de seguridad.

**Conclusión de diseño.** Ninguna arquitectura domina en todos los criterios. Una solución híbrida puede usar reglas verificadas para protección inmediata, un modelo para mantener creencias sobre componentes, objetivos para construir el plan, utilidad para ordenar alternativas y aprendizaje para actualizar estimaciones. Cada capa debe aportar una mejora medible: añadir complejidad sin pruebas, trazabilidad ni datos adecuados solo agrega modos de falla.

## 6.4. Representación computacional de problemas

Diseñar un agente requiere transformar una situación abierta en una representación sobre la que sea posible razonar. Una formulación clásica de problema es:

$$
\mathcal{P}=(S,A,T,s_0,G,C,R),
$$

donde $S$ es el espacio de estados, $A$ las acciones, $T$ el modelo de transición, $s_0$ el estado inicial, $G$ la condición objetivo, $C$ los costos y $R$ las restricciones. Esta tupla no es la realidad: es un instrumento. Su validez depende de conservar las distinciones que cambian decisiones.

### 6.4.1. Estados y variables de estado

Un **estado** reúne la información necesaria para predecir las consecuencias relevantes de acciones futuras y evaluar objetivos. Las **variables de estado** son sus componentes. Si $X_1,\ldots,X_n$ tienen dominios $D_1,\ldots,D_n$, entonces:

$$
s=(x_1,\ldots,x_n)\in S\subseteq D_1\times\cdots\times D_n.
$$

En asignación de cuadrillas, un estado puede incluir tareas pendientes, ubicación y disponibilidad de cada cuadrilla, tiempo actual y presupuesto restante. No necesita contener color de los vehículos si ese dato no afecta acciones, costos ni restricciones.

Un buen estado posee **suficiencia**: dado el estado actual y una acción, el pasado no aporta información adicional relevante para la transición. Esta es una propiedad de Markov respecto del modelo:

$$
P(S_{t+1}\mid S_{0:t},A_{0:t})=P(S_{t+1}\mid S_t,A_t).
$$

Si duración futura depende de desgaste acumulado y el estado solo guarda ubicación, no es suficiente. Se debe incorporar desgaste o una estadística que lo resuma.

También se distingue **estado del mundo**, que existe aunque no se observe; **percepción**, que aporta evidencia; **estado interno**, que estima o resume; y **nodo de búsqueda**, que además puede guardar padre, acción y costo. Confundirlos causa duplicación o uso indebido de información.

El tamaño del espacio crece multiplicativamente. Diez variables con diez valores producen hasta $10^{10}$ estados. Deben eliminarse combinaciones imposibles mediante restricciones y escoger variables relevantes, sin omitir aquellas que cambian factibilidad o costo.

### 6.4.2. Acciones y modelos de transición

Una **acción** transforma potencialmente un estado. Se especifica mediante nombre, parámetros, precondiciones y efectos. Para asignar una cuadrilla $q$ a una tarea $j$:

```text
ACCIÓN asignar(q, j)
PRECONDICIONES:
    q está disponible
    j está pendiente
    q posee habilidades requeridas por j
    el desplazamiento permite cumplir la ventana temporal
EFECTOS:
    j pasa a asignada
    q pasa a ocupada y cambia su destino
    se actualizan tiempo y presupuesto estimados
```

Las precondiciones determinan $A(s)$, acciones aplicables en $s$. Los efectos definen una transición determinista $T(s,a)=s'$ o una distribución $T(s'\mid s,a)$. En dominios inciertos, «inspeccionar» puede confirmar falla, descartar alerta o resultar inconcluso.

Debe distinguirse acción de evento exógeno. El agente asigna una cuadrilla; la lluvia o una nueva emergencia ocurren fuera de su control. Ambos cambian estado, pero atribuir eventos al agente distorsiona responsabilidad y planificación.

La transición debe conservar **invariantes**, propiedades verdaderas en todo estado legal: una cuadrilla no ocupa dos lugares simultáneamente; el presupuesto no es negativo; una tarea terminada no está pendiente. Las pruebas de modelo comprueban que toda acción aplicable produzca estados legales y que sus efectos correspondan al dominio.

**Error frecuente.** Especificar efectos favorables e ignorar efectos secundarios. Asignar consume tiempo, combustible y oportunidad. Si no se representan, el algoritmo puede reutilizar recursos ilimitadamente.

### 6.4.3. Estado inicial y estados objetivo

El **estado inicial** $s_0$ describe desde dónde comienza la resolución. Debe corresponder al instante de decisión y distinguir datos desconocidos. Si hay incertidumbre inicial, puede usarse un conjunto $S_0$ o una distribución $b_0(s)$, en vez de inventar valores.

Un **estado objetivo** satisface una prueba $Goal(s)$. Habitualmente hay un conjunto:

$$
G=\{s\in S:Goal(s)=verdadero\}.
$$

En asignación, «todas las tareas críticas cubiertas, ninguna restricción violada y cuadrillas dentro del turno» es condición; no exige una asignación única. Separar condición de un estado concreto permite descubrir soluciones alternativas.

Los objetivos pueden ser de logro («entregar suministro»), mantenimiento («presión siempre en rango») o evitación («nunca exceder capacidad»). Los de mantenimiento no se reducen fácilmente a alcanzar un estado final; se evalúan sobre trayectorias. También puede haber metas parciales y plazos.

Una formulación debe responder:

- ¿el estado inicial es legal y está fechado?;
- ¿el objetivo puede verificarse con variables representadas?;
- ¿existe al menos una solución en casos normales?;
- ¿qué ocurre si el objetivo es inalcanzable?;
- ¿terminar pronto tiene valor o solo importa llegar?;

Confundir objetivo con método restringe innecesariamente. «Usar la cuadrilla Q1» no es objetivo salvo que exista una razón de dominio; «resolver la tarea con personal habilitado» deja al algoritmo elegir.

### 6.4.4. Costos, restricciones y utilidad

El **costo de acción** $c(s,a,s')$ cuantifica recursos o consecuencias negativas. El costo de una trayectoria $\pi=(s_0,a_0,\ldots,s_k)$ suele ser aditivo:

$$
C(\pi)=\sum_{t=0}^{k-1}c(s_t,a_t,s_{t+1}).
$$

Puede representar tiempo, distancia, dinero o riesgo esperado. La aditividad es un supuesto: fatiga o descuentos por volumen pueden depender de la trayectoria completa y exigir ampliar el estado o usar otra función.

Una **restricción** define qué estados, acciones o trayectorias son admisibles. Las restricciones duras no pueden violarse; las blandas admiten incumplimiento penalizado. Declarar una condición legal como «costo muy alto» es peligroso: si otras ganancias son mayores, el optimizador la violará.

La **utilidad** expresa preferencia por consecuencias, incluida incertidumbre. Costos y utilidad se relacionan, pero no son idénticos. Minimizar costo puede equivaler a maximizar $-C$ en un caso simple; utilidad permite no linealidad, riesgo y valor de resultados. En problemas deterministas de alcance, costo suele bastar. En decisiones inciertas, la utilidad esperada es más adecuada.

| Concepto | Función | Ejemplo |
|---|---|---|
| Restricción dura | Excluir alternativas | Solo personal certificado atiende alta tensión |
| Restricción blanda | Desalentar, pero permitir | Preferir equilibrio de carga |
| Costo | Comparar consumo acumulado | Kilómetros y horas extra |
| Utilidad | Valorar consecuencias y riesgo | Beneficio de reducir daño crítico |

Las magnitudes deben compartir escala si se agregan. Los pesos requieren análisis de sensibilidad. Una precisión aparente como $0{,}37$ para «equidad» no sustituye la discusión sobre su significado.

### 6.4.5. Nivel de abstracción

La **abstracción** conserva rasgos relevantes y omite detalles. Un mapa de rutas representa conexiones y costos, no cada centímetro del pavimento. Sin abstracción, el problema puede ser intratable; con demasiada, la solución puede ser imposible o insegura en el mundo real.

Una abstracción es adecuada para una decisión si estados considerados equivalentes admiten acciones equivalentes y consecuencias relevantes comparables. Si dos cuadrillas se agrupan como «disponibles» pero solo una posee certificación, la abstracción elimina una restricción decisiva.

Se puede trabajar en niveles:

1. estratégico: cuántos recursos reservar por zona;
2. táctico: qué cuadrilla asignar a cada tarea;
3. operativo: ruta exacta y secuencia de maniobras.

La planificación jerárquica resuelve primero decisiones gruesas y refina después. Cada nivel debe declarar interfaces: una asignación táctica debe ser realizable en el nivel operativo.

Para validar la abstracción se toman soluciones abstractas y se intenta ejecutarlas o refinarlas en casos representativos y extremos. Si muchas fallan por detalles omitidos, el nivel no es adecuado. También se compara sensibilidad: incorporar una variable supuestamente irrelevante no debería cambiar decisiones de manera sistemática.

**Tensión fundamental.** Agregar detalle aumenta fidelidad y costo; eliminarlo mejora tractabilidad y puede introducir sesgo. No existe representación «completa». La pregunta correcta es si es suficiente para el propósito, horizonte y riesgo.

### 6.4.6. Introducción a la representación del conocimiento

La representación de problemas describe configuraciones y transformaciones; la **representación del conocimiento** organiza hechos, conceptos, relaciones y reglas que permiten inferir información no explícita. Un agente necesita saber no solo dónde está, sino qué significa una entidad, qué propiedades hereda y qué condiciones se cumplen.

Formas frecuentes incluyen:

- **lógica proposicional:** hechos verdaderos o falsos, como $SensorActivo$;
- **lógica de predicados:** objetos y relaciones, como $habilitado(q,t)$;
- **reglas de producción:** «si condición, entonces conclusión o acción»;
- **grafos semánticos y ontologías:** conceptos, relaciones y jerarquías;
- **representaciones probabilísticas:** creencias inciertas y dependencias;
- **vectores distribuidos:** similitud aprendida, con semántica menos explícita.

Una base de conocimiento puede contener:

$$
Certificado(q,agua)\land Requiere(t,agua)\Rightarrow Elegible(q,t).
$$

La inferencia deriva $Elegible(q,t)$ si se conocen ambas premisas. Debe distinguirse **mundo cerrado**, donde lo no registrado se asume falso, de **mundo abierto**, donde permanece desconocido. En seguridad, no encontrar una certificación no equivale a confirmar que no exista; pero tampoco autoriza a actuar. La política debe tratar explícitamente el desconocimiento.

Los criterios de calidad son expresividad, consistencia, eficiencia inferencial, explicabilidad y facilidad de actualización. Mayor expresividad puede hacer más costosa la inferencia. Las ontologías requieren gobernanza de términos; las reglas pueden entrar en conflicto; las representaciones aprendidas pueden reproducir sesgos y dificultar explicación.

Esta introducción no pretende cubrir todo el campo. Su propósito es mostrar que formular estados y acciones presupone vocabulario, relaciones y supuestos. Una mala semántica no se corrige con un algoritmo de búsqueda más potente.

### 6.4.7. Ejemplo práctico guiado: formulación de un problema de asignación de recursos

Un centro de datos debe asignar tres técnicos a cuatro intervenciones durante un turno. Las competencias relevantes son redes, energía y refrigeración. Cada intervención tiene duración, ubicación interna, ventana temporal, prioridad y habilidades requeridas; cada técnico posee competencias, certificaciones, horario y costo. Se busca completar las intervenciones críticas y minimizar demora, desplazamiento interno y horas extra sin vulnerar reglas de seguridad.

**Paso 1. Declarar alcance y abstracción.** El horizonte es un turno de ocho horas. Se decide quién atiende cada intervención y en qué orden, pero no se representan movimientos dentro de una sala ni pasos detallados del procedimiento técnico. Las duraciones se tratan inicialmente como deterministas. Esta abstracción es válida solo si la variabilidad no altera de forma sistemática la factibilidad de la agenda.

**Paso 2. Definir variables.** Sea $x_{ijt}=1$ si el técnico $i$ inicia la intervención $j$ en el bloque temporal $t$, y $0$ en otro caso. Para una formulación como búsqueda, un estado puede expresarse como:

$$
s=(t,\operatorname{pendientes},\operatorname{estado}_T,\operatorname{ubicaci\'on}_T,\operatorname{liberaci\'on}_T,\operatorname{presupuesto}),
$$

donde $\operatorname{estado}_T$ indica si cada técnico está disponible u ocupado y $\operatorname{liberaci\'on}_T$ conserva cuándo terminará su trabajo actual. La ubicación permite calcular el tiempo de acceso entre salas; omitir la liberación impediría decidir correctamente acciones posteriores.

**Paso 3. Estado inicial y conocimiento.** A las 08:00 los tres técnicos están disponibles, las cuatro intervenciones están pendientes y el presupuesto permanece completo. La base de conocimiento registra `Posee(técnico, habilidad)`, `Certificado(técnico, intervención)` y `Requiere(intervención, habilidad)`. Una competencia o certificación no registrada se considera desconocida y bloquea la asignación hasta su verificación; no se presume habilitación por ausencia de datos.

**Paso 4. Acciones y transición.** Las acciones son `asignar(técnico, intervención, inicio)`, `asignar_equipo(par, intervención, inicio)`, `esperar(hasta)` y `solicitar_dato(elemento)`. Asignar exige disponibilidad, habilidades, certificación, acceso autorizado, tiempo suficiente y presupuesto. La transición ocupa al técnico durante la duración prevista, actualiza su futura ubicación, retira la intervención de pendientes al completarse y descuenta el costo. Una intervención que exige dos personas produce una transición conjunta, no dos decisiones independientes.

**Paso 5. Formular restricciones duras.** Sea $n_j$ la cantidad de técnicos exigida por la intervención $j$, igual a dos para un trabajo en pareja y a uno en los demás casos. La cobertura válida requiere:

$$
\sum_i\sum_t x_{ijt}=n_j.
$$

Si $r_{jk}=1$ indica que $j$ requiere la habilidad $k$ y $h_{ik}=1$ que $i$ la posee, entonces $x_{ijt}\leq h_{ik}$ para toda habilidad que deba poseer cada participante. En trabajos donde las competencias puedan complementarse, se exige $\sum_i h_{ik}x_{ijt}\geq r_{jk}$ para cada $k$. Además, un técnico no puede atender intervenciones solapadas; los participantes de un trabajo en pareja deben iniciar juntos y permanecer disponibles durante todo el intervalo. También se respetan ventanas, precedencias, descansos, certificaciones, aforo de sala y presupuesto. Estas condiciones no se sustituyen por penalizaciones, porque una solución barata pero insegura sigue siendo inadmisible.

**Paso 6. Definir objetivo y costo.** Primero se exige que todas las intervenciones críticas queden terminadas dentro de su ventana. Entre soluciones factibles se minimiza:

$$
C=\sum_j\left(3D_j+1{,}5M_j+4H_j+2R_j\right),
$$

donde $D_j$ es demora normalizada, $M_j$ tiempo de desplazamiento interno, $H_j$ horas extra y $R_j$ costo de reasignar o interrumpir trabajo planificado. También puede añadirse el costo laboral específico de cada técnico. La prioridad crítica actúa como restricción temporal cuando existe un límite operativo, no solo como coeficiente alto.

**Paso 7. Construir una instancia pequeña.**

| Intervención | Prioridad | Duración | Habilidad requerida | Condición | Límite |
|---|---:|---:|---|---|---:|
| I1: reemplazo de conmutador | Crítica | 1 h | Redes | Una persona | 10:00 |
| I2: revisión de UPS | Crítica | 2 h | Energía | Dos personas; una certificada | 13:00 |
| I3: diagnóstico de unidad térmica | Alta | 2 h | Refrigeración | Una persona | 16:00 |
| I4: verificación de enlaces y sensores | Media | 1 h | Redes y refrigeración | Una persona con ambas | 17:00 |

T1 posee redes y refrigeración; T2 posee energía y la certificación de UPS; T3 posee energía y refrigeración. Asignar temprano I3 a T3 y ocupar T1 en I4 puede dejar a T2 sin acompañante para I2 antes de las 13:00. Una solución candidata asigna I1 a T1 de 08:00 a 09:00, I2 a T2 y T3 de 09:00 a 11:00, I3 a T3 de 11:00 a 13:00 e I4 a T1 posteriormente. La secuencia conserva la competencia escasa de energía conjunta para la intervención crítica.

**Paso 8. Validar la formulación.** Tras cada transición se comprueban invariantes: nadie aparece en dos lugares a la vez, toda habilidad requerida está cubierta, las tareas en pareja comparten intervalo, el presupuesto no es negativo y ninguna intervención completada reaparece como pendiente. Se prueban ausencia de T2, demora de I1, llegada de una alarma crítica y una certificación desconocida. Si el modelo declara factible una agenda que viola acceso, simultaneidad o tiempos de traslado, falta una variable o restricción.

**Paso 9. Reconocer límites.** Las duraciones pueden variar, pueden surgir incidentes y la competencia nominal no refleja toda la experiencia. La formulación es apropiada como punto de partida para búsqueda y optimización; la operación real requerirá replanificación ante eventos y conservación del historial de decisiones. En el capítulo 7, los estados podrán tratarse como nodos y las asignaciones como aristas; en el capítulo 8, la incertidumbre y los costos esperados permitirán comparar políticas de reasignación.

## Síntesis integradora

Un agente se define por el ciclo entre percepción y acción, pero su inteligencia solo puede evaluarse respecto de una tarea. La función de agente especifica conducta idealizada; el programa la implementa bajo límites. La racionalidad maximiza desempeño esperado con información disponible y no exige acertar siempre. La autonomía indica cuánto se apoya el agente en experiencia propia, mientras que la omnisciencia es una referencia imposible.

PEAS obliga a comenzar por consecuencias y a conectar entorno, actuadores y sensores. Las dimensiones del entorno no son etiquetas absolutas: dependen de frontera, abstracción y escala temporal. De ellas se derivan requisitos arquitectónicos. Reglas simples son valiosas cuando bastan; modelos internos ayudan con observación parcial; objetivos permiten planificar; utilidad compara resultados graduados; aprendizaje adapta el comportamiento, pero añade riesgos de retroalimentación y deriva.

Representar un problema es decidir qué diferencias importan. Estados suficientes, acciones ejecutables, transiciones plausibles, objetivos verificables, restricciones explícitas y costos alineados forman el puente entre una necesidad real y un algoritmo. Una representación demasiado pobre produce soluciones inválidas; una excesiva puede impedir calcular. La calidad se demuestra mediante invariantes, escenarios adversos, sensibilidad y posibilidad de traducir la solución al mundo real.

## Errores comunes y criterios de revisión

| Error | Consecuencia | Pregunta correctiva |
|---|---|---|
| Confundir predicción con acción | No se define responsabilidad ni efecto | ¿Quién decide y quién ejecuta? |
| Medir actividad en vez de resultado | El agente optimiza un indicador vacío | ¿Qué mejora realmente en el entorno? |
| Evaluar con información futura | Se sobreestima racionalidad y desempeño | ¿Estaba ese dato disponible al decidir? |
| Suponer observabilidad por tener muchos datos | Se oculta incertidumbre relevante | ¿Qué estados distintos generan la misma percepción? |
| Tratar una transición probable como segura | Planes frágiles ante variabilidad | ¿Qué otros resultados son plausibles y costosos? |
| Optimizar cada instante por separado | Se consumen opciones y recursos futuros | ¿Cómo cambia esta acción decisiones posteriores? |
| Penalizar en vez de prohibir una ilegalidad | El optimizador puede aceptar la violación | ¿Es preferencia o condición no negociable? |
| Omitir efectos secundarios | Se reutilizan recursos o se ignora desgaste | ¿Qué cambia además del efecto principal? |
| Añadir reglas sin revisar arquitectura | Conflictos y huecos difíciles de auditar | ¿La decisión requiere memoria o planificación? |
| Aprender sin un crítico válido | Se perfecciona un objetivo sustituto | ¿La retroalimentación representa el resultado? |

## Glosario

- **Acción:** decisión disponible para un agente que puede modificar el entorno.
- **Actuador:** mecanismo físico o lógico que intenta ejecutar una acción.
- **Agente:** entidad que percibe un entorno y selecciona acciones sobre él.
- **Arquitectura:** soporte de cómputo, memoria, comunicación, sensores y actuadores donde opera el programa.
- **Autonomía:** grado en que la conducta depende de experiencia propia y no solo de conocimiento inicial.
- **Costo:** valoración de recursos o consecuencias negativas de una acción o trayectoria.
- **Crítico:** componente que convierte resultados observados en retroalimentación respecto del desempeño.
- **Entorno de tarea:** ámbito externo, actores y condiciones relevantes para evaluar y operar el agente.
- **Estado:** resumen de información suficiente para razonar sobre transiciones, objetivos y costos.
- **Estado de creencia:** distribución o conjunto que representa incertidumbre sobre el estado real.
- **Exploración:** selección de acciones para obtener información sobre alternativas inciertas.
- **Función de agente:** correspondencia abstracta entre secuencias de percepciones y acciones.
- **Medida de desempeño:** criterio que evalúa consecuencias de la conducta del agente.
- **Modelo de observación:** relación entre estados del entorno y percepciones posibles.
- **Modelo de transición:** descripción de cómo cambian los estados por acciones y eventos.
- **Objetivo:** condición sobre estados o trayectorias que define un resultado deseado.
- **Omnisciencia:** conocimiento perfecto del estado, consecuencias y futuro; no es requisito de racionalidad.
- **PEAS:** descripción mediante desempeño, entorno, actuadores y sensores.
- **Percepción:** contenido informativo recibido por el agente en un instante.
- **Política:** regla que selecciona acciones a partir del estado, creencia o historia disponible.
- **Programa de agente:** procedimiento concreto que implementa una función de agente.
- **Racionalidad:** elección que maximiza desempeño esperado dadas información, alternativas y recursos.
- **Restricción:** condición que limita estados, acciones o trayectorias admisibles.
- **Sensor:** mecanismo físico o lógico que adquiere información del entorno.
- **Utilidad:** representación numérica de preferencias sobre consecuencias.

## Preguntas de autoevaluación

1. ¿Por qué un modelo que predice fallas no es necesariamente un agente? Identifique qué componentes faltarían.
2. Distinga percepción, sensor, acción y actuador mediante un ejemplo diferente de agua o movilidad.
3. ¿Por qué la función de agente tiene como entrada una secuencia y no solo la percepción actual?
4. Formule una medida de desempeño para un agente de turnos médicos e identifique una métrica susceptible de manipulación.
5. Una intervención racional produce un mal resultado. ¿Qué información se necesita para auditar la decisión sin sesgo retrospectivo?
6. Explique por qué autonomía y ausencia de supervisión no son equivalentes.
7. Construya un PEAS para un agente que administra consumo energético de un edificio.
8. ¿Puede un entorno ser observable y estocástico? Proponga un ejemplo y justifique ambas propiedades.
9. ¿Cómo puede un problema episódico convertirse en secuencial al ampliar el horizonte?
10. Compare los requisitos temporales de un entorno estático y uno dinámico.
11. ¿Qué se pierde al discretizar una variable continua? ¿Cómo validaría los intervalos?
12. Explique por qué un entorno con personas suele requerir una perspectiva multiagente.
13. ¿Cuándo elegiría un agente reactivo simple en lugar de uno basado en utilidad?
14. Distinga elemento de aprendizaje, crítico y generador de problemas.
15. ¿Qué significa que una representación de estado sea suficiente o markoviana?
16. Redacte precondiciones y efectos para la acción «reservar recurso».
17. ¿Por qué una restricción legal no debería representarse solo como costo elevado?
18. Dé un ejemplo de abstracción excesiva que convierta una solución computacional en una acción inviable.
19. Compare mundo abierto y mundo cerrado ante un dato de certificación ausente.
20. En el ejemplo de asignación, ¿qué cambios requeriría representar tiempos de viaje estocásticos?

## Actividad integradora de cierre

**Diseño y defensa de un agente para respuesta operativa.** Seleccione un dominio con impacto real, como gestión de residuos, mantenimiento de infraestructura, apoyo a emergencias o distribución de insumos. Elabore una especificación que pueda ser revisada por una persona técnica y por una responsable del dominio.

El producto debe incluir:

1. frontera del agente, actores y autoridad efectiva;
2. tabla PEAS con unidades, calidad de sensores y límites de actuadores;
3. clasificación razonada del entorno en las seis dimensiones estudiadas;
4. medida de desempeño con horizonte, restricciones y al menos un riesgo de desalineación;
5. comparación de dos arquitecturas y elección justificada;
6. formulación $\mathcal{P}=(S,A,T,s_0,G,C,R)$ con una instancia pequeña;
7. pseudocódigo de una decisión central y acción segura por defecto;
8. tres escenarios de prueba: normal, información faltante y evento adverso;
9. análisis de una variable omitida y de cómo podría invalidar la solución;
10. transición técnica hacia el capítulo 7 o el 8.

La defensa debe responder cuatro preguntas: ¿qué sabe realmente el agente?, ¿qué no sabe?, ¿qué puede ejecutar sin intervención? y ¿quién asume el costo de sus errores? Se valorará la coherencia entre PEAS, arquitectura y representación más que la complejidad del método.

Para enlazar con el **capítulo 7**, convierta la instancia en un grafo: cada estado será un nodo, cada acción aplicable una arista y cada costo una etiqueta. Anticipe si habrá ciclos, estados repetidos y qué información podría servir como heurística. Para enlazar con el **capítulo 8**, identifique al menos una transición incierta, una decisión que se repite y una consecuencia futura. Explique qué tendría que añadirse para definir una política bajo incertidumbre y cómo evitaría que el aprendizaje explore acciones inseguras.
