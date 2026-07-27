# Capitulo 11. Regresion y clasificacion: modelos fundamentales

## 11.1. Regresion lineal

La regresion modela `y = beta_0 + sum_j beta_j x_j + epsilon`. Minimos cuadrados resuelve `beta* = argmin_beta ||y-X beta||^2`; con rango completo, `beta=(X'X)^(-1)X'y`. Los coeficientes expresan cambio esperado condicionado a las restantes variables, no causalidad automatica.

### 11.1.7. Ejemplo practico guiado

Predecir demanda o consumo, comparar con media historica y revisar unidades e interpretacion de coeficientes.

## 11.2. Supuestos y diagnostico

Linealidad, independencia, homocedasticidad y residuos razonables permiten interpretar inferencia y errores. Multicolinealidad aumenta inestabilidad; observaciones influyentes pueden dominar ajuste. Graficos de residuos orientan, pero no prueban por si solos los supuestos.

### 11.2.8. Ejemplo practico guiado

Examinar residuos, transformar variables o cambiar especificacion y comprobar si mejora validacion, no solo ajuste interno.

## 11.3. Modelos lineales regularizados

Ridge minimiza `SSE + lambda sum beta_j^2`; Lasso minimiza `SSE + lambda sum|beta_j|`; Elastic Net combina ambas. La estandarizacion es importante y `lambda` se selecciona por validacion. La regularizacion reduce varianza a cambio de sesgo.

### 11.3.7. Ejemplo practico guiado

Comparar coeficientes, error de validacion y estabilidad al variar penalizacion.

## 11.4. Regresion logistica y clasificacion

Para clase binaria, `p(y=1|x)=1/(1+exp(-beta'x))`; `log(p/(1-p))=beta'x`. La probabilidad se convierte en accion mediante umbral. Multiclase puede usar esquemas uno-contra-resto o una salida normalizada. La calibracion verifica si probabilidades de 0.7 ocurren aproximadamente en 70% de casos.

### 11.4.8. Ejemplo practico guiado

Clasificar reclamos prioritarios, evaluar probabilidades, umbral y variables relevantes; incluir abstencion para baja confianza.

## Sintesis

Los modelos lineales son baselines valiosos porque explicitan supuestos, error, regularizacion y efecto de umbrales.
