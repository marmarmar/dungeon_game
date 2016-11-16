import sys
import os
import time
import gameboard
import random
import collections
import sfinx_graphic
import hangman_game
from termcolor import colored, cprint

os.system('clear')  # clear screen


def intro_graphic():
    data = [line.strip() for line in open("intro_graphic.txt", 'r')]
    for i in range(len(data)):
        if i == 0:
            print(" ", end='')
        if i == 9:
            print(" ", end='')
        if i > 7:
            print("            ", end='')
        for j in range(len(data[i])):
            time.sleep(0.001)
            cprint("{}".format(data[i][j]), 'red', attrs=['bold'], end='')
        print()
    print()


def print_table(order="count,asc"):
    """Prints sorted table of inventory"""
    os.system('clear')
    global inv
    # if user want to sort own inventory, sorts it by values
    if order == "count,desc":
        ordered = sorted(inv, key=inv.get, reverse=True)
    elif order == "count,asc":
        ordered = sorted(inv, key=inv.get, reverse=False)
    else:
        ordered = inv
    total = 0
    # checks maximal length of names of loot and if it's to short for
    # good presentation change it to 9
    max_len = len(max(inv, key=len))
    if max_len < 9:
        max_len = 9
    # creates string which will been displays
    formatted_text = "{:>7}{:>%d}" % (max_len + 3)
    print("Inventory:")
    print(formatted_text.format("count", "item name"))
    print("-" * (10 + max_len))
    for i in ordered:
        print(formatted_text.format(inv[i], i))
        total += inv[i]
    print("-" * (10 + max_len))
    print("Total number of items: {}\n".format(total))
    print('Press any key to exit')
    x = getch()


def sfinx(life):
    global num_gameb
    global inv
    # global life
    sfinx_graphic.print_sfinx()
    print("If you answer my riddle I will give you a ruby. If not I will attack you!")
    print("\nWhat creature walks on four legs in the morning, on two in the midday and on three in the evening?")
    answer_sfinx = input("\nWhat is your answer?: ")
    while answer_sfinx != "human":
        os.system('clear')  # clear screen
        life -= 1
        sfinx_graphic.print_sfinx()
        print("\nWhat creature walks on four legs in the morning, on two in the midday and on three in the evening?")
        print("lifes:", life)
        answer_sfinx = input("What is your answer?: ")
    else:
        print("You are correct. Here is your ruby. You can move on with your journey.")
        loot = ['ruby']
        inv = add_to_inventory(loot)
        num_gameb += 1
        return life


def merchant():
    global gold_coins
    global num_gameb
    life_potions = 5
    print("Welcome in my shop.")
    print("\nI sell potions that restore your life.")
    print("\nOne costs 30 gold coins")
    if gold_coins >= 30:
        print("You can buy at least one")
        while True:
            try:
                amount = int(input("\nHow many do you want?(0 for exit): "))
                if life_potions >= amount:
                    if amount == 0:
                        break
                        num_gameb += 1
                        num_gameb -= 1
                    elif gold_coins >= amount * 30:
                        life_potions = ['life potions'] * amount
                        gold_coins = gold_coins - 30 * amount
                        print(life_potions)
                        print("\nThank you for purchase.")
                        loot = life_potions*amount
                        add_to_inventory(loot)
                        num_gameb += 1
                        num_gameb -= 1
                    else:
                        print("You don't have enough gold.")
            except ValueError:
                break
                num_gameb += 1
                num_gameb -= 1
    elif gold_coins < 30:
        print("You don't have enough gold to trade with me")
        key = input("Press any key to go on")
        num_gameb += 1
        num_gameb -= 1



def add_to_inventory(loot):
    """it adding loot to current inventory"""
    global inv
    inv = collections.Counter(inv)
    # collections module helps to add dictionaries value
    loot = collections.Counter(loot)
    inv = inv+loot


def choice_gameboard(number, wide_gameboard, height_gameboard, user_coordinates):
    tab = []
    if number == 1:
        tab = gameboard.gameboard(wide_gameboard, height_gameboard, user_coordinates)
    elif number == 3:
        tab = gameboard.gameboard1(wide_gameboard, height_gameboard, user_coordinates)
    elif number == 6:
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
    print('     ', end='')
    cprint("\t\t  ...:::CHOOSE AN OPTION:::...\t\t", 'green', 'on_grey')
    print('     ', end='')
    cprint("{:>9}{:>16}{:>11}{:>8}\t".format('START', 'INSTRUCTIONS', 'CREDITS', 'EXIT'), 'green', 'on_grey')
    print('     ', end='')
    cprint("{:>7}{:>13}{:>13}{:>10}\t".format('1', '2', '3', 'X'), 'blue', 'on_grey')
    option1 = getch()
    if option1 == '1':
            start()
    elif option1 == '2':
        os.system('clear')  # clear screen
        instructions()
    elif option1 == '3':
        os.system('clear')  # clear screen
        credits()
    elif option1 == 'x':
        sys.exit()


def credits():
    cprint("Made by Maria Steinmec, Mateusz Siga and Marek Stopka", 'green', 'on_grey')
    cprint("Press <q> to go back to menu: ", 'red', 'on_grey')
    exit = getch()
    if exit == 'q':
        os.system('clear')
        option()
    else:
        cprint("Are you ready to go on?", attrs=['bold'])
        credits()


def instructions():
    """it shows how to move in a dungeon game"""
    cprint("Use WSAD to move up/down/left/right in DUNGEON GAME", 'green', 'on_grey')
    cprint("And x to exit the game.", 'green', 'on_grey')
    cprint("Press <q> to go back to menu: ", 'red', 'on_grey')
    exit = getch()
    if exit == 'q':
        os.system('clear')  # clear screen
        option()
    else:
        cprint("Are you ready to go on?", attrs=['bold'])
        instructions()


def display_gameboard(x, y, table, life, gold_coins):
    os.system('clear')  # clear screen
    for i in range(x):
        if i == 2:
            cprint("{:^15}".format("GOLD COINS"), 'green', attrs=['bold'], end='')
        elif i == 3:
            cprint("{:^15}".format(gold_coins), 'green', attrs=['bold'], end='')
        elif i == 6:
            cprint("{:^15}".format("LIFES"), 'green', attrs=['bold'], end='')
        elif i == 7:
            cprint("{:^15}".format(life), 'green', attrs=['bold'], end='')
        else:
            print('{:>15}'.format(''), end='')
        for j in range(y):
            if table[i][j] == '#':
                cprint(table[i][j], 'yellow', attrs=['bold'], end=' ')
            elif table[i][j] == 'M':
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
            elif table[i][j] == '.':
                print('\033[1;30;1m' + "{}".format(table[i][j]) + '\033[0m', end=' ')
        print('')
    cprint("{:^110}".format("For backpack press 'i'"), 'green', attrs=['bold'])


def user_move(table, user_position):
    """
    Moves user and clears previous position
    Returns new table with new position with user
    When touch '?' going to boss level
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
        # removes @ from previous position
        table[y_user][x_user - 1] = '.'
    elif move == 'a':
        x_user -= 1
        if table[y_user][x_user] == '#':
            x_user += 1
        table[y_user][x_user + 1] = '.'
    elif move == 'w':
        y_user -= 1
        if table[y_user][x_user] == '#':
            y_user += 1
        table[y_user + 1][x_user] = '.'
    elif move == 's':
        y_user += 1
        if table[y_user][x_user] == '#':
            y_user -= 1
        table[y_user - 1][x_user] = '.'
    elif move == 'x':
        sys.exit()
    elif move == 'i':
        print_table()
    user_position[0] = x_user
    user_position[1] = y_user
    check_touch(table, user_position)
    # sets @ on current position of user
    table[y_user][x_user] = '@'


def check_touch(table, user_position):
    """Checks if the user touches any item"""
    global num_gameb
    global gold_coins
    global life
    x_user = user_position[0]
    y_user = user_position[1]
    if table[y_user][x_user] == '?':
        num_gameb += 1
    elif table[y_user][x_user] == '!':
        # add ascii with weapon
        weapon = ['sword', 'axe', 'dagger']
        loot = [random.choice(weapon)]
        add_to_inventory(loot)
    elif table[y_user][x_user] == '$':
        gold_coins += random.randint(20, 50)
    elif table[y_user][x_user] == '%':
        loot = ['bootle']
        add_to_inventory(loot)
        # add ascii drinking
    elif table[y_user][x_user] == 'M':
        merchant()
    elif table[y_user][x_user] == '^':
        if 'sword' in inv.keys() or 'dagger' in inv.keys() or 'axe' in inv.keys():
            # add ascii ruby
            loot = ['ruby']
            add_to_inventory(loot)
        else:
            life -= 1
    elif table[y_user][x_user] == '&':
        # add ascii spell book
        loot = ['spell book', 'globe', 'abacus']
        add_to_inventory(loot)
    return life



def random_elements(tab, *args):
    """randoms items to gameboard"""
    elements = ('!', '$', '%', '^', '&', '?', 'M')
    for i in range(len(elements)):
        x = random.randint(2, len(tab)-1)
        y = random.randint(2, len(tab[0])-1)
        while tab[y][x] != '.':
            x = random.randint(2, len(tab)-1)
            y = random.randint(2, len(tab[0])-1)
        tab[y][x] = elements[i]
    return tab


def start():
    """
    Starts game
    num_gameb checks wich gameboard should be displayed
    if num_gameb ==
        #1 first gameboard
        #2 sfinx
        #3 create second gameboard
        #4 run second gameboard
        #5 ...
    """
    global gold_coins
    global num_gameb
    global inv
    global life
    life = 3
    gold_coins = 10
    inv = {'ruby': 1}
    num_gameb = 1
    user_coordinates = [1, 1]
    wide_gameboard = 40
    height_gameboard = 40
    gameboard_table = choice_gameboard(num_gameb, wide_gameboard, height_gameboard, user_coordinates)
    gameboard_table = random_elements(gameboard_table)
    while True:
        os.system('clear')
        if num_gameb == 1:
            display_gameboard(wide_gameboard, height_gameboard, gameboard_table, life, gold_coins)
            print('{}'.format(num_gameb))
            user_move(gameboard_table, user_coordinates)
            time.sleep(0.1)
        elif num_gameb == 2:
            # move to first boss
            life = sfinx(life)
        elif num_gameb == 3:
            # creates new gameboard
            user_coordinates = [1, 1]
            gameboard_table = choice_gameboard(num_gameb, wide_gameboard, height_gameboard, user_coordinates)
            gameboard_table = random_elements(gameboard_table)
            num_gameb += 1
        elif num_gameb == 4:
            # run next level
            display_gameboard(wide_gameboard, height_gameboard, gameboard_table, life, gold_coins)
            print('{}'.format(num_gameb))
            user_move(gameboard_table, user_coordinates)
            time.sleep(0.1)
        elif num_gameb == 5:
            hang_tupl = hangman_game.main(life, num_gameb)
            life = hang_tupl[0]
            num_gameb = hang_tupl[1]
        elif num_gameb == 6:
            # creates new gameboard
            user_coordinates = [1, 1]
            gameboard_table = choice_gameboard(num_gameb, wide_gameboard, height_gameboard, user_coordinates)
            gameboard_table = random_elements(gameboard_table)
            num_gameb += 1
        elif num_gameb == 7:
            # run next level
            display_gameboard(wide_gameboard, height_gameboard, gameboard_table, life, gold_coins)
            print('{}'.format(num_gameb))
            user_move(gameboard_table, user_coordinates)
            time.sleep(0.1)


def main():
    intro_graphic()
    # cprint("{:^48}".format("Welcome stranger in DUNGEON GAME!"), 'red', 'on_grey')
    option()


main()


if __name__ == '__main__':
    main()
