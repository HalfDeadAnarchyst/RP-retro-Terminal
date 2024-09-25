from settings import BREAKLINE
from utils.file_operations import load_csv
from utils.misc import output


def item(params):
    """Terminal command to show summarized of types of items of the ZONE or OWNER (check CSV)."""
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
                    output(BREAKLINE)
                    output(f" ZONE\t\t  {params[2].upper()}\n")
                    output(BREAKLINE)
                    for key in result:
                        output(f" {key:15}| AMOUNT: {result[key]:4}\n")
                    output(BREAKLINE)
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
                    output(BREAKLINE)
                    output(f" OWNER\t\t  {params[2].upper()}\n")
                    output(BREAKLINE)
                    for key in result:
                        output(f" {key:15}| AMOUNT: {result[key]:4}\n")
                    output(BREAKLINE)
                else:
                    output("No OWNER entry found, use HELP ITEM for detailed info\n")
            else:
                output("Enter name of the OWNER, use HELP ITEM for detailed info\n")
        else:
            output("Param unsupported. Use HELP ITEM or PING ITEM\n")
    else:
        output("No param received. Use HELP ITEM for detailed info\n")
