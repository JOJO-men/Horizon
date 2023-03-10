# Checking the Status of an External Application(game)
from time import sleep
from configparser import ConfigParser
from psutil import process_iter
from os import startfile
import sys


sys.stdout = open("outputCSEA.txt", 'w')

config = ConfigParser()  # создаём объекта парсера
try:
    config.read("cfg\\currectGame.ini")
    gamenumber = config["CurrectGame"]["GameNumber"]
    proccesname = config[gamenumber]["ProccesName"]
except BaseException:
    config.read("main\\cfg\\currectGame.ini")
    gamenumber = config["CurrectGame"]["GameNumber"]
    proccesname = config[gamenumber]["ProccesName"]
if proccesname == "NONE.NONE":
    try:
        startfile(r'Nightmare.exe')
    except (OSError, IOError):
        startfile(r'main\Nightmare.exe')
    sys.exit("указан NONE.NONE")
times = config["TimeToStartTheGameWithAMargin"]["TimeInSeconds"]
rate = config["HowManyTimesDoesItTakeMoreTimeFromTheFirstLaunch"]["rate"]
sleep(float(times) * int(rate))


# while 1:
def check():
    for proc in process_iter():
        if proccesname in proc.name():
            return 0
    return 1


while check() != 1:
    sleep(float(times))

try:
    startfile(r'Nightmare.exe')
except (OSError, IOError):
    startfile(r'main\Nightmare.exe')