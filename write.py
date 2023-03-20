import os

from create import create_file
from quit import is_stop


def write_file():
    txt = r'введите путь + файл (пример "test\text.txt"): '
    path = input(txt)
    is_stop(path)
    if os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            while True:
                x = input('Добавьте строчку текста. Для завершения введите "stop": ')
                if x != 'stop':
                    f.write(x + '\n')
                    continue
                break
    else:
        print('такой файл не найден')
        print('1 - создать файл')
        print('2 - ввести новый путь к файлу')
        while True:
            s_in = input('введите 1 или 2: ').strip()
            if s_in == '1':
                create_file(path)
            elif s_in == '2':
                write_file()
            else:
                print('введенные данные не распознаны')