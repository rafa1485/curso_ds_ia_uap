# Capitulo 4. Estadistica descriptiva, exploracion y visualizacion

## 4.1. Descripcion de una variable

Una poblacion tiene parametro; una muestra tiene estadistico. La media `x_barra = (1/n) sum x_i` es sensible a extremos; la mediana y los cuantiles son robustos. La varianza muestral es `s^2 = sum(x_i-x_barra)^2/(n-1)` y el rango intercuartilario es `IQR = Q3-Q1`.

La asimetria describe colas desiguales y la curtosis concentra informacion sobre extremos. Ninguna medida resume por completo una distribucion.

### 4.1.8. Ejemplo practico guiado

Construir el perfil del consumo de agua por periodo: tamaño, faltantes, mediana, cuantiles, dispersion y observaciones extremas. Comparar grupos solo si sus unidades y cobertura son equivalentes.

### Actividad EMO [AGUA-03]

Elaborar al menos tres visualizaciones, tres hallazgos cuantificados y una advertencia de causalidad o sesgo. Distinguir atipico estadistico, error y evento que requiere investigacion.

## 4.2. Relaciones entre variables

La covarianza mide variacion conjunta; la correlacion lineal `r = cov(X,Y)/(s_X s_Y)` esta acotada entre -1 y 1. Correlaciones de rango pueden ser preferibles ante relaciones monotónicas no lineales. Una asociacion no prueba causalidad: confusores, seleccion y temporalidad pueden producirla.

### 4.2.8. Ejemplo practico guiado

Explorar retrasos segun horario, clima, recorrido y demanda. Separar descripcion de mecanismo causal y declarar variables no observadas que podrian explicar el patron.

## 4.3. Visualizacion exploratoria

Histogramas y densidades muestran forma; cajas muestran posicion y dispersion; barras comparan categorias; dispersion examina relaciones; mapas y series agregan espacio y tiempo. El eje, la escala, la granularidad y los valores faltantes deben quedar visibles.

![Ciclo de trabajo de datos](imagenes/ciclo_vida_datos.png)

### 4.3.9. Ejemplo practico guiado

Construir un panel de movilidad con una vista temporal, una espacial y una distribucion por grupo. Cada grafico debe responder una pregunta y tener una interpretacion limitada a su evidencia.

### Actividad EMO [MOV-01]

Preparar datos geotemporales, mapear intensidad, detectar dos patrones y una observacion atipica. La unidad espacial y temporal, cobertura y posibles sesgos deben documentarse.

## 4.4. Comunicacion de resultados

Comunicar exige una pregunta, evidencia y mensaje principal. La eleccion grafica depende de comparar, distribuir, relacionar o localizar. Un dashboard no reemplaza una explicacion: debe indicar filtros, definiciones, fecha de actualizacion, incertidumbre y accesibilidad.

### 4.4.8. Ejemplo practico guiado

Transformar un hallazgo exploratorio en una pagina ejecutiva: titulo con conclusion, grafico principal, contexto, limitacion y accion sugerida. Evitar escalas truncadas que exageren diferencias.

## Sintesis

La exploracion describe patrones y genera hipotesis. La visualizacion es parte del razonamiento, pero no convierte asociacion en causalidad ni reemplaza el conocimiento del dominio.
