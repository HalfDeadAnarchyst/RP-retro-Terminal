import os

from utils.misc import output


def clear(params):
    """Terminal command to clear the screen of any commands."""
    if len(params) > 1:
        param1 = params[1].lower()
        if param1 == "version":
            output(" v1.0")
        else:
            output(" PARAM not found, use HELP CLEAR for HELP\n")
    else:
        os.system("cls" if os.name == "nt" else "clear")
