from app.create import create_file, create_dir
from app.quit import stop
from app.read import read_dir, read_file
from app.write import write_file, append_file


def incorrect_input_in_main_menu():
    print('\n' + 'не верный ввод')
    main_menu()


def main_menu():
    with open('main_menu.txt', encoding='utf-8') as f:
        print(f.read())

    inpt = input('ввод: ').strip()
    {
        '1': read_dir,
        '2': create_dir,
        '3': create_file,
        '4': read_file,
        '5': write_file,
        '6': append_file,
        'quit': stop
    }.get(inpt, incorrect_input_in_main_menu)()


if __name__ == '__main__':
    while True:
        main_menu()
