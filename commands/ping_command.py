from settings import BREAKLINE
from telegram_integration import send_notification
from utils.file_operations import load_csv
from utils.misc import output


def ping(params):
    """
    Terminal command to show the player all information about normal/quest item,
    if player knows exact name of the item.
    """
    if len(params) > 1:
        param = params[1].lower()
        if param == "version":
            output("V 0.75.0\n")
            return
        else:
            naming = []
            item_line = []
            for entry in load_csv("items"):
                if entry[0].upper() == "NAME":
                    naming = entry
                if entry[0] == params[1].upper():
                    item_line.append(entry)
            if len(item_line) > 1:
                output("Multiple ping detected, triangulation aborted\n")
            elif len(item_line) < 1:
                output("No entry found, triangulation aborted\n")
            else:
                item_line = item_line[0]
                send_notification(f" Player pinged {item_line}")
                output(BREAKLINE)
                for i in range(0, len(naming)):
                    output(f" {naming[i].upper():12} {item_line[i]:12}\n")
                output(BREAKLINE)

    else:
        output("No param received. Use HELP PING for detailed info\n")
