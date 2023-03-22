from urllib import request
from os import system, startfile
from time import sleep


def is_internet_available():
    try:
        request.urlopen('http://google.com')
        return True
    except:
        return False


while True:
    sleep(5)
    if is_internet_available():
        pass
    else:
        system("taskkill /f /im Nightmare.exe")
        try:
            startfile(r'Nightmare.exe')
        except (OSError, IOError):
            startfile(r'main\Nightmare.exe')
        break
