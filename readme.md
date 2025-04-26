# Manga E-book Converter

Esta aplicação permite baixar mangas do Mangadex no formato `.pdf` e convertê-los para diversos formatos compatíveis com leitores de e-books, como `.azw3`, `.epub`, `.mobi`, entre outros.

## Funcionalidades

1. **Baixar mangas do Mangadex**: Baixa capítulos de um manga diretamente do Mangadex, em formato `.pdf`.
2. **Converter arquivos para formatos de e-reader**: Converte arquivos `.pdf` para vários outros formatos, incluindo `.azw3`, `.epub` e `.mobi`.
3. **Suporte a múltiplos formatos**: A aplicação suporta conversão de diversos formatos de e-books para e-readers, incluindo `.azw3`, `.chm`, `.epub`, `.html`, `.mobi`, entre outros.

## Pré-requisitos

- Python 3.x
- `ebook-convert` (parte do Calibre).

## Instalação

1. Clone o repositório:

```bash
git clone
cd
```

2. Instalação calibri (Ubuntu):

```bash
sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin
```

3. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

4. Certifique-se de que as ferramentas `ebook-convert` e `mangadex-dl` estão instaladas no sistema.

```bash
which mangadex-dl
which ebook-convert
```

## Como usar

A aplicação possui dois principais comandos: `manga` e `converter`.

### 1. **Comando `manga`**

Baixa um manga do Mangadex, em formato `.pdf`, e converte para o formato desejado.

#### Exemplo de uso:

```bash
python manga_converter.py manga \
--url "https://mangadex.org/title/... " \
--out "azw3" \
-sc 1 \
-ec 10 \
--lang "pt-br" \
--ecp "/usr/bin/ebook-convert" \
--name "manga_convertido"
```

**Argumentos**:

- `--url`: URL do manga no Mangadex.
- `--out`: Formato de saída (ex: `azw3`, `epub`, `mobi`).
- `-sc`: Capítulo inicial para download.
- `-ec`: Capítulo final para download.
- `--lang`: Idioma (opcional).
- `--ecp`: Caminho para o executável `ebook-convert` (padrão é `/usr/bin/ebook-convert`).
- `--name`: Nome para o arquivo de saída.

### 2. **Comando `converter`**

Converte todos os arquivos na pasta `./ebooks/` para o formato desejado.

#### Exemplo de uso:

```bash
python manga_converter.py converter \
--out "epub" \
--ecp "/usr/bin/ebook-convert" \
--name "manga_convertido"
```

**Argumentos**:

- `--out`: Formato de saída (ex: `azw3`, `epub`, `mobi`).
- `--ecp`: Caminho para o executável `ebook-convert` (padrão é `/usr/bin/ebook-convert`).
- `--name`: Nome para o arquivo de saída.

## Diretórios

- **`./ebooks/`**: Diretório onde os mangas em `.pdf` serão baixados.
- **`./converted/`**: Diretório onde os arquivos convertidos serão salvos.
