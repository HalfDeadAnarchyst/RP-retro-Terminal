import os
import random
import time

from tqdm import tqdm

from settings import DECRYPTION_IS_SLOW, DECRYPTION_SPEED, DECRYPTION_SPEED_WAV, DECRYPTION_WAV_DIVIDER, DECRYPTION_LAG, \
    BREAKLINE
from telegram_integration import send_notification
from utils.misc import output


def load_csv(filename):
    """Loads CSV file into list of lists."""
    with open(f"hidden_data/{filename}.csv", "r", ) as file_:
        results = []
        for line in file_:
            if line[-1] == "\n":
                line = line[:-1]
            words = line.split(',')
            results.append(words)
    # print(results)
    return results


def replace_file_line(filename, search_line, replace_line):
    """Used in DOOR and SERVICES commands to save states. Replaces line in file."""
    with open(filename, "r", encoding = 'utf8') as change_file:
        buffer = change_file.read()
        buffer = buffer.replace(search_line, replace_line)
    with open(filename, "w", encoding = 'utf8') as change_file:
        change_file.write(buffer)


def read_the_file(filepath):
    """Reads the file to the terminal text output (.txt or .ascii)."""
    with open(filepath, "r", encoding = 'utf8') as read_file:
        output(read_file.read())


def is_file_password(filepath):
    """Shows if file need a password."""
    with open("hidden_data/files_passwords.txt", "r", encoding = 'utf8') as pass_file:
        passwords = {}
        for line in pass_file:
            if line != "\n":
                if line[-1] == "\n":
                    line = line[:-1]
                passwords.update({line.split(" ")[0]: line.split(" ")[1]})
    if filepath.split("/")[-1] in passwords:
        return True
    else:
        return False


def check_file_password(filepath):
    """If file for read has a password, this function will ask for this."""
    passwords = {}
    with open("hidden_data/files_passwords.txt", "r", encoding = 'utf8') as pass_file:
        for line in pass_file:
            if line != "\n":
                if line[-1] == "\n":
                    line = line[:-1]
                passwords.update({line.split(" ")[0]: line.split(" ")[1]})
    if filepath.split("/")[-1] in passwords:
        output(BREAKLINE)
        output("DATA CYPHED\n")
        user_password = input("INPUT DECYPHER CODE: ")
        size = os.path.getsize(filepath)
        # 5 lines below is slow password check
        if DECRYPTION_IS_SLOW:
            speed = DECRYPTION_SPEED
            if get_file_type(filepath.split('.', 1)[1]) == "AUDIOLOG":
                speed = DECRYPTION_SPEED_WAV
                size = size // DECRYPTION_WAV_DIVIDER
            for _ in tqdm(range(0, size),
                          desc = f"DECYPHING...",
                          bar_format = '{l_bar}{bar:20}{r_bar}{bar:-20b}'):  # shortens progress bar
                time.sleep(random.randrange(0, DECRYPTION_LAG) / speed)  # adjust speed of "decrypting"
        if user_password == passwords[filepath.split("/")[-1]]:
            output("ACCESS GRANTED\n")
            # Notify that player opened access to passworded file
            send_notification(f" Player opened protected file {filepath}")
            return True
        else:
            output("ACCESS DENIED\n")
            output(BREAKLINE)
            return False
    else:
        return True


def get_file_type(ending):
    """Translates windows .type into terminal lore format."""
    if ending == "txt":
        file_type = "TEXTLOG"
    elif ending == "wav":
        file_type = "AUDIOLOG"
    elif ending == "ascii":
        file_type = "IMAGE"
    else:
        file_type = "UNKWN FORMAT"
    return file_type
