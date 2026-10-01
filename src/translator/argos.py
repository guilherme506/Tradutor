import argostranslate.translate

def get_translation(from_code="en", to_code="pt"):
    langs = argostranslate.translate.get_installed_languages()
    
    from_lang = next((l for l in langs if l.code == from_code), None)
    to_lang = next((l for l in langs if l.code == to_code), None)

    if not from_lang or not to_lang:
        raise Exception("Idioma não instalado no Argos")

    return from_lang.get_translation(to_lang)


def translate_text(text, translator):
    if not text.strip():
        return text
    
    try:
        return translator.translate(text)
    except Exception:
        return text