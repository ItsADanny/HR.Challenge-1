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
import time
import colorama
import dialogue
import random


def introscreen():
    intro = dialogue.intro_dialogue
    select_space_center = random.randint(0, 12)

    random_number = ""
    if select_space_center != 12:
        while len(random_number) != 5:
            random_int = random.randint(0, 9)
            random_number += str(random_int)
    else:
        random_number = "69420"

    space_port = colorama.Fore.GREEN + "SPACE CENTER: " + colorama.Fore.BLUE + dialogue.spaces_centers[select_space_center] + colorama.Fore.GREEN + " - COMMUNICATION SYSTEMS - COMMUNICATION POD: " + colorama.Fore.CYAN + "#" + random_number + colorama.Style.RESET_ALL

    underscore = ""
    while len(space_port) != len(underscore):
        underscore += "-"

    print(space_port)
    print(underscore)
    print(
        f"<{colorama.Fore.BLUE + "SYSTEM" + colorama.Style.RESET_ALL}>  USER:<{colorama.Fore.CYAN + "Unknown" + colorama.Style.RESET_ALL}> CONNECTED TO COMMUNICATION SYSTEMS - ACCESS LEVEL: {colorama.Fore.RED}UNKNOWN{colorama.Style.RESET_ALL}")
    for i in intro:
        time.sleep(3)
        print(f"<{colorama.Fore.CYAN + "Unknown" + colorama.Style.RESET_ALL}> {i}")

    time.sleep(5)
    print(f"<{colorama.Fore.BLUE + "SYSTEM" + colorama.Style.RESET_ALL}>  USER:<{colorama.Fore.CYAN + "Unknown" + colorama.Style.RESET_ALL}> DISCONNECTED FROM COMMUNICATION SYSTEMS")
    time.sleep(5)
    con_input = input("Press ENTER to continue...")
    print(f"<{colorama.Fore.RED + "SYSTEM" + colorama.Style.RESET_ALL}>  {colorama.Fore.RED}ERROR{colorama.Style.RESET_ALL}: {colorama.Fore.RED}REMOTE SYSTEM BREACHED COMMUNICATIONS SYSTEM{colorama.Style.RESET_ALL}")
    time.sleep(2)
    print(f"<{colorama.Fore.RED + "SYSTEM" + colorama.Style.RESET_ALL}>  {colorama.Fore.RED}REMOTE COMMAND RECEIVED{colorama.Style.RESET_ALL}, COMMAND GIVEN: {colorama.Fore.RED}SUDO DELETE_MESSAGES{colorama.Style.RESET_ALL}, AUTHORITY: {colorama.Fore.MAGENTA}SYSTEM_ADMIN{colorama.Style.RESET_ALL}")
    print(f"<{colorama.Fore.RED + "SYSTEM" + colorama.Style.RESET_ALL}>  {colorama.Fore.RED + "DELETING ALL MESSAGES" + colorama.Style.RESET_ALL}")
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
    print(f"Version: 1.0 (07/03/2024)")
    print(f"Project by: <{colorama.Fore.MAGENTA}Sogaand Momayez{colorama.Style.RESET_ALL}>, <{colorama.Fore.YELLOW}Julian Gonzalez Verbeek{colorama.Style.RESET_ALL}>, <{colorama.Fore.RED}Danny de Snoo{colorama.Style.RESET_ALL}>\n\n\n")


def credits():
    credit = dialogue.intro_dialogue
    select_space_center = random.randint(0, 12)

    random_number = ""
    while len(random_number) != 5:
        random_int = random.randint(0, 9)
        random_number += str(random_int)

    space_port = colorama.Fore.GREEN + "SPACE STATION: " + colorama.Fore.BLUE + dialogue.spaces_centers[
        select_space_center] + colorama.Fore.GREEN + " - COMMUNICATION SYSTEMS - COMMUNICATION POD: " + colorama.Fore.CYAN + "#" + random_number + colorama.Style.RESET_ALL

    underscore = ""
    while len(space_port) != len(underscore):
        underscore += "-"


def rocketcheck(curr_player):
    players_rocketparts = curr_player.get_curr_rocketparts_list()

    heatshield = 0
    avionics = 0
    control_systems = 0
    fuel_tank = 0
    engines = 0
    fuselage = 0
    communication_system = 0
    unknown = 0

    for i in players_rocketparts:
        if i == "HEATSHIELD":
            heatshield += 1
        elif i == "AVIONICS":
            avionics += 1
        elif i == "CONTROL_SYSTEMS":
            control_systems += 1
        elif i == "FUEL_TANK":
            fuel_tank += 1
        elif i == "ENGINES":
            engines += 1
        elif i == "FUSELAGE":
            fuselage += 1
        elif i == "COMMUNICATION_SYSTEM":
            communication_system += 1
        else:
            unknown += 1

    if heatshield > 1 and avionics > 1 and control_systems > 1 and fuel_tank > 1 and engines > 1 and fuselage > 1 and communication_system > 1:
        return True
    else:
        return False


def rocketfuelcheck(curr_player):
    players_fuellevel = curr_player.get_curr_rocketparts_list()

    if players_fuellevel == 100:
        return True
    else:
        return False


def gen_board(player_list):
    print("BOARD")


def dice_single():
    dice = random.randint(1, 6)
    return dice
