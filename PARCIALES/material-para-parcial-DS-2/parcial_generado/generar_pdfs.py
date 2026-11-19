import re
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
import io
from reportlab.platypus import Flowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", F + "DejaVuSans-Bold.ttf"))
from reportlab.lib.fonts import addMapping
addMapping("DV", 0, 0, "DV"); addMapping("DV", 1, 0, "DVB")
import sys; sys.dont_write_bytecode = True
from banco_datos import TITULO, NOMBRE, PARES
PARES_N = PARES
CONSIGNA = "Seleccione la única alternativa correcta en cada pregunta."

texto = open(f"{NOMBRE}_grupos.md").read()
grupos = re.findall(r"## Grupo (\w+)\n(.*?)### Clave", texto, re.S)
st_t = ParagraphStyle("t", fontName="DVB", fontSize=15, leading=19, alignment=1, spaceAfter=14)
st_d = ParagraphStyle("d", fontName="DV", fontSize=11, leading=22)
st_c = ParagraphStyle("c", fontName="DV", fontSize=10.5, leading=14, spaceBefore=6, spaceAfter=10, textColor=colors.HexColor("#333333"))
st_q = ParagraphStyle("q", fontName="DV", fontSize=10.5, leading=14, spaceAfter=3)
st_o = ParagraphStyle("o", fontName="DV", fontSize=10.5, leading=14)
esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Opcion(Flowable):
    """Alternativa con la letra correcta circulada en las versiones de respuesta."""

    def __init__(self, letra, texto, correcta=False):
        super().__init__()
        self.letra = letra
        self.texto = Paragraph(esc(texto), st_o)
        self.correcta = correcta
        self.alto = 0

    def wrap(self, ancho_disponible, alto_disponible):
        _, alto_texto = self.texto.wrap(ancho_disponible - 22, alto_disponible)
        self.alto = max(14, alto_texto)
        return ancho_disponible, self.alto

    def draw(self):
        y = self.alto - 11
        self.canv.setFont("DVB" if self.correcta else "DV", 10.5)
        self.canv.setFillColor(colors.HexColor("#007F82") if self.correcta else colors.HexColor("#333333"))
        self.canv.drawCentredString(6, y, self.letra)
        if self.correcta:
            self.canv.setLineWidth(1.15)
            self.canv.circle(6, y + 3.2, 7.2, stroke=1, fill=0)
        self.canv.setFillColor(colors.HexColor("#333333"))
        self.canv.setFont("DV", 10.5)
        self.canv.drawString(13, y, ")")
        self.texto.drawOn(self.canv, 22, 0)


def leer_clave(nombre):
    bloque = re.search(rf"### Clave Grupo {nombre}\n(.*?)(?=\n## |\Z)", texto, re.S)
    assert bloque, f"No se encontró la clave del Grupo {nombre}"
    clave = {int(numero): letra for numero, letra in re.findall(r"\|\s*(\d+)\s*\|\s*([abc])\s*\|", bloque.group(1))}
    assert len(clave) == len(PARES_N), (nombre, len(clave))
    return clave


class DocConPaginas(SimpleDocTemplate):
    """Registra en qué página queda cada pregunta, para replicar los cortes en las respuestas."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pagina_de = {}

    def afterFlowable(self, flowable):
        numero = getattr(flowable, "numero_pregunta", None)
        if numero is not None:
            self.pagina_de[numero] = self.page


def pie(nombre):
    def dibujar_pie(canvas, documento):
        canvas.saveState()
        canvas.setFont("DV", 8)
        canvas.setFillColor(colors.grey)
        canvas.drawString(2 * cm, 1.2 * cm, f"Grupo {nombre}")
        canvas.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"Página {documento.page}")
        canvas.restoreState()
    return dibujar_pie


for nombre, cuerpo in grupos:
    preguntas = re.findall(r"\*\*(\d+)\.\*\* (.*?)\n\n((?:[abc]\) .*\n?){3})", cuerpo)
    assert len(preguntas) == len(PARES_N), (nombre, len(preguntas))

    # El PDF de alumnos se arma siempre para conocer sus cortes de página;
    # solo se guarda en disco con --estudiantes.
    if True:
        story = [Paragraph(TITULO, st_t),
                 Paragraph("Nombre: " + "_"*38, st_d),
                 Paragraph("Apellido: " + "_"*37, st_d),
                 Paragraph("Fecha: ____/____/________", st_d),
                 Paragraph(CONSIGNA, st_c)]
        for num, enun, ops in preguntas:
            bloque = [Paragraph(f"<b>{num}.</b> {esc(enun)}", st_q)]
            for linea in ops.strip().split("\n"):
                bloque.append(Paragraph(esc(linea.strip()), ParagraphStyle("estudiante", parent=st_o, leftIndent=18)))
            bloque.append(Spacer(1, 8))
            bloque[0].numero_pregunta = int(num)  # el enunciado marca la página de la pregunta
            story.append(KeepTogether(bloque))
        guardar = "--estudiantes" in sys.argv
        destino = TITULO.replace(":", "").replace(" ", "_") + f"_Grupo_{nombre}.pdf" if guardar else io.BytesIO()
        doc = DocConPaginas(destino, pagesize=A4,
                                leftMargin=2*cm, rightMargin=2*cm, topMargin=1.8*cm, bottomMargin=2*cm,
                                title=f"{TITULO} – Grupo {nombre}")
        doc.build(story, onFirstPage=pie(nombre), onLaterPages=pie(nombre))
        pagina_alumnos = doc.pagina_de
        assert len(pagina_alumnos) == len(preguntas), (nombre, len(pagina_alumnos))
        if guardar:
            print("PDF estudiantes", nombre, len(preguntas))

    clave = leer_clave(nombre)
    respuestas = [Paragraph(f"{TITULO} — Respuestas", st_t),
                  Paragraph(f"Grupo {nombre}", st_d),
                  Paragraph("Las letras circuladas indican la alternativa correcta.", st_c)]
    marcas = 0
    pagina_anterior = 1
    for num, enun, ops in preguntas:
        numero = int(num)
        if pagina_alumnos[numero] != pagina_anterior:
            respuestas.append(PageBreak())
            pagina_anterior = pagina_alumnos[numero]
        bloque = [Paragraph(f"<b>{num}.</b> {esc(enun)}", st_q)]
        for linea in ops.strip().split("\n"):
            coincidencia = re.fullmatch(r"([abc])\)\s+(.*)", linea.strip())
            assert coincidencia, linea
            letra, alternativa = coincidencia.groups()
            correcta = letra == clave[numero]
            marcas += correcta
            bloque.append(Opcion(letra, alternativa, correcta))
        bloque.append(Spacer(1, 8))
        bloque[0].numero_pregunta = numero
        respuestas.append(KeepTogether(bloque))
    assert marcas == len(preguntas), (nombre, marcas)
    archivo_respuestas = TITULO.replace(":", "").replace(" ", "_") + f"_Respuestas_Grupo_{nombre}.pdf"
    doc = DocConPaginas(archivo_respuestas, pagesize=A4,
                        leftMargin=2*cm, rightMargin=2*cm, topMargin=1.8*cm, bottomMargin=2*cm,
                        title=f"{TITULO} – Respuestas Grupo {nombre}")
    doc.build(respuestas, onFirstPage=pie(nombre), onLaterPages=pie(nombre))
    assert doc.pagina_de == pagina_alumnos, f"Grupo {nombre}: las respuestas quedaron con otra paginación"
    print("PDF respuestas", nombre, marcas)
