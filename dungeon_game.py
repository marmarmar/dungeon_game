import sys
import os
import time
from termcolor import colored, cprint

os.system('clear')  # clear screen


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


def gameboard(x=5, y=5, user_position=[1, 1]):
    x_user = user_position[1]
    y_user = user_position[0]
    table = []
    for row in range(x):
        table.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                table[row].append('#')
            elif row == x_user and column == y_user:
                table[row].append('@')
            else:
                table[row].append('.')
    return table


def display_gameboard(table):
    os.system('clear')  # clear screen
    for row in range(len(table)):
        cprint(' '.join(table[row]), 'magenta')


def user_move(x, y, user_position, *args):
    table = gameboard(x, y)
    x_user = user_position[0]
    y_user = user_position[1]
    move = getch()
    if move == 'd':
        x_user += 1
        if table[x_user][y_user] == '#':
            x_user -= 1
    elif move == 'a':
        x_user -= 1
        if table[x_user][y_user] == '#':
            x_user += 1
    elif move == 'w':
        y_user -= 1
        if table[x_user][y_user] == '#':
            y_user += 1
    elif move == 's':
        y_user += 1
        if table[x_user][y_user] == '#':
            y_user -= 1
    user_position[0] = x_user
    user_position[1] = y_user
    return user_position


def main():
    user_coordinates = [1, 1]
    wide_gameboard = 20
    height_gameboard = 20
    while True:
        display_gameboard(gameboard(wide_gameboard, height_gameboard, user_coordinates))
        user_move(wide_gameboard, height_gameboard, user_coordinates)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
