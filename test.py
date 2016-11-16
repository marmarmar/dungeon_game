
import collections

global inv
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


def add_to_inventory(loot):
    """it adding loot to current inventory"""
    inv = collections.Counter(inv)
    # collections module helps to add dictionaries value
    loot = collections.Counter(loot)
    inv = inv+loot



def merchant():
    global gold coins
    global inv
    global num_gameb
    life_potions = 5
    print("Welcome in my shop.")
    print("\nI sell potions that restore your life.")
    print("\nOne costs 30 gold coins")
    while True:
        if gold_coins >= 30:
        print("You can buy at least one")
        try:
           amount = int(input("\nHow much do you want?: ")
           if life_potions >= amount:
                if gold_coins >= amount * 30:
                    life_potions = ['life_potions'] * amount
                    gold_coins = gold_coins - 30 * amount
                    print(life_potions)
                    print("\nThank you for purchase.")
                    loot = life_potions*amount
                    add_to_inventory(loot)
                    num_gameb += 1
                    num_gameb -= 1
                    break
                else:
                    print("You don't have enough gold.")
            elif amount > life_potions:
                print("I do not have that many.")
        except ValueError:
            print("You need to give me some gold.")

weapon = ['sword', 'axe', 'dagger']
loot = random.choice(weapon)

print(loot)
