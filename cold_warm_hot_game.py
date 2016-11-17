import random
import os
import time
from termcolor import colored, cprint


def intro_graphic():
    data = [line.strip() for line in open("cold_intro.txt", 'r')]
    for i in range(len(data)):
        if i == 0:
            print(" ", end='')
        if i == 2:
            print(" ", end='')
        # if i > 6:
        #     print("            ", end='')
        for j in range(len(data[i])):
            time.sleep(0.005)
            cprint("{}".format(data[i][j]), 'red', attrs=['bold'], end='')
        print()
    print()


def rand_num():
    i = 0
    rand_list = []
    while not i == 3:
        rand_list.append(random.randint(0, 9))
        i = len(set(rand_list))
    end_list = list(set(rand_list))
    if end_list[0] == 0:
        buffor = end_list[0]
        end_list[0] = end_list[1]
        end_list[1] = buffor
    return end_list[0], end_list[1], end_list[2]


def comparison_numbers(rand):
    """
    Converts the random number to list
    Cheks length and type of input
    Prints the result of the comparison
    """
    hot = 0
    warm = 0
    rand = list(rand)
    attempt = 0
    print(rand)
    while attempt < 10:
        user_input = list(input('\t\tGuess #{}: \n\t\t'.format(attempt+1)))
        try:
            int(user_input[0])
            int(user_input[1])
            int(user_input[2])
        except ValueError:
            print("\n\t\tYOU MUST INPUT DIGITS\n")
            continue
        if len(user_input) != 3 or (user_input[0] in user_input[1:]) or user_input[1] == user_input[2]:
            print("\n\t\tYOU MUST INPUT 3 OTHERS DIGITS\n")
            continue
        i = 0
        while i != 3:
            user_input[i] = int(user_input[i])
            i += 1
        if user_input == rand:
            hot = 3
            # return
        i = 0
        if hot != 3:
            hot = 0
            warm = 0
            while not i == 3:
                compare_num = rand.count(user_input[i])
                if compare_num > 0:
                    # if rand.index(user_input[i]) == i:
                    if rand[i] == user_input[i]:
                        hot += 1
                    else:
                        warm += 1
                i += 1
        print('\t\t', end='')
        if hot > 0:
            if hot == 3:
                print("HOT " * hot, end='')
                return 1
                attempt = 10
            else:
                print("HOT " * hot, end='')
        if warm > 0:
            print("WARM " * warm, end='')
        if hot == 0 and warm == 0:
            print('COLD', end=" ")
        print('\n')
        hot = 0
        warm = 0
        attempt += 1
    return 0


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


def run():
    os.system('clear')  # clear screen
    intro_graphic()
    time.sleep(2)
    print_intro()
    result = comparison_numbers(rand_num())
    if result == 1:
        os.system('clear')
        print("\n\n\t\tYOU WIN!!!\n\n")
        time.sleep(2)
    if result == 0:
        os.system('clear')
        print("\n\n\t\tYOU LOSE...\n\n")
        time.sleep(2)

# main()
