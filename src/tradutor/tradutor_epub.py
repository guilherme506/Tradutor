from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
from tradutor.argos import get_translation, translate_text


def traduzir_epub(input_path, output_path):
    print(f"📘 Traduzindo EPUB: {input_path}")

    book = epub.read_epub(input_path)
    translator = get_translation()

    itens = [item for item in book.get_items() if item.get_type() == ITEM_DOCUMENT]
    total_capitulos = len(itens)

    total_textos = 0

    for i, item in enumerate(itens):
        print(f"\n📄 Capítulo {i+1}/{total_capitulos}")

        soup = BeautifulSoup(item.get_content(), "html.parser")

        for j, node in enumerate(soup.find_all(string=True)):
            texto = node.strip()

            if not texto:
                continue

            if node.parent.name in ["script", "style"]:
                continue

            print(f"   🔄 {j+1} textos", end="\r")

            try:
                traduzido = translate_text(texto, translator)
            except Exception as e:
                print(f"\n⚠️ Erro: {e}")
                continue

            node.replace_with(traduzido)
            total_textos += 1

        item.set_content(str(soup))

        print(f"   ✅ Capítulo concluído")

    epub.write_epub(output_path, book)

    print("\n✅ Tradução finalizada!")
    print(f"📊 Total de textos traduzidos: {total_textos}")
    print(f"💾 Arquivo salvo em: {output_path}")