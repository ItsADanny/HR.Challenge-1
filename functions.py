# ---------------------------------------------------------------------------------------
# Project                      : SPACE RACE
# Project collaborators        : Sogaand, Julian, Danny
# Project objective            : Creating a digital board game based in the Terminal
# Project documentation        :
# Last change preformed (Date) : 05/03/2024 15:45
# Last change preformed by     : Danny
# Last change (Description)    : Created the header for the .py files.
# ---------------------------------------------------------------------------------------

# Here we import the required functions and classes
import player
import os
import time
import colorama
import dialogue


def introscreen():
    intro = dialogue.intro_dialogue

    for i in intro:
        time.sleep(3)
        print(f">{i}")

    time.sleep(5)
    os.system("cls")

def menuscreen():
    game_logo = dialogue.game_logo
