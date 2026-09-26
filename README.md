# Tradutor

## 1) O que é o projeto?

O projeto Tradutor é uma ferramenta desenvolvida em Python para traduzir documentos em PDF e EPUB de forma automatizada. Ele foi criado para facilitar a leitura de arquivos em outros idiomas, especialmente quando o usuário precisa converter textos para o português sem realizar a tradução manual página por página.

A aplicação utiliza técnicas de extração de texto, OCR e tradução automática para processar documentos digitais de maneira prática e eficiente.

## 2) Quem pode usar?

Este projeto é útil para:

- estudantes que precisam ler materiais em inglês ou em outros idiomas;
- pesquisadores que trabalham com artigos e documentos em múltiplos idiomas;
- profissionais que lidam com arquivos digitais em outros idiomas;
- leitores de livros, manuais e materiais acadêmicos;
- desenvolvedores que desejam adaptar ou evoluir uma ferramenta de tradução automática.

## 3) Quando usar?

O projeto pode ser utilizado quando você precisa:

- traduzir um arquivo PDF para o português;
- transformar um EPUB em uma versão traduzida;
- lidar com documentos que possuem texto não selecionável;
- automatizar a leitura de materiais em outros idiomas;
- obter uma solução simples para tradução local de arquivos digitais.

## 4) Onde o projeto se encaixa?

O repositório está organizado em módulos Python dentro da pasta `src/tradutor`, incluindo:

- `main.py`: ponto de entrada da aplicação;
- `tradutor_pdf.py`: lógica de tradução para arquivos PDF;
- `tradutor_epub.py`: lógica de tradução para arquivos EPUB;
- `pdf_layout.py`: extração de texto e organização do layout das páginas;
- `ocr.py`: reconhecimento óptico de caracteres para páginas sem texto extraível;
- `argos.py`: integração com Argos Translate para tradução dos textos.

Além disso, o projeto conta com arquivos de configuração em `pyproject.toml`, documentação em `README.md` e a licença em `LICENSE`.

## 5) Por que esse projeto existe?

O objetivo principal do Tradutor é reduzir a barreira de idioma na leitura de documentos digitais. Em vez de traduzir manualmente cada página, o projeto automatiza esse processo com o uso de ferramentas de extração de texto e tradução.

O projeto também busca demonstrar como combinar:

- processamento de PDFs;
- leitura de textos em EPUB;
- OCR para páginas imagens;
- tradução automática por blocos;
- uso de bibliotecas Python para manipulação de documentos digitais.

## Visão geral das funcionalidades

- Tradução de arquivos PDF;
- Tradução de arquivos EPUB;
- Suporte a OCR para páginas com texto visual;
- Tradução por blocos de texto;
- Geração de arquivos traduzidos em diretório local;
- Uso simples via linha de comando.

## Tecnologias utilizadas

- Python
- PyMuPDF
- Tesseract OCR
- Pillow
- BeautifulSoup
- Argos Translate
- EbookLib

## Requisitos

- Python 3.14 ou superior
- Dependências listadas em `pyproject.toml`
- Bibliotecas de idioma instaladas para tradução via Argos Translate

## Instalação

Usando `uv`:

```bash
uv sync
```

Ou usando `pip`:

```bash
pip install .
```

## Como executar

Para traduzir um PDF:

```bash
python -m tradutor.main "arquivo.pdf"
```

Para traduzir um EPUB:

```bash
python -m tradutor.main "arquivo.epub"
```

O programa gera arquivos de saída com os nomes:

- `traduzido.pdf`
- `traduzido.epub`

## Estrutura do projeto

```text
Tradutor/
├── src/
│   └── tradutor/
│       ├── __init__.py
│       ├── argos.py
│       ├── instalar_idioma.py
│       ├── main.py
│       ├── ocr.py
│       ├── pdf_layout.py
│       ├── tradutor_epub.py
│       └── tradutor_pdf.py
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
├── uv.lock
└── ...
```

## Observações

Este projeto pode ser aprimorado em diversas áreas, como:

- melhoria da preservação do layout em PDFs complexos;
- suporte a mais idiomas;
- melhor qualidade na tradução contextual;
- interface gráfica mais amigável;
- testes automatizados;
- organização de código para maior escalabilidade.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## Conclusão

O Tradutor é uma solução prática para tradução automática de documentos em PDF e EPUB, com foco em acessibilidade, produtividade e leitura em outros idiomas. Seu objetivo principal é facilitar o acesso ao conteúdo internacional de forma simples, rápida e automatizada.
