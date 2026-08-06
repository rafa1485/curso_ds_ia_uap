<style>
@page { size: A4; margin: 16mm 16mm 17mm 16mm; }
body { font-family: "DejaVu Sans", sans-serif; color: #17324d; line-height: 1.38; font-size: 10pt; }
h1 { color: #17324d; border-bottom: 4px solid #007f82; padding-bottom: 8px; }
h2 { color: #17324d; border-bottom: 2px solid #e2a33a; padding-bottom: 4px; margin: 20px 0 8px; page-break-after: avoid; }
h3 { color: #007f82; margin: 12px 0 4px; page-break-after: avoid; }
h4 { color: #536471; margin: 9px 0 3px; page-break-after: avoid; }
p { margin: 6px 0; }
ul, ol { margin-top: 4px; margin-bottom: 8px; }
blockquote { border-left: 4px solid #e2a33a; background: #f3f6f8; margin: 10px 0; padding: 8px 12px; page-break-inside: avoid; }
table { border-collapse: collapse; width: 100%; font-size: 8.7pt; }
th { background: #17324d; color: white; }
th, td { border: 1px solid #aab7c1; padding: 6px; vertical-align: top; }
code { color: #007f82; }
strong { color: #17324d; }
</style>

# Guía docente: Fundamentos de Inteligencia Artificial

**Curso:** Inteligencia Artificial

**Semana y clase:** semana 1, clase 1

**Presentación asociada:** *Fundamentos de Inteligencia Artificial: agentes y racionalidad* (38 diapositivas)

**Fuentes:** capítulos 1 y 6 del libro *Ciencia de Datos e Inteligencia Artificial*

**Inteligencia Artificial (IA).** Es la disciplina que estudia y construye sistemas capaces de percibir, representar información, razonar, aprender, planificar, comunicarse o seleccionar acciones orientadas a objetivos. La sigla designa el campo y no implica por sí misma conciencia, comprensión humana general ni autonomía completa.

## Propósito y forma de uso

Esta guía desarrolla el contenido del libro que sostiene cada parte de la presentación. No está diseñada para ser proyectada ni leída literalmente durante la clase. Su función es ofrecer al docente el argumento completo: qué concepto introducir, cómo relacionarlo con los anteriores, qué fórmula interpretar, qué ejemplo desarrollar, qué error evitar y qué conclusión debe quedar antes de avanzar.

La presentación utiliza un caso transversal: un **asistente integrado de movilidad** que observa demanda, tráfico y estado de la flota; recomienda rutas o reasignaciones; comunica incertidumbre; puede abstenerse; y entrega la recomendación a una persona responsable de operaciones, quien conserva la autoridad de ejecución. Esta frontera se mantendrá en toda la exposición. Cuando el libro presenta por separado reasignación de flota y recomendación de rutas, la guía indicará que la clase realiza una adaptación integrada.

Las diapositivas 20 a 33 están organizadas en parejas. La primera desarrolla el concepto mediante texto y la segunda lo representa con un diagrama. En esos casos la guía distingue qué explicar antes de mostrar el gráfico y cómo recorrer visualmente sus elementos.

**PEAS (por *Performance measure, Environment, Actuators, Sensors*).** Es un marco para especificar la tarea de un agente mediante cuatro componentes: medida de desempeño, entorno, actuadores y sensores. Comienza por las consecuencias que deben evaluarse y luego delimita dónde opera el agente, qué acciones puede producir y qué información puede percibir.

### Recorrido de la clase

| Bloque | Diapositivas | Resultado esperado |
|---|---:|---|
| Delimitación | 1-5 | Diferenciar IA, aprendizaje automático y Ciencia de Datos |
| Enfoques y racionalidad | 6-13 | Comparar cuatro criterios de inteligencia y explicar racionalidad bajo incertidumbre |
| Fundamentos e historia | 14-19 | Relacionar métodos con bases disciplinares, datos, cómputo y límites |
| Agentes y ambientes | 20-33 | Especificar agente, PEAS y propiedades del entorno de movilidad |
| Aplicación y cierre | 34-38 | Producir, revisar y defender una especificación inicial |

> **Idea transversal del libro:** un modelo no es una decisión. Un modelo representa, resume o estima; una decisión selecciona una acción dentro de un contexto con objetivos, restricciones, costos y responsabilidades.

## Diapositivas 1-2. Portada y propósito

**Correspondencia con el libro:** capítulo 1, propósito y §1.1.2; capítulo 6, propósito y objetivos de aprendizaje.

### Contenido que debe exponerse

La apertura debe ubicar la clase como una construcción conceptual, no como una introducción a una herramienta concreta. La pregunta general es cómo diseñar sistemas que transforman información en comportamiento orientado a objetivos. Para responderla se necesitan tres niveles.

El primer nivel es **definitorio**: qué capacidades estudia la IA y por qué esa definición no exige conciencia o comprensión humana general. El segundo nivel es **evaluativo**: con qué criterio llamamos inteligente a un sistema. El tercero es **operacional**: cómo describimos una entidad que percibe, mantiene información, elige una acción y produce consecuencias en un entorno.

Los resultados de aprendizaje deben presentarse como capacidades observables. Al terminar, el estudiante deberá poder comparar los cuatro enfoques clásicos, explicar por qué racionalidad no equivale a perfección, distinguir un predictor de un agente, construir una especificación PEAS y justificar las propiedades del ambiente de movilidad. Todavía no se busca implementar un algoritmo. El propósito es formular correctamente la tarea que luego permitirá seleccionar reglas, búsqueda, planificación o aprendizaje.

### Énfasis docente

- La clase no define IA por una única técnica contemporánea.
- La inteligencia se evaluará respecto de una tarea y de sus consecuencias.
- El caso de movilidad servirá para integrar los conceptos, no para reducirlos a un solo dominio.

**Transición sugerida:** “Antes de adoptar una definición técnica, examinemos qué criterios usamos espontáneamente para decir que una máquina es inteligente”.

## Diapositiva 3. Pregunta de apertura

**Correspondencia con el libro:** capítulo 1, introducción de §1.2 y §§1.2.1-1.2.4.

### Contenido que debe exponerse

La pregunta “¿cuándo podemos afirmar que un sistema se comporta de manera inteligente?” no tiene una única respuesta porque la palabra inteligencia puede referirse a objetos de evaluación diferentes. Si observamos la conducta, interesa qué hace el sistema. Si observamos el proceso, interesa cómo llega a la respuesta. Si adoptamos la lógica, interesa si las conclusiones se siguen válidamente de las premisas. Si adoptamos la acción racional, interesa si la conducta produce el mejor desempeño esperado según la información disponible.

Conviene recoger ejemplos de los estudiantes y clasificarlos sin corregir inmediatamente. Un chatbot que imita una conversación corresponde inicialmente al criterio conductual. Un modelo psicológico de memoria corresponde al enfoque cognitivo. Un demostrador de teoremas representa las leyes del pensamiento. Un sistema que asigna recursos según costos y restricciones corresponde al agente racional.

La conclusión no debe ser que uno de los cuatro enfoques es universalmente correcto. Son preguntas diferentes. Un sistema puede conversar de manera convincente y, al mismo tiempo, utilizar premisas falsas. Puede producir una inferencia válida y seleccionar una acción perjudicial porque su función de utilidad es inadecuada.

> **Comprobación breve:** si dos sistemas producen la misma respuesta, ¿eso demuestra que pensaron del mismo modo? Respuesta esperada: no; la similitud de resultados no implica similitud del proceso.

## Diapositivas 4-5. Qué estudia la IA y relación con otros campos

**Correspondencia con el libro:** capítulo 1, §§1.1.1-1.1.3, §1.1.5 y síntesis.

### Qué debe explicarse en la diapositiva 4

La Inteligencia Artificial estudia la construcción de sistemas capaces de realizar tareas asociadas con percibir, representar estados, razonar, aprender, planificar, comunicarse y actuar. Esta lista describe capacidades funcionales. No permite concluir que el sistema posea conciencia, intención propia o comprensión general. Un sistema puede mostrar una capacidad sofisticada en una tarea estrecha y seguir dependiendo de un procedimiento, datos y objetivos definidos externamente.

Una forma mínima de representar la conducta es:

$$
a_t=\pi(h_t),
$$

donde $h_t$ es la historia de información disponible hasta el instante $t$, $a_t$ es la acción y $\pi$ es la política o regla de decisión. La política puede ser una tabla de reglas, un procedimiento de búsqueda o un modelo aprendido. La complejidad de $\pi$ no basta para determinar si la conducta es adecuada.

Debe distinguirse **capacidad** de **autonomía**. Un clasificador puede reconocer imágenes sin decidir qué hacer con la etiqueta. La autonomía aumenta cuando el sistema selecciona y ejecuta acciones con menos intervención humana. A medida que aumenta, también deben aumentar supervisión, trazabilidad, seguridad y posibilidad de reversión.

### Qué debe explicarse en la diapositiva 5

La Ciencia de Datos produce evidencia a partir de observaciones. El aprendizaje automático ajusta funciones o políticas a partir de ejemplos o experiencia. La IA construye sistemas que pueden incluir percepción, razonamiento, aprendizaje y acción. Hay superposición, pero no identidad.

- Un sistema experto basado en reglas puede ser IA sin aprendizaje automático.
- Una regresión puede formar parte de Ciencia de Datos sin constituir un agente.
- Un modelo predictivo puede ser un componente dentro de un sistema inteligente, pero no define por sí solo quién actúa.

El libro formaliza un problema de datos como:

$$
P=(U,O,X,Y,A,H,C),
$$

donde $U$ es la unidad de análisis, $O$ el objetivo, $X$ las variables, $Y$ el resultado, $A$ las acciones, $H$ el horizonte y $C$ las restricciones. La fórmula resulta útil aquí porque muestra que pasar de predicción a decisión requiere declarar acciones, horizonte y restricciones. Una probabilidad aislada no indica qué conviene hacer.

> **Advertencia:** los datos son representaciones parciales del fenómeno. Tener muchos registros no significa observar todo aquello que importa para decidir.

**Transición sugerida:** “Ya sabemos qué capacidades abarca la IA; ahora compararemos cuatro criterios para evaluar esas capacidades”.

## Diapositiva 6. Cuatro enfoques clásicos

**Correspondencia con el libro:** capítulo 1, §1.2 y §§1.2.1-1.2.4.

### Contenido que debe exponerse

La matriz cruza dos ejes. El primero diferencia **pensar** y **actuar**. El segundo compara con el ser humano o con un criterio de racionalidad. De esa combinación surgen cuatro enfoques.

1. **Pensar como humanos:** intenta modelar procesos cognitivos.
2. **Actuar como humanos:** compara conducta observable.
3. **Pensar racionalmente:** aplica reglas de inferencia válida.
4. **Actuar racionalmente:** selecciona acciones por desempeño esperado.

La tabla no describe cuatro tecnologías separadas. Un asistente puede evaluarse simultáneamente por fluidez conversacional, semejanza de su proceso con el humano, coherencia de sus inferencias y utilidad de sus recomendaciones. Cada evaluación requiere evidencia distinta.

Debe evitarse asociar “racional” con infalible, emocionalmente frío o moralmente correcto. En el libro, racionalidad significa elegir bien respecto de información, alternativas, objetivos y restricciones. Si el objetivo está mal definido, optimizarlo no vuelve aceptable la conducta.

### Recorrido de la tabla

Comenzar por las filas: pensar frente a actuar. Luego recorrer las columnas: comparación humana frente a norma racional. Finalizar preguntando qué evidencia se necesitaría para cada cuadrante. Esa pregunta prepara las cuatro diapositivas siguientes.

## Diapositivas 7-9. Conducta humana, test de Turing y cognición

**Correspondencia con el libro:** capítulo 1, §§1.2.1, 1.2.2 y 1.2.5.

### Diapositiva 7: actuar como humanos

El enfoque conductual evalúa si el comportamiento es comparable con el de una persona en una tarea definida. Puede incluir conversación, percepción, movimiento o uso de herramientas. Su ventaja es metodológica: permite observar resultados sin resolver primero qué significa pensar.

La comparación necesita tres delimitaciones: **tarea**, **contexto** y **población de referencia**. No existe una propiedad única llamada “actuar como una persona”. Una respuesta puede ser rápida pero imprecisa; una persona experta y una principiante no constituyen el mismo criterio; un sistema puede funcionar en condiciones normales y fallar ante ruido.

Una conducta convincente tampoco demuestra comprensión. Reglas específicas, recuperación de textos o generación estadística pueden producir respuestas plausibles. Por eso deben separarse fluidez, precisión, evidencia y seguridad.

### Diapositiva 8: test de Turing

El test propone que una persona converse por un canal textual con interlocutores ocultos e intente distinguir a la máquina. Su aporte histórico es transformar una pregunta filosófica general en una prueba de comportamiento.

No debe presentarse como certificación de inteligencia general. Una conversación no evalúa necesariamente percepción física, planificación prolongada, comprensión causal o desempeño en situaciones nuevas. Un sistema puede aprovechar imitación, evasión o respuestas plausibles. Superar una prueba tampoco demuestra que sus afirmaciones sean verdaderas ni que su uso sea seguro en un dominio sensible.

### Diapositiva 9: pensar como humanos

El modelado cognitivo estudia percepción, memoria, aprendizaje, lenguaje, tiempos de respuesta y patrones de error. Su pregunta no es solo si la respuesta es correcta, sino qué proceso podría explicarla. Un programa puede explorar miles de alternativas, usar memoria perfecta o explotar señales inaccesibles a una persona; por eso un resultado humano no implica un proceso humano.

Los enfoques conductual y cognitivo son complementarios. El primero pregunta si se cumple la tarea; el segundo pregunta cómo. El libro agrega un tercer nivel práctico: aunque el sistema cumpla y su proceso sea explicable, todavía debemos verificar si es seguro, trazable y apropiado para la decisión.

> **Ejemplo para exponer:** dos asistentes responden correctamente un reclamo. Uno consulta reglas y antecedentes; el otro genera una frase por similitud estadística. La respuesta final no permite distinguir sus procesos ni su confiabilidad fuera del caso observado.

## Diapositivas 10-11. Pensamiento racional e incertidumbre

**Correspondencia con el libro:** capítulo 1, §1.2.3 y conexión con §1.2.4; capítulo 6, §6.1.6 como ampliación.

### Diapositiva 10: inferencia lógica

Pensar racionalmente significa derivar conclusiones válidas desde premisas. El ejemplo básico es el modus ponens:

$$
A\rightarrow B,\qquad A\qquad\therefore B.
$$

La lógica hace explícitos hechos, reglas y conclusiones. Esa trazabilidad es valiosa para auditar el razonamiento. Sin embargo, validez no equivale a verdad. Si el sensor informa erróneamente que existe congestión, la inferencia puede ser válida respecto de una premisa falsa. También aparecen dificultades cuando el conocimiento es incompleto, ambiguo o posee excepciones.

Debe destacarse la separación entre tres preguntas: ¿la regla está bien formada?, ¿la premisa representa el mundo?, ¿la conclusión justifica una acción? La lógica responde principalmente la primera.

### Diapositiva 11: probabilidad condicionada

Cuando la evidencia no permite afirmaciones absolutas, la probabilidad representa grados de creencia:

$$
P(H\mid E),
$$

donde $H$ es una hipótesis y $E$ la evidencia. Una probabilidad de congestión de $0{,}75$ significa una creencia condicionada por el modelo y las observaciones; no es certeza ni garantía sobre el caso individual.

La estimación todavía no define la decisión. Debemos conocer acciones, consecuencias, costos de error y posibilidad de obtener más información. Si una medición adicional puede cambiar significativamente la acción, su valor esperado puede justificar el costo y la demora de obtenerla.

> **Ampliación opcional:** el valor de la información compara el desempeño esperado antes y después de observar un dato. Más información no siempre conviene: puede ser imperfecta, tardía o costosa.

**Transición sugerida:** “La probabilidad organiza creencias; la acción racional agrega preferencias y consecuencias”.

## Diapositivas 12-13. Acción racional, límites y omnisciencia

**Correspondencia con el libro:** capítulo 1, §§1.1.2 y 1.2.4; capítulo 6, §§6.1.4-6.1.6.

### Diapositiva 12: utilidad esperada

Un agente actúa racionalmente cuando selecciona la acción con mejor desempeño esperado dadas la evidencia, las alternativas factibles, el conocimiento previo y sus recursos. Una forma clásica es:

$$
a^*=\operatorname*{arg\,max}_a\sum_s P(s\mid E)U(a,s).
$$

$s$ representa un estado posible, $P(s\mid E)$ la creencia condicionada y $U(a,s)$ la utilidad de ejecutar $a$ si ocurre $s$. La suma pondera consecuencias posibles. La fórmula no elimina la incertidumbre: la incorpora en la comparación.

La utilidad debe reflejar resultados relevantes y las restricciones deben separar acciones inadmisibles. No toda condición debe convertirse en un costo negociable. Una violación de seguridad o legalidad puede excluir una acción antes de optimizar entre las restantes.

### Diapositiva 13: racionalidad no es perfección

La racionalidad se juzga con la información disponible al decidir. Un resultado malo no demuestra irracionalidad, y un resultado favorable no convierte en racional una apuesta temeraria. El libro ilustra esta diferencia con una falla de probabilidad $0{,}30$, una pérdida de 100 y una inspección de costo 10:

$$
0{,}30\times100=30>10.
$$

Inspeccionar minimiza el costo esperado. Si luego se descubre que no había falla, la decisión sigue siendo racional. Solo un agente omnisciente habría conocido el resultado de ese caso antes de actuar.

La **racionalidad limitada** reconoce tiempo, cómputo y datos finitos. Una solución perfecta que llega después del evento no tiene valor. La **autonomía** describe cuánto depende la conducta de experiencia propia; no equivale a ausencia de supervisión. Un agente puede aprender patrones y requerir aprobación humana para acciones críticas.

> **Advertencia de alineación:** maximizar una métrica mal elegida puede producir una conducta eficiente pero inaceptable. La ley de Goodhart señala que, al convertir una medida en objetivo, esta puede dejar de representar el propósito.

## Diapositivas 14-15. Fundamentos y anatomía de un sistema

**Correspondencia con el libro:** capítulo 1, §§1.1.4 y 1.2.6.

### Fundamentos disciplinares

La IA combina tradiciones filosóficas y herramientas formales. El racionalismo destaca estructuras explícitas de razón; el empirismo, aprendizaje desde experiencia; el pragmatismo, evaluación por consecuencias. Estas tradiciones reaparecen en sistemas basados en conocimiento, modelos aprendidos y agentes orientados a utilidad.

La lógica aporta representación y deducción. La probabilidad permite razonar con incertidumbre. La teoría de decisión conecta creencias con acciones mediante utilidad. La optimización selecciona parámetros, planes o políticas. Álgebra lineal y cálculo sostienen modelos numéricos; teoría de la información cuantifica incertidumbre; computación aporta representaciones, algoritmos y límites de complejidad.

La ingeniería de software convierte un método en sistema operable mediante pruebas, seguridad, control de versiones, monitoreo y gestión de dependencias. Una demostración aislada no equivale a un sistema confiable.

### Anatomía funcional

La diapositiva 15 separa percepción, representación, memoria, inferencia o aprendizaje, evaluación de acciones y ejecución con retroalimentación. Esta separación sirve para diagnosticar fallos. Una recomendación incorrecta puede originarse en un sensor, un estado interno incompleto, una predicción, una función de desempeño o un actuador.

**Sistema de Posicionamiento Global (GPS).** Es un sistema de navegación por satélite que proporciona estimaciones de posición, velocidad y tiempo. Como sensor, está sujeto a error, pérdida de señal, latencia y cobertura, por lo que cada lectura debe acompañarse de marca temporal y calidad.

Conviene recorrer un fallo de extremo a extremo: un GPS desactualizado produce una percepción incorrecta; el estado ubica mal al vehículo; el plan propone una reasignación inviable; el responsable la rechaza. Atribuir todo el error al “modelo de IA” ocultaría el mecanismo real.

## Diapositivas 16-18. Evolución histórica

**Correspondencia con el libro:** capítulo 1, §1.3 y §§1.3.1-1.3.4.

### Diapositiva 16: lectura de la historia

La historia no es una sucesión lineal de inventos mejores. Cada periodo combina una representación dominante, datos disponibles, capacidad de cómputo y expectativas. Un método puede ser correcto pero impracticable; puede funcionar en un mundo acotado y fallar en un entorno abierto; puede reaparecer cuando cambian los recursos.

Los antecedentes incluyen lógica, probabilidad, estadística, teoría de decisión, información y algoritmos. Esas herramientas no nacieron como IA, pero hoy sostienen clasificación, inferencia, búsqueda y control.

### Diapositiva 17: nacimiento y sistemas simbólicos

Dartmouth 1956 se considera un hito nominal. Los primeros proyectos abordaron teoremas, juegos y problemas expresables como búsqueda sobre estados. La dificultad apareció cuando el espacio creció, el lenguaje resultó ambiguo y la percepción incorporó ruido.

Los sistemas expertos separaron base de conocimiento y motor de inferencia. Permiten explicar conclusiones mediante cadenas de reglas e incorporar conocimiento con pocos datos. Sus límites son adquisición costosa, mantenimiento, excepciones y fragilidad. Las reglas no son objetivas por ser explícitas: reflejan decisiones, categorías y omisiones de quienes las diseñan.

Los enfoques simbólicos y estadísticos pueden combinarse. Un modelo aprendido puede percibir y un conjunto de reglas puede restringir acciones inseguras.

### Diapositiva 18: inviernos y resurgimiento

Los inviernos de la IA estuvieron asociados con promesas excesivas, resultados difíciles de generalizar, falta de datos y cómputo, y sistemas frágiles. La experiencia mostró que resolver un problema pequeño no equivale a inteligencia general y que la dificultad puede provenir de una representación inadecuada, no solo de falta de potencia.

El resurgimiento estadístico se apoyó en datasets extensos, sensores, almacenamiento económico, redes y procesadores especializados. El centro de gravedad pasó hacia métodos que aprenden regularidades. No desaparecieron sesgo, deriva ni evaluación; cambiaron las herramientas y la escala.

## Diapositiva 19. Aprendizaje profundo e IA generativa

**Correspondencia con el libro:** capítulo 1, §§1.1.3 y 1.3.5.

### Contenido que debe exponerse

**Unidad de procesamiento gráfico (GPU, por *Graphics Processing Unit*).** Es un procesador especializado en ejecutar muchas operaciones numéricas en paralelo. Aunque surgió para procesamiento gráfico, su arquitectura permite acelerar el entrenamiento y la ejecución de modelos de aprendizaje profundo basados en grandes cantidades de operaciones matriciales.

El aprendizaje profundo utiliza capas de transformaciones para aprender representaciones intermedias. En imágenes pueden emerger bordes, texturas y formas; en texto, relaciones entre unidades y contexto. Su expansión estuvo vinculada con datos, GPU, arquitecturas diferenciables y técnicas de entrenamiento más estables.

Los modelos fundacionales se preentrenan sobre colecciones amplias y se adaptan a tareas. Un modelo autoregresivo representa una secuencia como:

$$
P(x_1,\ldots,x_T)=P(x_1)\prod_{t=2}^{T}P(x_t\mid x_1,\ldots,x_{t-1}).
$$

La factorización permite generar paso a paso: cada elemento se produce condicionado por los anteriores. No garantiza que el contenido sea verdadero. La fluidez indica ajuste a patrones de generación, no conocimiento verificado. En aplicaciones reales se requieren recuperación de fuentes, validación, límites de uso y supervisión.

> **Advertencia:** “aprender” significa ajustar regularidades útiles para un objetivo. No implica comprensión humana y puede explotar correlaciones espurias o artefactos.

## Diapositivas 20-21. Concepto de agente

**Correspondencia con el libro:** capítulo 6, §§6.1.1-6.1.3; capítulo 1, §1.1.2.

### Diapositiva 20: desarrollo conceptual

Un agente es una entidad que percibe un entorno mediante sensores y actúa sobre él mediante actuadores. La definición incluye sistemas físicos o informacionales. Lo esencial es el ciclo percepción-acción, no que tenga cuerpo, aprenda o utilice una técnica compleja.

La frontera es una decisión de modelado. En movilidad el agente podría ser un vehículo, el coordinador de toda la flota o el conjunto conductor-vehículo. Si el conductor queda fuera, su aceptación debe observarse y su conducta forma parte del entorno. Si queda dentro, la decisión humana integra el mecanismo interno.

El ciclo puede formalizarse como:

$$
p_t=O(e_t),\qquad a_t=\pi(p_1,\ldots,p_t),\qquad e_{t+1}\sim T(e_t,a_t).
$$

$e_t$ es el estado real; $O$ produce una percepción parcial; $\pi$ selecciona una acción; y $T$ describe la transición, posiblemente incierta. No debe suponerse que percepción y estado son idénticos.

La función de agente especifica conducta:

$$
f:P^*\rightarrow A.
$$

El programa implementa esa función sobre una arquitectura. Una misma función puede tener implementaciones distintas, y un mismo programa puede comportarse de otro modo si cambian sensores, memoria o tiempo disponible. En síntesis:

$$
Agente=Arquitectura+Programa.
$$

### Diapositiva 21: recorrido del diagrama

Comenzar arriba con sensores y percepciones. Señalar que el sensor es el mecanismo y la percepción es la información resultante. Continuar hacia el estado interno y la decisión. Descender a acciones y actuadores. Finalizar con la línea discontinua: el efecto vuelve a observarse y actualiza la información.

El mensaje final del diagrama es que un predictor aislado no es necesariamente un agente. Si solo estima demora, es un componente inferencial. Se convierte en parte de un agente cuando su salida participa en una política que selecciona recomendaciones o acciones.

> **Error frecuente:** llamar agente a cualquier modelo que produce una salida.

## Diapositivas 22-23. Agente, entorno y retroalimentación

**Correspondencia con el libro:** capítulo 6, §§6.1.1-6.1.2 y ejemplo §6.2.8.

### Diapositiva 22: distinciones operativas

Una **percepción** es contenido informativo recibido en un instante. La secuencia de percepciones acumula experiencia. Un valor aislado puede ser ambiguo; una serie permite detectar tendencia. Un **sensor** es el mecanismo de adquisición y debe caracterizarse por unidad, frecuencia, resolución, latencia, cobertura y error.

Una **acción** es una decisión abstracta; un **actuador** es el canal que intenta materializarla. “Recomendar mover un vehículo a la zona B” es una acción del asistente. El mensaje enviado al responsable es el actuador. La reasignación efectiva depende de aprobación, disponibilidad y conducta del conductor.

La orden emitida no garantiza el efecto. Puede haber demora, rechazo o falla. Por eso se requiere retroalimentación. “Sin lectura” tampoco equivale a “valor cero”: debe representarse como información ausente y activar una política de respaldo.

### Diapositiva 23: lectura del diagrama

Empezar por la frontera entre entorno y agente. La flecha superior lleva percepciones hacia el agente; la inferior devuelve acciones al entorno. Luego señalar los ejemplos de sensores y actuadores. Finalizar con la pregunta de frontera: ¿el conductor está dentro o fuera?

Para el caso transversal se adopta esta respuesta: el asistente es el agente técnico y el responsable humano queda fuera, dentro del entorno organizacional. El asistente recomienda; la persona aprueba. Esto permite auditar por separado recomendación y ejecución.

> **Comprobación breve:** si el asistente recomienda una ruta y el conductor no la sigue, ¿falló necesariamente el algoritmo? No; debe verificarse el canal, la aceptación y la diferencia entre acción emitida y efecto.

## Diapositivas 24-25. Especificación PEAS

**Correspondencia con el libro:** capítulo 6, §§6.1.4 y 6.2.1.

### Diapositiva 24: contenido de PEAS

PEAS organiza **desempeño**, **entorno**, **actuadores** y **sensores**. El orden comienza por desempeño para evitar que la tecnología disponible defina accidentalmente el propósito.

La medida de desempeño debe declarar:

- unidad de evaluación: viaje, usuario, zona o trayectoria;
- horizonte: minutos, jornada o periodo prolongado;
- resultados positivos: puntualidad, cobertura o seguridad;
- costos: demora, distancia vacía, falsas alarmas o intervención;
- restricciones: capacidad, legalidad, seguridad y equidad;
- agregación: media, percentil, peor caso o combinación;
- fuente de verdad: cómo y cuándo se verifica el efecto.

Una forma general sobre una trayectoria $\tau$ es:

$$
J(\tau)=\sum_{t=0}^{H}w_t r(e_t,a_t)-\sum_{t=0}^{H}q(e_t,a_t),
$$

donde $r$ representa beneficios y $q$ costos. La fórmula es una plantilla, no una obligación de convertir todo en suma. Una restricción de seguridad puede excluir acciones antes de comparar utilidad.

El entorno enumera procesos y actores externos. Los actuadores especifican canales reales y reversibilidad. Los sensores declaran información y calidad. Un PEAS es consistente cuando cada criterio puede verificarse, cada acción tiene actuador y cada supuesto no observable aparece como incertidumbre.

### Diapositiva 25: lectura del diagrama

Comenzar por el círculo central, la tarea. Ir primero a P y preguntar qué consecuencia se valora. Continuar con E para delimitar lo externo. Después A para determinar autoridad efectiva y S para verificar qué puede observarse. Las flechas muestran dependencia: no se eligen sensores y acciones sin haber definido propósito y entorno.

> **Error frecuente:** escribir “GPS” como especificación completa de sensor o “optimizar movilidad” como desempeño. Ambos necesitan unidades, alcance y criterios.

## Diapositivas 26-27. Propiedades del ambiente

**Correspondencia con el libro:** capítulo 6, introducción de §6.2 y §§6.2.2-6.2.7.

### Diapositiva 26: seis dimensiones

**Observable o parcialmente observable.** Un entorno es completamente observable si la percepción contiene toda la información relevante para decidir. En observabilidad parcial se mantiene una creencia sobre estados posibles:

$$
b_t(s)=P(S_t=s\mid p_{1:t},a_{1:t-1}).
$$

Muchos datos no garantizan observabilidad completa. Debe evaluarse qué estaba disponible en el instante real de decisión.

**Determinista o estocástico.** En un entorno determinista, estado y acción fijan el siguiente estado. En uno estocástico existen varios resultados. La incertidumbre puede ser aleatoria o provenir de conocimiento insuficiente. Una transición más probable no debe tratarse como segura.

**Episódico o secuencial.** En un entorno episódico las decisiones son independientes. En uno secuencial la acción actual afecta oportunidades futuras. El desempeño puede expresarse como $J=\sum_{t=0}^{H}r_t$; por eso no basta optimizar el instante actual. La clasificación depende del horizonte.

**Estático o dinámico.** Un entorno dinámico cambia mientras el agente delibera. La relación

$$
\rho=\frac{\text{tiempo de deliberación}}{\text{escala de cambio relevante}}
$$

ayuda a determinar si se necesita actualizar, interrumpir o usar una política de respaldo. Aumentar frecuencia sin control puede introducir ruido u oscilación.

**Discreto o continuo.** Estado, acción, observación y tiempo pueden tener representaciones distintas. Discretizar facilita búsqueda, pero pierde información y puede crear cambios abruptos cerca de umbrales.

**Monoagente o multiagente.** En un entorno multiagente otros actores eligen y adaptan acciones. Las personas no son obstáculos pasivos: interpretan recomendaciones, pueden rechazarlas y cambian ante incentivos.

### Diapositiva 27: lectura del diagrama

Recorrer cada eje como un continuo de caracterización, no como etiquetas universales. Finalizar en la franja inferior: frontera, representación y escala temporal determinan la clasificación. La conclusión es operativa: de cada dimensión deben derivarse requisitos de memoria, incertidumbre, actualización, planificación o coordinación.

## Diapositivas 28-29. Recomendador de rutas

**Correspondencia con el libro:** capítulo 6, §6.2.8 y apoyo de §§6.2.2-6.2.7.

### Diapositiva 28: justificación de la clasificación

El sistema es **parcialmente observable** porque desconoce demanda futura, incidentes e intenciones de otros conductores. Es **estocástico** porque una misma ruta y hora pueden producir demoras diferentes. Es **secuencial** porque recomendar o reasignar modifica cobertura y opciones posteriores. Es **dinámico** porque el tráfico cambia durante el cálculo. Combina variables continuas, como tiempo y velocidad, con acciones discretas. Es **multiagente** porque conductores y pasajeros responden.

La clasificación no termina en las etiquetas. La observabilidad parcial exige estimar estado e incertidumbre. El dinamismo exige caducidad y replanificación. La secuencialidad obliga a considerar disponibilidad futura. La interacción requiere modelar aceptación y evitar que muchas recomendaciones concentren vehículos en la misma ruta.

### Ejemplo comparativo

La ruta A demora 15 minutos en promedio, pero presenta alta variabilidad. La ruta B demora 19 minutos y es estable. Para un compromiso crítico, elegir A solo por la media puede ser incorrecto. Debe compararse el costo de llegar tarde y la distribución de resultados.

Si 30 vehículos reciben simultáneamente la ruta A, la recomendación cambia el tráfico que intentaba predecir. El modelo deja de ser válido si supone un entorno constante. Este es un ejemplo de retroalimentación y multiagencia.

### Diapositiva 29: lectura del diagrama

Comenzar por el agente central y seguir las recomendaciones hacia las zonas. Luego señalar las líneas de tráfico y demanda entre zonas. La mitad derecha conecta propiedades con razones. Cerrar con el bloque “requisitos derivados”: la clasificación se traduce en componentes de diseño y pruebas.

## Diapositivas 30-31. Caso transversal integrado

**Correspondencia con el libro:** adaptación de capítulo 1, §1.1.6, y capítulo 6, §§6.1.1, 6.1.5 y 6.2.8.

### Diapositiva 30: formulación del asistente

La clase integra dos ejemplos del libro. El capítulo 1 formula la reasignación de vehículos entre zonas; el capítulo 6 desarrolla un recomendador de rutas. El asistente integrado puede proponer ambas acciones, pero no ejecutarlas autónomamente.

La necesidad “reducir demoras” debe convertirse en una tarea verificable. La unidad puede ser viaje o zona-franja horaria. El horizonte es la próxima ventana operativa. El usuario es el responsable de operaciones. Las acciones son recomendar ruta, proponer reasignación, mantener distribución, pedir información, alertar o abstenerse.

La autoridad debe ser explícita. El asistente produce una recomendación con evidencia y confianza. La persona responsable aprueba, modifica o rechaza. Esta separación permite asignar responsabilidad y evita presentar una salida predictiva como ejecución automática.

La recomendación necesita caducidad. Una ruta calculada con tráfico de hace veinte minutos puede ser inválida. La abstención se activa ante datos desactualizados, contradicción entre fuentes, baja trazabilidad o riesgo fuera del dominio previsto.

### Diapositiva 31: lectura del flujo

Recorrer de izquierda a derecha: demanda y flota, asistente, recomendación con confianza, responsable y acción. La rama inferior muestra abstención y escalamiento. La línea discontinua devuelve el efecto a las observaciones. Destacar que la persona no es un adorno en el diagrama: posee autoridad efectiva.

> **Ejemplo:** si falta conexión con varios vehículos, el asistente no debe reasignarlos como si estuvieran disponibles. Debe declarar incertidumbre, mantener una distribución segura y solicitar confirmación.

## Diapositivas 32-33. PEAS del asistente integrado

**Correspondencia con el libro:** capítulo 6, §§6.1.4, 6.2.1 y 6.2.8; conexión con capítulo 1, §1.1.6.

### Diapositiva 32: especificación textual

**Desempeño.** Combinar demora media, percentil alto de espera, cancelaciones, distancia vacía, seguridad, equidad y cobertura territorial. El promedio no basta: puede ocultar colas extremas y desigualdad entre zonas. Las restricciones de seguridad y capacidad son duras.

**Entorno.** Red vial, zonas, vehículos, conductores, pasajeros, peatones, tráfico, clima, obras, eventos, regulación y responsable de operaciones. Los actores reaccionan a las recomendaciones.

**Actuadores.** Emitir una recomendación de ruta, proponer una reasignación, recomendar mantener la distribución, actualizar una estimación, solicitar confirmación, alertar o abstenerse. “Asignar vehículo” se evita porque el agente no posee autoridad ejecutiva.

**Sensores.** GPS, velocidad, viajes activos, solicitudes, ocupación, capacidad, mapa, cierres, tráfico, clima, aceptación del conductor y calidad de conexión. Cada fuente debe incluir marca temporal, cobertura, error y disponibilidad.

### Riesgo de desalineación

Minimizar la demora media puede concentrar vehículos en zonas de alta demanda y reducir servicio de zonas remotas. El libro propone complementar media con percentil 90 y diferencia máxima entre zonas. La ley de Goodhart obliga a auditar cómo cambia la conducta cuando la métrica se vuelve objetivo.

### Diapositiva 33: lectura del diagrama

Recorrer P, E, A y S en ese orden. Señalar que las líneas cruzadas expresan coherencia: los sensores deben permitir estimar desempeño y estado; los actuadores deben ser factibles dentro del entorno. La vista visual resume; la tabla anterior contiene la especificación normativa completa.

> **Comprobación breve:** ¿por qué “cantidad de recomendaciones emitidas” sería una mala medida? Porque evalúa actividad y puede aumentar sin mejorar el servicio.

## Diapositiva 34. Actividad guiada

**Correspondencia con el libro:** capítulo 6, §§6.1.7, 6.2.8 y actividad integradora de cierre.

### Producto esperado

Cada equipo elaborará una ficha inicial del asistente integrado. Debe incluir:

1. propósito, usuario y personas afectadas;
2. frontera del agente y autoridad efectiva;
3. PEAS con unidades y calidad de sensores;
4. clasificación razonada en seis dimensiones;
5. medida de desempeño con horizonte y al menos una restricción dura;
6. acción de abstención o falla segura;
7. riesgo de desalineación;
8. tres escenarios de prueba.

### Ejemplo mínimo

**Percentil 90 (P90).** Es el valor que no supera el 90 % de las observaciones y deja por encima el 10 % más alto. En movilidad permite vigilar esperas extremas que una media puede ocultar, por lo que complementa las medidas de tendencia central.

**Situación:** aumenta la demanda en zona B y hay tres vehículos libres. **Percepciones:** ubicación, ocupación, solicitudes y tráfico con marcas temporales. **Acciones:** mantener distribución, proponer mover uno o dos vehículos, pedir confirmación o abstenerse. **Restricción:** no reducir cobertura de zona A por debajo del mínimo. **Desempeño:** espera media y P90, distancia vacía y cobertura. **Falla segura:** si dos posiciones están desactualizadas, no asumir disponibilidad y escalar al responsable.

### Escenarios obligatorios

- **Normal:** sensores actualizados y recomendación aceptada.
- **Información faltante:** GPS o conexión ausente; el agente debe explicitar incertidumbre.
- **Adverso:** incidente vial posterior a la recomendación; debe detectar caducidad y replanificar.

Durante el trabajo, el docente debe revisar primero autoridad y desempeño. Los equipos suelen comenzar por sensores o algoritmos; PEAS exige comenzar por consecuencias.

## Diapositivas 35-36. Revisión y defensa

**Correspondencia con el libro:** capítulo 6, errores comunes y criterios de revisión; actividad integradora de cierre.

### Criterios de revisión

La especificación es aceptable si existe coherencia temporal y operacional. Las entradas deben estar disponibles antes de recomendar. Cada acción debe tener un canal real. El desempeño debe medir consecuencias y no actividad. La clasificación del ambiente debe estar justificada y producir requisitos. La abstención debe ser concreta.

Aplicar estas preguntas correctivas:

| Riesgo | Pregunta de revisión |
|---|---|
| Confundir predicción y acción | ¿Quién recomienda, quién aprueba y quién ejecuta? |
| Usar información futura | ¿El dato existía cuando se tomó la decisión? |
| Suponer observabilidad | ¿Qué estados distintos generan la misma percepción? |
| Tratar lo probable como seguro | ¿Qué otros resultados son plausibles y costosos? |
| Optimizar el instante | ¿Cómo afecta esta acción la cobertura futura? |
| Negociar seguridad | ¿Es una preferencia o una condición inadmisible? |
| Omitir retroalimentación | ¿Cómo se confirma el efecto y se corrige el estado? |

### Puesta en común

Cada equipo presenta acción principal, medida de desempeño, propiedad crítica y condición de abstención. La defensa no debe premiar complejidad algorítmica. Se valora la coherencia entre necesidad, PEAS, autoridad y ambiente.

La retroalimentación docente debe seleccionar un supuesto y someterlo a tensión. Por ejemplo: “¿qué ocurre si todos los conductores rechazan la recomendación?”, “¿qué ocurre si la zona remota tiene pocos viajes pero consecuencias graves?” o “¿qué cambia si la conexión tiene diez minutos de demora?”.

## Diapositiva 37. Síntesis

**Correspondencia con el libro:** capítulo 1, síntesis; capítulo 6, síntesis integradora.

### Contenido de cierre

La inteligencia puede evaluarse como conducta, proceso cognitivo, inferencia o acción racional. Ningún criterio por sí solo garantiza que una aplicación sea segura o apropiada. La historia muestra que los métodos dependen de representaciones, recursos y expectativas.

Un agente se define por el ciclo percepción-acción respecto de una tarea. La función especifica conducta; el programa la implementa bajo límites. La racionalidad maximiza desempeño esperado con información disponible y no exige acertar siempre. Autonomía no equivale a ausencia de supervisión.

PEAS obliga a comenzar por consecuencias y conectar entorno, actuadores y sensores. Las dimensiones del ambiente no son etiquetas: derivan memoria, incertidumbre, actualización y coordinación. Representar bien el problema es el puente entre una necesidad real y un algoritmo.

El cierre debe recuperar la pregunta inicial y solicitar una reformulación: un sistema es inteligente, en sentido operacional, cuando selecciona acciones adecuadas para una tarea a partir de información disponible, pero su evaluación completa también exige revisar objetivos, restricciones, efectos y responsabilidad.

## Diapositiva 38. Lecturas y continuidad

**Correspondencia con el libro:** capítulo 1, §§1.1.2, 1.2 y 1.3; capítulo 6, §§6.1 y 6.2.

### Orientación final

Las secciones del capítulo 1 ofrecen definición, enfoques e historia. El capítulo 6 convierte esos conceptos en procedimientos de especificación. La lectura prioritaria debe ser §1.1.2, §1.2, §6.1 y §6.2. El ejemplo §6.2.8 permite revisar el caso de movilidad.

Como continuidad, cada estudiante debe corregir una parte de la ficha producida en clase. La revisión debe responder cuatro preguntas del libro:

1. ¿Qué sabe realmente el agente?
2. ¿Qué no sabe?
3. ¿Qué puede recomendar sin intervención?
4. ¿Quién asume el costo de sus errores?

La próxima etapa no comienza eligiendo un algoritmo. Comienza refinando la representación, los datos disponibles, la autoridad y los criterios con los que se evaluarán las consecuencias.

## Referencias

- `../../../Libro/Capitulo_01_Ciencia_de_Datos_e_IA.md`
- `../../../Libro/Capitulo_06_Agentes_inteligentes_y_representacion_de_problemas.md`
- `Clase_01_Fundamentos_de_IA_agentes_y_racionalidad.pdf`
