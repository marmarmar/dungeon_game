import sys
import operator
from termcolor import colored, cprint


def main():
    cprint("Welcome stranger in DUNGEON GAME!", 'green', 'on_red')
    option()


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


main()
if __name__ == '__main__':
    main()
