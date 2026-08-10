# Visor web del libro

Aplicación web para leer los capítulos Markdown de `MATERIAL_CURSOS/Libro/` con tablas, imágenes y fórmulas matemáticas renderizadas mediante MathJax.

## Documentacion para agentes de IA

- `AGENTS.md`: punto de entrada para agentes que trabajan en el repositorio.
- `GUIA_PRESENTACIONES.md`: desarrollo de presentaciones y guias docentes.
- `GUIA_LIBRO.md`: desarrollo de capitulos y recursos del libro.

## Instalación

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Ejecución

```bash
.venv/bin/python app.py
```

El libro estará disponible en <http://localhost:7000/libro_ds_ia/>.

## Servicio de usuario

El repositorio incluye dos unidades de usuario para equipos diferentes:

- `systemd/libro-digital.service`: unidad del equipo cuyo repositorio se encuentra en `%h/datos/curso_ds_ia_uap`; publica el visor en todas sus interfaces de red.
- `systemd/libro-digital-rafa-local.service`: unidad de este ordenador, con el repositorio en `/home/rafa/CLASES_DS_IA_UAP`; publica el visor solamente en `127.0.0.1:7000`.

Para instalar y arrancar la unidad local de este ordenador:

```bash
systemctl --user link "$PWD/systemd/libro-digital-rafa-local.service"
systemctl --user enable --now libro-digital-rafa-local.service
```

Comprobar su estado o reiniciarla con:

```bash
systemctl --user status libro-digital-rafa-local.service
systemctl --user restart libro-digital-rafa-local.service
```

Consultar los registros con:

```bash
journalctl --user -u libro-digital-rafa-local.service
```

Los archivos Markdown se leen en cada solicitud. Después de editar un capítulo basta con recargar el navegador; los capítulos nuevos también se detectan automáticamente cuando utilizan el nombre `Capitulo_XX_*.md`.

MathJax se carga desde CDN, por lo que el renderizado de fórmulas requiere conexión a Internet.

## Pruebas

```bash
.venv/bin/python -m unittest discover -s tests
```
