from git import Repo
from requests import get
from os import startfile, path, getcwd, listdir
from shutil import rmtree, move
from winsound import PlaySound, SND_FILENAME
import sys

sys.stdout = open("outputUpdate.txt", 'w+')

real_path = path.join(path.abspath(path.dirname(__file__)), 'main')
try:
    f = open('main\\cfg\\currect_version.ini', 'w+')
except FileNotFoundError:
    try:
        rmtree(real_path)
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
        move("main\\cfg\\ConfigGames.ini", getcwd())
        move("main\\cfg\\currectGame.ini", getcwd())
        try:
            for f in listdir("main\\icons"):
                move(f"main\\icons\\{f}", getcwd())
        except FileNotFoundError:
            pass
        try:
            for f in listdir("main\\games"):
                move(f"main\\games\\{f}", getcwd())
        except FileNotFoundError:
            pass
        rmtree(real_path)
        Repo.clone_from('https://github.com/JOJO-men/Horizon', 'main')
        try:
            move("main\\settings.exe", getcwd())
            try:
                move("ConfigGames.ini", "main\\cfg")
            except FileNotFoundError:
                pass
            try:
                move("currectGame.ini", "main\\cfg")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 9):
                    move(f"game{i}.lnk", "main\\games")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 5):
                    move(f"web{i}.lnk", "main\\games")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 9):
                    move(f"game{i}.png", "main\\icons")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 5):
                    move(f"web{i}.png", "main\\icons")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 9):
                    move(f"textgame{i}.png", "main\\icons")
            except FileNotFoundError:
                pass
            try:
                for i in range(1, 5):
                    move(f"textweb{i}.png", "main\\icons")
            except FileNotFoundError:
                pass
            startfile('main\\Nightmare.exe')
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
