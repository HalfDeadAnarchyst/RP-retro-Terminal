# essentials
import os
import sys
import time
import random
# for sounds
import pygame
# for progress bars
from tqdm import tqdm
# for self-destruct non-blocking timer
from threading import Thread
# messenger integration
from telegram_integration import send_notification

# SETTINGS SECTION
# Things to set up audio for terminal
pygame.mixer.init(buffer = 2048)
pygame.mixer.set_num_channels(20)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("audio/mother.wav")
sound1 = pygame.mixer.Sound("audio/typewriter-key-even.wav")
sound1.set_volume(0.1)
enable_music = True
enable_typewriter = True

# Parameters for slow typer
slow_line_sleep = 0.15
slow_type_speed = 1000

# file password settings
decryption_is_slow = True
decryption_speed = 1000
decryption_wav_divider = 10000
decryption_speed_wav = 1000
decryption_lag = 10

# Self Destruct settings
selfdestruct_timer = 600
selfdestruct_password_start = "hackme12"
selfdestruct_password_stop = "hackme14"
selfdestruct_active = False
selfdestruct_dead = False

# sleep time before startup starts working
start_sleep_time = 5

# break line for terminal AND (!) diag file
breakline = "- - - - - - - - - - - - - - - - - - - - - - -\n"


# Functions section
def param_extractor(command):
    """Splits the command into parameters."""
    params = command.split(" ")
    if params[-1] == "":
        params.pop()
    return params


# slow typer for all prints, fancy output. Global variables for this at the top
def output(text):
    for line in text:
        for symbol in line:
            # comment line below to mute the sound
            if enable_typewriter:
                pygame.mixer.find_channel(True).play(sound1)  # the typing sound, it SHOULD lag
            sys.stdout.write(symbol)
            sys.stdout.flush()
            time.sleep(random.random() * 10.0 / slow_type_speed)
            if symbol == "\n":
                time.sleep(slow_line_sleep)


# loads CSV file into list of lists
def load_csv(filename):
    with open(f"hidden_data/{filename}.csv", "r", ) as file_:
        results = []
        for line in file_:
            if line[-1] == "\n":
                line = line[:-1]
            words = line.split(',')
            results.append(words)
    # print(results)
    return results


# Gets duration of the WAV file in seconds and 1/10 of the seconds (45.4 sec will be 454) for TQDM
def get_wav_duration(filepath):
    with open(filepath, "r", errors="ignore") as wav_file:
        wav_file.seek(28)
        a = wav_file.read(4)
        byte_rate = 0
        for i in range(4):
            byte_rate = byte_rate + ord(a[i]) * pow(256, i)
        file_size = os.path.getsize(filepath)
        ms = ((file_size - 44) * 1000) / byte_rate
        return int((ms / 1000) // 0.1)


# used in DOOR command to save states. Replaces line in file
def replace_file_line(filename, search_line, replace_line):
    with open(filename, "r", encoding = 'utf8') as change_file:
        buffer = change_file.read()
        buffer = buffer.replace(search_line, replace_line)
    with open(filename, "w", encoding = 'utf8') as change_file:
        change_file.write(buffer)


# reads the file to the terminal text output (.txt or .ascii)
def read_the_file(filepath):
    with open(filepath, "r", encoding = 'utf8') as read_file:
        output(read_file.read())


# shows if file need a password
def is_file_password(filepath):
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


# if file for read has a password, this function will ask for this
def check_file_password(filepath):
    passwords = {}
    with open("hidden_data/files_passwords.txt", "r", encoding = 'utf8') as pass_file:
        for line in pass_file:
            if line != "\n":
                if line[-1] == "\n":
                    line = line[:-1]
                passwords.update({line.split(" ")[0]: line.split(" ")[1]})
    if filepath.split("/")[-1] in passwords:
        output(breakline)
        output("DATA CYPHED\n")
        user_password = input("INPUT DECYPHER CODE: ")
        size = os.path.getsize(filepath)
        # 5 lines below is slow password check
        if decryption_is_slow:
            speed = decryption_speed
            if get_file_type(filepath.split('.', 1)[1]) == "AUDIOLOG":
                speed = decryption_speed_wav
                size = size//decryption_wav_divider
            for _ in tqdm(range(0, size),
                          desc = f"DECYPHING...",
                          bar_format = '{l_bar}{bar:20}{r_bar}{bar:-20b}'):  # shortens progress bar
                time.sleep(random.randrange(0, decryption_lag)/speed)  # adjust speed of "decrypting"
        if user_password == passwords[filepath.split("/")[-1]]:
            output("ACCESS GRANTED\n")
            # Notify that player opened access to passworded file
            send_notification(f" Player opened protected file {filepath}")
            return True
        else:
            output("ACCESS DENIED\n")
            output(breakline)
            return False
    else:
        return True


# translates windows .type into terminal lore format
def get_file_type(ending):
    if ending == "txt":
        file_type = "TEXTLOG"
    elif ending == "wav":
        file_type = "AUDIOLOG"
    elif ending == "ascii":
        file_type = "IMAGE"
    else:
        file_type = "UNKWN FORMAT"
    return file_type


# function to read/list the file(s), ask for password, or play audio file
def file(command):
    if len(command.split(' ', 1)) > 1:
        param = command.split(' ', 1)[1].lower()
        if param == "version":
            output("V 0.2.5\n")
            return
        elif param == "list":
            # got this from stackoverflow, gets list of files in directory
            file_list = [f for f in os.listdir("open_data") if os.path.isfile(os.path.join("open_data", f))]
            output(breakline)
            for file_ in file_list:
                file_type = get_file_type(file_.split('.', 1)[1])
                if is_file_password(file_):
                    is_pass = "LOCK"
                else:
                    is_pass = "OPEN"
                output(f" {file_.split('.', 1)[0]:32} | {file_type:12} | {is_pass}\n")
            output(breakline)
        else:
            # param is name of file
            param = command.split(' ', 1)[1]
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
                    output(breakline)
                    output(f" {file_[0].split('.', 1)[0]}\t\t | {file_type}\n")
                    output(breakline)
                    read_the_file(f"open_data/{file_[0]}")
                    output(f"\n")
                    output(breakline)
                # WAV files playing
                elif file_type == "AUDIOLOG":
                    output(breakline)
                    sound_data = pygame.mixer.Sound(f"open_data/{file_[0]}")
                    pygame.mixer.find_channel(True).play(sound_data)
                    dur = get_wav_duration(f"open_data/{file_[0]}")
                    for _ in tqdm(range(0, dur),
                                  desc = f"{file_[0].split('.', 1)[0]}",
                                  bar_format = '{l_bar}{bar:20}{r_bar}{bar:-20b}'):  # shortens progress bar
                        time.sleep(.1)
                    output(breakline)
                else:
                    output(breakline)
                    output(f"Unknown format, aborting read\n")
                    output(breakline)
    else:
        output("No param recieved. Use HELP FILE for detailed info\n")


# displays all of some parts of hidden shipdiag file, used for technical roleplay
def diag(command):
    if len(command.split(' ', 1)) > 1:
        param = command.split(' ', 1)[1].lower()
        if param == "version":
            output("V 0.17.2\n")
            return
        elif param == "all":
            read_the_file("hidden_data/shipdiag.txt")
        elif param == "list":
            with open("hidden_data/shipdiag.txt", "r") as read_file:
                state = 0
                output(breakline)
                for line in read_file:
                    if line == breakline:
                        state += 1
                    elif state == 2:
                        output(line)
                        state -= 2
                output(breakline)
            return
        else:
            # reads particular module of the file
            param = param.upper()
            state = 0  # 0 is param not found yet, 1 param is found and output is active, 2 block ended
            with open("hidden_data/shipdiag.txt", "r") as read_file:
                for line in read_file:
                    if line == breakline and state == 2:
                        state = 3
                        output(line)
                        break
                    if line == breakline and state == 1:
                        state = 2
                        output(line)
                    elif state == 1 or state == 2:
                        output(line)
                    elif line.startswith(f" {param}") and state == 0:
                        output(breakline)
                        state = 1
                        output(line)
            if state == 0:
                output("No DIAG entry found\n")
    else:
        output("No param recieved. Use HELP DIAG for detailed info\n")


# shows the player all information about normal/quest item, if player knows exact name of the item
def ping(command):
    params = param_extractor(command)
    if len(command.split(' ', 1)) > 1:
        param = command.split(' ', 1)[1].lower()
        if param == "version":
            output("V 0.75.0\n")
            return
        else:
            naming = []
            item_line = []
            for entry in load_csv("items"):
                if entry[0].upper() == "NAME":
                    naming = entry
                if entry[0] == command.split(' ', 1)[1].upper():
                    item_line.append(entry)
            if len(item_line) > 1:
                output("Multiple ping detected, triangulation aborted\n")
            elif len(item_line) < 1:
                output("No entry found, triangulation aborted\n")
            else:
                item_line = item_line[0]
                send_notification(f" Player pinged {item_line}")
                output(breakline)
                for i in range(0, len(naming)):
                    output(f" {naming[i].upper():12} {item_line[i]:12}\n")
                output(breakline)

    else:
        output("No param received. Use HELP PING for detailed info\n")


# shows summarized of types of items of the ZONE or OWNER (check CSV)
def item(command):
    params = param_extractor(command)
    if len(params) > 1:
        param = params[1].lower()
        if param == "version":
            output("V 0.75.0")
            return
        elif param == "zone":
            if len(params) > 2:
                result = {}
                for entry in load_csv("items"):
                    if entry[3] == params[2].upper():
                        if entry[2] in result:
                            result[entry[2]] = result[entry[2]] + int(entry[7])
                        else:
                            result[entry[2]] = int(entry[7])
                if result:
                    output(breakline)
                    output(f" ZONE\t\t  {params[2].upper()}\n")
                    output(breakline)
                    for key in result:
                        output(f" {key:15}| AMOUNT: {result[key]:4}\n")
                    output(breakline)
                else:
                    output("No ZONE entry found, use HELP ITEM for detailed info\n")
            else:
                output("Enter name of the ZONE, use HELP ITEM for detailed info\n")
        elif param == "owner":
            if len(params) > 2:
                result = {}
                for entry in load_csv("items"):
                    if entry[5] == params[2].upper():
                        if entry[2] in result:
                            result[entry[2]] = result[entry[2]] + int(entry[7])
                        else:
                            result[entry[2]] = int(entry[7])
                if result:
                    output(breakline)
                    output(f" OWNER\t\t  {params[2].upper()}\n")
                    output(breakline)
                    for key in result:
                        output(f" {key:15}| AMOUNT: {result[key]:4}\n")
                    output(breakline)
                else:
                    output("No OWNER entry found, use HELP ITEM for detailed info\n")
            else:
                output("Enter name of the OWNER, use HELP ITEM for detailed info\n")
        else:
            output("Param unsupported. Use HELP ITEM or PING ITEM\n")
    else:
        output("No param received. Use HELP ITEM for detailed info\n")


# displays HELP of HELP_{NAME} from hidden directory
def help(command):
    params = param_extractor(command)
    if len(params) > 1:
        if os.path.isfile(f"hidden_data/help_{params[1].lower()}.txt"):
            read_the_file(f"hidden_data/help_{params[1].lower()}.txt")
        else:
            output("No HELP about this command yet\n")
    else:
        read_the_file("hidden_data/help_message.txt")


# lets the player control some doors on the ship/station, or use some doors as puzzle
def door(command):
    if len(command.split(' ', 1)) > 1:
        param1 = command.split(' ', 1)[1].lower()
        door_list = load_csv("doors")
        if param1 == "version":
            output(" v.0.99.9\n")
        elif param1 == "list":
            output(breakline)
            output(f" {door_list[0][0]:12}{door_list[0][1]:12}{door_list[0][2]:12}\n")
            for airlock in door_list:
                if airlock[3] == "TRUE":
                    output(f" {airlock[0]:12}{airlock[1]:12}{airlock[2]:12}\n")
            output(breakline)
        elif len(command.split(' ', 2)) > 2:
            param1 = command.split(' ', 2)[1].lower()
            door_name = command.split(' ', 2)[2]
            if param1 == "open":
                result = f" door not found\n"
                for airlock in door_list:
                    if airlock[0] == door_name:
                        if airlock[5] == "NOMINAL":
                            if airlock[2] == "UNLOCKED":
                                if airlock[1] == "CLOSED":
                                    old_door_line = (str(airlock)[1:-1]).replace("'", "").replace(" ", "")
                                    new_door_line = old_door_line.replace("CLOSED", "OPENED")
                                    replace_file_line("hidden_data/doors.csv", old_door_line, new_door_line)
                                    send_notification(f" Player opened {airlock[0]}")
                                    result = f" {airlock[0]} OPENED\n"
                                else:
                                    result = f" {airlock[0]} is already OPENED\n"
                            else:
                                result = f" Magnet lock is active, can't OPEN\n"
                        else:
                            result = f" door malfunction and need repair, can't OPEN\n"
                output(result)
            elif param1 == "close":
                result = f" door not found\n"
                for airlock in door_list:
                    if airlock[0] == door_name:
                        if airlock[5] == "NOMINAL":
                            if airlock[2] == "UNLOCKED":
                                if airlock[1] == "OPENED":
                                    old_door_line = (str(airlock)[1:-1]).replace("'", "").replace(" ", "")
                                    new_door_line = old_door_line.replace("OPENED", "CLOSED")
                                    replace_file_line("hidden_data/doors.csv", old_door_line, new_door_line)
                                    send_notification(f" Player closed {airlock[0]}")
                                    result = f" {airlock[0]} CLOSED\n"
                                else:
                                    result = f" {airlock[0]} is already CLOSED\n"
                            else:
                                result = f" Magnet lock is active, can't CLOSE\n"
                        else:
                            result = f" door malfunction and need repair, can't CLOSE\n"
                output(result)
            elif param1 == "lock":
                result = f" door not found\n"
                for airlock in door_list:
                    if airlock[0] == door_name:
                        if airlock[5] == "NOMINAL":
                            if airlock[4] != "NONE":
                                output(breakline)
                                password = input(" PASSWORD required:  ")
                                if password != airlock[4]:
                                    output(" PASSWORD doesn't match. Abort\n")
                                    return
                            if airlock[2] == "UNLOCKED":
                                old_door_line = (str(airlock)[1:-1]).replace("'", "").replace(" ", "")
                                new_door_line = old_door_line.replace("UNLOCKED", "LOCKED")
                                replace_file_line("hidden_data/doors.csv", old_door_line, new_door_line)
                                send_notification(f" Player locked {airlock[0]}")
                                result = f" {airlock[0]} LOCKED\n"
                            else:
                                result = f" {airlock[0]} is already LOCKED\n"
                        else:
                            result = f" door malfunction and need repair, can't LOCK\n"
                output(result)
            elif param1 == "unlock":
                result = f" door not found\n"
                for airlock in door_list:
                    if airlock[0] == door_name:
                        if airlock[5] == "NOMINAL":
                            if airlock[4] != "NONE":
                                output(breakline)
                                password = input(" PASSWORD required:  ")
                                if password != airlock[4]:
                                    output(" PASSWORD not match. Abort")
                                    return
                            if airlock[2] == "LOCKED":
                                old_door_line = (str(airlock)[1:-1]).replace("'", "").replace(" ", "")
                                new_door_line = old_door_line.replace("LOCKED", "UNLOCKED")
                                replace_file_line("hidden_data/doors.csv", old_door_line, new_door_line)
                                send_notification(f" Player unlocked {airlock[0]}")
                                result = f" {airlock[0]} UNLOCKED\n"
                            else:
                                result = f" {airlock[0]} is already UNLOCKED\n"
                        else:
                            result = f" door malfunction and need repair, can't UNLOCK\n"
                output(result)
            elif param1 == "status":
                result = ""
                for airlock in door_list:
                    if airlock[0] == door_name:
                        if airlock[4] == "NONE":
                            password = "NONE"
                        else:
                            password = "PROTECTED"
                        result = f" {door_list[0][0]:20}{airlock[0]:12}\n" \
                                 f" {door_list[0][1]:20}{airlock[1]:12}\n" \
                                 f" {door_list[0][2]:20}{airlock[2]:12}\n" \
                                 f" {door_list[0][4]:20}{password:12}\n" \
                                 f" {door_list[0][5]:20}{airlock[5]:12}\n"
                        send_notification(f" Player checked status \n{result}")
                if result:
                    output(breakline)
                    output(result)
                    output(breakline)
                else:
                    output(" No door found\n")
            else:
                output(" PARAM not found, use HELP DOOR for HELP\n")
        else:
            output(" PARAM not found, use HELP DOOR for HELP\n")
    else:
        output(" Not enough PARAMs received, use HELP DOOR for HELP\n")


# set of complex command for fast reaction
def alarm(command):
    if len(command.split(' ', 1)) > 1:
        param = command.split(' ', 1)[1].lower()
        if param == "lockdown":
            locked_door_list = ''
            door_list = load_csv("doors")
            for airlock in door_list:
                if airlock[3] == "TRUE" and airlock[4] == "NONE":
                    output(f" Locking {airlock[0]}...                     \n")
                    old_door_line = (str(airlock)[1:-1]).replace("'", "").replace(" ", "")
                    new_door_line_temp = old_door_line.replace("OPENED", "CLOSED")
                    new_door_line = new_door_line_temp.replace("UNLOCKED", "LOCKED")
                    replace_file_line("hidden_data/doors.csv", old_door_line, new_door_line)
                    locked_door_list += f" {airlock[0]} "
            send_notification(f" Player ALARMed LOCKDOWN, closed and locked next doors:\n{locked_door_list}")
            output(breakline)
        elif param == "version":
            output(" v 0.45.1.54.192.11\n")
        else:
            output(" PARAM not found, use HELP ALARM for HELP\n")
    else:
        output(" Not enough PARAMs received, use HELP ALARM for HELP\n")


# allows player to switch some services DM might control
def service(command):
    if len(command.split(' ', 1)) > 1:
        param1 = command.split(' ', 2)[1].lower()
        service_list = load_csv("service")
        if param1 == "on" or param1 == "enable":
            result = f" Service not found\n"
            param2 = command.split(' ', 2)[2]
            if param2 != "":
                for service_ in service_list:
                    if service_[0] == param2:
                        if service_[3] != "NONE":
                            output(breakline)
                            password = input(" PASSWORD required:  ")
                            if password != service_[3]:
                                output(" PASSWORD mismatch. Abort\n")
                                output(breakline)
                                return
                        if service_[2] == "OK":
                            if service_[1] == "ON":
                                result = f"Service {service_[0]} already enabled\n"
                            else:
                                old_service_line = (str(service_)[1:-1]).replace("'", "").replace(" ", "")
                                new_service_line = old_service_line.replace("OFF", "ON")
                                replace_file_line("hidden_data/service.csv", old_service_line, new_service_line)
                                result = f"Service {service_[0]} enabled\n"
                                send_notification(f"Player activate service {service_[0]}")
                        else:
                            result = "Service hardware MALFUNCTION, can't toggle\n"
                output(result)
            else:
                output(" Please enter service name\n")
        elif param1 == "off" or param1 == "disable":
            result = f" Service not found\n"
            param2 = command.split(' ', 2)[2]
            if param2 != "":
                for service_ in service_list:
                    if service_[0] == param2:
                        if service_[3] != "NONE":
                            output(breakline)
                            password = input(" PASSWORD required:  ")
                            if password != service_[3]:
                                output(" PASSWORD mismatch. Abort\n")
                                output(breakline)
                                return
                        if service_[2] == "OK":
                            if service_[1] == "OFF":
                                result = f"Service {service_[0]} already disabled\n"
                            else:
                                old_service_line = (str(service_)[1:-1]).replace("'", "").replace(" ", "")
                                new_service_line = old_service_line.replace("ON", "OFF")
                                replace_file_line("hidden_data/service.csv", old_service_line, new_service_line)
                                result = f"Service {service_[0]} disable\n"
                                send_notification(f"Player deactivated service {service_[0]}")
                        else:
                            result = "Service hardware MALFUNCTION, can't toggle\n"
                output(result)
            else:
                output(" Please enter service name\n")
        elif param1 == "status":
            param2 = command.split(' ', 2)[2]
            if param2 != "":
                result = f" Service not found\n"
                for service_ in service_list:
                    if service_[0] == param2:
                        result = f"{breakline}" \
                                 f"{service_list[0][0]:20}|{service_list[0][1]:6}|{service_list[0][2]}\n" \
                                 f"{service_[0]:20}|{service_[1]:6}|{service_[2]}\n" \
                                 f"{breakline}"
                output(result)
            else:
                output(" Please enter service name\n")
        elif param1 == "list":
            output(breakline)
            for service_ in service_list:
                output(f"{service_[0]:20}|{service_[1]:6}\n")
            output(breakline)
        else:
            output(" PARAM not found, use HELP SERVICE for HELP\n")
    else:
        output(" Not enough PARAMs received, use HELP SERVICE for HELP\n")


# spams the screen, not allowing to proceed
def destroy():
    output("bye")
    time.sleep(1)
    os.system("cls")
    send_notification(" Player commited suicide")
    while True:
        output("█")


# background timer for self-destruct function
def destroy_timer():
    global selfdestruct_active
    global selfdestruct_timer
    global selfdestruct_dead
    while True:
        if selfdestruct_active:
            if selfdestruct_timer == 0:
                selfdestruct_active = False
                selfdestruct_dead = True
                sound1.set_volume(0)
                destroy()
                SelfDestructThread.start()
            else:
                time.sleep(1)
                selfdestruct_timer -= 1
        else:
            time.sleep(1)


# allows player to "destroy" everything
def selfdestruct(command):
    global selfdestruct_timer
    global selfdestruct_active
    global selfdestruct_password_start
    global selfdestruct_password_stop
    global selfdestruct_dead
    params = param_extractor(command)
    if len(params) > 1:
        param1 = params[1].lower()
        if param1 == "timer":
            if len(params) > 2:
                param2 = params[2].lower()
                if param2.isnumeric():
                    selfdestruct_timer = int(param2)
                    send_notification(f"Player set self-destruct timer at {selfdestruct_timer}")
                    output(f" Self-desctruct timer set to {selfdestruct_timer} second(s)\n")
                else:
                    output(" Timer PARAM should be numeric\n")
            else:
                output(" Not enough PARAMs received, use HELP SELFDESTRUCT for HELP\n")
        elif param1 == "start" or param1 == "initiate":
            if selfdestruct_password_start != "":
                password = input(" PASSWORD required:  ")
                if password != selfdestruct_password_start:
                    output(" PASSWORD doesn't match. Abort\n")
                    return
            send_notification(" Player started self-destruct sequence")
            output(f" Self-destruct sequence initiated, time before end is {selfdestruct_timer}\n")
            selfdestruct_active = True
            # Start self-destruct timer. How to control?
        elif param1 == "stop" or param1 == "abort":
            if selfdestruct_password_start != "":
                password = input(" PASSWORD required:  ")
                if password != selfdestruct_password_stop:
                    output(" PASSWORD doesn't match. Abort\n")
                    return
            selfdestruct_active = False
            output(f" Self-destruct sequence aborted, time before end was {selfdestruct_timer}\n")
            send_notification(" Player aborted self-destruct sequence")
            # Stop self destruct
        elif param1 == "status":
            output(breakline)
            output(f" TIMER = {selfdestruct_timer} second(s)\n")
            if selfdestruct_password_start != "":
                output(f" PASSWORD is required to initiate sequence\n")
            else:
                output(f" PASSWORD is NOT required to initiate sequence\n")
            if selfdestruct_password_stop != "":
                output(f" PASSWORD is required to abort sequence\n")
            else:
                output(f" PASSWORD is NOT required to abort sequence\n")
            if selfdestruct_active:
                output(f" Sequence is ACTIVE, TIMER left before self-destruct: {selfdestruct_timer}\n")
            else:
                output(f" Sequence is INACTIVE, no active TIMER\n")
            output(breakline)
        elif param1 == "pleasedie":
            output("bye")
            time.sleep(1)
            os.system("cls")
            send_notification(" Player commited suicide")
            while True:
                output("█")
        elif param1 == "version":
            output(" v4.8.15.16.23.42\n")
        else:
            output(" PARAM not found, use HELP SELFDESTRUCT for HELP\n")
    else:
        output(" Not enough PARAMs received, use HELP SELFDESTRUCT for HELP\n")


# clears the screen of any commands
def clear(command):
    params = param_extractor(command)
    if len(params) > 1:
        param1 = params[1].lower()
        if param1 == "version":
            output(" v1.0")
        else:
            output(" PARAM not found, use HELP CLEAR for HELP\n")
    else:
        os.system("cls")


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
        global selfdestruct_active
        global selfdestruct_timer
        global selfdestruct_dead
        if selfdestruct_active:
            output(f"\n Time left: {selfdestruct_timer}")
        if selfdestruct_dead:
            time.sleep(10000)
        command = input("\n \\\\Root\\ >  ")
        first_word = param_extractor(command)[0].lower()
        if first_word in all_command_list:
            all_command_list[first_word](command)
        else:
            output("\nCommand not found. Use HELP for HELP\n")


# TODO: load settings from file

# Clear previous terminal
os.system("cls")
# Time to give my player the laptop
time.sleep(start_sleep_time)
# Print welcome message
read_the_file("hidden_data/startup.txt")

# Play background MUTHUR music
if enable_music:
    pygame.mixer.music.play(999)

# self-destruct service
try:
    SelfDestructThread = Thread(target = destroy_timer)
    SelfDestructThread.daemon = True
    SelfDestructThread.start()
    # Launch the Terminal
    main()
except (KeyboardInterrupt, SystemExit):
    # cleanup_stop_thread()
    sys.exit()
