import sys
import os
import time
import gameboard
import random
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


def option():
    """starting menu about inventory"""
    option1 = input("Choose an option(start/instructions/credits/exit): ")
    if option1 == 'start':
            start()
            pass
    elif option1 == "instructions":
        instructions()
    elif option1 == "credits":
        credits()
    elif option1 == "exit":
        sys.exit()
        pass


def credits():
    cprint("Made by Maria Steimetz, Mateusz Siga and Marek Stopka", 'green', 'on_grey')
    exit = input("Press <q> to go back to menu: ")
    if exit == 'q':
        option()
    else:
        cprint("Are you ready to go on?", attrs=['bold'])
        instructions()


def instructions():
    """it shows how to move in a dungeon game"""
    cprint("Use WSAD to move up/down/left/right in DUNGEON GAME", 'green', 'on_grey')
    cprint("And x to exit the game.", 'green', 'on_grey')
    exit = input("Press <q> to go back to menu: ")
    if exit == 'q':
        option()
    else:
        cprint("Are you ready to go on?", attrs=['bold'])
        instructions()


def display_gameboard(x, y, table):
    os.system('clear')  # clear screen
    for i in range(x):
        for j in range(y):
            if table[i][j] == '#':
                cprint(table[i][j], 'yellow', attrs=['bold'], end=' ')
            elif table[i][j] == '?':
                cprint(table[i][j], 'red', attrs=['bold'], end=' ')
            elif table[i][j] == '$' or table[i][j] == '%':
                cprint(table[i][j], 'blue', attrs=['bold'], end=' ')
            elif table[i][j] == '^':
                cprint(table[i][j], 'magenta', attrs=['bold'], end=' ')
            elif table[i][j] == '&' or table[i][j] == '!':
                cprint(table[i][j], 'green', attrs=['bold'], end=' ')
            elif table[i][j] == '@':
                cprint(table[i][j], 'white', attrs=['bold'], end=' ')
            else:
                print(table[i][j], end=' ')
        print('')


def user_move(table, user_position):
    """
    Moves user position
    Return new table with new position with user
    """
    global num_gameb
    x_user = user_position[0]
    y_user = user_position[1]
    move = getch()
    if move == 'd':
        x_user += 1
        # checks new position
        if table[y_user][x_user] == '#':
            x_user -= 1
        elif table[y_user][x_user] == '?':
            num_gameb += 1
        # removes @ from previous position
        table[y_user][x_user - 1] = '.'
    elif move == 'a':
        x_user -= 1
        # checks new position
        if table[y_user][x_user] == '#':
            x_user += 1
        elif table[y_user][x_user] == '?':
            num_gameb += 1
        # removes @ from previous position
        table[y_user][x_user + 1] = '.'
    elif move == 'w':
        y_user -= 1
        # checks new position
        if table[y_user][x_user] == '#':
            y_user += 1
        elif table[y_user][x_user] == '?':
            num_gameb += 1
        # removes @ from previous position
        table[y_user + 1][x_user] = '.'
    elif move == 's':
        y_user += 1
        # checks new position
        if table[y_user][x_user] == '#':
            y_user -= 1
        elif table[y_user][x_user] == '?':
            num_gameb += 1
        # removes @ from previous position
        table[y_user - 1][x_user] = '.'
    elif move == 'x':
        sys.exit()
    user_position[0] = x_user
    user_position[1] = y_user
    # sets @ on current position of user
    table[y_user][x_user] = '@'
    return table


def random_elements(tab, *args):
    """randoms items to gameboard"""
    elements = ('!', '$', '%', '^', '&', '?')
    for i in range(6):
        x = random.randint(2, len(tab)-1)
        y = random.randint(2, len(tab[0])-1)
        while tab[y][x] != '.':
            x = random.randint(2, len(tab)-1)
            y = random.randint(2, len(tab[0])-1)
        tab[y][x] = elements[i]
    return tab


def start():
    """Starts game"""
    global num_gameb
    num_gameb = 1
    user_coordinates = [1, 1]
    wide_gameboard = 40
    height_gameboard = 40
    gameboard_table = choice_gameboard(num_gameb, wide_gameboard, height_gameboard, user_coordinates)
    gameboard_table = random_elements(gameboard_table)
    while True:
        os.system('clear')
        if num_gameb == 1:
            display_gameboard(wide_gameboard, height_gameboard, gameboard_table)
            print('{}'.format(num_gameb))
            user_move(gameboard_table, user_coordinates)
            time.sleep(0.1)
        elif num_gameb == 2:
            sfinx()


def main():
    cprint("Welcome stranger in DUNGEON GAME!", 'green', 'on_red')
    option()


main()


if __name__ == '__main__':
    main()
