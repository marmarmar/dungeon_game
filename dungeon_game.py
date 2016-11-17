import sys
import os
import time
import gameboard
import random
import collections
import win
import sfinx_graphic
import hangman_game
import drunk
import sword
import ruby
import cold_warm_hot_game
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
    """
    Prints sorted table of inventory
    Lets to use items from inventory
    """
    os.system('clear')
    global inv
    global life
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
    print("'h' to use potion, 'p to use whisky' and 'q' to exit from inventory: ")
    use = input("r to see the ruby: ")
    # using inventory items
    while use != 'p' or use != 'q' or use != 'h' or use != 'r':
        if use == 'h':
            if 'life potions' in inv.keys():
                loot = ['life potions']
                remove_from_inventory(loot)
                life += 1
                print("press any key to exit")
                break
                x = getch()
            else:
                print("You don't have any life potions.")
                break
                x = getch()
        elif use == 'p':
            if 'whisky' in inv.keys():
                loot = ['whisky']
                remove_from_inventory(loot)
                os.system('clear')
                drunk.print_drunk()
                time.sleep(5)
                x = getch()
                break
            else:
                print("You don't have any whisky.")
                x = getch()
                break
        elif use == 'r':
            os.system('clear')
            ruby.print_ruby()
            time.sleep(5)
            x = getch()
            break
        elif use == 'q':
            break
            x = getch()
        else:
            use = input("I've already said 'p', 'r,', 'h' or 'q'!")


def sfinx(life):
    """
    Displays sphix graphic and asks user
    Wait for answer
    If answer is bad subtracts 1 life
    If answer is good adds ruby to inventory
    """
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
        add_to_inventory(loot)
        num_gameb += 1
        return life


def merchant():
    """NPC to buy life potions"""
    os.system('clear')
    global gold_coins
    global num_gameb
    life_potions = 5
    print_merchant()
    print("Welcome in my shop.")
    print("\nI sell potions that restore your life.")
    print("\nOne costs 30 gold coins")
    if gold_coins >= 30:
        print("You can buy at least one")
        while True:
            try:
                print("I've got 5 potions to sell.")
                amount = int(input("\nHow many do you want?(0 for exit): "))
                if life_potions >= amount:
                    if amount == 0:
                        break
                        num_gameb += 1
                        num_gameb -= 1
                    elif gold_coins >= amount * 30:

                        life_potions = ['life potions'] * amount
                        gold_coins = gold_coins - 30 * amount
                        loot = life_potions
                        print("\nThank you for purchase.")
                        loot = life_potions*amount
                        add_to_inventory(loot)
                        break
                        num_gameb += 1
                        num_gameb -= 1
                    else:
                        print("You don't have enough gold.")
            except ValueError:
                print("I will wait for serious offer.")
                time.sleep(3)
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
    checking_weight()


def checking_weight():
    global inv
    total = 0
    for i in inv:
        total += inv[i]
        if total > 3:
            print("You items are to heavy.")
            items = str(sum(inv.values()))
            # to delete unnecessery ''
            print("Inventory:")
            for key, value in inv.items():
                print('{}: {}'.format(value, key))
            print("Total number of items:", items)
            drop = input("Pick item to drop: ")
            while total > 3:
                try:
                    if drop in inv:
                        loot = [drop]
                        remove_from_inventory(loot)
                        checking_weight
                        break
                        getch()
                    elif drop not in inv:
                        print("There is no ", drop, "in your inventory.")
                        drop = input("Pick item to drop: ")
                    else:
                        print("what?")
                        drop = input("Pick item to drop: ")
                except ValueError:
                    print("what?")
                    drop = input("Pick item to drop: ")

def remove_from_inventory(loot):
    """it delete item from inventory"""
    global inv
    inv = collections.Counter(inv)
    # collections module helps to add dictionaries value
    loot = collections.Counter(loot)
    inv = inv-loot


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
    cprint("i to show inventory during the game, p use life potions", 'green', 'on_grey')
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
            cprint("{:^22}".format("GOLD COINS"), 'green', attrs=['bold'], end='')
        elif i == 3:
            cprint("{:^22}".format(gold_coins), 'green', attrs=['bold'], end='')
        elif i == 6:
            cprint("{:^22}".format("LIFES"), 'green', attrs=['bold'], end='')
        elif i == 7:
            cprint("{:^22}".format(life*'💗 '), 'red', attrs=['bold'], end='')
        elif i == 10:
            cprint("{:^22}".format("For ITEMS press 'i'"), 'green', attrs=['bold'], end='')
        else:
            print('{:>22}'.format(''), end='')
        for j in range(y):
            if table[i][j] == '🌴':
                cprint(table[i][j], 'yellow', end=' ')
            elif table[i][j] == '🞦':
                cprint(table[i][j], 'yellow', attrs=['bold'], end=' ')
            elif table[i][j] == '🔑':
                cprint(table[i][j], 'red', attrs=['bold'], end=' ')
            elif table[i][j] == '💰' or table[i][j] == '🎁':
                cprint(table[i][j], 'blue', attrs=['bold'], end=' ')
            elif table[i][j] == '😼':
                cprint(table[i][j], 'magenta', attrs=['bold'], end=' ')
            elif table[i][j] == '🟔' or table[i][j] == '🗡':
                cprint(table[i][j], 'green', attrs=['bold'], end=' ')
            elif table[i][j] == '🐵':
                cprint(table[i][j], 'white', end=' ')
            elif table[i][j] == '.':
                print('\033[1;30;8m' + "{}".format(table[i][j]) + '\033[0m', end=' ')
        print('')


def user_move(table, user_position):
    """
    Moves user and clears previous position
    Returns new table with new position with user
    When touch '?' going to boss level
    """
    global num_gameb
    last_position = user_position[:]
    x_user = user_position[0]
    y_user = user_position[1]
    move = getch()
    if move == 'd':
        x_user += 1
        # checks new position
        if table[y_user][x_user] == '🌴':
            x_user -= 1
        # removes @ from previous position
        table[y_user][x_user - 1] = '.'
    elif move == 'a':
        x_user -= 1
        if table[y_user][x_user] == '🌴':
            x_user += 1
        table[y_user][x_user + 1] = '.'
    elif move == 'w':
        y_user -= 1
        if table[y_user][x_user] == '🌴':
            y_user += 1
        table[y_user + 1][x_user] = '.'
    elif move == 's':
        y_user += 1
        if table[y_user][x_user] == '🌴':
            y_user -= 1
        table[y_user - 1][x_user] = '.'
    elif move == 'x':
        sys.exit()
    elif move == 'i':
        print_table()
    user_position[0] = x_user
    user_position[1] = y_user
    x = 0
    x = check_touch(table, user_position, last_position, x)
    if x != 0:
        user_position = x
        x_user = user_position[0]
        y_user = user_position[1]
    # sets @ on current position of user
    table[y_user][x_user] = '🐵'
    return user_position


def check_touch(table, user_position, last_position, x):
    """Checks if the user touches any item"""
    global num_gameb
    global gold_coins
    global life
    x_user = user_position[0]
    y_user = user_position[1]
    if table[y_user][x_user] == '🔑':
        num_gameb += 1
        return last_position
    elif table[y_user][x_user] == '🗡':
        # add ascii with weapon
        weapon = ['sword', 'axe', 'dagger']
        loot = [random.choice(weapon)]
        add_to_inventory(loot)
        os.system('clear')
        sword.print_sword()
        getch()
    elif table[y_user][x_user] == '💰':
        print_cash()
        gold_coins += random.randint(20, 50)
    elif table[y_user][x_user] == '🎁':
        loot = ['whisky']
        add_to_inventory(loot)
        print_whisky()
    elif table[y_user][x_user] == '🞦':
        merchant()
        return last_position
    elif table[y_user][x_user] == '😼':
        if 'sword' in inv.keys() or 'dagger' in inv.keys() or 'axe' in inv.keys():
            print_fight()
            loot = ['ruby']
            add_to_inventory(loot)
        else:
            print_fight()
            life -= 1
    elif table[y_user][x_user] == '🟔' and num_gameb == 1:
        # add ascii spell book
        loot = ['spell book']
        add_to_inventory(loot)
    elif table[y_user][x_user] == '🟔'and num_gameb == 4:
        loot = ['globe']
        add_to_inventory(loot)
    elif table[y_user][x_user] == '🟔'and num_gameb == 7:
        loot = ['abacus']
        add_to_inventory(loot)
    return x


def print_fight():
    os.system('clear')
    x = open("monster.txt", 'r')
    for line in x:
        cprint(line, "red", attrs=['bold'], end='')
    getch()


def print_whisky():
    os.system('clear')
    x = open("w.txt", 'r')
    for line in x:
        cprint(line, "yellow")
    getch()


def print_cash():
    os.system('clear')
    x = open("cash.txt", 'r')
    for line in x:
        cprint(line, "yellow")
    getch()

def print_merchant():
    os.system('clear')
    x = open("merchant.txt", 'r')
    for line in x:
        cprint(line, "yellow")



def random_elements(tab, *args):
    """randoms items to gameboard"""
    elements = ('🗡', '💰', '🎁', '🟔', '🔑', '🞦', '😼')
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
        #5 run hangman_game
        #6 create second gameboard
        #7 run third gameboard
        #8 move to cold_warm_hot_game
    """
    global gold_coins
    global num_gameb
    global inv
    global life
    life = 5
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
            user_coordinates = user_move(gameboard_table, user_coordinates)

        elif num_gameb == 2:
            # move to first boss
            if 'spell book' in inv.keys():
                life = sfinx(life)
            elif 'spell book' not in inv.keys():
                x = input("You don't have necessery item in your inventory. Search!")
                num_gameb -= 1

        elif num_gameb == 3:
            # creates new gameboard
            user_coordinates = [1, 1]
            gameboard_table = choice_gameboard(num_gameb, wide_gameboard, height_gameboard, user_coordinates)
            gameboard_table = random_elements(gameboard_table)
            num_gameb += 1

        elif num_gameb == 4:
            # run next level
            display_gameboard(wide_gameboard, height_gameboard, gameboard_table, life, gold_coins)
            user_coordinates = user_move(gameboard_table, user_coordinates)

        elif num_gameb == 5:
            # run hangman_game
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
            user_coordinates = user_move(gameboard_table, user_coordinates)

        elif num_gameb == 8:
            # move to last boss
            if 'spell book' in inv.keys():
                x = cold_warm_hot_game.run()
                if x == 1:
                    num_gameb += 1
                else:
                    num_gameb -= 1
                    life -= 1
            elif 'spell book' not in inv.keys():
                x = input("You don't have necessery item in your inventory. Search!")
                num_gameb -= 1

        elif num_gameb == 9:
            # win game
            win.win_game()


def main():
    intro_graphic()
    option()


main()


if __name__ == '__main__':
    main()
