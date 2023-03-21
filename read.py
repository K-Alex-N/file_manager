import os

from quit import is_stop, stop


def read_subfunction(func: any, msg: str) -> None:
    if msg:
        print('\n' + msg)
    print('1 - ввести новый путь')
    print('2 - вернуться в главное меню')
    s_in = input('введите (1 или 2): ').strip()
    dct = {
        '1': func,
        '2': lambda: 'ничего не делаем, текущая функция закончится и снова начнется main_menu',
        'quit': stop
    }
    ans = dct.get(s_in, lambda: 'repeat')()
    if ans == 'repeat':
        read_subfunction(func, 'не верный ввод')


def read_file(path=None) -> None:
    if not path:
        path = input(r'введите путь + файл (пример "test\text.txt"): ')
        is_stop(path)
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            print('___Данные из файла___' + '\n' + f.read() + '\n')
    else:
        print('\n' + 'такой файл не существует')
        read_subfunction(func=read_file, msg='')


def read_dir() -> None:
    path = input(r'введите путь до папки (пример "C:\" или "."): ')
    is_stop(path)
    if os.path.exists(path):
        print(f'___Файлы и папки в директории "{path}"___')
        [print(v) for v in os.listdir(path)] + [print('\n')]
    else:
        print('\n' + 'такого пути нет')
        read_subfunction(func=read_dir, msg='')
