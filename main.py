import argparse
import os

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='EPUB Converter')
    parser.add_argument('--path',
                        default='/usr/bin/ebook-convert',
                        help='Path to ebook-convert (calibre) file format')
    parser.add_argument('--out',
                        required=True,
                        choices=['azw3', 'docx', 'epub', 'fb2', 'html',
                                 'htmlz', 'lit', 'lrf', 'mobi',
                                 'oeb', 'pdb', 'pdf', 'pml', 'rb',
                                 'rtf', 'snb', 'tcr', 'txt', 'txtz'],
                        help='Output file format')

    args = parser.parse_args()

    out_ext = vars(args).get('out')
    path_ext = vars(args).get('path')

    input_list = ['.azw3', '.chm', '.comic', '.djvu', '.docx',
                  '.epub', '.fb2', '.htlz', '.html', '.lit',
                  '.lrf', '.mobi', '.odt', '.pdb', '.pdf', '.pml',
                  '.rb', '.rtf', '.recipe', '.snb', '.tcr', '.txt']

    directory = "./ebooks/"
    directory_formatted = "./converted/"

    for file in os.listdir(directory):

        file_name, ext = os.path.splitext(file)

        if ext not in input_list:
            break

        os.system(
            path_ext + " " +
            directory +
            file + " " +
            directory_formatted + file_name + "." + out_ext)
