
elif i == 11:
    total = 0
    # checks maximal length of names of loot and if it's to short for
    # good presentation change it to 9
    ordered = sorted(inv, key=inv.get, reverse=True)
    max_len = len(max(inv, key=len))
    if max_len < 9:
        max_len = 9
    # creates string which will been displays
    formatted_text = "{:>7}{:>%d}" % (max_len + 3)
    print(formatted_text.format("count", "item name"))
    print("-" * (10 + max_len))
    for i in ordered:
        print(formatted_text.format(inv[i], i))
        total += inv[i]
    print("-" * (10 + max_len))
    print("Total : {}\n".format(total))
