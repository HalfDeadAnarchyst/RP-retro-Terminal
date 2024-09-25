from settings import BREAKLINE
from telegram_integration import send_notification
from utils.file_operations import load_csv, replace_file_line
from utils.misc import output


def alarm(params):
    """Terminal command to set complex command for fast reaction."""
    if len(params) > 1:
        param = params[1].lower()
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
            output(BREAKLINE)
        elif param == "version":
            output(" v 0.45.1.54.192.11\n")
        else:
            output(" PARAM not found, use HELP ALARM for HELP\n")
    else:
        output(" Not enough PARAMs received, use HELP ALARM for HELP\n")
