# Capitulo 6. Agentes inteligentes y representacion de problemas

## 6.1. Agentes y racionalidad

Un agente percibe mediante sensores y actua mediante actuadores. Su funcion `f: P* -> A` transforma una historia de percepciones en una accion. Un programa implementa esa funcion con memoria y conocimiento limitados. La racionalidad maximiza desempeño esperado considerando informacion, costo y horizonte.

### 6.1.7. Ejemplo practico guiado

Definir un agente de red de agua: percepciones, acciones, objetivo, estado interno, medida de desempeño y fallas seguras.

## 6.2. Entornos de tarea

PEAS resume desempeño, entorno, actuadores y sensores. Observabilidad, determinismo, episodicidad, dinamismo, continuidad y numero de agentes determinan que arquitectura es adecuada. La clasificacion no es absoluta: depende del nivel de descripcion.

### 6.2.8. Ejemplo practico guiado

Caracterizar un recomendador de rutas con PEAS y señalar por que el trafico lo vuelve estocastico, dinamico y parcialmente observable.

## 6.3. Arquitecturas de agentes

Los agentes reactivos aplican reglas; los basados en modelo mantienen estado; los orientados a objetivos buscan planes; los basados en utilidad comparan consecuencias; los que aprenden modifican su comportamiento con experiencia. Separar percepcion, estado, razonamiento, aprendizaje y accion facilita pruebas.

### 6.3.7. Ejemplo practico guiado

Diseñar tres agentes para inspeccion de tuberias y comparar autonomia, explicabilidad, costo y respuesta a informacion nueva.

## 6.4. Representacion computacional de problemas

Un problema se representa como `P=(S,A,T,s0,G,C)`: estados, acciones, transicion, estado inicial, objetivos y costos. La abstraccion elimina detalles irrelevantes, pero no puede eliminar restricciones que cambien la solucion.

### 6.4.7. Ejemplo practico guiado

Modelar asignacion de inspectores como estados de tareas pendientes, acciones de asignacion, restricciones de horario y costo total. Validar que toda accion produzca un estado legal.

## Sintesis

La inteligencia de un agente depende de como representa percepciones, acciones, objetivos y consecuencias. Una buena representacion reduce complejidad sin ocultar decisiones relevantes.
