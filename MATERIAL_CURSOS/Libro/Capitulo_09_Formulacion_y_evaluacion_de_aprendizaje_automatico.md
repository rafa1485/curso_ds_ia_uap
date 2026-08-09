# Capítulo 9. Formulación y evaluación de problemas de aprendizaje automático

Un sistema de aprendizaje automático no comienza con la elección de un algoritmo, sino con una pregunta precisa: **¿qué regularidad debe aprenderse, a partir de qué información y para apoyar qué decisión?** La formulación transforma una necesidad del mundo real en unidades observables, entradas, resultados esperados y criterios de éxito. La evaluación, a su vez, intenta responder con evidencia si el sistema funcionará sobre casos que todavía no ha visto. Ambas tareas son inseparables: una métrica impecablemente calculada no corrige una etiqueta que representa mal el objetivo, ni una arquitectura sofisticada compensa una partición contaminada.

Este capítulo presenta el vocabulario y el razonamiento experimental necesarios para formular y evaluar problemas de aprendizaje. Primero distingue paradigmas y tipos de tarea; después relaciona pérdida, ajuste y generalización; a continuación diseña particiones que respetan la estructura de los datos; finalmente estudia métricas de regresión y clasificación. El hilo conductor es que el desempeño no es una propiedad absoluta del modelo. Es una estimación condicionada por una población, un horizonte, una muestra, un protocolo, una métrica y una regla de decisión.

## 9.1. Paradigmas de aprendizaje

Un paradigma especifica de dónde procede la señal con la que aprende un modelo. No debe confundirse con una familia algorítmica: una red neuronal puede entrenarse de forma supervisada, autosupervisada o semisupervisada; un método basado en distancias puede servir para clasificación supervisada o para agrupamiento no supervisado. Tampoco todo problema de datos requiere aprendizaje automático. Si una regla estable, auditable y suficientemente precisa resuelve la tarea, esa regla puede ser preferible.

### 9.1.1. Aprendizaje supervisado

En aprendizaje supervisado se dispone de observaciones emparejadas

$$
\mathcal{D}=\{(\mathbf{x}_i,y_i)\}_{i=1}^{n},
$$

donde $\mathbf{x}_i$ reúne las variables de entrada y $y_i$ representa el objetivo conocido. El propósito es aprender una función $f:\mathcal{X}\rightarrow\mathcal{Y}$ que produzca una predicción $\hat y=f(\mathbf{x})$ útil para observaciones nuevas. Si $y$ es cuantitativa, suele formularse una regresión; si pertenece a un conjunto de categorías, una clasificación.

«Supervisado» no significa que una persona observa cada paso del entrenamiento. Significa que existe una señal objetivo contra la cual comparar la salida. Esa señal puede proceder de una medición física, un registro administrativo, una anotación experta o un resultado futuro. Su origen determina qué aprende realmente el sistema. Por ejemplo, predecir «hospitalización registrada» no equivale a predecir «gravedad clínica»: intervienen acceso, decisiones médicas y calidad del registro.

Una formulación completa debe declarar la unidad de análisis, el instante de predicción y el horizonte. «Predecir retrasos» es ambiguo; «al momento de la salida programada, predecir si un viaje llegará con más de 15 minutos de retraso» delimita población, información disponible y etiqueta. Las entradas deben existir en ese instante. Incorporar la hora real de llegada produciría una fuga: permitiría reconstruir aquello que se pretende anticipar.

El modelo supervisado aproxima regularidades de la distribución que generó los pares observados. No memoriza una ley universal. Si cambian la población, el proceso de medición o la definición de la etiqueta, puede deteriorarse aun cuando el algoritmo permanezca intacto. Por eso la validez fuera de muestra y el ámbito de aplicación forman parte de la especificación.

### 9.1.2. Aprendizaje no supervisado

El aprendizaje no supervisado parte de entradas sin una etiqueta objetivo explícita:

$$
\mathcal{D}=\{\mathbf{x}_i\}_{i=1}^{n}.
$$

Busca describir estructura: grupos de observaciones parecidas, dimensiones latentes, regiones densas, asociaciones o casos atípicos. El agrupamiento de estaciones por patrones de consumo y la reducción de miles de atributos a unas pocas componentes son ejemplos. «No supervisado» no significa «sin decisiones humanas». La elección de variables, escala, distancia, número de grupos y criterio de interpretación introduce supuestos fuertes.

En ausencia de una verdad objetivo única, evaluar exige especial cautela. Dos particiones distintas pueden ser matemáticamente coherentes y responder a usos diferentes. Un índice interno de cohesión no demuestra que los grupos sean útiles, estables o sustantivamente válidos. Conviene combinar criterios internos, estabilidad ante remuestreo y validación externa por especialistas o por una tarea posterior. Nombrar un grupo después de observar sus rasgos no convierte ese nombre en una clase verdadera.

El análisis no supervisado también puede preceder a una tarea supervisada, por ejemplo para explorar segmentos o construir representaciones. En ese caso, cualquier transformación que use la distribución completa de los datos debe ajustarse solo con la porción de entrenamiento si luego será evaluada predictivamente. La falta de etiquetas no elimina el riesgo de contaminación.

### 9.1.3. Aprendizaje semisupervisado

El aprendizaje semisupervisado combina un conjunto pequeño de observaciones etiquetadas con otro, normalmente mayor, sin etiquetas:

$$
\mathcal{D}_{L}=\{(\mathbf{x}_i,y_i)\}_{i=1}^{n_L}, \qquad
\mathcal{D}_{U}=\{\mathbf{x}_j\}_{j=1}^{n_U}, \quad n_U\gg n_L.
$$

Resulta atractivo cuando obtener entradas es barato pero etiquetarlas requiere especialistas, tiempo o pruebas costosas. Un sistema puede aprender primero la geometría de todas las imágenes y después aprovechar las pocas diagnósticamente anotadas. Otros enfoques asignan pseudoetiquetas a predicciones muy confiables o exigen consistencia ante perturbaciones de una misma entrada.

Su beneficio depende de supuestos. Uno frecuente afirma que observaciones cercanas comparten etiqueta; otro, que las fronteras de clase atraviesan zonas de baja densidad. Si los datos no etiquetados proceden de otra población, o si el modelo inicial se equivoca sistemáticamente en una clase minoritaria, las pseudoetiquetas amplifican errores. «Más datos» puede empeorar el resultado cuando su relación con el objetivo es inadecuada.

La evaluación continúa siendo supervisada: validación y prueba necesitan etiquetas fiables y no deben participar en la creación de pseudoetiquetas ni en la selección de confianza. Debe compararse contra un baseline entrenado únicamente con $\mathcal{D}_L$, manteniendo constantes particiones y presupuesto de etiquetado. Así se atribuye la mejora al uso de datos no etiquetados y no a una comparación desigual.

### 9.1.4. Aprendizaje autosupervisado

En aprendizaje autosupervisado la señal objetivo se deriva de la propia estructura de los datos. Se oculta una parte de una entrada y se predice desde el contexto, se aprende a distinguir vistas relacionadas de no relacionadas o se anticipa un fragmento siguiente. La entrada proporciona tanto el ejemplo como el objetivo pretextual, sin requerir una anotación humana para cada caso.

El objetivo pretextual no suele coincidir con la tarea final. Su función es aprender una representación $h(\mathbf{x})$ que capture regularidades reutilizables. Después puede ajustarse un predictor supervisado con pocas etiquetas para clasificación, regresión u otra tarea. En texto, predecir unidades ocultas puede producir representaciones sensibles al contexto; en imágenes, aproximar vistas transformadas puede capturar forma y contenido visual.

Autosupervisión y semisupervisión no son sinónimos. La primera describe cómo se genera la señal durante una etapa; la segunda, cómo se combinan datos etiquetados y no etiquetados para una tarea objetivo. Un proyecto puede preentrenar autosupervisadamente y luego realizar ajuste supervisado, incluso dentro de un esquema semisupervisado.

Los datos de preentrenamiento pueden contener sesgos, duplicados o ejemplos de prueba. Una representación entrenada con documentos futuros puede violar un experimento temporal, aunque nunca vea explícitamente sus etiquetas. Deben documentarse corpus, fechas y solapamientos. La evaluación final debe corresponder a la tarea y población de destino, no solo al objetivo pretextual.

### 9.1.5. Regresión, clasificación y agrupamiento

La **regresión** estima una cantidad sobre una escala numérica: demanda, temperatura, duración o concentración. La salida puede ser puntual, $\hat y$, o probabilística, como un intervalo o una distribución condicional. Que la etiqueta esté codificada con números no basta para hablar de regresión: códigos postales y categorías `1`, `2`, `3` siguen siendo cualitativos.

La **clasificación** asigna una o más categorías. Es binaria cuando hay dos clases, multiclase cuando cada caso pertenece a una entre más de dos y multietiqueta cuando varias pueden coexistir. Una salida probabilística $\hat p_k=P(Y=k\mid\mathbf{x})$ permite separar estimación de decisión: primero se estiman puntuaciones o probabilidades y luego una regla determina la acción. Esta distinción será esencial al estudiar umbrales y costos.

El **agrupamiento** construye grupos sin disponer de categorías objetivo. Puede ser particional, jerárquico o permitir pertenencias suaves. Su resultado depende de la representación y de la noción de similitud. No debe evaluarse como clasificación salvo que exista una referencia externa y se resuelva que los grupos intentan recuperarla.

Una necesidad real admite formulaciones alternativas. Para gestionar agua se puede regresar la concentración esperada, clasificar si excederá un límite o agrupar estaciones por perfiles. Cambian las etiquetas, las pérdidas y las decisiones. La elección debe partir de la acción: si el operador necesita asignar capacidad continua, una regresión puede conservar más información; si debe activar un protocolo reglado, una clasificación basada en el umbral puede ser directamente interpretable. Aun así, predecir la cantidad y aplicar después el umbral puede ser mejor si interesa variar ese límite.

### 9.1.6. Variables de entrada, objetivos y etiquetas

Una **variable de entrada**, atributo o característica es información disponible para producir la predicción. El vector $\mathbf{x}=(x_1,\ldots,x_p)$ puede mezclar mediciones numéricas, categorías, texto, imágenes y relaciones. La calidad de una entrada no depende solo de su correlación histórica con el objetivo: debe estar disponible, medirse de forma consistente, ser legítima y conservar significado en el uso previsto.

El **objetivo** es el concepto que interesa anticipar; la **etiqueta** es su representación observable en los datos. Esta diferencia evita confundir un sustituto con el fenómeno. El objetivo podría ser «necesidad de revisión inmediata», pero una etiqueta como «respuesta tardía» no la representa necesariamente. Además, si la respuesta se observa después del ingreso, no puede utilizarse como entrada para decidir al ingreso.

Las etiquetas pueden contener ruido aleatorio, discrepancias entre anotadores o sesgo sistemático. Cuando especialistas discrepan, la incertidumbre no desaparece por mayoría de votos. Conviene documentar instrucciones, acuerdo, procedencia y fecha. En algunos problemas el resultado está censurado o solo se observa para quienes recibieron una intervención; entonces el conjunto etiquetado no es una muestra neutral.

Una ficha de formulación debería responder:

| Elemento | Pregunta de control |
|---|---|
| Unidad | ¿Qué representa una fila o ejemplo? |
| Población | ¿Sobre qué casos se pretende usar el sistema? |
| Entrada | ¿Qué se conoce exactamente al predecir? |
| Objetivo y etiqueta | ¿Qué concepto interesa y cómo se observa? |
| Instante y horizonte | ¿Cuándo se predice y hasta cuándo mira el resultado? |
| Salida | ¿Cantidad, clase, probabilidad, grupo o acción? |
| Error | ¿Qué consecuencias tienen los distintos fallos? |
| Abstención | ¿Cuándo debe derivarse el caso a revisión? |

Un identificador casi nunca es una entrada legítima. Puede conservarse para trazabilidad y partición. Variables posteriores, agregados calculados con el futuro y codificaciones de la etiqueta son fugas. La pregunta decisiva no es «¿está la columna en el archivo?», sino «¿existiría con el mismo significado al momento de usar el modelo?».

### 9.1.7. Ejemplo práctico guiado: formulación de cuatro tareas de aprendizaje

Consideremos cuatro dominios que reaparecen en el libro. El propósito no es escoger algoritmos, sino traducir necesidades a tareas verificables.

| Dominio | Unidad e instante | Entrada posible | Salida | Formulación |
|---|---|---|---|---|
| Movilidad | viaje, antes de iniciarse | ruta, calendario, clima disponible, historial anterior | minutos de demora | regresión supervisada |
| Agua | medición de una estación | variables fisicoquímicas simultáneas y antecedentes | excede/no excede un límite | clasificación supervisada |
| Reclamos | reclamo CFPB al ingreso | narrativa inicial | `Product` | clasificación multiclase supervisada |
| Imágenes vegetales | imagen adquirida | píxeles y metadatos permitidos | representación reutilizable | preentrenamiento autosupervisado; posterior clasificación supervisada |

El caso de movilidad exige definir si se predice demora continua o incumplimiento de un umbral. La fecha real de llegada queda excluida. Para agua, si las estaciones producen series repetidas, la evaluación debe considerar dependencia temporal y por estación. En reclamos, una respuesta empresarial posterior no describe lo conocido al ingreso y sería fuga. En imágenes, aprender representaciones sin diagnóstico no demuestra utilidad clínica o agronómica: la tarea posterior requiere sus propias etiquetas y evaluación.

Podría añadirse una quinta formulación no supervisada: agrupar estaciones de agua por perfiles estacionales. No habría una «etiqueta correcta» por estación; se juzgarían estabilidad, separación, interpretación y utilidad para diseñar muestreos. El mismo dominio admite paradigmas diferentes porque paradigma y objeto de estudio no son equivalentes.

## 9.2. Ajuste, error y generalización

Entrenar consiste en utilizar datos para elegir una función dentro de un conjunto de candidatos. Evaluar consiste en estimar qué ocurrirá fuera de esos datos. La diferencia entre ambas operaciones parece sencilla, pero organiza casi todo el diseño experimental del aprendizaje automático.

### 9.2.1. Funciones de pérdida

Una función de pérdida $L(y,\hat y)$ cuantifica el desacuerdo entre el resultado observado y la predicción para un caso. Es una señal de ajuste, no necesariamente la métrica final del proyecto. Debe ser compatible con la salida del modelo, tratable durante la optimización y razonablemente alineada con el objetivo.

En regresión son habituales la pérdida absoluta y la cuadrática:

$$
L_{1}(y,\hat y)=|y-\hat y|, \qquad
L_{2}(y,\hat y)=(y-\hat y)^2.
$$

La segunda penaliza con rapidez los errores grandes y es sensible a valores extremos. La primera crece linealmente y resulta más robusta. Bajo ciertas condiciones, minimizar error cuadrático estima una media condicional y minimizar error absoluto, una mediana condicional. Por tanto, elegir pérdida también define qué aspecto de la distribución se intenta predecir.

En clasificación, la pérdida 0-1 vale 1 cuando la clase es incorrecta y 0 cuando es correcta, pero no distingue grados de confianza y es difícil de optimizar directamente. La entropía cruzada binaria para una probabilidad $p$ es

$$
L(y,p)=-[y\log(p)+(1-y)\log(1-p)].
$$

Asigna gran penalización a errores expresados con confianza extrema. En multiclase, $L=-\sum_k y_k\log(p_k)$ con una codificación indicadora. Una pérdida ponderada puede dar mayor peso a ciertas clases, pero los pesos deben responder a costos o al diseño, no elegirse solo para elevar una cifra.

La pérdida de entrenamiento, la métrica de selección y la utilidad operativa pueden diferir. Un clasificador puede entrenarse con entropía cruzada, seleccionarse por macro-F1 y desplegarse con una política de revisión basada en costos. Esas decisiones deben mantener una relación explícita; de lo contrario, se optimiza una cantidad que no representa el éxito.

### 9.2.2. Riesgo empírico

El **riesgo esperado** de una función $f$ bajo una distribución poblacional $P(X,Y)$ es

$$
R(f)=\mathbb{E}_{(X,Y)\sim P}\left[L(Y,f(X))\right].
$$

Como $P$ se desconoce, se aproxima mediante el **riesgo empírico** sobre la muestra de entrenamiento:

$$
\widehat R_{\text{ent}}(f)=\frac{1}{n}\sum_{i=1}^{n}L(y_i,f(\mathbf{x}_i)).
$$

El principio de minimización del riesgo empírico elige, dentro de una familia $\mathcal F$, una función con bajo riesgo observado. Con regularización se añade una penalización de complejidad:

$$
\hat f=\arg\min_{f\in\mathcal F}
\left[\widehat R_{\text{ent}}(f)+\lambda\Omega(f)\right].
$$

$\Omega(f)$ desalienta soluciones demasiado complejas según una definición concreta y $\lambda$ controla el compromiso. La penalización no garantiza generalización por sí sola: depende de que la muestra represente el uso futuro y de que la evaluación sea independiente.

El promedio empírico presupone una unidad de muestreo adecuada. Si una persona aporta cien registros casi idénticos y otra uno, promediar por filas da a la primera cien veces más influencia. Puede ser necesario ponderar por entidad, episodio o diseño muestral. Asimismo, minimizar una pérdida promedio puede ocultar desempeño deficiente en subpoblaciones pequeñas.

### 9.2.3. Error de entrenamiento y error de generalización

El error de entrenamiento se calcula sobre datos empleados para ajustar parámetros. Por construcción suele ser optimista. El error de generalización describe el desempeño esperado sobre nuevos casos de la población objetivo. No puede observarse exactamente; se estima mediante datos no usados en el ajuste.

La **brecha de generalización** puede expresarse como

$$
G=\widehat R_{\text{eval}}(f)-\widehat R_{\text{ent}}(f).
$$

Una brecha grande sugiere que el modelo explota peculiaridades del entrenamiento, aunque una brecha pequeña no garantiza buen desempeño: ambos errores pueden ser altos. Además, la estimación de evaluación tiene incertidumbre. Un resultado de 0,82 no es una constante del modelo, sino una estadística de una muestra particular.

«Datos nuevos» debe significar nuevos bajo el escenario declarado. Si el sistema operará el próximo año, una muestra aleatoria de registros del mismo periodo puede ser menos informativa que un corte temporal. Si generalizará a pacientes nuevos, colocar visitas de una misma persona en entrenamiento y prueba sobreestima la capacidad. Generalización siempre requiere completar la frase: a nuevos registros, entidades, lugares, periodos o condiciones.

### 9.2.4. Sobreajuste y subajuste

Hay **subajuste** cuando el modelo no captura estructura relevante: el error de entrenamiento es alto y el de validación también. Puede deberse a una familia demasiado rígida, entradas poco informativas, exceso de regularización o entrenamiento insuficiente. Añadir datos sin cambiar esas limitaciones no siempre ayuda.

Hay **sobreajuste** cuando el modelo se adapta a fluctuaciones, ruido o particularidades del entrenamiento que no se repiten. El error de entrenamiento sigue disminuyendo mientras el de validación se estanca o empeora. Más capacidad, demasiadas decisiones de hiperparámetros y fugas sutiles aumentan este riesgo. También se sobreajusta la validación: después de cientos de comparaciones, el mejor resultado puede reflejar azar específico de ese conjunto.

Los diagnósticos no deben basarse en una sola cifra. Conviene comparar curvas de entrenamiento y validación, variación entre particiones, desempeño por periodo y errores concretos. Las respuestas posibles incluyen simplificar o regularizar, mejorar atributos, ampliar datos representativos, detener antes el ajuste o reducir la búsqueda. Si la causa es cambio de distribución, regularizar no sustituye una evaluación temporal adecuada.

Un error común consiste en llamar sobreajuste a cualquier desempeño bajo en prueba. También podría existir subajuste, una etiqueta defectuosa, una partición más difícil o deriva real. El diagnóstico compara patrones y formula hipótesis comprobables.

### 9.2.5. Compromiso entre sesgo y varianza

Para regresión con pérdida cuadrática, y bajo una descomposición idealizada, el error esperado en un punto puede escribirse como

$$
\mathbb{E}\left[(Y-\hat f(\mathbf{x}))^2\right]
=\operatorname{Sesgo}[\hat f(\mathbf{x})]^2
+\operatorname{Var}[\hat f(\mathbf{x})]
+\sigma^2.
$$

El **sesgo** mide la diferencia sistemática entre la predicción promedio del procedimiento y la función verdadera. La **varianza** mide cuánto cambiaría la predicción si se entrenara con otras muestras de la misma población. $\sigma^2$ representa ruido irreducible bajo los supuestos de la descomposición.

Modelos muy rígidos suelen tener sesgo alto y varianza baja; modelos muy flexibles pueden reducir sesgo pero aumentar varianza. No es una ley que obligue a escoger un punto medio fijo: más datos relevantes, mejor regularización o una representación adecuada pueden mejorar ambos componentes. Tampoco el «sesgo» de esta descomposición equivale al sesgo social o de muestreo, aunque pueden coexistir.

La varianza se manifiesta como inestabilidad entre particiones o semillas. Si pequeñas modificaciones de entrenamiento cambian mucho el resultado, una única división ofrece evidencia débil. El sesgo se sospecha cuando incluso el ajuste sobre entrenamiento es insuficiente. Las curvas de aprendizaje ayudan a distinguirlos, pero siempre dentro del dominio observado.

### 9.2.6. Complejidad del modelo

La complejidad es la capacidad efectiva para representar patrones. No se reduce al número de parámetros: también depende de restricciones, regularización, profundidad, representación de entradas y cantidad de datos. Un modelo con muchos parámetros preentrenados puede comportarse de manera estable al ajustarse poco; uno pequeño con atributos identificadores puede memorizar.

Al aumentar complejidad, el error de entrenamiento normalmente no sube, pero el de validación suele describir una curva con una región óptima. Elegir complejidad es una decisión empírica realizada en validación, no en prueba. Entre alternativas con desempeño indistinguible dentro de la incertidumbre, el modelo más simple puede ofrecer menor costo, mejor auditabilidad y mayor estabilidad.

La complejidad del **proceso de búsqueda** también cuenta. Probar numerosas transformaciones, subconjuntos y semillas equivale a ampliar la familia de hipótesis. Aunque cada modelo individual sea sencillo, escoger el máximo entre muchos resultados puede sobreajustar la validación. Registrar todos los intentos y limitar decisiones posteriores protege la honestidad experimental.

### 9.2.7. Modelos de referencia o baselines

Un baseline es una referencia sencilla y relevante que establece el nivel mínimo a superar. En regresión puede predecir la media o mediana de entrenamiento; en clasificación, la clase mayoritaria, frecuencias de clase o una regla operativa existente. En series temporales, repetir el último valor o el del mismo periodo anterior suele ser más exigente que una media global.

Debe ajustarse con la misma información permitida y evaluarse en exactamente los mismos casos y métricas. Comparar un modelo complejo en una partición favorable contra un baseline publicado en otra muestra no prueba mejora. Tampoco basta vencer a la clase mayoritaria si existe una regla manual barata y mejor.

Los baselines cumplen tres funciones. Detectan errores de pipeline cuando una solución sofisticada no supera una regla trivial; cuantifican valor incremental; y aportan una alternativa desplegable de bajo costo. Para clases desbalanceadas, la clase mayoritaria puede lograr alta exactitud y macro-F1 muy baja, demostrando por qué una sola métrica engaña. Un baseline aleatorio estratificado puede servir como control adicional, pero debe fijarse su semilla o evaluarse su distribución.

### 9.2.8. Ejemplo práctico guiado: curvas de aprendizaje

Una curva de aprendizaje representa desempeño de entrenamiento y validación frente al tamaño de la muestra. Para evitar comparaciones confusas, se usan subconjuntos anidados y el mismo protocolo de validación.

```text
ENTRADA: conjunto de desarrollo, tamaños crecientes m[1..J], procedimiento A
PARA cada tamaño m[j]:
    PARA cada repetición o partición válida:
        seleccionar m[j] ejemplos solo de la porción de entrenamiento
        ajustar todas las transformaciones y A con esos ejemplos
        medir pérdida en esos ejemplos y en la validación independiente
    resumir media y dispersión de ambas pérdidas
TRAZAR tamaño frente a pérdida de entrenamiento y validación
```

Supongamos los siguientes errores de clasificación, donde menor es mejor:

| Ejemplos | Entrenamiento | Validación |
|---:|---:|---:|
| 500 | 0,04 | 0,24 |
| 2 000 | 0,07 | 0,17 |
| 8 000 | 0,09 | 0,13 |
| 20 000 | 0,10 | 0,12 |

La brecha disminuye y validación continúa mejorando: más datos representativos probablemente ayuden, aunque con retornos decrecientes. Si ambas curvas se estabilizaran en 0,25, habría indicios de subajuste o entradas insuficientes. Si entrenamiento permaneciera cerca de cero y validación en 0,20, dominaría una brecha compatible con alta varianza, contaminación de categorías raras o cambio entre particiones.

Una curva no identifica automáticamente la causa. Debe acompañarse con intervalos o dispersión, baseline y análisis por clase. Si al aumentar $m$ también se incorporan periodos más recientes, se mezclan tamaño y tiempo; en datos temporales, los subconjuntos deben respetar el orden y la pregunta de generalización.

## 9.3. Diseño de la evaluación

El diseño de evaluación es un experimento. Su objeto no es producir el número más alto, sino una estimación relevante y reproducible con la menor contaminación posible. Debe escribirse antes de consultar repetidamente los resultados, igual que un protocolo experimental.

### 9.3.1. Conjuntos de entrenamiento, validación y prueba

El conjunto de **entrenamiento** ajusta parámetros y transformaciones aprendidas: coeficientes, vocabulario, imputación, escalado o selección de atributos. El conjunto de **validación** elige familias, hiperparámetros, umbrales y otras decisiones. El conjunto de **prueba** se reserva para estimar una sola vez el desempeño del procedimiento ya fijado.

Esta separación es funcional, no meramente física. Si se observa prueba y se cambia el modelo, prueba ha pasado a desempeñar el papel de validación. Si se normaliza con la media de todo el archivo antes de dividir, la prueba ya influyó en el entrenamiento. Toda operación que aprende de los datos debe ajustarse dentro de entrenamiento y aplicarse después a validación o prueba.

Un flujo correcto puede expresarse así:

```text
definir unidad, población, horizonte, grupos y métrica
reservar PRUEBA sin inspeccionar resultados predictivos
usar ENTRENAMIENTO y VALIDACIÓN para:
    ajustar transformaciones únicamente en ENTRENAMIENTO
    entrenar candidatos
    elegir hiperparámetros y regla de decisión con VALIDACIÓN
fijar procedimiento completo
reajustar, si estaba previsto, usando datos de desarrollo permitidos
evaluar una vez en PRUEBA y reportar incertidumbre y limitaciones
```

Las proporciones 60/20/20 u 80/10/10 no son universales. Dependen del tamaño, la estructura y la precisión deseada. Prueba debe contener suficientes ejemplos, especialmente de clases poco frecuentes, para estimar métricas con incertidumbre tolerable. En muestras pequeñas puede usarse validación cruzada en el conjunto de desarrollo y conservar una prueba externa.

### 9.3.2. Muestreo aleatorio y estratificado

Una división aleatoria asigna unidades a subconjuntos mediante azar controlado. Es apropiada cuando las observaciones son aproximadamente intercambiables y el futuro uso se parece a otra muestra de la misma distribución. La aleatorización reduce decisiones arbitrarias, pero no rompe dependencias existentes.

La división **estratificada** conserva aproximadamente la proporción de una variable, normalmente la clase, en cada subconjunto. Resulta útil con clases desbalanceadas para evitar que validación carezca por azar de ejemplos minoritarios. También puede estratificarse por combinaciones relevantes, siempre que haya soporte suficiente. Una estratificación excesivamente fina genera estratos diminutos e inestables.

Ejemplo: con 1 000 incidentes, 900 negativos y 100 positivos, una prueba aleatoria de 100 podría contener por azar pocos positivos. La estratificación 90/10 garantiza alrededor de 10, pero diez casos siguen dando una estimación muy incierta de sensibilidad. Estratificar no crea información; puede ser necesario ampliar prueba o agregar periodos.

Primero debe identificarse la unidad independiente. Dividir filas aleatoriamente es incorrecto si hay mediciones repetidas, duplicados, imágenes del mismo objeto o fragmentos de un mismo documento. En esos casos se asigna el grupo completo, y la estratificación pasa a ser secundaria o aproximada.

### 9.3.3. Validación cruzada

En validación cruzada de $K$ particiones, el conjunto de desarrollo se divide en $K$ bloques. Cada bloque actúa una vez como validación y los restantes como entrenamiento. Para una métrica $M$:

$$
\overline M_{CV}=\frac{1}{K}\sum_{k=1}^{K}M_k.
$$

La dispersión entre $M_k$ informa sensibilidad a la partición, aunque la desviación estándar de los folds no es automáticamente un intervalo de confianza: los entrenamientos se solapan y las estimaciones no son independientes.

Todas las transformaciones deben repetirse dentro de cada fold. Ajustar imputación, escalado, vocabulario o selección de variables antes de la validación cruzada filtra información. El objeto que se valida es el pipeline completo.

```text
crear folds respetando unidad, estratos, grupos o tiempo
PARA cada fold k:
    DESARROLLO_k = todos los folds excepto k
    VALIDACIÓN_k = fold k
    ajustar preprocesamiento con DESARROLLO_k
    transformar DESARROLLO_k y VALIDACIÓN_k
    entrenar con DESARROLLO_k
    calcular métricas en VALIDACIÓN_k
agregar métricas y conservar resultados por fold
```

$K=5$ o $10$ es frecuente, no obligatorio. Más folds aprovechan más datos para cada ajuste pero elevan costo y correlación entre estimaciones. La validación cruzada repetida permite estudiar variación aleatoria. La **validación cruzada anidada** utiliza un ciclo interno para hiperparámetros y uno externo para estimación, reduciendo optimismo cuando no existe prueba abundante. No debe usarse el promedio externo para volver a elegir configuraciones sin reconocer que se reutilizó como validación.

### 9.3.4. Validación para datos agrupados

Los datos están agrupados cuando varias observaciones comparten una fuente que induce dependencia: persona, hogar, vehículo, estación, empresa, dispositivo, sitio o plantilla. Si registros del mismo grupo aparecen a ambos lados, el modelo puede reconocer al grupo en lugar de aprender una regularidad transferible.

La partición por grupos asigna cada identificador a un único subconjunto. En validación cruzada, cada fold contiene grupos completos. La pregunta estimada es entonces generalización a grupos no vistos. Si el uso real acepta nuevas observaciones de grupos ya conocidos, puede diseñarse otra evaluación, pero debe declararse y quizá incluir ambas: dentro de grupo y fuera de grupo.

Los duplicados exactos y casi duplicados forman grupos de partición aunque no sean entidades naturales. Eliminarlos antes de dividir puede ser válido, pero debe documentarse. Si se conservan para representar frecuencia real, todas sus copias han de permanecer juntas. La detección debe realizarse sin usar la etiqueta como atajo y, cuando corresponda, considerar plantillas con pequeñas variaciones.

Agrupar puede alterar la proporción de clases y producir folds desiguales. No se debe romper grupos para obtener estratificación perfecta. Se buscan asignaciones aproximadas, se reporta soporte por fold y se reconoce la incertidumbre. Un único grupo dominante puede impedir estimar generalización independiente; es una limitación del dato, no un problema que resuelva una semilla distinta.

### 9.3.5. Validación temporal

Cuando el sistema se entrenará con pasado para operar en futuro, la evaluación debe respetar el tiempo. Un corte simple utiliza fechas tempranas para entrenamiento, un periodo posterior para validación y el más reciente para prueba. Así evita que patrones futuros informen decisiones del pasado y permite observar deriva.

En origen rodante se realizan varios experimentos:

```text
ordenar unidades por instante disponible
PARA cada fecha de corte t[k]:
    ENTRENAMIENTO = unidades disponibles hasta t[k]
    VALIDACIÓN = unidades del horizonte posterior definido
    eliminar o agrupar unidades que cruzan la frontera según el protocolo
    ajustar todo con ENTRENAMIENTO y evaluar en VALIDACIÓN
resumir por ventana y periodo; no mezclar el futuro en ajustes anteriores
```

Debe distinguirse tiempo de entrada, tiempo del resultado y tiempo de disponibilidad. Si una etiqueta tarda 30 días en confirmarse, al corte solo pueden entrenarse casos cuyo resultado ya maduró. Puede requerirse una **brecha** entre entrenamiento y validación para evitar ventanas objetivo solapadas. En pronósticos, el horizonte de evaluación debe coincidir con el operativo.

La estratificación aleatoria no debe imponerse sobre el orden temporal. Que una clase desaparezca en un periodo es información relevante sobre cambio de población. Se reporta soporte y, si el problema deja de ser factible, se revisa la formulación. Tampoco debe escogerse el corte después de mirar cuál produce el mejor resultado.

### 9.3.6. Selección de modelos e hiperparámetros

Los parámetros se aprenden durante el ajuste; los **hiperparámetros** controlan el procedimiento: fuerza de regularización, profundidad, número de componentes o decisiones de representación. Se seleccionan usando validación o el ciclo interno de validación cruzada.

Antes de buscar se define un espacio plausible, una métrica principal y una regla de desempate. La búsqueda exhaustiva, aleatoria o adaptativa no cambia el principio: cada consulta a validación consume información y aumenta el riesgo de sobreajuste. Deben registrarse configuraciones fallidas, no solo la ganadora.

Si varias configuraciones están cerca, conviene considerar dispersión, costo, latencia, estabilidad por grupo y simplicidad. La regla de «un error estándar», por ejemplo, puede elegir el candidato más simple cuyo desempeño sea compatible con el mejor. No debe proclamarse superioridad a partir de una diferencia minúscula sin cuantificar incertidumbre.

Tras seleccionar, puede reajustarse el procedimiento en entrenamiento más validación antes de prueba, siempre que estuviera previsto y que los hiperparámetros queden congelados. El preprocesamiento también se vuelve a ajustar sobre ese conjunto ampliado. El resultado de prueba evalúa todo el procedimiento fijado, no autoriza otra ronda de selección.

### 9.3.7. Reproducibilidad y comparación justa

Reproducibilidad significa que otra ejecución, con los mismos datos y decisiones, puede reconstruir el resultado y comprender sus límites. Una semilla es necesaria en procesos aleatorios, pero no suficiente. Deben registrarse versión y procedencia de datos, reglas de inclusión, identificadores de partición, entorno, configuración, orden de transformaciones y definición exacta de métricas.

Una comparación justa mantiene constantes:

- las unidades y particiones;
- la información disponible y el tratamiento de faltantes;
- el presupuesto de búsqueda o, al menos, su transparencia;
- la métrica y regla de selección;
- el conjunto de casos usado para el resultado final.

Reportar únicamente la mejor semilla es selección encubierta. Debe fijarse una semilla o resumir varias ejecuciones predefinidas. La determinación completa puede ser costosa o imposible en ciertos entornos; en ese caso se documentan fuentes de variación.

También importa la trazabilidad conceptual. Cada experimento necesita una hipótesis: «los bigramas mejorarán macro-F1 porque distinguen expresiones compuestas», no «probar opción B». Una tabla de experimentos debe incluir identificador, cambio único, datos, semilla, métrica de validación, costo y observaciones. Comparar versiones que cambian simultáneamente partición, limpieza y modelo impide atribuir diferencias.

### 9.3.8. Ejemplo práctico guiado: protocolo de evaluación sin contaminación

Supongamos 60 000 registros de incidentes, con 8 % positivos, observaciones repetidas por dispositivo y fechas de dos años. El sistema se desplegará en dispositivos nuevos durante el trimestre siguiente. Una división aleatoria estratificada por filas preservaría el 8 %, pero compartiría dispositivos y mezclaría futuro con pasado: contestaría una pregunta demasiado fácil.

El protocolo apropiado prioriza restricciones:

1. reservar el último trimestre como prueba temporal;
2. asignar cada dispositivo a un único conjunto para medir transferencia a dispositivos no vistos;
3. formar entrenamiento con periodos anteriores y validación con el trimestre inmediatamente anterior a prueba;
4. mantener duplicados y episodios vinculados en el mismo conjunto;
5. ajustar imputación, escalas y cualquier selección solo en entrenamiento;
6. escoger hiperparámetros y umbral en validación mediante una métrica definida;
7. congelar el pipeline y evaluar prueba una vez.

La combinación temporal y grupal puede reducir mucho la muestra y desequilibrar clases. Esa dificultad refleja el uso real. Si ningún dispositivo puede repetirse entre periodos pero muchos existen durante todo el intervalo, se define una cohorte de dispositivos futuros o se evalúan dos escenarios separados. No se debe improvisar una regla que coloque copias del mismo episodio en ambos lados.

Como auditoría de contaminación se comprueba: intersección nula de identificadores y grupos; rangos temporales; ausencia de variables posteriores; ajuste local de transformaciones; distribución de etiquetas y faltantes; y huellas de duplicados. Se conserva una tabla con la asignación de cada unidad. Esta evidencia es tan importante como la métrica resultante.

## 9.4. Métricas de desempeño

Una métrica reduce muchos resultados a una cantidad interpretable. Esa compresión siempre descarta información. Por ello se define una métrica principal coherente con la decisión, se acompaña con métricas auxiliares y se examinan distribuciones, grupos y errores concretos. Elegir después la cifra más favorable invalida la comparación.

### 9.4.1. MAE, MSE y RMSE

Para residuos $e_i=y_i-\hat y_i$, el error absoluto medio es

$$
\operatorname{MAE}=\frac{1}{n}\sum_{i=1}^{n}|e_i|.
$$

Se expresa en las unidades del objetivo y representa la magnitud absoluta promedio. Todos los errores aumentan su contribución linealmente. Es legible: un MAE de 2,4 minutos significa una desviación absoluta media de 2,4 minutos, aunque no describe dirección ni cuantiles.

El error cuadrático medio y su raíz son

$$
\operatorname{MSE}=\frac{1}{n}\sum_{i=1}^{n}e_i^2,
\qquad
\operatorname{RMSE}=\sqrt{\operatorname{MSE}}.
$$

MSE usa unidades al cuadrado; RMSE vuelve a la unidad original. Como los residuos se elevan al cuadrado, unos pocos errores grandes pesan mucho. Esto es apropiado si esos fallos tienen costo creciente; es problemático si son errores de medición o si se interpreta RMSE como un «error típico» sin revisar la distribución.

Ejemplo: para valores reales $(10,12,20,30)$ y predicciones $(12,11,17,38)$, los residuos son $(-2,1,3,-8)$. Entonces

$$
\operatorname{MAE}=\frac{2+1+3+8}{4}=3{,}5,
$$

$$
\operatorname{MSE}=\frac{4+1+9+64}{4}=19{,}5,
\qquad \operatorname{RMSE}\approx4{,}42.
$$

La diferencia entre MAE y RMSE señala la influencia del error de 8 unidades. Deben compararse contra una referencia y acompañarse con residuos por rango, tiempo y grupo. Ninguna distingue sobrepredicción de subpredicción; para ello se informa error medio firmado u otros resúmenes.

### 9.4.2. Coeficiente de determinación

El coeficiente de determinación habitual es

$$
R^2=1-\frac{\sum_i(y_i-\hat y_i)^2}{\sum_i(y_i-\bar y)^2}.
$$

Compara el error cuadrático del modelo con el de predecir la media de los valores evaluados. $R^2=1$ indica predicción perfecta; $R^2=0$ iguala esa referencia; un valor negativo significa que el modelo es peor que predecir la media en esa muestra. En prueba, valores negativos son perfectamente posibles.

No significa «porcentaje de predicciones correctas» ni demuestra causalidad. Puede ser alto cuando los errores son operacionalmente intolerables o bajo en un rango restringido aunque MAE sea pequeño. Tampoco permite comparar directamente tareas con poblaciones y variabilidad distintas.

Si se calcula $R^2$ por grupos pequeños, la varianza del denominador puede ser mínima o nula, volviendo la medida inestable o indefinida. En series temporales, una tendencia común puede inflar el valor aun si los cambios relevantes se predicen mal. Debe informarse junto con MAE o RMSE y con un baseline apropiado al dominio, no como única evidencia.

### 9.4.3. Matriz de confusión

Para clasificación binaria y una clase declarada positiva, la matriz cruza verdad y decisión:

|  | Predicción positiva | Predicción negativa |
|---|---:|---:|
| Real positiva | verdaderos positivos (TP) | falsos negativos (FN) |
| Real negativa | falsos positivos (FP) | verdaderos negativos (TN) |

Las denominaciones dependen de cuál clase se define positiva. Un falso positivo no es intrínsecamente peor ni mejor que un falso negativo: su costo depende de la acción. La matriz contiene conteos a un umbral concreto; cambiar el umbral cambia sus celdas.

Supongamos 200 incidentes: 40 positivos y 160 negativos. El sistema identifica 30 positivos, omite 10 y genera 20 alarmas falsas. Entonces $TP=30$, $FN=10$, $FP=20$ y $TN=140$. Estos números permiten calcular métricas, pero también estimar carga: habrá 50 alarmas para revisar, de las cuales 20 no corresponden a incidentes positivos.

En multiclase, la celda $(j,k)$ cuenta casos de clase real $j$ predichos como $k$. La diagonal representa aciertos. Conviene mostrar conteos y versiones normalizadas por fila; esta última revela qué proporción de cada clase se confunde, pero oculta soporte. Ordenar o agrupar categorías puede facilitar lectura, siempre sin modificar retrospectivamente la tarea.

### 9.4.4. Exactitud, precisión y sensibilidad

La **exactitud** o accuracy es

$$
\operatorname{Accuracy}=\frac{TP+TN}{TP+TN+FP+FN}.
$$

En el ejemplo, $(30+140)/200=0{,}85$. Resume la fracción de decisiones correctas. Es útil cuando clases y costos son aproximadamente equilibrados, pero puede engañar: predecir siempre negativo obtendría 0,80 sin detectar ningún positivo.

La **precisión** o valor predictivo positivo es

$$
\operatorname{Precision}=\frac{TP}{TP+FP}.
$$

Responde: de los casos declarados positivos, ¿qué fracción lo era? Aquí $30/50=0{,}60$. Interesa cuando una alarma activa una acción costosa. Depende de la prevalencia: aun con sensibilidad y especificidad constantes, cambia al cambiar la proporción de positivos.

La **sensibilidad**, exhaustividad o recall positivo es

$$
\operatorname{Recall}=\frac{TP}{TP+FN}.
$$

Responde: de los positivos reales, ¿qué fracción se detectó? Aquí $30/40=0{,}75$. Importa cuando omitir positivos es costoso. Si no se emite ninguna predicción positiva, precisión tiene denominador cero; la convención usada debe declararse, no esconderse asignando un valor conveniente.

En multiclase se calcula cada clase «contra el resto». El promedio **macro** da igual peso a cada clase; el **ponderado** usa su soporte; el **micro** agrega conteos antes de calcular. En clasificación multiclase de una sola etiqueta, micro-F1 coincide con accuracy. Reportar «F1 promedio» sin método de agregación es incompleto.

### 9.4.5. Especificidad y puntuación F1

La **especificidad** o tasa de verdaderos negativos es

$$
\operatorname{Specificity}=\frac{TN}{TN+FP}.
$$

En el ejemplo vale $140/160=0{,}875$. Mide qué fracción de negativos se descarta correctamente. Su complemento, $FPR=1-\text{especificidad}=FP/(FP+TN)$, es la tasa de falsos positivos.

La puntuación F1 es la media armónica de precisión y sensibilidad:

$$
F1=2\frac{\operatorname{Precision}\operatorname{Recall}}
{\operatorname{Precision}+\operatorname{Recall}}
=\frac{2TP}{2TP+FP+FN}.
$$

Para el ejemplo, $F1=60/(60+20+10)=0{,}667$. La media armónica cae cuando una de sus componentes es baja. F1 ignora verdaderos negativos; puede ser apropiada para recuperación de una clase positiva, pero no resume todos los costos. Dos modelos con la misma F1 pueden tener precisión y sensibilidad muy distintas.

En multiclase, **macro-F1** es

$$
\operatorname{MacroF1}=\frac{1}{K}\sum_{k=1}^{K}F1_k.
$$

Da visibilidad a clases poco frecuentes. También puede volverse inestable si algunas tienen muy pocos ejemplos; por eso se informa soporte y F1 por clase. No debe eliminarse una clase difícil después de ver prueba. Si se agrupan categorías por factibilidad, la regla debe fijarse antes y responder a sentido sustantivo.

### 9.4.6. Curvas ROC y área ROC-AUC

Un clasificador que produce puntuaciones puede evaluarse a múltiples umbrales. La curva ROC representa sensibilidad o tasa de verdaderos positivos frente a tasa de falsos positivos:

$$
TPR=\frac{TP}{TP+FN}, \qquad FPR=\frac{FP}{FP+TN}.
$$

Al bajar el umbral aumentan normalmente ambas. ROC-AUC es el área bajo la curva y puede interpretarse, bajo condiciones habituales y sin empates, como la probabilidad de que un positivo elegido al azar reciba mayor puntuación que un negativo. Un valor 0,5 corresponde a ordenamiento aleatorio y 1 a separación perfecta.

ROC-AUC evalúa ordenamiento a través de todos los umbrales, incluidos algunos que nunca se usarían. No elige un umbral, no garantiza probabilidades calibradas y no incorpora por sí sola costos. Con negativos muy abundantes, una tasa de falsos positivos aparentemente baja puede generar muchos FP absolutos. Deben inspeccionarse las regiones operativas y sus conteos.

En multiclase se usan esquemas uno-contra-resto y promedios macro o ponderados, que deben declararse. Comparar AUC exige los mismos casos. Si las curvas se cruzan, el modelo preferible depende de la región de operación; un único área puede ocultarlo.

### 9.4.7. Curvas precisión-recall y PR-AUC

La curva precisión-recall (PR) representa precisión frente a sensibilidad a medida que varía el umbral. Se centra en la recuperación de positivos y resulta informativa cuando estos son raros. Su referencia depende de prevalencia: un clasificador sin habilidad tiene precisión esperada cercana a la proporción positiva, no una línea universal de 0,5.

PR-AUC resume la curva, pero existen convenciones de integración distintas, como área trapezoidal y precisión promedio. El reporte debe indicar la utilizada. Al igual que ROC-AUC, no expresa desempeño en un umbral específico ni calidad de calibración.

Supongamos 1 000 casos con 20 positivos. Un punto con sensibilidad 0,80 y FPR 0,05 produce aproximadamente 16 TP y 49 FP: su precisión es solo $16/(16+49)\approx0{,}246$. ROC puede mostrar un FPR pequeño, mientras PR hace visible que tres de cada cuatro alarmas serían falsas. Este contraste no vuelve «mejor» a PR en todo contexto; responde a una lectura distinta.

Las curvas de modelos deben calcularse sobre la misma prueba y acompañarse con bandas de incertidumbre cuando sea posible. Si interesa una clase minoritaria en multiclase, se examina su curva uno-contra-resto y también las confusiones específicas; el promedio puede esconder el problema.

### 9.4.8. Umbrales, costos y datos desbalanceados

Una puntuación no es todavía una decisión. En clasificación binaria se decide positivo si $p\ge t$. El umbral $t=0{,}5$ no es una ley: solo tiene una justificación particular si las probabilidades están calibradas, la función de costos y las alternativas conducen a ese punto.

Con costos $C_{FP}$ y $C_{FN}$, el costo observado de un umbral puede estimarse como

$$
\widehat C(t)=C_{FP}\,FP(t)+C_{FN}\,FN(t),
$$

posiblemente añadiendo costos de verdaderos positivos, revisión o demora. Los costos pueden ser monetarios, de capacidad, seguridad o equidad; no siempre se reducen de manera responsable a dinero. Deben discutirse con responsables del proceso y analizarse en escenarios.

Si las probabilidades son calibradas y los únicos costos relevantes son un FP y un FN, una regla idealizada predice positivo cuando

$$
p>\frac{C_{FP}}{C_{FP}+C_{FN}}.
$$

Por ejemplo, si omitir cuesta nueve veces una falsa alarma, el umbral teórico es $1/(1+9)=0{,}10$. En la práctica se verifica en validación porque costos, calibración y restricciones son imperfectos. Nunca se escoge el umbral final en prueba.

El desbalance no se «soluciona» automáticamente equilibrando datos. Submuestreo, sobremuestreo y ponderación cambian el ajuste y pueden afectar calibración. Deben aplicarse solo dentro de cada entrenamiento, nunca antes de dividir. Para evaluación se conserva, por regla general, la prevalencia del escenario de uso. Se reportan matriz de confusión, soporte, métricas por clase y carga operativa.

En multiclase puede incorporarse una opción de **abstención**: si la mayor probabilidad es baja o el margen entre las dos primeras clases es pequeño, el sistema deriva a revisión. La cobertura es la fracción decidida automáticamente; el riesgo selectivo mide error entre esas decisiones. Una política útil especifica el compromiso entre cobertura, errores y capacidad humana. Ajustar umbrales por clase puede responder a costos diferentes, pero complica interpretación y requiere suficiente validación.

Errores comunes incluyen optimizar accuracy con una clase dominante, informar solo AUC, usar pesos como sustituto de una métrica apropiada, alterar el umbral por cada lote sin gobernanza y asumir que una puntuación de 0,9 es una probabilidad de 90 %. La calibración se evalúa separadamente mediante curvas o puntuaciones propias y con datos no empleados para ajustar el modelo base.

### 9.4.9. Ejemplo práctico guiado: evaluación de un clasificador de incidentes

Retomemos 200 incidentes con 40 positivos. Dos umbrales producen:

| Umbral | TP | FN | FP | TN | Precisión | Sensibilidad | Especificidad | F1 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0,30 | 36 | 4 | 48 | 112 | 0,429 | 0,900 | 0,700 | 0,581 |
| 0,65 | 28 | 12 | 8 | 152 | 0,778 | 0,700 | 0,950 | 0,737 |

El umbral 0,65 tiene mejor F1 y precisión; 0,30 recupera más incidentes. Si un FN cuesta 10 unidades y un FP 1, los costos son:

$$
C(0{,}30)=10(4)+1(48)=88,
$$

$$
C(0{,}65)=10(12)+1(8)=128.
$$

La decisión por costo preferiría 0,30 pese a su F1 menor. Sin embargo, genera 84 alarmas y quizá el equipo solo pueda revisar 50. Esa restricción convierte capacidad en parte del problema. Podría elegirse el umbral más bajo que no exceda 50 revisiones y luego estimar cuántos FN implica.

Un procedimiento guiado sería:

```text
ENTRADA: puntuaciones y etiquetas de VALIDACIÓN, costos y capacidad
definir una grilla de umbrales antes de consultar PRUEBA
PARA cada umbral:
    construir matriz de confusión
    calcular precisión, sensibilidad, especificidad, F1 y número de alarmas
    calcular costo bajo cada escenario acordado
descartar umbrales que violen capacidad o sensibilidad mínima
elegir mediante la regla predefinida; congelar el umbral
aplicar una sola vez a PRUEBA y reportar todas las métricas y conteos
```

El ejemplo muestra por qué «mejor clasificador» es una frase incompleta. Puede significar mejor ordenamiento, mejor probabilidad, mayor F1 o menor costo bajo una capacidad dada. El protocolo debe indicar cuál antes de seleccionar.

### Actividad EMO [REC-02]: diseñar la evaluación de un clasificador de reclamos

**Contexto y propósito.** La actividad se integra con el proyecto de reclamos del Apéndice D. La fuente es la base pública de quejas de la Consumer Financial Protection Bureau (CFPB). La unidad es un reclamo publicado, identificado por `Complaint ID`, con `Consumer complaint narrative` no vacía. La tarea obligatoria recomendada es predecir la categoría `Product` a partir de la narrativa inicial para sugerir enrutamiento temático. No se pretende determinar daño, urgencia, legitimidad ni una respuesta financiera.

**Capacidad mínima:** definir y justificar un protocolo de evaluación antes de entrenar el modelo de texto. El protocolo debe permitir una comparación común en REC-03 y REC-04 y demostrar ausencia de fuga evidente.

**Formulación fija.** La entrada obligatoria es `Consumer complaint narrative`; la etiqueta es `Product`. `Complaint ID` se conserva solo para trazabilidad. `Date received` define el corte temporal. La población evaluable queda condicionada a narrativas publicadas con consentimiento, por lo que no representa automáticamente todos los reclamos recibidos por CFPB.

Quedan excluidos como entradas `Product`, `Sub-product`, `Issue`, `Sub-issue` y cualquier derivado de la etiqueta. También se excluyen `Company public response`, `Date sent to company`, `Company response to consumer` y `Timely response?`: se producen después del ingreso o de la respuesta y generarían **fuga posterior a la respuesta**. `Company` no se usa en el baseline obligatorio porque puede actuar como atajo hacia su cartera de productos; `ZIP code` y `Tags` se excluyen por privacidad, granularidad o proxies sensibles. No basta eliminar columnas: debe comprobarse que esos campos no hayan sido concatenados a la narrativa analítica.

**Partición temporal.** Se congela una versión del corpus y se ordenan unidades por `Date received`. Se definen tres intervalos contiguos antes de entrenar: periodo anterior para entrenamiento, periodo posterior para validación y periodo más reciente para prueba. Las fechas concretas dependen de la versión distribuida, pero deben ser comunes a toda la cohorte y dejar soporte suficiente por producto. El conjunto de prueba no se usa para armonizar categorías, escoger términos, seleccionar modelos, calibrar confianza ni decidir umbrales.

La temporalidad tiene prioridad sobre conservar idénticas proporciones. Se reporta la distribución de `Product` por periodo para detectar deriva. Si una categoría tiene soporte insuficiente, el equipo docente puede fijar un mapa de agrupación antes de entregar la consigna. Cada estudiante debe usar el mismo mapa; no se agrupan productos después de ver errores de prueba.

**Duplicados y plantillas.** Narrativas exactas o casi duplicadas pueden provenir de reenvíos o plantillas. Su presencia en entrenamiento y evaluación inflaría el resultado por memorización textual. Se construye `grupo_duplicado` durante REC-01 y todas las unidades del grupo quedan en un solo conjunto. Cuando un grupo cruza una frontera temporal, el protocolo debe fijar una solución conservadora común, por ejemplo asignarlo íntegramente al periodo de su primera aparición o excluirlo de la comparación principal y contabilizarlo. Nunca se reparte para mejorar el balance. Deben informarse cantidad de grupos, registros afectados y regla aplicada.

**Baselines.** El mínimo es la clase mayoritaria estimada solo con entrenamiento. Debe informarse su accuracy y macro-F1 para mostrar cómo el desbalance afecta ambas. Se recomienda además un baseline textual de palabras simples, con vocabulario, frecuencias y pesos ajustados exclusivamente en entrenamiento. Su propósito es establecer una referencia reproducible, no agotar la modelización de REC-03. Cualquier regla por palabras clave debe definirse sin consultar prueba.

**Métrica principal y auxiliares.** La métrica principal es **macro-F1**, porque cada producto contribuye por igual y los productos menos frecuentes no quedan ocultos por categorías dominantes. Se reportan además accuracy, F1 por clase, precisión y sensibilidad por clase, soporte y matriz de confusión. La matriz debe mostrarse con conteos y normalización por clase real. Si se utilizan probabilidades o confianza para decidir `enrutar/revisar`, se añade evaluación de calibración o margen, cobertura de automatización y tasa de error entre casos enrutados.

Macro-F1 no elimina la necesidad de interpretación. Una clase con cinco ejemplos puede producir F1 muy variable; el soporte debe acompañarla. Accuracy permite cuantificar rendimiento global, pero no sustituye la métrica principal. Una mejora se acepta solo si procede del mismo conjunto, mapa de etiquetas y protocolo.

**Costos y regla de selección.** Un producto equivocado puede dirigir el reclamo a un equipo incorrecto y demorar atención; la revisión humana consume capacidad. Antes del entrenamiento, el grupo identifica pares de confusión especialmente costosos y define una regla, por ejemplo: maximizar macro-F1 sujeto a no degradar ninguna clase prioritaria más de una tolerancia y a una cobertura de revisión viable. Si se usa abstención, el umbral se elige en validación. `Timely response?` no puede convertirse en etiqueta de urgencia: es un resultado posterior y no valida daño ni vulnerabilidad.

**Protocolo en pseudocódigo.** Este diseño no implementa modelos; ordena las decisiones experimentales:

```text
congelar corpus, mapa común de Product y fechas de corte
verificar narrativa no vacía y campos permitidos
formar grupos de duplicados y plantillas
asignar grupos completos a ENTRENAMIENTO, VALIDACIÓN o PRUEBA respetando tiempo
publicar tabla de conteos, productos, fechas y solapamientos nulos

ajustar baseline mayoritario solo con ENTRENAMIENTO
PARA cada candidato posterior:
    ajustar representación y modelo solo con ENTRENAMIENTO
    evaluar macro-F1 y auxiliares en VALIDACIÓN
    seleccionar con la regla preinscrita
congelar representación, modelo, categorías y política de revisión
evaluar una vez en PRUEBA
documentar errores sin reproducir narrativas completas ni datos identificables
```

**Evidencia individual: ficha experimental.** La entrega debe contener:

| Campo | Contenido requerido |
|---|---|
| Versión | fuente, fecha de descarga, filtros y mapa de productos |
| Unidad y objetivo | reclamo con narrativa; clasificación de `Product` al ingreso |
| Particiones | fechas, conteos y soporte por clase en entrenamiento, validación y prueba |
| Duplicados | método, regla de asignación y prueba de intersección nula |
| Entradas excluidas | lista y justificación temporal, ética o de atajo |
| Baselines | mayoría y baseline textual simple previsto |
| Métricas | macro-F1 principal; auxiliares y forma de agregación |
| Selección | regla, costos, tolerancias y eventual umbral de revisión |
| Prueba | compromiso de uso único y condiciones para abrirla |
| Limitaciones | consentimiento, cobertura, deriva y clases con poco soporte |

**Comprobaciones de aprobación.** Debe observarse que ningún `Complaint ID` ni `grupo_duplicado` aparece en más de una partición; que validación y prueba son posteriores a entrenamiento; que vocabulario y cualquier estadística se ajustarán dentro de entrenamiento; y que no existe campo posterior a la respuesta. La métrica principal ha de responder al desbalance, prueba debe quedar reservada y los ejemplos de error no deben reproducir relatos completos ni información que facilite reidentificación.

**Modalidad de trabajo:** discusión grupal del caso y de los costos; protocolo y justificación individuales. El protocolo común permite que las diferencias posteriores correspondan a representaciones o modelos y no a particiones oportunistas.

**Aporte al laboratorio:** REC-02 fija la medición con la que se compararán unigramas, bigramas, decisiones de normalización y clasificadores lineales. REC-03 ajustará TF-IDF sin fuga; REC-04 analizará errores, confianza y abstención. El producto final sugerirá un producto y podrá derivar casos inciertos a revisión humana, pero no generará respuestas ni tomará decisiones financieras.

## Síntesis del capítulo

Formular un problema de aprendizaje exige especificar unidad, población, instante, entradas disponibles, objetivo, etiqueta y consecuencias del error. Supervisión describe el origen de la señal, mientras regresión, clasificación y agrupamiento describen la tarea. El aprendizaje semisupervisado aprovecha entradas no etiquetadas junto con etiquetas escasas; el autosupervisado deriva objetivos de los propios datos para aprender representaciones.

El ajuste minimiza una pérdida empírica, pero el objetivo científico y operativo es generalizar. Sobreajuste, subajuste, sesgo, varianza y complejidad ayudan a diagnosticar la relación entre entrenamiento y datos nuevos. Los baselines convierten una cifra aislada en una comparación con significado.

La evaluación separa entrenamiento, validación y prueba y replica la estructura del uso futuro. Aleatoriedad y estratificación sirven para unidades intercambiables; grupos, duplicados y tiempo requieren particiones específicas. Toda transformación aprendida se ajusta dentro de entrenamiento. La prueba no es un recurso de desarrollo.

MAE, RMSE y $R^2$ describen aspectos diferentes del error de regresión. En clasificación, la matriz de confusión conecta exactitud, precisión, sensibilidad, especificidad y F1 con conteos reales. ROC-AUC y PR-AUC resumen ordenamiento a través de umbrales, pero la decisión final requiere costos, capacidad, prevalencia y, cuando corresponde, abstención. Una evaluación honesta no busca la métrica más alta: construye evidencia relevante, trazable e incierta sobre una decisión definida.

## Glosario esencial

- **Atributo o entrada:** información disponible al momento de producir una predicción.
- **Baseline:** referencia sencilla y reproducible contra la cual se mide valor agregado.
- **Calibración:** correspondencia entre probabilidades pronosticadas y frecuencias observadas.
- **Clase positiva:** categoría elegida como referencia para definir TP, FP, TN y FN.
- **Deriva:** cambio temporal en entradas, etiquetas o su relación.
- **Etiqueta:** representación observable del objetivo en los datos.
- **Fuga de información:** uso durante entrenamiento o selección de información no disponible legítimamente al predecir.
- **Generalización:** desempeño sobre nuevas unidades bajo una población y escenario declarados.
- **Hiperparámetro:** decisión externa al ajuste ordinario que controla el procedimiento de aprendizaje.
- **Macro-F1:** promedio no ponderado del F1 calculado para cada clase.
- **Pérdida:** penalización por el desacuerdo entre resultado y predicción.
- **Prueba:** conjunto reservado para estimar el procedimiento final ya congelado.
- **Riesgo empírico:** pérdida promedio observada en una muestra.
- **Sobreajuste:** adaptación a particularidades del desarrollo que no se sostienen fuera de muestra.
- **Subajuste:** incapacidad para capturar estructura relevante incluso en entrenamiento.
- **Umbral:** punto que transforma una puntuación continua en una decisión.
- **Validación:** datos o procedimiento usado para seleccionar modelos, hiperparámetros y reglas.

## Preguntas de autoevaluación

1. ¿Por qué «predecir gravedad» no queda completamente definido sin una etiqueta, un instante y un horizonte?
2. ¿En qué difieren aprendizaje semisupervisado y autosupervisado? Proponga una cadena que use ambos.
3. ¿Por qué un código numérico de categoría no convierte una clasificación en regresión?
4. ¿Qué diferencia existe entre función de pérdida, métrica de selección y costo operativo?
5. ¿Cómo pueden ser simultáneamente bajos el error de entrenamiento y la validez externa?
6. ¿Qué patrones de curvas de aprendizaje sugieren subajuste y alta varianza?
7. ¿Por qué probar muchas configuraciones puede sobreajustar validación aunque cada modelo sea simple?
8. ¿Cuándo una partición aleatoria estratificada resulta inadecuada?
9. ¿Qué información debe ajustarse de nuevo dentro de cada fold de validación cruzada?
10. ¿Por qué la desviación entre folds no es automáticamente un intervalo de confianza?
11. ¿Cómo cambia la pregunta de generalización al dividir por persona en lugar de por fila?
12. ¿Qué diferencia práctica existe entre MAE y RMSE ante valores extremos?
13. ¿Puede $R^2$ ser negativo en prueba? Interprete ese resultado.
14. Con $TP=18$, $FP=6$, $FN=12$ y $TN=64$, calcule accuracy, precisión, sensibilidad, especificidad y F1.
15. ¿Por qué ROC-AUC alta no garantiza una carga aceptable de falsas alarmas en una población desbalanceada?
16. ¿Por qué el umbral 0,5 no debe adoptarse automáticamente?
17. En REC-02, ¿qué campos constituirían fuga posterior y por qué `Company` puede ser un atajo?
18. ¿Qué evidencia demostraría que los duplicados CFPB no contaminan la prueba?

## Actividad integradora de cierre

Redacte una ficha de evaluación para uno de estos problemas: regresión de demora de viajes, clasificación de excedencias de agua o clasificación temática de reclamos. No implemente un modelo. La ficha debe incluir unidad, población, instante, horizonte, entradas permitidas, etiqueta, dos riesgos de fuga, baseline, partición y su justificación, métrica principal, tres métricas auxiliares y costos de dos errores.

Añada un diagrama textual del flujo de datos y una tabla hipotética de resultados para dos candidatos. Decida cuál avanzaría a prueba aplicando una regla escrita antes de la tabla. Después analice qué cambio de población invalidaría la conclusión y qué evidencia de monitoreo permitiría detectarlo. La evaluación se considera completa cuando otra persona puede reproducir la partición, comprender la decisión y señalar con precisión qué afirmación de generalización está respaldada.
