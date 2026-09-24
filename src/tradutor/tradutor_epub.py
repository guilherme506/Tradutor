from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
from tradutor.argos import get_translation, translate_text


def traduzir_epub(input_path, output_path):
    print(f"📘 Traduzindo EPUB: {input_path}")

    book = epub.read_epub(input_path)
    translator = get_translation()

    itens = [item for item in book.get_items() if item.get_type() == ITEM_DOCUMENT]
    total_capitulos = len(itens)

    total_paragrafos = 0

    for i, item in enumerate(itens):
        print(f"\n📄 Capítulo {i+1}/{total_capitulos}")

        soup = BeautifulSoup(item.get_content(), "html.parser")

        # 🔥 pega só conteúdo relevante
        tags = soup.find_all(["p", "h1", "h2", "h3", "li"])
        total_tags = len(tags)

        for j, tag in enumerate(tags):
            texto = tag.get_text().strip()

            if not texto:
                continue

            # progresso limpo
            print(f"   🔄 {j+1}/{total_tags} parágrafos", end="\r")

            traduzido = translate_text(texto, translator)
            tag.string = traduzido

            total_paragrafos += 1

        item.set_content(str(soup))

        #linha nova depois do capítulo
        print(f"   ✅ {total_tags} parágrafos processados")

    epub.write_epub(output_path, book)

    print("\n✅ Tradução finalizada!")
    print(f"📊 Total de parágrafos traduzidos: {total_paragrafos}")
    print(f"💾 Arquivo salvo em: {output_path}")