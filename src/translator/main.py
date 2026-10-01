import sys
from tkinter import filedialog

from translator.pdf_layout import translate_pdf_layout
from translator.translator.epub import translate_epub


def main():
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
    else:
        arquivo = filedialog.askopenfilename(
            title="Escolha um arquivo",
            filetypes=[
                ("Arquivos suportados", "*.pdf *.epub"),
                ("PDF", "*.pdf"),
                ("EPUB", "*.epub"),
            ]
        )

    if not arquivo:
        print("Nenhum arquivo selecionado")
        return

    if arquivo.endswith(".pdf"):
        translate_pdf_layout(arquivo, "traduzido.pdf")

    elif arquivo.endswith(".epub"):
        translate_epub(arquivo, "traduzido.epub")

    else:
        print("Formato não suportado")

if __name__ == "__main__":
    main()


#python -m tradutor.main "arquivo.pdf"
#codigo para traduzir