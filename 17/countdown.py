"""
A simple countdown script.
"""
from os.path import dirname
from time import sleep
from subprocess import Popen


def wrapper():
    """
    At the end of the countdown, play a sound file.
    """
    path = dirname(__file__) + "\\"
    time_left = 10
    while time_left > 0:
        print(time_left, end="")
        sleep(1)
        time_left = time_left - 1
    with Popen(["start", f"{path}alarm.wav"], shell=True):
        print("alarm")


if __name__ == "__main__":
    wrapper()
