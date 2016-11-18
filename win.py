from termcolor import colored, cprint
import sys
import os
import time


def win_game():
    """prints ascii from file"""
    os.system('clear')
    col = ['green', 'yellow', 'blue', 'red']
    x = open("win.txt", 'r')
    i = 0
    j = 0
    for line in x:
        i += 1
        if i > 0 and i < 7:
            time.sleep(0.2)
            print('\t\t\t', end='')

        if i > 7 and i < 15:
            j = 1
            time.sleep(0.2)
            print('\t\t      ', end='')

        if i > 15 and i < 23:
            j = 2
            time.sleep(0.2)
            print('\t\t\t', end='')

        if i > 23 and i < 31:
            j = 3
            time.sleep(0.2)
            print('\t\t', end='')

        # cprint(line, "red", attrs=['bold'], end='')
        cprint(line, col[j], attrs=['bold'], end='')
        # print(line, end='')
    # plays music from current folder
    os.system("aplay hobbit.wav")
    # os.system("aplay ~/kodowanie/dungeon_game/hobbit.wav")
    sys.exit()

# print_win()
