# Tradutor de Documentos PDF e EPUB

## 1. Sobre o projeto

O **Tradutor** é uma aplicação desenvolvida em Python para traduzir documentos nos formatos PDF e EPUB. Seu objetivo é facilitar a leitura de materiais em outros idiomas, automatizando a extração de texto, o reconhecimento de caracteres em documentos digitalizados e a tradução para o português.

A aplicação utiliza o **Argos Translate**, uma ferramenta de tradução automática que funciona localmente, sem depender de serviços de tradução em nuvem durante o processamento.

## 2. Funcionalidades

- Tradução de documentos PDF.
- Tradução de livros e documentos EPUB.
- Extração de texto de arquivos PDF.
- Reconhecimento óptico de caracteres (OCR) em páginas digitalizadas.
- Tradução de textos utilizando o Argos Translate.
- Processamento de textos de documentos EPUB.
- Seleção de arquivos pela interface do sistema.
- Geração de arquivos traduzidos no computador.

## 3. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.14+ | Linguagem principal |
| uv | Gerenciamento do ambiente e das dependências |
| PyMuPDF | Leitura e manipulação de PDFs |
| Tesseract OCR | Reconhecimento de caracteres |
| pytesseract | Integração entre Python e Tesseract |
| Pillow | Manipulação de imagens |
| OpenCV | Processamento de imagens |
| LayoutParser | Recursos de análise de layout |
| Argos Translate | Tradução automática local |
| EbookLib | Leitura e escrita de EPUB |
| BeautifulSoup4 | Processamento do conteúdo HTML dos EPUBs |
| PyQt6 | Biblioteca de interface gráfica declarada no projeto |
| Tkinter | Seletor de arquivos utilizado na execução atual |

## 4. Requisitos para instalação

Antes de executar o projeto, é necessário ter:

- Python 3.14 ou superior.
- Git.
- uv.
- Tesseract OCR instalado no sistema.
- Dados de idioma do Tesseract para inglês e português.
- Dependências Python instaladas.
- Pacote de tradução inglês → português do Argos Translate.

### Dependências Python

As dependências são declaradas no arquivo `pyproject.toml` e incluem:

```toml
argostranslate
beautifulsoup4
ebooklib
layoutparser
opencv-python
pillow
pymupdf
pyqt6
pytesseract
```

Não é necessário instalar essas bibliotecas individualmente quando se utiliza o `uv`: o comando `uv sync` instala as versões definidas pelo projeto e pelo arquivo `uv.lock`.

## 5. Instalação

### 5.1. Instalar o Git

No Fedora:

```bash
sudo dnf install git
```

No Ubuntu ou Debian:

```bash
sudo apt install git
```

### 5.2. Instalar o uv

O uv é utilizado para gerenciar as versões do Python, criar o ambiente virtual e instalar as dependências.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Depois, atualize o PATH no terminal:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Verifique a instalação:

```bash
uv --version
```

### 5.3. Clonar o repositório

```bash
git clone https://github.com/guilherme506/Tradutor.git
```

Entre na pasta do projeto:

```bash
cd Tradutor
```

### 5.4. Instalar o Python e as dependências

O projeto exige Python 3.14 ou superior.

Instale o Python:

```bash
uv python install 3.14
```

Instale as dependências do projeto:

```bash
uv sync
```

O uv criará o ambiente virtual e instalará as bibliotecas declaradas no `pyproject.toml`.

## 6. Instalação do Tesseract OCR

O Tesseract é uma ferramenta externa. A biblioteca `pytesseract` instalada pelo uv não substitui o programa Tesseract.

### Fedora

```bash
sudo dnf install tesseract tesseract-langpack-eng tesseract-langpack-por
```

### Ubuntu e Debian

```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-eng tesseract-ocr-por
```

### Windows

Instale o Tesseract OCR por meio do instalador disponibilizado pelo projeto UB Mannheim:

https://github.com/UB-Mannheim/tesseract/wiki

Se necessário, adicione a pasta de instalação do Tesseract à variável de ambiente `PATH`.

### Verificar a instalação

Execute:

```bash
tesseract --version
```

Confira os idiomas disponíveis:

```bash
tesseract --list-langs
```

A instalação deve disponibilizar, no mínimo:

```text
eng
por
```

Esses idiomas são utilizados pelo projeto na configuração atual do OCR (`eng+por`).

## 7. Instalação do idioma no Argos Translate

O Argos Translate é instalado como dependência Python pelo `uv sync`. Entretanto, também é necessário instalar o pacote de idioma utilizado na tradução.

Atualmente, o projeto está configurado para traduzir de inglês (`en`) para português (`pt`).

Com o ambiente instalado, execute:

```bash
uv run python -m translator.instalar_idioma
```

O módulo irá:

1. Atualizar a lista de pacotes de idiomas disponíveis.
2. Procurar o pacote de tradução inglês → português.
3. Baixar o pacote encontrado.
4. Instalar o idioma no Argos Translate.

Essa etapa requer conexão com a internet. Depois que o pacote estiver instalado, a tradução poderá ser executada localmente.

## 8. Como executar o projeto

Na raiz do repositório, execute:

```bash
uv run python -m translator.main
```

O programa abrirá uma janela para selecionar um arquivo PDF ou EPUB.

Também é possível informar o arquivo diretamente pelo terminal:

### Traduzir PDF

```bash
uv run python -m translator.main "arquivo.pdf"
```

### Traduzir EPUB

```bash
uv run python -m translator.main "arquivo.epub"
```

Substitua o nome do arquivo pelo caminho correspondente ao documento que deseja traduzir.

## 9. Arquivos gerados

Após o processamento, o projeto salva o documento traduzido no diretório de execução com os seguintes nomes:

- `traduzido.pdf`
- `traduzido.epub`

Caso já exista um arquivo com o mesmo nome, ele poderá ser substituído.

## 10. Estrutura do projeto

```text
Tradutor/
│
├── DOC/
│
├── src/
│   └── translator/
│       ├── __init__.py
│       ├── argos.py
│       ├── instalar_idioma.py
│       ├── interface.py
│       ├── main.py
│       ├── ocr.py
│       ├── pdf_layout.py
│       │
│       └── translator/
│           ├── epub.py
│           └── pdf.py
│
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

### Descrição dos principais módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Ponto de entrada e seleção do documento |
| `argos.py` | Integração com o mecanismo de tradução |
| `instalar_idioma.py` | Instalação do pacote de idioma do Argos |
| `ocr.py` | Reconhecimento de texto em imagens |
| `pdf_layout.py` | Extração, tradução e reconstrução de PDFs |
| `translator/epub.py` | Processamento e tradução de arquivos EPUB |
| `translator/pdf.py` | Funções auxiliares para reconstrução de PDFs |
| `interface.py` | Módulo relacionado à interface do projeto |

## 11. Solução de problemas

### O comando uv não foi encontrado

Adicione o diretório de instalação ao PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Erro relacionado ao Python

Confira a versão:

```bash
uv python list
```

Instale a versão necessária:

```bash
uv python install 3.14
```

### Erro: Tesseract not found

Verifique se o Tesseract está instalado e disponível no PATH:

```bash
tesseract --version
```

### Erro: Idioma não instalado no Argos

Execute novamente:

```bash
uv run python -m translator.instalar_idioma
```

### Erro ao importar tkinter

A execução atual utiliza Tkinter para abrir a janela de seleção de arquivos. Em distribuições Linux, pode ser necessário instalar o pacote de suporte ao Tkinter do sistema.

No Fedora:

```bash
sudo dnf install python3-tkinter
```

No Ubuntu ou Debian:

```bash
sudo apt install python3-tk
```

O interpretador Python utilizado pelo ambiente também precisa ter suporte ao Tkinter.

## 12. Licença

Este projeto está licenciado sob a licença GPL-3.0. Consulte o arquivo `LICENSE` para obter os termos completos de utilização, modificação e distribuição.

## 13. Considerações finais

O Tradutor busca facilitar o acesso a documentos em outros idiomas por meio da combinação de extração de texto, OCR e tradução automática local.

O projeto utiliza ferramentas e bibliotecas de código aberto e pode ser evoluído com melhorias no processamento de documentos, na preservação de layouts, na qualidade das traduções e na interface com o usuário.