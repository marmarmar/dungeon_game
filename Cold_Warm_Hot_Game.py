import random
import os
from termcolor import colored, cprint


def rand_num():
    i = 0
    rand_list = []
    while not i == 3:
        rand_list.append(random.randint(0, 9))
        i = len(set(rand_list))
    end_list = list(set(rand_list))
    return end_list[0], end_list[1], end_list[2]


def comparison_numbers(rand):
    i = 0
    hot = 0
    warm = 0
    rand = list(rand)
    g = 0
    while g < 1:
        print(rand)
        user_input = list(input('Guess: '))
        while i != 3:
            user_input[i] = int(user_input[i])
            print(type(user_input[i]))
            print(type(rand[i]))
            i += 1
        if user_input == rand:
            hot = 3
            # return
        i = 0
        while not i == 3:
            compare_num = rand.count(user_input[i])
            if compare_num > 0:
                if rand.index(user_input[i]) == i:
                    hot += 1
                else:
                    warm += 1
            i += 1
        if hot == 3:
            print("HOT " * hot, end='')
            g = 1
        elif hot > 0:
            print("HOT " * hot, end='')
        if warm > 0:
            print("WARM " * warm, end='')
        if hot == 0 and warm == 0:
            print('COLD', end=" ")
        print()


def print_intro():
    print("\n\nI am thinking of a ", end='')
    cprint("3", 'green', end='')
    print('-digit number. Try to guess what it is.\n')
    print("Here are some clues:\n")
    print('When I say:    That means:\n')
    print("   Cold       No digit is correct.\n\n" +
          "   Warm       One digit is correct but in the wrong position.\n\n" +
          "   Hot        One digit is correct and in the right position.\n")
    print("I have thought up a number. You have ", end='')
    cprint("10", 'green', end=' ')
    print("guesses to get it.\n")


def main():
    os.system('clear')  # clear screen
    print_intro()
    while True:
        comparison_numbers(rand_num())


main()
