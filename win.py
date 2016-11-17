from termcolor import colored, cprint
import sys
import time
import os
os.system('clear')


def win_game():
    cprint("{:^100}".format("oooooo   oooo   .oooooo.   ooooo     ooo"), 'green', attrs=['bold'])
    cprint("{:^100}".format(" `888.   .8'   d8P'  `Y8b  `888'     `8'"), 'green', attrs=['bold'])
    cprint("{:^100}".format("  `888. .8'   888      888  888       8"), 'green', attrs=['bold'])
    cprint("{:^100}".format("   `888.8'    888      888  888       8"), 'green', attrs=['bold'])
    cprint("{:^100}".format("    `888'     888      888  888       8"), 'green', attrs=['bold'])
    cprint("{:^100}".format("     888      `88b    d88'  `88.    .8'"), 'green', attrs=['bold'])
    cprint("{:^100}".format("   o888o      `Y8bood8P'     `YbodP'\n"), 'green', attrs=['bold'])
    time.sleep(1)
    cprint("{:^100}".format(" oooooo   oooooo     oooo ooooo ooooo      ooo"), 'yellow', attrs=['bold'])
    cprint("{:^100}".format("  `888.    `888.     .8'  `888' `888b.     `8'"), 'yellow', attrs=['bold'])
    cprint("{:^100}".format("  `888.   .8888.   .8'    888   8 `88b.    8"), 'yellow', attrs=['bold'])
    cprint("{:^100}".format("   `888  .8'`888. .8'     888   8   `88b.  8"), 'yellow', attrs=['bold'])
    cprint("{:^100}".format("    `888.8'  `888.8'      888   8     `88b.8"), 'yellow', attrs=['bold'])
    cprint("{:^100}".format("     `888'    `888'       888   8       `888"), 'yellow', attrs=['bold'])
    cprint("{:^100}".format("       `8'      `8'       o888o o8o        `8\n"), 'yellow', attrs=['bold'])
    time.sleep(1)
    cprint("{:^100}".format("ooooooooooooo ooooo   ooooo oooooooooooo"), 'blue', attrs=['bold'])
    cprint("{:^100}".format("8'   888   `8 `888'   `888' `888'     `8"), 'blue', attrs=['bold'])
    cprint("{:^100}".format("888       888     888   888  "), 'blue', attrs=['bold'])
    cprint("{:^100}".format("  888       888ooooo888   888oooo8"), 'blue', attrs=['bold'])
    cprint("{:^100}".format(" 888       888     888   888    "), 'blue', attrs=['bold'])
    cprint("{:^100}".format("       888       888     888   888       o "), 'blue', attrs=['bold'])
    cprint("{:^100}".format("      o888o     o888o   o888o o888ooooood8\n"), 'blue', attrs=['bold'])
    time.sleep(1)
    cprint("{:^100}".format("    .oooooo.          .o.       ooo        ooooo oooooooooooo"), 'red', attrs=['bold'])
    cprint("{:^100}".format("   d8P'  `Y8b        .888.      `88.       .888' `888'     `8"), 'red', attrs=['bold'])
    cprint("{:^100}".format('  888               .8"888.      888b     d\'888   888        '), 'red', attrs=['bold'])
    cprint("{:^100}".format("  888              .8' `888.     8 Y88. .P  888   888oooo8    "), 'red', attrs=['bold'])
    cprint("{:^100}".format("  888     ooooo   .88ooo8888.    8  `888'   888   888        "), 'red', attrs=['bold'])
    cprint("{:^100}".format("  `88.    .88'   .8'     `888.   8    Y     888   888       o"), 'red', attrs=['bold'])
    cprint("{:^100}".format("   `Y8bood8P'   o88o     o8888o o8o        o888o o888ooooood8\n"), 'red', attrs=['bold'])
    time.sleep(1)
    # plays music from current folder
    os.system("aplay hobbit.wav")
    # os.system("aplay ~/kodowanie/dungeon_game/hobbit.wav")
    sys.exit()

win_game()
