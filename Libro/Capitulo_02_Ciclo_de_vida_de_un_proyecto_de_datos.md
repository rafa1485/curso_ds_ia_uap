# Capitulo 2. Ciclo de vida de un proyecto basado en datos

## 2.1. Formulacion del problema

Un problema real debe traducirse a una pregunta analitica y luego a una tarea computacional. La unidad de analisis define que representa una fila; la poblacion y el periodo definen el alcance. Deben separarse entradas disponibles antes de decidir, resultado objetivo y restricciones.

Una especificacion minima es `U = (unidad, usuario, accion, horizonte, objetivo, datos, restricciones, criterio)`. El baseline es una regla simple que permite saber si la complejidad aporta valor.

### 2.1.6. Ejemplo practico guiado

Para calidad del agua, transformar "reducir incidentes" en: describir mediciones por zona, estimar probabilidad de condicion anomala y priorizar muestreos con presupuesto limitado. Declarar como se observa la condicion, que informacion estaria disponible en el momento de la decision y que costo tiene cada error.

### Actividad EMO [AGUA-01]

Definir unidad, usuario, accion, variable objetivo, entradas, restricciones, baseline y criterio de valor. La evidencia individual es una ficha reproducible de una pagina. Se aprueba si existe correspondencia entre necesidad, tarea y decision, y si supuestos y limites son observables.

## 2.2. Metodologias para proyectos de datos

KDD enfatiza seleccion, limpieza, transformacion, mineria e interpretacion. CRISP-DM organiza comprension del negocio, comprension de datos, preparacion, modelado, evaluacion y despliegue. En la practica son ciclos: un hallazgo puede obligar a reformular la pregunta.

Pseudocodigo metodologico:

```text
definir_decision()
establecer_baseline_y_criterios()
recolectar_y_auditar_datos()
si la evidencia contradice el problema: reformular()
preparar_datos_sin_fuga()
entrenar_y_evaluar_con_protocolo()
revisar_riesgos_y_utilidad()
desplegar_con_monitoreo()
iterar_con_nueva_evidencia()
```

### 2.2.6. Ejemplo practico guiado

Diseñar un ciclo CRISP-DM para uno de los cuatro casos transversales, asignando entregable y responsable a cada etapa. La retroalimentacion debe registrar hipotesis confirmadas, rechazadas y aun no evaluadas.

## 2.3. Fuentes, tipos y arquitectura basica de datos

Los datos estructurados tienen esquema tabular; los semiestructurados incorporan claves variables; los no estructurados requieren representacion adicional. Observacionales, experimentales y simulados responden a supuestos distintos. Una arquitectura basica separa fuente, almacenamiento bruto, datos depurados, tabla analitica y resultados.

### 2.3.8. Ejemplo practico guiado

Inventariar para movilidad: fuente, licencia, identificador, frecuencia, cobertura espacial, calidad, formato, clave de integracion y riesgo de sesgo. No debe afirmarse que dos tablas son integrables solo porque comparten una columna con el mismo nombre.

## 2.4. Entornos, herramientas y reproducibilidad

Python y R son medios, no el metodo. Un proyecto reproducible fija versiones, dependencias, semillas, estructura de carpetas, transformaciones y resultados. Un experimento debe registrar pregunta, datos, particion, parametros, metrica, resultado y decision.

### 2.4.8. Ejemplo practico guiado

Crear `datos/`, `notebooks/`, `src/`, `resultados/`, `modelos/` y `documentacion/`; registrar dependencias y un identificador de experimento. El cuaderno debe poder ejecutarse desde cero y fallar explicitamente si falta una entrada.

## Sintesis

Un proyecto de datos es un proceso de decision con evidencia, no una sucesion de algoritmos. La formulacion y la trazabilidad condicionan todo resultado posterior.
