# Capitulo 1. Ciencia de Datos e Inteligencia Artificial: conceptos, historia y aplicaciones

## Proposito

La Ciencia de Datos convierte datos en evidencia para comprender fenomenos y decidir. La Inteligencia Artificial construye sistemas capaces de percibir, razonar, aprender o actuar. Son campos relacionados, pero no equivalentes: un informe descriptivo puede ser Ciencia de Datos sin IA, y un agente basado en reglas puede ser IA sin aprender de un dataset.

## 1.1. Ciencia de Datos, Inteligencia Artificial y aprendizaje automatico

La Ciencia de Datos combina dominio, estadistica, computacion y comunicacion. Su objeto no es solo el modelo, sino la cadena completa: pregunta, datos, transformacion, inferencia, decision y evaluacion.

La IA estudia agentes que reciben percepciones y producen acciones para alcanzar objetivos. El aprendizaje automatico estima una funcion a partir de ejemplos, por ejemplo `f: X -> Y`; el aprendizaje profundo usa composiciones de transformaciones parametrizadas. Los modelos descriptivos resumen, los predictivos estiman resultados futuros o no observados y los prescriptivos comparan acciones mediante una funcion de utilidad.

### Formulacion comun

Para observaciones `D = {(x_i, y_i)}`, un modelo se obtiene como:

`theta* = argmin_theta (1/n) sum_i L(y_i, f_theta(x_i)) + lambda Omega(theta)`

La funcion de perdida mide error; `Omega` controla complejidad. La formulacion no decide por si sola si el modelo es util: la utilidad depende del contexto, costos y restricciones.

### 1.1.6. Ejemplo practico guiado

Caso: una empresa de transporte registra viajes. La captura produce observaciones; el analisis descriptivo estima demanda por hora; un modelo predictivo estima viajes de la siguiente franja; una regla prescriptiva asigna vehiculos. Para cada etapa deben explicitarse unidad de analisis, horizonte, informacion disponible y accion resultante.

## 1.2. Enfoques y fundamentos de la Inteligencia Artificial

Los cuatro enfoques clasicos distinguen sistemas que actuan como humanos, piensan como humanos, piensan racionalmente o actuan racionalmente. El test de Turing evalua conducta observable, mientras que el modelado cognitivo intenta representar procesos internos. La logica formal, la teoria de la probabilidad, la optimizacion y la arquitectura de computadores aportan lenguajes distintos para describir inteligencia.

Un agente racional elige la accion que maximiza utilidad esperada con la informacion disponible, no una accion omnisciente. Esta distincion impide confundir buen resultado casual con buen procedimiento.

### 1.2.7. Ejemplo practico guiado

Analizar un asistente de reclamos: describir sus entradas, memoria, criterio de respuesta, accion y medida de desempeno. Separar imitacion conversacional, inferencia, objetivo operativo y riesgos de respuestas no verificadas.

## 1.3. Evolucion historica de la Ciencia de Datos y la IA

La logica y la probabilidad precedieron a los computadores. La IA formal se consolido en la decada de 1950; luego los sistemas expertos representaron conocimiento mediante reglas. Las limitaciones de datos, computo y generalizacion produjeron inviernos de la IA. El resurgimiento estadistico, el almacenamiento distribuido, las GPU y las arquitecturas profundas ampliaron la escala. La IA generativa agrega modelos capaces de producir texto, imagen, audio u otros datos, pero no elimina la necesidad de verificacion.

### 1.3.6. Ejemplo practico guiado

Construir una linea de tiempo con cinco columnas: hito, representacion, datos disponibles, capacidad de computo y limitacion principal. La explicacion historica debe relacionar tecnologia y contexto, no memorizar fechas aisladas.

## 1.4. Aplicaciones, alcances y riesgos

Las aplicaciones pueden asistir diagnosticos, detectar fallas, estimar demanda o priorizar inspecciones. El alcance se limita por cobertura de datos, cambios de distribucion, calidad de etiquetas, costos de error y capacidad de supervision.

Un riesgo debe describirse como una cadena causal: `dato o supuesto -> mecanismo -> dano -> control`. Privacidad, seguridad, sesgo, automatizacion excesiva y opacidad exigen controles tecnicos y organizacionales. La validacion debe incluir casos fuera del promedio y grupos afectados.

### 1.4.7. Ejemplo practico guiado

Completar una ficha con beneficio, usuarios, afectados, datos, decisiones automatizadas, falsos positivos, falsos negativos, mecanismo de apelacion y condicion de suspension. Una aplicacion responsable define tambien lo que el sistema no puede decidir.

## Sintesis

La IA es una forma de construir agentes o sistemas inteligentes; la Ciencia de Datos organiza evidencia para explicar, predecir y decidir. En ambos casos, la pregunta, la incertidumbre y la responsabilidad son parte del metodo.
