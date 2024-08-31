import os
import time

import pygame
from tqdm import tqdm

from settings import BREAKLINE
from utils.file_operations import get_file_type, is_file_password, check_file_password, read_the_file
from utils.misc import output, get_wav_duration


def file(params):
    """Terminal command to read/list the file(s), ask for password, or play audio file."""
    if len(params) > 1:
        param = params[1].lower()
        if param == "version":
            output("V 0.2.5\n")
            return
        elif param == "list":
            # got this from stackoverflow, gets list of files in directory
            file_list = [f for f in os.listdir("open_data") if os.path.isfile(os.path.join("open_data", f))]
            output(BREAKLINE)
            for file_ in file_list:
                file_type = get_file_type(file_.split('.', 1)[1])
                if is_file_password(file_):
                    is_pass = "LOCK"
                else:
                    is_pass = "OPEN"
                output(f" {file_.split('.', 1)[0]:32} | {file_type:12} | {is_pass}\n")
            output(BREAKLINE)
        else:
            # param is name of file
            param = params[1]
            # gets list of files and appends them into the list
            file_ = [filename for filename in os.listdir("open_data") if filename.startswith(param)]
            if len(file_) > 1:
                output("More than one file found, specify\n")
            elif len(file_) < 1:
                output("No matches found, use FILE LIST or FILE HELP\n")
            else:
                file_type = get_file_type(file_[0].split('.', 1)[1])
                # check if file passworded
                if not check_file_password(f"open_data/{file_[0]}"):
                    return

                # printing TXT or ASCII-images
                if file_type == "TEXTLOG" or file_type == "IMAGE":
                    output(BREAKLINE)
                    output(f" {file_[0].split('.', 1)[0]}\t\t | {file_type}\n")
                    output(BREAKLINE)
                    read_the_file(f"open_data/{file_[0]}")
                    output(f"\n")
                    output(BREAKLINE)
                # WAV files playing
                elif file_type == "AUDIOLOG":
                    output(BREAKLINE)
                    sound_data = pygame.mixer.Sound(f"open_data/{file_[0]}")
                    pygame.mixer.find_channel(True).play(sound_data)
                    dur = get_wav_duration(f"open_data/{file_[0]}")
                    for _ in tqdm(range(0, dur),
                                  desc = f"{file_[0].split('.', 1)[0]}",
                                  bar_format = '{l_bar}{bar:20}{r_bar}{bar:-20b}'):  # shortens progress bar
                        time.sleep(.1)
                    output(BREAKLINE)
                else:
                    output(BREAKLINE)
                    output(f"Unknown format, aborting read\n")
                    output(BREAKLINE)
    else:
        output("No param recieved. Use HELP FILE for detailed info\n")
