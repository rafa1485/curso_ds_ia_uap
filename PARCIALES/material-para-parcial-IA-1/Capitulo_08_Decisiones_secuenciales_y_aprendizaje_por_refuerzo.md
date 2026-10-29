# Capítulo 8. Decisiones secuenciales y aprendizaje por refuerzo

Decidir no consiste solamente en predecir qué ocurrirá. Una predicción estima resultados posibles; una decisión elige una acción teniendo en cuenta esos resultados, sus probabilidades, las preferencias del decisor y las restricciones existentes. La diferencia es sustantiva: dos organizaciones pueden compartir el mismo pronóstico de demanda y, sin embargo, tomar decisiones distintas porque afrontan costos, responsabilidades o tolerancias al riesgo diferentes.

La dificultad aumenta cuando las decisiones forman una secuencia. Bombear agua ahora modifica el nivel del depósito, ese nivel condiciona las acciones disponibles después y cada acción genera costos y riesgos futuros. En tales problemas no basta con optimizar el beneficio inmediato. Es preciso representar el estado del sistema, anticipar transiciones, acumular consecuencias a lo largo del tiempo y establecer una regla de actuación. Los procesos de decisión de Markov proporcionan el lenguaje matemático para hacerlo. Cuando el modelo de transición o de recompensa no se conoce, el aprendizaje por refuerzo estudia cómo aprender esa regla mediante interacción.

Este capítulo avanza desde decisiones únicas bajo incertidumbre hasta decisiones secuenciales y aprendizaje. El propósito no es presentar algoritmos como recetas aisladas, sino mostrar qué supuestos convierten una situación real en un problema formal, qué garantiza cada método y dónde puede fallar. Se empleará como caso conductor la operación simplificada de una red de agua. Las cantidades monetarias se expresan en unidades de costo (u.c.) para concentrar la atención en el razonamiento.

Al finalizar, el lector podrá distinguir alternativas, estados y consecuencias; justificar una función de utilidad; calcular utilidad esperada y valor de información; formular un proceso de decisión de Markov; interpretar funciones de valor y ecuaciones de Bellman; comparar iteración de políticas e iteración de valores; y explicar las diferencias entre Monte Carlo, diferencias temporales, Q-learning y SARSA. También podrá reconocer cuándo la recompensa no representa el objetivo social, cuándo explorar es inseguro y cuándo no corresponde desplegar aprendizaje por refuerzo.

## 8.1. Decisiones bajo incertidumbre

Una decisión bajo incertidumbre combina un conjunto de acciones controlables con hechos que el decisor no controla. Su tratamiento riguroso exige evitar tres confusiones frecuentes: una probabilidad no es una preferencia, el resultado más probable no tiene por qué ser la mejor base para actuar y una expectativa monetaria no siempre representa el valor que una persona u organización asigna a una consecuencia.

### 8.1.1. Alternativas, estados y consecuencias

Sea \(A=\{a_1,\ldots,a_m\}\) el conjunto de **alternativas** disponibles y \(S=\{s_1,\ldots,s_n\}\) el conjunto de **estados de la naturaleza** mutuamente excluyentes y exhaustivos. Una alternativa es controlable: inspeccionar una tubería, repararla de forma preventiva o esperar. Un estado no lo es: existe una fuga grave o no existe. La **consecuencia** \(c(a,s)\) resulta de ejecutar \(a\) cuando ocurre \(s\). Puede incluir costo, tiempo, continuidad del servicio, daño ambiental y reputación.

La tabla siguiente representa una decisión estática. Los valores son costos; por ello, cantidades menores son preferibles.

| Alternativa | Fuga grave \(s_1\) | Sin fuga grave \(s_2\) |
|---|---:|---:|
| Reparar preventivamente \(a_1\) | 32 | 28 |
| Inspeccionar \(a_2\) | depende del resultado y de la acción posterior | depende del resultado y de la acción posterior |
| Esperar \(a_3\) | 120 | 2 |

La consecuencia no debe confundirse con el estado. “Fuga grave” describe el mundo; “pérdida de 120 u.c. por esperar ante una fuga grave” describe la combinación de mundo y acción. Esta separación permite preguntar de dónde procede cada cantidad y someterla a análisis de sensibilidad.

Los estados deben cubrir las incertidumbres relevantes para la decisión, pero no todos los detalles imaginables. Si dos estados producen las mismas consecuencias para todas las alternativas, distinguirlos no modifica la elección. En cambio, agrupar “fuga leve” y “rotura inminente” puede ocultar una diferencia decisiva. La representación es, por tanto, un compromiso entre fidelidad y manejabilidad.

En ocasiones, la acción cambia la probabilidad del estado observado después. Entonces conviene escribir \(P(s\mid a)\), no \(P(s)\). Una intervención de mantenimiento puede reducir la probabilidad de falla; una prueba diagnóstica, en cambio, normalmente informa sobre una condición previa sin causarla. Confundir efectos causales con asociaciones observacionales genera decisiones incorrectas incluso si las probabilidades están bien calculadas.

**Error frecuente.** Elegir la alternativa asociada al estado más probable ignora los demás estados. Aunque la fuga grave tenga probabilidad baja, su daño puede justificar una reparación. La decisión debe considerar conjuntamente probabilidad y consecuencia.

### 8.1.2. Preferencias y teoría de utilidad

Una relación de preferencia \(\succeq\) expresa que una consecuencia o lotería se considera al menos tan deseable como otra. Se escribe \(x\succ y\) si \(x\) se prefiere estrictamente a \(y\), y \(x\sim y\) si existe indiferencia. La teoría de utilidad representa numéricamente preferencias coherentes; no descubre por sí sola qué debería valorar una institución.

En contextos inciertos, una **lotería** asigna probabilidades a consecuencias. Bajo axiomas como completitud, transitividad, continuidad e independencia, existe una función \(U\) tal que las preferencias entre loterías se representan por su utilidad esperada. Completitud exige poder comparar alternativas; transitividad impide ciclos como \(x\succ y\), \(y\succ z\) y \(z\succ x\); continuidad descarta saltos extremos; independencia establece una forma precisa de consistencia al mezclar loterías. Estos axiomas son modelos normativos y pueden no describir perfectamente el comportamiento humano.

La escala de utilidad de von Neumann-Morgenstern es única salvo transformaciones afines positivas. Si \(U\) representa las preferencias, \(U'(x)=\alpha U(x)+\beta\), con \(\alpha>0\), representa las mismas. Por ello, el cero y la unidad son convencionales, y no es válido comparar diferencias de utilidad obtenidas con escalas construidas independientemente para personas distintas.

Cuando hay múltiples atributos, por ejemplo costo \(C\), interrupción \(D\) y daño ambiental \(E\), puede formularse \(U(C,D,E)\). Una suma ponderada,

\[
U(C,D,E)=w_Cu_C(C)+w_Du_D(D)+w_Eu_E(E),
\]

solo es justificable bajo condiciones de independencia preferencial. Los pesos no son meramente “importancias”: dependen de las escalas de los atributos y de los intercambios aceptables. Las restricciones legales o de seguridad no deben convertirse sin reflexión en pequeñas penalizaciones. Si una consecuencia es inadmisible, puede excluirse del conjunto factible antes de optimizar.

Para elicitar utilidad se pueden comparar consecuencias ciertas con loterías de referencia. Si el decisor es indiferente entre una consecuencia \(x\) y una lotería que entrega el mejor resultado con probabilidad \(p\) y el peor con probabilidad \(1-p\), normalizando sus utilidades a 1 y 0 se obtiene \(U(x)=p\). El procedimiento debe documentar quién respondió, con qué información y bajo qué responsabilidad.

### 8.1.3. Utilidad esperada

Si la alternativa \(a\) induce probabilidades \(P(s\mid a)\), su utilidad esperada es

\[
EU(a)=\sum_{s\in S}P(s\mid a)\,U(c(a,s)).
\]

La regla de utilidad esperada selecciona

\[
a^*\in\arg\max_{a\in A}EU(a).
\]

El símbolo \(\arg\max\) devuelve una o varias alternativas; un empate requiere una regla adicional. Si se trabaja con costos y la utilidad es \(U(c)=-c\), maximizar utilidad equivale a minimizar costo esperado.

Supóngase que la probabilidad de fuga grave es \(0{,}20\). Reparar cuesta 32 si hay fuga y 28 si no la hay; esperar cuesta 120 o 2, respectivamente. Los costos esperados son

\[
EC(a_1)=0{,}20(32)+0{,}80(28)=28{,}8,
\]

\[
EC(a_3)=0{,}20(120)+0{,}80(2)=25{,}6.
\]

Con utilidad lineal en dinero, esperar es preferible pese a que la pérdida posible sea mucho mayor. La comparación no afirma que esperar sea universalmente correcto: depende de \(0{,}20\), de los costos incluidos y de la linealidad. Si el costo de una falla excluye sanciones, daño ambiental o pérdida de vidas, el cálculo está incompleto.

El **análisis de sensibilidad** pregunta cuándo cambia la decisión. Si \(p=P(s_1)\), reparar tiene costo \(28+4p\), mientras esperar tiene \(2+118p\). Son iguales cuando

\[
28+4p=2+118p \quad\Longrightarrow\quad p^*=\frac{26}{114}\approx0{,}228.
\]

Por encima de ese umbral conviene reparar bajo los supuestos del modelo; por debajo conviene esperar. Informar el umbral suele ser más útil que comunicar una recomendación sin contexto. También permite apreciar si una pequeña imprecisión probabilística podría invertir la decisión.

La esperanza es una media de largo plazo o una valoración coherente de una lotería, no una promesa sobre un caso individual. Tampoco elimina la incertidumbre. Debe acompañarse de escenarios extremos, distribución de consecuencias y restricciones de tolerancia.

### 8.1.4. Actitudes frente al riesgo

Para riqueza final \(w\), una utilidad lineal indica neutralidad al riesgo; una utilidad cóncava, \(U''(w)<0\), aversión; y una utilidad convexa, \(U''(w)>0\), propensión. Con utilidad cóncava y una lotería \(W\), la desigualdad de Jensen establece

\[
U(\mathbb{E}[W])\geq \mathbb{E}[U(W)].
\]

El **equivalente cierto** \(CE\) satisface \(U(CE)=\mathbb{E}[U(W)]\). Para una persona adversa al riesgo, \(CE<\mathbb{E}[W]\). La diferencia \(\mathbb{E}[W]-CE\) es la prima máxima que estaría dispuesta a pagar para eliminar el riesgo.

Considérese una riqueza de 100 y \(U(w)=\sqrt{w}\). Una lotería entrega riqueza 100 con probabilidad 0,8 y 0 con probabilidad 0,2. Su utilidad esperada es \(0{,}8\sqrt{100}+0{,}2\sqrt{0}=8\), por lo que \(CE=8^2=64\). Aunque la riqueza esperada es 80, la lotería se valora como 64 bajo esa función.

La aversión al riesgo no equivale a pesimismo ni a asignar más probabilidad a eventos adversos. Las probabilidades describen creencias; la curvatura describe preferencias. Tampoco toda organización debe usar una utilidad cóncava sobre costos agregados: una entidad grande puede diversificar pérdidas financieras, pero no “diversificar” muertes o daños irreversibles. En seguridad se combinan a menudo utilidad esperada, restricciones duras, medidas de riesgo de cola y criterios robustos.

Entre esas medidas se encuentra el valor en riesgo, \(VaR_\alpha\), un cuantil de pérdida, y el valor en riesgo condicional, \(CVaR_\alpha\), que resume pérdidas en la cola más desfavorable. El primero puede ocultar la severidad más allá del cuantil; el segundo es más informativo sobre extremos, pero depende igualmente de un modelo probabilístico fiable.

**Error frecuente.** Modificar probabilidades “para reflejar prudencia” mezcla creencias con preferencias. Es más transparente conservar probabilidades calibradas y representar prudencia mediante utilidad, restricciones o una medida de riesgo explícita.

### 8.1.5. Árboles de decisión

Un árbol de decisión ordena cronológicamente elecciones e incertidumbres. Los nodos de decisión se representan convencionalmente con cuadrados, los nodos aleatorios con círculos y las hojas con consecuencias. Cada rama aleatoria lleva una probabilidad condicional; las ramas que parten del mismo nodo deben sumar uno.

La evaluación se realiza **de derecha a izquierda**. En un nodo aleatorio se calcula utilidad esperada. En un nodo de decisión se conserva la rama de mayor utilidad esperada. Este proceso, llamado repliegue o *rollback*, produce una estrategia contingente: no solo la primera acción, sino qué hacer después de cada observación posible.

**Pseudocódigo: repliegue de un árbol**

```text
FUNCIÓN VALOR(nodo)
    SI nodo es una hoja
        DEVOLVER utilidad de su consecuencia
    SI nodo es aleatorio
        total <- 0
        PARA CADA rama del nodo
            total <- total + probabilidad(rama) * VALOR(hijo(rama))
        DEVOLVER total
    SI nodo es de decisión
        evaluar VALOR(hijo) para cada acción factible
        registrar una acción que alcance el valor máximo
        DEVOLVER el valor máximo
FIN FUNCIÓN
```

El orden importa. “Inspeccionar y luego reparar si el resultado es positivo” es diferente de “reparar y luego inspeccionar”: la segunda observación ya no puede mejorar la primera acción. Asimismo, las probabilidades posteriores a un resultado de prueba deben calcularse mediante Bayes, no confundirse con sensibilidad o especificidad.

Los árboles son especialmente claros para pocas etapas, pero crecen exponencialmente cuando aumentan observaciones y decisiones. Además, repetir el mismo estado por caminos distintos duplica subproblemas. Los procesos de decisión de Markov compactan esa repetición al representar estados y reutilizar sus valores.

Antes de calcular, conviene auditar el árbol: ¿todas las acciones son realmente factibles?, ¿cada incertidumbre aparece después de la información que la condiciona?, ¿las hojas contienen todas las consecuencias relevantes?, ¿se han normalizado probabilidades?, ¿una misma cantidad se contó dos veces? Un diagrama visualmente impecable puede formalizar mal el problema.

### 8.1.6. Valor de la información

La información tiene valor instrumental: vale porque permite elegir mejor. El **valor esperado de la información perfecta** (VEIP) compara decidir después de observar exactamente el estado con decidir sin esa observación:

\[
VEIP=\sum_s P(s)\max_a U(c(a,s))-\max_a\sum_sP(s)U(c(a,s)).
\]

En una formulación de costos,

\[
VEIP=\min_a\mathbb{E}[C(a,S)]-\mathbb{E}[\min_a C(a,S)].
\]

El VEIP es no negativo y constituye un límite superior para pagar por cualquier prueba imperfecta acerca del mismo estado. No es el valor de eliminar físicamente la incertidumbre, sino el de conocer su realización antes de actuar.

Para una prueba con resultado \(Y\), el **valor esperado de la información muestral** (VEIM) es

\[
VEIM=\sum_yP(y)\max_a\sum_sP(s\mid y)U(c(a,s))
-\max_a\sum_sP(s)U(c(a,s)).
\]

La prueba conviene si su valor neto, \(VEIM-C_{prueba}\), es positivo y si satisface restricciones de tiempo y seguridad. Una prueba gratuita puede tener valor cero si nunca cambia la acción. Del mismo modo, una prueba muy precisa puede llegar demasiado tarde.

Con los costos de la sección 8.1.3 y \(p=0{,}20\), sin información se espera y el costo es 25,6. Con información perfecta se repara ante fuga y se espera sin fuga: \(0{,}2(32)+0{,}8(2)=8\). Por tanto, \(VEIP=25{,}6-8=17{,}6\) u.c. Ninguna inspección orientada únicamente a identificar ese estado debería pagarse por encima de 17,6 u.c. bajo este modelo.

**Errores frecuentes.** Restar el costo de la prueba dos veces; usar \(P(y\mid s)\) como si fuera \(P(s\mid y)\); y valorar información con una acción posterior fijada de antemano. La esencia del cálculo es volver a optimizar después de cada resultado.

### 8.1.7. Ejemplo práctico guiado: decisión de inspección y reemplazo de un transformador

Una empresa opera un transformador cuyo estado real no se observa directamente. Puede existir una falla interna relevante, \(F\), con probabilidad previa \(P(F)=0{,}20\), o el equipo puede estar sano, \(\neg F\). La decisión inmediata es reemplazarlo, esperar y mantenerlo en servicio, o inspeccionarlo por 4 u.c. Si se inspecciona, el resultado es positivo o negativo y luego se elige entre reemplazar y esperar.

Los costos, expresados en unidades comparables, incorporan intervención, indisponibilidad y daño esperado:

| Acción | Falla \(F\) | Sin falla \(\neg F\) |
|---|---:|---:|
| Reemplazar | 32 | 28 |
| Esperar | 120 | 2 |

Tomando utilidad monetaria \(U=-C\), maximizar utilidad esperada equivale a minimizar costo esperado. Sin inspección,

\[
EC(\text{reemplazar})=0{,}2(32)+0{,}8(28)=28{,}80,
\]

\[
EC(\text{esperar})=0{,}2(120)+0{,}8(2)=25{,}60.
\]

Por tanto, con la creencia previa conviene esperar. Si \(p=P(F)\), reemplazar pasa a ser preferible cuando

\[
28+4p<2+118p,
\qquad p>\frac{26}{114}\approx0{,}228.
\]

La inspección tiene sensibilidad \(P(+\mid F)=0{,}90\) y tasa de falsos positivos \(P(+\mid\neg F)=0{,}10\). Las probabilidades de sus observaciones son

\[
P(+)=0{,}9(0{,}2)+0{,}1(0{,}8)=0{,}26,
\qquad P(-)=0{,}74.
\]

La regla de Bayes actualiza la creencia sobre la falla:

\[
P(F\mid +)=\frac{0{,}9(0{,}2)}{0{,}26}\approx0{,}6923,
\]

\[
P(F\mid -)=\frac{0{,}1(0{,}2)}{0{,}74}\approx0{,}0270.
\]

El resultado positivo supera el umbral de 0,228, mientras que el negativo queda por debajo. La regla posterior óptima es entonces reemplazar tras `+` y esperar tras `-`. Antes de sumar el precio de la prueba, los costos condicionales son

\[
EC(\text{reemplazar}\mid +)=28+4(0{,}6923)=30{,}769,
\]

\[
EC(\text{esperar}\mid -)=2+118(0{,}0270)=5{,}189.
\]

Así, el costo esperado de inspeccionar y actuar según el resultado es

\[
EC(\text{inspeccionar})=4+0{,}26(30{,}769)+0{,}74(5{,}189)=15{,}84.
\]

| Estrategia inicial | Regla posterior | Costo esperado |
|---|---|---:|
| Reemplazar ahora | no aplica | 28,80 |
| Esperar | no aplica | 25,60 |
| Inspeccionar | reemplazar si `+`; esperar si `-` | 15,84 |

La información muestral vale, antes de pagarla, \(25{,}60-(15{,}84-4)=13{,}76\) u.c. Su valor neto es \(13{,}76-4=9{,}76\) u.c.; por eso la inspección es la mejor decisión inicial. Con información perfecta se reemplazaría ante falla y se esperaría en caso contrario, con costo \(0{,}2(32)+0{,}8(2)=8\). El VEIP es \(25{,}60-8=17{,}60\) u.c., mayor que el valor de la prueba imperfecta.

La recomendación depende de los supuestos. Si la prueba demora y el deterioro puede avanzar durante ese lapso, debe agregarse esa consecuencia. Si una falla plantea un riesgo no compensable, la utilidad monetaria esperada deja de ser el único criterio. También deben verificarse la validez de sensibilidad y especificidad para este tipo de equipo, la disponibilidad del repuesto y la capacidad de ejecutar el reemplazo indicado por cada observación.

## 8.2. Procesos de decisión de Markov

En una decisión secuencial, la acción actual altera las situaciones futuras. Un proceso de decisión de Markov (MDP, por sus siglas en inglés) finito puede definirse mediante la tupla

\[
\mathcal{M}=(\mathcal{S},\mathcal{A},P,R,\gamma,\rho_0),
\]

donde \(\mathcal{S}\) es el espacio de estados, \(\mathcal{A}\) el de acciones, \(P\) el modelo de transición, \(R\) el de recompensa, \(\gamma\) el factor de descuento y \(\rho_0\) la distribución inicial. En horizonte finito también se especifica el número de etapas \(H\). Algunas convenciones incorporan estados terminales o acciones dependientes del estado.

### 8.2.1. Propiedad de Markov

Sea la historia hasta el tiempo \(t\), \(H_t=(S_0,A_0,R_1,\ldots,S_t)\). La propiedad de Markov afirma que, condicionado al estado y la acción actuales, el siguiente resultado no depende de la historia completa:

\[
P(S_{t+1},R_{t+1}\mid H_t,A_t)
=P(S_{t+1},R_{t+1}\mid S_t,A_t).
\]

No significa que el pasado sea irrelevante. Significa que toda información del pasado necesaria para predecir el futuro y valorar decisiones ha sido resumida en \(S_t\). Por ejemplo, “nivel actual del depósito” quizá no sea suficiente si el desgaste acumulado de una bomba cambia su probabilidad de falla. Incorporar una categoría de desgaste puede restaurar aproximadamente la propiedad.

El carácter markoviano depende de la representación, no solo del sistema físico. Una observación parcial puede no ser un estado. Si el operador ve presión pero no el daño oculto de la tubería, dos historias con igual presión pueden tener futuros distintos. El marco apropiado sería entonces un MDP parcialmente observable, donde se decide a partir de una creencia sobre estados ocultos, o bien un MDP aproximado cuya limitación debe declararse.

La propiedad también suele acompañarse de **estacionariedad**: \(P\) y \(R\) no cambian con \(t\). Son supuestos diferentes. Un proceso puede ser markoviano y tener demanda estacional. Agregar hora, día o estación al estado puede representar esa variación; si las dinámicas cambian por envejecimiento o clima no observado, el entorno es no estacionario.

Una prueba empírica de Markov perfecta rara vez es posible. Se examina si variables históricas aportan predicción residual una vez condicionado el estado, se consulta conocimiento del dominio y se analiza el desempeño fuera de muestra. Un estado demasiado pequeño pierde información; uno excesivamente detallado agrava el costo computacional y la escasez de experiencia en cada combinación.

### 8.2.2. Estados, acciones y transiciones

El estado \(s\in\mathcal{S}\) debe ser suficiente para decidir. En un depósito simplificado podría ser nivel bajo (B), medio (M) o alto (A). Las acciones podrían ser apagar (0) o encender (1) una bomba. No todas las acciones tienen que ser factibles en todos los estados; \(\mathcal{A}(s)\) representa las disponibles.

La dinámica se expresa mediante

\[
P(s'\mid s,a)=P(S_{t+1}=s'\mid S_t=s,A_t=a),
\]

con \(P(s'\mid s,a)\geq0\) y \(\sum_{s'}P(s'\mid s,a)=1\). Para espacios finitos, cada acción puede asociarse con una matriz de transición. La fila corresponde al estado actual y la columna al siguiente.

| Estado y acción | Próximo B | Próximo M | Próximo A |
|---|---:|---:|---:|
| B, apagar | 0,8 | 0,2 | 0,0 |
| B, encender | 0,2 | 0,7 | 0,1 |
| M, apagar | 0,6 | 0,4 | 0,0 |
| M, encender | 0,1 | 0,6 | 0,3 |
| A, apagar | 0,1 | 0,7 | 0,2 |
| A, encender | 0,0 | 0,2 | 0,8 |

La incertidumbre puede provenir de demanda, clima, medición o fallas. Una transición determinista es el caso especial en que una probabilidad vale uno. La tabla debe reflejar el intervalo temporal elegido: las probabilidades por hora no se usan directamente como probabilidades diarias.

Estimar \(P\) a partir de datos históricos requiere atender al sesgo de política. Si la organización siempre enciende la bomba cuando el nivel es bajo, habrá poca evidencia sobre “B, apagar”. Además, los registros observacionales pueden mezclar acciones con condiciones no incluidas en el estado. Una transición aprendida describe asociaciones condicionadas; interpretarla como efecto de intervenir exige supuestos causales.

**Error frecuente.** Definir como estado la identificación única de cada registro. Eso permite memorizar, pero no generalizar ni reutilizar valores. El estado debe agrupar situaciones equivalentes para la decisión sin borrar diferencias predictivas relevantes.

### 8.2.3. Recompensas

La recompensa \(R_{t+1}\) es la señal numérica recibida tras actuar. El modelo puede especificar su esperanza como

\[
r(s,a,s')=\mathbb{E}[R_{t+1}\mid S_t=s,A_t=a,S_{t+1}=s']
\]

o como \(r(s,a)\) cuando no se necesita distinguir \(s'\). Una recompensa positiva no es necesariamente dinero y una penalización puede representarse como recompensa negativa. Cambiar todos los signos transforma maximización de recompensa en minimización de costo, pero mezclar ambas convenciones dentro del cálculo produce errores.

En el depósito, una recompensa posible es “servicio menos energía y desgaste”:

\[
r(s,a,s')=-c_{\text{energ\'ia}}(a)-c_{\text{desgaste}}(s,a)-c_{\text{servicio}}(s').
\]

Una penalización alta por llegar a B expresa la importancia de evitar desabastecimiento. Sin embargo, la recompensa es una **representación** del objetivo, no el objetivo mismo. Debe distinguir indicadores sustitutivos, como nivel del depósito, de resultados finales, como continuidad segura y equitativa del servicio.

Las recompensas densas aparecen con frecuencia y facilitan atribuir mérito; las escasas ocurren solo al alcanzar un objetivo o terminar un episodio. Una señal densa mal construida puede incentivar mantener el indicador sin resolver el problema. Una señal escasa dificulta aprender qué acciones tempranas contribuyeron al resultado.

En tareas continuas, sumar una constante a cada recompensa puede cambiar preferencias si los episodios tienen longitudes distintas, aunque en un problema continuo descontado con longitud fija no cambie la política óptima bajo ciertos supuestos. Escalar recompensas tampoco es inocuo para la estabilidad numérica de algoritmos de aprendizaje. La unidad, el rango y la frecuencia deben documentarse.

No deben ocultarse restricciones críticas mediante penalizaciones arbitrarias. Si está prohibido superar una presión, el conjunto de acciones o un mecanismo de seguridad puede excluir esa conducta. Una penalización finita podría ser compensada por otras recompensas y permitir una violación.

### 8.2.4. Políticas

Una **política** especifica cómo actuar. Una política determinista estacionaria es una función \(\pi:\mathcal{S}\to\mathcal{A}\). Una política estocástica asigna una distribución:

\[
\pi(a\mid s)=P(A_t=a\mid S_t=s),
\qquad \sum_a\pi(a\mid s)=1.
\]

Por ejemplo, una política determinista puede encender en B y M, y apagar en A. Una política estocástica podría encender en M con probabilidad 0,7. La aleatorización es útil para explorar, resolver ciertos problemas con restricciones o evitar predictibilidad frente a otros agentes; no es sinónimo de indecisión.

Una política abierta fija una secuencia de acciones sin observar estados. Una política de realimentación condiciona cada acción al estado observado y suele ser más robusta frente a perturbaciones. En horizonte finito, la política óptima puede depender del tiempo restante, \(\pi_t(a\mid s)\): con una etapa pendiente puede no valer la pena encender una bomba, aunque sí con muchas etapas.

El objetivo habitual es hallar \(\pi^*\) que maximice el retorno esperado desde todos los estados o desde una distribución inicial. Puede haber varias políticas óptimas. La política calculada solo tiene sentido para las acciones, estados, recompensas y horizonte modelados. Si en operación se impone una regla externa que modifica acciones, la política ejecutada difiere de la evaluada.

Evaluar una política exige especificar también su **cobertura**: en qué estados es válida y qué hace ante estados desconocidos. Una tabla incompleta no es una política desplegable. En sistemas reales se añaden reglas de abstención, intervención humana y retorno a un modo seguro.

### 8.2.5. Horizonte y factor de descuento

El retorno desde el tiempo \(t\) acumula recompensas futuras. Para horizonte finito \(H\),

\[
G_t=\sum_{k=0}^{H-t-1}\gamma^kR_{t+k+1}.
\]

Para horizonte infinito descontado,

\[
G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1},
\qquad 0\leq\gamma<1.
\]

El factor \(\gamma\) reduce el peso matemático de recompensas lejanas y, con recompensas acotadas, garantiza que la suma infinita sea finita. También puede modelar preferencia temporal o probabilidad de que el proceso continúe. No debe elegirse solo porque “el algoritmo converge”: su interpretación afecta la política.

El horizonte puede ser episódico, con un estado terminal, o continuo, como la operación permanente de una red. En tareas episódicas con terminación segura se puede usar \(\gamma=1\). En procesos continuos también existe el criterio de recompensa promedio a largo plazo, que no equivale siempre al criterio descontado.

La escala temporal importa. Si \(\gamma_d\) es descuento diario, un descuento horario coherente satisface aproximadamente \(\gamma_h^{24}=\gamma_d\). Usar el mismo número al cambiar el paso temporal altera el horizonte efectivo. Una interpretación práctica es que el peso cae a la mitad después de

\[
h_{1/2}=\frac{\log(0{,}5)}{\log(\gamma)}
\]

etapas. Con \(\gamma=0{,}9\), la semivida es unas 6,58 etapas; con \(0{,}99\), unas 68,97.

Un descuento pequeño favorece resultados inmediatos y puede inducir miopía; uno cercano a uno propaga efectos lejanos, pero aumenta sensibilidad a errores del modelo y suele ralentizar convergencia. Los impactos intergeneracionales o irreversibles no deberían devaluarse automáticamente mediante un parámetro técnico sin deliberación ética.

### 8.2.6. Funciones de valor

La función de valor de estado bajo una política \(\pi\) es el retorno esperado al comenzar en \(s\) y seguir \(\pi\):

\[
V^\pi(s)=\mathbb{E}_\pi[G_t\mid S_t=s].
\]

La función de valor de acción es

\[
Q^\pi(s,a)=\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a],
\]

donde la primera acción se fija en \(a\) y luego se sigue \(\pi\). Se relacionan mediante

\[
V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a).
\]

Las funciones óptimas son \(V^*(s)=\max_\pi V^\pi(s)\) y \(Q^*(s,a)=\max_\pi Q^\pi(s,a)\). Una política codiciosa respecto de \(Q^*\) elige una acción en \(\arg\max_aQ^*(s,a)\).

El valor no es una propiedad intrínseca del estado. Depende de recompensa, horizonte, descuento y política. Un depósito bajo puede tener valor moderado si existe una bomba fiable y energía barata, o muy negativo si la recuperación es lenta. Comparar valores de modelos con escalas de recompensa distintas carece de significado directo.

El **valor de ventaja**,

\[
A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s),
\]

indica cuánto mejora o empeora una acción respecto del promedio de la política en ese estado. Esta descomposición es importante en métodos más avanzados, pero también ofrece una lectura operacional: identifica dónde cambiar la acción tendría mayor efecto.

Una estimación de valor puede ser precisa en estados frecuentes y deficiente en estados raros. Reportar solo el promedio bajo \(\rho_0\) puede esconder fallas críticas. Es necesario examinar valores, incertidumbre y acciones por subgrupos de estados relevantes.

### 8.2.7. Ecuaciones de Bellman

La idea central de Bellman es descomponer el retorno en recompensa inmediata más valor del futuro. Para una política \(\pi\),

\[
V^\pi(s)=\sum_a\pi(a\mid s)\sum_{s'}P(s'\mid s,a)
\left[r(s,a,s')+\gamma V^\pi(s')\right].
\]

En términos de valores de acción,

\[
Q^\pi(s,a)=\sum_{s'}P(s'\mid s,a)
\left[r(s,a,s')+\gamma\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')\right].
\]

Las ecuaciones de optimalidad sustituyen el promedio de acciones futuras por la mejor elección:

\[
V^*(s)=\max_a\sum_{s'}P(s'\mid s,a)
\left[r(s,a,s')+\gamma V^*(s')\right],
\]

\[
Q^*(s,a)=\sum_{s'}P(s'\mid s,a)
\left[r(s,a,s')+\gamma\max_{a'}Q^*(s',a')\right].
\]

Estas expresiones son ecuaciones de punto fijo, no simples definiciones circulares. El operador óptimo de Bellman \(T\), definido por el lado derecho, es una contracción en norma suprema cuando \(\gamma<1\):

\[
\|TV-TW\|_\infty\leq\gamma\|V-W\|_\infty.
\]

Por ello existe un único punto fijo \(V^*\) y aplicar repetidamente \(T\) converge hacia él en el caso tabular finito.

**Errores frecuentes.** Maximizar por separado para cada estado siguiente, como si se pudiera elegir la acción antes de conocer \(s'\); omitir la probabilidad de transición; usar recompensa de \(s\) cuando fue definida sobre \(s'\); y descontar también la recompensa inmediata. La cronología debe estar explícita.

### 8.2.8. Ejemplo práctico guiado: control secuencial de un sistema simplificado

Considérese una batería que se revisa al comienzo de cada período. Su estado de carga se resume como bajo \(B\) o suficiente \(S\), y el controlador elige cargar \(C\) o esperar \(E\). El estado siguiente depende del consumo incierto y de la eficacia de la carga. La siguiente tabla especifica el modelo:

| Estado | Acción | \(P(B\mid s,a)\) | \(P(S\mid s,a)\) | \(r(s,a)\) |
|---|---|---:|---:|---:|
| B | E | 0,8 | 0,2 | -8 |
| B | C | 0,2 | 0,8 | -4 |
| S | E | 0,3 | 0,7 | 0 |
| S | C | 0,1 | 0,9 | -3 |

Las recompensas son negativas porque representan costos. Cargar cuesta electricidad: 4 u.c. en \(B\) y 3 u.c. en \(S\), por diferencias en duración y tarifa esperada. Esperar en \(B\) genera una penalización esperada de 8 u.c. por indisponibilidad; esperar en \(S\) no tiene costo inmediato. Las probabilidades ya resumen consumo y pérdidas durante el período.

Sea \(\gamma=0{,}9\) y considérese la política \(\pi\) que carga en \(B\) y espera en \(S\). Sus ecuaciones de Bellman son

\[
V^\pi(B)=-4+0{,}9[0{,}2V^\pi(B)+0{,}8V^\pi(S)],
\]

\[
V^\pi(S)=0+0{,}9[0{,}3V^\pi(B)+0{,}7V^\pi(S)].
\]

Reordenando,

\[
0{,}82V^\pi(B)-0{,}72V^\pi(S)=-4,
\]

\[
-0{,}27V^\pi(B)+0{,}37V^\pi(S)=0.
\]

La solución es aproximadamente \(V^\pi(B)=-28{,}92\) y \(V^\pi(S)=-21{,}10\). Aunque esperar en \(S\) tiene recompensa inmediata cero, su valor es negativo porque el consumo puede llevar la batería a \(B\) en un período posterior.

Para evaluar una desviación puntual en \(S\),

\[
Q^\pi(S,C)=-3+0{,}9[0{,}1(-28{,}92)+0{,}9(-21{,}10)]\approx-22{,}70.
\]

Como \(Q^\pi(S,E)=V^\pi(S)\approx-21{,}10\), esperar es mejor en \(S\). En \(B\), la alternativa de esperar produce

\[
Q^\pi(B,E)=-8+0{,}9[0{,}8(-28{,}92)+0{,}2(-21{,}10)]\approx-32{,}61,
\]

valor inferior al de cargar, \(-28{,}92\). Ninguna desviación de una etapa mejora la política, de modo que, para este MDP, cargar en \(B\) y esperar en \(S\) es óptimo.

El ejemplo muestra por qué no basta comparar costos inmediatos: cargar en \(S\) reduce la probabilidad de llegar a \(B\), pero ese beneficio futuro no compensa 3 u.c. de electricidad. Una penalización mayor por indisponibilidad, una tarifa más barata o una dinámica distinta podrían cambiar la acción. Antes de aplicar el modelo deben comprobarse degradación de la batería, límites térmicos, potencia disponible y variación horaria de precios; las restricciones críticas deben representarse como acciones no factibles y no solo como costos.

## 8.3. Resolución de procesos de decisión

Cuando \(P\) y \(R\) son conocidos, la programación dinámica aprovecha la estructura recursiva de Bellman. Evaluar una política responde “¿qué rendimiento tendrá esta regla?”. Mejorarla responde “¿qué acción sería preferible según esos valores?”. Iteración de políticas alterna ambas tareas; iteración de valores las combina mediante actualizaciones óptimas.

### 8.3.1. Evaluación de políticas

Para una política fija, la ecuación de Bellman puede escribirse matricialmente:

\[
\mathbf{v}_\pi=\mathbf{r}_\pi+\gamma P_\pi\mathbf{v}_\pi,
\qquad
\mathbf{v}_\pi=(I-\gamma P_\pi)^{-1}\mathbf{r}_\pi.
\]

La solución directa requiere almacenar y resolver un sistema lineal. Para muchos estados se usa evaluación iterativa:

\[
V_{k+1}(s)=\sum_a\pi(a\mid s)\sum_{s'}P(s'\mid s,a)
[r(s,a,s')+\gamma V_k(s')].
\]

**Pseudocódigo: evaluación iterativa de una política**

```text
inicializar V(s) arbitrariamente para estados no terminales
REPETIR
    cambio_máximo <- 0
    PARA CADA estado s
        anterior <- V(s)
        V(s) <- promedio de recompensa inmediata más valor descontado
                según la política y las transiciones desde s
        cambio_máximo <- máximo(cambio_máximo, |anterior - V(s)|)
HASTA QUE cambio_máximo sea menor que la tolerancia
DEVOLVER V
```

Las actualizaciones pueden ser síncronas, usando una copia de \(V_k\), o en el lugar, reutilizando valores recién calculados. Ambas convergen bajo condiciones estándar, aunque con velocidades diferentes. El orden de barrido puede importar para eficiencia, no para el punto fijo.

Detenerse cuando \(\|V_{k+1}-V_k\|_\infty<\varepsilon\) controla el residuo entre iteraciones. No debe confundirse con error exacto, aunque la contracción permite establecer cotas. Una tolerancia excesivamente estricta desperdicia cómputo si \(P\), \(R\) y los datos ya contienen mayor incertidumbre.

Evaluar también puede hacerse mediante simulación cuando el modelo es generativo, pero entonces aparece error muestral. La programación dinámica exacta realiza expectativas sobre todos los sucesores y presupone acceso al modelo completo.

### 8.3.2. Mejora de políticas

El teorema de mejora de políticas establece que, si para todo estado se elige una acción codiciosa respecto de \(V^\pi\), la nueva política \(\pi'\) no es peor:

\[
\pi'(s)\in\arg\max_a\sum_{s'}P(s'\mid s,a)
[r(s,a,s')+\gamma V^\pi(s')].
\]

Entonces \(V^{\pi'}(s)\geq V^\pi(s)\) para todo \(s\). Si la acción actual ya maximiza en todos los estados, \(\pi\) satisface la ecuación de optimalidad y es óptima.

La mejora considera una desviación de una etapa seguida por la política anterior. Aunque parezca local, el valor \(V^\pi(s')\) resume todas las consecuencias futuras, por lo que la comparación no es miope. Después de cambiar acciones, se evalúa la nueva política para propagar los efectos.

Los empates requieren cuidado. Cambiar repetidamente entre acciones de igual valor puede dificultar detectar estabilidad. Una regla determinista, por ejemplo conservar la acción previa cuando está entre las máximas, evita oscilaciones artificiales. En problemas con restricciones, el máximo solo se toma sobre \(\mathcal{A}(s)\).

**Error frecuente.** Mejorar con respecto a recompensas inmediatas \(r(s,a)\) en lugar de \(Q^\pi(s,a)\). Esa estrategia codiciosa de una etapa puede agotar recursos o desplazar costos al futuro. Otro error es usar valores aproximados como si garantizaran mejora exacta; con error de aproximación, una diferencia pequeña entre acciones puede no ser significativa.

### 8.3.3. Iteración de políticas

La iteración de políticas alterna evaluación y mejora hasta que la política no cambia.

```text
inicializar una política factible pi
REPETIR
    evaluar pi para obtener V_pi
    estable <- verdadero
    PARA CADA estado s
        acción_anterior <- pi(s)
        pi(s) <- una acción factible que maximice
                 la recompensa esperada más el valor futuro descontado
        SI pi(s) difiere de acción_anterior
            estable <- falso
HASTA QUE estable
DEVOLVER pi y V_pi
```

En un MDP finito descontado hay un número finito de políticas deterministas estacionarias. Cada mejora estricta produce una política mejor; por ello el procedimiento termina en una política óptima, suponiendo evaluación exacta y tratamiento consistente de empates.

La **iteración de políticas modificada** no evalúa cada política hasta convergencia. Ejecuta pocos barridos y vuelve a mejorar. Así interpola entre iteración de políticas e iteración de valores. Puede reducir trabajo cuando una evaluación muy precisa es innecesaria en etapas tempranas.

El costo por iteración de una evaluación exacta puede ser alto, pero el número de cambios de política suele ser pequeño en muchos problemas. No existe una superioridad universal frente a iteración de valores. Importan la dispersión de transiciones, la facilidad de resolver sistemas, el descuento y la precisión requerida.

Una política estable dentro del modelo no implica estabilidad operacional. Si pequeñas variaciones de costos cambian muchas acciones, la recomendación es frágil. Debe repetirse el cálculo sobre escenarios plausibles y reportar estados donde la acción depende de supuestos inciertos.

### 8.3.4. Iteración de valores

La iteración de valores aplica directamente el operador óptimo:

\[
V_{k+1}(s)=\max_a\sum_{s'}P(s'\mid s,a)
[r(s,a,s')+\gamma V_k(s')].
\]

```text
inicializar V(s) arbitrariamente para estados no terminales
REPETIR
    cambio_máximo <- 0
    PARA CADA estado s
        anterior <- V(s)
        V(s) <- máximo, sobre acciones factibles, de
                recompensa esperada más valor futuro descontado
        actualizar cambio_máximo con |anterior - V(s)|
HASTA QUE se satisfaga el criterio de parada
PARA CADA estado s
    pi(s) <- una acción codiciosa respecto de V
DEVOLVER pi y V
```

Puede interpretarse como evaluación truncada y mejora en cada barrido. Si \(V_0=0\), las primeras iteraciones incorporan consecuencias progresivamente más lejanas, aunque con descuento y ciclos la interpretación exacta requiere cuidado.

La política debe extraerse usando un barrido codicioso coherente con el valor final. Detenerse porque la política no cambia puede ser suficiente para la decisión, aun si los valores continúan ajustándose. A la inversa, un residuo pequeño no garantiza que acciones casi empatadas sean robustas frente a error del modelo.

Para estados terminales se fija normalmente \(V=0\) después de incorporar la recompensa de entrada. Contar además una recompensa terminal en cada permanencia dentro del estado absorbente duplica beneficios o costos. La convención temporal debe declararse.

La iteración de valores requiere conocer las transiciones de todas las acciones. No es aprendizaje por refuerzo libre de modelos. Puede usarse sobre un modelo estimado, pero entonces su exactitud numérica no elimina el error de estimación.

### 8.3.5. Convergencia y costo computacional

En MDP finitos con \(\gamma<1\), la contracción de Bellman garantiza

\[
\|V_k-V^*\|_\infty\leq\gamma^k\|V_0-V^*\|_\infty.
\]

Si las recompensas están acotadas por \(|R|\leq R_{max}\) y \(V_0=0\), entonces \(\|V^*\|_\infty\leq R_{max}/(1-\gamma)\). Cuando \(\gamma\) se aproxima a uno, la cota empeora y se necesitan más iteraciones.

Para una representación densa, un barrido de Bellman cuesta aproximadamente \(O(|\mathcal{S}|^2|\mathcal{A}|)\), porque cada par estado-acción suma sobre todos los sucesores. Si cada par tiene a lo sumo \(d\) sucesores, el costo baja a \(O(|\mathcal{S}||\mathcal{A}|d)\). Almacenar transiciones densas requiere \(O(|\mathcal{S}|^2|\mathcal{A}|)\). La estructura dispersa es decisiva.

La “maldición de la dimensionalidad” surge cuando el estado combina variables. Diez variables con diez niveles producen \(10^{10}\) estados. Discretizar más finamente aumenta fidelidad local, pero hace inviable enumerar y reduce datos por celda. La aproximación de funciones aborda parte del problema, a costa de perder garantías tabulares simples y de introducir generalización potencialmente errónea.

Convergencia numérica no es validez. Un algoritmo puede converger exactamente a la política óptima de un modelo equivocado. Deben distinguirse al menos cuatro fuentes de error: especificación de objetivo, representación del estado, estimación de \(P\) y \(R\), y aproximación computacional. La última suele ser la más fácil de medir y no necesariamente la más importante.

Otras limitaciones son memoria, comunicación en sistemas distribuidos, latencia de decisión y cambios del entorno. La política óptima calculada fuera de línea puede quedar obsoleta. La revisión periódica debe basarse en indicadores de cambio y no solo en un calendario.

### 8.3.6. Ejemplo práctico guiado: selección de una política operativa

Una empresa debe fijar una regla operativa para cargar su flota eléctrica. Al inicio de cada franja horaria, el estado agregado es bajo \(B\) si pocos vehículos tienen autonomía suficiente para los próximos servicios, y suficiente \(S\) en caso contrario. Las acciones son cargar \(C\) o esperar \(E\). Para concentrar el análisis en la resolución, se usan las transiciones y recompensas de la sección 8.2.8: la penalización de \(-8\) representa indisponibilidad esperada y los valores \(-4\) y \(-3\) representan electricidad.

Se aplica iteración de valores con \(\gamma=0{,}9\) y \(V_0(B)=V_0(S)=0\). En el primer barrido solo influyen las recompensas inmediatas:

\[
V_1(B)=\max\{-8,-4\}=-4,
\qquad V_1(S)=\max\{0,-3\}=0.
\]

En el segundo barrido ya se incorpora el efecto sobre la franja siguiente:

\[
V_2(B)=\max\{-8+0{,}9[0{,}8(-4)+0{,}2(0)],
-4+0{,}9[0{,}2(-4)+0{,}8(0)]\}
=-4{,}72,
\]

\[
V_2(S)=\max\{0+0{,}9[0{,}3(-4)+0{,}7(0)],
-3+0{,}9[0{,}1(-4)+0{,}9(0)]\}
=-1{,}08.
\]

Las acciones codiciosas son cargar en \(B\) y esperar en \(S\). Los valores continúan bajando a medida que se incorporan costos futuros y convergen aproximadamente a \(V^*(B)=-28{,}92\) y \(V^*(S)=-21{,}10\). La política seleccionada es, por tanto,

\[
\pi^*(B)=C,
\qquad \pi^*(S)=E.
\]

La evaluación tiene una interpretación operativa: cuando la autonomía agregada es baja, pagar electricidad evita una probabilidad alta de indisponibilidad; cuando es suficiente, la carga adicional no justifica su costo. Los valores no son el costo de una única franja, sino el retorno descontado de ejecutar la regla repetidamente.

Conviene comprobar si la política es sensible al precio de cargar en \(S\). Sea \(c\) ese costo. Manteniendo por el momento el futuro de la política calculada,

\[
Q(S,C)=-c+0{,}9[0{,}1V(B)+0{,}9V(S)].
\]

El punto de indiferencia frente a esperar satisface

\[
-c+0{,}9[0{,}1(-28{,}92)+0{,}9(-21{,}10)]=-21{,}10,
\]

de donde \(c\approx1{,}40\). Con costo 3 se espera; si una tarifa reducida llevara el costo por debajo de aproximadamente 1,40, cargar en \(S\) podría ser preferible. Este cálculo identifica una frontera local: si la acción cambia de forma permanente, hay que resolver otra vez las ecuaciones porque también cambia el valor futuro.

La sensibilidad debe extenderse a la penalización por vehículos no disponibles y a las probabilidades estimadas. Si pequeñas variaciones alteran la acción, la recomendación es frágil y requiere mejor estimación o una regla conservadora. La entrega técnica debe declarar franja temporal, criterio de parada, valores residuales y acciones casi empatadas. Antes del despliegue se prueban picos de demanda, errores del estado de carga, límites de potencia, degradación y vehículos fuera de servicio; cualquier acción físicamente inadmisible se elimina del conjunto factible antes de volver a resolver el MDP.

## 8.4. Aprendizaje por refuerzo

El aprendizaje por refuerzo (RL) estudia agentes que aprenden a actuar a partir de interacción y recompensas. A diferencia del aprendizaje supervisado, no recibe para cada estado una etiqueta con la acción correcta. Las acciones influyen en datos futuros, las recompensas pueden demorarse y explorar una opción modifica tanto el conocimiento como el desempeño.

El bucle básico es: el agente observa \(S_t\), elige \(A_t\), el entorno produce \(R_{t+1}\) y \(S_{t+1}\), y el agente actualiza su conocimiento. El problema formal puede ser un MDP, pero los algoritmos difieren en si conocen el modelo, esperan al final del episodio, aprenden sobre la conducta ejecutada o sobre una política objetivo distinta.

### 8.4.1. Aprendizaje basado en modelos y libre de modelos

Un método **basado en modelos** dispone de, estima o aprende \(P(s'\mid s,a)\) y \(r(s,a,s')\). Luego planifica con ese modelo, por ejemplo mediante iteración de valores. También puede combinar experiencia real con transiciones simuladas. Su ventaja es reutilizar cada observación para considerar varias políticas y anticipar resultados; su riesgo es explotar errores del modelo.

Un método **libre de modelos** aprende valores o políticas sin construir explícitamente toda la dinámica. Q-learning estima \(Q^*\); SARSA estima el valor de la política de conducta mientras esta evoluciona. “Libre de modelos” no significa libre de supuestos: sigue suponiendo estados adecuados, recompensa representativa, cierta estabilidad y experiencia suficiente.

Otra distinción es entre métodos **basados en valor**, que derivan la política de valores; **basados en política**, que optimizan parámetros de la política directamente; y actor-crítico, que combina un actor con un estimador de valor. Este capítulo desarrolla los primeros en espacios discretos.

| Enfoque | Qué aprende | Uso de experiencia | Riesgo característico |
|---|---|---|---|
| Modelo conocido + planificación | valores/política | expectativas del modelo | modelo mal especificado |
| Modelo aprendido + planificación | dinámica y política | datos reales y simulación | sesgo acumulado al simular |
| Libre de modelos | valores o política | transiciones observadas | baja eficiencia muestral |

La elección depende del costo de interacción. Si existe un simulador físico fiable, un enfoque basado en modelos puede ser eficiente. Si las dinámicas son difíciles pero se dispone de abundante interacción segura, uno libre de modelos puede ser práctico. En sistemas críticos, aprender directamente en operación suele ser inaceptable; se combinan datos históricos, simulación, límites y validación humana.

### 8.4.2. Exploración frente a explotación

**Explotar** es elegir la acción con mayor valor estimado; **explorar** es probar acciones para reducir incertidumbre o descubrir mejores resultados. Explotación prematura consolida una estimación posiblemente errónea. Exploración excesiva incurre en costo y puede impedir un desempeño estable.

Una regla \(\varepsilon\)-codiciosa elige una acción codiciosa con probabilidad \(1-\varepsilon\) y una acción al azar con probabilidad \(\varepsilon\). Si la selección aleatoria incluye la acción codiciosa, su probabilidad total es \(1-\varepsilon+\varepsilon/|\mathcal{A}(s)|\). Reducir \(\varepsilon\) con el tiempo favorece explotación; reducirlo demasiado rápido puede dejar acciones sin aprender.

Otras estrategias asignan probabilidades suaves según valores, añaden bonos por incertidumbre o mantienen intervalos de confianza. La exploración dirigida es más eficiente que el azar cuando se puede cuantificar incertidumbre. En cualquier caso, “probar todo” no es una obligación moral ni técnica: las acciones inseguras deben excluirse.

Para convergencia tabular de muchos métodos se requiere que cada par estado-acción relevante se visite repetidamente y que las tasas de aprendizaje disminuyan de forma apropiada. Esta condición asintótica rara vez se cumple literalmente en una operación finita y cambiante. Por eso, la cobertura debe medirse: conteos de visitas, distribución de estados y desempeño por regiones.

Existe además aprendizaje fuera de línea, que intenta aprender de un conjunto fijo. Allí no se puede explorar y aparece el problema de extrapolación: valorar acciones escasamente representadas requiere inferencias frágiles. Una política nueva puede elegir precisamente esas acciones porque sus errores estimados parecen favorables. Se necesitan métodos conservadores y evaluación fuera de política.

**Error frecuente.** Evaluar una política exploratoria por su recompensa de entrenamiento sin separar el costo de explorar ni medir una política final. La conducta usada para aprender y la política destinada a operar pueden ser distintas.

### 8.4.3. Métodos Monte Carlo

Los métodos Monte Carlo aprenden de episodios completos sin modelo. Para una visita al par \((s,a)\) en el tiempo \(t\), calculan el retorno observado

\[
G_t=R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{T-t-1}R_T
\]

y actualizan una media o una estimación incremental:

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha[G_t-Q(S_t,A_t)].
\]

En Monte Carlo de **primera visita** se usa solo la primera aparición de un estado o par en el episodio; en **cada visita** se usan todas. Ambos convergen bajo condiciones estándar, aunque sus muestras están correlacionadas dentro del episodio.

```text
inicializar Q y una política exploratoria
PARA CADA episodio
    generar un episodio siguiendo la política
    calcular hacia atrás el retorno de cada instante
    PARA CADA visita seleccionada de un par estado-acción
        acercar Q(estado, acción) al retorno observado
    mejorar la política para favorecer acciones con Q mayor,
    conservando exploración suficiente
DEVOLVER política y Q
```

Monte Carlo no introduce sesgo de arranque porque usa retornos reales completos, pero puede tener varianza alta. Además, debe esperar al final y se adapta naturalmente a tareas episódicas. En episodios muy largos o sin terminación, el método básico es poco práctico.

La cobertura puede obtenerse mediante “inicios exploratorios”, que suponen poder comenzar en cualquier par estado-acción, o mediante políticas blandas que asignan probabilidad positiva a las acciones. El primer supuesto rara vez es realista en sistemas físicos.

Una recompensa final ruidosa atribuye el mismo retorno general a muchas decisiones, lo que dificulta identificar mérito. Promediar reduce varianza con más episodios, pero no corrige confusión por estados omitidos ni sesgo de datos recolectados bajo otra política.

### 8.4.4. Aprendizaje por diferencias temporales

El aprendizaje por diferencias temporales (TD) combina muestreo de experiencia con **arranque**: actualiza una estimación usando otra estimación antes de terminar el episodio. TD(0) para evaluar una política usa

\[
V(S_t)\leftarrow V(S_t)+\alpha\delta_t,
\]

\[
\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t).
\]

\(\delta_t\) es el error TD. Si el estado siguiente es terminal, su valor se toma como cero. La actualización ocurre tras cada transición, por lo que TD sirve en tareas continuas y aprende en línea.

Monte Carlo apunta a \(G_t\), una muestra completa generalmente no sesgada del retorno bajo la política; TD(0) apunta a \(R_{t+1}+\gamma V(S_{t+1})\), que depende de una estimación y puede ser sesgada. A cambio, suele tener menor varianza y propaga información sin esperar.

Los retornos de \(n\) pasos intermedian entre ambos:

\[
G_t^{(n)}=R_{t+1}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^nV(S_{t+n}).
\]

Las trazas de elegibilidad TD(\(\lambda\)) mezclan escalas temporales y asignan crédito a estados recientes. Un \(\lambda\) cercano a cero se parece a TD(0); cercano a uno se aproxima a Monte Carlo bajo ciertas condiciones.

La tasa \(\alpha\) controla cuánto pesa la observación nueva. Una tasa constante permite adaptarse a cambios, pero mantiene variabilidad; una secuencia decreciente facilita convergencia en entornos estacionarios. Una tasa grande junto con aproximación de funciones puede causar oscilaciones o divergencia.

El error TD es una señal de aprendizaje, no necesariamente una anomalía ni una medida directa de calidad de la política. Puede ser alto por recompensa aleatoria, transición rara o estimación deficiente. Su análisis requiere contexto.

### 8.4.5. Q-learning

Q-learning es un método TD de control libre de modelos y fuera de política. Actualiza

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha
\left[R_{t+1}+\gamma\max_{a'}Q(S_{t+1},a')-Q(S_t,A_t)\right].
\]

La política de conducta puede ser \(\varepsilon\)-codiciosa, pero el objetivo usa la mejor acción estimada en el siguiente estado. Por ello aprende sobre una política codiciosa mientras ejecuta otra exploratoria.

```text
inicializar Q para todos los pares factibles
PARA CADA episodio
    observar estado inicial s
    MIENTRAS s no sea terminal
        elegir a con una política de conducta exploratoria derivada de Q
        ejecutar a y observar recompensa r y siguiente estado s_nuevo
        objetivo <- r si s_nuevo es terminal;
                    en otro caso, r + descuento * máximo Q(s_nuevo, acción)
        Q(s,a) <- Q(s,a) + tasa * (objetivo - Q(s,a))
        s <- s_nuevo
DEVOLVER una política codiciosa respecto de Q
```

En el caso tabular, con recompensas acotadas, visitas suficientes y tasas que cumplen condiciones de aproximación estocástica, Q-learning converge a \(Q^*\). Estas garantías no se trasladan automáticamente a redes neuronales, datos finitos o entornos no estacionarios.

El operador máximo produce sesgo de sobreestimación: entre estimaciones ruidosas tiende a seleccionar errores positivos. Variantes de doble estimación reducen ese efecto separando selección y evaluación. La inicialización optimista puede estimular exploración tabular, pero es ineficaz si estados no se revisitan o si la escala está mal elegida.

Q-learning puede aprender una política que atraviesa estados peligrosos durante entrenamiento porque su objetivo es codicioso, aunque la conducta explore. La seguridad debe imponerse a la conducta real, no confiarse al valor objetivo futuro.

### 8.4.6. SARSA

SARSA recibe su nombre de la secuencia \((S_t,A_t,R_{t+1},S_{t+1},A_{t+1})\). Su actualización es

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha
[R_{t+1}+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t)].
\]

Es un método **en política**: la acción siguiente usada en el objetivo procede de la misma política de conducta. Si esta es \(\varepsilon\)-codiciosa, SARSA valora también las consecuencias de sus errores exploratorios. Q-learning, en cambio, valora la continuación codiciosa.

```text
inicializar Q
PARA CADA episodio
    observar s y elegir a según la política exploratoria
    MIENTRAS s no sea terminal
        ejecutar a; observar r y s_nuevo
        SI s_nuevo no es terminal
            elegir a_nueva según la misma política exploratoria
            objetivo <- r + descuento * Q(s_nuevo, a_nueva)
        EN OTRO CASO
            objetivo <- r
        actualizar Q(s,a) hacia objetivo
        s <- s_nuevo; a <- a_nueva
DEVOLVER la política deseada derivada de Q
```

En una tarea con un camino corto junto a una zona de gran penalización, Q-learning puede preferir el borde porque supone acciones futuras codiciosas; una conducta exploratoria, sin embargo, puede desviarse y caer. SARSA suele aprender una ruta más alejada mientras \(\varepsilon>0\), porque incorpora ese riesgo. No significa que SARSA sea siempre “más seguro”: si la política de conducta permite acciones catastróficas, también las ejecutará para aprender.

Si \(\varepsilon\) disminuye hasta cero con exploración suficiente, ambos pueden converger a una política óptima en condiciones tabulares. Con \(\varepsilon\) persistente, SARSA optimiza el desempeño de esa política blanda, mientras Q-learning apunta a la codiciosa. La comparación experimental debe declarar tanto política de entrenamiento como de evaluación.

### 8.4.7. Diseño de recompensas

Diseñar recompensas es especificar qué comportamiento se incentiva. Una señal incompleta puede producir **manipulación de la recompensa**: el agente encuentra un atajo que aumenta el indicador sin cumplir la intención. Si se recompensa solo el nivel alto de un depósito, podría bombear continuamente, desperdiciar energía o superar presiones seguras.

Un proceso disciplinado comienza con resultados deseados, daños inaceptables y actores afectados; después identifica medidas observables y comprueba cómo podrían ser explotadas. Conviene separar:

| Elemento | Ejemplo | Tratamiento posible |
|---|---|---|
| Objetivo | continuidad del servicio | retorno acumulado |
| Costo operativo | energía y desgaste | término de recompensa |
| Restricción dura | presión máxima | filtro de acciones |
| Indicador sustituto | nivel del depósito | señal auxiliar auditada |
| Preferencia distributiva | evitar barrios desatendidos | criterio explícito por grupos |

El moldeado potencial añade

\[
F(s,a,s')=\gamma\Phi(s')-\Phi(s)
\]

a la recompensa. Bajo condiciones conocidas, acelera el aprendizaje sin cambiar las políticas óptimas. Bonificaciones arbitrarias no ofrecen esa garantía y pueden redefinir la tarea.

Las escalas relativas importan. Una penalización de seguridad “grande” puede no serlo frente a miles de recompensas pequeñas acumuladas. Se deben calcular retornos máximos plausibles y probar escenarios adversariales. También hay que evitar recompensar acciones en vez de resultados si eso induce actividad innecesaria.

Las preferencias cambian y son objeto de gobernanza. Versionar la recompensa, documentar responsables y conservar evaluaciones por componente permite saber por qué cambió una política. Una recompensa única no resuelve desacuerdos éticos. En decisiones públicas, eficiencia, equidad y derechos requieren deliberación, restricciones y rendición de cuentas.

**Error frecuente.** Ajustar recompensas hasta que una demostración se vea razonable y declarar éxito. Ese procedimiento sobreajusta escenarios conocidos. La evaluación debe incluir casos no usados en el diseño, perturbaciones y búsqueda deliberada de atajos.

### 8.4.8. Seguridad, estabilidad y límites de aplicación

Un agente puede causar daño durante entrenamiento, al desplegarse o cuando el entorno cambia. La seguridad no se reduce a una recompensa promedio alta. Debe medir violaciones, colas de pérdida, peor caso plausible, recuperación y efectos sobre grupos vulnerables.

Entre las salvaguardas se encuentran: restringir acciones; usar un supervisor que sustituya decisiones inseguras; entrenar primero en simulación; limitar velocidad de cambio; desplegar gradualmente; detectar estados fuera de distribución; permitir abstención; mantener anulación humana; registrar transiciones; y definir retorno a una política segura. Cada mecanismo necesita pruebas independientes.

La estabilidad tiene varias dimensiones. El aprendizaje puede oscilar por tasas altas, objetivos móviles o aproximación de funciones. La política puede ser sensible a pequeñas variaciones de observación. El entorno puede reaccionar estratégicamente o cambiar por estacionalidad. Un promedio estable no descarta alternancia perjudicial de acciones, como encendidos y apagados que aceleran desgaste.

La llamada tríada mortal combina aproximación de funciones, arranque y aprendizaje fuera de política; su interacción puede producir divergencia. Incluso cuando la pérdida de entrenamiento disminuye, los valores pueden estar mal calibrados. Las garantías tabulares no deben citarse para justificar sistemas complejos sin verificar sus condiciones.

RL no es apropiado cuando no hay decisiones secuenciales significativas, cuando una regla simple resuelve el problema, cuando la interacción es escasa o no ética, cuando no puede medirse el objetivo, o cuando la organización carece de capacidad para monitorear. Predicción más optimización restringida, control clásico, investigación operativa o supervisión humana pueden ser mejores alternativas.

Persisten limitaciones de causalidad, observabilidad, transferencia de simulación a realidad, eficiencia muestral, reproducibilidad y explicabilidad. Además, una política aprende dentro de instituciones: puede desplazar trabajo, concentrar riesgos y modificar incentivos. La aprobación debe considerar responsabilidad legal, participación de afectados y mecanismos de apelación.

Una lista mínima antes del despliegue pregunta: ¿qué acciones nunca debe realizar?, ¿cómo se detecta una observación inválida?, ¿qué política actúa si falla el agente?, ¿quién puede detenerlo?, ¿qué datos permiten auditar una decisión?, ¿qué cambio activa reentrenamiento o retirada? Si estas respuestas no existen, mejorar la recompensa media no convierte el sistema en aceptable.

### 8.4.9. Ejemplo práctico guiado: entrenamiento de un agente en un entorno discreto

Considérese una cuadrícula de \(4\times4\). El agente comienza en la esquina inferior izquierda y debe llegar a una estación de control en la superior derecha. Cada movimiento cuesta \(-1\), llegar aporta \(+20\), entrar en una celda de riesgo aporta \(-15\) y termina el episodio. Las acciones son norte, sur, este y oeste; chocar con un borde deja al agente en el mismo estado. Una franja de riesgo hace que el camino más corto pase cerca de consecuencias graves.

El experimento conceptual compara Q-learning y SARSA con igual inicialización, tasa, descuento y regla \(\varepsilon\)-codiciosa. La unidad experimental no es un episodio aislado, sino una ejecución completa con semilla independiente. Se separan entrenamiento y evaluación: durante evaluación se fija una política codiciosa, sin actualizaciones, y se prueban también perturbaciones.

**Protocolo**

1. Definir estados, acciones factibles, terminales, recompensas y convención temporal.
2. Fijar \(\gamma=0{,}95\), una tasa inicial y un calendario de exploración declarado.
3. Entrenar ambos métodos durante el mismo presupuesto de transiciones, no solo igual número de episodios.
4. Repetir con múltiples semillas y conservar curvas individuales.
5. Evaluar retorno, tasa de llegada, longitud de ruta, entradas en riesgo y peor retorno.
6. Inspeccionar la política en cada celda y no solo la recompensa acumulada.
7. Repetir con ruido de actuación: con probabilidad 0,05 se ejecuta un movimiento lateral.

Se espera que Q-learning tienda al camino nominal más corto junto al riesgo porque su objetivo presupone futuras acciones codiciosas. SARSA, mientras explora, puede valorar el peligro de desviación y aprender una ruta más separada. Con exploración reducida a cero y suficientes visitas, las políticas pueden acercarse. Bajo ruido permanente, la ruta prudente puede seguir teniendo mejor desempeño real.

| Métrica | Pregunta que responde | Insuficiencia si se usa sola |
|---|---|---|
| Retorno medio | ¿qué utilidad promedio obtiene? | oculta colas y fallas |
| Tasa de éxito | ¿con qué frecuencia llega? | ignora costo y longitud |
| Entradas en riesgo | ¿viola seguridad? | no mide eficiencia |
| Cuantil 5 % | ¿cómo son casos desfavorables? | no explica su causa |
| Pasos por episodio | ¿qué tan directa es la ruta? | favorece atajos peligrosos |

No debe inferirse convergencia porque una media móvil se aplana. Se revisan cambios de política, dispersión entre semillas y cobertura de pares estado-acción. Tampoco es válido seleccionar la mejor semilla. Si una acción riesgosa es inaceptable, se elimina mediante una restricción en lugar de permitir que el agente la pruebe para descubrir su penalización.

El ejemplo evidencia una tensión esencial: el algoritmo aprende exactamente de la experiencia y del objetivo que se le proporcionan. Una cuadrícula es útil para entender actualizaciones, pero no demuestra seguridad en redes físicas, donde estados son continuos, observaciones fallan y las acciones tienen inercia. La progresión responsable va de pruebas unitarias del entorno a simulación adversarial, evaluación fuera de muestra, piloto supervisado y despliegue reversible.

## Síntesis del capítulo

La teoría de decisión separa lo controlable de lo incierto y conecta creencias con preferencias. Las probabilidades describen estados; la utilidad valora consecuencias. La utilidad esperada permite comparar loterías, la curvatura representa actitudes frente al riesgo y los árboles ordenan decisiones e información. El valor de información mide cuánto mejora una decisión por observar antes de actuar, no cuánto resulta interesante un dato.

Los MDP extienden esa lógica a secuencias. Un estado resume la historia relevante; las transiciones describen dinámica; las recompensas formalizan el objetivo; una política prescribe acciones; y horizonte y descuento determinan cómo se acumula el futuro. Las funciones de valor condensan consecuencias de largo plazo y Bellman expresa su recursión.

Con modelo conocido, evaluación, mejora, iteración de políticas e iteración de valores permiten planificar. Sus garantías dependen de finitud, descuento, exactitud y representación. Con modelo desconocido, Monte Carlo aprende de retornos completos y TD aprende por arranque. Q-learning es fuera de política; SARSA es en política. Ningún algoritmo repara un estado insuficiente o una recompensa mal diseñada.

El aprendizaje por refuerzo introduce una tensión inevitable entre conocer y rendir. Explorar tiene costo y puede ser peligroso. Por ello, seguridad, restricciones, evaluación por escenarios y gobernanza no son complementos posteriores, sino parte de la formulación. La solución técnicamente óptima es siempre óptima respecto de un modelo y un objetivo declarados; la responsabilidad profesional consiste en examinar ambos y reconocer lo que queda fuera.

## Errores de razonamiento que deben evitarse

| Error | Por qué falla | Corrección |
|---|---|---|
| Elegir por el estado más probable | ignora magnitud de consecuencias | calcular utilidad sobre todos los estados |
| Tratar costo esperado como costo seguro | borra dispersión y extremos | reportar distribución, colas y restricciones |
| Confundir sensibilidad con posterior | invierte condicionamiento | aplicar Bayes con prevalencia |
| Considerar una observación como estado | puede faltar memoria relevante | probar suficiencia y ampliar representación |
| Optimizar recompensa inmediata | desplaza costos al futuro | usar retorno y valor |
| Descontar dos veces | altera la escala temporal | fijar una convención de retorno |
| Declarar válido porque convergió | solo prueba estabilidad numérica | validar modelo, objetivo y datos |
| Llamar “sin supuestos” a un método libre de modelos | aún depende de estado y entorno | explicitar hipótesis y cobertura |
| Explorar acciones prohibidas | aprender su peligro ya causa daño | restringir y supervisar acciones |
| Evaluar con episodios de entrenamiento | mezcla exploración y selección | usar protocolo de evaluación separado |

## Glosario esencial

**Acción o alternativa.** Intervención que el decisor puede elegir.

**Actitud frente al riesgo.** Forma en que la utilidad valora dispersión alrededor de una consecuencia esperada.

**Arranque (*bootstrapping*).** Actualización de una estimación a partir de otra estimación, como en TD.

**Consecuencia.** Resultado relevante producido por una acción bajo un estado.

**Descuento.** Peso \(\gamma\) aplicado progresivamente a recompensas futuras.

**Entorno.** Sistema que recibe acciones y produce estados y recompensas.

**Estado.** Resumen de información suficiente para predecir y decidir bajo el modelo.

**Estado terminal.** Estado que finaliza un episodio.

**Explotación.** Elección de acciones estimadas como mejores.

**Exploración.** Elección orientada a obtener información sobre acciones o estados.

**Función de valor.** Retorno esperado desde un estado, o desde un par estado-acción, bajo una política.

**Horizonte.** Cantidad de etapas consideradas o naturaleza continua del proceso.

**MDP.** Modelo de decisión secuencial con estados, acciones, transiciones, recompensas y criterio temporal.

**Política.** Regla determinista o probabilística que asigna acciones a estados.

**Propiedad de Markov.** Independencia del futuro respecto de la historia una vez conocidos estado y acción actuales.

**Recompensa.** Señal numérica inmediata que contribuye al retorno.

**Retorno.** Suma, posiblemente descontada, de recompensas futuras.

**Transición.** Distribución del próximo estado condicionada al estado y acción actuales.

**Utilidad.** Representación numérica de preferencias coherentes.

**Valor de información.** Mejora esperada de la decisión posibilitada por observar información antes de actuar.

## Autoevaluación

1. ¿Por qué “fuga” es un estado y “costo de esperar ante una fuga” es una consecuencia?
2. ¿Qué supuestos permiten representar preferencias mediante utilidad esperada?
3. Calcule el umbral de probabilidad que iguala dos alternativas con costos \((20,8)\) y \((60,2)\) en los estados adverso y normal.
4. Explique la diferencia entre aversión al riesgo y asignar alta probabilidad a un daño.
5. ¿Por qué el valor de una prueba puede ser cero aunque sea exacta?
6. Formule el VEIP en términos de minimización de costos e interprete cada término.
7. ¿Qué información histórica debería incorporarse al estado de una bomba cuyo riesgo depende de horas acumuladas de uso?
8. Distinga propiedad de Markov de estacionariedad.
9. ¿Por qué una recompensa no es necesariamente el objetivo real?
10. Compare política abierta, política de realimentación y política estocástica.
11. ¿Cómo cambia el horizonte efectivo cuando \(\gamma\) pasa de 0,9 a 0,99?
12. Derive la ecuación de Bellman para \(Q^\pi\) a partir de la definición de retorno.
13. ¿Qué diferencia hay entre evaluación y mejora de una política?
14. ¿Por qué la iteración de valores no es un método libre de modelos?
15. Enumere las cuatro fuentes de error distinguidas en la sección de convergencia.
16. Compare el blanco de actualización de Monte Carlo con el de TD(0).
17. ¿En qué sentido Q-learning es fuera de política y SARSA es en política?
18. ¿Por qué una curva de recompensa estable no demuestra convergencia segura?
19. Proponga un atajo no deseado para una recompensa basada solo en cantidad de agua bombeada.
20. Mencione tres situaciones en las que no usaría aprendizaje por refuerzo.

## Actividad integradora de cierre

**Situación.** Una organización administra dos bombas que abastecen un depósito. La demanda tiene niveles bajo, medio y alto; el precio de energía varía; una bomba presenta desgaste; y una inspección puede revelar con error si requiere mantenimiento. La organización desea evitar interrupciones, controlar energía y no superar límites de presión.

**Producto.** Elaborar un informe técnico reproducible, sin implementar todavía un agente, que conecte una decisión de inspección con una política secuencial.

1. Definir alternativas iniciales, estados de naturaleza y consecuencias multiatributo de inspeccionar, mantener o esperar.
2. Proponer probabilidades previas y desempeño de la inspección, justificando su origen.
3. Construir el árbol de decisión, calcular posteriores, utilidad esperada, VEIP y VEIM, y realizar sensibilidad sobre dos parámetros.
4. Formular un MDP posterior a la decisión inicial: estado, acciones factibles, transiciones, recompensas, horizonte, descuento y distribución inicial.
5. Justificar por qué el estado propuesto es aproximadamente markoviano e identificar variables ocultas.
6. Escribir las ecuaciones de Bellman de una política base para al menos dos estados.
7. Ejecutar manualmente dos barridos de iteración de valores sobre un subconjunto pequeño y extraer acciones codiciosas.
8. Diseñar un protocolo conceptual para comparar Q-learning y SARSA, incluyendo exploración, presupuesto y múltiples semillas.
9. Separar objetivo, indicadores sustitutos y restricciones duras; proponer dos posibles fallas de especificación de recompensa.
10. Definir métricas de desempeño, seguridad, equidad y estabilidad, además de criterios de suspensión.

**Criterios de evaluación.** La representación distingue creencias de preferencias; los cálculos respetan condicionamiento y cronología; el MDP es internamente coherente; las recompensas no sustituyen restricciones críticas; la comparación experimental separa entrenamiento de evaluación; y las conclusiones declaran sensibilidad, límites y condiciones de despliegue. Se valorará más una formulación pequeña y auditable que un modelo extenso cuyos parámetros no puedan justificarse.
