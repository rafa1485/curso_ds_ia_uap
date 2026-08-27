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

# Guía docente: Exploración, diagnóstico y visualización de datos

**Curso:** Data Science

**Semana y clase:** semana 3, clase 3

**Presentación asociada:** *Exploración, diagnóstico y visualización de datos: de una tabla analítica a hallazgos defendibles* (40 diapositivas)

**Modalidad:** clase teórica y conceptual de 150 minutos. La práctica se realizará después en un notebook que aún no ha sido creado.

**Fuente principal:** capítulo 4 del libro *Ciencia de Datos e Inteligencia Artificial*, con continuidad de los capítulos 2 y 3

### Propósito y forma de uso

Esta guía sincroniza cada diapositiva con una pregunta docente, una afirmación permitida y una comprobación conceptual. La sesión parte de la tabla analítica defendible construida conceptualmente en la semana 2 y enseña a describir variables, estudiar relaciones, elegir codificaciones visuales y redactar hallazgos sin exceder población, cobertura ni diseño.

El caso transversal conserva una fila **zona de origen-hora local** y tres familias de información: conteos de pickups de NYC TLC, atributos de zona y observaciones horarias de una estación NOAA. Los **pickups TLC son viajes realizados y reportados con origen registrado, no demanda total**. NOAA aporta observaciones de **una estación meteorológica, no clima zonal**. Repetir estas fronteras cada vez que aparezcan mapas, perfiles temporales o asociaciones con clima.

La palabra **diagnóstico** se usa en sentido descriptivo: revisión sistemática de distribuciones, cobertura, relaciones y casos que requieren explicación. **Diagnóstico no significa causalidad**. La exploración genera hipótesis y candidatos para análisis posterior; no confirma hipótesis descubiertas en los mismos datos. No se presentarán cifras, patrones o resultados empíricos porque el notebook práctico todavía no existe.

### Recorrido por bloques

| Bloque | Diapositivas | Resultado esperado |
|---|---:|---|
| Apertura, continuidad y contrato | 1-5 | Ubicar la sesión, sus límites y la pregunta que organizará la exploración |
| Fundamentos del EDA | 6-10 | Delimitar exploración, ciclo, población, estimando, denominador y semántica |
| Descripción univariada | 11-19 | Construir un perfil coherente de frecuencia, posición, dispersión, forma y extremos |
| Codificación y selección visual | 20-25 | Elegir una representación según pregunta, variable, denominador y tarea perceptiva |
| Relaciones entre variables | 26-34 | Estudiar asociaciones por etapas y reconocer condicionamiento, confusión y heterogeneidad |
| Tiempo, espacio y multivariado | 35-37 | Explorar dependencias estructurales sin confundir agregación con explicación |
| Hallazgos, continuidad y cierre | 38-40 | Redactar evidencia limitada, fijar el contrato de práctica y recuperar la síntesis |

> **Tesis de la clase:** explorar es someter una tabla analítica a preguntas coordinadas sobre representación, distribución, relación y cobertura para producir hallazgos trazables. Un patrón visible o un estadístico genera una hipótesis; no demuestra por sí solo representatividad, causalidad ni validez fuera de los datos observados.

### Agenda temporal sugerida: 150 minutos

| Tiempo | Actividad | Diapositivas |
|---:|---|---:|
| 0-12 min | Apertura, resultados, continuidad y alcance | 1-5 |
| 12-32 min | Qué es EDA y contrato poblacional/semántico | 6-10 |
| 32-62 min | Distribuciones, centro, posición y dispersión | 11-16 |
| 62-75 min | Forma, atípicos y perfil coherente | 17-19 |
| 75-83 min | Pausa breve | -- |
| 83-105 min | Principios visuales y selección de gráficos | 20-25 |
| 105-130 min | Relaciones, correlación, causalidad y estratos | 26-34 |
| 130-141 min | Exploración temporal, espacial y multivariada | 35-37 |
| 141-150 min | Hallazgos, contrato futuro y síntesis | 38-40 |

Los tiempos son orientativos. Si la discusión conceptual se extiende, priorizar denominadores, semántica, forma antes que coeficiente y límites causales. No convertir esta sesión en demostración de software ni improvisar resultados con datos no auditados.

### Preparación previa del docente

1. Leer el capítulo 4 completo y revisar en los capítulos 2 y 3 las secciones sobre formulación, población, unidad, disponibilidad, calidad, integración, agregación y reproducibilidad.
2. Revisar la presentación junto con esta guía y comprobar que existan exactamente cuarenta diapositivas, con títulos, fórmulas, tablas y diagramas alineados con las correspondencias aquí descritas.
3. Preparar una versión limpia de la pregunta de apertura y dos frases deliberadamente problemáticas: “los pickups miden demanda” y “la lluvia causa más viajes”; no proporcionar respuestas antes de recoger argumentos.
4. Mantener visibles las definiciones del caso: unidad zona-hora, periodo todavía por fijar en la práctica, pickups como viajes realizados/reportados, NOAA como una estación y clima no zonal.
5. Ensayar la lectura visual de histogramas, cajas, tablas, dispersión, serie y mapa usando esquemas conceptuales sin valores. El objetivo es enseñar qué mirar y qué comprobar, no anticipar una forma empírica.
6. Preparar tarjetas o preguntas de respuesta breve para las comprobaciones de las diapositivas 9, 12, 18, 25, 28, 32, 33 y 38.
7. No anunciar nombre, estructura, biblioteca ni resultados del notebook futuro. Registrar las decisiones conceptuales que la práctica deberá materializar cuando se diseñe.
8. Reservar los últimos nueve minutos para evaluación y cierre; la comprensión de límites forma parte del resultado y no debe quedar como advertencia opcional.

### Evaluación conceptual de la sesión

| Criterio | Evidencia observable | Peso sugerido |
|---|---|---:|
| Contrato descriptivo | Declara población, población registrada, unidad, variable, periodo, estimando, peso y denominador | 25 % |
| Selección estadística | Justifica medidas clásicas y robustas según escala, forma y pregunta | 20 % |
| Selección visual | Elige gráfico y codificación compatibles con la comparación requerida | 20 % |
| Interpretación de relaciones | Distingue condicionamiento, asociación, confusión, heterogeneidad y causalidad | 20 % |
| Hallazgo defendible | Redacta evidencia, alcance, límite, alternativa y siguiente comprobación sin inventar resultados | 15 % |

La evaluación puede realizarse mediante respuestas orales, una ficha de salida o discusión por parejas. Una respuesta que trate pickups como demanda total, NOAA como clima de cada zona, un atípico como error automático o una correlación como efecto causal requiere corrección aunque use terminología estadística adecuada.

### Preguntas de salida sugeridas

1. ¿Qué cambia entre describir todos los viajes registrados y estimar una cantidad para la movilidad total?
2. ¿Por qué mediana e IQR no vuelven representativa una muestra sesgada?
3. ¿Qué pregunta responde una proporción condicionada por fila y qué denominador usa?
4. ¿Cómo puede existir una relación fuerte con correlación lineal cercana a cero?
5. ¿Qué elementos mínimos convierten un patrón exploratorio en un hallazgo defendible, sin volverlo confirmatorio?

## Diapositiva 1. Portada

**Correspondencia con el libro.** Capítulo 4, propósito y objetivos; continuidad con capítulos 2 y 3.

**Propósito.** Presentar la exploración como paso entre tabla analítica y afirmación limitada, no como galería de gráficos.

**Guion sugerido.** Abrir con: “La semana pasada preguntamos qué representa una fila y cómo fue construida; hoy preguntaremos qué distribuciones y relaciones permite describir y qué lenguaje soporta”. Leer el subtítulo completo. Explicar que *diagnóstico* nombra una indagación descriptiva de patrones y problemas, no identificación de causas.

**Conceptos y términos.** *Exploración de datos*, *diagnóstico descriptivo*, *visualización*, *tabla analítica*, *hallazgo defendible*.

**Descripción visual relevante.** La portada debe unir visualmente una tabla, varias vistas estadísticas y una tarjeta de hallazgo. Las flechas indican refinamiento de evidencia, no una transformación automática ni causal. La palabra “defendibles” debe recibir el énfasis final.

**Ejemplo de movilidad.** Una tabla zona-hora puede sostener perfiles de pickups reportados y comparaciones entre registros; todavía no demuestra demanda total ni explica sus causas.

**Error frecuente o límite.** Suponer que explorar equivale a encontrar una historia atractiva o que “diagnóstico” autoriza lenguaje causal.

**Comprobación.** “¿Qué producto final promete el título?”. Hallazgos argumentados y limitados, no una decisión automática ni una explicación causal.

**Conclusión que debe quedar.** La sesión enseñará a convertir una tabla auditada en preguntas y hallazgos que puedan revisarse.

**Transición sugerida.** “Definamos qué capacidades concretas deberán poder demostrar al terminar”.

## Diapositiva 2. Propósito y resultados

**Correspondencia con el libro.** Capítulo 4, objetivos de aprendizaje y síntesis.

**Propósito.** Fijar cinco resultados: delimitar el análisis, describir distribuciones, elegir gráficos, estudiar relaciones y comunicar límites.

**Guion sugerido.** Recorrer los resultados como cadena de control. Primero se declara qué se describe; después se combinan medidas y forma; luego se codifica una comparación; a continuación se estudian relaciones y estratos; finalmente se redacta un hallazgo con incertidumbre y próximo paso. Aclarar que no se programará en esta clase.

**Conceptos y términos.** *Posición*, *dispersión*, *forma*, *asociación*, *codificación visual*, *trazabilidad*.

**Ejemplo de movilidad.** El estudiante deberá poder proponer cómo explorar pickups zona-hora y clima de estación sin afirmar resultados ni confundir observación con demanda.

**Error frecuente o límite.** Convertir los resultados en una lista de nombres de gráficos o coeficientes.

**Comprobación.** Pedir completar: “Antes de calcular correlación debo...”. Respuestas esperadas: comprender cada variable, revisar calidad, graficar forma y declarar unidad.

**Conclusión que debe quedar.** La correspondencia entre pregunta, medida, gráfico e interpretación es el criterio de logro.

**Transición sugerida.** “Esa correspondencia prolonga dos semanas de decisiones previas; reconstruyámoslas”.

## Diapositiva 3. Continuidad semanas 1-3

**Correspondencia con el libro.** Capítulo 2, formulación y ciclo; capítulo 3, preparación e integración; capítulo 4, exploración.

**Propósito.** Mostrar que EDA hereda el problema formulado y el contrato de la tabla.

**Guion sugerido.** Semana 1: necesidad, pregunta, unidad, población, horizonte y decisión. Semana 2: fuente, procedencia, calidad, clave, integración, agregación y tabla analítica. Semana 3: distribución, relación, visualización y hallazgo. Leer también hacia atrás: un hallazgo incoherente obliga a revisar representación o formulación.

**Conceptos y términos.** *Continuidad metodológica*, *contrato analítico*, *retorno*, *coherencia*.

**Descripción detallada del diagrama.** Tres bloques horizontales representan semanas 1, 2 y 3. Las flechas continuas avanzan desde formulación hasta hallazgo; dos flechas discontinuas regresan desde exploración a preparación y formulación. El retorno indica revisión trazable, no permiso para redefinir datos hasta obtener el patrón deseado. Leer primero hacia adelante y luego preguntar qué bloque se revisa si aparece una categoría imposible.

**Ejemplo de movilidad.** La exploración no puede cambiar silenciosamente una fila zona-hora a viaje ni olvidar que el conteo procede de pickups reportados.

**Error frecuente o límite.** Tratar EDA como una fase independiente que corrige por sí sola defectos de cobertura.

**Comprobación.** “Si un histograma revela dos unidades mezcladas, ¿se arregla solo cambiando bins?”. No; se vuelve al diccionario y a la preparación.

**Conclusión que debe quedar.** Explorar también audita las decisiones que produjeron la tabla.

**Transición sugerida.** “La continuidad no significa que hoy cubriremos toda la inferencia estadística; fijemos el alcance”.

## Diapositiva 4. Alcance del cronograma

**Correspondencia con el libro.** Capítulo 4, secuencia del capítulo; capítulos posteriores para inferencia y modelado.

**Propósito.** Delimitar la clase teórica de 150 minutos y separar exploración, práctica e inferencia confirmatoria.

**Guion sugerido.** Mostrar el recorrido por bloques y la pausa. Explicar que hoy se estudian decisiones conceptuales; el notebook práctico se diseñará y realizará después y todavía no existe. No se cubrirán pruebas confirmatorias, identificación causal, predicción ni despliegue.

**Conceptos y términos.** *Alcance*, *sesión conceptual*, *práctica posterior*, *análisis confirmatorio*.

**Descripción visual relevante.** La tabla organiza los seis bloques y sus rangos de diapositivas; el bloque inferior separa explícitamente los temas fuera de alcance y la práctica futura.

**Ejemplo de movilidad.** Se podrá justificar qué vistas necesita un futuro notebook, pero no afirmar qué patrón mostrará TLC o NOAA.

**Error frecuente o límite.** Improvisar una ejecución para “demostrar” conceptos y terminar presentando selecciones no auditadas como evidencia.

**Comprobación.** “¿Qué se evaluará hoy: sintaxis o razonamiento?”. Razonamiento sobre estimandos, medidas, gráficos, relaciones y límites.

**Conclusión que debe quedar.** La sesión construye el contrato intelectual que deberá respetar la práctica posterior.

**Transición sugerida.** “Abramos ese contrato con una pregunta que obliga a decidir qué significa conocer una tabla”.

## Diapositiva 5. Pregunta de apertura

**Correspondencia con el libro.** Capítulo 4, propósito; §§4.1, 4.2 y 4.4.1.

**Propósito.** Hacer visibles las decisiones ocultas en “¿qué nos dicen los datos?”.

**Guion sugerido.** Plantear: “Tenemos una tabla zona-hora con pickups reportados, zona y clima de una estación: ¿qué mirarían primero y qué podrían afirmar?”. Clasificar respuestas en representación, distribución, relación y límite. No corregir de inmediato; pedir denominador, unidad y evidencia necesaria.

**Conceptos y términos.** *Pregunta exploratoria*, *afirmación permitida*, *evidencia necesaria*, *explicación alternativa*.

**Descripción visual relevante.** La tabla alinea cuatro dimensiones con su pregunta inicial: representación, distribución, relación y límite. El bloque del caso y la advertencia inferior mantienen visible el alcance de TLC y NOAA.

**Ejemplo de movilidad.** Son preguntas válidas cómo varían los viajes realizados/reportados entre horas o zonas y si coinciden con observaciones de la estación. No es válida sin más diseño “cuánta demanda total existe” ni “qué efecto causa la lluvia”.

**Error frecuente o límite.** Elegir correlación antes de definir unidad o hablar de demanda porque la columna se llama `pickups`.

**Comprobación.** Pedir una afirmación prohibida y su reformulación descriptiva.

**Conclusión que debe quedar.** Una pregunta exploratoria útil incluye objeto, comparación, población y límite.

**Transición sugerida.** “Ahora sí podemos delimitar el método que organizará esas preguntas”.

## Diapositiva 6. Qué es y qué no es EDA

**Correspondencia con el libro.** Capítulo 4, propósito; §4.3, visualización exploratoria.

**Propósito.** Definir el **análisis exploratorio de datos (EDA, por *Exploratory Data Analysis*)** como indagación disciplinada.

**Guion sugerido.** EDA examina representación, calidad, distribuciones, relaciones y casos influyentes mediante vistas complementarias. No es buscar hasta hallar significancia, confirmar una historia elegida, reparar automáticamente datos ni sustituir inferencia. “Diagnóstico” significa localizar preguntas y posibles problemas; no identificar mecanismos causales.

**Conceptos y términos.** *EDA*, *hipótesis generada*, *sensibilidad*, *vista complementaria*, *diagnóstico descriptivo*.

**Ejemplo de movilidad.** Comparar perfiles zona-hora, revisar faltantes climáticos y observar una dispersión puede generar hipótesis sobre calendario, cobertura u oferta.

**Error frecuente o límite.** Presentar la asociación más llamativa entre muchas como si hubiera sido planteada antes de mirar.

**Comprobación.** “¿Una hipótesis encontrada durante EDA queda confirmada por el mismo gráfico?”. No; requiere evaluación posterior adecuada, idealmente con datos independientes.

**Conclusión que debe quedar.** EDA produce comprensión provisional, controles e hipótesis explícitas, no veredictos.

**Transición sugerida.** “Veamos cómo se encadenan esas operaciones sin convertirlas en una receta lineal”.

## Diapositiva 7. Ciclo exploratorio

**Correspondencia con el libro.** Capítulo 4, §§4.1, 4.2, 4.3 y estrategia de §4.2.7; capítulo 2, ciclo iterativo.

**Propósito.** Organizar la exploración como ciclo de pregunta, revisión, representación, cuantificación, contraste y registro.

**Guion sugerido.** Formular una pregunta; revisar unidad, semántica y cobertura; visualizar; resumir; segmentar o cambiar resolución; proponer explicación alternativa; registrar hallazgo provisional y próximo control. Cada retorno debe responder qué evidencia motivó el cambio.

**Conceptos y términos.** *Iteración exploratoria*, *resolución*, *contraste*, *bitácora de decisiones*, *sensibilidad*.

**Descripción detallada del diagrama.** Seis nodos forman un anillo. Las flechas continuas muestran el recorrido principal y las discontinuas permiten volver desde visualización a calidad y desde contraste a pregunta. El nodo central es la bitácora; `Registrar` permanece en el recorrido porque documentar también es una operación del ciclo.

**Ejemplo de movilidad.** Una aparente segunda moda horaria conduce a revisar bins, día de semana, aeropuertos, cobertura y definición de hora antes de nombrar un patrón.

**Error frecuente o límite.** Cambiar filtros sin registrarlos o conservar solo las vistas compatibles con una narración.

**Comprobación.** “¿Qué retorno corresponde a un pico exactamente en el máximo del sensor?”. Volver a captura, semántica y calidad antes de interpretarlo como fenómeno.

**Conclusión que debe quedar.** Iterar es contrastar interpretaciones con decisiones visibles, no explorar sin memoria.

**Transición sugerida.** “El ciclo debe comenzar distinguiendo el mundo de las unidades que efectivamente llegaron a la tabla”.

## Diapositiva 8. Población, muestra y población registrada

**Correspondencia con el libro.** Capítulo 4, §4.1.1; capítulos 2 y 3, población, cobertura y selección.

**Propósito.** Separar población objetivo, muestra y conjunto completo de registros de un sistema.

**Guion sugerido.** Definir población mediante unidad, espacio, periodo e inclusión. Una muestra es el subconjunto observado bajo un mecanismo de selección. La **población registrada** es el universo de eventos que el sistema logró materializar para el alcance declarado; puede ser toda la base de un operador sin ser toda la población sustantiva.

**Conceptos y términos.** *Población objetivo*, *muestra*, *población registrada*, *marco*, *cobertura*, *selección*.

**Descripción visual relevante.** La población registrada se superpone parcialmente con la población objetivo; la muestra observada queda dentro de la población registrada. Las áreas son conceptuales y no codifican cantidades. La figura separa cobertura externa de selección interna.

**Ejemplo de movilidad.** Todos los pickups TLC Yellow Taxi reportados en un periodo pueden formar la población registrada del análisis; no incluyen solicitudes no atendidas, otros operadores ni viajes no reportados y por ello no son demanda total.

**Error frecuente o límite.** Llamar censo de movilidad a todos los registros de una fuente administrativa.

**Comprobación.** “¿Más filas corrigen falta de operadores?”. No; aumentan precisión descriptiva dentro de la cobertura, no representatividad externa.

**Conclusión que debe quedar.** El tamaño no sustituye una definición de población ni un análisis del mecanismo de registro.

**Transición sugerida.** “Una vez delimitado sobre qué observamos, debemos precisar qué cantidad queremos resumir”.

## Diapositiva 9. Unidad, estimando, ponderación y denominador

**Correspondencia con el libro.** Capítulo 4, §4.1.1, estimando y ponderaciones; §4.1.2, denominadores.

**Propósito.** Mostrar que el resumen cambia cuando cambia qué unidad recibe peso y qué total define una proporción.

**Guion sugerido.** El **estimando** es la cantidad precisa que se desea conocer. Comparar promedio por zona, promedio por zona-hora y promedio por viaje: cada uno pondera unidades de forma distinta. Exigir la frase del libro: “Este estadístico describe ___ para ___ durante ___, dando a cada ___ un peso de ___”. Añadir el denominador de toda proporción o tasa.

**Conceptos y términos.** *Unidad de análisis*, *estimando*, *peso*, *denominador*, *exposición*, *promedio de promedios*.

**Descripción visual relevante.** La fracción conceptual señala numerador y denominador. La frase profesional obliga a completar población, periodo, unidad, peso y denominador; dos rótulos contrastan “cada zona pesa igual” y “cada viaje reportado pesa igual”.

**Ejemplo de movilidad.** Promediar pickups por zona da el mismo peso a zonas con distinta cantidad de horas observadas; una tasa por hora observada necesita cobertura temporal explícita.

**Error frecuente o límite.** Promediar promedios zonales sin reportar pesos o comparar porcentajes cuyo denominador cambia.

**Comprobación.** Pedir completar la frase profesional para “pickups medios por zona-hora”, especificando que son viajes realizados/reportados.

**Conclusión que debe quedar.** Ningún estadístico es interpretable sin unidad, estimando, peso y denominador.

**Transición sugerida.** “Incluso con el estimando claro, solo ciertas operaciones son válidas para el significado de cada variable”.

## Diapositiva 10. Tipos semánticos y preguntas válidas

**Correspondencia con el libro.** Capítulo 3, tipos físicos y semánticos; capítulo 4, §§4.1-4.3.

**Propósito.** Vincular escala semántica con preguntas, resúmenes y gráficos admisibles.

**Guion sugerido.** Distinguir nominal, ordinal, cuantitativa de intervalo, cuantitativa de razón, tiempo y espacio. Un ID numérico sigue siendo nominal; Celsius no posee cero absoluto; hora y zona incorporan orden y dependencia. Para cada tipo preguntar qué significa igualdad, orden, diferencia y razón.

**Conceptos y términos.** *Nominal*, *ordinal*, *intervalo*, *razón*, *identificador*, *variable temporal*, *variable espacial*.

**Descripción visual relevante.** Una matriz cruza tipo con operaciones válidas: contar, ordenar, restar, dividir y representar. Las marcas indican posibilidades semánticas generales, no autorizan una operación sin contexto.

**Ejemplo de movilidad.** `PULocationID` se cuenta o agrupa, no se promedia; pickups es un conteo; temperatura de estación admite diferencias, pero “el doble de grados Celsius” no es una razón física válida.

**Error frecuente o límite.** Dejar que el tipo físico del software determine el análisis.

**Comprobación.** “¿Qué pregunta responde la media de IDs de zona?”. Ninguna pregunta geográfica defendible.

**Conclusión que debe quedar.** La semántica gobierna qué comparación y qué gráfico tienen sentido.

**Transición sugerida.** “Comencemos la descripción con el objeto que conserva valores y frecuencias”.

## Diapositiva 11. Distribuciones de frecuencia

**Correspondencia con el libro.** Capítulo 4, §4.1.2.

**Propósito.** Presentar la distribución como base de todo resumen univariado.

**Guion sugerido.** Frecuencia absoluta cuenta observaciones; relativa divide por un denominador; acumulada requiere orden. Para variables numéricas, intervalos aproximan la distribución y su elección modifica la percepción. Una tabla debe informar cantidad válida y excluida.

**Conceptos y términos.** *Frecuencia absoluta*, *relativa*, *porcentual*, *acumulada*, *intervalo*, *resolución*.

**Descripción visual relevante.** Las fórmulas y la tabla distinguen frecuencia absoluta, relativa, porcentual y acumulada. La línea inferior exige reportar válidos, faltantes, exclusiones y denominador.

**Ejemplo de movilidad.** Puede contarse cuántas zonas-hora pertenecen a cada franja o distribuir el número de pickups reportados por zona-hora, declarando horas sin fila y horas con cero.

**Error frecuente o límite.** Acumular categorías nominales o comparar conteos de grupos con exposiciones distintas.

**Comprobación.** “¿Cuándo deben sumar 100 % las categorías?”. Cuando son mutuamente excluyentes, exhaustivas respecto del denominador declarado y cada unidad aporta una vez.

**Conclusión que debe quedar.** Una distribución hace visibles valores, frecuencia y exclusiones antes de condensarlos.

**Transición sugerida.** “Para construirla correctamente debemos separar tres situaciones que suelen verse iguales en una tabla”.

## Diapositiva 12. Cero, faltante y ausencia de fila

**Correspondencia con el libro.** Capítulo 4, §4.1.2, ceros y faltantes; capítulo 3, mecanismos de ausencia y estructura.

**Propósito.** Distinguir valor cero, celda ausente y unidad potencial no materializada.

**Guion sugerido.** Un cero es una observación cuyo valor es cero bajo una regla. Un faltante indica que existe la fila pero no el valor. Una ausencia de fila indica que la unidad esperada no fue materializada. Para distinguir “cero pickups” de “sin observación”, se necesita un marco completo de zona-hora y procedencia.

**Conceptos y términos.** *Cero estructural o observado*, *faltante*, *ausencia de fila*, *marco esperado*, *cobertura*.

**Descripción detallada del diagrama.** Tres tarjetas muestran: fila con valor 0, fila con celda vacía y combinación zona-hora inexistente. Una flecha desde el marco esperado permite detectar la tercera. No se conectan como etapas ni se permite convertir automáticamente una en otra.

**Ejemplo de movilidad.** Una zona-hora sin pickups reportados podría ser cero real dentro de la fuente o una hora no materializada; NOAA ausente en una hora no equivale a precipitación cero.

**Error frecuente o límite.** Rellenar toda ausencia con cero o excluir faltantes sin actualizar el denominador.

**Comprobación.** Presentar las tres tarjetas y pedir qué metadato o tabla permite diferenciarlas.

**Conclusión que debe quedar.** El patrón de ceros y ausencias forma parte del fenómeno de observación y debe permanecer visible.

**Transición sugerida.** “Con una distribución válida podemos elegir cómo resumir su centro sin llamarlo simplemente promedio”.

## Diapositiva 13. Media, mediana y moda

**Correspondencia con el libro.** Capítulo 4, §4.1.3.

**Propósito.** Elegir una medida de centro según escala, forma y uso.

**Guion sugerido.** La media es balance aritmético y usa magnitudes; la mediana divide posiciones y resiste extremos; la moda identifica el valor o categoría más frecuente. Ninguna es universalmente “la correcta”. Comparar experiencia típica, planificación de volumen y categoría más frecuente.

**Conceptos y términos.** *Media*, *mediana*, *moda*, *centro*, *robustez*, *media recortada*.

**Descripción visual relevante.** La fórmula de la media y la tabla comparan interpretación y sensibilidad de media, mediana y moda. El bloque inferior recuerda que ningún centro reemplaza colas o cobertura.

**Ejemplo de movilidad.** Para pickups por zona-hora, la media puede apoyar volumen agregado, la mediana una zona-hora típica registrada y la moda un conteo frecuente; siempre dentro de la población registrada.

**Error frecuente o límite.** Decir “promedio” sin especificar medida o concluir que la mediana describe las colas.

**Comprobación.** “¿Por qué dos grupos con igual mediana pueden ser operativamente distintos?”. Porque dispersión y colas pueden diferir.

**Conclusión que debe quedar.** El centro responde una pregunta parcial y debe acompañarse con forma y dispersión.

**Transición sugerida.** “Para describir posiciones y colas necesitamos más de un punto central”.

## Diapositiva 14. Cuantiles y percentiles

**Correspondencia con el libro.** Capítulo 4, §4.1.4.

**Propósito.** Interpretar cuantiles como posiciones acumuladas y comparar centro y colas.

**Guion sugerido.** El cuantil de orden $p$ deja aproximadamente una proporción $p$ de observaciones por debajo o igual. Los percentiles expresan cien partes; los cuartiles corresponden a 25, 50 y 75 %. Explicar que las convenciones muestrales pueden interpolar de forma distinta.

**Conceptos y términos.** *Cuantil*, *percentil*, *cuartil*, *posición acumulada*, *interpolación*.

**Descripción visual relevante.** Una distribución ordenada muestra $Q_1$, mediana, $Q_3$ y un percentil alto. Las áreas indican proporciones aproximadas, no probabilidades del próximo caso.

**Ejemplo de movilidad.** Un percentil alto de pickups zona-hora describiría la cola de conteos reportados observados; no significa probabilidad de demanda futura ni incluye solicitudes no registradas.

**Error frecuente o límite.** Confundir percentil 90 con 90 % de una escala o con probabilidad individual futura.

**Comprobación.** Pedir interpretar un P90 sin asignar valor: aproximadamente 90 % de las unidades observadas no lo supera bajo población y periodo declarados.

**Conclusión que debe quedar.** Los cuantiles describen posiciones sin asumir simetría, pero dependen de referencia y método.

**Transición sugerida.** “La posición no indica cuán extendidos están los valores; añadamos dispersión clásica”.

## Diapositiva 15. Rango, varianza y desviación estándar

**Correspondencia con el libro.** Capítulo 4, §4.1.5.

**Propósito.** Distinguir extensión total, desviación cuadrática media y dispersión en unidades originales.

**Guion sugerido.** El rango depende de mínimo y máximo. La varianza promedia desviaciones cuadradas respecto de la media con denominador poblacional o muestral según estimando. La desviación estándar vuelve a la unidad original. La regla 68-95 exige una forma aproximadamente normal y no debe aplicarse mecánicamente.

**Conceptos y términos.** *Rango*, *varianza poblacional*, *varianza muestral*, *desviación estándar*, *unidad*.

**Descripción visual relevante.** Las fórmulas distinguen rango, varianza poblacional, varianza muestral y desviación estándar. La lista inferior relaciona unidades y denominadores; la advertencia separa la regla 68-95 de una propiedad universal.

**Ejemplo de movilidad.** La desviación de pickups zona-hora queda en pickups; su varianza, en pickups al cuadrado. Ninguna corrige selección de viajes reportados.

**Error frecuente o límite.** Comparar varianzas en escalas distintas o interpretar una desviación estándar como intervalo que siempre contiene 68 %.

**Comprobación.** “¿Por qué $n-1$ no es una regla universal?”. Depende de estimar varianza poblacional desde una muestra bajo supuestos; si se describe toda la población registrada, cambia el estimando.

**Conclusión que debe quedar.** La dispersión clásica es informativa y sensible a extremos, unidades y definición poblacional.

**Transición sugerida.** “Para formas asimétricas conviene contrastarla con medidas robustas”.

## Diapositiva 16. IQR, MAD y robustez

**Correspondencia con el libro.** Capítulo 4, §4.1.6 y §4.1.3, estimadores robustos.

**Propósito.** Presentar dispersión robusta sin confundir resistencia a extremos con inmunidad a sesgo.

**Guion sugerido.** El **rango intercuartílico (IQR)** es $Q_3-Q_1$ y resume el 50 % central. La **desviación absoluta mediana (MAD)** toma la mediana de distancias absolutas a la mediana. Son menos sensibles a extremos, pero pueden ocultar falta sistemática de valores altos.

**Conceptos y términos.** *IQR*, *MAD*, *robustez*, *50 % central*, *contaminación*, *sesgo de observación*.

**Descripción visual relevante.** Las fórmulas definen IQR y MAD; la tabla resume qué describe cada medida y la advertencia inferior separa robustez estadística de representatividad.

**Ejemplo de movilidad.** Mediana e IQR de pickups por zona-hora pueden resistir horas excepcionalmente altas, pero no recuperan viajes de otros operadores ni demanda no atendida.

**Error frecuente o límite.** Afirmar que una medida robusta vuelve confiables datos con mala cobertura.

**Comprobación.** “Si faltan sistemáticamente las horas de mayor actividad, ¿el IQR lo corrige?”. No; puede incluso parecer artificialmente pequeño.

**Conclusión que debe quedar.** Robustez limita influencia de ciertos valores, no repara el proceso de observación.

**Transición sugerida.** “Centro y dispersión todavía pueden ocultar colas, mezclas y acumulaciones”.

## Diapositiva 17. Asimetría, colas y multimodalidad

**Correspondencia con el libro.** Capítulo 4, §4.1.7 y §4.3.2.

**Propósito.** Leer forma más allá de coeficientes únicos.

**Guion sugerido.** Asimetría describe orientación de colas; curtosis se relaciona con colas y extremos, no solo altura del pico; multimodalidad sugiere mezcla o regímenes. Revisar redondeo, censura, saturación y grupos antes de atribuir una forma al fenómeno.

**Conceptos y términos.** *Asimetría positiva/negativa*, *cola*, *curtosis*, *modo*, *multimodalidad*, *censura*.

**Descripción visual relevante.** Cuatro curvas conceptuales muestran simetría, cola derecha, cola izquierda y dos modos. Son arquetipos didácticos sin resultados del caso. Marcadores advierten que coeficientes parecidos pueden acompañar formas distintas.

**Ejemplo de movilidad.** Dos modos en pickups zona-hora podrían corresponder a franjas o zonas mezcladas, resolución, calendario o captura; solo generan preguntas.

**Error frecuente o límite.** Etiquetar una segunda moda como “hora pico causada por clima” sin estratificación ni diseño.

**Comprobación.** Pedir tres explicaciones alternativas para una forma bimodal: mezcla de grupos, ciclo temporal, redondeo o cambio de captura.

**Conclusión que debe quedar.** La forma se investiga con gráficos, cuantiles, calidad y contexto; no se reduce a un coeficiente.

**Transición sugerida.** “La cola nos lleva a observaciones señaladas que deben investigarse sin condenarlas”.

## Diapositiva 18. Atípico no equivale a error

**Correspondencia con el libro.** Capítulo 4, §4.1.6, regla de bigotes; ejemplo §4.1.8.

**Propósito.** Separar señal estadística, incompatibilidad de datos y evento sustantivo raro.

**Guion sugerido.** La regla de Tukey marca observaciones fuera de $Q_1-1.5IQR$ o $Q_3+1.5IQR$. Es una convención visual, no una prueba de error. Clasificar casos: plausible y relevante; compatible pero influyente; problema de unidad o captura; desconocido que requiere verificación.

**Conceptos y términos.** *Atípico*, *caso influyente*, *plausibilidad*, *validez*, *regla de Tukey*, *investigación*.

**Descripción visual relevante.** La regla de Tukey encabeza una tabla de cuatro situaciones y acciones responsables. Ninguna fila conduce automáticamente a eliminar; la frase inferior exige investigar contexto y agregación.

**Ejemplo de movilidad.** Una zona-hora con muchos pickups reportados puede reflejar aeropuerto, evento, error de agregación o combinación de periodos; debe contrastarse con procedencia y contexto.

**Error frecuente o límite.** Borrar extremos para “normalizar” o inferir fraude, evento o falla desde distancia estadística.

**Comprobación.** “¿Qué evidencia mínima pediría antes de excluir?”. Regla de validez, unidad, registros vecinos, fuente y consecuencia sobre el análisis.

**Conclusión que debe quedar.** Un atípico es una invitación a investigar; su tratamiento requiere evidencia trazable.

**Transición sugerida.** “Integramos ahora estas piezas en un perfil que no contradiga su propia unidad ni cobertura”.

## Diapositiva 19. Perfil estadístico coherente

**Correspondencia con el libro.** Capítulo 4, §4.1.8 y síntesis de §4.1.

**Propósito.** Definir el producto mínimo de exploración univariada.

**Guion sugerido.** El perfil reúne contrato, cobertura, frecuencias, centro, cuantiles, dispersión clásica y robusta, forma, extremos y sensibilidad a decisiones. Cada medida debe usar la misma población y regla de inclusión o declarar la diferencia. Cerrar con una oración permitida y otra no permitida.

**Conceptos y términos.** *Perfil estadístico*, *coherencia interna*, *sensibilidad*, *regla de inclusión*, *triangulación*.

**Descripción visual relevante.** Una tabla de ocho componentes empareja cada elemento del perfil con su control mínimo. El bloque de coherencia exige reglas de inclusión comunes y la frase inferior destaca que cobertura y unidad gobiernan el conjunto.

**Ejemplo de movilidad.** El futuro perfil podría incluir cobertura zona-hora, distribución de pickups reportados y resúmenes por franja, sin anticipar cifras ni forma.

**Error frecuente o límite.** Combinar una media calculada tras excluir ceros con cuantiles que los incluyen sin declararlo.

**Comprobación.** Entregar dos mini perfiles y pedir identificar cuál cambia denominador silenciosamente.

**Conclusión que debe quedar.** Un perfil defendible combina medidas complementarias bajo un contrato común y hace visibles excepciones.

**Transición sugerida.** “Para percibir ese perfil debemos codificar cantidades mediante canales visuales”.

## Diapositiva 20. Visualización como codificación

**Correspondencia con el libro.** Capítulo 4, §4.3 y §4.4.2.

**Propósito.** Tratar el gráfico como función entre datos, marcas, canales y tarea de lectura.

**Guion sugerido.** Toda visualización elige marcas como puntos, líneas o áreas y canales como posición, longitud, color o forma. También elige agregación, escala, orden y exclusiones. Preguntar qué comparación debe hacer el lector antes de elegir tipo de gráfico.

**Conceptos y términos.** *Marca*, *canal visual*, *escala*, *agregación*, *tarea perceptiva*, *codificación*.

**Descripción detallada del diagrama.** Una cadena “datos definidos → transformación → marcas y canales → comparación → interpretación” se lee en ambos sentidos. Las flechas expresan decisiones auditables, no neutralidad. Una alerta inferior indica que cambiar escala o denominador puede cambiar el patrón visible.

**Ejemplo de movilidad.** Pickups por zona pueden codificarse con longitud en barras o color en mapa; cada opción facilita una comparación distinta y sigue representando viajes reportados.

**Error frecuente o límite.** Elegir un gráfico por estética o por la cantidad de variables que permite colocar.

**Comprobación.** “¿Qué pregunta debe preceder a ‘usar un mapa’?”. Si interesa localización espacial y si existe una medida y denominador comparables por área.

**Conclusión que debe quedar.** Diseñar un gráfico es decidir qué será fácil comparar y qué contexto debe conservarse.

**Transición sugerida.** “No todos los canales permiten comparar con la misma precisión”.

## Diapositiva 21. Posición, longitud, área y color

**Correspondencia con el libro.** Capítulo 4, §4.3.1 y §4.3.8.

**Propósito.** Establecer una jerarquía perceptiva y los usos apropiados del color.

**Guion sugerido.** Posición en escala común suele permitir comparación más precisa; sigue longitud; área y color son menos exactos. El color secuencial representa magnitud, divergente distancia a un centro y cualitativo categorías. Área debe escalarse proporcionalmente al dato, no por radio.

**Conceptos y términos.** *Posición común*, *longitud*, *área*, *intensidad*, *paleta secuencial/divergente/cualitativa*.

**Descripción visual relevante.** La tabla ordena posición, longitud, área y color por precisión comparativa y uso. Las viñetas inferiores fijan reglas para paletas, faltantes y escalamiento de áreas.

**Ejemplo de movilidad.** Para ordenar zonas por pickups reportados, barras o puntos alineados facilitan precisión; el mapa reserva color para patrón espacial, no ranking exacto.

**Error frecuente o límite.** Usar arcoíris, color como único canal o círculos cuyo radio representa el valor.

**Comprobación.** Pedir el canal preferible para comparar diferencias pequeñas entre categorías: posición sobre escala común.

**Conclusión que debe quedar.** La codificación debe ajustarse a la tarea y no exagerar diferencias.

**Transición sugerida.** “Con esa jerarquía podemos seleccionar una familia gráfica desde la pregunta”.

## Diapositiva 22. Matriz de selección de gráficos

**Correspondencia con el libro.** Capítulo 4, §4.4.2 y figura de selección de §4.3.

**Propósito.** Elegir vistas según objetivo, variables, estructura y control de lectura.

**Guion sugerido.** Recorrer filas: comparar magnitudes, mostrar distribución, relacionar variables, evolucionar en tiempo, mostrar composición y representar espacio. Para cada opción leer la pregunta de control. Recordar que una tabla supera al gráfico cuando se necesitan valores exactos.

**Conceptos y términos.** *Objetivo visual*, *comparación*, *distribución*, *relación*, *evolución*, *composición*, *espacio*.

**Lectura detallada de la tabla.** Las columnas son objetivo, opciones y control. Leer cada fila horizontalmente; no elegir desde la columna de nombres. Una misma variable puede requerir vistas distintas según tarea y varias vistas pueden ser complementarias, no redundantes.

**Ejemplo de movilidad.** Distribución de pickups: histograma; comparación por zona: puntos o barras; evolución: línea; espacio: mapa con medida pertinente; relación clima-pickups: dispersión a unidad temporal coherente.

**Error frecuente o límite.** Creer que “variable categórica igual barras” resuelve denominador, orden y propósito.

**Comprobación.** Proponer tres preguntas sobre la misma columna `pickups` y seleccionar tres vistas justificadas.

**Conclusión que debe quedar.** El gráfico lo determina la comparación requerida, no el nombre de una variable.

**Transición sugerida.** “Apliquemos la matriz a la vista más sensible a decisiones de resolución”.

## Diapositiva 23. Histogramas, intervalos y densidad

**Correspondencia con el libro.** Capítulo 4, §§4.1.2 y 4.3.2.

**Propósito.** Enseñar cómo bins y suavizado alteran la forma percibida.

**Guion sugerido.** Un histograma agrupa observaciones en intervalos; probar varias anchuras separa estructura estable de artefacto. Con intervalos desiguales, el área y no la altura debe representar proporción mediante densidad. Una densidad kernel es una estimación suavizada y depende de ancho de banda.

**Conceptos y términos.** *Bin*, *anchura*, *límite*, *densidad*, *ancho de banda*, *resolución*.

**Descripción detallada del diagrama.** Tres histogramas conceptuales del mismo conjunto usan bins ancho, intermedio y estrecho; una curva suavizada aparece separada y rotulada como estimación. No se invita a escoger la vista “más interesante”, sino la estructura estable entre resoluciones.

**Ejemplo de movilidad.** La distribución de pickups zona-hora puede verse distinta según bins; los límites deben ser comunes al comparar franjas o zonas.

**Error frecuente o límite.** Interpretar picos del suavizado como observaciones o permitir densidad en valores imposibles sin advertencia.

**Comprobación.** “¿Qué haría antes de afirmar multimodalidad?”. Variar bins/ancho de banda, revisar resolución, grupos, unidades y captura.

**Conclusión que debe quedar.** La forma visible es una interacción entre datos y decisiones de representación.

**Transición sugerida.** “Otra familia resume cuantiles y, con cautela, puede recuperar parte de la forma”.

## Diapositiva 24. Caja y violín

**Correspondencia con el libro.** Capítulo 4, §§4.1.6 y 4.3.3.

**Propósito.** Comparar grupos distinguiendo resumen robusto y forma suavizada.

**Guion sugerido.** La caja muestra cuartiles, mediana, IQR, bigotes convencionales y puntos externos. El violín añade densidad estimada, pero depende del ancho de banda. Combinar tamaño, puntos y cuantiles cuando las muestras son pequeñas.

**Conceptos y términos.** *Caja*, *bigote*, *violín*, *densidad suavizada*, *tamaño de grupo*.

**Descripción visual relevante.** Caja y violín aparecen para una misma distribución conceptual. La tabla explica qué aporta cada vista y el bloque inferior fija condiciones para comparar grupos. No hay datos empíricos.

**Ejemplo de movilidad.** Comparar pickups reportados por franja requeriría mismo periodo, reglas y unidad, además del número de zona-horas por grupo.

**Error frecuente o límite.** Llamar errores a puntos fuera de bigotes o tratar bigotes superpuestos como prueba estadística.

**Comprobación.** “¿Qué puede mostrar un violín que una caja oculta?”. Modos y forma aproximada; a cambio introduce sensibilidad al suavizado.

**Conclusión que debe quedar.** Caja y violín orientan comparaciones descriptivas; no prueban diferencias ni calidad.

**Transición sugerida.** “Para categorías, la primera decisión no es el color de la barra, sino la cantidad que codifica”.

## Diapositiva 25. Barras, conteos, proporciones y tasas

**Correspondencia con el libro.** Capítulo 4, §§4.1.2 y 4.3.4.

**Propósito.** Separar volumen, composición y ocurrencia respecto de exposición.

**Guion sugerido.** Conteos responden cuántos; proporciones, qué parte de un total; tasas, cuántos por unidad de exposición. Las barras comparan longitud y suelen comenzar en cero. Mostrar volumen y proporción en paneles separados cuando ambos importan.

**Conceptos y términos.** *Conteo*, *proporción*, *tasa*, *exposición*, *línea base cero*, *barra apilada*.

**Descripción visual relevante.** Tres paneles usan las mismas categorías con conteos, porcentajes y tasas conceptuales. Los títulos y ejes cambian explícitamente. La comparación demuestra que el ranking puede variar con el denominador; no presenta resultados reales.

**Ejemplo de movilidad.** Pickups reportados por zona son conteos. Pickups por hora observada es una tasa temporal descriptiva. Ninguna es tasa de demanda total sin un denominador y mecanismo adecuados.

**Error frecuente o límite.** Truncar el eje, comparar zonas por conteo bruto como si fuera riesgo o ocultar volumen con barras al 100 %.

**Comprobación.** Pedir denominadores posibles para una pregunta espacial: hora observada, población, superficie u oferta; la elección depende del estimando.

**Conclusión que debe quedar.** La barra solo es honesta cuando título, eje y denominador nombran la cantidad correcta.

**Transición sugerida.** “Con variables individuales comprendidas, estudiemos relaciones mediante una secuencia que preserve su forma”.

## Diapositiva 26. Secuencia para estudiar relaciones

**Correspondencia con el libro.** Capítulo 4, introducción de §4.2 y estrategia de §4.2.7.

**Propósito.** Impedir que un coeficiente sustituya comprensión univariada, gráfica y contextual.

**Guion sugerido.** Secuencia: comprender cada variable y faltantes; confirmar unidad conjunta; visualizar relación; estratificar; cuantificar con medida apropiada; revisar casos influyentes; formular alternativas; registrar hipótesis. La medida se elige después de observar forma y escala.

**Conceptos y términos.** *Relación bivariada*, *unidad conjunta*, *forma*, *estrato*, *caso influyente*, *hipótesis alternativa*.

**Descripción detallada del diagrama.** Ocho pasos forman una ruta con retornos. Un candado antes de cuantificar exige unidad y pares válidos; otro antes de interpretar exige estratos y alternativas. Las flechas no indican confirmación creciente.

**Ejemplo de movilidad.** Antes de relacionar clima y pickups, volver a una unidad por hora evita contar muchas veces la misma observación NOAA repetida en zonas.

**Error frecuente o límite.** Calcular una matriz completa y buscar la celda más intensa.

**Comprobación.** “¿Por qué no correlacionar directamente zona-hora con clima repetido por zona?”. Introduce pseudorreplicación y una unidad incoherente para la señal de una estación.

**Conclusión que debe quedar.** Estudiar relaciones exige forma, unidad, condicionamiento y alternativas antes de interpretar magnitud.

**Transición sugerida.** “Comencemos con dos variables categóricas y sus conteos conjuntos”.

## Diapositiva 27. Tablas de contingencia

**Correspondencia con el libro.** Capítulo 4, §4.2.1.

**Propósito.** Leer conteos conjuntos, marginales, celdas esperadas y categorías raras.

**Guion sugerido.** Una tabla cruza categorías; cada celda contiene un conteo conjunto y los márgenes suman filas o columnas. Bajo independencia, los esperados dependen de marginales. Las celdas pequeñas son inestables y los ceros pueden reflejar ausencia o cobertura.

**Conceptos y términos.** *Tabla de contingencia*, *conteo conjunto*, *marginal*, *independencia*, *frecuencia esperada*.

**Lectura detallada de la tabla.** Leer primero el título y la unidad, luego una celda, después marginales y total. Los conteos muestran volumen, todavía no comparabilidad. Colores, si existen, deben distinguir desviación respecto de referencia y no gravedad causal.

**Ejemplo de movilidad.** Cruzar franja y categoría de volumen de pickups reportados describe zona-horas registradas, no pasajeros ni solicitudes no atendidas.

**Error frecuente o límite.** Comparar celdas sin considerar tamaños marginales o agrupar categorías raras solo para reforzar un patrón.

**Comprobación.** Pedir identificar numerador y unidad de una celda: número de zona-horas que cumplen ambas categorías.

**Conclusión que debe quedar.** La tabla conjunta organiza evidencia; la asociación requiere elegir condicionamiento y denominador.

**Transición sugerida.** “Normalicemos la tabla en la dirección que responda nuestra pregunta”.

## Diapositiva 28. Proporciones condicionadas

**Correspondencia con el libro.** Capítulo 4, §4.2.1, proporciones por fila y condicionamiento.

**Propósito.** Mostrar que invertir numerador y denominador cambia la pregunta.

**Guion sugerido.** Una proporción por fila divide cada celda por su total de fila y pregunta cómo se distribuye la columna dentro de esa fila. Una proporción por columna responde la inversa. Pronunciar “entre” con cuidado y señalar el grupo condicionado.

**Conceptos y términos.** *Condicionamiento*, *proporción por fila*, *proporción por columna*, *distribución condicional*, *denominador*.

**Descripción visual relevante.** Dos copias de la misma tabla conceptual normalizan filas y columnas. Flechas rodean el denominador correspondiente y muestran que ambas tablas pueden tener porcentajes correctos pero responder preguntas diferentes.

**Ejemplo de movilidad.** “Proporción de zona-horas con volumen alto dentro de cada franja” no equivale a “proporción de franjas entre zona-horas con volumen alto”. Ambas se limitan a pickups reportados.

**Error frecuente o límite.** Interpretar $P(A\mid B)$ como $P(B\mid A)$ o comparar porcentajes sin mostrar tamaños.

**Comprobación.** Dar dos frases inversas y pedir señalar qué margen debe sumar 100 %.

**Conclusión que debe quedar.** Toda proporción condicionada debe nombrar explícitamente “dentro de qué” se calcula.

**Transición sugerida.** “Cuando la respuesta es numérica y los grupos son categóricos, comparamos distribuciones completas”.

## Diapositiva 29. Comparación numérica entre grupos

**Correspondencia con el libro.** Capítulo 4, §§4.1.4, 4.1.6, 4.3.3 y §4.2.

**Propósito.** Comparar posición, dispersión, forma, tamaño y cobertura bajo reglas comunes.

**Guion sugerido.** Verificar misma unidad, periodo, escala, inclusión y significado. Reportar tamaño, centro, cuantiles, dispersión y forma. Una diferencia de medias puede coexistir con gran solapamiento o estar dominada por composición y extremos.

**Conceptos y términos.** *Comparabilidad*, *solapamiento*, *composición*, *heterogeneidad*, *tamaño de grupo*.

**Descripción visual relevante.** Paneles de cajas, violines o puntos usan una escala común y grupos ordenados por criterio sustantivo. Cobertura y $n$ aparecen junto a cada grupo. No se dibujan diferencias inventadas.

**Ejemplo de movilidad.** Comparar pickups zona-hora entre franjas exige igual marco de zonas y días; una franja con más horas o cobertura distinta no se compara solo por conteo total.

**Error frecuente o límite.** Declarar “diferencia significativa” desde cajas separadas o atribuirla a la franja como causa.

**Comprobación.** Pedir cinco controles antes de comparar dos grupos: unidad, periodo, inclusión, tamaño/cobertura y distribución.

**Conclusión que debe quedar.** Una comparación descriptiva válida conserva reglas comunes y presenta distribución, no solo un promedio.

**Transición sugerida.** “Para dos variables numéricas, la nube de puntos permite observar forma antes de resumir”.

## Diapositiva 30. Diagrama de dispersión

**Correspondencia con el libro.** Capítulo 4, §4.3.5.

**Propósito.** Leer forma, dirección, densidad, heterogeneidad y casos influyentes.

**Guion sugerido.** Definir qué representa cada punto. Observar rango, curvatura, grupos, límites y sobreposición antes de trazar una recta. Transparencia, hexágonos o paneles pueden mostrar densidad; cualquier muestreo debe declararse.

**Conceptos y términos.** *Par ordenado*, *nube*, *linealidad*, *sobreposición*, *hexágono*, *curva descriptiva*.

**Descripción detallada del diagrama.** Cuatro nubes conceptuales muestran relación lineal, curva, grupos y un punto influyente. Comparten escalas y no incluyen coeficientes para obligar a describir forma primero. Una etiqueta fija la unidad de cada punto.

**Ejemplo de movilidad.** En una vista horaria, cada punto podría ser una hora con pickups reportados totales y observación NOAA de estación; no una zona-hora si el clima se repite entre zonas.

**Error frecuente o límite.** Agregar una recta y narrarla como efecto, ocultar densidad con puntos opacos o ignorar grupos temporales.

**Comprobación.** Pedir describir una nube sin usar “causa”, “impacto” ni “significativo”.

**Conclusión que debe quedar.** La dispersión revela si un resumen lineal es plausible y qué estructura podría ocultar.

**Transición sugerida.** “Solo después de observar la nube tiene sentido introducir un resumen de variación lineal conjunta”.

## Diapositiva 31. Covarianza y correlación

**Correspondencia con el libro.** Capítulo 4, §§4.2.2-4.2.4.

**Propósito.** Diferenciar variación conjunta dependiente de unidades y asociación estandarizada.

**Guion sugerido.** La covarianza promedia productos de desviaciones y conserva producto de unidades. Pearson la divide por desviaciones y resume linealidad entre -1 y 1. Spearman y Kendall resumen orden monotónico. Ningún coeficiente captura toda dependencia ni resuelve confusión.

**Conceptos y términos.** *Covarianza*, *Pearson*, *Spearman*, *Kendall*, *lineal*, *monotónico*, *estandarización*.

**Lectura conceptual de las medidas.** Signo indica dirección promedio; magnitud depende de forma, rango, ruido y población. Correlación cero descarta asociación lineal muestral, no independencia. Elegir el coeficiente por pregunta y escala, no por el valor más alto.

**Ejemplo de movilidad.** Una asociación entre temperatura de estación y pickups horarios reportados describiría la ventana y la unidad horaria; no clima zonal, demanda total ni efecto.

**Error frecuente o límite.** Confundir correlación con pendiente o interpretar un decimal adicional como certeza.

**Comprobación.** “¿Puede una U perfecta tener correlación de Pearson cercana a cero?”. Sí; productos positivos y negativos pueden compensarse.

**Conclusión que debe quedar.** Un coeficiente es un resumen de una forma específica en una población observada.

**Transición sugerida.** “Examinemos las condiciones que pueden volver engañoso incluso un coeficiente correctamente calculado”.

## Diapositiva 32. Trampas de correlación

**Correspondencia con el libro.** Capítulo 4, §§4.2.2-4.2.4 y §4.4.4, riesgo exploratorio.

**Propósito.** Reconocer no linealidad, extremos, rango restringido, mezcla, dependencia, multiplicidad y correlación mecánica.

**Guion sugerido.** Recorrer seis trampas: forma no lineal; punto influyente; rango estrecho; mezcla de grupos; observaciones repetidas o pseudorreplicación; muchas comparaciones o variables derivadas. Para cada una pedir qué gráfico o estrato la haría visible.

**Conceptos y términos.** *Restricción de rango*, *pseudorreplicación*, *multiplicidad*, *correlación mecánica*, *caso influyente*.

**Descripción visual relevante.** La tabla enumera seis trampas y qué puede ocultar cada una. El bloque NOAA materializa pseudorreplicación y la frase inferior advierte contra seleccionar el coeficiente por conveniencia narrativa.

**Ejemplo de movilidad.** Replicar una observación NOAA en cada zona-hora y tratar todas las filas como clima independiente infla el tamaño aparente. Hora y zona repetidas también introducen dependencia.

**Error frecuente o límite.** Escoger Pearson o Spearman según cuál respalde mejor una historia.

**Comprobación.** Presentar una nube con dos grupos y pedir correlación global versus pregunta dentro de grupos; no hace falta calcular.

**Conclusión que debe quedar.** La validez de una correlación depende tanto del diseño de observación como de la fórmula.

**Transición sugerida.** “La trampa más importante es convertir una asociación descriptiva en intervención causal”.

## Diapositiva 33. Asociación, causalidad, confusión y Simpson

**Correspondencia con el libro.** Capítulo 4, §§4.2.5-4.2.6.

**Propósito.** Separar coexistencia, efecto de intervención, tercera variable e inversión por agregación.

**Guion sugerido.** Asociación significa que la distribución conjunta no se explica como producto de las marginales. Causalidad afirma qué cambiaría bajo una intervención y requiere contrafactual, diseño o supuestos. Un confusor plausible es una causa común previa; asociarse con exposición y resultado no basta, pues también existen mediadores y colisionadores. La paradoja de Simpson muestra que una asociación agregada puede invertirse dentro de estratos. Estratificar ayuda a describir, no garantiza causalidad.

**Conceptos y términos.** *Asociación*, *causalidad*, *contrafactual*, *confusor*, *paradoja de Simpson*, *agregación*.

**Descripción detallada del diagrama.** El esquema $Z\rightarrow X$ y $Z\rightarrow Y$ representa una hipótesis de causa común. La línea discontinua entre $X$ e $Y$ representa la asociación por investigar, no un efecto identificado. La tabla contigua separa asociación, causalidad, confusión y Simpson.

**Ejemplo de movilidad.** Hora del día, día, oferta, ruta, aeropuerto y eventos pueden relacionarse con pickups reportados y clima o circulación. Una estación NOAA no representa exposición climática específica de cada zona.

**Error frecuente o límite.** Usar precedencia temporal o una correlación alta como prueba de efecto, o decir que estratificar por hora “elimina toda confusión”.

**Comprobación.** Reformular “la lluvia aumenta la demanda” como hipótesis: “la asociación observada entre precipitación de estación y pickups reportados podría variar por hora, día, oferta y cobertura”.

**Conclusión que debe quedar.** Diagnóstico descriptivo localiza asociaciones y confusores plausibles; no identifica causalidad.

**Transición sugerida.** “La respuesta exploratoria inmediata es comparar relaciones dentro de grupos sustantivos y documentados”.

## Diapositiva 34. Segmentación y estratificación

**Correspondencia con el libro.** Capítulo 4, §§4.2.1, 4.2.6 y 4.2.7.

**Propósito.** Usar grupos para revelar heterogeneidad sin fragmentar hasta fabricar patrones.

**Guion sugerido.** Segmentar describe subconjuntos relevantes; estratificar compara una relación dentro de niveles de una tercera variable. Los grupos deben definirse por dominio y antes de interpretar cuando sea posible. Reportar tamaño, cobertura y reglas; demasiados estratos generan celdas vacías y multiplicidad.

**Conceptos y términos.** *Segmento*, *estrato*, *heterogeneidad*, *modificación de efecto*, *celdas escasas*.

**Descripción visual relevante.** Dos bloques distinguen segmentar y estratificar; la tabla enfrenta criterios de un estrato útil con riesgos como partición oportunista, celdas escasas y escalas incompatibles.

**Ejemplo de movilidad.** Comparar por franja, borough o tipo de zona puede distinguir composiciones, pero pickups siguen siendo reportes realizados y cada grupo necesita suficiente cobertura.

**Error frecuente o límite.** Probar muchas particiones y publicar solo aquella con mayor contraste, o confundir heterogeneidad con causa.

**Comprobación.** Pedir criterios para un estrato útil: relevancia sustantiva, temporalidad adecuada, tamaño, cobertura y definición reproducible.

**Conclusión que debe quedar.** Estratificar comprueba estabilidad descriptiva y revela heterogeneidad; no crea evidencia causal por sí solo.

**Transición sugerida.** “Dos estructuras no deben tratarse como categorías ordinarias: tiempo y espacio”.

## Diapositiva 35. Exploración temporal

**Correspondencia con el libro.** Capítulo 4, §§4.3.6-4.3.7 y ejemplo §4.3.9.

**Propósito.** Analizar orden, frecuencia, huecos, ciclos y cambios de definición.

**Guion sugerido.** Una línea sugiere continuidad y exige orden e intervalos claros. Mostrar frecuencia, zona horaria, huecos y cobertura. Comparar periodos alineando calendario y estacionalidad. Suavizar puede revelar tendencia, pero desplaza picos y oculta cambios.

**Conceptos y términos.** *Serie temporal*, *frecuencia*, *estacionalidad*, *tendencia*, *hueco*, *dependencia temporal*.

**Descripción detallada del diagrama.** Una serie conceptual incluye puntos regulares, un hueco visible y una anotación de cambio de definición. Las líneas no atraviesan el hueco como si hubiera observación; la lista contigua exige declarar frecuencia, cobertura, ciclos y calendario.

**Ejemplo de movilidad.** Una serie de pickups reportados por hora describe viajes registrados. La señal NOAA corresponde a una estación; coincidencias temporales no son clima zonal ni causalidad.

**Error frecuente o límite.** Elegir una ventana favorable, conectar observaciones irregulares o comparar lunes con feriado sin contexto.

**Comprobación.** “¿Qué debe acompañar un pico?”. Hora/zona horaria, cobertura, denominador, eventos y estabilidad ante resolución.

**Conclusión que debe quedar.** El tiempo agrega orden y dependencia; una tendencia visible necesita calendario, cobertura y definición estable.

**Transición sugerida.** “El espacio agrega vecindad, área, proyección y riesgos propios de representación”.

## Diapositiva 36. Exploración espacial

**Correspondencia con el libro.** Capítulo 4, §4.3.7 y ejemplo §4.3.9; capítulo 3, integración espacial.

**Propósito.** Elegir mapas y denominadores sin confundir área, cobertura y concentración.

**Guion sugerido.** Coropletas suelen representar tasas o proporciones; conteos brutos mezclan tamaño y exposición. Declarar proyección, límites, clasificación de color y zonas sin datos. Cuantiles y cortes fijos producen mapas distintos. Considerar dependencia espacial y privacidad.

**Conceptos y términos.** *Coropleta*, *mapa de puntos*, *densidad*, *proyección*, *clasificación*, *dependencia espacial*.

**Descripción detallada del diagrama.** Tres mapas conceptuales usan la misma geometría para distinguir conteo, tasa y cobertura. La tabla superior indica que cero y sin dato deben diferenciarse y que denominador, cortes, sobreposición y privacidad son controles obligatorios; los esquemas no codifican resultados.

**Ejemplo de movilidad.** Un mapa TLC localiza pickups realizados/reportados. No representa demanda total. Incorporar NOAA no convierte una estación en clima de cada polígono; repetir el mismo valor solo alinea tiempo bajo un supuesto espacial fuerte.

**Error frecuente o límite.** Interpretar color oscuro como riesgo individual, ocultar zonas sin cobertura o usar conteos como tasas.

**Comprobación.** Pedir qué cambiaría entre mapa por superficie, población, hora observada u oferta: cambia el estimando y posiblemente el patrón.

**Conclusión que debe quedar.** Un mapa describe una medida espacial definida; no explica por sí solo por qué aparece su patrón.

**Transición sugerida.** “Al sumar variables y filtros crece la capacidad de descubrir, pero también la de encontrar casualidades”.

## Diapositiva 37. Exploración multivariada y riesgo exploratorio

**Correspondencia con el libro.** Capítulo 4, §4.2.7 y §4.4.4, riesgo exploratorio.

**Propósito.** Equilibrar vistas multivariadas con selección de hipótesis, escala, dependencia y multiplicidad.

**Guion sugerido.** Matrices de pares, mapas de calor y facetas detectan redundancia, grupos y casos extraños en combinación. Estandarizar equilibra escala matemática, no importancia sustantiva. Muchas variables, filtros y cortes permiten descubrir patrones casuales; registrar universo explorado y separar descubrimiento de confirmación.

**Conceptos y términos.** *Multivariado*, *matriz de pares*, *estandarización*, *redundancia*, *multiplicidad*, *riesgo exploratorio*.

**Descripción visual relevante.** La tabla vincula selección de variables, estandarización, filtros y elección de patrones con sus controles. Una frontera discontinua separa “hipótesis generada” de “evaluación futura”.

**Ejemplo de movilidad.** Explorar hora, zona, pickups y clima de estación puede proponer segmentos; no autoriza elegir la combinación más llamativa como ley general.

**Error frecuente o límite.** Interpretar una matriz de correlación como lista de descubrimientos confirmados o duplicar peso con variables derivadas.

**Comprobación.** “¿Qué debe registrarse además del gráfico elegido?”. Variables y filtros probados, exclusiones, transformaciones, decisiones y resultados que limitaron la historia.

**Conclusión que debe quedar.** Cuanto mayor sea la libertad exploratoria, mayor debe ser la transparencia y la necesidad de confirmación independiente.

**Transición sugerida.** “Convirtamos una observación provisional en una afirmación que conserve evidencia y límites”.

## Diapositiva 38. Anatomía de un hallazgo defendible

**Correspondencia con el libro.** Capítulo 4, §§4.4.1, 4.4.6-4.4.8 y síntesis.

**Propósito.** Proporcionar una estructura verificable para redactar hallazgos exploratorios.

**Guion sugerido.** Un hallazgo contiene pregunta; población, unidad y periodo; patrón y magnitud observada; evidencia visual o tabular; cobertura; interpretación limitada; alternativa; sensibilidad; próximo análisis. Separar dato, interpretación y recomendación. Usar verbos “se observa”, “se asocia” o “coincide”, no “produce”.

**Conceptos y términos.** *Hallazgo*, *magnitud*, *alcance*, *limitación*, *explicación alternativa*, *siguiente paso*.

**Descripción detallada del diagrama.** La tabla organiza seis campos: contrato, observación, soporte, cobertura, interpretación y defensa. El bloque inferior ofrece una plantilla sin resultado y la frase final controla el lenguaje causal.

**Ejemplo de movilidad.** Plantilla sin resultado: “En [periodo y unidades observadas], los pickups TLC realizados/reportados muestran [patrón por completar desde evidencia], bajo [cobertura]; el patrón coincide con [variable], pero puede reflejar calendario, oferta, selección u otros factores. NOAA representa una estación, no clima zonal”.

**Error frecuente o límite.** Redactar una conclusión primero y buscar luego una figura, o esconder límites en una nota que contradice el título.

**Comprobación.** Evaluar una frase deliberadamente causal y reconstruirla con los nueve campos sin inventar dirección ni magnitud.

**Conclusión que debe quedar.** Un hallazgo defendible es específico, trazable, proporcional a la evidencia y abierto a refutación.

**Transición sugerida.** “La práctica futura deberá producir varios hallazgos con este mismo contrato, no cinco gráficos aislados”.

## Diapositiva 39. Contrato de cinco hallazgos y continuidad

**Correspondencia con el libro.** Capítulo 4, actividad integradora y ejemplos §§4.1.8, 4.2.8 y 4.3.9; continuidad con capítulos 2 y 3.

**Propósito.** Definir el producto conceptual que orientará el notebook posterior sin diseñarlo ni anticipar resultados.

**Guion sugerido.** El futuro trabajo deberá entregar cinco hallazgos complementarios: distribución univariada; comparación de grupos; relación entre variables; patrón temporal; patrón espacial o multivariado. Cada uno tendrá contrato, evidencia, cobertura, sensibilidad, límite y próximo paso. Incluir una revisión transversal de ceros/faltantes y atípicos.

**Conceptos y términos.** *Contrato de hallazgo*, *complementariedad*, *evidencia reproducible*, *continuidad*, *defensa*.

**Descripción visual relevante.** La tabla enumera los cinco hallazgos requeridos y la pregunta de cada uno. El bloque inferior concentra los controles comunes y el texto inicial indica que el notebook todavía no existe.

**Ejemplo de movilidad.** Los cinco hallazgos deberán nombrar siempre pickups como viajes realizados/reportados; cualquier análisis NOAA deberá declarar una estación y no clima zonal. Toda asociación se presentará como hipótesis, nunca confirmación causal.

**Error frecuente o límite.** Forzar cinco resultados “interesantes”, contar cinco vistas del mismo patrón o evaluar por cifras esperadas.

**Comprobación.** Pedir qué invalida un hallazgo aunque el gráfico sea correcto: unidad ambigua, denominador oculto, causalidad no identificada o límite incompatible.

**Conclusión que debe quedar.** La práctica se evaluará por coherencia y defensa de cinco hallazgos, no por encontrar patrones predeterminados.

**Transición sugerida.** “Cerremos recuperando las decisiones que todo hallazgo deberá conservar y las lecturas que permiten profundizar”.

## Diapositiva 40. Síntesis y lecturas

**Correspondencia con el libro.** Síntesis y autoevaluación del capítulo 4; continuidad de capítulos 2 y 3.

**Propósito.** Consolidar ocho ideas y orientar lectura y práctica posterior.

**Guion sugerido.** Recuperar los ocho puntos de la lámina: población y estimando; cero y faltante; distribución, forma y cobertura; robustez y atípicos; codificación y forma antes que coeficiente; asociación y causalidad; estratos, tiempo y espacio; alcance y defensa del hallazgo. Repetir que EDA genera hipótesis, no confirmación.

**Conceptos y términos.** No introducir vocabulario nuevo; integrar población, estimando, distribución, robustez, codificación, asociación, confusión y hallazgo.

**Descripción visual relevante.** La enumeración consolida ocho decisiones y el bloque inferior presenta la lectura principal del capítulo 4. La frase de cierre resume precisión descriptiva, comparación honesta y límites visibles.

**Ejemplo de movilidad.** La pregunta final es: “¿Qué evidencia adicional permitiría distinguir mejor viajes realizados, oferta y demanda no atendida, y qué diseño permitiría estudiar una causa?”. Se aceptan propuestas justificadas, no resultados.

**Error frecuente o límite.** Cerrar con una lista de gráficos o sugerir que una exploración exhaustiva elimina incertidumbre.

**Comprobación.** Cada estudiante formula una regla que conservará en la práctica y una afirmación que no estará autorizada a hacer.

**Conclusión que debe quedar.** Explorar responsablemente significa describir con precisión, comparar con honestidad y mantener visibles población, denominadores, cobertura, alternativas y límites.

**Transición sugerida.** “La próxima práctica materializará este contrato en un notebook reproducible que todavía debe diseñarse”.

### Referencias

- `../../../Libro/Capitulo_02_Ciclo_de_vida_de_un_proyecto_de_datos.md`
- `../../../Libro/Capitulo_03_Preparacion_calidad_y_transformacion_de_datos.md`
- `../../../Libro/Capitulo_04_Estadistica_descriptiva_exploracion_y_visualizacion.md`
