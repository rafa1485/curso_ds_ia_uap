# Capitulo 7. Busqueda y resolucion algoritmica

## 7.1. Espacios de estados y procesos de busqueda

Un grafo `G=(V,E)` representa estados y transiciones. Un nodo contiene estado, padre, accion, costo y profundidad. La frontera contiene candidatos y el conjunto explorado evita repetir estados. Tiempo y memoria dependen del factor de ramificacion, profundidad y estructura del grafo.

### 7.1.7. Ejemplo practico guiado

Representar una red vial: vertices como zonas, aristas como desplazamientos y costo como tiempo o consumo. Las aristas deben respetar la direccion y disponibilidad reales.

## 7.2. Busqueda no informada

Anchura usa cola y es completa y optima con costos unitarios. Profundidad usa pila, consume menos memoria y puede no terminar. Costo uniforme expande el menor `g(n)` y es optimo con costos no negativos. Profundizacion iterativa combina memoria de profundidad con completitud bajo supuestos usuales.

### 7.2.8. Ejemplo practico guiado

Resolver el mismo grafo con anchura, profundidad y costo uniforme; comparar camino, costo, nodos expandidos y memoria.

## 7.3. Busqueda informada y heuristicas

Una heuristica `h(n)` estima costo restante. A* ordena por `f(n)=g(n)+h(n)`. Es optimo si la heuristica es admisible (`h(n)<=h*(n)`) y, en grafos, consistente (`h(n)<=c(n,n')+h(n')`). La heuristica debe usar solo informacion permitida.

### 7.3.7. Ejemplo practico guiado

Comparar distancia geografica con costo real de viaje y cuantificar nodos explorados.

### Actividad EMO [MOV-02]

Construir grafo simplificado, comparar costo uniforme y A*, justificar costos y evaluar admisibilidad, calidad de solucion y computo.

## 7.4. Busqueda local y restricciones

Ascenso de colinas mejora un vecino, pero puede quedar en maximos locales, mesetas o crestas. Recocido simulado acepta ocasionalmente empeoramientos con probabilidad `exp(-Delta/T)`. Un problema de satisfaccion de restricciones define variables, dominios y restricciones; la consistencia de dominios reduce busqueda.

### 7.4.7. Ejemplo practico guiado

Optimizar una ruta de inspeccion bajo tiempo, prioridades y recursos; comparar calidad, reinicios y factibilidad.

## Sintesis

Buscar es explorar representaciones con una estrategia y una garantia. La optimalidad debe declararse junto con supuestos sobre costos, heuristica y terminacion.
