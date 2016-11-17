from termcolor import colored, cprint
import sys
import random
import time
import os
os.system('clear')


def check_life(life):
    if life == 0:
        game_over()


def game_over():
    for i in range(20):
        col = ['red', 'yellow']
        x = random.randint(0, 1)
        os.system('clear')
        time.sleep(0.1)

        cprint("{:^100}".format(" @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@"), col[x], attrs=['bold'])
        cprint("{:^100}".format("@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@"), col[x], attrs=['bold'])
        cprint("{:^100}".format("!@@        @@!  @@@  @@! @@! @@!  @@!     "), col[x], attrs=['bold'])
        cprint("{:^100}".format("!@!        !@!  @!@  !@! !@! !@!  !@!     "), col[x], attrs=['bold'])
        cprint("{:^100}".format("!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!  "), col[x], attrs=['bold'])
        cprint("{:^100}".format("!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:  "), col[x], attrs=['bold'])
        cprint("{:^100}".format(":!!   !!:  !!:  !!!  !!:     !!:  !!:     "), col[x], attrs=['bold'])
        cprint("{:^100}".format(":!:   !::  :!:  !:!  :!:     :!:  :!:     "), col[x], attrs=['bold'])
        cprint("{:^100}".format(" ::: ::::  ::   :::  :::     ::    :: ::::"), col[x], attrs=['bold'])
        cprint("{:^100}".format(" :: :: :    :   : :   :      :    : :: :: "), col[x], attrs=['bold'])

        cprint("{:^100}".format(" @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@ "), col[x], attrs=['bold'])
        cprint("{:^100}".format("@@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@"), col[x], attrs=['bold'])
        cprint("{:^100}".format("@@!  @@@  @@!  @@@  @@!       @@!  @@@"), col[x], attrs=['bold'])
        cprint("{:^100}".format("!@!  @!@  !@!  @!@  !@!       !@!  @!@"), col[x], attrs=['bold'])
        cprint("{:^100}".format("@!@  !@!  @!@  !@!  @!!!:!    @!@!!@! "), col[x], attrs=['bold'])
        cprint("{:^100}".format("!@!  !!!  !@!  !!!  !!!!!:    !!@!@!  "), col[x], attrs=['bold'])
        cprint("{:^100}".format("!!:  !!!  :!:  !!:  !!:       !!: :!! "), col[x], attrs=['bold'])
        cprint("{:^100}".format(":!:  !:!   ::!!:!   :!:       :!:  !:!"), col[x], attrs=['bold'])
        cprint("{:^100}".format("::::: ::    ::::     :: ::::  ::   :::"), col[x], attrs=['bold'])
        cprint("{:^100}".format(" : :  :      :      : :: ::    :   : :"), col[x], attrs=['bold'])
        time.sleep(0.1)
    sys.exit()
