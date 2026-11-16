---
title: "Series temporales y pronóstico"
subtitle: "Del orden temporal a decisiones con incertidumbre"
author: "Curso de Data Science"
course: "Data Science"
week: 7
class: 7
lang: es
---

# Series temporales y pronóstico

## Del orden temporal a decisiones con incertidumbre

**Semana 7 · Clase 7 · Cierre del curso**

**Recorrido conceptual:** `objeto temporal → estructura → modelo → validación → seguimiento`

---

# Propósito de la clase

Construir y evaluar pronósticos respetando el orden, la información disponible y la incertidumbre.

Al finalizar podremos:

- definir frecuencia, origen y horizonte;
- reconocer componentes y dependencia temporal;
- interpretar SARIMA y alternativas;
- validar con múltiples orígenes y baselines;
- diagnosticar, actualizar y comunicar límites.

---

# ¿Qué cambia cuando aparece el tiempo?

Las observaciones conservan secuencia y dependencia:

$$
\mathcal F_t=\{\text{información disponible hasta }t\}
\longrightarrow \widehat y_{t+h\mid t}.
$$

- El pasado puede informar sobre el futuro.
- La distribución puede cambiar con calendario y régimen.
- Mezclar filas aleatoriamente destruye orden y puede filtrar futuro.

**Regla:** reproducir qué se sabía en cada origen de pronóstico.

---

# Definir el objeto temporal

Una serie bien especificada requiere:

| Concepto | Pregunta |
|---|---|
| Unidad | ¿qué cuenta cada $y_t$? |
| Índice | ¿qué instante o intervalo identifica $t$? |
| Frecuencia | ¿cada cuánto se observa? |
| Origen | ¿hasta cuándo llega $\mathcal F_t$? |
| Horizonte | ¿a cuántos pasos se decide, $h$? |

En el caso: $y_t$ es el total diario reportado tras filtros; $h=1,\ldots,H$ días.

---

# Frecuencia, periodo y horizonte

- **Frecuencia de muestreo:** una observación por día.
- **Periodo:** pasos entre repeticiones; semana candidata $m=7$.
- **Horizonte:** distancia entre emisión y objetivo.

$$
\widehat y_{t+h\mid t}=\text{pronóstico para }t+h\text{ usando }\mathcal F_t.
$$

Agregar por día responde una pregunta distinta de agregar por hora. Tres meses permiten explorar semanas; una estacionalidad anual requiere ventanas de varios años.

---

# Series univariadas y multivariadas

| Tipo | Información | Ejemplo |
|---|---|---|
| Univariada | historia de una respuesta $y_t$ | pickups diarios totales |
| Con variables exógenas | $y_t$ y predictores disponibles | calendario conocido |
| Multivariada | varias series endógenas | pickups de varias zonas |

La información futura crece cuando las variables adicionales están disponibles al emitir el pronóstico y aportan señal pertinente.

---

# Componentes de una serie

$$
y_t=T_t+S_t+C_t+R_t.
$$

- **Tendencia $T_t$:** evolución suave del nivel.
- **Estacionalidad $S_t$:** repetición ligada al calendario.
- **Ciclo $C_t$:** expansión y contracción con duración variable.
- **Resto $R_t$:** variación pendiente de explicación; puede contener estructura.

Los componentes son hipótesis dependientes de escala, ventana y método.

---

# Descomposición: aditiva o multiplicativa

| Estructura | Expresión | Indicio |
|---|---|---|
| Aditiva | $y_t=T_t+S_t+R_t$ | amplitud estacional estable |
| Multiplicativa | $y_t=T_tS_tR_t$ | amplitud proporcional al nivel |

Con valores positivos, $\log y_t$ vuelve aditiva la segunda estructura.

**Límite:** una descomposición retrospectiva puede usar ambos lados de $t$; una característica predictiva debe calcularse solo con pasado.

---

# Regularidad, ceros y cobertura

Una serie regular exige una fila por cada día esperado.

| Situación | Representación |
|---|---|
| cobertura confirmada, conteo observado igual a cero | cero observado |
| interrupción o cobertura incompleta | faltante |
| más de una fila para el día | revisar duplicación y agregación |

Completar todo hueco con cero inventa actividad nula. También deben fijarse zona horaria, límites diarios y filtros iguales entre meses.

---

# Faltantes y anomalías temporales

- **Puntual:** valor extremo aislado.
- **Contextual:** inusual para ese día de semana.
- **Colectiva:** secuencia de duración anómala.
- **Cambio de nivel:** nuevo régimen persistente.

Investigar captura, calendario y eventos antes de imputar o sustituir. En validación, cualquier imputación debe usar solo información disponible en el origen.

**Trazabilidad:** conservar valor original, valor tratado, bandera y motivo.

---

# Pronóstico y explicación causal

| Pronóstico | Explicación causal |
|---|---|
| anticipa $Y_{t+h}$ | estima efecto de una intervención |
| explota regularidades predictivas | requiere supuestos de identificación |
| se evalúa fuera de muestra | se evalúa frente a alternativas causales |

La semejanza entre martes sostiene una regularidad predictiva. Atribuir un efecto causal al calendario requiere supuestos y un diseño de identificación; SARIMA aprovecha la regularidad para pronosticar.

---

# Dependencia temporal

Conocer el pasado cambia la distribución esperada:

$$
E(Y_t\mid Y_{t-1},Y_{t-2},\ldots)=g(Y_{t-1},Y_{t-2},\ldots).
$$

Puede surgir por hábitos, calendario, inercia o agregación. También puede ser espuria si dos valores comparten tendencia.

**Consecuencia doble:** la dependencia hace posible pronosticar y obliga a separar entrenamiento y evaluación en orden cronológico.

---

# Baselines que deben superarse

| Baseline | Pronóstico |
|---|---|
| media histórica | $\widehat y_{t+h\mid t}=\bar y_{1:t}$ |
| último valor | $\widehat y_{t+h\mid t}=y_t$ |
| estacional | $\widehat y_{t+h\mid t}=y_{t+h-7}$ |
| media por día semanal | promedio pasado de esa posición |

El baseline estacional es fuerte para pickups diarios con patrón semanal. Todos los métodos deben compararse en los mismos orígenes y horizontes.

---

# Medias móviles y modelos MA

Media móvil centrada para describir tendencia:

$$
\widetilde T_t=\frac{1}{2k+1}\sum_{j=-k}^{k}y_{t+j}.
$$

Usa observaciones posteriores a $t$ y sirve para descripción retrospectiva. En operación se utiliza una versión causal.

Una media causal para predecir $t$ usa $y_{t-1},\ldots,y_{t-w}$. El modelo MA($q$), en cambio, combina innovaciones pasadas.

---

# Suavizado exponencial y ETS

El suavizado simple actualiza un nivel:

$$
\ell_t=\alpha y_t+(1-\alpha)\ell_{t-1},\qquad 0<\alpha<1.
$$

ETS combina componentes de **error, tendencia y estacionalidad** en variantes aditivas o multiplicativas.

- útil cuando nivel y patrones evolucionan gradualmente;
- produce pronósticos e intervalos bajo una especificación probabilística;
- se compara con baselines mediante validación temporal.

---

# Regresión con tiempo y calendario

$$
Y_t=\beta_0+\beta_1t+\sum_{j=1}^{6}\gamma_jD_{j,t}+\varepsilon_t.
$$

Los indicadores de día de semana son conocidos de antemano. La tendencia lineal resume cambio, pero extrapolarla supone que continuará.

Si $\varepsilon_t$ conserva autocorrelación, los errores mantienen dependencia temporal y puede necesitarse una regresión dinámica.

---

# AR: memoria en los valores

$$
Y_t=c+\phi_1Y_{t-1}+\cdots+\phi_pY_{t-p}+\varepsilon_t.
$$

- $p$ indica cuántos rezagos regulares entran.
- En AR(1), $|\phi|<1$ permite reversión hacia la media.
- $\phi$ cercano a uno implica choques persistentes.

Los coeficientes expresan asociación predictiva condicionada por otros rezagos. La interpretación causal requiere supuestos adicionales.

---

# MA, ARMA y ARIMA

Una **innovación** es la información nueva que aparece en $t$ respecto de lo anticipado con el pasado:

$$
\varepsilon_t=Y_t-E(Y_t\mid\mathcal F_{t-1}).
$$

En datos ajustados se aproxima mediante el residuo de predicción a un paso, $\widehat\varepsilon_t=y_t-\widehat y_{t\mid t-1}$.

$$
\text{MA}(q):\quad Y_t=\mu+\varepsilon_t+\sum_{j=1}^{q}\theta_j\varepsilon_{t-j}.
$$

MA($q$) combina innovaciones recientes; ARMA($p,q$) agrega valores rezagados. ARIMA aplica esta dinámica después de diferenciar.

---

# Estacionariedad: estabilidad útil

En estacionariedad débil:

$$
E(Y_t)=\mu,\quad \operatorname{Var}(Y_t)=\sigma^2,
\quad \operatorname{Cov}(Y_t,Y_{t-k})=\gamma_k.
$$

Media y varianza permanecen estables en $t$; la covarianza depende del rezago. Tendencia, amplitud creciente o cambios de régimen señalan otra dinámica.

Estacionarizar busca patrones transferibles; la validación temporal determina su aporte al pronóstico.

---

# Diferencias regulares y estacionales

Una serie $I(d)$ alcanza una dinámica aproximadamente estacionaria después de $d$ diferencias entre periodos consecutivos.

$$
\nabla Y_t=(1-B)Y_t=Y_t-Y_{t-1},
$$

$$
\nabla_7Y_t=(1-B^7)Y_t=Y_t-Y_{t-7}.
$$

- $d=0$ modela niveles; $d=1$ modela cambios consecutivos.
- $D$ cuenta diferencias entre posiciones equivalentes de un periodo $m$.
- Sobrediferenciar aumenta varianza y puede inducir ACF negativa en rezago 1.

Elegir los mínimos $d,D$ que estabilicen la dinámica.

---

# ACF y PACF

- **ACF:** correlación entre $Y_t$ y $Y_{t-k}$.
- **PACF:** asociación con $k$ tras controlar rezagos intermedios.
- Picos en $7,14,21$ sugieren estructura semanal pendiente.
- ACF con caída muy lenta puede indicar tendencia o raíz unitaria.

Patrones ideales orientan órdenes pequeños: PACF truncada sugiere AR; ACF truncada sugiere MA. La decisión integra validación y conocimiento del proceso.

---

# SARIMA: mapa completo

$$
\operatorname{SARIMA}(p,d,q)(P,D,Q)_m
$$

| Orden | Función |
|---|---|
| $p,d,q$ | dinámica AR, diferencias y MA regulares |
| $P,D,Q$ | dinámica AR, diferencias y MA estacionales |
| $m$ | pasos por periodo; aquí, semana diaria $m=7$ |

La notación separa memoria de corto plazo y memoria en múltiplos de la estación.

---

# Órdenes regulares: $(p,d,q)$

- **$p$:** usa $Y_{t-1},\ldots,Y_{t-p}$ después de transformar y diferenciar.
- **$d$:** cantidad de diferencias entre periodos consecutivos utilizadas para estabilizar la dinámica.
- **$q$:** usa innovaciones $\varepsilon_{t-1},\ldots,\varepsilon_{t-q}$.

Ejemplo: ARIMA$(1,1,1)$ modela el cambio diario con un término AR(1) y un término MA(1).

Órdenes altos consumen información, dificultan identificación y pueden memorizar ruido.

---

# Órdenes estacionales: $(P,D,Q)_m$

- **$P$:** términos AR en $m,2m,\ldots,Pm$.
- **$D$:** diferencias $(1-B^m)^D$.
- **$Q$:** innovaciones en $m,2m,\ldots,Qm$.
- **$m=7$:** compara posiciones del ciclo semanal diario.

SARIMA$(0,0,0)(0,1,0)_7$ implica $Y_t-Y_{t-7}=\varepsilon_t$: el baseline semanal escrito como modelo.

---

# SARIMA con operadores

$$
\Phi(B^7)\phi(B)(1-B)^d(1-B^7)^DY_t
=\Theta(B^7)\theta(B)\varepsilon_t.
$$

Con AR regular y estacional de orden uno:

$$
(1-\phi B)(1-\Phi B^7)Y_t=\varepsilon_t,
$$

aparece también el término cruzado $\phi\Phi Y_{t-8}$. Los factores estacionales y regulares interactúan dentro de un único modelo.

---

# Una grilla pequeña y defendible

1. Fijar $m=7$ por dominio y evidencia gráfica.
2. Comparar $d,D\in\{0,1\}$ evitando sobrediferenciación.
3. Probar $p,q,P,Q\in\{0,1\}$ con un límite de complejidad.
4. Excluir fallas de convergencia o raíces problemáticas.
5. Usar AIC/AICc para filtrar y *walk-forward* para decidir.

Si dos candidatos rinden parecido, preferir el más simple, estable y actualizable.

---

# SARIMAX o regresión dinámica

$$
Y_t=\beta_0+\boldsymbol\beta^\top\mathbf x_t+n_t,
\qquad n_t\sim\operatorname{SARIMA}.
$$

Calendario, feriados o eventos programados pueden explicar nivel mientras SARIMA modela el error temporal.

Para pronosticar $t+h$, $\mathbf x_{t+h}$ debe conocerse en $t$ o construirse mediante escenarios. Las variables de fin de viaje quedan disponibles para análisis retrospectivo.

---

# VAR: vectores autorregresivos

VAR significa **vectores autorregresivos**. Esta familia aplica autorregresión vectorial para modelar conjuntamente varias series temporales.

Para un vector de series $\mathbf y_t$:

$$
\mathbf y_t=\mathbf c+A_1\mathbf y_{t-1}+\cdots+A_p\mathbf y_{t-p}+\boldsymbol\varepsilon_t.
$$

Cada componente del vector utiliza sus propios rezagos y los rezagos de las demás series. Por ejemplo, los pickups de cada zona pueden aprovechar la historia conjunta de varias zonas. El número de parámetros crece rápido con series y rezagos.

**Lectura prudente:** la utilidad predictiva conjunta describe dependencia temporal; una influencia causal entre zonas requiere supuestos adicionales.

---

# ML con rezagos: de serie a tabla

Para cada origen $t$, convertimos la historia disponible en una fila supervisada:

`historia hasta t → atributos X_t → modelo → pronóstico ŷ_(t+h|t)`

1. Definir el horizonte $h$ y ubicar $y_{t+h}$ como objetivo.
2. Crear rezagos $y_t,y_{t-1},y_{t-7}$, medias hasta $t$ y calendario conocido.
3. Comenzar en la primera fecha con todos los rezagos y medias disponibles; luego dividir por fecha en entrenamiento y prueba.
4. Ajustar árboles o *boosting* y reconstruir el pronóstico en cada origen.

Cada fila representa exactamente la información disponible al emitir su pronóstico.

---

# Flujo de trabajo completo

`definir → auditar → visualizar → proponer → validar → diagnosticar → desplegar`

1. Especificar unidad, frecuencia, origen, horizonte y decisión.
2. Regularizar y auditar cobertura, ceros, faltantes y anomalías.
3. Formular baselines y pocos candidatos.
4. Ajustar todo dentro de cada ventana temporal.
5. Comparar errores, intervalos, residuos y costo operativo.

---

# Separación cronológica y walk-forward

En cada origen $t_k$:

`entrenamiento hasta t_k | objetivos t_k+1 … t_k+H`

- **Ventana expansiva:** conserva toda la historia.
- **Ventana deslizante:** conserva longitud fija y se adapta antes.
- Los métodos comparten exactamente pares origen–objetivo.
- Transformación, imputación y selección de orden se reajustan dentro de la ventana.

Un único corte puede depender de una semana excepcional; varios orígenes revelan estabilidad.

---

# MAE, RMSE y MASE

$$
\operatorname{MAE}=\frac1N\sum|e_i|,
\qquad
\operatorname{RMSE}=\sqrt{\frac1N\sum e_i^2}.
$$

$$
\operatorname{MASE}=
\frac{N^{-1}\sum|e_i|}
{(n-7)^{-1}\sum_{t=8}^{n}|y_t-y_{t-7}|}.
$$

MAE mantiene unidades; RMSE castiga más errores grandes; MASE $<1$ supera la escala del baseline estacional de entrenamiento. Informar por horizonte y añadir sesgo.

---

# Pronósticos e intervalos

Un intervalo predictivo nominal de $1-\alpha$ busca:

$$
P(L_{t,h}\le Y_{t+h}\le U_{t,h}\mid\mathcal F_t)=1-\alpha.
$$

Debe evaluarse con:

- **cobertura:** proporción de observados dentro del intervalo;
- **anchura:** precisión del intervalo junto con su cobertura;
- resultados por horizonte y régimen.

Intervalos demasiado estrechos comunican falsa certeza; suelen ampliarse con $h$.

---

# Residuos y Ljung–Box

Un residuo de un paso es $e_t=y_t-\widehat y_{t\mid t-1}$. Revisar serie, ACF, varianza, colas, calendario y horizonte.

$$
Q=n(n+2)\sum_{k=1}^{H}\frac{\widehat\rho_k^2}{n-k}.
$$

Ljung–Box evalúa autocorrelaciones conjuntamente. Un valor $p$ alto indica compatibilidad con ruido blanco y uno bajo señala estructura temporal remanente. Diagnóstico gráfico y validación determinan su relevancia operativa.

---

# Fugas temporales frecuentes

| Fuga | Corrección |
|---|---|
| mezcla aleatoria | cortes cronológicos |
| media o imputación centrada | cálculo causal por ventana |
| perfil semanal con toda la serie | aprender solo con entrenamiento |
| elegir orden mirando abril repetidamente | selección interna y confirmación final |
| usar monto, propina u hora de descenso | usar variables disponibles al origen |

Una puntuación extraordinaria exige auditoría de disponibilidad antes que celebración.

---

# Actividad: seleccionar un orden

**En grupos, 12 minutos.** Serie diaria con $m=7$; tras $D=1$, la ACF muestra pico en 1, la PACF decae y el nivel fluctúa alrededor de una media estable.

1. Propongan baseline y dos candidatos SARIMA parsimoniosos.
2. Expliquen cada orden y qué evidencia lo motiva.
3. Diseñen una grilla máxima de 8 modelos.
4. Definan cómo decidir con *walk-forward*, residuos e intervalos.

**Salida:** una recomendación provisional y una razón para descartarla.

---

# Resultados: datos y patrón semanal

`Ejemplo_entrenamiento_SARIMA_Yellow_Taxi.ipynb`

| Evidencia ejecutada | Resultado |
|---|---:|
| pickups válidos reportados | 11.183.510 |
| cobertura temporal | 89 días |
| promedio diario | 125.657 |
| promedio de lunes | 101.494 |
| promedio de sábado | 140.377 |
| partición cronológica | 75 días + 14 días |

El perfil semanal mostró su máximo promedio el sábado y su mínimo el lunes. La diferencia regular alcanzó $p=0,0019$ en ADF y aportó evidencia para candidatos con $d=1$.

---

# Resultados: selección y diagnóstico

Los cuatro candidatos convergieron con cero avisos. El menor AIC de entrenamiento correspondió a:

$$
\operatorname{SARIMA}(0,1,1)(0,1,1)_7,
\qquad \mathrm{AIC}=1287,84.
$$

| Diagnóstico | Resultado |
|---|---:|
| Ljung–Box, rezago 7 | $p=0,0459$ |
| Ljung–Box, rezago 14 | $p=0,0639$ |
| Ljung–Box, rezago 21 | $p=0,2642$ |
| cobertura del intervalo al 90 % | 100 % en 14 días |

La señal en rezago 7 orienta una revisión de la dinámica semanal. Más orígenes permiten estimar la calibración de intervalos con mayor estabilidad.

---

# Resultados: desempeño predictivo

| Procedimiento | MAE | RMSE | MASE |
|---|---:|---:|---:|
| último valor, 14 días | 14.185,7 | 17.683,7 | 1,224 |
| baseline semanal, 14 días | **5.300,9** | 7.058,6 | **0,457** |
| SARIMA fijo, 14 días | 9.388,8 | 11.471,1 | 0,810 |
| SARIMA actualizado, $h=1$ | 5.461,3 | **6.741,1** | 0,471 |

El baseline ganó el corte fijo. La actualización diaria respondió otra pregunta y redujo el error del SARIMA. La complejidad se justifica cuando aporta mejoras dentro del mismo horizonte de evaluación.

---

# Actualización y seguimiento

Actualizar puede significar incorporar estado, reestimar parámetros o volver a seleccionar modelo.

Monitorizar en una ventana reciente:

- MAE, sesgo y desempeño frente al baseline;
- cobertura y anchura de intervalos;
- faltantes, anomalías y cambios de distribución;
- tiempo de ajuste y fallas de convergencia.

Una alarma inicia una revisión; la evidencia resultante guía la continuidad, actualización o sustitución del modelo.

---

# Síntesis final

- El objeto temporal incluye valores, frecuencia, calendario, cobertura y horizonte.
- Dependencia permite pronosticar; orden y disponibilidad limitan lo aprendible.
- SARIMA separa dinámica regular y estacional con órdenes interpretables.
- Un modelo se juzga contra baselines, en múltiples orígenes y con incertidumbre.
- Residuos, fuga, actualización y representatividad forman parte del resultado.

**Cierre del curso:** una predicción útil es una afirmación delimitada, reproducible y revisable.
