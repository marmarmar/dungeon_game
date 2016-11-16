def merchant():
    global gold coins
    global inv
    global num_gameb
    loot =['life_potions']
    life_potions = 5
    print("Welcome in my shop.")
    print("\nI sell potions that restore your life.")
    print("\nOne costs 30 gold coins")
    amount = int(input("\nHow much do you want?: "))
    if life_potions >= amount:
        if inv["gold coin"] >= amount * 30:
            life_potions = life_potions * amount
            gold_coins = gold_coins - 30 * amount
            print(inv)
            print("\nThank you for purchase.")
            print(life_potions)
            loot = ['life_potions']*amount
            add_to_inventory(loot)
            num_gameb -= 1
        else:
            print("You don't have enough gold.")
    elif ValueError:
        print("You need to give me some gold.")
    else:
        print("I do not have that many.")
