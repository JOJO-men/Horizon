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
    except FileNotFoundError:
        f = open('FatalErrorDownloading.ini', 'w+')
        f.close()
        exit()
    exit()
filename = 'main\\sounds\\updating.wav'

try:
    response = get("https://api.github.com/repos/JOJO-men/Horizon/releases/latest")

    if response.json()["published_at"] == f.read():
        startfile('main\\Nightmare.exe')
        f.close()
    elif response.json()["published_at"] != f.read():
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
                move(getcwd(), "main\\cfg\\")
            except FileNotFoundError:
                pass
            try:
                move(getcwd(), "main\\cfg\\")
            except FileNotFoundError:
                pass
            try:
                move("game1.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("game2.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("game3.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("game4.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("game5.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("game6.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("game7.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("game8.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("web1.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("web2.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("web3.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            try:
                move("web4.lnk", "main\\games\\")
            except FileNotFoundError:
                pass
            startfile('settings.exe')
        except FileNotFoundError:
            f = open('FatalErrorDownloading.ini', 'w+')
            f.close()
            exit()

except BaseException:
    try:
        startfile('main\\Nightmare.exe')
        f = open('FatalErrorDownloading.ini', 'w+')
        f.close()
        exit()
    except FileNotFoundError:
        f = open('FatalErrorDownloading.ini', 'w+')
        f.close()
        exit()
