import os

from app.quit import stop, input_with_quit_check


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
        read_subfunction(func=read_file, msg='')


def read_dir() -> None:
    str_in = input_with_quit_check(r'введите путь до папки (пример "C:\" или "."): ')
    if os.path.exists(str_in):
        print(f'___Файлы и папки в директории "{str_in}"___')
        [print(v) for v in os.listdir(str_in)] + [print('\n')]
    else:
        print('\n' + 'такого пути нет')
        read_subfunction(func=read_dir, msg='')
