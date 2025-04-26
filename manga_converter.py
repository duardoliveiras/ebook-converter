import argparse
import os

DIRECTORY = "./ebooks/"
OUTPUT_DIRECTORY = "./converted/"

def remove_pdf_files():
    for file in os.listdir(DIRECTORY):
        if file.endswith(".pdf"):
            file_path = os.path.join(DIRECTORY, file)
            os.remove(file_path)

def converter(ecp: str, out: str, filename: str):

    input_list = ['.azw3', '.chm', '.comic', '.djvu', '.docx',
                '.epub', '.fb2', '.htlz', '.html', '.lit',
                '.lrf', '.mobi', '.odt', '.pdb', '.pdf', '.pml',
                '.rb', '.rtf', '.recipe', '.snb', '.tcr', '.txt']

    for root, dirs, files in os.walk(DIRECTORY):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext not in input_list:
                continue

            command = f"{ecp} '{root}{file}' '{OUTPUT_DIRECTORY}{filename}.{out}'"
            os.system(command)

def download_and_convert(ecp: str, filename: str,  url: str, out: str, start_chapter: int, end_chapter: int, lang: str = ""):
    remove_pdf_files()
    command_mangadl = f"mangadex-dl {url} -sc {start_chapter} -ec {end_chapter} --path './ebooks/' {f'--language {lang}' if lang != "" else ''} --save-as pdf-single --filename-single {filename}.pdf"
    os.system(command_mangadl)
    converter(ecp, out, filename)


if __name__ == '__main__':
    choices=['azw3', 'docx', 'epub', 'fb2', 'html',
                                 'htmlz', 'lit', 'lrf', 'mobi',
                                 'oeb', 'pdb', 'pdf', 'pml', 'rb',
                                 'rtf', 'snb', 'tcr', 'txt', 'txtz']

    parser = argparse.ArgumentParser(description='AZW3 MANGA DOWNLOADER')

    subparsers = parser.add_subparsers(dest='command', required=False)

    parser_manga = subparsers.add_parser('manga', description='Mangadex manga dowload')
    parser_manga.add_argument('--url', required=False, help='Mangadex url. Example: https://mangadex.org/title/...  ')
    parser_manga.add_argument('--out', required=False, choices=choices,  help='Output format')
    parser_manga.add_argument('-sc', required=True, help="Start chapter")
    parser_manga.add_argument('-ec', required=True, help="End chapter")
    parser_manga.add_argument('--lang', default="", help="Language")
    parser_manga.add_argument('--ecp',
                        default='/usr/bin/ebook-convert',
                        help='Path to ebook-convert (calibre) file format')
    parser_manga.add_argument('--name',
                default="output",
                help='Output file format')

    parser_converter = subparsers.add_parser('converter', description='Converte todos os arquivos dentro da pasta ./ebooks/')
    parser_converter.add_argument('--ecp',
                        default='/usr/bin/ebook-convert',
                        help='Path to ebook-convert (calibre)')
    parser_converter.add_argument('--out',
                        required=True,
                        choices=choices,
                        help='Output file format')
    parser_converter.add_argument('--name',
                    default="output",
                    help='Output file format')

    args = parser.parse_args()

    if args.command == 'manga':
        print(args)
        download_and_convert(args.ecp, args.name, args.url, args.out, args.sc, args.ec, args.lang)
    else: 
        out = vars(args).get('out')
        ecp = vars(args).get('ecp')
        filename = vars(args).get('name')

        converter(ecp, out, filename)



