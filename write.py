import os

from create import create_file
from quit import is_stop
from read import read_file


def write_into_file(path):
    with open(path, 'w', encoding='utf-8') as f:
        while True:
            x = input('Добавьте строчку текста. Для завершения введите "stop": ')
            if x == 'stop':
                break
            f.write(x + '\n')
    read_file(path)


def question_to_add_information_to_file(path):
    x = input('Добавить информацию в файл? ("Да"/"Нет"): ').lower()
    if x == 'да':
        write_into_file(path)
    elif x == 'нет':
        return
    else:
        print('команда не распознана')
        question_to_add_information_to_file(path)


def file_does_not_exist(path, first_phrase=True):
    if first_phrase:
        print('такой файл не найден')
    print('1 - создать файл')
    print('2 - ввести другой путь к файлу')
    s_in = input('выберите 1 или 2: ').strip()
    if s_in == '1':
        create_file(path)
        question_to_add_information_to_file(path)
    elif s_in == '2':
        write_file()
    else:
        print('введенные данные не распознаны')
        file_does_not_exist(path, first_phrase=False)


def write_file(path=None):
    if not path:
        path = input(r'введите путь + файл (пример "test\text.txt"): ')
        is_stop(path)
    if os.path.exists(path):
        write_into_file(path)
    else:
        file_does_not_exist(path)
