# Visor web del libro

Aplicación web para leer los capítulos Markdown de `Libro/` con tablas, imágenes y fórmulas matemáticas renderizadas mediante MathJax.

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

La unidad `systemd/libro-digital.service` inicia la aplicación automáticamente al comenzar la sesión del usuario. Para instalarla y arrancarla:

```bash
systemctl --user link "$PWD/systemd/libro-digital.service"
systemctl --user enable --now libro-digital.service
```

Comprobar su estado o reiniciarla con:

```bash
systemctl --user status libro-digital.service
systemctl --user restart libro-digital.service
```

Consultar los registros con:

```bash
journalctl --user -u libro-digital.service
```

Los archivos Markdown se leen en cada solicitud. Después de editar un capítulo basta con recargar el navegador; los capítulos nuevos también se detectan automáticamente cuando utilizan el nombre `Capitulo_XX_*.md`.

MathJax se carga desde CDN, por lo que el renderizado de fórmulas requiere conexión a Internet.

## Pruebas

```bash
.venv/bin/python -m unittest discover -s tests
```
