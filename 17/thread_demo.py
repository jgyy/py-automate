"""
thread demo
"""
from time import sleep
from threading import Thread


def take_a_nap():
    """
    wrapper function
    """
    sleep(5)
    print("Wake up!")


if __name__ == "__main__":
    print("Start of program.")
    threadObj = Thread(target=take_a_nap)
    threadObj.start()
    print("End of program.")
