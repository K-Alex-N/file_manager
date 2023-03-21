import os

from quit import is_stop
from read import read_file


def append_file():
    path = input(r'введите путь + файл (пример "test\text.txt"): ')
    is_stop(path)
    if os.path.exists(path):
        read_file(path)
        with open(path, 'a', encoding='utf-8') as f:
            while True:
                x = input('Добавьте строчку текста. Для завершения введите "stop": ')
                if x == 'stop':
                    break
                f.write(x + '\n')
        read_file(path)
    else:
        print('такой файл не найден')
        print('1 - создать файл')
        print('2 - ввести другой путь к файлу')
        s_in = input('выберите 1 или 2: ').strip()
        if s_in == '1':
            create_file(path)
            question_to_add_information_to_file(path)
        elif s_in == '2':
            append_file()
        else:
            print('введенные данные не распознаны')
            write_file(path)