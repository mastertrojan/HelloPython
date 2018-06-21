import os
import subprocess
import platform
import cat_service


def main():
    print_header()
    folder = get_or_create_folder()
    download_cats(folder)
    display(folder)
    # display cats


def print_header():
    print('________________________')
    print('     Cat Factory')
    print('________________________')


def get_or_create_folder():
    base = os.path.dirname(__file__)
    folder = "kittens"
    file_dir = os.path.join(base, folder)

    if not os.path.exists(file_dir) or not os.path.isdir(file_dir):
        print('Creating new directory at {}'.format(file_dir))
        os.mkdir(file_dir)

    return file_dir


def download_cats(folder):
    cat_count = 8
    for i in range(0, cat_count):
        name = 'lolcat_{}'.format(i)
        # print(i, end=', ')
        cat_service.get_cat(folder, name)


def display(folder):
    operating_system = platform.system()
    print(operating_system)
    print(folder)
    if operating_system == 'Darwin':
        print('Displaying cats in OS window.')
        subprocess.call(['open', folder])
    elif operating_system == 'Windows':
        subprocess.call(['start', folder], shell=True)
    elif operating_system == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('We don\'t support your os: {}'.format(operating_system))


if __name__ == '__main__':
    main()
