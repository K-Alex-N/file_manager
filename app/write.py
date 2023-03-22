import os

from typing import Literal
from app.create import create_file
from app.quit import input_with_quit_check
from app.read import read_file


def question_to_add_information_to_file(path):
    x = input('Добавить информацию в файл? ("Да"/"Нет"): ').lower()
    if x == 'да':
        write_or_append_into_file(path, 'w')
    elif x == 'нет':
        return
    else:
        print('команда не распознана')
        question_to_add_information_to_file(path)


def file_does_not_exist(path: str, mode: Literal['a', 'w'], first_phrase=True):
    if first_phrase:
        print('такой файл не найден')
    print('1 - создать файл')
    print('2 - ввести другой путь к файлу')
    s_in = input('выберите 1 или 2: ').strip()
    if s_in == '1':
        create_file(path)
        question_to_add_information_to_file(path)
    elif s_in == '2':
        d = {
            'w': write_file,
            'a': append_file
        }
        d[mode]()
    else:
        print('введенные данные не распознаны')
        file_does_not_exist(path, mode, first_phrase=False)


def write_or_append_into_file(path: str, mode: Literal['a', 'w']) -> None:
    try:
        if mode == 'a':
            read_file(path)
        with open(path, mode, encoding='utf-8') as f:
            while True:
                x = input('Добавьте строчку текста. Для завершения введите "stop": ')
                if x == 'stop':
                    break
                f.write(x + '\n')
        read_file(path)
    except Exception:
        print('произошла ошибка')
        d = {
            'w': write_file,
            'a': append_file
        }
        d[mode]()


def write_or_append_file(mode: Literal['a', 'w']) -> None:
    str_in = input_with_quit_check(r'введите путь + файл (пример "test\text.txt"): ')
    if os.path.exists(str_in):  # не видит разницу между файлом и папкой!
        write_or_append_into_file(str_in, mode)
    else:
        file_does_not_exist(str_in, mode)


def write_file():
    write_or_append_file('w')


def append_file():
    write_or_append_file('a')
