import sys
import os
from termcolor import colored, cprint
os.system('clear')

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


def gameboard(x=5, y=5, x_user=1, y_user=1):
    table = []
    for row in range(x):
        table.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                table[row].append('#')
            else:
                table[row].append('.')
    return table


def display_gameboard(table):
    os.system('clear')  # clear screen
    for row in range(len(table)):
        cprint(' '.join(table[row]), 'magenta')

display_gameboard(gameboard(10, 10))

user_coordinates = [1, 1]
