import re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", F + "DejaVuSans-Bold.ttf"))
from reportlab.lib.fonts import addMapping
addMapping("DV", 0, 0, "DV"); addMapping("DV", 1, 0, "DVB")
TITULO = "Parcial 1: Ciencia de Datos 2026"
CONSIGNA = "Seleccione la única alternativa correcta en cada pregunta."

texto = open("parcial_DS1_grupos.md").read()
grupos = re.findall(r"## Grupo (\w+)\n(.*?)### Clave", texto, re.S)
st_t = ParagraphStyle("t", fontName="DVB", fontSize=15, leading=19, alignment=1, spaceAfter=14)
st_d = ParagraphStyle("d", fontName="DV", fontSize=11, leading=22)
st_c = ParagraphStyle("c", fontName="DV", fontSize=10.5, leading=14, spaceBefore=6, spaceAfter=10, textColor=colors.HexColor("#333333"))
st_q = ParagraphStyle("q", fontName="DV", fontSize=10.5, leading=14, spaceAfter=3)
st_o = ParagraphStyle("o", fontName="DV", fontSize=10.5, leading=14, leftIndent=18)
esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

for nombre, cuerpo in grupos:
    preguntas = re.findall(r"\*\*(\d+)\.\*\* (.*?)\n\n((?:[abc]\) .*\n?){3})", cuerpo)
    assert len(preguntas) == 25, (nombre, len(preguntas))
    def pie(c, d):
        c.saveState(); c.setFont("DV", 8); c.setFillColor(colors.grey)
        c.drawString(2*cm, 1.2*cm, f"Grupo {nombre}")
        c.drawRightString(A4[0]-2*cm, 1.2*cm, f"Página {d.page}")
        c.restoreState()
    story = [Paragraph(TITULO, st_t),
             Paragraph("Nombre: " + "_"*38, st_d),
             Paragraph("Apellido: " + "_"*37, st_d),
             Paragraph("Fecha: ____/____/________", st_d),
             Paragraph(CONSIGNA, st_c)]
    for num, enun, ops in preguntas:
        bloque = [Paragraph(f"<b>{num}.</b> {esc(enun)}", st_q)]
        for linea in ops.strip().split("\n"):
            bloque.append(Paragraph(esc(linea.strip()), st_o))
        bloque.append(Spacer(1, 8))
        story.append(KeepTogether(bloque))
    doc = SimpleDocTemplate(f"Parcial_1_Ciencia_de_Datos_2026_Grupo_{nombre}.pdf", pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm, topMargin=1.8*cm, bottomMargin=2*cm,
                            title=f"{TITULO} – Grupo {nombre}")
    doc.build(story, onFirstPage=pie, onLaterPages=pie)
    print("PDF", nombre, len(preguntas))
