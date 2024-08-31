import os

from utils.file_operations import read_the_file
from utils.misc import output


def help(params):
    """Terminal command to display HELP of HELP_{NAME} from hidden directory."""
    if len(params) > 1:
        if os.path.isfile(f"hidden_data/help_{params[1].lower()}.txt"):
            read_the_file(f"hidden_data/help_{params[1].lower()}.txt")
        else:
            output("No HELP about this command yet\n")
    else:
        read_the_file("hidden_data/help_message.txt")
