# Capitulo 9. Formulacion y evaluacion de problemas de aprendizaje automatico

## 9.1. Paradigmas de aprendizaje

El aprendizaje supervisado usa pares `(x,y)`; el no supervisado busca estructura; el semisupervisado combina pocas etiquetas y muchos datos; el autosupervisado construye objetivos desde los propios datos. Regresion predice cantidades, clasificacion categorias y agrupamiento particiones sin etiqueta.

### 9.1.7. Ejemplo practico guiado

Clasificar los cuatro casos del libro por entradas, salida, etiqueta, horizonte, paradigma y riesgo de error.

## 9.2. Ajuste, error y generalizacion

El riesgo empirico es `R_hat(f)=1/n sum L(y_i,f(x_i))`. Sobreajuste ocurre cuando el error de entrenamiento baja pero el de datos nuevos sube; subajuste indica capacidad insuficiente. El compromiso sesgo-varianza explica parte de esa tension. Un baseline cuantifica el valor agregado.

### 9.2.8. Ejemplo practico guiado

Usar curvas de aprendizaje para diagnosticar separadamente capacidad, cantidad de datos y regularizacion.

## 9.3. Diseño de la evaluacion

Entrenamiento ajusta, validacion selecciona y prueba estima desempeño final. La particion debe respetar grupos, tiempo y duplicados. Validacion cruzada no debe romper dependencia temporal ni compartir una misma entidad entre particiones.

### 9.3.8. Ejemplo practico guiado

Elegir particion estratificada para clases desbalanceadas, por grupos para sujetos repetidos y temporal para pronosticos. Fijar semilla y protocolo antes de comparar modelos.

## 9.4. Metricas de desempeño

`MAE=mean|y-y_hat|`, `RMSE=sqrt(mean(y-y_hat)^2)` y `R2=1-SSE/SST`. En clasificacion, TP, FP, TN y FN forman la matriz de confusion; precision es `TP/(TP+FP)`, sensibilidad `TP/(TP+FN)`, especificidad `TN/(TN+FP)` y F1 la media armonica de precision y sensibilidad. ROC-AUC y PR-AUC resumen umbrales, pero no reemplazan costos.

### 9.4.9. Ejemplo practico guiado

Evaluar un clasificador de incidentes y seleccionar umbral mediante matriz de costos.

### Actividad EMO [REC-02]

Definir particiones, baseline, metrica principal, auxiliares, costos y regla de seleccion antes de entrenar el clasificador. Reservar prueba para una unica evaluacion final.

## Sintesis

Evaluar es diseñar una medicion honesta de generalizacion y utilidad, no elegir la metrica que produce el numero mayor.
