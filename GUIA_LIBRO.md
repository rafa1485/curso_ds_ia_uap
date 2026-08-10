# Guia para el desarrollo del libro

Este documento orienta a los agentes de IA que crean, amplian o revisan los capitulos, imagenes y recursos del libro almacenado en `MATERIAL_CURSOS/Libro/`. Debe consultarse antes de modificar ese material.

El libro trata sobre fundamentos, metodos y aplicaciones de Ciencia de Datos e Inteligencia Artificial. El contenido teorico es independiente del lenguaje de implementacion; el codigo aparece solamente en ejemplos practicos, actividades EMO y laboratorios.

## Criterios de desarrollo

Al trabajar en el libro, el agente debe preservar la estructura, terminologia y profundidad de los capitulos existentes. Los enlaces internos y las referencias a imagenes deben usar rutas relativas validas desde el archivo Markdown que las contiene.

## Organizacion

- [Indice del libro](MATERIAL_CURSOS/Libro/00_Indice.md)
- [Capitulo 1](MATERIAL_CURSOS/Libro/Capitulo_01_Ciencia_de_Datos_e_IA.md)
- [Capitulo 2](MATERIAL_CURSOS/Libro/Capitulo_02_Ciclo_de_vida_de_un_proyecto_de_datos.md)
- [Capitulo 3](MATERIAL_CURSOS/Libro/Capitulo_03_Preparacion_calidad_y_transformacion_de_datos.md)
- [Capitulo 4](MATERIAL_CURSOS/Libro/Capitulo_04_Estadistica_descriptiva_exploracion_y_visualizacion.md)
- [Capitulo 5](MATERIAL_CURSOS/Libro/Capitulo_05_Probabilidad_incertidumbre_e_inferencia_bayesiana.md)
- [Capitulo 6](MATERIAL_CURSOS/Libro/Capitulo_06_Agentes_inteligentes_y_representacion_de_problemas.md)
- [Capitulo 7](MATERIAL_CURSOS/Libro/Capitulo_07_Busqueda_y_resolucion_algoritmica.md)
- [Capitulo 8](MATERIAL_CURSOS/Libro/Capitulo_08_Decisiones_secuenciales_y_aprendizaje_por_refuerzo.md)
- [Capitulo 9](MATERIAL_CURSOS/Libro/Capitulo_09_Formulacion_y_evaluacion_de_aprendizaje_automatico.md)
- [Capitulo 10](MATERIAL_CURSOS/Libro/Capitulo_10_Ingenieria_seleccion_y_reduccion_de_atributos.md)
- [Capitulo 11](MATERIAL_CURSOS/Libro/Capitulo_11_Regresion_y_clasificacion.md)
- [Capitulo 12](MATERIAL_CURSOS/Libro/Capitulo_12_Metodos_supervisados_avanzados_y_ensambles.md)
- [Capitulo 13](MATERIAL_CURSOS/Libro/Capitulo_13_Aprendizaje_no_supervisado.md)
- [Capitulo 14](MATERIAL_CURSOS/Libro/Capitulo_14_Series_temporales.md)
- [Capitulo 15](MATERIAL_CURSOS/Libro/Capitulo_15_Redes_neuronales_vision_y_aprendizaje_profundo.md)
- [Capitulo 16](MATERIAL_CURSOS/Libro/Capitulo_16_Procesamiento_del_lenguaje_y_modelos_de_lenguaje.md)
- [Laboratorios integradores](MATERIAL_CURSOS/LABORATORIOS/Laboratorios_integradores.md)
- [Apendices](MATERIAL_CURSOS/Libro/Apendices.md)
- [Apendice D: proyectos y datasets](MATERIAL_CURSOS/LABORATORIOS/Apendice_D_Proyectos_integradores.md)

## Material grafico

Los generadores reproducibles estan en `MATERIAL_CURSOS/Libro/creadores_de_imagenes/`. Sus salidas se guardan en `MATERIAL_CURSOS/Libro/imagenes/` y se referencian desde los capitulos con rutas relativas.

## Entorno de trabajo

Crear el entorno e instalar dependencias desde la raiz del repositorio con:

```text
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Ejecutar un generador desde la raiz del repositorio con `.venv/bin/python MATERIAL_CURSOS/Libro/creadores_de_imagenes/generador_NOMBRE.py`.
