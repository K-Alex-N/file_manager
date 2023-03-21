import sys


def is_stop(str):
    if str == 'quit':
        stop()


def stop():
    print('Завершение работы программы')
    sys.exit()
