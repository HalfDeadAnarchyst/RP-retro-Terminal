from settings import BREAKLINE
from telegram_integration import send_notification
from utils.file_operations import load_csv, replace_file_line
from utils.misc import output


def door(params):
    """Terminal command to let the player control some doors on the ship/station, or use some doors as puzzle."""
    if len(params) > 1:
        param1 = params[1].lower()
        door_list = load_csv("doors")
        if param1 == "version":
            output(" v.0.99.9\n")
        elif param1 == "list":
            output(BREAKLINE)
            output(f" {door_list[0][0]:12}{door_list[0][1]:12}{door_list[0][2]:12}\n")
            for airlock in door_list:
                if airlock[3] == "TRUE":
                    output(f" {airlock[0]:12}{airlock[1]:12}{airlock[2]:12}\n")
            output(BREAKLINE)
        elif len(params) > 2:
            param1 = params[1].lower()
            door_name = params[2]
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
                                output(BREAKLINE)
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
                                output(BREAKLINE)
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
                    output(BREAKLINE)
                    output(result)
                    output(BREAKLINE)
                else:
                    output(" No door found\n")
            else:
                output(" PARAM not found, use HELP DOOR for HELP\n")
        else:
            output(" PARAM not found, use HELP DOOR for HELP\n")
    else:
        output(" Not enough PARAMs received, use HELP DOOR for HELP\n")
