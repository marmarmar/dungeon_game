import sys
import os
import time
import gameboard
import random
from termcolor import colored, cprint

os.system('clear')  # clear screen


def choice_gameboard(number, wide_gameboard, height_gameboard, user_coordinates):
    tab = []
    if number == 1:
        tab = gameboard.gameboard(wide_gameboard, height_gameboard, user_coordinates)
    elif number == 2:
        tab = gameboard.gameboard1(wide_gameboard, height_gameboard, user_coordinates)
    elif number == 3:
        tab = gameboard.gameboard2(wide_gameboard, height_gameboard, user_coordinates)
    return tab


def getch():
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def display_gameboard(x, y, table):
    os.system('clear')  # clear screen
    for i in range(x):
        for j in range(y):
            if table[i][j] == '#':
                cprint(table[i][j], 'yellow', end=' ')
            else:
                print(table[i][j], end=' ')
        print('')


def user_move(table, user_position, *args):
    x_user = user_position[0]
    y_user = user_position[1]
    move = getch()
    if move == 'd':
        x_user += 1
        if table[y_user][x_user] == '#':
            x_user -= 1
    elif move == 'a':
        x_user -= 1
        if table[y_user][x_user] == '#':
            x_user += 1
    elif move == 'w':
        y_user -= 1
        if table[y_user][x_user] == '#':
            y_user += 1
    elif move == 's':
        y_user += 1
        if table[y_user][x_user] == '#':
            y_user -= 1
    elif move == 'x':
        sys.exit()
    user_position[0] = x_user
    user_position[1] = y_user
    return user_position


def random_elements(tab, *args):
    """randoms items to gameboard"""
    elements = ['!', '$', '%', '^', '&', '?']
    for i in range(6):
        x = random.randint(2, len(tab)-1)
        y = random.randint(2, len(tab[0])-1)
        while tab[y][x] != '.':
            x = random.randint(2, len(tab)-1)
            y = random.randint(2, len(tab[0])-1)
        tab[y][x] = elements[i]
    return tab


def main():
    user_coordinates = [1, 1]
    wide_gameboard = 40
    height_gameboard = 40
    while True:
        os.system('clear')
        gameboard_table = choice_gameboard(3, wide_gameboard, height_gameboard, user_coordinates)
        gameboard_table = random_elements(gameboard_table)
        display_gameboard(wide_gameboard, height_gameboard, gameboard_table)
        user_move(gameboard_table, user_coordinates)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
