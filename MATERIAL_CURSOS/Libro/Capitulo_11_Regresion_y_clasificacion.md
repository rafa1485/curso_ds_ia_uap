# Capítulo 11. Regresión y clasificación: modelos fundamentales

Los modelos lineales ocupan un lugar central en la ciencia de datos. No son únicamente algoritmos sencillos con los que iniciar una comparación: proporcionan un lenguaje preciso para separar señal, ruido, incertidumbre y decisión. Una regresión lineal permite expresar cómo cambia una respuesta continua al variar unas características, manteniendo constantes las demás. La regresión logística traslada esa estructura a probabilidades de clase. Ridge, Lasso y Elastic Net muestran, además, cómo introducir preferencias explícitas por soluciones estables o parsimoniosas.

Su aparente simplicidad exige disciplina. Una recta puede predecir bien y, sin embargo, no justificar una lectura causal; un coeficiente puede cambiar de signo por colinealidad; una exactitud elevada puede esconder probabilidades mal calibradas; y un umbral de 0,5 puede ser incompatible con los costos reales. En estos modelos, la formulación, los supuestos y la regla de decisión son tan importantes como el ajuste numérico.

El capítulo adopta dos perspectivas complementarias. La perspectiva **predictiva** pregunta cuánto generaliza el procedimiento a observaciones nuevas. La perspectiva **inferencial** pregunta qué puede sostenerse sobre parámetros, asociaciones e incertidumbre bajo determinados supuestos. Ambas usan fórmulas semejantes, pero no son intercambiables. La validación fuera de muestra es indispensable para predicción; la identificación del diseño, los supuestos probabilísticos y los errores estándar son indispensables para inferencia.

Al finalizar, el lector podrá formular problemas de regresión y clasificación, derivar mínimos cuadrados, interpretar su geometría, especificar categorías e interacciones, diagnosticar incumplimientos, explicar el compromiso sesgo-varianza de la regularización y convertir probabilidades logísticas calibradas en decisiones justificadas.

## 11.1. Regresión lineal

### 11.1.1. Formulación del problema de regresión

En regresión, la variable objetivo $Y$ toma valores numéricos y se desea aproximar su comportamiento a partir de un vector de características $X=(X_1,\ldots,X_p)^T$. El objeto poblacional natural bajo pérdida cuadrática es la **función de regresión**

$$
m(\mathbf x)=\mathbb E(Y\mid X=\mathbf x).
$$

Esta definición no supone linealidad. Afirma que, entre todas las predicciones puntuales posibles para un mismo $\mathbf x$, la media condicional minimiza el error cuadrático esperado. En efecto, para cualquier número $a$,

$$
\mathbb E[(Y-a)^2\mid X=\mathbf x]
=\operatorname{Var}(Y\mid X=\mathbf x)+[m(\mathbf x)-a]^2,
$$

por lo que el mínimo se alcanza en $a=m(\mathbf x)$. La regresión lineal restringe esa función a la familia afín

$$
f_{\boldsymbol\beta}(\mathbf x)=\beta_0+\sum_{j=1}^{p}\beta_jx_j.
$$

Para la observación $i$ se escribe

$$
y_i=\beta_0+\sum_{j=1}^{p}\beta_jx_{ij}+\varepsilon_i,
$$

donde $\varepsilon_i$ reúne variación no explicada, variables omitidas, ruido de medición y posible error de especificación. Conviene distinguir tres entidades: el valor observado $y_i$, la media modelada $\mu_i=\mathbb E(Y_i\mid X_i)$ y la predicción ajustada $\widehat y_i$. El residuo $e_i=y_i-\widehat y_i$ es observable después del ajuste; el error $\varepsilon_i=y_i-\mu_i$ no lo es.

Formular bien el problema requiere declarar la unidad de análisis, el instante de predicción, el horizonte, las entradas disponibles entonces y la pérdida relevante. Para demanda energética horaria, una fila podría ser edificio-hora; predecir una hora después no admite mediciones que lleguen al finalizar esa hora. Si los errores grandes son especialmente costosos, el error cuadrático medio puede ser adecuado; si se busca robustez frente a extremos, puede preferirse pérdida absoluta. La elección de pérdida define qué resumen condicional se estima y no debe decidirse por costumbre.

La muestra de aprendizaje es $\mathcal D=\{(\mathbf x_i,y_i)\}_{i=1}^n$. El riesgo poblacional de un predictor $f$ bajo pérdida $L$ es

$$
R(f)=\mathbb E[L(Y,f(X))],
$$

mientras que el riesgo empírico promedia sobre la muestra. Ajustar minimiza una versión empírica; evaluar estima comportamiento futuro. Confundir ambos produce sobreajuste. También debe fijarse el dominio de generalización: otro turno de la misma planta, una campaña agrícola posterior o una región no observada plantean distribuciones y particiones diferentes.

**Asociación no es intervención.** Un coeficiente predictivo describe una relación condicionada a las variables incluidas y a la población observada. Para afirmar que modificar $X_j$ causará un cambio en $Y$ se necesitan supuestos adicionales sobre asignación, confundidores, temporalidad y consistencia. La regresión es una herramienta de estimación; no crea por sí sola un diseño causal.

### 11.1.2. Regresión lineal simple

La regresión lineal simple usa un solo predictor:

$$
Y_i=\beta_0+\beta_1x_i+\varepsilon_i.
$$

$\beta_0$ es la media modelada cuando $x=0$ y $\beta_1$ es el cambio medio de $Y$ asociado con una unidad adicional de $x$. La palabra «asociado» es deliberada. Si $x$ es temperatura exterior y $Y$ consumo eléctrico diario, la pendiente resume una tendencia en los datos, no necesariamente el efecto aislado de elevar físicamente la temperatura.

Al minimizar $S(\beta_0,\beta_1)=\sum_i(y_i-\beta_0-\beta_1x_i)^2$ y anular derivadas se obtienen las ecuaciones normales. La primera implica que la recta pasa por $(\bar x,\bar y)$; la segunda conduce a

$$
\widehat\beta_1=
\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}
{\sum_i(x_i-\bar x)^2}
=\frac{s_{xy}}{s_x^2},
\qquad
\widehat\beta_0=\bar y-\widehat\beta_1\bar x.
$$

Así, la pendiente es covarianza dividida por varianza del predictor. También puede escribirse $\widehat\beta_1=r_{xy}s_y/s_x$: correlación y pendiente comparten signo, pero la primera no tiene unidades y la segunda sí. Si $x$ se expresa en centenas en lugar de unidades, el coeficiente cambia aunque las predicciones no.

**Ejemplo calculado.** Para cinco jornadas de una línea de fabricación se registran horas de operación $x=(2,4,6,8,10)$ y consumo energético $y=(18,25,29,36,42)$ MWh. Se tiene $\bar x=6$, $\bar y=30$,

$$
\sum(x_i-\bar x)(y_i-\bar y)=118,
\qquad
\sum(x_i-\bar x)^2=40.
$$

Por tanto, $\widehat\beta_1=2{,}95$ MWh/h y $\widehat\beta_0=12{,}3$ MWh. Para siete horas, $\widehat y=12{,}3+2{,}95(7)=32{,}95$ MWh. El intercepto representa consumo a cero horas solo si ese punto tiene sentido y la relación sigue siendo válida allí. Como cero está fuera de los valores observados, su interpretación física requiere cautela; centrar $x$ en seis horas convertiría el intercepto en el consumo esperado para una jornada típica.

Los residuos suman cero cuando hay intercepto, y son ortogonales al predictor centrado: $\sum e_i=0$ y $\sum(x_i-\bar x)e_i=0$. Estas propiedades son consecuencias algebraicas del ajuste, no evidencia de que los errores poblacionales tengan media cero o sean independientes.

Interpolar dentro del rango observado suele ser menos arriesgado que extrapolar. Una recta estimada entre 2 y 10 horas no garantiza comportamiento a 20: saturación, turnos adicionales o cambios de tarifa pueden alterar el mecanismo. Siempre deben comunicarse el rango de soporte y la incertidumbre, y compararse las predicciones con un baseline, por ejemplo $\widehat y=\bar y$.

### 11.1.3. Regresión lineal múltiple

La regresión múltiple introduce varios predictores:

$$
Y_i=\beta_0+\beta_1x_{i1}+\cdots+\beta_px_{ip}+\varepsilon_i.
$$

Al añadir una columna de unos para el intercepto, se usa la notación matricial

$$
\mathbf y=X\boldsymbol\beta+\boldsymbol\varepsilon,
$$

con $X\in\mathbb R^{n\times(p+1)}$, $\boldsymbol\beta\in\mathbb R^{p+1}$ y $\mathbf y\in\mathbb R^n$. Cada fila describe una observación; cada columna, un término del modelo. «Lineal» significa lineal en los parámetros, no necesariamente en las entradas originales. El modelo $\beta_0+\beta_1t+\beta_2t^2$ sigue siendo lineal en $\boldsymbol\beta$.

El valor de múltiples predictores no consiste solamente en elevar $R^2$. Permiten comparar observaciones a igualdad de otras características y reducir error si aportan información complementaria. En consumo de un edificio podrían intervenir temperatura, ocupación, superficie, día laboral y una tendencia temporal. La lectura de $\beta_j$ es parcial: cambio esperado por una unidad de $x_j$, **manteniendo fijas** las demás columnas. Esa comparación puede ser poco realista si las variables casi nunca varían por separado.

El teorema de Frisch-Waugh-Lovell aclara esta lectura. Para estimar el efecto de $x_j$, primero se elimina de $x_j$ la parte linealmente explicada por las otras columnas; se hace lo mismo con $y$; después se regresa el residuo de $y$ sobre el residuo de $x_j$. La pendiente resultante es exactamente $\widehat\beta_j$. Por tanto, el coeficiente usa solo la variación de $x_j$ que no es redundante con el resto.

Agregar variables nunca aumenta la suma de cuadrados residual sobre entrenamiento, porque el modelo ampliado puede asignar cero a los nuevos coeficientes. Sin embargo, puede aumentar el error futuro, ensanchar intervalos e introducir variables disponibles demasiado tarde. El $R^2$,

$$
R^2=1-\frac{\sum_i(y_i-\widehat y_i)^2}{\sum_i(y_i-\bar y)^2},
$$

mide fracción de variación muestral explicada respecto de la media. No mide causalidad, calibración individual ni desempeño fuera de muestra. El $R^2$ ajustado penaliza grados de libertad, pero tampoco sustituye una validación adecuada.

La especificación exige decidir forma funcional. Una relación curva puede representarse con transformaciones, polinomios de grado moderado o bases por tramos; una periodicidad, con seno y coseno; un efecto condicionado, con interacciones. Cada término amplía la hipótesis y debe justificarse por dominio y validación. Un modelo con menos columnas, unidades claras y comportamiento de extrapolación plausible puede ser preferible aunque su ajuste interno sea ligeramente peor.

### 11.1.4. Estimación por mínimos cuadrados

Mínimos cuadrados ordinarios, OLS por sus siglas en inglés, elige

$$
\widehat{\boldsymbol\beta}
=\arg\min_{\boldsymbol\beta}
S(\boldsymbol\beta),
\qquad
S(\boldsymbol\beta)=\|\mathbf y-X\boldsymbol\beta\|_2^2.
$$

Al expandir,

$$
S=\mathbf y^T\mathbf y-2\boldsymbol\beta^TX^T\mathbf y
+\boldsymbol\beta^TX^TX\boldsymbol\beta.
$$

Su gradiente es $-2X^T\mathbf y+2X^TX\boldsymbol\beta$. Igualarlo a cero produce las **ecuaciones normales**

$$
X^TX\widehat{\boldsymbol\beta}=X^T\mathbf y.
$$

Si las columnas de $X$ son linealmente independientes, $X^TX$ es invertible y

$$
\widehat{\boldsymbol\beta}=(X^TX)^{-1}X^T\mathbf y.
$$

Esta expresión sirve para derivar propiedades, pero no prescribe calcular explícitamente la inversa: factorizaciones QR o SVD suelen ser más estables. Si $X$ no tiene rango completo, las predicciones proyectadas pueden ser únicas aunque los coeficientes no; la pseudoinversa selecciona una solución de norma mínima.

La geometría es especialmente reveladora. Los vectores predichos pertenecen al espacio columna $\mathcal C(X)$. OLS proyecta ortogonalmente $\mathbf y$ sobre ese subespacio:

$$
\widehat{\mathbf y}=H\mathbf y,
\qquad
H=X(X^TX)^{-1}X^T.
$$

$H$ es la matriz sombrero, simétrica e idempotente. El residuo $\mathbf e=(I-H)\mathbf y$ es ortogonal a cada columna de $X$, porque $X^T\mathbf e=0$. Se obtiene la descomposición pitagórica, si hay intercepto,

$$
\sum_i(y_i-\bar y)^2
=\sum_i(\widehat y_i-\bar y)^2+\sum_i e_i^2.
$$

Bajo el modelo condicional $\mathbb E(\boldsymbol\varepsilon\mid X)=0$ y $\operatorname{Var}(\boldsymbol\varepsilon\mid X)=\sigma^2I$,

$$
\mathbb E(\widehat{\boldsymbol\beta}\mid X)=\boldsymbol\beta,
\qquad
\operatorname{Var}(\widehat{\boldsymbol\beta}\mid X)=\sigma^2(X^TX)^{-1}.
$$

La varianza se estima con $\widehat\sigma^2=SSE/(n-p-1)$. Si además los errores son normales, pueden obtenerse pruebas e intervalos exactos en muestra finita. La normalidad no es necesaria para que OLS minimice cuadrados ni para la insesgadez; sí facilita inferencia paramétrica exacta. Con muestras grandes, resultados asintóticos pueden ser suficientes bajo condiciones más generales.

El teorema de Gauss-Markov establece que, con linealidad en parámetros, esperanza condicional cero, rango completo y errores homocedásticos no correlacionados, OLS es el estimador lineal insesgado de menor varianza. No afirma que sea el mejor predictor entre todos los métodos ni que los errores sean normales.

**Pseudocódigo conceptual de ajuste y evaluación:**

```text
ENTRADA: datos de desarrollo, especificación y particiones válidas
PARA cada partición:
    aprender transformaciones solo con el entrenamiento
    construir matrices de diseño de entrenamiento y validación
    resolver las ecuaciones de mínimos cuadrados en entrenamiento
    predecir una sola vez sobre validación
    registrar pérdida y diagnósticos por grupos relevantes
AGREGAR resultados y compararlos con el baseline
REAJUSTAR la especificación elegida con todos los datos de desarrollo
EVALUAR una vez en prueba intacta o iniciar monitorización prospectiva
```

### 11.1.5. Interpretación de coeficientes

En un modelo aditivo, $\beta_j$ representa el cambio en la media condicional de $Y$ por cada unidad adicional de $X_j$, manteniendo las restantes columnas constantes. Las unidades son «unidades de $Y$ por unidad de $X_j$». Si el objetivo está en kWh y superficie en m², un coeficiente de $0{,}8$ se lee como 0,8 kWh adicionales por m² bajo la comparación condicionada especificada.

El intercepto es el valor esperado cuando todas las columnas valen cero. Puede ser sustantivo, como demanda base a cero producción, o solo algebraico. Centrar $x_j^c=x_j-c_j$ desplaza el punto de referencia sin cambiar las predicciones. Con $c_j$ igual a una media o valor operativo, el intercepto se vuelve más interpretable y las interacciones suelen ser numéricamente más estables.

Las transformaciones cambian la lectura:

| Especificación | Interpretación aproximada de $\beta_1$ |
|---|---|
| $Y=\beta_0+\beta_1X$ | una unidad más de $X$ cambia $Y$ en $\beta_1$ |
| $Y=\beta_0+\beta_1\log X$ | 1% más de $X$ cambia $Y$ en $0{,}01\beta_1$ |
| $\log Y=\beta_0+\beta_1X$ | una unidad más de $X$ cambia $Y$ aproximadamente en $100\beta_1$% |
| $\log Y=\beta_0+\beta_1\log X$ | 1% más de $X$ se asocia con $\beta_1$% más de $Y$ |

La aproximación porcentual es precisa para coeficientes pequeños; en un modelo log-lineal, el cambio exacto por una unidad es $100(e^{\beta_1}-1)$%. Si se retransfieren predicciones desde $\log Y$, exponentiar la media logarítmica no recupera automáticamente $\mathbb E(Y\mid X)$ debido a la desigualdad de Jensen; se necesita considerar la distribución residual.

Un intervalo de confianza para un coeficiente, bajo los supuestos correspondientes, tiene forma

$$
\widehat\beta_j\pm t_{1-\alpha/2,\,n-p-1}
\widehat{se}(\widehat\beta_j).
$$

No es la probabilidad posterior de que ese parámetro fijo esté dentro del intervalo. Tampoco un valor $p$ pequeño cuantifica importancia predictiva o magnitud práctica. Con muestras enormes, efectos irrelevantes pueden ser estadísticamente distinguibles de cero; con colinealidad, efectos sustantivos pueden tener intervalos amplios.

La interpretación depende del conjunto de ajuste. El coeficiente de temperatura puede cambiar al incluir ocupación porque responde otra pregunta condicionada. Si ocupación es consecuencia de temperatura o de una decisión relacionada, ajustarla puede incluso introducir sesgo para una pregunta causal. Deben informarse la especificación, la población y el rango de datos junto al coeficiente. Comparar magnitudes solo es razonable con escalas compatibles; coeficientes estandarizados ayudan, pero una desviación estándar puede no representar un cambio factible ni igualmente costoso.

### 11.1.6. Variables categóricas e interacciones

Una categoría nominal no debe codificarse como entero con distancia artificial. Si turno tiene niveles mañana, tarde y noche, con intercepto se elige una referencia y se incluyen $K-1$ indicadores:

$$
Y=\beta_0+\beta_T I(\text{tarde})+\beta_N I(\text{noche})+\varepsilon.
$$

$\beta_0$ es la media modelada de mañana; $\beta_T$ y $\beta_N$ son diferencias respecto de ella. Cambiar la referencia modifica coeficientes, no valores ajustados ni comparaciones globales. Incluir los $K$ indicadores junto al intercepto crea dependencia lineal perfecta, conocida como trampa de variables ficticias. También puede emplearse una codificación con suma cero, útil para comparar cada nivel con una media global, siempre que se documente.

Para una categoría ordinal, asignar 1, 2, 3 impone efectos igualmente espaciados. Esa restricción puede ser razonable o no; los indicadores permiten diferencias libres. Categorías raras producen estimaciones inestables y niveles nuevos requieren una política definida antes del despliegue. Agruparlos por observar su objetivo en todo el conjunto genera fuga.

Una interacción expresa que el efecto de una variable depende de otra:

$$
Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_{12}X_1X_2+\varepsilon.
$$

Ahora $\partial\mathbb E(Y\mid X)/\partial X_1=\beta_1+\beta_{12}X_2$. Por ello, $\beta_1$ es el efecto de $X_1$ cuando $X_2=0$, no un promedio universal. Centrar continuas sitúa ese cero en un valor relevante. El principio de jerarquía recomienda conservar ambos efectos principales al incluir el producto, salvo justificación fuerte.

**Ejemplo.** Un modelo de tiempo de mecanizado usa tamaño de lote centrado $L$, indicador $A$ para aleación especial y $L\times A$:

$$
\widehat Y=42+1{,}8L+9A+0{,}7LA.
$$

Para material estándar, cada unidad de lote agrega 1,8 minutos; para aleación especial, agrega $1{,}8+0{,}7=2{,}5$. A tamaño medio ($L=0$), la aleación especial requiere 9 minutos adicionales. Afirmar simplemente que «el coeficiente de lote es 1,8» omitiría la interacción.

Las interacciones categoría-categoría generan diferencias entre combinaciones; las continuas pueden usar productos o superficies por tramos. Su número crece rápido y muchas combinaciones tienen poco soporte. No se deben generar miles de términos y seleccionar mirando la prueba. Antes de incluir una interacción conviene formular el mecanismo, revisar cobertura conjunta, evaluar fuera de muestra y representar efectos predichos con incertidumbre. Un coeficiente de interacción tampoco es, por sí solo, evidencia de mecanismo causal.

### 11.1.7. Ejemplo práctico guiado: predicción de consumo o demanda

Una empresa administra edificios comerciales y desea anticipar a las 18:00 el consumo eléctrico total del día siguiente, en MWh. La unidad de observación es edificio-día. Están disponibles superficie, ocupación programada, temperatura media pronosticada, indicador de día laboral y consumo de los siete días anteriores. Se dispone de tres años de historia; el último trimestre se reserva como prueba temporal.

**1. Baseline y métrica.** El baseline predice el consumo del mismo día de la semana anterior. Se eligen MAE para expresar desviación típica en MWh y RMSE como medida secundaria sensible a errores grandes. El objetivo no es superar la media de entrenamiento, sino una regla operacional razonable.

**2. Especificación.** El análisis del dominio sugiere una respuesta térmica en U: calefacción bajo una temperatura de confort y refrigeración sobre ella. En vez de forzar una sola pendiente, se crean grados-día de frío $C=(18-T)_+$ y calor $H=(T-22)_+$, donde $(a)_+=\max(a,0)$. Se incluye interacción $H\times D$, con $D=1$ para día laboral, porque la refrigeración puede crecer con ocupación. El modelo es

$$
Y=\beta_0+\beta_SS+\beta_OO+\beta_CC+\beta_HH+
\beta_DD+\beta_{HD}HD+\beta_LL+\varepsilon,
$$

donde $S$ es superficie en miles de m², $O$ ocupación programada en centenas y $L$ consumo de la semana previa.

**3. Ajuste temporal.** Las transformaciones y cualquier imputación se aprenden en cada ventana de entrenamiento. Se usan validaciones que avanzan en el tiempo, pues una partición aleatoria mezclaría estaciones y versiones operativas. Tras comparar especificaciones sin consultar prueba, se obtiene en una ventana representativa:

| Término | Coeficiente estimado | Lectura condicionada |
|---|---:|---|
| intercepto | 4,10 | demanda base en los valores de referencia |
| superficie | 0,62 | MWh por cada 1000 m² |
| ocupación | 0,28 | MWh por cada 100 personas programadas |
| frío | 0,19 | MWh por grado bajo 18 °C |
| calor | 0,24 | MWh por grado sobre 22 °C en día no laboral |
| laboral | 1,35 | diferencia laboral a $H=0$ |
| calor × laboral | 0,11 | incremento adicional por grado en laboral |
| semana previa | 0,57 | MWh por MWh del día comparable previo |

Para un edificio de 12 000 m², ocupación 800, temperatura pronosticada 27 °C, día laboral y consumo previo de 20 MWh, $C=0$, $H=5$:

$$
\widehat Y=4{,}10+0{,}62(12)+0{,}28(8)+0{,}24(5)
+1{,}35+0{,}11(5)+0{,}57(20)=28{,}28\text{ MWh}.
$$

La pendiente térmica en laboral es $0{,}24+0{,}11=0{,}35$ MWh/°C. Esta lectura no afirma que modificar la temperatura exterior cause exactamente ese cambio.

**4. Resultados.** En prueba, el baseline logra MAE 2,8 y RMSE 4,1 MWh; el modelo, MAE 2,1 y RMSE 3,4. La mejora relativa de MAE es $(2{,}8-2{,}1)/2{,}8=25$%. También se revisan errores por edificio, estación y días de alta ocupación. En edificios nuevos sin rezago, la cobertura cae: el modelo necesita una política explícita, como una variante sin $L$, y no una imputación futura.

**5. Límites.** La temperatura empleada durante entrenamiento debe ser la pronosticada históricamente, no la observada al final del día. De lo contrario se evalúa una tarea artificialmente fácil. Una ampliación de superficie o un cambio de equipos rompe estabilidad. Se monitorizan distribución de entradas, residuo medio, MAE por segmento y frecuencia de extrapolación. El modelo se acepta porque supera el baseline de manera estable y sus fallos son compatibles con el uso, no porque todos sus coeficientes sean «significativos».

## 11.2. Supuestos y diagnóstico del modelo lineal

### 11.2.1. Linealidad

El supuesto de linealidad relevante es

$$
\mathbb E(Y\mid X)=X\boldsymbol\beta,
$$

es decir, la media condicional está bien representada por los términos incluidos. No exige que cada variable bruta tenga una relación recta: bases polinómicas, logaritmos, tramos e interacciones siguen formando un modelo lineal en parámetros. Tampoco exige que el histograma de $Y$ sea normal.

Si la especificación omite curvatura, los residuos frente a valores ajustados o frente a un predictor pueden mostrar arcos. Por ejemplo, modelar consumo con una sola pendiente de temperatura puede producir residuos positivos en días muy fríos y muy cálidos y negativos en días templados. La suma residual puede seguir siendo cero; el patrón local revela el problema.

El diagnóstico combina conocimiento del mecanismo, gráficos y validación. Se pueden superponer suavizados de residuos, comparar especificaciones anidadas y observar error por intervalos de cada entrada. Un patrón en entrenamiento podría ser azar; una mejora debe repetirse en datos no usados para proponerla. Añadir un polinomio de grado alto hasta eliminar cualquier ondulación suele sobreajustar y extrapola de forma extrema.

La solución no siempre es transformar. Puede faltar una interacción, existir un cambio de régimen o haberse medido mal una entrada. Si la variable objetivo es un conteo pequeño o está acotada, otra familia probabilística puede representar mejor varianza y soporte. Para predicción, cierta no linealidad puede tolerarse si el error externo satisface el uso; para inferencia sobre una pendiente, una forma incorrecta invalida su interpretación incluso con buen promedio predictivo.

Una revisión responsable pregunta: ¿en qué rango hay datos?, ¿la pendiente local conserva signo?, ¿qué predice el modelo fuera del rango?, ¿hay soporte para comparar casos manteniendo lo demás fijo? La linealidad es una hipótesis aproximada y localizada, no una propiedad que un único gráfico pueda certificar.

### 11.2.2. Independencia

El supuesto clásico considera errores no correlacionados:

$$
\operatorname{Cov}(\varepsilon_i,\varepsilon_j\mid X)=0,
\qquad i\ne j.
$$

Se viola cuando observaciones comparten tiempo, entidad, ubicación, lote o documento de origen. Mediciones horarias del mismo edificio se parecen; piezas del mismo lote comparten materia prima; rendimientos de parcelas vecinas comparten clima. Aumentar el número de filas no crea la misma información que añadir unidades independientes.

Con autocorrelación positiva, OLS puede conservar coeficientes insesgados si la esperanza condicional es correcta, pero los errores estándar clásicos suelen ser demasiado pequeños. Además, una partición aleatoria produce validaciones optimistas al situar casos casi duplicados en ambos lados. El problema afecta tanto a inferencia como a evaluación.

En series ordenadas se inspeccionan residuos en el tiempo, autocorrelaciones por rezago y patrones de rachas. En datos agrupados se comparan residuos dentro y entre entidades. Una estadística aislada no sustituye entender el muestreo. La dependencia puede tratarse mediante características temporales, errores estándar robustos por conglomerado, mínimos cuadrados generalizados, efectos aleatorios o modelos dinámicos, según la pregunta. Ninguna corrección recupera información independiente inexistente.

El diseño de validación debe imitar el despliegue. Si se predice el futuro de edificios conocidos, se separa por tiempo manteniendo edificios; si se generaliza a edificios nuevos, se retienen edificios completos; si ambas cosas importan, se evalúan ambos escenarios. Agrupar solo en el cálculo de errores estándar y luego mezclar grupos en prueba no resuelve fuga predictiva.

La independencia se refiere a errores condicionados, no a que las variables de entrada sean independientes entre sí. Predictores correlacionados plantean multicolinealidad, un asunto diferente. También debe distinguirse dependencia serial de deriva: la primera relaciona errores cercanos; la segunda cambia la distribución o el mecanismo con el tiempo.

### 11.2.3. Homocedasticidad

La homocedasticidad establece varianza condicional constante:

$$
\operatorname{Var}(\varepsilon_i\mid X)=\sigma^2.
$$

Cuando la dispersión depende de $X$ existe heterocedasticidad. En ventas, variación absoluta suele crecer con tamaño de tienda; en manufactura, lotes grandes pueden acumular más variación total. Un gráfico de residuos contra ajustados con forma de embudo es una señal habitual.

Con esperanza condicional correcta, la heterocedasticidad no sesga por sí misma los coeficientes OLS, pero los vuelve ineficientes y hace incorrecta la fórmula clásica $\sigma^2(X^TX)^{-1}$. Los intervalos de predicción también deben ensancharse donde la variabilidad sea mayor. Reportar una banda constante en todo el rango oculta riesgo precisamente en observaciones grandes.

Las respuestas posibles dependen del origen. Los errores estándar robustos a heterocedasticidad corrigen inferencia asintótica sin cambiar coeficientes. Mínimos cuadrados ponderados usa pesos inversamente proporcionales a la varianza si esta puede modelarse: minimizar $\sum_iw_i e_i^2$. Una transformación logarítmica puede estabilizar variación multiplicativa, pero cambia el objetivo y requiere cuidado al volver a escala original. Modelar directamente media y dispersión puede ser más honesto.

No conviene ponderar por intuición sin definir el estimando. Dar menos peso a edificios grandes puede mejorar error relativo y empeorar error absoluto total. La pérdida debe reflejar la decisión. Asimismo, una prueba formal puede detectar desviaciones minúsculas con $n$ grande o tener poca potencia con $n$ pequeño. Importan magnitud, patrón y consecuencia.

Para predicción se comparan MAE, RMSE o error porcentual por bandas de escala, evitando porcentajes cuando $Y$ se aproxima a cero. Para inferencia se declara la corrección de varianza usada. La homocedasticidad no significa que los residuos observados tengan exactamente igual dispersión en cada grupo: es una afirmación poblacional aproximada.

### 11.2.4. Distribución de residuos

El modelo clásico completo suele añadir

$$
\boldsymbol\varepsilon\mid X\sim\mathcal N(\mathbf0,\sigma^2I).
$$

La normalidad permite derivar distribuciones $t$ y $F$ exactas en muestras finitas. No es necesaria para calcular OLS ni para que, bajo esperanza condicional cero, sus coeficientes sean insesgados. En muestras grandes, aproximaciones asintóticas suelen funcionar si no dominan extremos y existen momentos apropiados.

Un gráfico cuantíl-cuantíl compara cuantiles residuales con los normales. Desviaciones en colas sugieren extremos frecuentes; asimetría, una cola más larga; escalones, una respuesta discreta o redondeada. Sin embargo, los residuos no son errores independientes idénticos: su varianza es $\sigma^2(1-h_{ii})$. Para comparar casos se usan residuos estudentizados, aunque tampoco convierten un diagnóstico en prueba definitiva.

Los extremos pueden proceder de errores de captura, eventos válidos, mezcla de poblaciones o una distribución de cola pesada. Eliminar observaciones solo para aproximarse a una campana falsea la población. Primero se verifica linaje; después se evalúa sensibilidad con y sin el caso, se consideran pérdidas robustas o una distribución adecuada y se informa la decisión. Un evento raro pero operativo debe formar parte del riesgo, no desaparecer del análisis.

También se distingue intervalo para la media e intervalo para una observación futura. En $\mathbf x_0$, bajo el modelo clásico,

$$
\widehat y_0\pm t^*\widehat\sigma
\sqrt{\mathbf x_0^T(X^TX)^{-1}\mathbf x_0}
$$

estima incertidumbre de la media; para una observación nueva se añade 1 dentro de la raíz. El segundo es más ancho porque incorpora ruido irreducible. Fuera del soporte, ambos pueden dar una falsa apariencia de precisión si la forma lineal deja de ser válida.

### 11.2.5. Multicolinealidad

Existe multicolinealidad cuando columnas de $X$ están fuertemente relacionadas; es perfecta si una es combinación exacta de otras. En el caso perfecto, $X^TX$ no es invertible y los coeficientes no son identificables. En el caso aproximado, la inversión amplifica pequeñas perturbaciones: coeficientes grandes, signos inesperados e intervalos amplios pueden coexistir con predicciones razonables.

De la varianza

$$
\operatorname{Var}(\widehat{\boldsymbol\beta})=\sigma^2(X^TX)^{-1}
$$

se observa que poca variación independiente de una columna implica alta incertidumbre. El factor de inflación de varianza para $X_j$ es

$$
VIF_j=\frac{1}{1-R_j^2},
$$

donde $R_j^2$ procede de regresar $X_j$ sobre las demás. Un VIF alto señala que queda poca variación exclusiva, pero no existe un umbral universal. Los valores dependen de codificación, interacciones y población.

Correlaciones por pares no detectan toda dependencia multivariada. También se examinan valores singulares y número de condición después de considerar escalas. Términos polinómicos sin centrar pueden ser altamente correlacionados por construcción; centrar mejora estabilidad interpretativa, pero no agrega información. Eliminar una variable puede ser razonable si es redundante y costosa, pero peligroso si era un control necesario para una pregunta causal.

Las soluciones incluyen recolectar observaciones con combinaciones más variadas, combinar mediciones justificadamente, reformular el estimando, usar componentes o regularizar. Ridge estabiliza predicciones al aceptar sesgo. Lasso puede seleccionar arbitrariamente entre sustitutos. Si el objetivo es interpretar efectos separados de dos temperaturas casi idénticas, ningún algoritmo reemplaza falta de soporte experimental.

Multicolinealidad no sesga automáticamente OLS ni reduce siempre capacidad predictiva dentro de la distribución. Su principal efecto es dificultar atribución y estabilidad. Por ello deben reportarse predicciones y coeficientes bajo perturbaciones o remuestreos, no una única tabla como verdad fija.

### 11.2.6. Observaciones influyentes

Una observación puede ser atípica en $Y$, extrema en las entradas o influyente sobre el ajuste. Son conceptos distintos. El **apalancamiento** es $h_{ii}$, elemento diagonal de $H$; mide cuán lejos está la fila en el espacio de predictores. Como $\sum_i h_{ii}=p+1$, su promedio es $(p+1)/n$. Un caso de alto apalancamiento puede tener residuo pequeño precisamente porque arrastra la recta hacia sí.

La influencia combina apalancamiento y discrepancia. La distancia de Cook puede expresarse como

$$
D_i=\frac{e_i^2}{(p+1)\widehat\sigma^2}
\frac{h_{ii}}{(1-h_{ii})^2}.
$$

Cuantifica cuánto cambiaría globalmente el ajuste al retirar el caso. DFBETAS estudia cambios en coeficientes concretos; residuos eliminados comparan cada punto con un modelo ajustado sin él. Los umbrales difundidos son guías de inspección, no reglas automáticas.

**Ejemplo conceptual.** Una planta registra producción diaria entre 80 y 120 unidades, salvo un día de 300 por una campaña especial. Ese día tiene alto apalancamiento. Si sigue exactamente la tendencia, puede no ser influyente; si usa otra configuración de maquinaria, puede cambiar mucho la pendiente. La pregunta sustantiva es si pertenece a la población futura. Si sí, excluirlo oculta un régimen; si no, tal vez convenga modelar campañas por separado.

El protocolo es: verificar la observación en la fuente, comprender por qué es extrema, calcular sensibilidad del resultado, considerar una variable o régimen omitido y documentar cualquier exclusión. Ajustar con y sin casos influyentes muestra dependencia, pero elegir la versión que favorece una conclusión es selección sesgada.

En dimensiones altas, casi toda fila puede tener apalancamiento apreciable y las medidas clásicas pierden simplicidad. También hay influencia colectiva: varios casos similares se enmascaran mutuamente. Diagnósticos por grupos, tiempo y fuentes complementan índices individuales.

### 11.2.7. Análisis gráfico de residuos

Los gráficos de residuos son instrumentos de falsación: buscan estructura que el modelo no capturó. No prueban que los supuestos se cumplan cuando no muestran patrones. Un conjunto mínimo incluye:

| Gráfico | Patrón buscado | Hipótesis posible |
|---|---|---|
| residuos vs. ajustados | curva, embudo, bandas | no linealidad, varianza cambiante, grupos omitidos |
| residuos vs. predictor | tendencia local | forma funcional incorrecta o interacción |
| Q-Q | asimetría o colas | distribución no normal, extremos |
| escala-localización | dispersión creciente | heterocedasticidad |
| residuos vs. apalancamiento | casos aislados | influencia elevada |
| residuos vs. tiempo | rachas, ciclos, saltos | dependencia o deriva |

Se prefieren residuos estudentizados para comparar observaciones con varianzas distintas. El eje horizontal debe mostrar también densidad o soporte: un suavizado llamativo sostenido por tres puntos no equivale a un patrón en una región poblada. Colorear por turno, tipo de producto o estación puede revelar una variable omitida, pero explorar muchos grupos aumenta riesgo de descubrir azar.

Los gráficos deben construirse tanto en entrenamiento como sobre predicciones fuera de muestra. Los residuos de entrenamiento han sido minimizados y tienden a ser optimistas; los de validación reflejan mejor generalización. En validación temporal, representar errores por fecha permite separar estacionalidad residual y cambio de régimen.

Una secuencia diagnóstica razonable es:

```text
COMPROBAR unidades, faltantes, rangos y momento de disponibilidad
GRAFICAR residuos frente a ajustados, entradas clave, tiempo y grupos
IDENTIFICAR un patrón concreto y formular una explicación de dominio
PROPONER una sola modificación interpretable
EVALUARLA en particiones no usadas para descubrir el patrón
CONSERVARLA solo si mejora estabilidad, riesgo y coherencia operacional
DOCUMENTAR los patrones que permanezcan y sus consecuencias
```

No debe perseguirse una nube «perfectamente aleatoria» añadiendo términos hasta agotar grados de libertad. El propósito es conocer dónde falla la aproximación y si ese fallo compromete la decisión.

### 11.2.8. Ejemplo práctico guiado: diagnóstico y mejora de una regresión

Una fábrica predice minutos de mecanizado por lote a partir de número de piezas, dureza media, antigüedad de la máquina y turno. El modelo aditivo inicial logra MAE de validación 14,2 minutos. El equipo desea reducir error y obtener intervalos útiles para programar capacidad.

**Diagnóstico inicial.** Residuos contra ajustados presentan embudo: la variación crece con tamaño de lote. Residuos contra número de piezas muestran curvatura; los lotes grandes tardan más que la recta. En el tiempo aparecen rachas positivas durante dos semanas, coincidentes con una herramienta desgastada. Dos lotes experimentales tienen alto apalancamiento. El Q-Q revela cola derecha, pero gran parte procede de esos períodos de desgaste.

**Interpretación.** Hay al menos tres mecanismos: economía de preparación para lotes pequeños y saturación para grandes, dispersión proporcional a duración y estado temporal de herramienta omitido. Eliminar los lotes experimentales no resuelve ninguno. La variable «estado final de herramienta» no está disponible antes del mecanizado y sería fuga; sí está disponible el número acumulado de ciclos desde el último reemplazo.

**Modificación.** Se añade una base por tramos para piezas con un nudo operativo en 100, y ciclos desde reemplazo. Se conserva turno como categoría. Para estabilizar error relativo se compara modelar $\log Y$ con mantener $Y$ y usar inferencia robusta. La validación avanza por semanas y todas las elecciones se hacen antes de la prueba final.

El modelo en escala original con tramo queda conceptualmente

$$
Y=\beta_0+\beta_1P+\beta_2(P-100)_+
+\beta_3D+\beta_4C+\boldsymbol\gamma^T\text{turno}+\varepsilon.
$$

Si $\widehat\beta_1=0{,}72$ y $\widehat\beta_2=0{,}31$, cada pieza adicional se asocia con 0,72 minutos hasta 100 piezas y 1,03 minutos después. No hay discontinuidad en el nudo.

**Comparación.** El modelo inicial obtiene MAE 14,2 y RMSE 23,8; el modelo por tramos, MAE 10,9 y RMSE 17,6; el logarítmico, MAE 11,1 y mejor error relativo, pero subestima algunos lotes largos al retransfomarse. Se elige el modelo por tramos porque el costo operativo es absoluto y sus intervalos con varianza modelada alcanzan cobertura más uniforme.

**Influencia y límites.** Los lotes experimentales se conservan y se etiquetan como régimen; el resultado cambia poco al retirarlos después de introducir el tramo. Persisten rachas leves, por lo que se declara dependencia y se calculan incertidumbres agrupadas por semana. El error final se reporta por tamaño, turno y antigüedad. La mejora no se atribuye a «normalizar residuos», sino a representar mecanismos disponibles al momento de decisión y validar su utilidad.

## 11.3. Modelos lineales regularizados

### 11.3.1. Complejidad y sobreajuste

Un modelo flexible reduce error de entrenamiento, pero puede aprender fluctuaciones particulares de la muestra. La diferencia entre buen ajuste interno y mal riesgo futuro es sobreajuste. En modelos lineales, la complejidad aumenta con predictores, bases, interacciones y libertad de sus coeficientes. Cuando $p$ se acerca a $n$, OLS puede tener varianza enorme; si $p\ge n$, incluso puede interpolar los datos sin identificar una solución única.

El compromiso sesgo-varianza se ilustra, para error cuadrático en un punto $\mathbf x$, mediante

$$
\mathbb E[(Y-\widehat f(\mathbf x))^2]
=\sigma^2+\operatorname{Sesgo}[\widehat f(\mathbf x)]^2
+\operatorname{Var}[\widehat f(\mathbf x)].
$$

OLS busca poco sesgo bajo una especificación correcta, pero puede ser muy variable. Regularizar restringe coeficientes, introduce sesgo deliberado y puede reducir varianza más que suficiente para disminuir riesgo total.

La complejidad no es solo cantidad de columnas. Escalas, colinealidad y rango de $X$ determinan cuánto puede oscilar una predicción. La norma de $\boldsymbol\beta$ sirve como control: coeficientes grandes permiten respuestas sensibles a perturbaciones. Las penalizaciones agregan a la pérdida un costo por esa magnitud:

$$
\text{objetivo}=\text{error de ajuste}+\lambda\,\text{complejidad}.
$$

$\lambda=0$ recupera OLS; al crecer $\lambda$, aumenta contracción. No es un parámetro que deba optimizarse sobre prueba. El procedimiento completo, incluida transformación, selección de $\lambda$ y reajuste, se evalúa fuera de muestra.

Regularizar no corrige etiquetas erróneas, fuga, muestreo sesgado ni forma funcional absurda. Tampoco garantiza interpretabilidad causal. Es una herramienta contra varianza y mal condicionamiento. La curva de aprendizaje ayuda a distinguir problemas: una brecha grande entre entrenamiento y validación sugiere varianza; errores altos en ambos pueden indicar sesgo, variables insuficientes o ruido.

### 11.3.2. Regresión Ridge

Ridge minimiza pérdida cuadrática con penalización L2:

$$
\widehat{\boldsymbol\beta}^{R}
=\arg\min_{\boldsymbol\beta}
\left\{\frac{1}{n}\|\mathbf y-X\boldsymbol\beta\|_2^2
+\lambda\sum_{j=1}^{p}\beta_j^2\right\},
$$

donde el intercepto suele excluirse de la suma. Con columnas centradas, la solución es

$$
\widehat{\boldsymbol\beta}^{R}
=(X^TX+n\lambda I)^{-1}X^T\mathbf y.
$$

Agregar $n\lambda$ a la diagonal mejora condicionamiento y garantiza invertibilidad para $\lambda>0$. Ridge no suele producir ceros exactos: conserva señales débiles, pero contraídas.

La SVD muestra qué hace. Si $X=UDV^T$, con valores singulares $d_k$, OLS multiplica cada componente por $1/d_k$; Ridge usa

$$
\frac{d_k}{d_k^2+n\lambda}.
$$

Las direcciones con $d_k$ pequeño, mal determinadas por los datos, sufren mayor contracción. Esto explica su eficacia con predictores correlacionados. Si dos sensores energéticos casi duplican información, OLS puede asignarles coeficientes opuestos inestables; Ridge tiende a repartir el efecto.

Existe una forma restringida equivalente: minimizar SSE sujeto a $\|\boldsymbol\beta\|_2^2\le t$. Geométricamente, las elipses de pérdida tocan una esfera suave. Como la frontera no tiene esquinas, el contacto rara vez ocurre exactamente en un eje; de ahí que no seleccione variables.

El sesgo de Ridge invalida aplicar sin más la inferencia clásica de OLS. Su objetivo usual es predicción estable. Los grados de libertad efectivos son

$$
df(\lambda)=\operatorname{tr}\{X(X^TX+n\lambda I)^{-1}X^T\},
$$

que decrecen continuamente con la penalización. Ridge es particularmente útil cuando muchas variables aportan efectos pequeños y correlacionados, como términos de texto o indicadores económicos. Si se necesita retirar fuentes completas, coeficientes pequeños no equivalen a selección operacional.

### 11.3.3. Regresión Lasso

Lasso emplea la norma L1:

$$
\widehat{\boldsymbol\beta}^{L}
=\arg\min_{\boldsymbol\beta}
\left\{\frac{1}{n}\|\mathbf y-X\boldsymbol\beta\|_2^2
+\lambda\sum_{j=1}^{p}|\beta_j|\right\}.
$$

La región restringida $\|\boldsymbol\beta\|_1\le t$ posee esquinas sobre los ejes. Las elipses de pérdida suelen tocarla en una esquina, generando coeficientes exactamente cero. Lasso combina contracción y selección embebida.

Con predictores ortonormales, la solución se entiende mediante umbral suave. Si $z_j$ es el coeficiente OLS en la escala correspondiente,

$$
\widehat\beta_j^{L}=\operatorname{sign}(z_j)
(|z_j|-c\lambda)_+,
$$

con $c$ dependiente de la convención de escala. Señales bajo el umbral desaparecen; las restantes se acercan a cero. En general no hay fórmula cerrada conjunta y se usan métodos de optimización como descenso por coordenadas, pero el objetivo es convexo.

La selección no convierte los términos no nulos en «variables verdaderas». Con dos predictores muy correlacionados, Lasso puede elegir uno y descartar otro ante una mínima perturbación. La predicción puede ser estable mientras la lista no lo es. Se deben examinar frecuencias de selección en remuestreos, trayectorias y grupos de variables originales, especialmente cuando una categoría produce varios indicadores.

Lasso es atractivo cuando existe una representación potencialmente grande y se espera esparsidad, como miles de términos textuales con pocos relevantes por tarea. Puede seleccionar como máximo un número limitado de variables en ciertos regímenes y sesga efectos grandes por la misma penalización lineal. Tras seleccionar y volver a ajustar OLS se reduce contracción, pero se reintroduce varianza y la inferencia ingenua ignora que la selección miró $Y$.

Si el fin es inferencial, se necesitan procedimientos postselección específicos o una separación confirmatoria. Para predicción, lo esencial es que toda selección ocurra dentro de validación. Un coeficiente cero significa que esa variable no fue necesaria para esa solución penalizada, escala y muestra; no prueba ausencia de asociación ni de efecto causal.

### 11.3.4. Elastic Net

Elastic Net combina L1 y L2:

$$
\widehat{\boldsymbol\beta}^{EN}
=\arg\min_{\boldsymbol\beta}
\left\{\frac{1}{n}\|\mathbf y-X\boldsymbol\beta\|_2^2
+\lambda\left[\alpha\sum_j|\beta_j|
+\frac{1-\alpha}{2}\sum_j\beta_j^2\right]\right\}.
$$

$\alpha=1$ corresponde a Lasso y $\alpha=0$ a Ridge, según esta parametrización. $\lambda$ controla fuerza global; $\alpha$, mezcla. La parte L1 produce ceros y la L2 estabiliza grupos correlacionados.

Supóngase que un modelo financiero incluye tasas a 3, 6 y 12 meses, altamente correlacionadas. Ridge conserva las tres con pesos repartidos; Lasso puede escoger una de modo inestable; Elastic Net puede retener un subconjunto conjunto con menor sensibilidad. El «efecto de agrupamiento» no garantiza seleccionar grupos semánticos completos, pero reduce la competición extrema de Lasso.

Elastic Net es útil cuando $p>n$, hay bloques de variables relacionadas y se desea alguna esparsidad. Añade un hiperparámetro, por lo que aumenta búsqueda y riesgo de sobreajustar la validación. Se evalúa una cuadrícula razonable de $(\alpha,\lambda)$ dentro de cada pliegue, no una exploración ilimitada sobre el conjunto de prueba.

La elección entre las tres familias responde al objetivo. Si muchas señales pequeñas son plausibles y se prioriza estabilidad, Ridge. Si se espera una solución escasa y retirar variables tiene valor, Lasso, verificando estabilidad. Si ambas condiciones coexisten, Elastic Net. Estas son hipótesis que la validación puede refutar, no recetas automáticas.

También existen penalizaciones estructuradas: Group Lasso selecciona grupos, y otras variantes respetan jerarquía o suavidad. No deben introducirse solo por sofisticación. Si una categoría se representa con diez indicadores, penalizarlos como grupo puede ser más coherente que permitir que sobrevivan niveles aislados, pero requiere definir esa unidad antes de observar resultados.

### 11.3.5. Estandarización y regularización

Las penalizaciones actúan sobre coeficientes, por lo que dependen de unidades. Si $X_1$ se expresa en euros y $X_2$ en miles de euros, idéntico efecto predictivo requiere coeficientes de magnitudes distintas y recibe penalizaciones distintas. Se estandarizan las continuas:

$$
z_{ij}=\frac{x_{ij}-\bar x_j}{s_j},
$$

usando media y desviación aprendidas solo en entrenamiento. El objetivo se centra de modo similar; el intercepto queda sin penalizar. Tras ajustar, puede recuperarse la escala original para interpretación.

La estandarización no vuelve comparables todos los cambios. Una desviación estándar de ingreso quizá sea un cambio amplio, mientras una de temperatura sea habitual. Tampoco corrige asimetría, extremos ni unidades equivocadas. Para distribuciones de cola pesada puede considerarse una escala robusta, pero debe formar parte del procedimiento validado.

Las variables binarias plantean una decisión. Estandarizarlas iguala varianza y puede penalizar menos los niveles raros en escala original; dejarlas en 0/1 conserva lectura, pero la fuerza efectiva difiere. No hay regla universal: se documenta la convención y, para variables categóricas, puede usarse una penalización por grupos. Nunca se estandariza el intercepto.

**Fuga frecuente.** Calcular $\bar x_j$ y $s_j$ sobre todo el conjunto antes de validación comunica información de validación al entrenamiento. Aunque no use directamente $Y$, altera la representación y puede optimizar resultados. En cada pliegue se ajustan imputación, codificación, escala y modelo únicamente con la parte de entrenamiento.

La estandarización también mejora optimización, pues evita contornos extremadamente alargados. Una columna de varianza cero no puede escalarse y debe tratarse explícitamente. En producción se persisten los parámetros del entrenamiento; recalcular medias con cada lote cambiaría silenciosamente el modelo. Si la distribución deriva, se monitoriza y se decide un reentrenamiento completo, no una normalización improvisada.

### 11.3.6. Selección del parámetro de penalización

$\lambda$ se elige para minimizar una estimación de riesgo futuro, no SSE de entrenamiento. Se define una secuencia logarítmica desde penalización casi nula hasta una que contrae fuertemente. Para cada valor se repite el pipeline en los mismos pliegues y se agrega la métrica operacional.

```text
DEFINIR particiones coherentes con el despliegue y una rejilla de penalizaciones
PARA cada lambda (y cada alpha, si corresponde):
    PARA cada pliegue:
        ajustar preprocesamiento con entrenamiento interno
        ajustar el modelo penalizado
        evaluar en validación interna intacta
    calcular media, dispersión y estabilidad de coeficientes
ELEGIR según una regla predefinida
REAJUSTAR el pipeline con todos los datos de desarrollo
EVALUAR una vez en prueba externa
```

La curva de validación suele ser plana cerca del mínimo. Elegir el valor con menor decimal aparenta precisión inexistente. La regla de un error estándar selecciona la mayor penalización cuyo error está dentro de un error estándar del mínimo; favorece parsimonia y estabilidad. Debe declararse de antemano y el error estándar debe respetar dependencia entre pliegues.

Una validación aleatoria no sirve para toda tarea. En movilidad temporal se usan cortes futuros; en agricultura regional, grupos geográficos; en texto, documentos de la misma fuente pueden necesitar agruparse. Si se comparan muchos hiperparámetros, el ganador sobreajusta los pliegues. Una validación anidada estima el procedimiento completo: el bucle interno elige $\lambda$ y el externo evalúa.

Además de pérdida media se examinan error por subgrupo, número de coeficientes no nulos, estabilidad de selección y sensibilidad a valores vecinos. La penalización óptima puede cambiar si cambia la métrica. Un $\lambda$ que minimiza RMSE no necesariamente minimiza costo de adquisición de variables.

Después de reajustar, no se informa el error interno como rendimiento definitivo. La prueba intacta o evaluación prospectiva mantiene la separación entre selección y estimación. En despliegue, $\lambda$ no se adapta continuamente mirando resultados futuros sin versionar y reevaluar todo el procedimiento.

### 11.3.7. Ejemplo práctico guiado: comparación de regresiones regularizadas

Una entidad financiera predice pérdida mensual de una cartera a partir de 180 indicadores: saldos, atrasos por ventana, tasas, variables macroeconómicas y decenas de razones correlacionadas. Hay 900 meses-segmento de desarrollo. El objetivo es predicción estable; una lista corta es deseable, pero no a costa de perder grupos de señales.

Se separa el último año como prueba y se valida con ventanas temporales. En cada pliegue se imputan medianas, se estandarizan continuas y se ajustan OLS, Ridge, Lasso y Elastic Net. El baseline usa la pérdida del mes anterior. Para Elastic Net se prueban pocos valores predefinidos de $\alpha$; para cada familia se aplica la regla de un error estándar.

| Modelo | RMSE de prueba | Coeficientes no nulos | Estabilidad cualitativa |
|---|---:|---:|---|
| baseline | 1,00 | — | alta, pero rezagado ante cambios |
| OLS | 0,94 | 180 | baja; signos cambian entre ventanas |
| Ridge | 0,78 | 180 | alta |
| Lasso | 0,83 | 24 | baja entre indicadores sustitutos |
| Elastic Net | 0,79 | 51 | media-alta |

Los errores están normalizados respecto del baseline. OLS mejora poco y presenta grandes coeficientes opuestos para atrasos a 30 y 60 días. Ridge los contrae y obtiene el mejor RMSE. Lasso produce la solución más escasa, pero el conjunto cambia: selecciona atraso a 30 días en unas ventanas y a 60 en otras. Elastic Net conserva ambos con pesos moderados y casi iguala Ridge.

La trayectoria muestra que, con $\lambda$ pequeño, la varianza entre pliegues es alta; una región intermedia estabiliza error; penalización excesiva aproxima el intercepto y empeora. Elegir solo por cantidad de ceros habría favorecido Lasso, ignorando 6% de pérdida relativa frente a Ridge. Como mantener 180 columnas no implica 180 fuentes distintas, el ahorro operacional de Lasso era menor de lo supuesto.

Se elige Elastic Net aunque Ridge tenga una ventaja mínima: su error queda dentro de incertidumbre, reduce términos y mantiene grupos. Se conservan como bloque todas las columnas necesarias para calcular una razón seleccionada; no se afirma que las 51 sean causas de pérdida. Una prueba de estrés con subida abrupta de tasas revela subestimación común a todos los modelos, señal de cambio fuera del soporte, no problema resoluble ajustando $\lambda$.

El informe incluye curvas de validación, distribución temporal del error, frecuencia de selección y parámetros de escalado. La conclusión es comparativa: regularizar mejora estabilidad frente a OLS; Lasso aporta esparsidad inestable; Elastic Net ofrece el compromiso más útil bajo el costo declarado.

## 11.4. Regresión logística y clasificación

### 11.4.1. Formulación de la clasificación binaria

En clasificación binaria, $Y\in\{0,1\}$. El objetivo estadístico puede ser estimar

$$
p(\mathbf x)=P(Y=1\mid X=\mathbf x),
$$

y el objetivo decisional, tomar una acción a partir de esa probabilidad. Son etapas distintas. Una probabilidad bien estimada permite múltiples políticas; una etiqueta rígida oculta incertidumbre y costos.

La codificación de la clase positiva debe declararse. En detección de incumplimiento financiero, $Y=1$ podría significar impago; sensibilidad y precisión se referirán entonces a ese evento. Cambiar etiquetas transforma interpretaciones aunque no la información.

Una regla de clase $a(\mathbf x)\in\{0,1\}$ tiene riesgo esperado según una matriz de costos. Si un falso negativo cuesta $C_{FN}$ y un falso positivo $C_{FP}$, sin otros costos se elige clase 1 cuando

$$
C_{FP}[1-p(\mathbf x)]<C_{FN}p(\mathbf x),
$$

equivalentemente $p(\mathbf x)>C_{FP}/(C_{FP}+C_{FN})$. Por tanto, el umbral 0,5 solo es óptimo con costos simétricos y probabilidades aplicables a la población de decisión.

La prevalencia $P(Y=1)$ condiciona métricas y baselines. Con 1% de positivos, predecir siempre cero logra 99% de exactitud y ninguna utilidad para detectar positivos. Se reportan matriz de confusión, sensibilidad, especificidad, precisión, métricas de ranking y pérdidas probabilísticas según el uso. Precisión depende especialmente de prevalencia; no se transporta sin más a otra población.

La partición debe impedir fuga. En clasificación de documentos, versiones del mismo texto no pueden repartirse entre entrenamiento y prueba; en crédito, variables posteriores al incumplimiento no son entradas válidas. También se define una ventana para observar la etiqueta: casos recientes cuyo resultado aún no maduró no son negativos, sino censurados o desconocidos.

### 11.4.2. Función logística

Un modelo lineal aplicado directamente a etiquetas puede producir valores fuera de $[0,1]$ y asumir varianza constante, incompatible con Bernoulli. La regresión logística modela un puntaje lineal $\eta=\beta_0+\mathbf x^T\boldsymbol\beta$ y lo transforma mediante la sigmoide:

$$
\sigma(\eta)=\frac{1}{1+e^{-\eta}},
\qquad
p(\mathbf x)=\sigma(\eta).
$$

La función es monótona, está acotada y satisface $\sigma(0)=0{,}5$ y $\sigma(-\eta)=1-\sigma(\eta)$. Su derivada es

$$
\frac{dp}{d\eta}=p(1-p),
$$

máxima en $p=0{,}5$ y pequeña cerca de 0 o 1. Por eso un mismo cambio en el puntaje produce mayor cambio absoluto de probabilidad en casos inciertos que en extremos.

La frontera para umbral 0,5 es $\eta=0$, un hiperplano en las características transformadas. El modelo puede representar fronteras curvas si $X$ incluye términos polinómicos o interacciones, aunque sigue siendo lineal en parámetros. El umbral no cambia el ranking; desplaza la frontera paralelamente para otros valores.

**Ejemplo.** Si $\eta=-3+0{,}8x$ y $x=4$, entonces $\eta=0{,}2$ y $p=1/(1+e^{-0{,}2})\approx0{,}55$. Para $x=5$, $\eta=1$ y $p\approx0{,}731$. El incremento de probabilidad no es constante: depende del punto inicial.

Numéricamente, probabilidades extremas deben manejarse en escala estable, pero la teoría no cambia. La sigmoide no garantiza calibración: solo restringe la forma. Si faltan no linealidades, cambia la prevalencia o se seleccionó la muestra, las probabilidades pueden ser sistemáticamente erróneas.

### 11.4.3. Odds y log-odds

Los **odds** o momios de un evento son

$$
\operatorname{odds}(p)=\frac{p}{1-p}.
$$

Una probabilidad de 0,75 corresponde a odds 3:1; una de 0,20, a 1:4. Probabilidad y odds no son lo mismo: aumentar odds en 50% no suma 50 puntos porcentuales.

La transformación logit es el logaritmo de los odds:

$$
\operatorname{logit}(p)=\log\frac{p}{1-p}
=\beta_0+\sum_j\beta_jx_j.
$$

Convierte $(0,1)$ en toda la recta real. En esta escala, cada coeficiente es aditivo. Si $x_j$ aumenta una unidad manteniendo el resto fijo, los log-odds aumentan $\beta_j$ y los odds se multiplican por $e^{\beta_j}$. $e^{\beta_j}$ es la razón de odds.

Si $\beta_j=0{,}40$, la razón de odds es $e^{0{,}40}\approx1{,}49$: los odds son 49% mayores. No significa que la probabilidad aumente 49% ni 0,40. Si la probabilidad inicial es 0,10, los odds pasan de 0,111 a 0,166 y la probabilidad a 0,142; si era 0,70, pasa a aproximadamente 0,777. El efecto en puntos porcentuales depende de todas las entradas.

Para comunicar efectos se pueden mostrar probabilidades predichas en perfiles representativos o efectos marginales

$$
\frac{\partial p}{\partial x_j}=\beta_jp(1-p).
$$

El promedio de estos efectos sobre la muestra resume una escala de probabilidad, pero sigue condicionado al modelo y población. Con interacción, $\beta_j$ deja de ser una razón de odds constante para todos los valores del modificador.

La razón de odds también requiere cautela en eventos frecuentes: puede parecer mucho mayor que la razón de riesgos. Un odds ratio de 2 no implica duplicar probabilidad. En estudios observacionales, ni siquiera una razón ajustada demuestra causalidad sin identificación adecuada.

### 11.4.4. Estimación e interpretación de coeficientes

Condicionado a $X$, se modela $Y_i\sim\operatorname{Bernoulli}(p_i)$ con $p_i=\sigma(\mathbf x_i^T\boldsymbol\beta)$. La verosimilitud es

$$
L(\boldsymbol\beta)=\prod_{i=1}^n
p_i^{y_i}(1-p_i)^{1-y_i}.
$$

Tomar logaritmos da

$$
\ell(\boldsymbol\beta)=\sum_i
\left[y_i\log p_i+(1-y_i)\log(1-p_i)\right].
$$

Maximizar $\ell$ equivale a minimizar log-loss o entropía cruzada. Sustituyendo la sigmoide,

$$
-\ell=\sum_i\left[\log(1+e^{\eta_i})-y_i\eta_i\right].
$$

El gradiente es $X^T(\mathbf p-\mathbf y)$ y la Hessiana $X^TWX$, con $W$ diagonal y $w_i=p_i(1-p_i)$. No existe, en general, solución cerrada; algoritmos iterativos como Newton-Raphson o mínimos cuadrados reponderados convergen al óptimo convexo si el problema está bien planteado.

En el máximo, $X^T(\mathbf y-\mathbf p)=0$. Con intercepto, $\sum y_i=\sum p_i$: la cantidad esperada total coincide con la observada en entrenamiento, propiedad que no garantiza calibración fuera de muestra.

La varianza asintótica se estima mediante $(X^T\widehat W X)^{-1}$ bajo especificación correcta. Puede construirse un intervalo para $\beta_j$ y exponentiar extremos para obtener uno de la razón de odds. Valores $p$, intervalos y coeficientes sufren los mismos problemas de multiplicidad, colinealidad y selección que en regresión lineal.

Un problema especial es la **separación**: una característica o combinación distingue perfectamente clases. La verosimilitud aumenta al llevar ciertos coeficientes a infinito y el MLE finito no existe. Coeficientes enormes y errores de convergencia son síntomas. Reunir más datos con solapamiento, revisar fuga o aplicar regularización son soluciones; eliminar arbitrariamente casos difíciles no lo es.

La regularización logística añade L1, L2 o Elastic Net a la log-loss. Mejora estabilidad en alta dimensión, como clasificación textual, pero exige estandarización y selección de hiperparámetros dentro de validación. La interpretación corresponde al modelo penalizado y no hereda automáticamente inferencia clásica.

### 11.4.5. Probabilidades y umbrales de decisión

Una probabilidad es una estimación de riesgo; un umbral la convierte en acción:

$$
\widehat y_t=I(\widehat p\ge t).
$$

Al bajar $t$ aumentan verdaderos positivos y falsos positivos; al subirlo, disminuyen ambos. La matriz de confusión contiene $TP$, $FP$, $TN$ y $FN$. De ella se derivan

$$
\text{sensibilidad}=\frac{TP}{TP+FN},\quad
\text{especificidad}=\frac{TN}{TN+FP},\quad
\text{precisión}=\frac{TP}{TP+FP}.
$$

La curva ROC representa sensibilidad frente a tasa de falsos positivos para todos los umbrales; su AUC es la probabilidad de ordenar un positivo al azar por encima de un negativo al azar. No mide calibración ni utilidad en un umbral concreto. Con clases raras, la curva precisión-recall suele mostrar mejor el compromiso sobre la clase positiva.

El umbral se elige con datos de validación y costos definidos, nunca maximizando retrospectivamente una métrica en prueba. Si revisar una alerta cuesta 5 unidades y omitir un caso prioritario cuesta 80, la política minimiza costo esperado y puede estar lejos de 0,5. También hay restricciones: «revisar como máximo 200 casos diarios» induce seleccionar los mayores riesgos hasta agotar capacidad; el umbral variará con volumen.

F1 armoniza precisión y sensibilidad, pero ignora verdaderos negativos y fija implícitamente una valoración. La exactitud balanceada pondera clases, pero tampoco representa todos los costos. Una política defendible informa métrica, prevalencia, capacidad y costo.

Puede existir una zona de abstención: aceptar por debajo de $t_b$, revisar manualmente entre $t_b$ y $t_a$, actuar automáticamente por encima de $t_a$. La abstención no elimina errores; redistribuye casos y requiere medir cobertura, desempeño y carga humana. Los umbrales por grupo pueden satisfacer restricciones distintas, pero plantean cuestiones legales y de equidad y deben evaluarse cuidadosamente.

Tras desplegar, cambios de prevalencia alteran precisión y costo aunque ROC permanezca similar. Se monitorizan probabilidades, decisiones, resultados demorados y capacidad. Reoptimizar el umbral sin recalibrar ni considerar nueva población puede empeorar el sistema.

### 11.4.6. Clasificación multiclase

Cuando $Y\in\{1,\ldots,K\}$, se necesitan probabilidades que sumen uno. La regresión logística multinomial usa *softmax*:

$$
P(Y=k\mid\mathbf x)=
\frac{\exp(\eta_k)}{\sum_{r=1}^{K}\exp(\eta_r)},
\qquad
\eta_k=\beta_{0k}+\mathbf x^T\boldsymbol\beta_k.
$$

Como sumar la misma constante a todos los puntajes no cambia probabilidades, se fija una clase de referencia o una restricción. Respecto de referencia $K$,

$$
\log\frac{P(Y=k\mid X)}{P(Y=K\mid X)}
=\beta_{0k}+X^T\boldsymbol\beta_k.
$$

Cada coeficiente modifica log-odds de clase $k$ frente a la referencia, condicionado a las demás. Cambiar referencia altera tablas, no probabilidades.

Otra estrategia es uno contra el resto: se ajustan $K$ clasificadores binarios. Es flexible, pero sus probabilidades no suman necesariamente uno y cada tarea enfrenta prevalencia distinta. Uno contra uno ajusta pares y combina votos; resulta costoso cuando $K$ crece. Softmax aprende las clases conjuntamente y suele ser la opción lineal coherente cuando son mutuamente excluyentes.

No debe confundirse multiclase con multietiqueta. Un documento puede pertenecer simultáneamente a «finanzas» y «regulación»; entonces se estiman eventos binarios relacionados y no se fuerza suma uno. Si las clases tienen orden, una regresión ordinal puede aprovecharlo en vez de tratarlas como nominales.

La evaluación incluye matriz de confusión y métricas por clase. El promedio macro da igual peso a clases; el micro agrega decisiones y favorece clases frecuentes; el ponderado queda entre ambos. Top-$k$ es útil si se muestran varias alternativas, pero debe corresponder a la interfaz. Log-loss multiclase evalúa probabilidades y penaliza confianza equivocada.

En producción pueden aparecer clases nuevas. Forzarlas a una categoría conocida genera errores confiados. Detección de fuera de distribución, una clase «otro» entrenada con ejemplos representativos o abstención son políticas posibles, ninguna garantizada solo por softmax.

### 11.4.7. Calibración de probabilidades

Un predictor está calibrado si, entre casos a los que asigna probabilidad $q$, aproximadamente una fracción $q$ resulta positiva:

$$
P(Y=1\mid \widehat p=q)=q.
$$

Calibración y discriminación son diferentes. Un modelo puede ordenar perfectamente riesgos pero asignar 0,9 donde ocurre 0,6; otro puede estar calibrado prediciendo la prevalencia a todos, sin discriminar. Las decisiones basadas en costos necesitan ambas.

El **Brier score** es

$$
BS=\frac1n\sum_i(\widehat p_i-y_i)^2,
$$

y combina calibración y resolución. Log-loss penaliza con fuerza probabilidades extremas erróneas. Un diagrama de confiabilidad agrupa predicciones y compara promedio predicho con frecuencia observada; debe acompañarse de cantidad de casos por intervalo e incertidumbre. Pocos casos en 0,9 no permiten afirmar mala calibración por una diferencia aislada.

El intercepto de calibración detecta sesgo global y una pendiente de calibración menor que uno suele indicar probabilidades demasiado extremas. Métricas como error esperado de calibración dependen del binning y pueden ocultar compensaciones; no deben reportarse solas.

La calibración se evalúa en datos no usados para ajustar el modelo. Si se corrige, se necesita una partición adicional o predicciones fuera de pliegue. El escalado de Platt ajusta una transformación logística del puntaje; la regresión isotónica aprende una función monótona más flexible y necesita más datos. La calibración por temperatura es común en multiclase. Ajustar y evaluar el calibrador sobre los mismos casos produce optimismo.

Cambios de prevalencia y de relación $P(Y\mid X)$ degradan calibración. Un modelo de prioridad entrenado durante una campaña puede sobreestimar riesgo después. Recalibrar intercepto puede bastar bajo cambio de prevalencia simple; si cambian relaciones, se requiere revisión mayor. La calibración debe comprobarse globalmente, por tiempo y en grupos con suficiente tamaño, sin asumir que calibración total implica calibración en cada subpoblación.

### 11.4.8. Ejemplo práctico guiado: clasificación de reclamos prioritarios

Una plataforma financiera recibe reclamos escritos y debe priorizar cuáles revisar en menos de dos horas. Un comité define $Y=1$ cuando el caso combina posible perjuicio económico inmediato y plazo regulatorio breve. La etiqueta procede de revisión posterior, no de la prioridad histórica, para evitar copiar decisiones anteriores. La unidad es reclamo inicial; mensajes posteriores no están disponibles al ingreso.

**Datos y representación.** Se usan canal, producto, antigüedad de la cuenta, importe discutido, hora, historial agregado anterior y términos del texto inicial. Identidad personal se excluye salvo necesidad justificada. Reclamos del mismo expediente permanecen en el mismo grupo. Los últimos dos meses constituyen prueba temporal; dentro del desarrollo, validaciones avanzan en el tiempo. Un baseline asigna la prevalencia y otro usa una regla vigente por palabras clave.

**Modelo.** Una regresión logística con Elastic Net resulta apropiada para miles de términos correlacionados y variables estructuradas. Escala, vocabulario, ponderaciones y penalización se aprenden dentro de cada pliegue. El modelo entrega $\widehat p$, no prioridad automática. En prueba obtiene ROC-AUC 0,88, PR-AUC 0,54 frente a prevalencia 0,12, Brier 0,083 y log-loss 0,286. La regla previa alcanza PR-AUC 0,31.

**Calibración.** El diagrama muestra sobreconfianza: casos predichos alrededor de 0,8 son prioritarios en 0,68. Se ajusta un calibrador con predicciones fuera de pliegue, sin tocar prueba. Tras calibrar, Brier baja a 0,075; ROC-AUC casi no cambia, como es esperable porque el ranking se conserva. En el período de prueba, el intervalo 0,6–0,7 contiene 64% positivos con muestra suficiente.

**Umbral operacional.** Revisar cuesta 8 unidades; omitir un prioritario, 120. El umbral teórico con esos costos sería $8/(8+120)=0{,}0625$, pero la capacidad diaria limita revisiones al 35%. Se simulan políticas en validación. El umbral 0,18 usa 34% de capacidad, logra sensibilidad 0,91 y precisión 0,32. El umbral 0,50 usa 11%, sensibilidad 0,58 y precisión 0,61. El primero evita más omisiones y satisface capacidad, por lo que se elige. No se selecciona sobre prueba.

Se establece además una política de tres zonas:

| Probabilidad calibrada | Acción |
|---|---|
| $p<0{,}18$ | cola ordinaria, con muestreo de auditoría |
| $0{,}18\le p<0{,}65$ | revisión prioritaria humana |
| $p\ge0{,}65$ | revisión inmediata; nunca resolución automática adversa |

La auditoría aleatoria de la cola baja permite estimar falsos negativos y descubrir deriva. La zona alta acelera atención, pero una explicación textual no reemplaza el expediente.

**Interpretación.** Razones de odds elevadas aparecen para plazos próximos y determinados términos de urgencia; importes y antigüedad interactúan. No se publican palabras como causas ni reglas: el significado depende de coocurrencias y las personas podrían adaptar lenguaje. Se revisan falsos positivos, como usos negados de términos urgentes, y falsos negativos, como mensajes breves sin vocabulario explícito.

**Equidad y seguimiento.** Se evalúan sensibilidad, precisión y calibración por canal y tipo de producto. Diferencias pueden surgir por calidad textual o acceso digital. No se corrigen ocultando un atributo sin estudiar sus proxies. Cada semana se monitorizan prevalencia madura, capacidad, distribución de puntajes, tasa de abstención y desempeño por grupo; las etiquetas retrasadas se analizan por cohorte. Un cambio normativo activa reevaluación y versionado.

El resultado final es un sistema de apoyo: una probabilidad validada, una política de umbral ligada a costo y capacidad, revisión humana y auditoría. El éxito no se resume en AUC; incluye calibración, cobertura, tiempo de atención y consecuencias de los errores.

## Síntesis

La regresión lineal aproxima una media condicional mediante una combinación de características. OLS puede entenderse algebraicamente, como solución de ecuaciones normales, y geométricamente, como proyección de $\mathbf y$ sobre el espacio columna de $X$. Esta geometría explica ortogonalidad de residuos, apalancamiento y sensibilidad al condicionamiento. Los coeficientes tienen una interpretación condicionada por unidades, transformaciones, categorías, interacciones y población; no adquieren significado causal automáticamente.

Los supuestos cumplen funciones diferentes. Esperanza condicional lineal sostiene la especificación; independencia y homocedasticidad sustentan la varianza clásica; normalidad permite inferencia exacta en muestras finitas; rango completo identifica coeficientes. Una violación no conduce siempre a descartar el modelo, pero sí obliga a determinar qué conclusión afecta. Gráficos, sensibilidad, diseño de validación y conocimiento del dominio se complementan.

Ridge, Lasso y Elastic Net controlan complejidad mediante normas L2, L1 y mixtas. Su utilidad surge del compromiso sesgo-varianza, especialmente con muchas variables o colinealidad. Escalar dentro de cada pliegue y elegir penalización sin consultar prueba forman parte del estimador. Esparsidad no equivale a verdad y estabilidad predictiva no garantiza estabilidad de selección.

La regresión logística modela log-odds lineales y estima parámetros por máxima verosimilitud. Sus probabilidades deben distinguirse de la decisión: umbrales dependen de costos, capacidad, prevalencia y restricciones. Ranking, calibración y utilidad son propiedades distintas. En multiclase, softmax coordina probabilidades; en cualquier caso, evaluación y recalibración deben reflejar la población de uso.

La lección transversal es metodológica: especificar primero la pregunta y el momento de información; ajustar sin fuga; comparar con un baseline; diagnosticar dónde falla; cuantificar incertidumbre; y separar una descripción estadística de una acción operacional.

## Glosario

- **Apalancamiento:** singularidad de una observación en el espacio de predictores, medida en OLS por $h_{ii}$.
- **Calibración:** concordancia entre probabilidades predichas y frecuencias observadas.
- **Coeficiente:** parámetro que cuantifica un cambio en la escala lineal o de enlace, condicionado a los demás términos.
- **Elastic Net:** regularización que combina penalizaciones L1 y L2.
- **Error:** diferencia no observable entre respuesta y media poblacional modelada.
- **Heterocedasticidad:** variación de la varianza condicional del error entre observaciones.
- **Influencia:** grado en que una observación altera coeficientes o predicciones ajustadas.
- **Interacción:** término que permite que el efecto de una variable dependa de otra.
- **Lasso:** regresión penalizada por norma L1, capaz de producir coeficientes cero.
- **Logit:** logaritmo de los odds, $\log[p/(1-p)]$.
- **Máxima verosimilitud:** elección de parámetros que hace más compatibles los datos observados con el modelo probabilístico.
- **Mínimos cuadrados ordinarios:** estimación que minimiza la suma de residuos al cuadrado.
- **Multicolinealidad:** dependencia lineal fuerte o exacta entre columnas de la matriz de diseño.
- **Odds:** cociente entre probabilidad de evento y de no evento, $p/(1-p)$.
- **Regularización:** restricción o penalización que controla complejidad y estabiliza estimaciones.
- **Residuo:** diferencia observable $y_i-\widehat y_i$ después del ajuste.
- **Ridge:** regresión penalizada por norma L2, que contrae coeficientes sin hacerlos usualmente cero.
- **Sigmoide:** función $1/(1+e^{-z})$ que transforma un puntaje real en probabilidad.
- **Umbral:** punto de corte que convierte una probabilidad en una acción o clase.
- **Verosimilitud:** función de los parámetros inducida por la probabilidad de los datos observados.

## Preguntas de revisión

1. ¿Por qué la media condicional minimiza el error cuadrático esperado? Derive la descomposición correspondiente.
2. ¿Qué diferencia hay entre error poblacional y residuo? ¿Cuál puede observarse?
3. Derive $\widehat\beta_0$ y $\widehat\beta_1$ en regresión simple a partir de las ecuaciones normales.
4. Explique la solución OLS como una proyección. ¿Qué significa $X^T\mathbf e=0$?
5. ¿Por qué invertir explícitamente $X^TX$ puede ser numéricamente desaconsejable?
6. Interprete un coeficiente de una variable continua, uno categórico y uno de interacción, indicando sus referencias.
7. ¿Qué supuestos requiere Gauss-Markov y qué conclusión permite? ¿Exige normalidad?
8. Distinga las consecuencias de heterocedasticidad para coeficientes, errores estándar e intervalos predictivos.
9. ¿Por qué la multicolinealidad puede perjudicar interpretación sin arruinar predicciones internas?
10. Compare apalancamiento, residuo e influencia mediante un caso conceptual.
11. Explique cómo Ridge modifica las direcciones asociadas con valores singulares pequeños.
12. ¿Por qué Lasso genera ceros y por qué esos ceros pueden ser inestables?
13. ¿Qué información debe aprenderse dentro de cada pliegue al validar un modelo regularizado?
14. Derive el gradiente de la log-verosimilitud logística y explique por qué no hay fórmula cerrada usual.
15. Con probabilidad inicial 0,20 y coeficiente logístico 0,7, calcule la nueva probabilidad tras aumentar una unidad el predictor.
16. ¿Por qué AUC alta no implica buena calibración ni una política útil?
17. Obtenga el umbral óptimo con costos $C_{FP}=10$ y $C_{FN}=90$, bajo los supuestos del texto.
18. Compare softmax, uno contra el resto y clasificación multietiqueta.
19. Diseñe una partición válida para predecir demanda futura y otra para clasificar textos con versiones duplicadas.
20. Enumere tres afirmaciones que un coeficiente predictivo no autoriza a realizar.

## Actividad integradora

Una cooperativa agrícola desea estimar el rendimiento de una próxima cosecha y clasificar parcelas con riesgo alto de rendimiento insuficiente. Dispone de superficie, variedad, fecha de siembra, análisis de suelo, pronósticos disponibles al inicio de campaña, historial de rendimientos y prácticas declaradas. Algunas parcelas pertenecen a la misma explotación y las campañas están ordenadas temporalmente.

Elabore un informe técnico, sin implementar software, que contenga:

1. Definición de unidad, momento de corte, horizonte, objetivo continuo y etiqueta binaria. Identifique al menos tres fugas posibles.
2. Un baseline de regresión y otro de clasificación, con métricas justificadas.
3. Una matriz de diseño conceptual con continuas, una categoría, una transformación y una interacción. Escriba ambos modelos mediante fórmulas.
4. Interpretación completa de cinco coeficientes hipotéticos, incluidas unidades y condiciones «manteniendo constante».
5. Derivación matricial de OLS y explicación geométrica para esa matriz.
6. Plan diagnóstico que trate linealidad, dependencia por explotación, heterocedasticidad, residuos, colinealidad e influencia.
7. Comparación razonada de OLS, Ridge, Lasso y Elastic Net. Anticipe qué ocurrirá con variables climáticas correlacionadas.
8. Pseudocódigo de validación temporal y agrupada en el que preprocesamiento y selección de penalización ocurran sin fuga.
9. Para el clasificador, una tabla con probabilidades hipotéticas y resultados que permita calcular log-loss, Brier, sensibilidad, precisión y especificidad en dos umbrales.
10. Una política de decisión basada en costos de inspección, costo de omisión y capacidad máxima. Incluya opción de abstención.
11. Un diagrama de calibración conceptual y una propuesta de recalibración que preserve un conjunto de evaluación intacto.
12. Una sección final de límites: extrapolación climática, cambio de variedades, retraso de etiquetas, equidad entre explotaciones y monitorización.

La evaluación de la actividad debe valorar coherencia entre pregunta, datos, modelo, validación y decisión. No basta con presentar fórmulas correctas: cada elección debe corresponder al momento real de uso, reconocer incertidumbre y distinguir predicción, asociación e intervención.
