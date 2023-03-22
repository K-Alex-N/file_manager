import os
from typing import Callable

from app.quit import input_with_quit_check


def incorrect_input(func):
    print('\n' + 'не верный ввод')
    read_subfunction(func)


def read_subfunction(func: Callable) -> None:
    print('1 - ввести новый путь')
    print('2 - вернуться в главное меню')
    str_in = input_with_quit_check('введите (1 или 2): ')
    action = {
        '1': func,
        '2': lambda: 'ничего не делаем, текущая функция закончится и снова начнется main_menu',
    }.get(str_in, incorrect_input(func))()



def read_file(str_in=None) -> None:
    if not str_in:
        str_in = input_with_quit_check(r'введите путь + файл (пример "test\text.txt"): ')
    if os.path.exists(str_in):
        try:
            with open(str_in, encoding='utf-8') as f:
                print(f'___Данные из файла {str_in}___' + '\n' + f.read() + '\n')
        except Exception:
            print('ошибка')
            read_file()
    else:
        print('\n' + 'такой файл не существует')
        read_subfunction(read_file)


def read_dir() -> None:
    str_in = input_with_quit_check(r'введите путь до папки (пример "C:\" или "."): ')
    if os.path.exists(str_in):
        try:
            print(f'___Файлы и папки в директории "{str_in}"___')
            [print(v) for v in os.listdir(str_in)] + [print('\n')]
        except Exception:
            print('ошибка')
            read_dir()
    else:
        print('\n' + 'такого пути нет')
        read_subfunction(read_dir)
