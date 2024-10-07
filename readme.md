### Epub batch converter

Esse script python foi desenvolvido para realizar a conversão de um grupo de arquivos para um determinado formato de saída. Ele utiliza o [calibre](https://calibre-ebook.com/) para converter e o python para manipular a pasta de entrada/saída.

`/ebook`: pasta de entrada
`/converted`: pasta de saída

#### Como usar?

Definir `ebook_convert_path` de acordo com o seu sistema operacional.

Para encontrar o caminho no linux:

```bash
$ where ebook-convert
/usr/bin/ebook-convert

```

```bash
python3 main.py --path /usr/bin/ebook-convert --out [format]
```

O calibre tem suporte para conversão de:

- .azw3
- .chm
- .comic
- .djvu
- .docx
- .epub
- .fb2
- .htlz
- .html
- .lit
- .lrf
- .mobi
- .odt
- .pdb
- .pdf
- .pml
- .rb
- .rtf
- .recipe
- .snb
- .tcr
- .txt

#### Extra

Para baixar volumes de mangás direto do Manga Dex:

```bash
$ python -m venv .venv
$ source ./.venv/bin/activate
$ pip install mangadex-downloader
$ pip install lxml
$ pip install bs4
$ pip install Pillow
$ mangadex-dl "https://mangadex.org/title/.../" --save-as "epub-volume"
```
