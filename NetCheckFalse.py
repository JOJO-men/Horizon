import socket
from os import system, startfile
from time import sleep


def is_internet_available(hostname="www.google.com"):
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        return False


while True:
    sleep(5)
    if is_internet_available():
        system("taskkill /f /im Nightmare.exe")
        try:
            startfile(r'Nightmare.exe')
        except (OSError, IOError):
            startfile(r'main\Nightmare.exe')
        break
    else:
        pass
