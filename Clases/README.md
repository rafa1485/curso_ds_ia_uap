# Presentaciones de clase

Los archivos `.tex` utilizan LaTeX Beamer en formato panorámico 16:9. Cada presentación es autónoma y puede compilarse desde su propio directorio.

## Dependencias

En Debian o Ubuntu:

```bash
sudo apt install texlive-latex-recommended texlive-pictures texlive-lang-spanish
```

La instalación debe proporcionar, como mínimo, `pdflatex`, `beamer.cls`, `booktabs.sty`, `tabularx.sty` y el soporte de español para `babel`.

## Data Science, semana 1

```bash
cd Clases/Data_Science/Semana_01
pdflatex Clase_01_Introduccion_a_la_Ciencia_de_Datos.tex
pdflatex Clase_01_Introduccion_a_la_Ciencia_de_Datos.tex
```

## Inteligencia Artificial, semana 1

```bash
cd Clases/Inteligencia_Artificial/Semana_01
pdflatex Clase_01_Fundamentos_de_IA_agentes_y_racionalidad.tex
pdflatex Clase_01_Fundamentos_de_IA_agentes_y_racionalidad.tex
```

La segunda ejecución actualiza correctamente la numeración total de diapositivas. Los PDF se generan en los respectivos directorios de cada clase.
