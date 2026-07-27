# Capitulo 14. Analisis y pronostico de series temporales

## 14.1. Estructura de las series

Una serie es una secuencia indexada por tiempo. Puede descomponerse como `y_t=T_t+S_t+R_t` o multiplicativamente. Tendencia, estacionalidad, ciclos, ruido, faltantes y atipicos deben distinguirse antes de pronosticar.

### 14.1.8. Ejemplo practico guiado

Descomponer demanda y discutir que componentes son predecibles y cuales reflejan shocks.

## 14.2. Dependencia y estacionariedad

Autocorrelacion mide relacion entre `y_t` y `y_{t-k}`; autocorrelacion parcial elimina rezagos intermedios. Una serie estacionaria mantiene propiedades distribucionales en el tiempo. Diferenciar, transformar varianza y retirar estacionalidad son operaciones que deben aprenderse solo con pasado.

### 14.2.7. Ejemplo practico guiado

Aplicar transformaciones, observar autocorrelaciones y comprobar si el cambio mejora estabilidad y validacion futura.

## 14.3. Modelos ARIMA

AR(p) usa rezagos; MA(q) usa errores pasados; ARMA combina ambos; ARIMA agrega diferenciacion y SARIMA componentes estacionales. Un esquema AR es `y_t=c+sum phi_i y_{t-i}+epsilon_t`; variables exogenas agregan informacion disponible al pronosticar. Residuos deben aproximarse a ruido no autocorrelacionado.

### 14.3.9. Ejemplo practico guiado

Pronosticar consumo de agua con ARIMA o SARIMA, revisar residuos y producir intervalos, no solo una linea puntual.

## 14.4. Evaluacion de pronosticos

El horizonte define dificultad. MAE y RMSE miden error; MAPE falla con ceros. La validacion walk-forward entrena con pasado y prueba el siguiente bloque. Un baseline estacional es obligatorio cuando existe periodicidad.

### 14.4.8. Ejemplo practico guiado

Comparar baseline, ARIMA y aprendizaje automatico con particiones temporales identicas y metricas por horizonte.

### Actividad EMO [MOV-04]

Construir serie regular por zona, definir horizonte, comparar baseline con un modelo temporal mediante walk-forward e interpretar intervalos y errores.

## Sintesis

El tiempo impone orden, dependencia y disponibilidad progresiva. Un pronostico valido no utiliza futuro ni oculta su incertidumbre.
