import fitz
import pytesseract
from PIL import Image
import io



def extrair_texto_ocr(page):
    pix = page.get_pixmap()
    img_bytes = pix.tobytes("png")
    img = Image.open(io.BytesIO(img_bytes))

    texto = pytesseract.image_to_string(img, lang="eng+por")
    return texto