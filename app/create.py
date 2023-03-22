import os

from app.quit import input_with_quit_check


def is_exist(path, text):
    if os.path.exists(path):
        print(text)
        return True
    return False


def create_dir():
    str_in = input_with_quit_check(r'введите путь (пример "test"): ')
    if is_exist(str_in, 'Папка уже существует'):
        create_dir()
    else:
        os.makedirs(str_in)
        print(f'Папка "{str_in}" успешно создана')

        # может предлагать сразу же создать файл в этой папке?
        # print('1 - добавить в папку файл')
        # print('2 - вернуться в главное меню')


def create_file(str_in=None):
    if not str_in:
        str_in = input_with_quit_check(r'введите путь до файла и название файла (пример "test\text.txt"): ')
    if is_exist(str_in, 'Файл уже существует'):
        create_file()
    else:
        open(str_in, 'w')
        print(f'Файл "{str_in}" успешно создан')

    # если введен пути нет то предлагать его создать?
