# Capitulo 5. Probabilidad, incertidumbre e inferencia bayesiana

## 5.1. Fundamentos de probabilidad

Un experimento tiene espacio muestral `Omega`; un evento es un subconjunto. Los axiomas son `P(Omega)=1`, `P(A)>=0` y aditividad para eventos disjuntos. `P(A union B)=P(A)+P(B)-P(A intersection B)` y `P(A|B)=P(A intersection B)/P(B)`.

### 5.1.7. Ejemplo practico guiado

Estimar incidentes de transporte por turno usando frecuencias conjuntas y condicionales. Revisar denominadores y no confundir `P(A|B)` con `P(B|A)`.

## 5.2. Variables aleatorias y distribuciones

Una variable aleatoria asigna valores a resultados. La esperanza `E[X]` y la varianza `Var(X)=E[(X-E[X])^2]` resumen posicion y dispersión. Bernoulli, binomial, Poisson, normal y exponencial son modelos utiles bajo supuestos diferentes. Distribuciones conjuntas permiten estudiar dependencia; marginalizar suma o integra variables.

### 5.2.8. Ejemplo practico guiado

Comparar una distribucion Poisson de fallas con frecuencias observadas y evaluar si la tasa parece constante. Un modelo plausible no queda validado solo por su forma conocida.

## 5.3. Teorema de Bayes e inferencia probabilistica

`P(H|E) = P(E|H) P(H) / P(E)`. La previa expresa conocimiento anterior, la verosimilitud compatibilidad de evidencia y la posterior la creencia actualizada. Con varias evidencias, la actualizacion secuencial exige declarar si son condicionalmente independientes.

![Actualizacion bayesiana](imagenes/actualizacion_bayesiana.png)

### 5.3.7. Ejemplo practico guiado

Actualizar el riesgo de fuga con evidencia de presion, caudal y reclamos. Calcular primero la previa, luego las verosimilitudes y finalmente normalizar entre hipotesis.

### Actividad EMO [AGUA-04]

Construir un modelo probabilistico, actualizar con dos evidencias y definir prioridad considerando costos. La evidencia debe incluir sensibilidad ante previas, verosimilitudes y costos alternativos.

## 5.4. Incertidumbre y comunicacion probabilistica

La incertidumbre aleatoria surge del fenomeno; la epistemica, de conocimiento limitado. Un intervalo no garantiza que un parametro fijo tenga esa probabilidad, salvo una interpretacion bayesiana explicita. La calibracion compara probabilidades pronosticadas con frecuencias observadas.

### 5.4.7. Ejemplo practico guiado

Redactar un reporte que separe probabilidad, intervalo, supuestos, calidad de datos y recomendacion. Indicar que evidencia cambiaria la decision.

## Sintesis

La probabilidad cuantifica incertidumbre; Bayes actualiza creencias; una decision requiere ademas utilidad, costos y tolerancia al riesgo.
