def reconstruir_pdf(blocos, output):
    import fitz

    doc = fitz.open()
    page = doc.new_page()

    for bloco in blocos:
        x0, y0, x1, y1 = bloco["bbox"]

        page.insert_textbox(
            fitz.Rect(x0, y0, x1, y1),
            bloco["text"],
            fontsize=10
        )

    doc.save(output)