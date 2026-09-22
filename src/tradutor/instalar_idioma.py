import argostranslate.package

print("Buscando pacotes disponíveis...")

available_packages = argostranslate.package.get_available_packages()

print("Pacotes encontrados:", len(available_packages))

for p in available_packages:
    print(p.from_code, "->", p.to_code)

package = next(
    (p for p in available_packages if p.from_code == "en" and p.to_code == "pt"),
    None
)

if not package:
    print("❌ Pacote en->pt NÃO encontrado!")
    exit()

print("Baixando pacote...")

download_path = package.download()

print("Instalando...")

argostranslate.package.install_from_path(download_path)

print("✅ Idioma instalado com sucesso!")