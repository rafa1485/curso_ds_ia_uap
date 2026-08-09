---
title: "Fundamentos de Inteligencia Artificial"
subtitle: "Enfoques, agentes y racionalidad"
course: "Inteligencia Artificial"
week: 1
class: 1
language: es
---

# Fundamentos de Inteligencia Artificial

## Enfoques, agentes y racionalidad

**Semana 1 · Clase 1**

<!-- Notas docentes:
Introducir la IA como estudio y construcción de sistemas orientados a objetivos, no como sinónimo de aprendizaje automático ni como afirmación de conciencia.
-->

---

# Propósito de la clase

Comprender distintas formas de definir la Inteligencia Artificial y utilizarlas para especificar un agente situado en un entorno.

Al finalizar, podremos:

- distinguir los cuatro enfoques clásicos de la IA;
- reconocer hitos, continuidades y límites de su evolución;
- explicar agente, percepción, acción y racionalidad;
- especificar una tarea mediante PEAS;
- caracterizar el ambiente de un agente de movilidad urbana.

---

# Pregunta de apertura

> ¿Cuándo podemos afirmar que un sistema se comporta de manera inteligente?

Posibles criterios:

- ¿Imita correctamente a una persona?
- ¿Utiliza procesos similares al pensamiento humano?
- ¿Deriva conclusiones válidas?
- ¿Elige acciones adecuadas para sus objetivos?

**La respuesta depende del criterio de inteligencia que adoptemos.**

<!-- Notas docentes:
Solicitar un ejemplo conocido por cada criterio. No intentar consensuar una única definición todavía.
-->

---

# ¿Qué estudia la Inteligencia Artificial?

La IA estudia la construcción de sistemas capaces de:

`percibir · representar · razonar · aprender · planificar · comunicar · actuar`

En sentido técnico, “inteligente” significa que el sistema transforma información en comportamiento dirigido a un objetivo bajo ciertas condiciones.

No implica necesariamente:

- conciencia;
- comprensión humana general;
- intenciones propias;
- autonomía completa.

---

# IA, aprendizaje automático y Ciencia de Datos

- La **IA** construye sistemas que perciben, razonan, aprenden o actúan.
- El **aprendizaje automático** ajusta funciones o políticas desde datos o experiencia.
- La **Ciencia de Datos** organiza procesos para producir evidencia y apoyar decisiones.

Relaciones importantes:

- Puede existir IA basada en reglas sin aprendizaje automático.
- Puede existir análisis predictivo sin un agente autónomo.
- Un sistema de IA puede combinar reglas, búsqueda, probabilidad y aprendizaje.

---

# Cuatro enfoques clásicos

| | Como humanos | Racionalmente |
|---|---|---|
| **Pensar** | Modelado cognitivo | Leyes del pensamiento |
| **Actuar** | Test de Turing | Agente racional |

Cada enfoque responde una pregunta diferente:

- ¿Qué conducta observamos?
- ¿Qué proceso produce la respuesta?
- ¿La inferencia es válida?
- ¿La acción mejora el desempeño esperado?

---

# Actuar como humanos

Evalúa la **conducta observable** del sistema en una tarea definida.

Puede considerar:

- conversación y uso del lenguaje;
- percepción de imágenes o sonidos;
- movimiento y manipulación;
- adaptación a situaciones de interacción.

Ventaja: permite evaluar resultados sin definir qué ocurre internamente.

Límite: imitar una respuesta no demuestra comprensión ni confiabilidad.

---

# El test de Turing

Una persona conversa mediante un canal textual con interlocutores ocultos e intenta distinguir a la máquina de la persona.

## Aporte histórico

Desplaza la pregunta “¿puede pensar una máquina?” hacia una prueba de comportamiento.

## Límites

- Evalúa una interacción particular, no inteligencia general.
- No garantiza verdad, seguridad ni comprensión causal.
- Puede favorecer imitación, evasión o respuestas plausibles.
- No evalúa necesariamente percepción física o planificación prolongada.

---

# Pensar como humanos

Busca modelar procesos de la cognición:

`percepción · memoria · aprendizaje · lenguaje · razonamiento`

La evaluación observa no solo la respuesta final, sino también:

- tiempos de respuesta;
- secuencia de pasos;
- patrones de error;
- reacción ante información nueva.

Resolver correctamente una tarea no demuestra que se utilizó un proceso humano.

---

# Pensar racionalmente

Consiste en derivar conclusiones válidas desde premisas y reglas.

Ejemplo de inferencia:

```text
Si hay congestión, aumenta el tiempo de viaje.
Hay congestión.
Por lo tanto, aumenta el tiempo de viaje.
```

Fortaleza: premisas, reglas y conclusiones pueden inspeccionarse.

Límite: el mundo real contiene observaciones incompletas, ruido, ambigüedad y excepciones.

---

# Razonar bajo incertidumbre

La lógica clásica trabaja con proposiciones verdaderas o falsas. La probabilidad permite representar grados de creencia:

`P(estado | evidencia)`

Ejemplo:

`P(congestión | velocidad, hora, zona) = 0,75`

La evidencia puede modificar nuestras creencias, pero aún falta decidir:

- ¿Qué acciones están disponibles?
- ¿Qué consecuencias tiene cada acción?
- ¿Qué errores son más costosos?

---

# Actuar racionalmente

Un sistema actúa racionalmente cuando selecciona la acción con mejor desempeño esperado según:

- sus percepciones y conocimiento;
- los objetivos definidos;
- las acciones disponibles;
- los costos y restricciones;
- el tiempo y los recursos de cómputo.

`a* = argmax_a E[U(a, S) | evidencia]`

La acción racional depende de la información disponible, no de conocer el futuro con certeza.

---

# Racionalidad no es perfección

Un agente racional:

- puede equivocarse bajo incertidumbre;
- no conoce aquello que no puede observar;
- dispone de recursos limitados;
- puede obtener información antes de actuar;
- evalúa resultados esperados, no garantías absolutas.

Un agente puede ejecutar perfectamente una función mal definida.

> Optimizar rapidez solamente puede producir respuestas rápidas pero incorrectas.

---

# Fundamentos de la IA

| Fundamento | Aporte |
|---|---|
| Filosofía | Razón, conocimiento, experiencia y consecuencias |
| Lógica | Representación explícita e inferencia |
| Probabilidad | Incertidumbre y actualización de creencias |
| Teoría de decisión | Utilidad, costos y elección de acciones |
| Optimización | Selección de parámetros, planes o políticas |
| Matemática | Álgebra lineal, cálculo e información |
| Computación | Algoritmos, memoria, complejidad y sistemas |

---

# Anatomía de un sistema inteligente

Una arquitectura completa suele incluir:

1. percepción o entrada de datos;
2. representación interna;
3. memoria o estado;
4. inferencia, búsqueda o aprendizaje;
5. evaluación de acciones;
6. ejecución y retroalimentación.

Separar componentes ayuda a localizar fallos:

`¿falló la percepción, la representación, la predicción o la decisión?`

---

# Evolución: ideas, recursos y expectativas

| Periodo | Enfoque destacado | Limitación visible |
|---|---|---|
| Antecedentes | Lógica, probabilidad y algoritmos | Cálculo manual y representación |
| Década de 1950 | Búsqueda y manipulación simbólica | Explosión de estados |
| Sistemas expertos | Reglas y conocimiento de dominio | Adquisición y mantenimiento |
| Resurgimiento estadístico | Aprendizaje desde datos | Calidad, sesgo y generalización |
| Aprendizaje profundo | Representaciones aprendidas | Datos, cómputo y explicabilidad |
| IA generativa | Modelos fundacionales | Veracidad, control y uso responsable |

---

# Nacimiento formal y enfoque simbólico

- La conferencia de Dartmouth de 1956 es un hito nominal del campo.
- Los primeros proyectos abordaron teoremas, juegos y resolución de problemas.
- Los sistemas expertos separaron una base de conocimiento de un motor de inferencia.
- Las representaciones simbólicas permiten inspeccionar entidades, reglas y conclusiones.

Desafíos:

- demasiados estados posibles;
- conocimiento del mundo difícil de codificar;
- reglas costosas de mantener;
- fragilidad ante excepciones no previstas.

---

# Inviernos y resurgimiento estadístico

Los inviernos de la IA estuvieron asociados con:

- promesas desproporcionadas;
- resultados que no generalizaban;
- cómputo y datos insuficientes;
- sistemas frágiles fuera del laboratorio.

El resurgimiento estadístico fue impulsado por:

- datasets más extensos;
- sensores y redes de comunicación;
- almacenamiento más económico;
- procesadores especializados;
- métodos capaces de aprender regularidades.

---

# Deep learning e IA generativa

El aprendizaje profundo combina múltiples capas para aprender representaciones intermedias.

Los modelos fundacionales se preentrenan sobre grandes colecciones y se adaptan a diferentes tareas.

La IA generativa produce nuevas instancias condicionadas por una entrada:

`texto · imágenes · audio · código`

**La fluidez es una propiedad de generación, no una prueba de verdad.**

Se requieren fuentes, validación, límites de uso y supervisión.

---

# El concepto de agente

Un agente:

1. recibe percepciones mediante sensores;
2. mantiene o construye una representación del entorno;
3. selecciona acciones;
4. actúa mediante actuadores;
5. recibe retroalimentación.

Su función transforma una historia de percepciones en una acción:

`f: P* → A`

El programa implementa esa función con memoria, conocimiento y cómputo limitados.

---

# Agente y entorno

```text
          percepciones
Entorno ----------------> Agente
   ^                         |
   |                         |
   +-------------------------+
              acciones
```

Ejemplo de movilidad:

- **sensores:** GPS, reloj, demanda y estado del tráfico;
- **agente:** recomendador de reasignación;
- **actuadores:** mensajes, órdenes o actualización de rutas;
- **entorno:** flota, vías, pasajeros, clima y otros vehículos.

---

# PEAS: especificar la tarea

| Componente | Pregunta |
|---|---|
| **P**erformance | ¿Cómo se mide el desempeño? |
| **E**nvironment | ¿En qué entorno actúa? |
| **A**ctuators | ¿Cómo interviene en el entorno? |
| **S**ensors | ¿Qué puede percibir? |

PEAS evita describir al agente solo por su algoritmo.

> Primero se especifican la tarea y el entorno; después se elige la arquitectura.

---

# Propiedades del ambiente

Un ambiente puede ser:

- totalmente o parcialmente observable;
- determinista o estocástico;
- episódico o secuencial;
- estático o dinámico;
- discreto o continuo;
- de uno o múltiples agentes;
- conocido o desconocido.

La clasificación depende del nivel de descripción y condiciona el diseño del agente.

---

# Ejemplo: recomendador de rutas

| Propiedad | Caracterización | Justificación |
|---|---|---|
| Observabilidad | Parcial | No conoce todos los incidentes ni intenciones |
| Resultado | Estocástico | Una misma acción puede producir tiempos distintos |
| Dependencia | Secuencial | Una ruta actual modifica opciones posteriores |
| Cambio | Dinámico | El tráfico cambia mientras se calcula |
| Estado | Continuo | Tiempo, posición y velocidad varían continuamente |
| Participantes | Multiagente | Interactúa con conductores y otros vehículos |

---

# Caso transversal: movilidad urbana

## Necesidad

Reducir demoras mediante reasignación de vehículos entre zonas.

## Agente propuesto

Un asistente operativo que observa demanda y estado de la flota, compara reasignaciones y recomienda una acción al responsable de operaciones.

## Decisiones iniciales

- ¿Recomienda o ejecuta?
- ¿Cada cuánto vuelve a decidir?
- ¿Puede abstenerse?
- ¿Qué errores requieren intervención humana?

---

# PEAS inicial para movilidad

| Componente | Especificación inicial |
|---|---|
| Desempeño | Demora, cancelaciones, distancia vacía, seguridad y equidad entre zonas |
| Entorno | Vías, zonas, flota, pasajeros, tráfico, clima y regulación |
| Actuadores | Recomendar traslado, asignar vehículo, mantener distribución o alertar |
| Sensores | GPS, viajes activos, demanda, capacidad, tiempo y estado del tráfico |

**Pregunta crítica:** ¿qué ocurre si optimizamos solamente la demora promedio?

---

# Actividad guiada: diseñar el agente

En equipos, completar:

1. propósito y usuario del agente;
2. medida de desempeño con al menos tres criterios;
3. entorno y actores afectados;
4. acciones permitidas y acción de abstención;
5. percepciones disponibles antes de decidir;
6. propiedades del ambiente;
7. un riesgo de optimizar una métrica inadecuada;
8. un mecanismo de supervisión o falla segura.

**Tiempo sugerido:** 30 minutos de trabajo + 10 minutos de contraste.

---

# Criterios de revisión

La especificación es adecuada si:

- las percepciones existen antes de elegir la acción;
- los actuadores pueden producir cambios reales o recomendaciones claras;
- el desempeño combina objetivo, costos y restricciones;
- la caracterización del entorno está justificada;
- se distingue recomendación de ejecución autónoma;
- existe una respuesta segura ante incertidumbre o fallos;
- se identifican responsables y personas afectadas.

**Entregable de semana 1:** sección PEAS de la ficha del proyecto.

---

# Puesta en común

Cada equipo presenta en un minuto:

1. la acción principal del agente;
2. su medida de desempeño;
3. una propiedad crítica del ambiente;
4. una condición en la que debe abstenerse.

Preguntas para contrastar:

- ¿Un resultado racional según la métrica también es aceptable para los usuarios?
- ¿Qué percepción faltante genera más incertidumbre?
- ¿Qué cambia si el agente ejecuta en vez de recomendar?

---

# Síntesis

- “Inteligencia” puede evaluarse como conducta, cognición, inferencia o acción racional.
- El test de Turing evalúa comportamiento, no verdad ni inteligencia general.
- La historia de la IA relaciona representaciones, datos, cómputo y expectativas.
- Un agente transforma percepciones en acciones dentro de un entorno.
- La racionalidad depende de información, objetivos y restricciones.
- PEAS permite especificar una tarea antes de elegir el algoritmo.

---

# Autoevaluación

1. ¿Qué diferencia existe entre actuar como humano y actuar racionalmente?
2. ¿Por qué pensar racionalmente no garantiza actuar correctamente?
3. ¿Qué limitación principal tiene el test de Turing?
4. ¿Qué factores favorecieron el resurgimiento estadístico de la IA?
5. ¿Qué componentes forman una especificación PEAS?
6. ¿Por qué el tráfico constituye un ambiente parcialmente observable y dinámico?
7. ¿Cómo puede un agente ejecutar correctamente una función mal definida?

---

# Lecturas y recursos

## Lectura principal

- [Capítulo 1. Ciencia de Datos e Inteligencia Artificial](../../../Libro/Capitulo_01_Ciencia_de_Datos_e_IA.md): secciones 1.1.2, 1.2 y 1.3.
- [Capítulo 6. Agentes inteligentes y representación de problemas](../../../Libro/Capitulo_06_Agentes_inteligentes_y_representacion_de_problemas.md): secciones 6.1 y 6.2.

## Para continuar

- Revisar el glosario esencial y las preguntas de autoevaluación del capítulo 1.
- Integrar PEAS con la ficha del problema elaborada en Data Science.
