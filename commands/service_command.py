from settings import BREAKLINE
from telegram_integration import send_notification
from utils.file_operations import load_csv, replace_file_line
from utils.misc import output


def service(params):
    """Terminal command tp allow player to switch some services DM might control."""
    if len(params) > 1:
        param1 = params[1].lower()
        service_list = load_csv("service")
        if param1 == "on" or param1 == "enable":
            result = f" Service not found\n"
            if len(params) > 2:
                param2 = " ".join(params[2:])
                for service_ in service_list:
                    if service_[0] == param2:
                        if service_[3] != "NONE":
                            output(BREAKLINE)
                            password = input(" PASSWORD required:  ")
                            if password != service_[3]:
                                output(" PASSWORD mismatch. Abort\n")
                                output(BREAKLINE)
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
            if len(params) > 2:
                param2 = " ".join(params[2:])
                for service_ in service_list:
                    if service_[0] == param2:
                        if service_[3] != "NONE":
                            output(BREAKLINE)
                            password = input(" PASSWORD required:  ")
                            if password != service_[3]:
                                output(" PASSWORD mismatch. Abort\n")
                                output(BREAKLINE)
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
            if len(params) > 2:
                param2 = " ".join(params[2:])
                result = f" Service not found\n"
                for service_ in service_list:
                    if service_[0] == param2:
                        result = f"{BREAKLINE}" \
                                 f"{service_list[0][0]:20}|{service_list[0][1]:6}|{service_list[0][2]}\n" \
                                 f"{service_[0]:20}|{service_[1]:6}|{service_[2]}\n" \
                                 f"{BREAKLINE}"
                output(result)
            else:
                output(" Please enter service name\n")
        elif param1 == "list":
            output(BREAKLINE)
            for service_ in service_list:
                output(f"{service_[0]:20}|{service_[1]:6}\n")
            output(BREAKLINE)
        else:
            output(" PARAM not found, use HELP SERVICE for HELP\n")
    else:
        output(" Not enough PARAMs received, use HELP SERVICE for HELP\n")
