# ---------------------------------------------------------------------------------------
# Project                      : SPACE RACE
# Project collaborators        : Sogaand, Julian, Danny
# Project objective            : Creating a digital board game based in the Terminal
# Project documentation        :
# Last change preformed (Date) : 05/03/2024 15:45
# Last change preformed by     : Danny
# Last change (Description)    : Created the header for the .py files.
# ---------------------------------------------------------------------------------------

# Here we import the required functions, classes and dialogue
import player
import os
import time
import colorama
import dialogue
import random


def introscreen():
    intro = dialogue.intro_dialogue
    select_space_center = random.randint(0, 12)

    random_number = ""
    while len(random_number) != 5:
        random_int = random.randint(0, 9)
        random_number += str(random_int)

    space_port = colorama.Fore.GREEN + "SPACE CENTER: " + colorama.Fore.BLUE + dialogue.spaces_centers[select_space_center] + colorama.Fore.GREEN + " - COMMUNICATION SYSTEMS - COMMUNICATION POD: " + colorama.Fore.CYAN + "#" + random_number + colorama.Style.RESET_ALL

    underscore = ""
    while len(space_port) != len(underscore):
        underscore += "-"

    print(space_port)
    print(underscore)

    for i in intro:
        time.sleep(3)
        print(f"<{colorama.Fore.CYAN + "Unknown" + colorama.Style.RESET_ALL}> {i}")

    time.sleep(5)
    con_input = input("Press ENTER to continue...")
    print(f"<{colorama.Fore.RED + "SYSTEM" + colorama.Style.RESET_ALL}> {colorama.Fore.RED + "DELETING ALL MESSAGES" + colorama.Style.RESET_ALL}")
    time.sleep(5)

def menuscreen():
    game_logo = dialogue.game_logo

    # print(colorama.Back.BLUE + colorama.Fore.WHITE + f"{game_logo[0]}" + colorama.Style.RESET_ALL)
    # print(colorama.Back.RED + colorama.Fore.WHITE + f"{game_logo[1]}" + colorama.Style.RESET_ALL)
    # print(colorama.Back.MAGENTA + colorama.Fore.WHITE + f"{game_logo[2]}" + colorama.Style.RESET_ALL)
    # print(colorama.Back.CYAN + colorama.Fore.WHITE + f"{game_logo[3]}" + colorama.Style.RESET_ALL)
    # print(colorama.Back.BLUE + colorama.Fore.WHITE + f"{game_logo[4]}" + colorama.Style.RESET_ALL)

    print(colorama.Fore.BLUE + f"{game_logo[0]}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + f"{game_logo[1]}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + f"{game_logo[2]}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + f"{game_logo[3]}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE + f"{game_logo[4]}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + f"{game_logo[5]}" + colorama.Style.RESET_ALL)
    print(f"Project by: <{colorama.Fore.MAGENTA}Sogaand Momayez{colorama.Style.RESET_ALL}>, <{colorama.Fore.YELLOW}Julian Gonzalez Verbeek{colorama.Style.RESET_ALL}>, <{colorama.Fore.RED}Danny de Snoo{colorama.Style.RESET_ALL}>\n\n\n")


def dice_single():
    dice = random.randint(1, 6)
    return dice


def dice_multiple():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1,6)
    return dice1, dice2

