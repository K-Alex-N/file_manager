import os

from create import create_file
from quit import is_stop

from read import read_file

def write_file(path=None):
    if not path:
        path = input(r'введите путь + файл (пример "test\text.txt"): ')
        is_stop(path)
    if os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            while True:
                x = input('Добавьте строчку текста. Для завершения введите "stop": ')
                if x == 'stop':
                    break
                f.write(x + '\n')
        read_file(path)

    else:
        print('такой файл не найден')
        print('1 - создать файл')
        print('2 - ввести новый путь к файлу')
        # избавиться от while True!!!
        while True:
            s_in = input('введите 1 или 2: ').strip()
            if s_in == '1':
                create_file(path)
                x = input('Добавить информацию в файл ("Да"/"Нет"): ')
                if x.lower() == 'да':
                    write_file(path)
            elif s_in == '2':
                write_file()
            else:
                print('введенные данные не распознаны')