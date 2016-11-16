inv = {'gold coin': 300}


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
    while life_potions > 0 and inv["gold coin"] >= 30:
        try:
            amount = int(input("\nHow much do you want?: "))
            if life_potions >= amount:
                if inv["gold coin"] >= amount * 30:
                    life_potions = life_potions - amount
                    inv['gold coin'] = int(inv['gold coin']) - 30 * amount
                    print(inv)
                    print("\nThank you for purchase.")
                    print(life_potions)
                else:
                    print("You don't have enough gold.")
            else:
                print("I do not have that many.")
        except ValueError:
            print("You need to give me some gold.")
    if life_potions <1:
        print("\nYou bought everything I had to sell. Good luck on your journey!")
    else:
        print("\nSadly you don't have enough money to trade with me. Go away!")

    return inv

merchant()

def brandy():
    sfinx_graphic.print_sfinx()
