import argostranslate.package

print("Baixando lista de idiomas...")
argostranslate.package.update_package_index()

available_packages = argostranslate.package.get_available_packages()

# Procurando inglês -> português
package_to_install = next(
    filter(
        lambda x: x.from_code == "en" and x.to_code == "pt",
        available_packages
    )
)

print("Instalando pacote...")
argostranslate.package.install_from_path(package_to_install.download())

print("✅ Idioma instalado!")
