import sys
import random
import os
import time


def clear():
    """clear screen"""
    os.system('clear')


def print_cap_da():
    print("\n     "+'\x1b[1;30;43m' +
          "{}\n".format(" ".join(random_capital_dashes)) + '\x1b[0m')


def print_full():
    print("\n     "+'\x1b[3;37;41m' + "{}\n".format(" ".join(CAPITOL_SAVE)) + '\x1b[0m')


def load_list():
    """loads capitals and graphics from files"""
    global capitals
    global graphics
    f = open('capitals.txt', 'r')
    f_graphics = open('hangman_graphic.txt', 'r')
    capitals = f.read().splitlines()
    graphics = f_graphics.read()
    f.close()
    f_graphics.close()


def create_dashes_capital():
    """
    1. Picks a random capital from list
    2. Converts random capital to uppercase
    3. Saves string to list
    4. Copy to new id
    5. Converts to dash list
    """
    global CAPITOL_SAVE
    global random_capital
    global random_capital_dashes
    random_capital = capitals[random.randrange(0, len(capitals))]  # 1
    random_capital = random_capital.upper()  # 2
    random_capital = list(random_capital)  # 3
    CAPITOL_SAVE = random_capital[:]  # 4
    random_capital_dashes = random_capital[:]
    for i in range(len(random_capital_dashes)):  # 5
        if random_capital_dashes[i] == " ":
            continue
        else:
            random_capital_dashes[i] = "_"
    hangman_graphic()


def check_user_input(n, x):
    """Check occurrence n in random_capital"""
    if len(n) == 1:
        count = random_capital.count(n)
        if count == 0:
            life()
            clear()
            hangman_graphic()
        else:
            for i in range(1, count+1):
                # looking for index of n in random_capital
                random_capital_dashes[random_capital.index(n)] = n
                # set n in random_capital to 0
                random_capital[random_capital.index(n)] = 0
            clear()
            hangman_graphic()
    else:
        n = list(n)
        if n == CAPITOL_SAVE:
            clear()
            hangman_graphic()
            print_full()
            print("You are GOOD!!")
            time.sleep(3)
            x = 1
            return x
        else:
            life()


def user_input():
    '''get user input and convert to upper'''
    print_cap_da()  # prints encrypted word
    global health
    global n
    global user_letter
    global user_word
    global space_key
    count = 0
    print("Your life : {}".format(health))  # print health
    get_user_input = input('Pick a letter or a word :\t')
    count = get_user_input.count(" ")  # counts spaces in input
    space_key = [0]*(count+1)
    # if word contains spaces deletes them and stores them in space_key
    if count > 0:
        for i in range(0, count):
            get_user_input = list(get_user_input)
            space_key[i] = get_user_input.index(" ")
            get_user_input.pop(space_key[i])
            get_user_input = "".join(get_user_input)

    # if input is a sequence of numbers repeat function user_input()
    if get_user_input.isdigit():
        clear()
        hangman_graphic()
        user_input()

    # checks whether it contains special characters
    elif get_user_input.isalnum() is False:
        clear()
        hangman_graphic()
        user_input()

    # user did not input
    elif len(get_user_input) < 1:
        user_input()

    # user input word
    elif len(get_user_input) >= 2:
        if count > 0:
            for i in range(0, count):
                get_user_input = list(get_user_input)
                get_user_input.insert(space_key[i]+i, " ")
                get_user_input = "".join(get_user_input)
        user_word = get_user_input
        user_word = user_word.upper()
        n = user_word

    # user input char
    elif len(get_user_input) == 1:
        user_letter = get_user_input
        user_letter = user_letter.upper()
        n = user_letter


def life():
    """subtracts 1 point from health"""
    global health
    health -= 1
    print("Sorry, you wrong.")
    time.sleep(1)
    clear()  # clear screen
    hangman_graphic()


def play_again():
    """asks if user want to play again"""
    if health == 0:
        clear()
        print_full()
        print("\tYou looosee...")
    x = input("Do you want to play again? (y/n):\t")
    if x == 'y':
        clear()
        main()
    else:
        clear()
        sys.exit()


def hangman_graphic():
    """
    shows graphics from list graphics[]
    '\x1b[6;30;42m' + ... + '\x1b[0m' - adds color to the string
    """
    global health
    if health == 5:
        print('\x1b[6;30;42m' + graphics[0:167] + '\x1b[0m')
    elif health == 4:
        print('\x1b[6;30;42m' + graphics[168:335] + '\x1b[0m')
    elif health == 3:
        print('\x1b[6;30;42m' + graphics[336:503] + '\x1b[0m')
    elif health == 2:
        print('\x1b[6;30;42m' + graphics[504:671] + '\x1b[0m')
    elif health == 1:
        print('\x1b[6;30;42m' + graphics[672:839] + '\x1b[0m')


def main(life, num_gameb):
    x = 0
    load_list()
    clear()
    # global num_gameb
    global health
    health = life
    create_dashes_capital()
    while health > 0:
        user_input()
        x = check_user_input(n, x)
        if x == 1:
            num_gameb += 1
            return health, num_gameb  # , num_gameb
        if CAPITOL_SAVE == random_capital_dashes:
            break
    return health, num_gameb


if __name__ == '__main__':
    main()
