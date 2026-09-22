from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
from tradutor.argos import get_translation, translate_text

def traduzir_epub(input_path, output_path):
    print(f"Traduzindo EPUB: {input_path}")

    book = epub.read_epub(input_path)
    translator = get_translation()

    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), "html.parser")

            for tag in soup.find_all(text=True):
                texto = tag.strip()
                if texto:
                    traduzido = translate_text(texto, translator)
                    tag.replace_with(traduzido)

            item.set_content(str(soup))

    epub.write_epub(output_path, book)
    print("✅ EPUB traduzido salvo em:", output_path)