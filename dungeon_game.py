import sys
import os
import time
from termcolor import colored, cprint

os.system('clear')  # clear screen

inv = {}


def sfinx():
    life = 3
    print("If you answer my riddle I will give you a ruby. If not I will attack you!")
    print("\nWhat creature walks on four legs in the morning, on two in the midday and on three in the evening?")
    answer_sfinx = input("\nWhat is your answer?: ")
    while answer_sfinx != "human":
        life -= 1
        answer_sfinx = input("What is your answer?: ")
        print(life)
    else:
        print("You are correct. Here is your ruby. You can move on with your journey.")
        loot = ['ruby']
        add_to_inventory(inv, loot)


def add_to_inventory(inv, loot):
    for b in loot:
        if not b in inv:  # for new items
            inv[b] = 1
        else:
            inv[b] += 1   # for already acquired items

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
            if row == 0 or row == x-1 or column == 0 or column == y-1 or \
                    (row > 15 and row < 16 and column > 8 and column < 13) or \
                    (row > 7 and row < 10 and column > 5 and column < 8) or \
                    (row > 24 and row < 27 and column > 30 and column < 35) or \
                    (row > 5 and row < 10 and column > 20 and column < 30) or \
                    (row > 12 and row < 15 and column > 20 and column < 25) or \
                    (row < 2 and column > 12 and column < 17) or \
                    (row > 27 and row < 33 and column > 2 and column < 9):
                table[row].append('#')
            elif row == x_user and column == y_user:
                table[row].append('@')
            else:
                table[row].append('.')
    return table


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


def main():

    user_coordinates = [1, 1]
    wide_gameboard = 40
    height_gameboard = 40
    while True:
        os.system('clear')
        gameboard_table = gameboard(wide_gameboard, height_gameboard, user_coordinates)
        display_gameboard(wide_gameboard, height_gameboard, gameboard_table)
        user_move(gameboard_table, user_coordinates)
        time.sleep(0.1)



if __name__ == '__main__':
    main()

