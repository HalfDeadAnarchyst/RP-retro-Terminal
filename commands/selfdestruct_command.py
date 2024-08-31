import os
import time

# for self-destruct non-blocking timer
from threading import Thread

from audio_manager import sound1

from settings import SELFDRSTRUCT_TIMER, SELFDRSTRUCT_ACTIVE, SELFDRSTRUCT_DEAD, SELFDRSTRUCT_PASSWORD_START, \
    SELFDRSTRUCT_PASSWORD_STOP, BREAKLINE
from telegram_integration import send_notification
from utils.misc import output


selfdestruct_state = {
    "timer": SELFDRSTRUCT_TIMER,
    "active": SELFDRSTRUCT_ACTIVE,
    "dead": SELFDRSTRUCT_DEAD,
    "password_start": SELFDRSTRUCT_PASSWORD_START,
    "password_stop": SELFDRSTRUCT_PASSWORD_STOP,
}


def destroy():
    output("bye")
    time.sleep(1)
    os.system("cls")
    send_notification(" Player commited suicide")
    while True:
        output("█")


def destroy_timer():
    while True:
        if selfdestruct_state["active"]:
            if selfdestruct_state["timer"] == 0:
                selfdestruct_state["active"] = False
                selfdestruct_state["dead"] = True
                sound1.set_volume(0)
                destroy()
                break
            else:
                time.sleep(1)
                selfdestruct_state["timer"] -= 1
        else:
            time.sleep(1)


def selfdestruct_thread_init():
    thread  = Thread(target=destroy_timer)
    thread .daemon = True
    thread .start()


def selfdestruct(params):
    if len(params) > 1:
        param1 = params[1].lower()
        if param1 == "timer":
            if len(params) > 2:
                param2 = params[2].lower()
                if param2.isnumeric():
                    selfdestruct_state["timer"] = int(param2)
                    send_notification(f"Player set self-destruct timer at {selfdestruct_state['timer']}")
                    output(f" Self-desctruct timer set to {selfdestruct_state['timer']} second(s)\n")
                else:
                    output(" Timer PARAM should be numeric\n")
            else:
                output(" Not enough PARAMs received, use HELP SELFDESTRUCT for HELP\n")
        elif param1 == "start" or param1 == "initiate":
            if selfdestruct_state["password_start"] != "":
                password = input(" PASSWORD required:  ")
                if password != selfdestruct_state["password_start"]:
                    output(" PASSWORD doesn't match. Abort\n")
                    return
            send_notification(" Player started self-destruct sequence")
            output(f" Self-destruct sequence initiated, time before end is {selfdestruct_state['timer']}\n")
            selfdestruct_state["active"] = True
            selfdestruct_thread_init()
        elif param1 == "stop" or param1 == "abort":
            if selfdestruct_state["password_start"] != "":
                password = input(" PASSWORD required:  ")
                if password != selfdestruct_state["password_stop"]:
                    output(" PASSWORD doesn't match. Abort\n")
                    return
            selfdestruct_state["active"] = False
            output(f" Self-destruct sequence aborted, time before end was {selfdestruct_state['timer']}\n")
            send_notification(" Player aborted self-destruct sequence")
            # Stop self destruct
        elif param1 == "status":
            output(BREAKLINE)
            output(f" TIMER = {selfdestruct_state['timer']} second(s)\n")
            if selfdestruct_state["password_start"] != "":
                output(f" PASSWORD is required to initiate sequence\n")
            else:
                output(f" PASSWORD is NOT required to initiate sequence\n")
            if selfdestruct_state["password_stop"] != "":
                output(f" PASSWORD is required to abort sequence\n")
            else:
                output(f" PASSWORD is NOT required to abort sequence\n")
            if selfdestruct_state["active"]:
                output(f" Sequence is ACTIVE, TIMER left before self-destruct: {selfdestruct_state['timer']}\n")
            else:
                output(f" Sequence is INACTIVE, no active TIMER\n")
            output(BREAKLINE)
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
