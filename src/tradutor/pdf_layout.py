import fitz
from tradutor.argos import get_translation, translate_text
from tradutor.ocr import extrair_texto_ocr


def traduzir_pdf_layout(input_path, output_path):
    print(f"Traduzindo: {input_path}")

    doc = fitz.open(input_path)
    new_doc = fitz.open()

    translator = get_translation()

    for i, page in enumerate(doc):
        print(f"Página {i+1}")

        new_page = new_doc.new_page(
            width=page.rect.width,
            height=page.rect.height
        )

        # 🔹 pega blocos de texto
        blocks = page.get_text("blocks")

        # 🔥 se não tiver texto → usa OCR
        if not blocks:
            print(f"⚠️ OCR na página {i+1}")
            texto = extrair_texto_ocr(page)

            traduzido = translate_text(texto, translator)

            new_page.insert_textbox(
                fitz.Rect(50, 50, page.rect.width - 50, page.rect.height - 50),
                traduzido,
                fontsize=10
            )

        else:
            # 🔹 traduz bloco por bloco
            for b in blocks:
                x0, y0, x1, y1, text, *_ = b

                if not text.strip():
                    continue

                traduzido = translate_text(text, translator)

                new_page.insert_textbox(
                    fitz.Rect(x0, y0, x1, y1),
                    traduzido,
                    fontsize=10
                )

    print("Salvando arquivo...")
    new_doc.save(output_path)
    print("Arquivo salvo:", output_path)