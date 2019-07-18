import os
import sys
import yaml
from pprint import pprint
import django


BASE_DIR = os.path.join(os.path.dirname((os.path.abspath(__file__))))


def read_yaml(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
    except Exception as e:
        print(f'ERROR!\n{e}')
    return data


def main():
    sys.path.append(os.path.join(BASE_DIR, 'test_project'))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    django.setup()
    from test_app.models import Product

    print(Product.objects.all())

    file_list = os.listdir(os.path.join(BASE_DIR, 'data'))
    for filename in file_list:
        data = read_yaml(os.path.join(BASE_DIR, 'data', filename))


if __name__ == '__main__':
    main()

