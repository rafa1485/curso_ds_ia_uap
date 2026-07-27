# Capitulo 10. Ingenieria, seleccion y reduccion de atributos

## 10.1. Ingenieria de caracteristicas

Una caracteristica es una representacion medible de una observacion. Transformaciones temporales, espaciales, categoricas e interacciones deben estar disponibles en el momento de prediccion. El conocimiento del dominio orienta hipotesis, pero no garantiza validez.

### 10.1.8. Ejemplo practico guiado

Crear atributos de hora, dia, zona, distancia y demanda previa para transporte, cuidando que ningun atributo use viajes futuros.

## 10.2. Seleccion de atributos

Filtros usan asociacion independiente; envolventes prueban subconjuntos con un modelo; embebidos seleccionan durante el ajuste. L1 penaliza suma de valores absolutos y puede producir ceros; L2 penaliza cuadrados y estabiliza coeficientes correlacionados. La seleccion debe ocurrir dentro de cada particion de validacion.

### 10.2.8. Ejemplo practico guiado

Comparar relevancia, redundancia, estabilidad y utilidad de variables de calidad del agua; no interpretar importancia como causalidad.

## 10.3. Reduccion de dimensionalidad

PCA centra datos y busca direcciones ortogonales de maxima varianza. Si `X` es la matriz centrada, los autovectores de `X'X` forman componentes. La proporcion de varianza explicada por componente `j` es `lambda_j/sum lambda`. Alta varianza no implica alta relevancia predictiva.

### 10.3.8. Ejemplo practico guiado

Proyectar un dataset, elegir componentes por varianza y revisar si las cargas son interpretables.

## 10.4. Pipelines de representacion y modelado

Un pipeline separa columnas numericas, categoricas y textuales, ajusta transformaciones con entrenamiento y persiste el mismo esquema para inferencia. La busqueda de hiperparametros debe estar anidada en el protocolo de evaluacion.

### 10.4.7. Ejemplo practico guiado

Integrar imputacion, codificacion, escalado, seleccion y estimacion; registrar transformaciones y version de datos.

## Sintesis

Representar mejor los datos puede aportar mas que elegir un modelo mas complejo. Toda caracteristica debe tener disponibilidad, significado, estabilidad y control de fuga.
