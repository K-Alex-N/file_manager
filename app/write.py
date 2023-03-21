import os

from app.create import create_file
from app.quit import is_stop
from app.read import read_file


def write_into_file(path):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            while True:
                x = input('Добавьте строчку текста. Для завершения введите "stop": ')
                if x == 'stop':
                    break
                f.write(x + '\n')
        read_file(path)
    except Exception:
        print('произошла ошибка')
        write_file()

def append_into_file(path):
    try:
        read_file(path)
        with open(path, 'a', encoding='utf-8') as f:
            while True:
                x = input('Добавьте строчку текста. Для завершения введите "stop": ')
                if x == 'stop':
                    break
                f.write(x + '\n')
        read_file(path)
    except Exception:
        print('произошла ошибка')
        append_file()

def question_to_add_information_to_file(path):
    x = input('Добавить информацию в файл? ("Да"/"Нет"): ').lower()
    if x == 'да':
        write_into_file(path)
    elif x == 'нет':
        return
    else:
        print('команда не распознана')
        question_to_add_information_to_file(path)


def file_does_not_exist(path, write_file_or_append_file, first_phrase=True):
    if first_phrase:
        print('такой файл не найден')
    print('1 - создать файл')
    print('2 - ввести другой путь к файлу')
    s_in = input('выберите 1 или 2: ').strip()
    if s_in == '1':
        create_file(path)
        question_to_add_information_to_file(path)
    elif s_in == '2':
        write_file_or_append_file()
    else:
        print('введенные данные не распознаны')
        file_does_not_exist(path, write_file_or_append_file, first_phrase=False)


def write_file():
    path = input(r'введите путь + файл (пример "test\text.txt"): ')
    is_stop(path)
    if os.path.exists(path):  # не видит разницу между файлом и папкой!
        write_into_file(path)
    else:
        file_does_not_exist(path, write_file)

def append_file():
    path = input(r'введите путь + файл (пример "test\text.txt"): ')
    is_stop(path)
    if os.path.exists(path):
        append_into_file(path)
    else:
        file_does_not_exist(path, append_file)
