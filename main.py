from append import append_file
from create import create_file, create_dir
from quit import stop
from read import read_dir, read_file
from write import write_file


def incorrect_input_in_main_menu():
    print('\n' + 'не верный ввод')
    main_menu()


def main_menu():
    with open('main_menu.txt', encoding='utf-8') as f:
        print(f.read())

    inpt = input('ввод: ').strip()
    d.get(inpt, incorrect_input_in_main_menu)()


d = {
    '1': read_dir,
    '2': create_dir,
    '3': create_file,
    '4': read_file,
    '5': write_file,
    '6': append_file,
    'quit': stop
}

if __name__ == '__main__':
    while True:
        main_menu()
