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

# Guía docente: Introducción a la Ciencia de Datos

**Curso:** Data Science

**Semana y clase:** semana 1, clase 1

**Presentación asociada:** *Introducción a la Ciencia de Datos: de una necesidad a evidencia útil para decidir* (38 diapositivas)

**Fuentes principales:** capítulos 1 y 2 del libro *Ciencia de Datos e Inteligencia Artificial*

## Propósito y forma de uso

Esta guía desarrolla relaciones conceptuales, fórmulas, recorridos visuales, comprobaciones y transiciones. La clase no comienza con software, sino con una necesidad, la evidencia posible y la decisión que apoyaría.

El caso transversal es una empresa de **movilidad urbana** que desea reducir demoras. El producto puede describir, predecir o recomendar, pero operaciones conserva autoridad para aprobar y ejecutar. Se mantendrán cuatro niveles:

1. **Modelo:** representación o función que resume o estima.
2. **Evidencia:** resultado interpretado y validado dentro de un alcance.
3. **Decisión:** selección de una acción con objetivos, costos y restricciones.
4. **Autoridad humana:** persona o instancia institucional que aprueba, ejecuta, revisa y responde por la acción.

La secuencia amplía la presentación actual. El aprendizaje se comprueba mediante preguntas, actividad, revisión y defensa.

### Recorrido de la clase

| Bloque | Diapositivas | Resultado esperado |
|---|---:|---|
| Apertura y concepto | 1-6 | Delimitar Ciencia de Datos y entender los datos como representaciones |
| Proceso y propósitos | 7-14 | Explicar el ciclo, clasificar preguntas y separar predicción de decisión |
| Formulación | 15-18 | Especificar problema, unidad, población, horizonte y alcance |
| Organización del trabajo | 19-28 | Comparar workflow, metodologías, estructuras, fuentes y reproducibilidad |
| Caso aplicado | 29-32 | Formular movilidad, distinguir tareas y detectar fuga temporal |
| Producción y defensa | 33-35 | Elaborar, revisar y defender una ficha de problema |
| Cierre | 36-38 | Sintetizar el marco y orientar lecturas verificadas |

> **Tesis de la clase:** un proyecto de datos es un sistema de producción de evidencia para una decisión. Un modelo puede formar parte de ese sistema, pero no reemplaza la formulación, la validación, la responsabilidad ni la autoridad de uso.

## Diapositivas 1-3. Apertura: título, propósito y pregunta inicial

**Correspondencia con el libro:** capítulo 1, propósito y §1.1.1; capítulo 2, propósito y objetivos de aprendizaje, introducción de §2.1 y §2.1.1.

### Qué exponer

La diapositiva 1 pregunta: **¿cómo se transforma una necesidad real en evidencia útil para decidir?** Útil no significa solo exacta: debe llegar a tiempo, representar la unidad de acción y encajar en la capacidad del decisor.

La diapositiva 2 plantea desempeños: distinguir problema, observación, modelo, evidencia y decisión; clasificar preguntas; reconocer iteración; caracterizar datos; y formular movilidad. No se entrena un modelo.

En la diapositiva 3, presentar “mejorar el servicio” y registrar fenómeno, usuario, unidad, acción y evaluación. Abrir un dataset antes de precisarlos puede llevar a responder rigurosamente la pregunta equivocada.

### Fórmulas e interpretación

No se introduce aún una fórmula de modelado. Se presenta la cadena conceptual del capítulo 2:

$$
\text{necesidad}\rightarrow\text{pregunta analítica}\rightarrow
\text{tarea computacional}\rightarrow\text{evidencia}\rightarrow\text{decisión}.
$$

Cada flecha exige justificación: una tarea produce una salida, no evidencia automática, y la evidencia no posee autoridad de ejecución.

### Ejemplo de movilidad

“Mejorar” puede significar reducir demora, cancelaciones o desigualdad territorial. Una predicción por viaje no resuelve directamente una reasignación por zona.

### Error frecuente o advertencia

El error inicial es traducir “queremos mejorar” como “necesitamos aprendizaje automático”. La técnica no define el problema. También debe evitarse prometer impacto operativo sin identificar quién puede modificar una acción a partir del resultado.

### Comprobación

Preguntar: “Si la empresa usará exactamente la misma distribución de vehículos cualquiera sea el análisis, ¿existe una decisión asociada?”. Respuesta esperada: no; puede existir valor descriptivo, pero no debe afirmarse que el pronóstico reducirá demoras por sí mismo.

**Transición sugerida:** “Para diseñar esa cadena necesitamos aclarar qué hace la Ciencia de Datos y qué tipo de objeto es un dato”.

## Diapositivas 4-6. Definición y datos como representaciones

**Correspondencia con el libro:** capítulo 1, §1.1.1 y distinción entre datos, información, conocimiento y decisión; capítulo 2, introducción de §2.3 y §§2.3.1-2.3.3.

### Qué exponer

La diapositiva 4 define Ciencia de Datos como campo interdisciplinario que obtiene conocimiento y apoya decisiones desde datos. Conocimiento exige validación; apoyar no significa sustituir al decisor.

La diapositiva 5 separa fenómeno, medición y registro. Un dato es una representación producida con unidad, precisión, frecuencia, cobertura y propósito. Dos columnas `demora` pueden significar cálculo horario o categoría declarada.

La diapositiva 6 organiza niveles: **datos**, observaciones codificadas; **información**, datos contextualizados; **conocimiento**, patrones interpretados; **decisión**, selección de acción. El modelo resume o estima, pero no convierte automáticamente un nivel en otro.

### Fórmulas e interpretación

Introducir una representación mínima de medición:

$$
x_{obs}=g(z, instrumento, contexto)+\varepsilon,
$$

donde $z$ es el fenómeno, $g$ el proceso de observación y $\varepsilon$ el error. Es una expresión didáctica, no literal del libro: corregir ruido no recupera todo lo omitido por $g$.

### Ejemplo de movilidad

El GPS puede omitir carril, pérdida de señal o contexto. Un reclamo representa a quien usó el canal, no a todos los pasajeros. La hora real se registra después del viaje.

### Recorrido visual

Recorrer fenómeno, captura, registro y tabla; preguntar qué cambia en cada flecha. Terminar en decisión, separada de la fila.

### Error frecuente o advertencia

No decir que un dato es “objetivo” solo porque proviene de un sensor. Los sensores tienen calibración, cobertura y fallos; los registros administrativos contienen reglas del proceso que los genera. Más volumen no elimina un sesgo sistemático de representación.

### Comprobación

Mostrar `sin señal GPS = 0,0` y preguntar si es una ubicación válida. La respuesta esperada es que ausencia, cero y valor inválido son estados diferentes y deben conservar significado.

**Transición sugerida:** “Si los datos son representaciones parciales, necesitamos un proceso que conserve su significado desde la pregunta hasta la evaluación”.

## Diapositivas 7-8. Ciclo general de un proyecto de datos

**Correspondencia con el libro:** capítulo 1, §1.1.1; capítulo 2, propósito, figura inicial y síntesis del capítulo.

### Qué exponer

La diapositiva 7 presenta `problema -> datos -> representación -> análisis -> evidencia -> decisión -> evaluación`: delimitar, observar, construir variables, analizar, validar, decidir con autoridad y observar consecuencias.

La diapositiva 8 niega una lectura lineal. Pregunta no medible, etiqueta inválida o salida tardía obligan a volver y registrar la evidencia que motivó la revisión.

### Fórmulas e interpretación

No se requiere una nueva fórmula cuantitativa. La formalización relevante es la composición de transformaciones:

$$
D_0 \xrightarrow{T_1} D_1 \xrightarrow{T_2} R
\xrightarrow{V} E,
$$

donde $D_0$ son fuentes, $T_i$ transformaciones, $R$ resultado, $V$ validación y $E$ evidencia. Resultado y evidencia no son sinónimos.

### Ejemplo de movilidad

Los cancelados carecen de `hora_real`; eliminarlos haría parecer mejor el servicio. Se debe revisar el resultado y tratar demora y cancelación separadas o juntas.

### Recorrido visual

Recorrer la flecha principal y volver desde evaluación: a representación si cambia la unidad, a datos si falta cobertura y a problema si no hay acción. El modelo ocupa solo un tramo.

### Error frecuente o advertencia

Evitar presentar el ciclo como una cinta transportadora donde cada equipo entrega un archivo al siguiente. Sin retroalimentación, los errores semánticos se consolidan. Tampoco confundir “iterativo” con cambiar criterios después de ver resultados para favorecerlos.

### Comprobación

Preguntar: “¿Qué etapa debe revisarse si la predicción llega diez minutos después de que operaciones asignó los vehículos?”. Deben aparecer formulación temporal, arquitectura de datos y proceso de uso, no solo “hacer más rápido el algoritmo”.

**Transición sugerida:** “Dentro del ciclo, el tipo de pregunta determina qué evidencia debe producirse”.

## Diapositivas 9-11. Taxonomía de objetivos analíticos

**Correspondencia con el libro:** capítulo 1, §1.1.1 y §1.1.5; capítulo 2, §2.1.1, especialmente preguntas descriptivas, predictivas y prescriptivas.

### Qué exponer

La diapositiva 9 presenta cinco objetivos: **describir** lo ocurrido, **diagnosticar** factores asociados, **predecir** lo desconocido, **prescribir** acciones y **monitorear** cambios. Cada uno requiere evidencia distinta.

La diapositiva 10 contrasta descripción y predicción. Una media resume lo observado; anticipar exige casos no usados para ajustar y un protocolo de generalización realista.

La diapositiva 11 separa asociación y causalidad. Lluvia y demora juntas no prueban el efecto de intervenir. Aquí diagnosticar significa explorar asociaciones; una afirmación causal requiere otro diseño.

### Fórmulas e interpretación

Una descripción puede estimar una media $E[Y]$ o proporción $P(Y=1)$. Una predicción utiliza información condicionante:

$$
P(Y\mid X)
$$

para una distribución de resultados, o

$$
E[Y\mid X]
$$

para un valor esperado. $X$ está disponible y $Y$ no se conoce. La barra se lee “dado”, no “causado por”.

### Ejemplo de movilidad

En movilidad, mediana y P90 describen; hora y lluvia diagnostican asociaciones; la demora siguiente se predice; reasignaciones se prescriben; cambios de demora o GPS se monitorean.

### Recorrido visual

Recorrer preguntas, productos y evaluación. En el gráfico marcar pasado, corte y futuro; la exactitud predictiva no mide el valor de reasignar.

### Error frecuente o advertencia

No usar “predecir” como sinónimo de explicar ni “diagnosticar” como prueba causal. Tampoco exigir a toda iniciativa un modelo predictivo: un inventario de fuentes o una medición de cobertura puede ser el producto correcto.

### Comprobación

Solicitar clasificar: “¿Dónde se concentraron las demoras?”, “¿cuánto demorará el viaje?” y “¿qué vehículo debe moverse?”. Respuestas: descriptiva, predictiva y prescriptiva. Pedir además qué información nueva incorpora cada paso.

**Transición sugerida:** “La diferencia más peligrosa aparece al convertir una predicción en una decisión; ahora haremos explícito ese salto”.

## Diapositivas 12-13. De predicción a decisión

**Correspondencia con el libro:** capítulo 1, §1.1.2, §1.1.5 y §1.2.4; capítulo 2, §2.1.1 y §2.1.5.

### Qué exponer

La diapositiva 12 separa cajas: el modelo estima; la evidencia delimita validez; la decisión compara; la autoridad humana aprueba o rechaza. Así se evita “el modelo decidió”.

La diapositiva 13 agrega costos y utilidad. La misma probabilidad produce acciones distintas según capacidad y costo. Las restricciones excluyen acciones; la autoridad queda fuera de la fórmula.

### Fórmulas e interpretación

La regla general de decisión por utilidad esperada es:

$$
a^*=\operatorname*{arg\,max}_{a\in\mathcal A}
\sum_s P(s\mid x)U(a,s).
$$

$s$ son estados, $P(s\mid x)$ creencias, $U(a,s)$ consecuencias valoradas y $\mathcal A$ acciones factibles. `arg max` devuelve una acción; la incertidumbre se pondera.

Una regla binaria sencilla recomienda intervenir cuando:

$$
pC_f>C_i,
$$

donde $p$ es probabilidad, $C_f$ costo de no intervenir y $C_i$ costo de intervención. Con $0{,}30$, 100 y 10, no intervenir cuesta 30 en esperanza. La regla depende de sus supuestos.

### Ejemplo de movilidad

Con 70 % de demanda alta en B, mover dos vehículos reduce espera pero puede dejar A sin cobertura. El sistema presenta opciones; operaciones decide y se registran acción y resultado.

### Recorrido visual

Recorrer $X$, modelo, predicción, evidencia, acciones, recomendación y responsable. Mostrar abstención y retorno del resultado a evaluación.

### Error frecuente o advertencia

No afirmar que una probabilidad alta “ordena” intervenir. La utilidad refleja prioridades discutibles y las restricciones no siempre deben transformarse en costos negociables. Seguridad, normativa y cobertura mínima pueden ser condiciones obligatorias.

### Comprobación

Preguntar: “¿Puede recomendarse una acción con una predicción incierta?”. Sí, si es barata, reversible y tiene buen valor esperado. “¿Puede rechazarse una predicción muy precisa?”. Sí, si no cambia acciones, llega tarde o su uso genera riesgo inaceptable.

**Transición sugerida:** “Construir y evaluar esta cadena requiere perspectivas que ningún perfil aislado reúne por completo”.

## Diapositiva 14. Interdisciplinariedad

**Correspondencia con el libro:** capítulo 1, §1.1.1 y §1.1.4; capítulo 2, §2.2.5.

### Qué exponer

Presentar la interdisciplinariedad como coordinación: estadística estudia evidencia; optimización, objetivos; computación, algoritmos; ingeniería, confiabilidad; dominio, significado; comunicación, comprensión; gobernanza, usos; usuarios, consecuencias.

Una persona puede cubrir varios roles, pero ninguna pregunta desaparece. Debe declararse quién aprueba definiciones, fuentes, métricas y uso.

### Fórmulas e interpretación

No se agrega una fórmula. Retomar la utilidad esperada para indicar que estadística contribuye a $P(s\mid x)$, dominio y gobernanza a $U$ y restricciones, ingeniería a disponer de $x$ a tiempo, y autoridad institucional a aprobar la acción. Ninguna disciplina controla legítimamente toda la expresión por sí sola.

### Ejemplo de movilidad

Operaciones define acciones; ingeniería conserva eventos; Ciencia de Datos evalúa; legal revisa ubicación; afectados aportan cobertura; dirección aprueba. Perjudicar zonas periféricas exige revisar el objetivo.

### Error frecuente o advertencia

Evitar que “interdisciplinario” signifique consultar al dominio solo al final para validar una interfaz. Las definiciones y restricciones deben acordarse antes del modelado. La revisión humana tampoco es efectiva si la persona no tiene tiempo, información o autoridad para contradecir.

### Comprobación

Pedir identificar quién responde: “¿qué significa viaje cancelado?”, “¿puede almacenarse la trayectoria?” y “¿quién autoriza mover vehículos?”. Deben distinguirse conocimiento del dominio, gobernanza de datos y autoridad operativa.

**Transición sugerida:** “El primer artefacto compartido por esas perspectivas es una formulación explícita del problema”.

## Diapositivas 15-16. Formulación: del problema real a una especificación

**Correspondencia con el libro:** capítulo 1, §1.1.1 y §1.1.6; capítulo 2, §§2.1.1, 2.1.2 y 2.1.4.

### Qué exponer

La diapositiva 15 distingue situación (“hay demoras”), pregunta (“¿cuál será la demora por zona?”) y tarea (pronóstico). Reasignar agrega optimización y restricciones. Debe explicarse sin nombrar algoritmos.

La diapositiva 16 presenta una ficha compacta. Para evitar que la población quede implícita y conservar el objetivo del capítulo 1, la clase usa:

$$
P=(U,R,O,X,Y,A,H,C).
$$

$U$ es unidad; $R$, población; $O$, objetivo; $X$, entradas; $Y$, resultado; $A$, acciones; $H$, horizonte; y $C$, restricciones. La notación combina formulaciones de ambos capítulos; no es una ecuación literal única del libro.

Interpretar: ¿qué entidad, población, propósito, información previa, resultado, acción, momento y límites? Agregar usuario, afectados, baseline y éxito en la ficha.

### Ejemplo de movilidad

$U$: zona-franja; $R$: zonas cubiertas por los operadores participantes durante operación ordinaria; $O$: reducir espera alta sin degradar cobertura; $X$: solicitudes, vehículos libres, tráfico y calendario conocidos al corte; $Y$: demanda y demora de la franja siguiente; $A$: mantener o proponer reasignaciones factibles; $H$: treinta minutos; $C$: capacidad, distancia, descanso, cobertura y aprobación humana.

### Recorrido visual

Recorrer necesidad, preguntas y tareas, y volver para comprobar correspondencia. En $P$, comenzar por $O$, usuario y acción; revisar luego los demás componentes.

### Error frecuente o advertencia

No usar un indicador disponible como sustituto silencioso del objetivo. Cantidad de reclamos no equivale a mala calidad; depende de acceso y propensión a reclamar. No incluir en $X$ información producida después de decidir.

### Comprobación

Pedir que un estudiante cambie $U$ de zona-franja a viaje y describa qué elementos deben revisarse. Deben cambiar resultado, entradas, partición, producto y quizá acción; no basta renombrar una columna.

**Transición sugerida:** “La unidad no solo organiza filas: determina sobre quién generalizamos y dónde es válida la evidencia”.

## Diapositivas 17-18. Unidad, población y alcance

**Correspondencia con el libro:** capítulo 2, §2.1.3 y conexión con §2.1.4; capítulo 1, §1.1.6.

### Qué exponer

La diapositiva 17 compara viaje, vehículo-día, parada-hora y zona-franja. La unidad determina claves, agregaciones, dependencias, particiones y decisión; una fila no es natural.

La diapositiva 18 separa población objetivo, muestra observada y despliegue. El alcance declara lugar, periodo, condiciones, acciones y exclusiones; operación ordinaria no autoriza uso en emergencias.

### Fórmulas e interpretación

Representar el cambio de distribución como:

$$
P_T(X,Y)\neq P_D(X,Y),
$$

donde $P_T$ es entrenamiento y $P_D$ despliegue. La desigualdad advierte que la evaluación puede no transferirse por cambios de población, estación, política o sensores. Tamaño no garantiza representatividad.

La declaración de generalización debe completar: “El resultado pretende aplicarse a ___, bajo ___, durante ___; no se ha evaluado en ___”. Esta frase es una especificación comprobable, no una promesa universal.

### Ejemplo de movilidad

Un millón de viajes céntricos puede representar peor la periferia que una muestra menor deliberada. Reasignar por zona exige agregar predicciones por viaje; evaluar semanas futuras exige separar por tiempo.

### Recorrido visual

Recorrer población objetivo, muestra y despliegue, identificando ausencias. Leer cada unidad desde significado hasta acción.

### Error frecuente o advertencia

No llamar censo de la realidad a un censo del sistema: la base puede contener todos los viajes registrados y omitir viajes de otros operadores o cancelaciones no ingresadas. No ampliar alcance mediante una simple modificación de interfaz; se requiere nueva evidencia.

### Comprobación

Preguntar cómo evaluar si se usará en zonas nunca observadas. La prueba debe reservar zonas, no mezclar viajes de todas las zonas al azar. Si se usará en días futuros de las mismas zonas, corresponde una separación temporal.

**Transición sugerida:** “Con el problema y su alcance definidos, podemos ordenar el trabajo sin confundir orden pedagógico con rigidez”.

## Diapositivas 19-20. Workflow y retroalimentación

**Correspondencia con el libro:** capítulo 2, propósito, §§2.1.5, 2.2.3 y 2.2.4; síntesis del capítulo.

### Qué exponer

La diapositiva 19 recorre necesidad, baseline, inventario, preparación, análisis, evaluación, integración y monitoreo. Asociar ficha, criterios, inventario, dataset versionado, experimento, informe y registro.

La diapositiva 20 usa puertas con evidencia mínima. Un producto mínimo evaluable prueba la incertidumbre crítica: si se desconoce cobertura, primero se perfila, no se modela.

### Fórmulas e interpretación

Introducir el criterio multicriterio del capítulo 2:

$$
J(m)=w_1Q(m)-w_2C(m)-w_3R(m),
$$

donde $Q$ mide calidad, $C$ costo y $R$ riesgo. Los pesos son prioridades acordadas. Una restricción dura excluye opciones, aunque su índice sea alto.

### Ejemplo de movilidad

Mejorar 2 % el error puede no compensar doble latencia y una fuente inestable. Descubrir 40 % de GPS oportuno justifica reformular alcance.

### Recorrido visual

Asociar evidencia a cada puerta y seguir retornos por fuga, falta de uso o cambio de esquema. En $J$, las dimensiones requieren documentación.

### Error frecuente o advertencia

No elegir criterios después de ver qué candidato gana. Tampoco confundir el “mejor de los probados” con un candidato aceptable. Puede ganar y no superar baseline, capacidad o riesgo permitido.

### Comprobación

Preguntar qué haría detener el proyecto. Respuestas válidas: datos sin correspondencia con el objetivo, ausencia de proceso de uso, no superar baseline, impacto insuficiente o riesgos no controlables.

**Transición sugerida:** “KDD y CRISP-DM ofrecen dos vocabularios conocidos para organizar estas actividades y hacer visibles omisiones”.

## Diapositivas 21-22. KDD y CRISP-DM

**Correspondencia con el libro:** capítulo 2, §§2.2.1 y 2.2.2.

### Qué exponer

La diapositiva 21 desarrolla KDD: selección, preprocesamiento, transformación, minería e interpretación/evaluación. La minería es una etapa; un patrón aún debe validarse e interpretarse.

La diapositiva 22 desarrolla CRISP-DM: problema, datos, preparación, modelado, evaluación y despliegue. “Negocio” incluye fines públicos; despliegue no implica automatización. Ambas son cíclicas.

### Fórmulas e interpretación

No se añade fórmula numérica. Usar la jerarquía:

$$
\text{resultado}\rightarrow\text{patrón}\rightarrow
\text{hipótesis}\rightarrow\text{hallazgo validado}\rightarrow
\text{regla operativa}.
$$

Cada transición demanda evidencia o aprobación distinta. La última incorpora autoridad institucional; no la produce el algoritmo de minería.

### Ejemplo de movilidad

Que demanda aumente a las 8:00 puede ser correcto pero trivial. Debe preguntarse si cambia una asignación, existe capacidad y cómo se integra. Reclamos y demora pueden compartir un sesgo de registro.

### Recorrido visual

En KDD recorrer selección a interpretación y volver a preprocesamiento. En CRISP-DM recorrer seis fases y retornos; alinear sin declarar identidad.

### Error frecuente o advertencia

No tratar las fases como casillas administrativas ni considerar conocimiento toda correlación novedosa para el analista. Una metodología hace preguntas visibles; no sustituye juicio, validación ni responsabilidad.

### Comprobación

Preguntar dónde se revisa un cluster bien separado sin significado operativo. En KDD, interpretación/evaluación; en CRISP-DM, evaluación respecto de la comprensión del problema, posiblemente con retorno a formulación.

**Transición sugerida:** “Las metodologías ordenan el trabajo; ahora debemos reconocer qué estructuras concretas pueden tener sus insumos”.

## Diapositivas 23-24. Datos según su estructura

**Correspondencia con el libro:** capítulo 2, §§2.3.1, 2.3.2 y 2.3.3.

### Qué exponer

La diapositiva 23 distingue estructurados con esquema; semiestructurados con claves variables o anidadas; y texto, imagen, audio o video sin variables tabulares inmediatas, aunque con estructura interna.

La diapositiva 24 muestra que aplanar puede multiplicar filas y representar texto o imagen decide qué conservar. El esquema indica almacenamiento; el diccionario, significado.

### Fórmulas e interpretación

Representar $\phi(r)=x$: del registro original a la representación analítica. $\phi$ puede perder información; se conserva original y procedencia.

### Ejemplo de movilidad

SQL de viajes es estructurado; JSON de tráfico, semiestructurado; reclamos o video, no estructurados. Expandir incidentes puede inflar viajes y exige agregar o separar tablas.

### Recorrido visual

Recorrer las tres columnas por pares “forma original -> decisión de representación”. Después seguir el diagrama desde fuente original hasta validación, tabla derivada y análisis. Señalar que el original permanece intacto y que cada derivado conserva clave y versión.

### Error frecuente o advertencia

No afirmar que “no estructurado” significa caótico o sin estructura. No equiparar `null`, clave ausente y lista vacía. No desnormalizar sin comprobar cardinalidades, porque una unión muchos-a-muchos puede multiplicar observaciones.

### Comprobación

Preguntar qué ocurre si cada viaje tiene tres incidentes y se expande la lista antes de contar viajes. El conteo puede triplicarse; debe preservarse la unidad mediante agregación o tablas relacionadas.

**Transición sugerida:** “La forma del dato explica cómo procesarlo; la procedencia explica qué podemos afirmar a partir de él”.

## Diapositivas 25-26. Fuentes, mecanismo generador y procedencia

**Correspondencia con el libro:** capítulo 2, introducción de §2.3 y §§2.3.4-2.3.6; para movilidad, §2.3.8.

### Qué exponer

La diapositiva 25 distingue observacionales, experimentales y simulados; también primarios y secundarios. Estas clasificaciones describen generación y propósito, no formato.

La diapositiva 26 registra propietario, propósito, unidad, cobertura, captura, formato, frecuencia, licencia, sensibilidad, cambios, corte, claves, zona horaria, versión y responsable. El inventario prueba integración y legitimidad.

### Fórmulas e interpretación

No se incorpora una nueva ecuación. Usar la cadena de linaje:

$$
fuente\xrightarrow{extracción}original\xrightarrow{transformación}
dataset\xrightarrow{análisis}resultado.
$$

Cada flecha registra código, configuración y tiempo. Simulación no es observación; asociación observacional no identifica por sí sola efectos.

### Ejemplo de movilidad

Viajes, clima, calendario, obras y polígonos exigen reconciliar relojes, granularidad y geometría. Se declara cobertura parcial y se descartan fuentes inestables.

### Recorrido visual

Leer unidad y reloj de cada fuente, detenerse en las uniones y retroceder desde una celda para comprobar reconstrucción.

### Error frecuente o advertencia

No considerar descargable como sinónimo de permitido. No sobrescribir originales ni ejecutar hoy la misma consulta esperando idéntico resultado en una base mutable. Una API con respuesta exitosa puede estar paginada o incompleta.

### Comprobación

Preguntar qué debe saberse antes de unir clima con demanda. Como mínimo: unidad, hora y zona, cobertura, regla espacial, frecuencia, zona horaria, faltantes y disponibilidad al momento de decisión.

**Transición sugerida:** “Cuando estas fuentes crecen y cambian, las seis V permiten diagnosticar el desafío sin reducirlo al tamaño”.

## Diapositiva 27. Las seis V de Big Data

**Correspondencia con el libro:** capítulo 2, §2.3.7; capítulo 1, §1.3.5, que presenta cinco V y sirve como antecedente.

### Qué exponer

Presentar seis dimensiones: **volumen**, cantidad; **velocidad**, ritmo; **variedad**, formatos; **veracidad**, confiabilidad; **valor**, utilidad; **variabilidad**, cambios de significado o distribución. El capítulo 1 presenta cinco y el 2 agrega variabilidad.

Velocidad exige oportunidad; variedad, integración; volumen, recursos; veracidad, controles; variabilidad, monitoreo; valor, conexión con acciones. Distribuir no corrige semántica.

### Fórmulas e interpretación

No hay fórmula obligatoria. Relacionar valor con $J(m)$: más volumen puede aumentar $Q$, pero también $C$ y $R$. La arquitectura debe justificarse mediante medidas de tamaño, crecimiento, latencia y memoria, no por la etiqueta “Big Data”.

### Ejemplo de movilidad

GPS aporta velocidad y volumen; viajes, clima y obras aportan variedad; pérdida o congelamiento de sensores afecta veracidad; eventos y políticas estacionales introducen variabilidad; una predicción que llega después de reasignar carece de valor operativo aunque procese millones de puntos.

### Recorrido visual

Recorrer el hexágono desde volumen y velocidad hacia variedad y veracidad; terminar en variabilidad y colocar valor en el centro. El recorrido comunica que valor depende de las otras dimensiones y de una decisión, no del tamaño aislado.

### Error frecuente o advertencia

No confundir precisión numérica con validez semántica. Mil millones de registros mal definidos permiten estimar con mucha estabilidad el dato equivocado. Tampoco adoptar distribución cuando una solución simple cabe y puede probarse en una máquina.

### Comprobación

Plantear un dataset pequeño de incidentes críticos, bien medidos y accionables. ¿Puede tener alto valor sin alto volumen? Sí. Pedir además qué V describe que `zona` cambió de definición: variabilidad.

**Transición sugerida:** “Independientemente de la escala, la evidencia necesita poder reconstruirse y auditarse”.

## Diapositiva 28. Reproducibilidad y trazabilidad

**Correspondencia con el libro:** capítulo 1, §1.1.4; capítulo 2, introducción de §2.4 y §§2.4.2, 2.4.5-2.4.7.

### Qué exponer

Reproducibilidad es reconstruir desde entradas y procedimiento identificados, en niveles computacional, analítico, operativo y científico. Un notebook debe ejecutarse completo en entorno limpio.

Enlazar código, datos, esquema, transformaciones, entorno, partición, parámetros, semilla, métricas y conclusión. Fuentes inmutables, productos regenerables, rutas relativas y secretos fuera del repositorio.

### Fórmulas e interpretación

Expresar un resultado como:

$$
r=F(D,v_c,v_e,\theta,s),
$$

donde $D$ identifica datos, $v_c$ código, $v_e$ entorno, $\theta$ configuración y $s$ semilla. La semilla no controla hardware o no determinismo; se reportan tolerancias.

### Ejemplo de movilidad

Un gráfico de demora por zona debe indicar corte de datos, operadores incluidos, versión de límites geográficos, zona horaria, consulta, código y reglas para cancelaciones. Otra persona debe regenerarlo sin buscar un archivo local llamado `final_v2.csv`.

### Recorrido visual

En el diagrama de reproducibilidad partir del resultado y retroceder: artefacto, ejecución, código/configuración, dataset derivado y fuentes. Después avanzar nuevamente para mostrar reconstrucción. Si una flecha depende de una acción manual no registrada, marcar la ruptura.

### Error frecuente o advertencia

No equiparar reproducibilidad con “corre en mi equipo” ni creer que guardar el modelo basta. Tampoco almacenar datos sensibles indefinidamente: cuando la retención está restringida se conserva evidencia y metadatos compatibles con privacidad.

### Comprobación

Preguntar qué falta si se conocen código y semilla, pero la API devuelve datos actuales. Falta una instantánea, versión o consulta con corte verificable; repetir el código no reconstruye la entrada original.

**Transición sugerida:** “Apliquemos ahora formulación, procedencia y reproducibilidad a una sola cadena de movilidad”.

## Diapositivas 29-30. Caso transversal de movilidad

**Correspondencia con el libro:** capítulo 1, §1.1.6; capítulo 2, §§2.1.3, 2.1.4 y 2.3.8.

### Qué exponer

La diapositiva 29 formula: usuario, operaciones; unidad, zona-franja; población, cobertura declarada; horizonte, treinta minutos; resultado, demanda y demora; acciones, mantener o mover; restricciones, capacidad, traslado, cobertura, seguridad y aprobación.

La diapositiva 30 muestra: datos antes del corte, modelo, evaluación como evidencia, regla, recomendación, aprobación humana, ejecución y monitoreo. Mantener cada frontera visible.

### Fórmulas e interpretación

Aplicar $P=(U,R,O,X,Y,A,H,C)$ al caso y recordar que $P(Y\mid X)$ estima, no decide. La recomendación podría maximizar utilidad esperada entre planes factibles, mientras una cobertura mínima pertenece a $C$ y no debe compensarse con menor demora promedio.

### Ejemplo de movilidad

A las 17:00 se estima 18:00-19:00 y se propone mover uno, no dos, para conservar cobertura. Operaciones incorpora un evento nuevo, modifica y registra motivo.

### Recorrido visual

En la ficha, recorrer objetivo, unidad, población, horizonte, entradas, resultado, acciones y restricciones. En el flujo, comenzar en el reloj de corte, seguir hasta recomendación y detenerse ante la figura humana. Mostrar ramas aprobar, modificar, rechazar y abstenerse. La retroalimentación vuelve a datos y evaluación, pero no borra quién decidió.

### Error frecuente o advertencia

No escribir “el algoritmo reasigna vehículos” si solo recomienda. No usar una unidad viaje cuando la acción y el impacto se miden por zona sin explicar agregación. No mezclar información retrospectiva corregida con la disponible en línea.

### Comprobación

Preguntar qué debe registrarse si operaciones rechaza. Predicción, versión, evidencia presentada, propuesta, motivo, decisión humana, acción efectiva y resultado; el rechazo puede revelar información no capturada o una interfaz inadecuada.

**Transición sugerida:** “La misma necesidad admite tareas distintas; debemos separarlas y comprobar que cada una use solo información legítimamente disponible”.

## Diapositivas 31-32. Tareas concretas y fuga de información

**Correspondencia con el libro:** capítulo 1, §§1.1.5 y 1.1.6; capítulo 2, §§2.1.1, 2.1.3, 2.1.4 y tiempo de evento, procesamiento y decisión en §2.3.6.

### Qué exponer

La diapositiva 31 separa descripción, predicción, prescripción y monitoreo, cada una con producto y evaluación propios. Prescribir exige acciones y consecuencias, no solo ranking.

La diapositiva 32 define fuga como usar información no disponible en uso real. `hora_real`, cancelación final o tráfico corregido no anticipan el mismo viaje. Repartir al azar viajes dependientes también contamina.

### Fórmulas e interpretación

Definir un instante de decisión $t_0$ y exigir:

$$
X_i\in\mathcal I(t_0),
$$

donde $\mathcal I(t_0)$ es lo disponible al corte. $Y$ se observa después para evaluar. En flujo se distinguen evento, recepción y decisión.

### Ejemplo de movilidad

Campos válidos incluyen horario, zona, solicitudes previas, clima recibido y tráfico vigente. `hora_real` y cancelación final son posteriores; de datos corregidos debe reconstruirse la versión conocida al corte.

### Recorrido visual

Marcar captura, corte, predicción, acción y $Y$. Una flecha del futuro a entradas es fuga. Recorrer cada tarea hasta su métrica.

### Error frecuente o advertencia

Existencia en el dataset no implica disponibilidad operativa. Un desempeño extraordinario exige auditar fuga, duplicados y particiones.

### Comprobación

Preguntar si puede usarse a las 17:00 un evento ocurrido a las 16:55 pero recibido a las 17:08. No para esa decisión. Puede incorporarse a una reconstrucción retrospectiva solo si se mantiene separada de la información en línea.

**Transición sugerida:** “La actividad integrará estas distinciones en una ficha breve que otro equipo pueda revisar”.

## Diapositiva 33. Actividad guiada: ficha del problema

**Correspondencia con el libro:** capítulo 1, §1.1.6 y actividad de reflexión; capítulo 2, §§2.1.1-2.1.5 y §2.3.8. La actividad adapta esos contenidos al caso de movilidad; no reproduce una actividad titulada del libro.

### Qué exponer y organizar

Asignar 30 minutos de construcción y 10 de contraste, incluida una defensa de un minuto por equipo. Se diseña una ficha para movilidad de la próxima franja, sin elegir algoritmo.

### Producto esperado

Una página, legible y versionada, que contenga:

1. necesidad observable, beneficio y personas afectadas;
2. usuario y autoridad: quién interpreta, aprueba y ejecuta;
3. especificación $P=(U,R,O,X,Y,A,H,C)$;
4. una pregunta descriptiva, una predictiva y una prescriptiva;
5. separación explícita entre modelo, evidencia, decisión y autoridad humana;
6. inventario mínimo de fuentes con unidad, frecuencia, cobertura, procedencia y reloj;
7. baseline operativo y criterios técnico, operativo y de riesgo;
8. declaración de generalización y exclusiones;
9. una variable que produciría fuga y explicación temporal;
10. condición de abstención, detención o retorno a formulación.

### Ejemplo mínimo

**Necesidad:** reducir espera en A y B. **Unidad:** zona-franja. **Población:** días laborables y zonas cubiertas. **Autoridad:** operaciones. **Entradas:** solicitudes y vehículos recibidos antes de 17:00. **Resultado:** demanda 17:00-17:30. **Acción:** mantener o mover uno. **Restricción:** un vehículo libre por zona. **Baseline:** solicitudes previas. **Valor:** P90 sin más cancelaciones. **Fuga:** solicitudes posteriores. **Abstención:** GPS menor de 80 %.

### Tres escenarios obligatorios

- **Normal:** fuentes oportunas y cobertura suficiente; mostrar evidencia, recomendación y aprobación.
- **Información incompleta:** GPS tardío en 30 %; ajustar alcance, usar baseline o abstenerse.
- **Cambio adverso:** cierre vial posterior; explicar caducidad, revisión y retorno seguro.

### Fórmulas e interpretación

Usar $P$ y una conexión: $P(Y\mid X)$, utilidad esperada o $J(m)$. Se evalúa interpretación, no cantidad de fórmulas.

### Recorrido visual del producto

Recorrer necesidad, formulación, fuentes, modelo, evidencia, acciones, autoridad, criterios y retorno. Las flechas muestran tiempo sin atribuir ejecución al predictor.

### Error frecuente o advertencia

Si comienzan por algoritmos, preguntar quién decide, sobre qué unidad y con qué consecuencia. “Supervisión humana” debe nombrar persona, información y autoridad.

### Comprobación

Antes del intercambio, cada equipo debe responder en veinte segundos: “¿Qué cambia en el mundo si nuestra evidencia es distinta?”. Si la acción no cambia, la conexión con decisión aún no está formulada.

**Transición sugerida:** “La revisión no premiará complejidad; comprobará que no existan saltos entre necesidad, evidencia, acción y responsabilidad”.

## Diapositiva 34. Criterios y rúbrica de revisión

**Correspondencia con el libro:** capítulo 2, método de revisión de la pregunta en §2.1.1, objetivos en §2.1.2, §2.1.5 y criterios de aprobación de la actividad EMO [AGUA-01].

### Qué exponer

La revisión marca una fortaleza, un supuesto no demostrado y una corrección prioritaria, y registra su aceptación o rechazo.

### Rúbrica

| Criterio | 2: logrado | 1: parcial | 0: ausente o incoherente |
|---|---|---|---|
| Formulación | $U,R,O,X,Y,A,H,C$ definidos y compatibles | Hay ambigüedad menor | Faltan elementos críticos o se contradicen |
| Temporalidad y fuga | Corte explícito; entradas disponibles; fuga identificada | Disponibilidad incompleta | Usa información futura o no hay reloj |
| Evidencia y decisión | Separa modelo, evidencia, regla y acción | Separación implícita | La predicción aparece como decisión automática |
| Autoridad y afectados | Aprueba, ejecuta, revisa y afectados están identificados | Solo se nombra un “usuario” | Se atribuye responsabilidad al modelo |
| Datos y alcance | Fuentes, procedencia, población y exclusiones claros | Inventario parcial | Se supone cobertura universal |
| Criterios y baseline | Integra técnica, utilidad, riesgo y referencia real | Métrica o baseline débil | Solo propone exactitud o no compara |
| Escenarios y seguridad | Responde a los tres escenarios y puede abstenerse | Respuesta genérica | No contempla fallos ni retorno seguro |

**Puntaje:** 11-14, defendible; 7-10, corregir; 0-6, reformular. No compensa restricciones críticas.

### Fórmulas e interpretación

$J(m)=w_1Q-w_2C-w_3R$ recuerda criterios múltiples; una violación dura sigue siendo inaceptable. Se evalúa formulación, no un modelo inexistente.

### Ejemplo de movilidad

Una ficha coherente es inaceptable si deja una zona sin cobertura; un baseline simple es válido con alcance, reloj y autoridad claros.

### Error frecuente o advertencia

No compensar fuga o falta de autoridad con puntos, ni penalizar una abstención justificada.

### Comprobación

Presentar una ficha con alta precisión esperada, pero sin baseline ni usuario capaz de actuar. Pedir puntuación y diagnóstico. Debe bajar en evidencia-decisión y criterios; no es suficiente afirmar que el modelo sería bueno.

**Transición sugerida:** “La defensa mostrará si las elecciones de la ficha resisten preguntas sobre tiempo, alcance y responsabilidad”.

## Diapositiva 35. Defensa y contraste

**Correspondencia con el libro:** capítulo 2, preguntas para la defensa de la actividad EMO [AGUA-01], §2.2.5 sobre responsabilidad y revisión, y §2.2.4 sobre hipótesis operativas.

### Qué exponer y organizar

Cada equipo presenta decisión, unidad, valor y supuesto riesgoso; luego responde dos preguntas. Debe justificar una elección y reconocer un límite.

Preguntar por variable posterior, cambio de unidad, población excluida, baseline real, rechazo humano, falta de GPS, detención, reconstrucción o retroalimentación sobre tráfico.

### Fórmulas e interpretación

Para $P(Y\mid X)$ exigir resultado, instante y población; para utilidad, acciones y consecuencias; para $J(m)$, pesos y restricciones.

### Ejemplo de movilidad

Defensa mínima: “Elegimos zona-franja porque allí se reasigna; estimamos la franja siguiente con datos al corte; operaciones aprueba; con GPS bajo 80 % usamos baseline; no evaluamos emergencias”.

### Recorrido visual

Mantener unidad, reloj, acción y autoridad. Mover el supuesto riesgoso a “evidencia siguiente”.

### Error frecuente o advertencia

No premiar incertidumbre oculta. Un límite explícito es mejor que generalización; revisión humana exige capacidad de detener.

### Comprobación

Cerrar cada defensa preguntando: “¿Qué evidencia mínima buscarían a continuación?”. La respuesta debe ser un artefacto evaluable, por ejemplo perfil de cobertura o prueba de integración, no “entrenar un modelo más complejo”.

**Transición sugerida:** “Las defensas muestran que la calidad comienza en la representación del problema y se conserva durante todo el ciclo”.

## Diapositivas 36-37. Síntesis conceptual y operativa

**Correspondencia con el libro:** capítulo 1, síntesis; capítulo 2, síntesis del capítulo.

### Qué exponer

La diapositiva 36 recupera que los datos son parciales, las tareas difieren, $P(Y\mid X)$ no decide y las fronteras deben permanecer explícitas.

La diapositiva 37 integra formulación, unidad, población, reloj, metodologías, procedencia, seis V, reproducibilidad, baseline, utilidad y riesgo.

Volver a la apertura y transformar “datos y modelo” en usuario, unidad, horizonte, acción, criterios y límites.

### Fórmulas e interpretación

Mostrar una secuencia integrada, sin derivarla de nuevo:

$$
P=(U,R,O,X,Y,A,H,C),\qquad
P(Y\mid X),\qquad
a^*=\arg\max_a E[U(a,S)\mid X].
$$

La primera especifica, la segunda estima y la tercera compara acciones. Entre ellas se necesitan procedencia, evaluación, restricciones y autoridad. Si $P_T\neq P_D$, la evidencia puede no transferirse.

### Ejemplo de movilidad

La tabla representa, el modelo estima, la evaluación valida, la regla recomienda, operaciones aprueba y el monitoreo puede devolver el proyecto a etapas anteriores.

### Recorrido visual

En la diapositiva 36 recorrer cinco cajas y detenerse entre modelo y evidencia, y entre recomendación y autoridad. En la 37 recorrer el ciclo completo y señalar el reloj transversal: cada dato, salida y acción tiene un instante. Terminar en evaluación y seguir la flecha de retorno hasta problema.

### Error frecuente o advertencia

No cerrar con una lista de herramientas. Python y R son medios dentro del ciclo. Tampoco afirmar que toda decisión debe automatizarse o que más datos siempre mejoran evidencia.

### Comprobación

Solicitar una frase final: “Un proyecto de datos es...”. Respuesta esperada en contenido: proceso reproducible que transforma observaciones situadas en evidencia evaluada para apoyar una decisión bajo objetivos, restricciones y responsabilidad.

**Transición sugerida:** “Las lecturas permiten profundizar primero definición y formulación, y después metodologías, fuentes y reproducibilidad”.

## Diapositiva 38. Lecturas y continuidad

**Correspondencia con el libro:** capítulo 1, propósito, §§1.1.1, 1.1.4-1.1.6 y síntesis; capítulo 2, propósito, §§2.1-2.4 y síntesis.

### Qué exponer

Orientar: capítulo 1, §§1.1.1 y 1.1.4-1.1.6 para definición, tipos y movilidad; capítulo 2, §2.1 para formulación, §2.2 metodologías, §2.3 fuentes y seis V, y §2.4 reproducibilidad.

Incorporar una corrección prioritaria y registrar cómo cambia la validez. Conservar la versión previa y no agregar algoritmos.

### Fórmulas e interpretación

No hay fórmula nueva. Releer especificación, predicción, utilidad, costos, cambio de distribución y multicriterio explicando sus supuestos.

### Ejemplo de movilidad

Corregir “toda la ciudad” a “zonas cubiertas en días laborables” o usar partición temporal vuelve evaluable la afirmación.

### Recorrido visual

Recorrer la diapositiva de arriba hacia abajo: lectura conceptual, lectura metodológica, caso aplicado y producto revisado. Señalar los enlaces relativos, que permiten consultar las fuentes desde el directorio de la clase.

### Error frecuente o advertencia

No sustituir el producto de la clase por un cuestionario. La evidencia de aprendizaje es la ficha revisada y su defensa. No inventar subsecciones: usar las denominaciones y numeración indicadas en los capítulos.

### Comprobación y cierre

Pedir que cada equipo nombre la sección que consultaría para resolver su corrección: §2.1.3 para población, §2.3.8 para inventario de movilidad o §2.4 para reproducibilidad. Cerrar con la idea: “Primero se diseña la pregunta y su uso; después se decide qué datos y métodos necesita”.

## Referencias

- `../../../Libro/Capitulo_01_Ciencia_de_Datos_e_IA.md`
- `../../../Libro/Capitulo_02_Ciclo_de_vida_de_un_proyecto_de_datos.md`
- `Clase_01_Introduccion_a_la_Ciencia_de_Datos.md`
- `Clase_01_Introduccion_a_la_Ciencia_de_Datos.pdf`
