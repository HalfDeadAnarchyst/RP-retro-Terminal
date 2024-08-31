import os
import sys
import time
import pygame

from commands import alarm, clear, diag, door, file, help, item, ping, selfdestruct, service

from settings import ENABLE_MUSIC, SELFDRSTRUCT_TIMER, SELFDRSTRUCT_ACTIVE, SELFDRSTRUCT_DEAD, START_SLEEP_TIME

from utils.file_operations import read_the_file
from utils.misc import output, param_extractor


# List of all available commands in the terminal. They're not showing in help
# Delete some commands if you don't want your players to use them
# Rename some commands at the left part of list if you want to
all_command_list = {
    "help": help,
    "diag": diag,
    "file": file,
    "clear": clear,
    "item": item,
    "ping": ping,
    "door": door,
    "alarm": alarm,
    "service": service,
    "selfdestruct": selfdestruct,
    "suicide": selfdestruct
}


# The Terminal main loop (no exit)
def main():
    while True:
        if SELFDRSTRUCT_ACTIVE:
            output(f"\n Time left: {SELFDRSTRUCT_TIMER}")
        if SELFDRSTRUCT_DEAD:
            time.sleep(10000)
        command = input("\n \\\\Root\\ >  ")
        command_parameters = param_extractor(command)
        first_word = command_parameters[0].lower()
        if first_word in all_command_list:
            all_command_list[first_word](command_parameters)
        else:
            output("\nCommand not found. Use HELP for HELP\n")


# TODO: load settings from file

if __name__ == "__main__":
    # platform-specific terminal clear previous terminal
    os.system("cls" if os.name == "nt" else "clear")

    # Time to give my player the laptop
    time.sleep(START_SLEEP_TIME)

    # Print welcome message
    read_the_file("hidden_data/startup.txt")

    # Play background MUTHUR music
    if ENABLE_MUSIC:
        pygame.mixer.music.play(999)

    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
