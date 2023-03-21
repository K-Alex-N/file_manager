import os

from quit import is_stop


def is_exist(path, text):
    if os.path.exists(path):
        print(text)
        return True
    return False


def create_dir():
    path = input(r'введите путь (пример "test"): ')
    is_stop(path)
    if is_exist(path, 'Папка уже существует'):
        create_dir()
    else:
        os.makedirs(path)
        print(f'Папка "{path}" успешно создана')

        # может предлагать сразу же создать файл в этой папке?
        # print('1 - добавить в папку файл')
        # print('2 - вернуться в главное меню')


def create_file(path=None):
    if not path:
        path = input(r'введите путь до файла и название файла (пример "test\text.txt"): ')
    is_stop(path)
    if is_exist(path, 'Файл уже существует'):
        create_file()
    else:
        open(path, 'w')
        print(f'Файл "{path}" успешно создан')

    #если введен пути нет то предлагать его создать?
