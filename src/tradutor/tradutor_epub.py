from ebooklib import epub
from bs4 import BeautifulSoup
from tradutor.argos import get_translation, translate_text

def traduzir_epub(input_path, output_path):
    print(f"Traduzindo EPUB: {input_path}")

    book = epub.read_epub(input_path)
    translator = get_translation()

    for item in book.get_items():
        if item.get_type() == epub.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.content, "html.parser")

            for tag in soup.find_all(string=True):
                if tag.strip():
                    tag.replace_with(translate_text(tag, translator))

            item.set_content(str(soup).encode("utf-8"))

    epub.write_epub(output_path, book)
    print("EPUB salvo:", output_path)