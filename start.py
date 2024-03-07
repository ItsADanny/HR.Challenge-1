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
import functions
import os
import time
import colorama
import dialogue

players = []

functions.introscreen()
os.system("cls")
functions.menuscreen()

valid_player = False

while not valid_player:
    player_count = input("With how many player would you like to play? : ")
    if player_count.isnumeric() and 0 < int(player_count) <= 4:
        player_count = int(player_count)
        for i in range(player_count):
            temp_playername = input(f"Player {(i + 1)} what is your name? : ")
            new_player = player.Player()
            new_player.set_username(temp_playername)
            players.append(new_player)
        valid_player = True
    else:
        print("Invalid player count given, Please use a valid player count between 2 and 4")
        time.sleep(3)
        os.system("cls")
        functions.menuscreen()

# game_running = True
#
# while game_running:
#
