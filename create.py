import os

from quit import is_stop


def is_exist(path, text):
    if os.path.exists(path):
        print(text)
        return True
    return False


def create_dir():
    txt = r'введите путь до папки и название папки (пример "test"): '
    path = input(txt)
    is_stop(path)
    if is_exist(path, 'Папка уже существует'):
        create_dir()
    else:
        os.makedirs(path)
        print(f'Папка "{path}" успешно создана')


def create_file(path=None):
    if not path:
        txt = r'введите путь до файла и название файла (пример "test\text.txt"): '
        path = input(txt)

    if is_exist(path, 'Файл уже существует'):
        create_file()
    else:
        open(path, 'w')
        if path.count('/'):
            path = path.replace('/', '\\')
            i = path.rindex('\\')
            path = path[i + 1:]
        print(f'Файл "{path}" успешно создан')

    #TODO: если вдруг введен новый путь до файла и пути нет то предлагать его создать
