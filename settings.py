import configparser
from pathlib import Path
from win32com.client import Dispatch
from os import path, getcwd, startfile, listdir, remove
from shutil import copyfile


def create_shortcut(file_name: str, target: str, work_dir: str, arguments: str = ''):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path.join(f"{getcwd()}\\main\\games\\", file_name))
    shortcut.TargetPath = target
    shortcut.Arguments = arguments
    shortcut.WorkingDirectory = work_dir
    shortcut.save()


if input("сброс картинок(1) или полная настройка(0) ((Напишите 1 или 0)): ") == "0":
    for i in range(1, 9):
        config = configparser.ConfigParser()
        config.read('main\\cfg\\ConfigGames.ini')
        print("\n\n\n\n\n\n")
        print(f"настройка {i} игры")
        config[f'Game{i}']['IsOnline'] = '"true"' if input("игре нужен интернет (да/нет): ") == "да" else '"false"'
        config[f'Game{i}']['Name'] = input("название игры: ")
        path1 = Path(input("путь до ярлыка игры или exe файла игры: "))
        create_shortcut(
            file_name=f"Game{i}.lnk",
            target=str(path1),
            work_dir=str(path1.parent),
            arguments='',)
        with open('main\\cfg\\ConfigGames.ini', 'w') as configfile:
            config.write(configfile)
        config = configparser.ConfigParser()
        config.read('main\\cfg\\currectGame.ini')
        config[f'Game{i}']['ProccesName'] = input("имя процесса (можно посмотреть в диспетчере задач): ")
        copyfile(input("путь до превьюшки(фона кнопки)(обязательно .png): "), f'main\\icons\\game{i}.png')
        with open('main\\cfg\\currectGame.ini', 'w') as configfile:
            config.write(configfile)

    for i in range(1, 5):
        config = configparser.ConfigParser()
        config.read('main\\cfg\\ConfigGames.ini')
        print("\n\n\n\n\n")
        print(f"настройка {i} сайта")
        config[f'Web{i}']['Name'] = input("название игры: ")
        path1 = Path(input("url ссылка: "))
        create_shortcut(
            file_name=f"web{i}.lnk",
            target=str(path1),
            work_dir=str(path1.parent),
            arguments='',)
        with open('main\\cfg\\ConfigGames.ini', 'w') as configfile:  # save
            config.write(configfile)
        config = configparser.ConfigParser()
        config.read('main\\cfg\\currectGame.ini')
        config[f'Game{i}']['ProccesName'] = input("имя процесса (можно посмотреть в диспетчере задач): ")
        copyfile(input("путь до превьюшки(фона кнопки)(обязательно .png): "), f'main\\icons\\web{i}.png')
        with open('main\\cfg\\currectGame.ini', 'w') as configfile:  # save
            config.write(configfile)
else:
    for f in listdir("main\\icons"):
        remove(path.join("main\\icons", f))
    print("все вревьюшки удалены")
    for i in range(1, 9):
        print("\n\n\n\n\n\n")
        print(f"настройка {i} игры")
        copyfile(input("путь до превьюшки(фона кнопки)(обязательно .png): "), f'main\\icons\\game{i}.png')

    for i in range(1, 5):
        print("\n\n\n\n\n")
        print(f"настройка {i} сайта")
        copyfile(input("путь до превьюшки(фона кнопки)(обязательно .png): "), f'main\\icons\\web{i}.png')
startfile('Nightmare.lnk')
