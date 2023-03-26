from tkinter import *
from urllib import request
from configparser import ConfigParser
from winsound import PlaySound, SND_FILENAME
from os import startfile, system, getcwd, path, remove
from PIL import Image
import sys


# функции
def resize_image(image_path, size):
    original_image = Image.open(image_path)
    resized_image = original_image.resize(size)
    resized_image.save(image_path)


# функция завершения работы пк
def off():
    system("shutdown /s /t 1 /f")


def anydesk():
    try:
        startfile("main\\additional_app\\AnyDesk.exe")
    except (OSError, IOError):
        startfile("additional_app\\AnyDesk.exe")


# передача CSEA информацию о запущенной игре
def game_number_write(game_number):
    # read input file
    try:
        fin = open("main\\cfg\\currectGame.ini", "rt")
    except (OSError, IOError):
        fin = open("cfg\\currectGame.ini", "rt")
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    data = data.replace(last_line, game_number)
    # close the input file
    fin.close()
    # open the input file in write mode
    try:
        fin = open("main\\cfg\\currectGame.ini", "wt")
    except (OSError, IOError):
        fin = open("cfg\\currectGame.ini", "wt")
    # overrite the input file with the resulting data
    fin.write(data)
    # close the file
    fin.close()


# функции старта игр(ДОЛЖНЫ БЫТЬ ЯРЛЫКИ)
def startgame1():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\game1.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\game1.url")
        except (OSError, IOError):
            try:
                startfile("games\\game1.url")
            except (OSError, IOError):
                try:
                    startfile("games\\game1.lnk")
                except (OSError, IOError):
                    print("файл запуска игры1 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=Game1")

    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startgame2():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\game2.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\game2.url")
        except (OSError, IOError):
            try:
                startfile("games\\game2.url")
            except (OSError, IOError):
                try:
                    startfile("games\\game2.lnk")
                except (OSError, IOError):
                    print("файл запуска игры2 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=Game2")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startgame3():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\game3.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\game3.url")
        except (OSError, IOError):
            try:
                startfile("games\\game3.url")
            except (OSError, IOError):
                try:
                    startfile("games\\game3.lnk")
                except (OSError, IOError):
                    print("файл запуска игры3 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=Game3")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startgame4():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\game4.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\game4.url")
        except (OSError, IOError):
            try:
                startfile("games\\game4.url")
            except (OSError, IOError):
                try:
                    startfile("games\\game4.lnk")
                except (OSError, IOError):
                    print("файл запуска игры4 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=Game4")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startgame5():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\game5.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\game5.url")
        except (OSError, IOError):
            try:
                startfile("games\\game5.url")
            except (OSError, IOError):
                try:
                    startfile("games\\game5.lnk")
                except (OSError, IOError):
                    print("файл запуска игры5 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=Game5")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startgame6():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\game6.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\game6.url")
        except (OSError, IOError):
            try:
                startfile("games\\game6.url")
            except (OSError, IOError):
                try:
                    startfile("games\\game6.lnk")
                except (OSError, IOError):
                    print("файл запуска игры6 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=Game6")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startgame7():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\game7.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\game7.url")
        except (OSError, IOError):
            try:
                startfile("games\\game7.url")
            except (OSError, IOError):
                try:
                    startfile("games\\game7.lnk")
                except (OSError, IOError):
                    print("файл запуска игры7 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=Game7")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startgame8():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\game8.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\game8.url")
        except (OSError, IOError):
            try:
                startfile("games\\game8.url")
            except (OSError, IOError):
                try:
                    startfile("games\\game8.lnk")
                except (OSError, IOError):
                    print("файл запуска игры8 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=Game8")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startweb1():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\web1.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\web1.url")
        except (OSError, IOError):
            try:
                startfile("games\\web1.url")
            except (OSError, IOError):
                try:
                    startfile("games\\web1.lnk")
                except (OSError, IOError):
                    print("файл запуска сайта1 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=web1")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startweb2():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\web2.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\web2.url")
        except (OSError, IOError):
            try:
                startfile("games\\web2.url")
            except (OSError, IOError):
                try:
                    startfile("games\\web2.lnk")
                except (OSError, IOError):
                    print("файл запуска сайта2 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=web2")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startweb3():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\web3.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\web3.url")
        except (OSError, IOError):
            try:
                startfile("games\\web3.url")
            except (OSError, IOError):
                try:
                    startfile("games\\web3.lnk")
                except (OSError, IOError):
                    print("файл запуска сайта3 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=web3")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def startweb4():
    PlaySound(filename3, SND_FILENAME)
    try:
        startfile("main\\games\\web4.lnk")
    except (OSError, IOError):
        try:
            startfile("main\\games\\web4.url")
        except (OSError, IOError):
            try:
                startfile("games\\web4.url")
            except (OSError, IOError):
                try:
                    startfile("games\\web4.lnk")
                except (OSError, IOError):
                    print("файл запуска сайта4 не найден")
                    PlaySound(filename2, SND_FILENAME)
    game_number_write("GameNumber=web4")
    try:
        startfile(r'CSEA.exe')
    except (OSError, IOError):
        startfile(r'main\CSEA.exe')
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
    raise SystemExit


def admin():
    system("explorer.exe")


if __name__ == '__main__':
    try:
        sys.stdout = open("outputmain.txt", 'w')
    except (OSError, IOError):
        sys.stdout = open("main\\outputmain.txt", 'w')
    try:
        with open('main\\cfg\\currectGame.ini', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
    except (OSError, IOError):
        with open('cfg\\currectGame.ini', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
    print("Hello World")
    web1 = None
    web2 = None
    web3 = None
    web4 = None
    game1 = None
    game2 = None
    game3 = None
    game4 = None
    game5 = None
    game6 = None
    game7 = None
    game8 = None
    dopknopka1 = None
    dopknopka2 = None
    dopknopka3 = None
    textgame1 = None
    textgame2 = None
    textgame3 = None
    textgame4 = None
    textgame5 = None
    textgame6 = None
    textgame7 = None
    textgame8 = None
    textweb1 = None
    textweb2 = None
    textweb3 = None
    textweb4 = None
    window = Tk()
    filename2 = 'main\\sounds\\CRASH.wav'
    filename3 = 'main\\sounds\\StartVoice.WAV'
    filename2nomain = 'sounds\\CRASH.wav'
    filename3nomain = 'sounds\\StartVoice.WAV'
    internet = 1
    config = ConfigParser()  # создаём объекта парсера
    try:
        config.read("main\\cfg\\ConfigGames.ini")  # читаем конфиг
    except (OSError, IOError):
        config.read("cfg\\ConfigGames.ini")  # читаем конфиг
    # проверка на наличие интернета
    try:
        request.urlopen("http://google.com")
    except IOError:
        internet = 0
        filename12 = 'sounds\\InternetConnectionTimedOut.wav'
        filename12nomain = 'sounds\\InternetConnectionTimedOut.wav'
        filename142 = 'sounds\\InternetConnectionTimedOut2.wav'
        filename142nomain = 'sounds\\InternetConnectionTimedOut2.wav'
        try:
            PlaySound(filename12, SND_FILENAME)
        except (OSError, IOError):
            PlaySound(filename12nomain, SND_FILENAME)
        try:
            PlaySound(filename142, SND_FILENAME)
        except (OSError, IOError):
            PlaySound(filename142nomain, SND_FILENAME)

    # окно
    window.title("Absolute")
    window.geometry('1365x768')
    window.overrideredirect(True)
    window.state('zoomed')

    if path.exists("main\\first_launch.txt") or path.exists("first_launch.txt"):
        try:
            for p in range(1, 9):
                try:
                    resize_image(f'main\\icons\\game{p}.png', size=(312, 196))
                except (OSError, IOError):
                    resize_image(f'icons\\game{p}.png', size=(312, 196))
                try:
                    im = Image.open(f'main\\icons\\game{p}.png')
                except (OSError, IOError):
                    im = Image.open(f'icons\\game{p}.png')
                w = 255
                x, y = im.size
                pixels = im.load()
                for i in range(x):
                    for j in range(137, y):
                        try:
                            r, g, b, w = pixels[i, j]
                        except ValueError:
                            r, g, b = pixels[i, j]
                        a = r * 0.099 + g * 0.387 + b * 0.114
                        try:
                            pixels[i, j] = int(a), int(a), int(a), int(w)
                        except ValueError:
                            pixels[i, j] = int(a), int(a), int(a)
                try:
                    im.save(f"main\\icons\\game{p}.png")
                except (OSError, IOError):
                    im.save(f"icons\\game{p}.png")
                im.close()

            for p in range(1, 5):
                try:
                    resize_image(f'main\\icons\\web{p}.png', size=(312, 107))
                except (OSError, IOError):
                    resize_image(f'icons\\web{p}.png', size=(312, 107))
                try:
                    im = Image.open(f'main\\icons\\web{p}.png')
                except (OSError, IOError):
                    im = Image.open(f'icons\\web{p}.png')
                w = 255
                x, y = im.size
                pixels = im.load()
                for i in range(x):
                    for j in range(65, y):
                        try:
                            r, g, b, w = pixels[i, j]
                        except ValueError:
                            r, g, b = pixels[i, j]
                        a = r * 0.099 + g * 0.387 + b * 0.114
                        try:
                            pixels[i, j] = int(a), int(a), int(a), int(w)
                        except ValueError:
                            pixels[i, j] = int(a), int(a), int(a)
                try:
                    im.save(f"main\\icons\\web{p}.png")
                except (OSError, IOError):
                    im.save(f"icons\\web{p}.png")
                im.close()

            for p in range(1, 9):
                try:
                    resize_image(f'main\\icons\\game{p}.png', size=(312, 196))
                except (OSError, IOError):
                    resize_image(f'icons\\game{p}.png', size=(312, 196))
                try:
                    im = Image.open(f'main\\icons\\game{p}.png')
                except (OSError, IOError):
                    im = Image.open(f'icons\\game{p}.png')
                w = 255
                x, y = im.size
                pixels = im.load()
                for i in range(x):
                    for j in range(137, y):
                        try:
                            r, g, b, w = pixels[i, j]
                        except ValueError:
                            r, g, b = pixels[i, j]
                        a = r * 0.099 + g * 0.387 + b * 0.114
                        try:
                            pixels[i, j] = int(a), int(a), int(a), int(w)
                        except ValueError:
                            pixels[i, j] = int(a), int(a), int(a)
                try:
                    im.save(f"main\\icons\\game{p}.png")
                except (OSError, IOError):
                    im.save(f"icons\\game{p}.png")
                im.close()

            for p in range(1, 5):
                try:
                    resize_image(f'main\\icons\\web{p}.png', size=(312, 107))
                except (OSError, IOError):
                    resize_image(f'icons\\web{p}.png', size=(312, 107))
                try:
                    im = Image.open(f'main\\icons\\web{p}.png')
                except (OSError, IOError):
                    im = Image.open(f'icons\\web{p}.png')
                w = 255
                x, y = im.size
                pixels = im.load()
                for i in range(x):
                    for j in range(65, y):
                        try:
                            r, g, b, w = pixels[i, j]
                        except ValueError:
                            r, g, b = pixels[i, j]
                        a = r * 0.099 + g * 0.387 + b * 0.074
                        try:
                            pixels[i, j] = int(a), int(a), int(a), int(w)
                        except ValueError:
                            pixels[i, j] = int(a), int(a), int(a)
                try:
                    im.save(f"main\\icons\\web{p}.png")
                except (OSError, IOError):
                    im.save(f"icons\\web{p}.png")
                im.close()
        except BaseException:
            pass
        try:
            remove("main\\first_launch.txt")
        except (OSError, IOError):
            try:
                remove("first_launch.txt")
            except (OSError, IOError):
                pass

    try:
        game1 = PhotoImage(file=f"{getcwd()}\\main\\icons\\game1.png")
    except (OSError, IOError):
        try:
            game1 = PhotoImage(file=f"{getcwd()}\\icons\\game1.png")
        except (OSError, IOError):
            print("нет картинки для game1")
            PlaySound(filename2, SND_FILENAME)
    try:
        game2 = PhotoImage(file=f"{getcwd()}\\main\\icons\\game2.png")
    except (OSError, IOError):
        try:
            game2 = PhotoImage(file=f"{getcwd()}\\icons\\game2.png")
        except (OSError, IOError):
            print("нет картинки для game2")
            PlaySound(filename2, SND_FILENAME)
    try:
        game3 = PhotoImage(file=f"{getcwd()}\\main\\icons\\game3.png")
    except (OSError, IOError):
        try:
            game3 = PhotoImage(file=f"{getcwd()}\\icons\\game3.png")
        except (OSError, IOError):
            print("нет картинки для game3")
            PlaySound(filename2, SND_FILENAME)
    try:
        game4 = PhotoImage(file=f"{getcwd()}\\main\\icons\\game4.png")
    except (OSError, IOError):
        try:
            game4 = PhotoImage(file=f"{getcwd()}\\icons\\game4.png")
        except (OSError, IOError):
            print("нет картинки для game4")
            PlaySound(filename2, SND_FILENAME)
    try:
        game5 = PhotoImage(file=f"{getcwd()}\\main\\icons\\game5.png")
    except (OSError, IOError):
        try:
            game5 = PhotoImage(file=f"{getcwd()}\\icons\\game5.png")
        except (OSError, IOError):
            print("нет картинки для game5")
            PlaySound(filename2, SND_FILENAME)
    try:
        game6 = PhotoImage(file=f"{getcwd()}\\main\\icons\\game6.png")
    except (OSError, IOError):
        try:
            game6 = PhotoImage(file=f"{getcwd()}\\icons\\game6.png")
        except (OSError, IOError):
            print("нет картинки для game6")
            PlaySound(filename2, SND_FILENAME)
    try:
        game7 = PhotoImage(file=f"{getcwd()}\\main\\icons\\game7.png")
    except (OSError, IOError):
        try:
            game7 = PhotoImage(file=f"{getcwd()}\\icons\\game7.png")
        except (OSError, IOError):
            print("нет картинки для game7")
            PlaySound(filename2, SND_FILENAME)
    try:
        game8 = PhotoImage(file=f"{getcwd()}\\main\\icons\\game8.png")
    except (OSError, IOError):
        try:
            game8 = PhotoImage(file=f"{getcwd()}\\icons\\game8.png")
        except (OSError, IOError):
            print("нет картинки для game8")
            PlaySound(filename2, SND_FILENAME)
    try:
        web1 = PhotoImage(file=f"{getcwd()}\\main\\icons\\web1.png")
    except (OSError, IOError):
        try:
            web1 = PhotoImage(file=f"{getcwd()}\\icons\\web1.png")
        except (OSError, IOError):
            print("нет картинки для web1")
            PlaySound(filename2, SND_FILENAME)
    try:
        web2 = PhotoImage(file=f"{getcwd()}\\main\\icons\\web2.png")
    except (OSError, IOError):
        try:
            web2 = PhotoImage(file=f"{getcwd()}\\icons\\web2.png")
        except (OSError, IOError):
            print("нет картинки для web2")
            PlaySound(filename2, SND_FILENAME)
    try:
        web3 = PhotoImage(file=f"{getcwd()}\\main\\icons\\web3.png")
    except (OSError, IOError):
        try:
            web3 = PhotoImage(file=f"{getcwd()}\\icons\\web3.png")
        except (OSError, IOError):
            print("нет картинки для web3")
            PlaySound(filename2, SND_FILENAME)
    try:
        web4 = PhotoImage(file=f"{getcwd()}\\main\\icons\\web4.png")
    except (OSError, IOError):
        try:
            web4 = PhotoImage(file=f"{getcwd()}\\icons\\web4.png")
        except (OSError, IOError):
            print("нет картинки для web4")
            PlaySound(filename2, SND_FILENAME)
    try:
        resize_image('main\\background\\off.png', size=(45, 45))
        dopknopka1 = PhotoImage(file=f"{getcwd()}\\main\\background\\off.png")
    except (OSError, IOError):
        try:
            resize_image('background\\off.png', size=(45, 45))
            dopknopka1 = PhotoImage(file=f"{getcwd()}\\background\\off.png")
        except (OSError, IOError):
            print("нет картинки для доп кнопки1")
            PlaySound(filename2, SND_FILENAME)
    try:
        dopknopka2 = PhotoImage(file=f"{getcwd()}\\main\\background\\help.png")
    except (OSError, IOError):
        try:
            dopknopka2 = PhotoImage(file=f"{getcwd()}\\background\\help.png")
        except (OSError, IOError):
            print("нет картинки для доп кнопки2")
            PlaySound(filename2, SND_FILENAME)
    try:
        dopknopka3 = PhotoImage(file=f"{getcwd()}\\main\\background\\settings.png")
    except (OSError, IOError):
        try:
            dopknopka3 = PhotoImage(file=f"{getcwd()}\\background\\settings.png")
        except (OSError, IOError):
            print("нет картинки для доп кнопки3")
            PlaySound(filename2, SND_FILENAME)
    try:
        for c in range(1, 9):
            pill = Image.open(f'main\\icons\\game{c}.png')
            cuttext = pill.crop((0, 155, 310, 176))
            cuttext.save(f"main\\icons\\textgame{c}.png")
        for c in range(1, 5):
            pill = Image.open(f'main\\icons\\web{c}.png')
            cuttext = pill.crop((0, 70, 310, 95))
            cuttext.save(f"main\\icons\\textweb{c}.png")
    except (OSError, IOError):
        try:
            for c in range(1, 9):
                pill = Image.open(f'icons\\game{c}.png')
                cuttext = pill.crop((0, 155, 310, 176))
                cuttext.save(f"icons\\textgame{c}.png")
            for c in range(1, 5):
                pill = Image.open(f'icons\\web{c}.png')
                cuttext = pill.crop((0, 70, 310, 95))
                cuttext.save(f"icons\\textweb{c}.png")
        except (OSError, IOError):
            print("нет картинок")
            PlaySound(filename2, SND_FILENAME)
    try:
        textgame1 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textgame1.png")
    except (OSError, IOError):
        try:
            textgame1 = PhotoImage(file=f"{getcwd()}\\icons\\textgame1.png")
        except (OSError, IOError):
            print("нет картинки для доп textgame1")
            PlaySound(filename2, SND_FILENAME)
    try:
        textgame2 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textgame2.png")
    except (OSError, IOError):
        try:
            textgame2 = PhotoImage(file=f"{getcwd()}\\icons\\textgame2.png")
        except (OSError, IOError):
            print("нет картинки для доп textgame2")
            PlaySound(filename2, SND_FILENAME)
    try:
        textgame3 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textgame3.png")
    except (OSError, IOError):
        try:
            textgame3 = PhotoImage(file=f"{getcwd()}\\icons\\textgame3.png")
        except (OSError, IOError):
            print("нет картинки для доп textgame3")
            PlaySound(filename2, SND_FILENAME)
    try:
        textgame4 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textgame4.png")
    except (OSError, IOError):
        try:
            textgame4 = PhotoImage(file=f"{getcwd()}\\icons\\textgame4.png")
        except (OSError, IOError):
            print("нет картинки для доп textgame4")
            PlaySound(filename2, SND_FILENAME)
    try:
        textgame5 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textgame5.png")
    except (OSError, IOError):
        try:
            textgame5 = PhotoImage(file=f"{getcwd()}\\icons\\textgame5.png")
        except (OSError, IOError):
            print("нет картинки для доп textgame5")
            PlaySound(filename2, SND_FILENAME)
    try:
        textgame6 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textgame6.png")
    except (OSError, IOError):
        try:
            textgame6 = PhotoImage(file=f"{getcwd()}\\icons\\textgame6.png")
        except (OSError, IOError):
            print("нет картинки для доп textgame6")
            PlaySound(filename2, SND_FILENAME)
    try:
        textgame7 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textgame7.png")
    except (OSError, IOError):
        try:
            textgame7 = PhotoImage(file=f"{getcwd()}\\icons\\textgame7.png")
        except (OSError, IOError):
            print("нет картинки для доп textgame7")
            PlaySound(filename2, SND_FILENAME)
    try:
        textgame8 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textgame8.png")
    except (OSError, IOError):
        try:
            textgame8 = PhotoImage(file=f"{getcwd()}\\icons\\textgame8.png")
        except (OSError, IOError):
            print("нет картинки для доп textgame8")
            PlaySound(filename2, SND_FILENAME)
    try:
        textweb1 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textweb1.png")
    except (OSError, IOError):
        try:
            textweb1 = PhotoImage(file=f"{getcwd()}\\icons\\textweb1.png")
        except (OSError, IOError):
            print("нет картинки для доп textweb1")
            PlaySound(filename2, SND_FILENAME)
    try:
        textweb2 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textweb2.png")
    except (OSError, IOError):
        try:
            textweb2 = PhotoImage(file=f"{getcwd()}\\icons\\textweb2.png")
        except (OSError, IOError):
            print("нет картинки для доп textweb2")
            PlaySound(filename2, SND_FILENAME)
    try:
        textweb3 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textweb3.png")
    except (OSError, IOError):
        try:
            textweb3 = PhotoImage(file=f"{getcwd()}\\icons\\textweb3.png")
        except (OSError, IOError):
            print("нет картинки для доп textweb3")
            PlaySound(filename2, SND_FILENAME)
    try:
        textweb4 = PhotoImage(file=f"{getcwd()}\\main\\icons\\textweb4.png")
    except (OSError, IOError):
        try:
            textweb4 = PhotoImage(file=f"{getcwd()}\\icons\\textweb4.png")
        except (OSError, IOError):
            print("нет картинки для доп textweb4")
            PlaySound(filename2, SND_FILENAME)

    # фон
    try:
        window.image = PhotoImage(file='main\\background\\logo.png')
        bg_logo = Label(window, image=window.image, borderwidth=0)
        bg_logo.place(x=0, y=0)
    except BaseException:
        window.image = PhotoImage(file='background\\logo.png')
        bg_logo = Label(window, image=window.image, borderwidth=0)
        bg_logo.place(x=0, y=0)
    # bg
    # Название проги
    # кнопка1 для игры1

    if internet == 1:
        try:
            startfile(r'NetCheckTrue.exe')
        except (OSError, IOError):
            startfile(r'main\NetCheckTrue.exe')
        btn1 = Button(window, command=startgame1, image=game1, height=195, width=309, compound="center")
        btn1.place(x=49, y=145)
        try:
            stickimage = PhotoImage(file='main\\background\\black_stick.png')
            error = Label(window, image=stickimage, borderwidth=0)
            error.place(x=0, y=66)
            error2 = Label(window, image=stickimage, borderwidth=0)
            error2.place(x=0, y=716)
        except BaseException:
            stickimage = PhotoImage(file='background\\black_stick.png')
            error = Label(window, image=stickimage, borderwidth=0)
            error.place(x=0, y=66)
            error2 = Label(window, image=stickimage, borderwidth=0)
            error2.place(x=0, y=716)
        namegame1 = Label(window, text=config["Game1"]["Name"], font=10, borderwidth=0, anchor="center",
                          compound="center",
                          justify="center", fg="#ffffff", image=textgame1)
        namegame1.place(x=49, y=305)

    else:
        try:
            startfile(r'NetCheckFalse.exe')
        except (OSError, IOError):
            startfile(r'main\NetCheckFalse.exe')
        print("Нет подключения к интернету. Некоторые игры могут не работать")
        lbl = Label(window, text="Нет подключения к интернету. Некоторые игры могут не работать", bg="#cd5c5c",
                    font=("Paper Cuts 2", 20))
        lbl.place(x=250, y=80)
        lbl = Label(window, text="Нет подключения к интернету. Некоторые игры могут не работать", bg="#cd5c5c",
                    font=("Paper Cuts 2", 20))
        lbl.place(x=250, y=728)

        print(config["Game1"]["IsOnline"])
        if config["Game1"]["IsOnline"] == '"false"':
            btn1 = Button(window, command=startgame1, image=game1, height=195, width=309, compound="center")
            btn1.place(x=49, y=145)
            namegame1 = Label(window, text=config["Game1"]["Name"], font=10, borderwidth=0, anchor="center",
                              compound="center",
                              justify="center", fg="#ffffff", image=textgame1)
            namegame1.place(x=49, y=305)

    # -кнопка2 для игры2
    if internet == 1:
        btn2 = Button(window, command=startgame2, image=game2, height=195, width=309, compound="center")
        btn2.place(x=367, y=145)
        namegame2 = Label(window, text=config["Game2"]["Name"], font=10, borderwidth=0, anchor="center",
                          compound="center",
                          justify="center", fg="#ffffff", image=textgame2)
        namegame2.place(x=367, y=305)

    else:
        print(config["Game2"]["IsOnline"])
        if config["Game2"]["IsOnline"] == '"false"':
            btn2 = Button(window, command=startgame2, image=game2, height=195, width=309, compound="center")
            btn2.place(x=367, y=145)
            namegame2 = Label(window, text=config["Game2"]["Name"], font=10, borderwidth=0, anchor="center",
                              compound="center",
                              justify="center", fg="#ffffff", image=textgame2)
            namegame2.place(x=367, y=305)

    # -кнопка3 для игры3
    if internet == 1:
        btn3 = Button(window, command=startgame3, image=game3, height=195, width=309, compound="center")
        btn3.place(x=685, y=145)
        namegame3 = Label(window, text=config["Game3"]["Name"], font=10, borderwidth=0, anchor="center",
                          compound="center",
                          justify="center", fg="#ffffff", image=textgame3)
        namegame3.place(x=685, y=305)

    else:
        print(config["Game3"]["IsOnline"])
        if config["Game3"]["IsOnline"] == '"false"':
            btn3 = Button(window, command=startgame3, image=game3, height=195, width=309, compound="center")
            btn3.place(x=685, y=145)
            namegame3 = Label(window, text=config["Game3"]["Name"], font=10, borderwidth=0, anchor="center",
                              compound="center",
                              justify="center", fg="#ffffff", image=textgame3)
            namegame3.place(x=685, y=305)

    # кнопка4 для игры4
    if internet == 1:
        btn4 = Button(window, command=startgame4, image=game4, height=195, width=310, compound="center")
        btn4.place(x=1003, y=145)
        namegame4 = Label(window, text=config["Game4"]["Name"], font=10, borderwidth=0, anchor="center",
                          compound="center",
                          justify="center", fg="#ffffff", image=textgame4)
        namegame4.place(x=1003, y=305)

    else:
        print(config["Game4"]["IsOnline"])
        if config["Game4"]["IsOnline"] == '"false"':
            btn4 = Button(window, command=startgame4, image=game4, height=195, width=310, compound="center")
            btn4.place(x=1003, y=145)
            namegame4 = Label(window, text=config["Game4"]["Name"], font=10, borderwidth=0, anchor="center",
                              compound="center",
                              justify="center", fg="#ffffff", image=textgame4)
            namegame4.place(x=1003, y=305)

    # кнопка5 для игры5
    if internet == 1:
        btn5 = Button(window, command=startgame5, image=game5, height=195, width=308, compound="center")
        btn5.place(x=49, y=501)
        namegame5 = Label(window, text=config["Game5"]["Name"], font=10, borderwidth=0, anchor="center",
                          compound="center",
                          justify="center", fg="#ffffff", image=textgame5)
        namegame5.place(x=49, y=658)

    else:
        print(config["Game5"]["IsOnline"])
        if config["Game5"]["IsOnline"] == '"false"':
            btn5 = Button(window, command=startgame5, image=game5, height=195, width=308, compound="center")
            btn5.place(x=49, y=501)
            namegame5 = Label(window, text=config["Game5"]["Name"], font=10, borderwidth=0, anchor="center",
                              compound="center",
                              justify="center", fg="#ffffff", image=textgame5)
            namegame5.place(x=49, y=658)

    # кнопка6 для игры6
    if internet == 1:
        btn6 = Button(window, command=startgame6, image=game6, height=195, width=308, compound="center")
        btn6.place(x=367, y=501)
        namegame6 = Label(window, text=config["Game6"]["Name"], font=10, borderwidth=0, anchor="center",
                          compound="center",
                          justify="center", fg="#ffffff", image=textgame6)
        namegame6.place(x=367, y=658)

    else:
        print(config["Game6"]["IsOnline"])
        if config["Game6"]["IsOnline"] == '"false"':
            btn6 = Button(window, command=startgame6, image=game6, height=195, width=308, compound="center")
            btn6.place(x=367, y=501)
            namegame6 = Label(window, text=config["Game6"]["Name"], font=10, borderwidth=0, anchor="center",
                              compound="center",
                              justify="center", fg="#ffffff", image=textgame6)
            namegame6.place(x=367, y=658)

    # кнопка7 для игры7
    if internet == 1:
        btn7 = Button(window, command=startgame7, image=game7, height=195, width=309, compound="center")
        btn7.place(x=685, y=501)
        namegame7 = Label(window, text=config["Game7"]["Name"], font=10, borderwidth=0, anchor="center",
                          compound="center",
                          justify="center", fg="#ffffff", image=textgame7)
        namegame7.place(x=685, y=658)

    else:
        print(config["Game7"]["IsOnline"])
        if config["Game7"]["IsOnline"] == '"false"':
            namegame7 = Label(window, text=config["Game7"]["Name"], font=10, borderwidth=0, anchor="center",
                              compound="center",
                              justify="center", fg="#ffffff", image=textgame7)
            namegame7.place(x=685, y=658)
            btn7 = Button(window, command=startgame7, image=game7, height=195, width=309, compound="center")
            btn7.place(x=685, y=501)

    # кнопка8 для игры8
    if internet == 1:
        btn8 = Button(window, command=startgame8, image=game8, height=195, width=310, compound="center")
        btn8.place(x=1003, y=501)
        namegame8 = Label(window, text=config["Game8"]["Name"], font=10, borderwidth=0, anchor="center",
                          compound="center",
                          justify="center", fg="#ffffff", image=textgame8)
        namegame8.place(x=1003, y=658)

    else:
        print(config["Game8"]["IsOnline"])
        if config["Game8"]["IsOnline"] == '"false"':
            btn8 = Button(window, command=startgame8, image=game8, height=195, width=310, compound="center")
            btn8.place(x=1003, y=501)
            namegame8 = Label(window, text=config["Game8"]["Name"], font=10, borderwidth=0, anchor="center",
                              compound="center",
                              justify="center", fg="#ffffff", image=textgame8)
            namegame8.place(x=1003, y=658)

    # кнопка1 для сайта1
    if internet == 1:
        webBtn1 = Button(window, command=startweb1, image=web1, height=102, width=308, compound="center")
        webBtn1.place(x=49, y=367)
        nameweb1 = Label(window, text=config["Web1"]["Name"], font=10, borderwidth=0, anchor="center",
                         compound="center",
                         justify="center", fg="#ffffff", image=textweb1)
        nameweb1.place(x=49, y=440)

    # кнопка2 для сайта2
    if internet == 1:
        webBtn2 = Button(window, command=startweb2, image=web2, height=102, width=308, compound="center")
        webBtn2.place(x=367, y=367)
        nameweb2 = Label(window, text=config["Web2"]["Name"], font=10, borderwidth=0, anchor="center",
                         compound="center",
                         justify="center", fg="#ffffff", image=textweb2)
        nameweb2.place(x=367, y=440)

    # кнопка3 для сайта3
    if internet == 1:
        webBtn3 = Button(window, command=startweb3, image=web3, height=102, width=309, compound="center")
        webBtn3.place(x=685, y=367)
        nameweb3 = Label(window, text=config["Web3"]["Name"], font=10, borderwidth=0, anchor="center",
                         compound="center",
                         justify="left", fg="#ffffff", image=textweb3)
        nameweb3.place(x=685, y=440)

    # кнопка4 для сайта4
    if internet == 1:
        webBtn4 = Button(window, command=startweb4, image=web4, height=102, width=310, compound="center")
        webBtn4.place(x=1003, y=367)
        nameweb4 = Label(window, text=config["Web4"]["Name"], font=10, borderwidth=0,
                         fg="#ffffff", image=textweb4, anchor='w', compound="center")
        nameweb4.place(x=1004, y=440)

    helpBTN = Button(window, command=anydesk, borderwidth=0, image=dopknopka2, height=38, width=124, compound="center")
    helpBTN.place(x=26, y=12)

    offBTN = Button(window, command=off, borderwidth=0, background="#101010", image=dopknopka1, height=36, width=36,
                    compound="center")
    offBTN.place(x=1237, y=12)

    adminBTN = Button(window, command=admin, borderwidth=0, background="#101010", image=dopknopka3, height=37, width=37,
                      compound="center")
    adminBTN.place(x=1299, y=12)

    window.mainloop()

    print("Goodbye World")
    try:
        system("taskkill /f /im NetCheckTrue.exe")
    except BaseException:
        pass
    try:
        system("taskkill /f /im NetCheckFalse.exe")
    except BaseException:
        pass
