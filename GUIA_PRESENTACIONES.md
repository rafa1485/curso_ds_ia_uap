# Guia para el desarrollo de presentaciones de clases

Este documento orienta a los agentes de IA que crean, amplian, revisan o compilan las presentaciones y guias docentes almacenadas en `MATERIAL_CURSOS/Clases/`. Debe consultarse antes de modificar ese material.

## Organizacion

Las clases se organizan por curso y semana dentro de:

- `MATERIAL_CURSOS/Clases/Data_Science/`
- `MATERIAL_CURSOS/Clases/Inteligencia_Artificial/`

Cada presentacion debe mantener junto a sus fuentes los recursos, la guia docente y los PDF que correspondan a la misma clase.

## Formato de las presentaciones

Los archivos `.tex` utilizan LaTeX Beamer en formato panoramico 16:9. Cada presentacion es autonoma y puede compilarse desde su propio directorio.

Al desarrollar o revisar una presentacion, el agente debe preservar el estilo visual y la estructura establecidos por las clases existentes del mismo curso. Tambien debe comprobar que el contenido sea legible, que las figuras no se desborden y que la guia docente corresponda con la version final de las diapositivas.

## Dependencias

En Debian o Ubuntu:

```bash
sudo apt install texlive-latex-recommended texlive-pictures texlive-lang-spanish
```

La instalacion debe proporcionar, como minimo, `pdflatex`, `beamer.cls`, `booktabs.sty`, `tabularx.sty` y el soporte de espanol para `babel`.

## Data Science, semana 1

```bash
cd MATERIAL_CURSOS/Clases/Data_Science/Semana_01
pdflatex Clase_01_Introduccion_a_la_Ciencia_de_Datos.tex
pdflatex Clase_01_Introduccion_a_la_Ciencia_de_Datos.tex
```

## Data Science, semana 2

```bash
cd MATERIAL_CURSOS/Clases/Data_Science/Semana_02
pdflatex Clase_02_Adquisicion_comprension_y_preparacion_inicial_de_datos.tex
pdflatex Clase_02_Adquisicion_comprension_y_preparacion_inicial_de_datos.tex
```

El taller asociado se encuentra en `Taller_Clase_02_Movilidad.ipynb`. Su modo predeterminado procesa una semana consecutiva de enero de 2024 y requiere acceso a las fuentes públicas NYC TLC y NOAA.

## Inteligencia Artificial, semana 1

```bash
cd MATERIAL_CURSOS/Clases/Inteligencia_Artificial/Semana_01
pdflatex Clase_01_Fundamentos_de_IA_agentes_y_racionalidad.tex
pdflatex Clase_01_Fundamentos_de_IA_agentes_y_racionalidad.tex
```

### Resolucion del agente didactico de movilidad

```bash
cd MATERIAL_CURSOS/Clases/Inteligencia_Artificial/Semana_01
pdflatex Presentacion_resolucion_agente_didactico_movilidad.tex
pdflatex Presentacion_resolucion_agente_didactico_movilidad.tex
```

## Inteligencia Artificial, semana 2

```bash
cd MATERIAL_CURSOS/Clases/Inteligencia_Artificial/Semana_02
pdflatex Clase_02_Representacion_y_busqueda_en_espacios_de_estados.tex
pdflatex Clase_02_Representacion_y_busqueda_en_espacios_de_estados.tex
```

La segunda ejecucion actualiza correctamente la numeracion total de diapositivas. Los PDF se generan en los respectivos directorios de cada clase.
