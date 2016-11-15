import collections



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
    """it adding loot to current inventory"""
    inv = collections.Counter(inv)
    # collections module helps to add dictionaries value
    loot = collections.Counter(loot)
    inv = inv+loot
    return inv



def merchant():
    inv = {'gold coin': 210}
    bottles = {'life_potions'}
    print("Welcome in my shop.")
    print("\nI sell potions that restore your life.")
    print("\nOne costs 30 gold coins")
    try:
        amount = input("\nHow much do you want?: ")
        bottles = int(amount)*bottles
        bottles = collections.Counter(bottles)
        inv = collections.Counter(inv)
        inv = inv+bottles
        print(inv)
    except ValueError:
        print("else")

merchant()
