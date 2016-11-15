inv = {'gold coin': 210}


def sfinx():
    life = 3
    print("If you answer my riddle I will give you a ruby. If not, I will attack you!")
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
    print("\nI sell potions that restore your life.")
    print("\nOne costs 30 gold coins")
    amount = int(input("\nHow much do you want?: "))
    try:
        while life_potions >= amount:
            amount = int(input("How much do you want?: "))
            life_potions = life_potions - amount
            int(inv['gold coin']) - 30 * amount
            print("Thank you for purchase.")
        else:
            print("Not more than 5.")
    except ValueError:
        print("You need to give me some gold.")

merchant()
