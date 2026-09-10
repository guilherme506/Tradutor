from ebooklib import epub
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import re

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

# ===== CONFIG =====
arquivo_epub = "The Eminence in Shadow Vol.7.epub"
arquivo_pdf = "livro_traduzido.pdf"

# ===== 1. Ler EPUB =====
book = epub.read_epub("The Eminence in Shadow Vol.7.epub")

capitulos = []

for item in book.get_items():
    if item.get_type() == 9:
        soup = BeautifulSoup(item.get_content(), "html.parser")
        texto = soup.get_text()
        if texto.strip():
            capitulos.append(texto.strip())

# ===== 2. Tradutor =====
tradutor = GoogleTranslator(source='auto', target='pt')

# ===== 3. Dividir frases =====
def dividir_em_frases(texto):
    return re.split(r'(?<=[.!?]) +', texto)

# ===== 4. Tradução mais natural =====
def traduzir_natural(texto):
    frases = dividir_em_frases(texto)

    resultado = ""
    bloco = ""

    for frase in frases:
        if len(bloco) + len(frase) < 2500:
            bloco += " " + frase
        else:
            try:
                resultado += tradutor.translate(bloco.strip()) + " "
            except:
                resultado += bloco + " "
            bloco = frase

    if bloco:
        try:
            resultado += tradutor.translate(bloco.strip())
        except:
            resultado += bloco

    return resultado

# ===== 5. Ajuste de linguagem =====
def ajustar_texto(texto):
    ajustes = {
        "Você": "você",
        "No entanto": "Mas",
        "Portanto": "Então",
        "Eu estou": "Eu tô",
        "Não é?": "né?"
    }

    for k, v in ajustes.items():
        texto = texto.replace(k, v)

    return texto

# ===== 6. PDF estilo livro =====
doc = SimpleDocTemplate(
    arquivo_pdf,
    pagesize=A4,
    rightMargin=2.5*cm,
    leftMargin=2.5*cm,
    topMargin=2.5*cm,
    bottomMargin=2.5*cm
)

titulo_style = ParagraphStyle(
    name="Titulo",
    fontSize=18,
    leading=22,
    spaceAfter=20,
    alignment=1
)

texto_style = ParagraphStyle(
    name="Texto",
    fontSize=12,
    leading=18,
    firstLineIndent=20,
    spaceAfter=10,
    alignment=4
)

conteudo = []

# ===== 7. Processar =====
for i, cap in enumerate(capitulos):
    print(f"Capítulo {i+1}/{len(capitulos)}")

    traduzido = traduzir_natural(cap)
    final = ajustar_texto(traduzido)

    paragrafos = final.split("\n")

    conteudo.append(Paragraph(f"Capítulo {i+1}", titulo_style))
    conteudo.append(Spacer(1, 12))

    for p in paragrafos:
        if p.strip():
            conteudo.append(Paragraph(p, texto_style))
            conteudo.append(Spacer(1, 6))

    conteudo.append(PageBreak())

# ===== 8. Gerar PDF =====
doc.build(conteudo)

print("✅ PDF traduzido estilo livro pronto!")