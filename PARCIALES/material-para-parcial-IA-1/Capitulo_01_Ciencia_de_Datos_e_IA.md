# Capitulo 1. Ciencia de Datos e Inteligencia Artificial: conceptos, historia y aplicaciones

## Proposito

La Ciencia de Datos y la Inteligencia Artificial suelen presentarse como campos nuevos, pero sus preguntas fundamentales tienen una historia mucho más larga: ¿cómo representar un fenómeno?, ¿cómo razonar con información incompleta?, ¿cómo aprender a partir de observaciones? y ¿cómo actuar cuando las consecuencias de una decisión son inciertas? Este capítulo introduce esos campos, delimita sus conceptos centrales y muestra cómo se relacionan sin convertirlos en sinónimos.

El objetivo no es aprender todavía a implementar un algoritmo particular. Es construir un mapa conceptual que permita reconocer qué problema se está resolviendo, qué tipo de evidencia se necesita, qué modelo resulta pertinente y qué riesgos aparecen cuando una predicción se transforma en una acción. Los capítulos siguientes desarrollarán las técnicas matemáticas, estadísticas y computacionales que aquí se presentan de manera introductoria.

Una idea orienta todo el capítulo: un modelo no es una decisión. Un modelo representa, resume o estima algún aspecto de la realidad; una decisión utiliza ese resultado dentro de un contexto, con objetivos, restricciones, costos y responsabilidades. Por eso, evaluar un sistema exige considerar tanto su desempeño técnico como la utilidad y las consecuencias de su uso.

## 1.1. Ciencia de Datos, Inteligencia Artificial y aprendizaje automático

### 1.1.1. Definición y objetivos de la Ciencia de Datos

La Ciencia de Datos es un campo interdisciplinario que desarrolla métodos para obtener conocimiento y apoyar decisiones a partir de datos. La definición contiene tres elementos importantes.

En primer lugar, los datos son representaciones parciales de fenómenos. Una medición de temperatura no es la temperatura en sí misma; es un registro producido por un sensor, en una ubicación, con una unidad, una precisión y un procedimiento de observación determinados. Un reclamo escrito no es el evento financiero completo; es una expresión textual condicionada por el canal, el lenguaje y la información que el usuario decidió proporcionar. La Ciencia de Datos comienza, por tanto, preguntando qué representan los datos y qué aspectos del fenómeno quedan fuera de ellos.

En segundo lugar, la disciplina es interdisciplinaria. La estadística permite describir variabilidad e inferir a partir de muestras; la informática proporciona estructuras, algoritmos y sistemas; la matemática formaliza relaciones, incertidumbre y optimización; el conocimiento del dominio permite interpretar si un resultado es plausible; y la comunicación convierte la evidencia en una explicación útil para otras personas. Ninguna de esas dimensiones, por sí sola, constituye todo el trabajo de datos.

En tercer lugar, el resultado no es necesariamente un modelo predictivo. Un proyecto puede producir un inventario de fuentes, una medición de calidad, un análisis descriptivo, una estimación causal, una segmentación, una visualización o una recomendación. La pregunta y la decisión determinan qué producto es apropiado.

El ciclo general puede representarse como:

`problema -> datos -> representación -> análisis -> evidencia -> decisión -> evaluación`

![Ciclo de vida de un proyecto de datos](imagenes/ciclo_vida_datos.png)

El ciclo es iterativo. La exploración puede mostrar que la pregunta original no es medible; una auditoría puede revelar que la variable objetivo se registró de manera inconsistente; una evaluación puede demostrar que un modelo no supera una regla simple. En esos casos, volver a formular el problema no significa fracasar, sino aprender algo relevante sobre el sistema estudiado.

Los objetivos de la Ciencia de Datos pueden clasificarse de la siguiente manera:

- **Describir:** resumir qué ocurrió, con qué frecuencia, en qué grupos y durante qué periodos.
- **Diagnosticar:** investigar factores asociados con un resultado o posibles explicaciones de un comportamiento.
- **Predecir:** estimar un valor o una categoría no observada, futura o costosa de medir.
- **Prescribir o recomendar:** comparar acciones posibles considerando consecuencias, restricciones y preferencias.
- **Monitorear:** detectar cambios, anomalías o degradación en datos, procesos y modelos.

Estas categorías pueden combinarse, pero no deben confundirse. Describir que dos variables se mueven juntas no demuestra que una cause la otra. Predecir que ocurrirá un evento no indica automáticamente qué acción es conveniente. Recomendar una acción requiere una función de utilidad o una regla de decisión, no solo una probabilidad.

Una especificación inicial de un problema puede expresarse como:

$$
P = (U, O, X, Y, A, H, C)
$$

donde $U$ es la unidad de análisis, $O$ el objetivo, $X$ las variables disponibles, $Y$ el resultado de interés, $A$ el conjunto de acciones posibles, $H$ el horizonte temporal y $C$ las restricciones. Esta notación obliga a preguntar qué representa cada observación y en qué momento se conocerá cada dato.

Por ejemplo, si una empresa desea reducir retrasos de transporte, una fila podría representar un viaje, una parada, una zona o un intervalo de quince minutos. Cada elección conduce a una pregunta diferente. Predecir el retraso de un viaje requiere variables disponibles antes de iniciarlo; analizar la congestión de una zona puede requerir agregar muchos viajes; asignar vehículos necesita además conocer recursos y restricciones operativas.

La Ciencia de Datos también debe distinguir entre datos, información y conocimiento. Los datos son observaciones codificadas; la información surge al organizarlos en un contexto; el conocimiento combina patrones y explicaciones con experiencia y reglas de uso; una decisión selecciona una acción. El paso de un nivel a otro puede introducir errores, supuestos y sesgos, por lo que la trazabilidad es parte del resultado científico.

### 1.1.2. Definición y objetivos de la Inteligencia Artificial

La Inteligencia Artificial estudia la construcción de sistemas capaces de realizar tareas que asociamos con capacidades inteligentes: percibir, representar estados, razonar, aprender, planificar, comunicarse y actuar. La expresión “inteligente” no implica que el sistema posea conciencia, comprensión humana general o intenciones propias. En un sentido técnico, significa que el sistema transforma información en comportamiento dirigido a un objetivo bajo determinadas condiciones.

Una forma clásica de describir un sistema inteligente es mediante el concepto de agente. Un agente recibe una secuencia de percepciones y selecciona acciones:

$$
a_t = \pi(h_t)
$$

donde $h_t$ es la historia de percepciones hasta el instante $t$, $a_t$ es la acción y $\pi$ es la política o función de decisión. En un sistema sencillo, $\pi$ puede ser una tabla de reglas. En otro, puede ser un modelo aprendido a partir de datos. La complejidad de la implementación no determina por sí sola la inteligencia del comportamiento.

El agente actúa en un entorno. El entorno puede ser físico, como una red de agua o un vehículo, o informacional, como un sistema de reclamos. Las acciones producen consecuencias que pueden medirse mediante una función de desempeño $U$. Un agente racional intenta seleccionar acciones con buen desempeño esperado, dadas sus percepciones, su conocimiento y sus recursos.

La formulación general de una decisión bajo incertidumbre es:

$$
a^* = \operatorname*{arg\,max}_{a}\;\mathbb{E}\!\left[U(a,S)\mid\text{evidencia disponible}\right]
$$

El valor de la expresión depende de cómo se definan los estados posibles $S$, sus probabilidades, la utilidad y las restricciones. Esto es importante porque un sistema puede optimizar perfectamente una función mal elegida. Si se recompensa únicamente la rapidez de respuesta, un asistente puede producir respuestas rápidas pero incorrectas; si se penalizan demasiado los falsos negativos, un detector puede generar demasiadas alertas innecesarias.

La IA incluye enfoques basados en reglas, búsqueda, lógica, probabilidades, planificación, aprendizaje automático, visión artificial, procesamiento del lenguaje y agentes autónomos. El aprendizaje automático es una parte de la IA, no su totalidad. Un sistema experto construido con reglas puede ser IA aunque no aprenda automáticamente. Del mismo modo, una regresión usada para describir una relación puede pertenecer a Ciencia de Datos sin constituir un agente inteligente.

La distinción entre capacidad y autonomía también es fundamental. Un sistema puede realizar una tarea compleja y, sin embargo, operar dentro de un procedimiento muy acotado. Un clasificador de imágenes que asigna una etiqueta no decide necesariamente qué debe hacer una persona. La autonomía aparece cuando el sistema puede seleccionar y ejecutar acciones con poca intervención humana. A mayor autonomía, mayor importancia tienen la seguridad, la supervisión, la posibilidad de reversión y la responsabilidad institucional.

### 1.1.3. Aprendizaje automático y aprendizaje profundo

El aprendizaje automático construye una función a partir de ejemplos o experiencia. En el aprendizaje supervisado se dispone de observaciones $D=\{(x_i,y_i)\}_{i=1}^{n}$, donde $x_i$ representa entradas y $y_i$ el resultado asociado. El objetivo es estimar una función $f_\theta$ cuyos parámetros $\theta$ produzcan resultados útiles en observaciones nuevas.

Una formulación frecuente es:

$$
\theta^* = \operatorname*{arg\,min}_{\theta}\left[
\frac{1}{n}\sum_{i=1}^{n}L\!\left(y_i,f_\theta(x_i)\right)
+ \lambda\Omega(\theta)
\right]
$$

La primera parte mide el error sobre los ejemplos disponibles. $L$ puede ser una pérdida cuadrática para regresión, una pérdida logarítmica para clasificación u otra función apropiada. El término $\Omega(\theta)$ penaliza complejidad; $\lambda$ controla la intensidad de la regularización. La optimización encuentra parámetros, pero no garantiza que la tarea esté bien formulada ni que el modelo generalice.

La generalización es la capacidad de funcionar sobre datos que no se utilizaron para ajustar el modelo. Si un algoritmo memoriza peculiaridades del conjunto de entrenamiento, puede presentar bajo error interno y fallar en producción. Por eso se separan entrenamiento, validación y prueba, y se diseñan protocolos que respetan tiempo, grupos, duplicados y disponibilidad de información.

En el aprendizaje no supervisado no se dispone necesariamente de una variable objetivo. El propósito puede ser encontrar grupos, representaciones, componentes o anomalías. En el aprendizaje por refuerzo, un agente interactúa con un entorno, recibe recompensas y aprende una política. Cada paradigma responde a una pregunta diferente y exige una evaluación diferente.

El aprendizaje profundo utiliza redes neuronales con múltiples capas de transformaciones. Una capa puede calcular:

$$
h^{(\ell)} = \phi\!\left(W^{(\ell)}h^{(\ell-1)}+b^{(\ell)}\right)
$$

donde $W$ son pesos, $b$ sesgos y $\phi$ una función no lineal. Al apilar capas, el sistema aprende representaciones intermedias: en una imagen pueden aparecer bordes, texturas y formas; en un texto, relaciones entre tokens y contexto. La profundidad aumenta la capacidad representacional, pero también la necesidad de datos, cómputo, regularización, diagnóstico y explicabilidad.

“Aprender” no significa comprender en el sentido humano. Un modelo estadístico identifica regularidades útiles para su objetivo de entrenamiento. Puede explotar correlaciones espurias, señales de fondo o artefactos de captura. Por eso la inspección de ejemplos, la evaluación por subgrupos y el análisis fuera de distribución son tan importantes como la métrica global.

### 1.1.4. Relación con la estadística, la optimización y la ingeniería de software

La estadística aporta conceptos para describir variabilidad, estimar parámetros, construir intervalos, contrastar hipótesis y distinguir señal de ruido. Un dataset suele ser una muestra de una población más amplia. La pregunta estadística es qué puede inferirse de esa muestra y bajo qué supuestos. La pregunta de aprendizaje automático suele ser qué tan bien puede predecirse un resultado en datos futuros. Ambas preguntas se relacionan, pero no son idénticas.

La optimización formaliza la selección de parámetros o acciones. En un modelo supervisado, se minimiza una función de pérdida; en un problema de planificación, se minimiza un costo; en un agente, se maximiza una utilidad. Las funciones objetivo expresan prioridades. Cambiar la función objetivo cambia el comportamiento que se considera correcto.

La ingeniería de software transforma un método en un sistema mantenible. Incluye diseño modular, pruebas, control de versiones, gestión de dependencias, seguridad, observabilidad y despliegue. Un notebook que produce una métrica una vez no equivale a un sistema reproducible. Un modelo que funciona en una evaluación controlada puede fallar si el sistema de producción cambia el formato, la frecuencia o la población de los datos.

Puede resumirse la relación así:

| Disciplina | Pregunta principal | Contribución al proyecto |
|---|---|---|
| Estadística | ¿Qué evidencia permiten los datos y cuál es la incertidumbre? | Descripción, inferencia y evaluación |
| Optimización | ¿Qué parámetros o acciones maximizan el objetivo? | Ajuste y decisión |
| Computación | ¿Cómo se representa y calcula el procedimiento? | Algoritmos y eficiencia |
| Ingeniería de software | ¿Cómo se mantiene y opera el sistema? | Reproducibilidad y confiabilidad |
| Conocimiento del dominio | ¿Qué significa el resultado en el contexto real? | Interpretación y restricciones |

Un proyecto sólido necesita que estas perspectivas sean compatibles. Un modelo estadísticamente adecuado puede ser demasiado lento para una decisión en tiempo real; un algoritmo rápido puede optimizar una variable que no representa el objetivo institucional; una solución técnicamente correcta puede ser imposible de operar porque no existe un proceso de supervisión.

### 1.1.5. Diferencias entre modelos descriptivos, predictivos y prescriptivos

Un modelo descriptivo resume observaciones. Puede calcular frecuencias, medias, cuantiles, distribuciones, asociaciones o segmentos. Su propósito es responder qué ocurrió o qué estructuras aparecen. Un modelo descriptivo no necesita predecir el futuro para ser valioso; por ejemplo, identificar horarios con mayor demanda puede orientar una investigación operativa.

Un modelo predictivo estima un resultado desconocido. La predicción puede referirse al futuro, a una observación cuyo valor aún no se midió o a una etiqueta que requiere evaluación costosa. Formalmente, se busca estimar $P(Y\mid X)$ o una cantidad condicional como $\mathbb{E}[Y\mid X]$. La calidad se mide comparando predicciones con resultados observados mediante un protocolo que represente el uso real.

Un modelo prescriptivo compara acciones. Puede usar predicciones, pero agrega una función de utilidad, costos, restricciones y consecuencias. Si $p$ es la probabilidad de una falla, $C_i$ el costo de inspección y $C_f$ el costo de no detectar la falla, una regla simple puede seleccionar inspección cuando:

$$
p\,C_f > C_i
$$

La desigualdad no es una ley universal. Es una consecuencia de un modelo de costos determinado. Si existen beneficios de inspeccionar, restricciones de capacidad o daños irreversibles, la regla debe ampliarse.

Los tres tipos se conectan en una cadena, pero no se sustituyen:

`descripción -> predicción -> evaluación de acciones -> decisión`

Una predicción precisa puede ser inútil si no cambia ninguna acción. Una recomendación puede ser razonable aun cuando la predicción sea incierta, si la acción es barata y reversible. Del mismo modo, un análisis descriptivo puede ser preferible a automatizar una decisión cuando faltan datos confiables o las consecuencias son graves.

### 1.1.6. Ejemplo práctico guiado: identificación de componentes de Ciencia de Datos e IA en un problema real

Considérese una empresa que administra una flota de vehículos y desea reducir demoras. El problema inicial es amplio: “mejorar el servicio”. Para volverlo analizable se define la unidad de análisis como un viaje, el horizonte como la próxima franja horaria y la decisión como reasignar vehículos entre zonas.

La captura registra identificador del viaje, origen, destino, hora programada, hora real, zona, vehículo y eventualmente condiciones climáticas. Antes de modelar es necesario verificar qué significa cada campo, cuándo queda disponible y si la hora real, que se conoce después del viaje, estaría disponible al momento de predecir.

El análisis descriptivo calcula cantidad de viajes, demora media y cuantiles por zona y franja horaria. Su resultado puede ser una tabla o visualización que muestre dónde y cuándo se concentran los retrasos. Todavía no predice un viaje futuro ni recomienda una acción.

La predicción estima, por ejemplo, la demora esperada del siguiente intervalo. La variable objetivo puede ser continua, como minutos de retraso, o categórica, como “a tiempo”, “demorado” y “crítico”. La evaluación debe utilizar datos posteriores a los usados para ajustar, respetar el orden temporal y comparar el modelo con un baseline.

La prescripción utiliza la predicción junto con vehículos disponibles, capacidad, tiempos de traslado, prioridades y costos. Una regla puede asignar un vehículo a la zona donde el beneficio esperado de reducir retrasos sea mayor. Esa regla es un componente de decisión y debe evaluarse con una métrica operativa, no solo con el error predictivo.

El procedimiento conceptual es:

```text
definir unidad, horizonte y accion
auditar campos, disponibilidad temporal y calidad
describir demanda y demoras por zona y periodo
definir objetivo predictivo y baseline
separar datos respetando el tiempo
ajustar modelo y evaluar generalizacion
estimar consecuencias de cada accion posible
seleccionar accion factible con utilidad esperada
monitorear resultados y revisar supuestos
```

El ejemplo muestra que la Ciencia de Datos aparece en la definición, preparación, análisis y evaluación. La IA puede aparecer en la predicción, en la búsqueda de una asignación o en un agente que actúe sobre la flota. La captura de datos no es todavía inteligencia; es una condición para producir evidencia.

## 1.2. Enfoques y fundamentos de la Inteligencia Artificial

Una misma aplicación puede considerarse inteligente según criterios diferentes. La clasificación clásica distingue sistemas que actúan como seres humanos, sistemas que piensan como seres humanos, sistemas que piensan racionalmente y sistemas que actúan racionalmente. Los enfoques no describen necesariamente cuatro tecnologías separadas; son cuatro preguntas sobre qué significa inteligencia.

### 1.2.1. Sistemas que actúan como seres humanos

Este enfoque evalúa la conducta observable. Un sistema se considera exitoso si su comportamiento resulta indistinguible o comparable al de una persona en una tarea definida. Incluye conversación, percepción, movimiento, uso de herramientas y respuesta a situaciones.

La ventaja del criterio conductual es que permite evaluar resultados sin resolver el problema filosófico de qué ocurre dentro del sistema. Sin embargo, una conducta similar puede producirse mediante mecanismos muy distintos. Un sistema puede dar respuestas apropiadas usando reglas específicas sin poseer una representación general del mundo. También puede imitar el estilo humano y cometer errores que una persona no cometería, o producir una respuesta convincente sin contar con evidencia suficiente.

El criterio debe especificar tarea, contexto y población de evaluación. “Actuar como una persona” no es una propiedad única: una persona puede ser rápida en conversación, pero no necesariamente precisa en diagnóstico; puede reconocer un objeto en condiciones normales y fallar en una imagen degradada.

### 1.2.2. Sistemas que piensan como seres humanos

Este enfoque intenta modelar procesos cognitivos humanos: percepción, memoria, aprendizaje, lenguaje, razonamiento y resolución de problemas. La evaluación no se limita a la respuesta final, sino que considera tiempos, errores, secuencias de pasos y cambios frente a nueva información.

El modelado cognitivo puede apoyarse en experimentos psicológicos, neurociencia, modelos simbólicos y modelos conexionistas. Su objetivo no siempre es construir la solución más eficaz, sino formular hipótesis sobre cómo funciona la cognición.

Un sistema que resuelve un problema correctamente no necesariamente piensa como una persona. Puede explorar miles de alternativas de manera impracticable para un humano, utilizar una memoria completa del conjunto de datos o aprovechar una regularidad que no está disponible para la percepción humana. La similitud de resultados y la similitud del proceso son criterios distintos.

Este enfoque es útil cuando se diseñan interfaces, tutores o herramientas de asistencia que deben adaptarse a capacidades humanas. También permite estudiar qué tipos de explicaciones, alertas o representaciones son comprensibles para sus usuarios.

### 1.2.3. Sistemas que piensan racionalmente

Pensar racionalmente significa derivar conclusiones válidas a partir de premisas y reglas de inferencia. La lógica proposicional y la lógica de predicados ofrecen lenguajes formales para representar hechos y relaciones. Si se tiene $A\to B$ y se observa $A$, el modus ponens permite inferir $B$.

La ventaja de la lógica es la claridad: las premisas, reglas y conclusiones pueden inspeccionarse. Sus limitaciones aparecen cuando el conocimiento es incompleto, ambiguo o incierto. Un sistema médico raramente dispone de premisas absolutas; una observación puede ser ruidosa y una regla puede tener excepciones.

La probabilidad amplía este enfoque al permitir grados de creencia. En lugar de afirmar únicamente que una hipótesis es verdadera o falsa, se puede calcular $P(H\mid E)$, la probabilidad de una hipótesis $H$ dada la evidencia $E$. La lógica difusa, los modelos gráficos y otras formalizaciones representan incertidumbre o vaguedad de maneras diferentes.

Pensar racionalmente tampoco garantiza actuar bien. Una inferencia puede ser válida y conducir a una acción perjudicial si las premisas son incorrectas o si no se consideraron costos y consecuencias.

### 1.2.4. Sistemas que actúan racionalmente

Un sistema actúa racionalmente cuando selecciona, entre las acciones disponibles, aquella que maximiza el desempeño esperado según sus objetivos, información y limitaciones. Este enfoque es central para los agentes inteligentes.

Sea $S$ el estado del entorno, $E$ la evidencia, $A$ una acción y $U$ la utilidad. La elección ideal puede escribirse como:

$$
a^* = \operatorname*{arg\,max}_{a}\sum_s P(s\mid E)\,U(a,s)
$$

El agente no necesita conocer el estado verdadero con certeza. Necesita representar creencias sobre estados posibles, evaluar consecuencias y reconocer el costo de obtener más información. La racionalidad es, por tanto, relativa a la información disponible. Un agente no es irracional por no elegir una acción que solo sería óptima con información que no podía observar.

La racionalidad también incluye acciones de recolección de información. Si una medición puede cambiar significativamente la decisión, su valor esperado puede justificar el costo de obtenerla. Esta idea anticipa el valor de la información y la planificación bajo incertidumbre.

El enfoque racional es especialmente adecuado para sistemas de recomendación, control, asignación y asistencia a decisiones. Su desafío principal es definir correctamente la utilidad y las restricciones. Optimizar una función simplificada puede producir un comportamiento eficiente en términos numéricos pero inaceptable en términos sociales, ambientales o de seguridad.

### 1.2.5. Test de Turing y modelado cognitivo

El test de Turing propone evaluar si un interlocutor humano puede distinguir, mediante una conversación, entre una persona y una máquina. Su importancia histórica está en desplazar la discusión desde una definición abstracta de inteligencia hacia una prueba de comportamiento.

El test tiene límites. Una conversación no evalúa necesariamente percepción física, planificación prolongada, comprensión causal o desempeño en situaciones nuevas. Además, un sistema puede utilizar estrategias de evasión, imitación o generación de respuestas plausibles. Superar una prueba particular no demuestra inteligencia general ni confiabilidad en dominios sensibles.

El modelado cognitivo plantea una pregunta diferente: ¿qué mecanismos internos podrían explicar el comportamiento? Dos sistemas pueden aprobar una prueba con respuestas similares, pero uno puede utilizar memoria, reglas y búsqueda, mientras que otro utiliza representaciones distribuidas y estimación estadística. Para diferenciarlos se estudian patrones de error, tiempos de respuesta, generalización y reacción a cambios controlados.

Los dos enfoques son complementarios. La evaluación conductual pregunta si el sistema cumple la tarea; el modelado cognitivo pregunta qué proceso explica ese cumplimiento. En aplicaciones reales conviene agregar un tercer nivel: si el sistema es seguro, trazable y apropiado para la decisión que se pretende apoyar.

### 1.2.6. Fundamentos filosóficos, matemáticos y computacionales

La IA se apoya en varias tradiciones filosóficas. El racionalismo destaca la razón y las estructuras formales; el empirismo destaca la experiencia y la observación; el pragmatismo evalúa ideas por sus consecuencias prácticas. Estas tradiciones reaparecen en el contraste entre sistemas basados en conocimiento explícito y sistemas que aprenden regularidades de datos.

La lógica aporta representación y deducción. La probabilidad permite razonar ante incertidumbre. La teoría de la decisión relaciona creencias con acciones mediante utilidad. La optimización permite elegir parámetros o políticas. El álgebra lineal representa datos, transformaciones y redes; el cálculo proporciona gradientes; la teoría de la información cuantifica incertidumbre y contenido informativo.

Desde la computación, un sistema de IA requiere una representación de estados, una forma de producir transiciones, un algoritmo de búsqueda o aprendizaje y recursos de memoria y tiempo. La complejidad computacional importa porque un método exacto puede ser impracticable a gran escala. La aproximación, la heurística y la paralelización intercambian garantías, velocidad y calidad.

Una arquitectura completa suele incluir:

1. percepción o entrada de datos;
2. representación interna;
3. memoria o estado;
4. inferencia, búsqueda o aprendizaje;
5. evaluación de acciones;
6. ejecución, comunicación y retroalimentación.

La separación ayuda a localizar fallos. Una predicción incorrecta puede deberse a una representación inadecuada; una acción incorrecta puede deberse a una función de utilidad mal definida aunque la predicción sea buena; un sistema inestable puede deberse a la interacción entre modelo y entorno.

### 1.2.7. Ejemplo práctico guiado: análisis de un asistente inteligente desde los cuatro enfoques de la IA

Considérese un asistente que recibe el texto de un reclamo, consulta antecedentes y propone una respuesta. Desde el enfoque de actuar como humano se evalúa si conversa con fluidez, identifica la intención y mantiene el contexto. La prueba debe incluir preguntas ambiguas, errores de escritura, cambios de tema y solicitudes fuera de alcance.

Desde el enfoque de pensar como humano se estudia si separa hechos, interpreta referencias y utiliza una secuencia de razonamiento comparable a la de un agente de atención. No es suficiente observar una respuesta correcta; también interesa cómo reacciona cuando falta información y si puede explicar qué dato necesita.

Desde el enfoque de pensar racionalmente se inspeccionan las reglas de inferencia, las fuentes consultadas y la coherencia entre evidencia y conclusión. Una respuesta debe poder justificarse mediante antecedentes verificables y no solamente por su plausibilidad lingüística.

Desde el enfoque de actuar racionalmente se analiza si la recomendación maximiza el objetivo del servicio bajo restricciones de política, privacidad, tiempos y costos. El asistente podría decidir responder, pedir información, derivar el caso o abstenerse. La abstención es una acción racional cuando la incertidumbre o el riesgo son altos.

La evaluación debe registrar entradas, fuentes usadas, respuesta, nivel de confianza, acción sugerida y revisión humana. Así se distingue capacidad conversacional de confiabilidad operativa.

## 1.3. Evolución histórica de la Ciencia de Datos y la IA

La historia de estos campos no es una sucesión lineal de inventos cada vez mejores. Es una alternancia entre representaciones, expectativas y recursos disponibles. Un método puede ser conceptualmente correcto y fracasar porque no existen datos, memoria o capacidad de cómputo suficientes. También puede ser técnicamente eficaz y resultar limitado cuando cambia el problema.

### 1.3.1. Antecedentes lógicos y matemáticos

La lógica formal permitió expresar proposiciones y reglas de inferencia. El cálculo y el álgebra proporcionaron herramientas para modelar cambio, geometría y transformaciones. La probabilidad formalizó la incertidumbre y la estadística desarrolló procedimientos para aprender sobre poblaciones a partir de muestras.

La teoría de la información introdujo formas de cuantificar incertidumbre y transmisión de señales. La teoría de la decisión relacionó probabilidades con preferencias y costos. Estos desarrollos no fueron inicialmente “IA”, pero constituyen la base de métodos contemporáneos de clasificación, compresión, estimación y control.

La computación agregó una condición práctica: que los procedimientos pudieran ejecutarse mecánicamente. La idea de algoritmo precede al computador moderno, pero la máquina programable permitió automatizar secuencias generales de operaciones. El límite entre un cálculo explícito y un sistema que aprende aparece cuando el procedimiento no especifica directamente todas las respuestas, sino que ajusta una representación a partir de ejemplos.

### 1.3.2. Nacimiento formal de la Inteligencia Artificial

Durante la década de 1950 se consolidó la idea de estudiar inteligencia mediante programas. La conferencia de Dartmouth de 1956 suele considerarse un hito nominal para el campo. Los primeros proyectos exploraron demostración de teoremas, juegos, resolución de problemas y manipulación simbólica.

La expectativa inicial era que muchas tareas inteligentes pudieran expresarse como búsqueda en espacios de estados y manipulación de símbolos. La computadora recibiría una representación del problema, aplicaría reglas y encontraría una solución. Este enfoque fue exitoso en mundos acotados, donde las reglas y estados eran relativamente claros.

Pronto aparecieron dificultades: la cantidad de estados crecía rápidamente, el lenguaje natural era ambiguo, el conocimiento del mundo era enorme y la percepción contenía ruido. La diferencia entre resolver un rompecabezas formal y actuar en un entorno abierto obligó a incorporar heurísticas, conocimiento de dominio, probabilidades y aprendizaje.

### 1.3.3. Sistemas expertos y representación simbólica

Los sistemas expertos separaron una base de conocimiento de un motor de inferencia. La base podía contener reglas como “si se observa A y B, considerar C”; el motor aplicaba esas reglas a hechos disponibles. Este diseño permitía explicar una conclusión mediante una cadena de reglas, una característica valiosa en dominios profesionales.

La representación simbólica ofrece conceptos legibles: entidades, relaciones, categorías, causas y restricciones. También permite incorporar conocimiento que no sería fácil aprender de pocos ejemplos. Sus dificultades son el costo de adquirir y mantener reglas, la ambigüedad de las excepciones y la fragilidad ante situaciones no contempladas.

Un sistema experto no es automáticamente objetivo. Las reglas reflejan decisiones de quienes las diseñan, datos históricos y políticas institucionales. Si la base de conocimiento omite una población o utiliza una definición inadecuada, el razonamiento será coherente con premisas problemáticas.

La representación simbólica y el aprendizaje estadístico pueden combinarse. Un sistema puede usar un modelo aprendido para percibir una imagen y reglas explícitas para controlar una decisión. Esta combinación conserva conocimiento verificable sin exigir que toda la tarea se resuelva con reglas.

### 1.3.4. Invierno de la IA y resurgimiento estadístico

Los inviernos de la IA fueron periodos de reducción de financiamiento y entusiasmo. Las causas incluyeron promesas desproporcionadas, resultados difíciles de generalizar, limitaciones de cómputo, falta de datos y sistemas demasiado frágiles fuera de entornos controlados.

La experiencia mostró que una demostración en un problema pequeño no equivalía a inteligencia general. También mostró que una tarea podía ser difícil por razones de representación y no solo por falta de potencia. En reconocimiento visual, por ejemplo, especificar manualmente todas las formas posibles era poco viable; en lenguaje, las reglas no podían cubrir todas las expresiones.

El resurgimiento estadístico dio mayor importancia a modelos que estiman regularidades a partir de datos. La disponibilidad de bases más grandes, mejores sensores, almacenamiento barato, redes de comunicación y procesadores especializados permitió entrenar modelos más complejos. Los avances no eliminaron los problemas de sesgo, cambio de distribución y evaluación; simplemente desplazaron el centro de gravedad hacia los datos y el aprendizaje.

### 1.3.5. Big Data, aprendizaje profundo e IA generativa

Big Data no significa solamente “muchos datos”. Suele describirse mediante volumen, velocidad, variedad, veracidad y valor. Un flujo de sensores puede tener gran velocidad y volumen, pero mediciones incompletas; un corpus textual puede tener variedad, pero etiquetas ambiguas; un dataset pequeño puede tener alto valor si representa con precisión una tarea crítica.

El aprendizaje profundo se benefició de datasets extensos, GPU, arquitecturas diferenciables y técnicas de entrenamiento más estables. Las redes convolucionales mejoraron tareas visuales; los modelos secuenciales y Transformers ampliaron el procesamiento del lenguaje y de otras secuencias.

Los modelos fundacionales se preentrenan sobre grandes colecciones y luego se adaptan a tareas o dominios. La IA generativa produce nuevas instancias condicionadas por una entrada: texto, imágenes, audio, código u otros contenidos. En un modelo autoregresivo, una secuencia puede factorizarse como:

$$
P(x_1,\ldots,x_T)
=P(x_1)\prod_{t=2}^{T}P\!\left(x_t\mid x_1,\ldots,x_{t-1}\right)
$$

Esta formulación permite generar paso a paso, pero no garantiza que el contenido sea verdadero. La fluidez lingüística es una propiedad de generación, no una prueba de conocimiento. Por eso los modelos generativos deben combinarse con recuperación de fuentes, validación, límites de uso y supervisión.

### 1.3.6. Ejemplo práctico guiado: construcción de una línea de tiempo tecnológica

Construir una línea de tiempo con cinco columnas: hito, representación dominante, datos disponibles, capacidad de cómputo y limitación principal. Incluir, por ejemplo, antecedentes lógicos, nacimiento de la IA simbólica, sistemas expertos, resurgimiento estadístico, aprendizaje profundo y modelos generativos.

La tarea no consiste en memorizar fechas. Para cada hito se debe responder: ¿qué problema podía resolverse?, ¿qué supuesto se utilizaba?, ¿qué recurso faltante limitaba la expansión? Una línea de tiempo útil conecta la aparición de un método con las condiciones que lo hicieron posible.

## 1.4. Aplicaciones, alcances y riesgos

Una aplicación de datos o IA transforma observaciones en una salida que puede influir en personas, recursos o procesos. La utilidad depende del contexto de uso. El mismo clasificador puede ser aceptable como herramienta exploratoria y no serlo como mecanismo automático de rechazo de solicitudes.

### 1.4.1. Aplicaciones en ingeniería e industria

En ingeniería, los modelos pueden estimar vida útil, detectar fallas, optimizar consumo, programar mantenimiento y controlar procesos. En industria, los sensores permiten construir series de temperatura, vibración, presión o producción. La predicción de mantenimiento puede reducir interrupciones, pero requiere que las mediciones estén disponibles antes de la falla y que exista capacidad de intervenir.

La confiabilidad técnica exige distinguir entre detección y diagnóstico. Detectar una señal anómala indica que el comportamiento difiere del patrón esperado; diagnosticar implica asociarla con una causa; prescribir requiere elegir una intervención. Cada paso tiene un nivel distinto de evidencia.

### 1.4.2. Aplicaciones en salud, ambiente y agricultura

En salud, la IA puede apoyar clasificación de imágenes, priorización, búsqueda bibliográfica y estimación de riesgos. El modelo no reemplaza automáticamente la evaluación clínica: las consecuencias de un error, la prevalencia de la condición y la calidad de la población de validación son determinantes.

En ambiente, los datos pueden provenir de sensores, satélites, estaciones y registros comunitarios. La cobertura espacial y temporal rara vez es uniforme. Un mapa de riesgo puede reflejar tanto el fenómeno como la distribución de sensores. En agricultura, la visión artificial puede identificar síntomas en hojas, pero la generalización desde imágenes controladas a condiciones de campo debe probarse explícitamente.

### 1.4.3. Aplicaciones en finanzas y sistemas de información

En finanzas y servicios, los modelos se usan para detectar transacciones anómalas, clasificar reclamos, estimar riesgo y recomendar productos. Los datos históricos pueden contener decisiones previas, por lo que un modelo puede aprender patrones institucionales en lugar de medir directamente el comportamiento que interesa.

En sistemas de información, la IA puede mejorar búsqueda, recomendación, extracción de datos y asistencia al usuario. Los objetivos de interacción, retención o rapidez pueden entrar en tensión con precisión, privacidad y bienestar. Por eso la métrica de negocio no debe ser la única medida de éxito.

### 1.4.4. Automatización, asistencia y apoyo a decisiones

La automatización ejecuta una acción con intervención humana reducida. La asistencia presenta información, predicciones o alternativas para que una persona decida. El apoyo a decisiones puede incluir una recomendación, pero mantiene responsabilidad y control humanos.

Una clasificación útil considera cuatro niveles:

1. **Observación:** el sistema resume o visualiza datos.
2. **Sugerencia:** propone una interpretación o acción.
3. **Ejecución supervisada:** actúa después de una aprobación.
4. **Ejecución autónoma:** actúa sin aprobación caso por caso.

El nivel apropiado depende de reversibilidad, velocidad, consecuencias, posibilidad de auditoría y capacidad de supervisión. En una tarea de bajo riesgo puede ser eficiente automatizar; en una decisión sensible puede ser preferible que el sistema se abstenga y derive el caso.

### 1.4.5. Limitaciones técnicas y organizacionales

Las limitaciones técnicas incluyen datos incompletos, etiquetas ruidosas, variables mal definidas, fuga de información, sobreajuste, deriva, cambios de distribución, errores de medición y vulnerabilidades adversariales. El desempeño promedio puede ocultar fallos sistemáticos en subgrupos o situaciones poco frecuentes.

Las limitaciones organizacionales incluyen falta de responsables, procesos de revisión inexistentes, infraestructura insuficiente, incentivos mal alineados, resistencia de usuarios y ausencia de un mecanismo para corregir decisiones. Un modelo no se despliega en el vacío: entra en un proceso que puede amplificar o neutralizar sus errores.

La validez debe considerarse en varias dimensiones:

- **Validez de constructo:** las variables representan el concepto que se quiere medir.
- **Validez interna:** el resultado está respaldado dentro de los datos y diseño utilizados.
- **Validez externa:** generaliza a la población y condiciones de uso.
- **Validez operativa:** puede integrarse en un proceso que ejecuta la decisión.

### 1.4.6. Sesgos, privacidad, seguridad y uso responsable

El sesgo no es una propiedad única de un algoritmo. Puede aparecer durante la definición del problema, la medición, la selección de datos, el etiquetado, el entrenamiento, el umbral, la interfaz o el uso posterior. Un dataset puede representar de manera desigual a una población; una etiqueta puede reflejar decisiones históricas; una métrica puede favorecer un grupo y perjudicar otro.

La privacidad exige limitar recolección, acceso, retención y reutilización. Anonimizar identificadores no garantiza que una persona no pueda ser reidentificada si se combinan atributos. La seguridad incluye proteger datos, modelos y canales de inferencia, así como prevenir manipulación de entradas y filtración de información.

El uso responsable requiere, como mínimo, propósito definido, base legal o legitimidad, documentación de datos y modelo, evaluación de impacto, controles de acceso, supervisión, posibilidad de apelación y monitoreo posterior. La explicabilidad debe adaptarse al usuario y a la decisión: una explicación técnica de pesos no necesariamente permite cuestionar una decisión concreta.

Una cadena de análisis de riesgo puede escribirse como:

`dato o supuesto -> mecanismo de error -> impacto -> control -> responsable -> evidencia de control`

Este esquema evita declaraciones generales como “el sistema es ético” y obliga a especificar qué puede fallar, quién debe detectarlo y qué se hará cuando ocurra.

### 1.4.7. Ejemplo práctico guiado: evaluación inicial de oportunidades y riesgos

Elegir una aplicación concreta, por ejemplo, un sistema que prioriza reclamos financieros. Elaborar una ficha con:

- problema y beneficio esperado;
- usuarios, personas afectadas y responsables;
- datos utilizados y datos excluidos;
- salida del modelo y acción asociada;
- falsos positivos y falsos negativos;
- grupos o condiciones con posible desempeño desigual;
- riesgos de privacidad y seguridad;
- controles, revisión humana y mecanismo de apelación;
- condición para suspender o retirar el sistema.

La evaluación debe distinguir el riesgo del modelo del riesgo de la decisión. Un clasificador puede tener una métrica aceptable, pero ser inadecuado si la organización convierte automáticamente una prioridad en un rechazo. También debe distinguir posibilidad y severidad: un error raro puede requerir controles estrictos si sus consecuencias son graves.

## Sintesis

La Ciencia de Datos organiza un proceso para producir evidencia a partir de observaciones; la Inteligencia Artificial construye sistemas que perciben, razonan, aprenden o actúan. El aprendizaje automático estima funciones desde datos y el aprendizaje profundo utiliza representaciones compuestas, pero ninguno reemplaza la formulación del problema ni el juicio sobre el uso.

Los cuatro enfoques de la IA muestran que “inteligencia” puede referirse a conducta, proceso cognitivo, razonamiento o acción racional. La historia del campo evidencia que los métodos dependen de representaciones, datos, cómputo y expectativas. Las aplicaciones actuales amplían capacidades, pero también hacen visibles riesgos de sesgo, privacidad, seguridad y automatización.

En los capítulos siguientes, estos conceptos se convertirán en procedimientos: el Capítulo 2 formalizará el ciclo de vida; los Capítulos 3 y 4 tratarán calidad, exploración y comunicación; los Capítulos 5 a 8 desarrollarán incertidumbre, agentes, búsqueda y decisión; y los Capítulos 9 a 16 estudiarán aprendizaje automático, visión y lenguaje.

## Glosario esencial

- **Agente:** sistema que recibe percepciones y selecciona acciones en un entorno.
- **Aprendizaje automático:** métodos que ajustan una función o política a partir de datos o experiencia.
- **Aprendizaje profundo:** aprendizaje basado en redes con múltiples transformaciones parametrizadas.
- **Baseline:** regla o modelo simple usado como referencia.
- **Dato:** representación registrada de una observación, evento o entidad.
- **Generalización:** capacidad de funcionar sobre casos no utilizados durante el ajuste.
- **Modelo descriptivo:** representación que resume estructuras o patrones observados.
- **Modelo predictivo:** función que estima resultados no observados o futuros.
- **Modelo prescriptivo:** método que compara acciones considerando utilidad y restricciones.
- **Racionalidad:** selección de acciones con mejor desempeño esperado dada la información disponible.
- **Sesgo:** desviación sistemática producida por datos, mediciones, procedimientos o decisiones.

## Preguntas de autoevaluacion

1. ¿Por qué Ciencia de Datos e Inteligencia Artificial no son sinónimos?
2. ¿Qué diferencia existe entre describir, predecir y prescribir?
3. ¿Por qué una predicción precisa no garantiza una decisión útil?
4. ¿Qué papel cumplen la estadística, la optimización y la ingeniería de software?
5. ¿Qué diferencia existe entre actuar como humano y actuar racionalmente?
6. ¿Qué limitaciones tiene el test de Turing?
7. ¿Por qué los sistemas expertos pueden ser útiles y frágiles al mismo tiempo?
8. ¿Qué relación existe entre datos, cómputo y resurgimiento del aprendizaje profundo?
9. ¿Cómo puede aparecer un sesgo antes de entrenar un modelo?
10. ¿Qué condiciones justificarían abstenerse de automatizar una decisión?

## Actividad de reflexión

Seleccione una aplicación de su entorno y descríbala sin utilizar todavía un algoritmo. Identifique el fenómeno, la unidad de análisis, las observaciones disponibles, el resultado que se desea conocer, las acciones posibles, los costos de error y las personas afectadas. Finalmente, determine si la aplicación requiere descripción, predicción, prescripción o una combinación de ellas, y justifique qué nivel de automatización sería aceptable.
