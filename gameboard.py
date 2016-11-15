def gameboard(x=5, y=5, user_position=[1, 1]):
    x_user = user_position[1]
    y_user = user_position[0]
    table = []
    for row in range(x):
        table.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1 or \
                    (row > 15 and row < 16 and column > 8 and column < 13) or \
                    (row > 7 and row < 10 and column > 5 and column < 8) or \
                    (row > 24 and row < 27 and column > 30 and column < 35) or \
                    (row > 5 and row < 10 and column > 20 and column < 30) or \
                    (row > 12 and row < 15 and column > 20 and column < 25) or \
                    (row < 2 and column > 12 and column < 17) or \
                    (row > 27 and row < 33 and column > 2 and column < 9):
                table[row].append('#')
            elif row == x_user and column == y_user:
                table[row].append('@')
            else:
                table[row].append('.')
    return table


def gameboard1(x=5, y=5, user_position=[1, 1]):
    x_user = user_position[1]
    y_user = user_position[0]
    table1 = []
    for row in range(x):
        table1.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1 or \
                    (row > 5 and row < 7 and column > 3 and column < 8) or \
                    (row > 22 and row < 28 and column > 22 and column < 33) or \
                    (row > 13 and row < 17 and column > 3 and column < 5) or \
                    (row > 5 and row < 10 and column > 34 and column < 37) or \
                    (row > 12 and row < 15 and column > 2 and column < 6) or \
                    (row < 4 and column > 12 and column < 17) or \
                    (row > 27 and row < 33 and column > 2 and column < 9):
                table1[row].append('#')
            elif row == x_user and column == y_user:
                table1[row].append('@')
            else:
                table1[row].append('.')
    return table1


def gameboard2(x=5, y=5, user_position=[1, 1]):
    x_user = user_position[1]
    y_user = user_position[0]
    table2 = []
    for row in range(x):
        table2.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1 or \
                    (row > 15 and row < 17 and column > 13 and column < 18) or \
                    (row > 22 and row < 28 and column > 12 and column < 23) or \
                    (row > 33 and row < 37 and column > 33 and column < 35) or \
                    (row > 5 and row < 10 and column > 34 and column < 37) or \
                    (row > 32 and row < 35 and column > 22 and column < 26) or \
                    (row < 4 and column > 7 and column < 12) or \
                    (row > 37 and row < 39 and column > 24 and column < 29):
                table2[row].append('#')
            elif row == x_user and column == y_user:
                table2[row].append('@')
            else:
                table2[row].append('.')
    return table2
