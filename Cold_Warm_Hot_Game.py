import random


def rand_num():
    i = 0
    rand_list = []
    while not i == 3:
        rand_list.append(random.randint(0, 9))
        i = len(set(rand_list))
    end_list = list(set(rand_list))
    return end_list[0], end_list[1], end_list[2]


def eval_numbers(rand):
    i = 0
    user_input = list(input('SHOOT!!'))
    # while
    # user_input = list(user_input)

    while not i == 3:
        compare_num = rand.count(user_input[i])
        if compare_num > 0:
            if rand.index(user_input[i]) == i:
                print('HOT', end=" ")
            else:
                print('WARM', end=" ")
        else:
            print('COLD', end=" ")
        i += 1

print(rand_num())
print(type(rand_num()))


def main():
    while True:
        eval_numbers(rand_num())


main()
