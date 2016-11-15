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


def merchant():
    life_potions = 5
    print("Welcome in my shop.")
    print("I sell potions that restore your life.")
    print("One costs 30 gold coins")
    try:
        amount = int(input("How much do you want?: "))
        inv[gold_coins] - 30 * amount
        if amount> life_potions:
            print

    except ValueError:
        print("You need to give me some gold.")
    if life_potions == 0


