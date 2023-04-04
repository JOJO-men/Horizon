import configparser
from pathlib import Path
from win32com.client import Dispatch
from os import path, getcwd, startfile
from shutil import copyfile
from sys import exit


def create_shortcut(file_name: str, target: str, work_dir: str, arguments: str = ''):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path.join(f"{getcwd()}\\main\\games\\", file_name))
    shortcut.TargetPath = target
    shortcut.Arguments = arguments
    shortcut.WorkingDirectory = work_dir
    shortcut.save()


answer = input("сброс картинок(1) или полная настройка(0) ((Напишите 1 или 0)): ")
if answer == "0":
    try:
        for i in range(1, 9):
            if input("настроить ещё одну кнопку? (напишите 1 если надо или 0 если не надо): ") == "1":
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
            else:
                break
    except BaseException:
        pass
    for k in range(1, 5):
        try:
            if input("настроить ещё одну кнопку? (напишите 1 если надо или 0 если не надо): ") == "1":
                config = configparser.ConfigParser()
                config.read('main\\cfg\\ConfigGames.ini')
                print("\n\n\n\n\n")
                print(f"настройка {k} сайта")
                config[f'Web{k}']['Name'] = input("название игры: ")
                path1 = Path(input("url ссылка: "))
                create_shortcut(
                    file_name=f"web{k}.lnk",
                    target=str(path1),
                    work_dir=str(path1.parent),
                    arguments='',)
                with open('main\\cfg\\ConfigGames.ini', 'w') as configfile:  # save
                    config.write(configfile)
                config = configparser.ConfigParser()
                config.read('main\\cfg\\currectGame.ini')
                config[f'Game{k}']['ProccesName'] = input("имя процесса (можно посмотреть в диспетчере задач): ")
                copyfile(input("путь до превьюшки(фона кнопки)(обязательно .png): "), f'main\\icons\\web{k}.png')
                with open('main\\cfg\\currectGame.ini', 'w') as configfile:  # save
                    config.write(configfile)
            else:
                break
        except BaseException:
            pass
elif answer == 1:
    for f in range(1, 9):
        try:
            copyfile(f"main\\recovery\\game{f}.png", f'main\\icons\\game{f}.png')
        except BaseException:
            pass
    for g in range(1, 5):
        try:
            copyfile(f"main\\recovery\\web{g}.png", f'main\\icons\\web{g}.png')
        except BaseException:
            pass
    print("все вревьюшки удалены")
    for i in range(1, 9):
        if input("настроить ещё одну кнопку? (напишите 1 если надо или 0 если не надо): ") == "1":
            print("\n\n\n\n\n\n")
            print(f"настройка {i} игры")
            try:
                copyfile(input("путь до превьюшки(фона кнопки)(обязательно .png): "), f'main\\icons\\game{i}.png')
            except BaseException:
                pass
        else:
            break

    for k in range(1, 5):
        if input("настроить ещё одну кнопку? (напишите 1 если надо или 0 если не надо): ") == "1":
            print("\n\n\n\n\n")
            print(f"настройка {k} сайта")
            try:
                copyfile(input("путь до превьюшки(фона кнопки)(обязательно .png): "), f'main\\icons\\web{k}.png')
            except BaseException:
                pass
        else:
            break
else:
    print("Вы написали НЕ 0 и НЕ 1, будьте внимательней НЕ допускайте лишних символов и пробелов")
    input("нажмите любую клавишу чтобы начать заново (настройка обязательна)")
    startfile('settings.exe')
    exit("неправильный ответ(НЕ 0 и НЕ 1)")
startfile('main\\Nightmare.exe')
