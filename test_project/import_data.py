import os
import yaml
from pprint import pprint

BASE_DIR = os.path.join(os.path.dirname((os.path.abspath(__file__))), 'data')


def read_yaml(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            #

            pprint(data.keys())

            #
    except Exception as e:
        print(f'ERROR!\n{e}')


def main():
    file_list = os.listdir(BASE_DIR)
    for filename in file_list:
        read_yaml(os.path.join(BASE_DIR, filename))


if __name__ == '__main__':
    main()

