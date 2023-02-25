from git import Repo
from requests import get
from os import startfile, path, getcwd, listdir, system, remove
from shutil import move
from winsound import PlaySound, SND_FILENAME
import sys

sys.stdout = open("outputUpdate.txt", 'w+')

try:
    f = open('main\\cfg\\currect_version.ini', 'r')
except FileNotFoundError:
    try:
        system('RMDIR "main" /S /Q')
    except BaseException:
        pass
    Repo.clone_from('https://github.com/JOJO-men/Horizon', 'main')
    try:
        move("main\\settings.exe", getcwd())
        startfile('settings.exe')
    except FileNotFoundError as e:
        f = open('FatalErrorDownloading.ini', 'w+')
        f.write(str(e))
        f.close()
    sys.exit("Done install")
filename = 'main\\sounds\\updating.wav'

try:
    response = get("https://api.github.com/repos/JOJO-men/Horizon/releases/latest")
    online = response.json()["published_at"]
    offline = f.read()
    if str(online) == str(offline):
        startfile('main\\Nightmare.exe')
        f.close()
    elif str(online) != str(offline):
        PlaySound(filename, SND_FILENAME)
        f.close()
        if path.isfile('ConfigGames.ini'):
            remove('ConfigGames.ini')
        move("main\\cfg\\ConfigGames.ini", getcwd())
        if path.isfile('currectGame.ini'):
            remove('currectGame.ini')
        move("main\\cfg\\currectGame.ini", getcwd())
        try:
            for f in listdir("main\\icons"):
                if path.isfile(f):
                    remove(f)
                move(f"main\\icons\\{f}", getcwd())
        except FileNotFoundError:
            pass
        try:
            for f in listdir("main\\games"):
                if path.isfile(f):
                    remove(f)
                move(f"main\\games\\{f}", getcwd())
        except FileNotFoundError:
            pass

        system('RMDIR "main" /S /Q')
        Repo.clone_from('https://github.com/JOJO-men/Horizon', 'main')
        try:
            if path.isfile('settings.exe'):
                remove('settings.exe')
            try:
                move("main\\settings.exe", getcwd())
            except BaseException:
                pass
            if path.isfile('main\\cfg\\ConfigGames.ini'):
                remove('main\\cfg\\ConfigGames.ini')
            try:
                move("ConfigGames.ini", "main\\cfg")
            except FileNotFoundError:
                pass
            if path.isfile('main\\cfg\\currectGame.ini'):
                remove('main\\cfg\\currectGame.ini')
            try:
                move("currectGame.ini", "main\\cfg")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 9):
                    if path.isfile(f'main\\games\\game{i}.lnk'):
                        remove(f'main\\games\\game{i}.lnk')
                    move(f"game{i}.lnk", "main\\games")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 5):
                    if path.isfile(f'main\\games\\web{i}.lnk'):
                        remove(f'main\\games\\web{i}.lnk')
                    move(f"web{i}.lnk", "main\\games")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 9):
                    if path.isfile(f'main\\icons\\game{i}.png'):
                        remove(f'main\\icons\\game{i}.png')
                    move(f"game{i}.png", "main\\icons")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 5):
                    if path.isfile(f'main\\icons\\web{i}.png'):
                        remove(f'main\\icons\\web{i}.png')
                    move(f"web{i}.png", "main\\icons")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 9):
                    if path.isfile(f'main\\icons\\textgame{i}.png'):
                        remove(f'main\\icons\\textgame{i}.png')
                    move(f"textgame{i}.png", "main\\icons")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 5):
                    if path.isfile(f'main\\icons\\textweb{i}.png'):
                        remove(f'main\\icons\\textweb{i}.png')
                    move(f"textweb{i}.png", "main\\icons")
            except FileNotFoundError:
                pass
            startfile('main\\start.bat')
        except FileNotFoundError as e:
            f = open('FatalErrorDownloading.ini', 'w+')
            f.write(str(e))
            f.close()


except BaseException as e:
    try:
        startfile('main\\Nightmare.exe')
        f = open('FatalErrorDownloading.ini', 'w+')
        f.write(str(e))
        f.close()
    except FileNotFoundError as e:
        f = open('FatalErrorDownloading.ini', 'w+')
        f.write(str(e))
        f.close()
