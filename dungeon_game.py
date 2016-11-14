import os
import time
os.system('clear')  # clear screen


def getch():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def gameboard(x=5, y=5, user_position=[1, 1]):
    x_user = user_position[1]
    y_user = user_position[0]
    table = []
    for row in range(x):
        table.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                table[row].append('#')
            elif row == x_user and column == y_user:
                table[row].append('@')
            else:
                table[row].append('.')
    return table


def display_gameboard(table):
    os.system('clear')  # clear screen
    for row in range(len(table)):
        print(' '.join(table[row]))


def user_move(user_position):
    print(user_position[0][0])
    return user_position

def main():
    user_coordinates = [3, 1]
    while True:
        display_gameboard(gameboard(10, 20, user_coordinates))
        #user_move(user_coordinates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
