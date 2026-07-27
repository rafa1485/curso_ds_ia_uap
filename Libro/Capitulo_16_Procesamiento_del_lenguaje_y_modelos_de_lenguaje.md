# Capitulo 16. Procesamiento del lenguaje natural y grandes modelos de lenguaje

## 16.1. Preparacion y representacion clasica

Un corpus contiene documentos, oraciones y tokens. Normalizar, tokenizar, tratar palabras vacias, aplicar stemming o lematizacion y construir n-gramas cambia la informacion disponible. Bag of Words representa conteos; TF-IDF pondera un termino `t` en documento `d` como `tf(t,d)*log(N/df(t))`.

### 16.1.9. Ejemplo practico guiado

Comparar matrices Bag of Words y TF-IDF para reclamos, observando dimensionalidad, vocabulario y terminos relevantes.

### Actividad EMO [REC-03]

Construir pipeline de normalizacion y TF-IDF, comparar tokenizacion o n-gramas y verificar que vocabulario y pesos se ajustan solo con entrenamiento.

## 16.2. Modelado y evaluacion de textos

La similitud coseno compara vectores; clasificadores predicen categorias; extraccion identifica entidades o relaciones. Desbalance, lenguaje ambiguo, duplicados y cambio de vocabulario afectan resultados. La evaluacion cuantitativa debe complementarse con ejemplos anonimizados de errores.

### 16.2.8. Ejemplo practico guiado

Entrenar baseline de reclamos, revisar falsos positivos y negativos, y convertir el umbral en regla operativa con supervision.

### Actividad EMO [REC-04]

Comparar baseline y modelo, seleccionar umbral con costos, analizar errores por clase y subgrupo, y definir abstencion para baja confianza.

## 16.3. Embeddings, atencion y Transformers

Los embeddings densos representan relaciones distribucionales. Las representaciones contextuales dependen de la posicion y del contexto. La atencion calcula pesos entre consultas, claves y valores:

`Attention(Q,K,V)=softmax(QK' / sqrt(d_k))V`.

Los Transformers combinan atencion, conexiones residuales y redes feed-forward; el preentrenamiento aprende objetivos generales y el ajuste fino adapta una tarea.

![Flujo de un Transformer](imagenes/transformer.png)

### 16.3.8. Ejemplo practico guiado

Comparar TF-IDF y embeddings en similitud o clasificacion, controlar particiones y explicar casos donde el contexto cambia significado.

## 16.4. Grandes modelos de lenguaje y aplicaciones generativas

Un modelo de lenguaje autoregresivo estima `P(x_1,...,x_T)=prod_t P(x_t|x_<t)`. Prompting especifica tarea, contexto, formato y limites; aprendizaje en contexto usa ejemplos dentro de la entrada. La generacion aumentada con recuperacion separa recuperar evidencia de redactar respuesta.

Las alucinaciones, sesgos, privacidad, propiedad intelectual y filtraciones de instrucciones exigen evaluacion, trazabilidad, control de acceso y supervision. Una API es una interfaz de despliegue, no evidencia de veracidad.

### 16.4.10. Ejemplo practico guiado

Diseñar un asistente de reclamos que recupere fuentes, cite antecedentes, genere respuesta y derive casos ambiguos. Evaluar fidelidad, cobertura, seguridad y tasa de abstencion.

## Sintesis

NLP transforma lenguaje en representaciones y decisiones. Los modelos generativos amplian capacidades, pero requieren evidencia recuperable, evaluacion especifica y control humano.
