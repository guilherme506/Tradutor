import sys
from tkinter import filedialog
from tradutor.pdf_layout import traduzir_pdf_layout
from tradutor.tradutor_epub import traduzir_epub

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
        traduzir_pdf_layout(arquivo, "traduzido.pdf")

    elif arquivo.endswith(".epub"):
        traduzir_epub(arquivo, "traduzido.epub")

    else:
        print("Formato não suportado")

if __name__ == "__main__":
    main()