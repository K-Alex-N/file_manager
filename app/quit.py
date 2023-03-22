import sys


def input_with_quit_check(txt: str) -> str:
    str_in = input(txt).strip()
    if str_in == 'quit':
        stop()
    return str_in


def stop():
    print('Завершение работы программы')
    sys.exit()
