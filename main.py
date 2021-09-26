import argparse
import os
from files import *


def is_file_exists(path: str):
    """
    Check if a file exists.
    :param path: Path to file
    :return: True if file exists, else False
    """
    if os.path.isfile(path):
        return True
    return False


def guess_extensions(path: str):
    with open(path, 'rb') as f:
        for filetype in FILETYPES:
            finder = filetype()
            score = finder.get_score(f)
            print(f'{finder.NAME} {finder.EXTS}: {score}%')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Guess files\' extension.')
    parser.add_argument('file', type=str, help='Path to file(s)', nargs='+')

    args = parser.parse_args()
    files_list = args.file

    for file in files_list:
        if is_file_exists(file):
            print(f'Predicting extension for {file}.')
            guess_extensions(file)
        else:
            print(f'{file} does not exist. Skipping')
