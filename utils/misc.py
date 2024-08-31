import os
import random
import sys
import time

import pygame

from audio_manager import sound1
from settings import SLOW_LINE_SLEEP, SLOW_TYPE_SPEED, ENABLE_TYPEWRITER


def param_extractor(command):
    """Splits the command into parameters."""
    params = command.split(" ")
    if params[-1] == "":
        params.pop()
    return params


def output(text):
    """Slow typer for all prints, fancy output."""
    for line in text:
        for symbol in line:
            # comment line below to mute the sound
            if ENABLE_TYPEWRITER:
                pygame.mixer.find_channel(True).play(sound1)  # the typing sound, it SHOULD lag
            sys.stdout.write(symbol)
            sys.stdout.flush()
            time.sleep(random.random() * 10.0 / SLOW_TYPE_SPEED)
            if symbol == "\n":
                time.sleep(SLOW_LINE_SLEEP)


def get_wav_duration(filepath):
    """Gets duration of the WAV file in seconds and 1/10 of the seconds (45.4 sec will be 454) for TQDM."""
    with open(filepath, "r", errors="ignore") as wav_file:
        wav_file.seek(28)
        a = wav_file.read(4)
        byte_rate = 0
        for i in range(4):
            byte_rate = byte_rate + ord(a[i]) * pow(256, i)
        file_size = os.path.getsize(filepath)
        ms = ((file_size - 44) * 1000) / byte_rate
        return int((ms / 1000) // 0.1)
