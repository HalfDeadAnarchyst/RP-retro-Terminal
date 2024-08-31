from settings import BREAKLINE
from utils.file_operations import read_the_file
from utils.misc import output


def diag(params):
    """Terminal command to display all of some parts of hidden shipdiag file, used for technical roleplay."""
    if len(params) > 1:
        param = params[1].lower()
        if param == "version":
            output("V 0.17.2\n")
            return
        elif param == "all":
            read_the_file("hidden_data/shipdiag.txt")
        elif param == "list":
            with open("hidden_data/shipdiag.txt", "r") as read_file:
                state = 0
                output(BREAKLINE)
                for line in read_file:
                    if line == BREAKLINE:
                        state += 1
                    elif state == 2:
                        output(line)
                        state -= 2
                output(BREAKLINE)
            return
        else:
            # reads particular module of the file
            param = param.upper()
            state = 0  # 0 is param not found yet, 1 param is found and output is active, 2 block ended
            with open("hidden_data/shipdiag.txt", "r") as read_file:
                for line in read_file:
                    if line == BREAKLINE and state == 2:
                        state = 3
                        output(line)
                        break
                    if line == BREAKLINE and state == 1:
                        state = 2
                        output(line)
                    elif state == 1 or state == 2:
                        output(line)
                    elif line.startswith(f" {param}") and state == 0:
                        output(BREAKLINE)
                        state = 1
                        output(line)
            if state == 0:
                output("No DIAG entry found\n")
    else:
        output("No param recieved. Use HELP DIAG for detailed info\n")
