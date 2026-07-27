# Capitulo 12. Metodos supervisados avanzados y ensambles

## 12.1. Arboles de decision

Un arbol particiona recursivamente. La entropia es `H=-sum p_k log p_k`; la ganancia compara impureza antes y despues. Gini es `1-sum p_k^2`. Profundidad, minimo de hoja y poda controlan complejidad.

### 12.1.8. Ejemplo practico guiado

Entrenar un arbol de incidentes, leer reglas, podar y comparar claridad con generalizacion.

## 12.2. Maquinas de soporte vectorial

SVM busca hiperplano con margen maximo. El margen blando permite violaciones penalizadas por `C`. Kernels calculan similitud implicita y permiten fronteras no lineales. Escalado y costo computacional son parte del modelo.

### 12.2.8. Ejemplo practico guiado

Comparar kernels sobre una tarea no lineal y evaluar sensibilidad de `C` y parametros del kernel.

## 12.3. Metodos de ensamble

Bagging promedia modelos entrenados sobre muestras; Random Forest agrega aleatoriedad de variables; boosting ajusta modelos sucesivos a errores previos. Stacking combina predicciones mediante un metamodelo. Las comparaciones requieren mismo protocolo, baseline y presupuesto.

### 12.3.8. Ejemplo practico guiado

Competencia controlada entre arbol, bosque y boosting, con validacion comun y analisis de estabilidad.

## 12.4. Explicabilidad y aprendizaje distribuido

Importancia por permutacion mide degradacion al perturbar una variable; dependencia parcial resume efecto medio; SHAP descompone una prediccion bajo supuestos de coalicion. Explicacion global no sustituye explicacion local. El aprendizaje federado mueve modelos y no datos, pero no garantiza privacidad por si mismo: existen filtraciones, costos de comunicacion y deriva entre nodos.

### 12.4.8. Ejemplo practico guiado

Explicar una prediccion individual y contrastarla con importancia global, señalando correlacion y limites de la explicacion.

## Sintesis

Mayor capacidad no implica mayor validez. Ensambles, explicabilidad y distribucion deben evaluarse por generalizacion, estabilidad, costo y condiciones de uso.
