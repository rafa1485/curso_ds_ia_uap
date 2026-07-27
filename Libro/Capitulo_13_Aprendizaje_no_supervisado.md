# Capitulo 13. Aprendizaje no supervisado y descubrimiento de estructuras

## 13.1. Distancias, similitudes y representacion

Euclidea `d(x,z)=sqrt(sum(x_j-z_j)^2)` depende de escala; Manhattan suma diferencias absolutas; coseno compara orientacion. En datos mixtos deben definirse codificaciones y pesos. La distancia es una hipotesis sobre semejanza.

### 13.1.7. Ejemplo practico guiado

Comparar vecinos antes y despues de escalar variables, y explicar que cambios representan una decision de modelado.

## 13.2. Agrupamiento particional y jerarquico

K-means minimiza `sum_i ||x_i-mu_{c_i}||^2` alternando asignacion y centroides; su resultado depende de inicializacion y supone grupos aproximadamente convexos. El agrupamiento jerarquico construye un dendrograma usando enlaces simple, completo, promedio o Ward.

### 13.2.8. Ejemplo practico guiado

Segmentar consumo, comparar K-means y jerarquico, caracterizar grupos sin convertirlos automaticamente en categorias reales.

## 13.3. Densidad y representaciones neuronales

DBSCAN define vecindad por `epsilon` y minimo de puntos; identifica densidad, ruido y formas no convexas. Sus resultados son sensibles a escala y parametros. Los mapas autoorganizados proyectan prototipos preservando vecindades aproximadas.

### 13.3.7. Ejemplo practico guiado

Detectar zonas atipicas de movilidad y diferenciar ruido algorítmico de evento operativo.

### Actividad EMO [MOV-03]

Construir variables por zona, aplicar dos estrategias, seleccionar parametros con metricas, estabilidad y utilidad, y entregar ficha interpretativa.

## 13.4. Evaluacion, interpretacion y anomalias

Inercia favorece mas grupos; silhouette compara cohesion y separacion; Davies-Bouldin penaliza grupos solapados. La evaluacion externa requiere una referencia independiente. Una anomalia es relativa a la representacion y al contexto.

### 13.4.8. Ejemplo practico guiado

Combinar metricas, visualizacion, estabilidad ante inicializacion y conocimiento del dominio antes de aceptar una segmentacion.

## Sintesis

El aprendizaje no supervisado descubre estructuras candidatas. Su utilidad se demuestra interpretando estabilidad, contexto y consecuencias, no solo con un numero de grupos.
