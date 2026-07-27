# Capitulo 3. Preparacion, calidad y transformacion de datos

## 3.1. Comprension y evaluacion de la calidad

Una tabla se interpreta mediante filas, columnas, claves y granularidad. Tipos nominales, ordinales, discretos y continuos admiten operaciones diferentes. Exactitud, completitud, consistencia, unicidad, actualidad y validez deben evaluarse con reglas explicitas.

Un perfil puede expresarse como `Q = (faltantes, duplicados, rango, unicidad, consistencia, actualidad)`. Un diccionario documenta significado, unidad, dominio permitido, origen y momento de disponibilidad.

### 3.1.7. Ejemplo practico guiado

Auditar un dataset: identificar esquema, contar faltantes, comprobar claves, resumir rangos y contrastar limites del dominio. Cada hallazgo debe distinguir error de registro, ausencia y evento real.

## 3.2. Limpieza de datos

Los faltantes pueden ser completamente aleatorios, depender de variables observadas o depender del valor ausente. Eliminar, imputar o conservar un indicador de ausencia es una decision que debe justificarse. Los atipicos requieren contexto: un valor extremo puede ser una falla o el fenomeno de interes.

Para una imputacion por media de entrenamiento: `x'_ij = mean({x_kj: k en train, x_kj observado})`. Nunca se calcula con validacion o prueba. La deteccion por rango intercuartil usa `Q1 - 1.5 IQR` y `Q3 + 1.5 IQR`, como señal, no como sentencia de error.

### 3.2.7. Ejemplo practico guiado

En mediciones de presion y caudal, aplicar reglas fisicas, revisar unidades, conservar una marca de correccion y comparar antes/despues. Los eventos plausibles deben quedar para investigacion.

### Actividad EMO [AGUA-02]

Perfilar mediciones, identificar faltantes, duplicados, unidades, imposibles y atipicos; aplicar limpieza e imputacion sin usar el futuro ni prueba. Entregar notebook, tabla de reglas y comparacion antes/despues.

## 3.3. Integracion y transformacion

Filtrar conserva una condicion; unir relaciona claves; agregar cambia granularidad. Las uniones uno-a-muchos pueden duplicar observaciones sin advertencia. La codificacion categorica, la estandarizacion `z = (x - mu)/sigma`, las transformaciones logaritmicas y la discretizacion deben responder al modelo y al dominio.

### 3.3.9. Ejemplo practico guiado

Integrar reclamos con contexto temporal y geográfico, comprobando cardinalidad, cobertura de claves y procedencia de cada columna.

### Actividad EMO [REC-01]

Construir corpus con identificador, texto, etiqueta y variables permitidas. Documentar duplicados, campos que filtran la respuesta, faltantes y procedencia. La reconstruccion desde originales debe producir el mismo corpus.

## 3.4. Pipelines y prevencion de fugas

Un pipeline encadena transformaciones y estimador. Las operaciones que aprenden parametros se ajustan solo con entrenamiento. La fuga ocurre cuando informacion de validacion, prueba o futuro influye en el ajuste.

Pseudocodigo seguro:

```text
separar train, validacion y prueba
ajustar transformaciones con train
transformar train, validacion y prueba usando esos parametros
ajustar modelo con train transformado
seleccionar con validacion
evaluar una sola vez en prueba
```

### 3.4.7. Ejemplo practico guiado

Comparar el calculo incorrecto de un escalador sobre toda la tabla con un pipeline que aprende media y desviacion solo en entrenamiento. Documentar que columnas y parametros se ajustan en cada etapa.

## Sintesis

Preparar datos significa preservar significado y procedencia mientras se hace posible el analisis. La calidad no se corrige con una unica operacion y la ausencia de fuga es una propiedad del proceso completo.
