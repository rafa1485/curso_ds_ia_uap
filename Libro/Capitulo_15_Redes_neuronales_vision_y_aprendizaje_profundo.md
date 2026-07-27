# Capitulo 15. Redes neuronales, aprendizaje profundo y vision artificial

## 15.1. Fundamentos de redes neuronales

Una neurona calcula `z=w'x+b` y `a=phi(z)`. Capas componen funciones; pesos y sesgos se ajustan minimizando una perdida. El perceptron solo representa fronteras lineales, mientras que capas no lineales amplian capacidad.

![Esquema de red neuronal](imagenes/red_neuronal.png)

### 15.1.8. Ejemplo practico guiado

Implementar una red pequeña para visualizar una frontera de decision y relacionar cambios de pesos con regiones clasificadas.

### Actividad EMO [VEG-01]

Auditar imagenes, clases, duplicados y metadatos; fijar particiones por planta, captura o procedencia cuando sea posible. Entregar controles de calidad y archivo reproducible de particiones.

## 15.2. Entrenamiento de redes profundas

El descenso del gradiente actualiza `theta <- theta-alpha grad L(theta)`. La retropropagacion aplica regla de la cadena. Mini-batches aproximan el gradiente; epocas recorren datos. Inicializacion, normalizacion, dropout, regularizacion y early stopping controlan inestabilidad y sobreajuste. GPU acelera operaciones, pero no corrige datos o objetivos defectuosos.

### 15.2.9. Ejemplo practico guiado

Leer curvas de entrenamiento y validacion para diagnosticar sobreajuste, subajuste, gradientes inestables y tasa de aprendizaje inadecuada.

### Actividad EMO [VEG-02]

Entrenar baseline, registrar perdida y metricas por epoca, comparar dos controles y justificar diagnostico a partir de curvas.

## 15.3. Imagenes digitales y redes convolucionales

Una imagen es un tensor de alto, ancho y canales. Una convolucion aplica filtros locales; padding y stride controlan dimensiones; pooling resume invariantes locales. Las capas profundas forman mapas de caracteristicas de bordes a patrones complejos.

### 15.3.8. Ejemplo practico guiado

Entrenar una CNN sencilla, examinar matriz de confusion, metricas por clase y galeria de errores.

### Actividad EMO [VEG-03]

Comparar CNN con baseline, informar resultados por clase y relacionar errores con calidad, similitud y cobertura de imagenes.

## 15.4. Transferencia, evaluacion y tareas avanzadas

Transfer learning reutiliza representaciones aprendidas; congelar capas reduce parametros y ajustar fino adapta dominio, con riesgo de sobreajuste. Aumento solo se aplica a entrenamiento. Deteccion localiza objetos y segmentacion asigna clase por region. TensorFlow, Keras y PyTorch son implementaciones, no definiciones del metodo.

### 15.4.9. Ejemplo practico guiado

Comparar extractor congelado y ajuste fino, evaluar por clase y probar generalizacion en imagenes con condiciones distintas.

### Actividad EMO [VEG-04]

Comparar transferencia, calibrar confianza y definir abstencion o revision humana segun errores observados, costo y estabilidad.

## Sintesis

El aprendizaje profundo aprende representaciones, pero depende de particiones, etiquetas, controles de entrenamiento y condiciones de uso. La confianza del modelo no equivale a certeza.
