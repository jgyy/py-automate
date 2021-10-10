"""
Debugging
"""
from logging import (
    error,
    basicConfig,
    debug,
    info,
    warning,
    critical,
    disable,
    DEBUG,
    INFO,
    CRITICAL,
)
from os.path import dirname
from random import randint, choice
from traceback import format_exc

PATH = dirname(__file__) + "//"


def wrapper1():
    """
    wrapper function part 1
    """

    def box_print(symbol, width, height):
        try:
            if len(symbol) != 1:
                raise KeyError("Symbol must be a single character string.")
            if width <= 2:
                raise TabError("Width must be greater than 2.")
            if height <= 2:
                raise NameError("Height must be greater than 2.")
            print(symbol * width)
            for _ in range(height - 2):
                print(symbol + (" " * (width - 2)) + symbol)
            print(symbol * width)
        except (KeyError, TabError, NameError):
            print("NEXT!!!!")

    for sym, width, height in (("*", 4, 4), ("O", 20, 5), ("x", 1, 3), ("ZZ", 3, 3)):
        try:
            box_print(sym, width, height)
        except KeyError as err:
            print("An exception happened: " + str(err))
    try:
        raise TabError("This is the error message.")
    except TabError:
        with open(f"{PATH}error_info.txt", "w", encoding="utf-8") as error_file:
            error_file.write(format_exc())
            print("The traceback info was written to errorInfo.txt.")
    pod_bay_door_status = "open"
    assert pod_bay_door_status == "open", 'The pod bay doors need to be "open".'
    market_2nd = {"ns": "green", "ew": "red"}

    def switch_lights(stoplight):
        for key in stoplight.keys():
            if stoplight[key] == "green":
                stoplight[key] = "yellow"
            elif stoplight[key] == "yellow":
                stoplight[key] = "red"
            elif stoplight[key] == "red":
                stoplight[key] = "green"
        assert "yellow" in stoplight.values(), "Neither light is yellow! " + str(stoplight)

    switch_lights(market_2nd)
    basicConfig(level=DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
    debug("Start of program")

    def factorial(num):
        debug(f"Start of factorial({num})")
        total = 1
        for i in range(num + 1):
            total *= i
            debug("i is " + str(i) + ", total is " + str(total))
        debug(f"End of factorial({num})")
        return total

    print(factorial(5))


def wrapper2():
    """
    wrapper function part 2
    """
    debug("End of program")
    basicConfig(level=DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
    debug("Some debugging details.")
    info("The logging module is working.")
    warning("An error message is about to be logged.")
    error("An error has occurred.")
    critical("The program is unable to recover!")
    basicConfig(level=INFO, format=" %(asctime)s - %(levelname)s - %(message)s")
    critical("Critical error! Critical error!")
    disable(CRITICAL)
    critical("Critical error! Critical error!")
    error("Error! Error!")

    basicConfig(
        filename=f"{PATH}my_program_log.txt",
        level=DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    print("Enter the first number to add:")
    first = 1
    print("Enter the second number to add:")
    second = 2
    print("Enter the third number to add:")
    third = 3
    print(f"The sum is {first + second + third}")
    heads = 0

    for i in range(1, 1001):
        if randint(0, 1) == 1:
            heads = heads + 1
        if i == 500:
            print("Halfway done!")
    print("Heads came up " + str(heads) + " times.")

    guess = ""
    while guess not in ("heads", "tails"):
        print("Guess the coin toss! Enter heads or tails:")
        guess = choice(("heads", "tails"))
        toss = randint(0, 1)
        if toss == guess:
            print("You got it!")
        else:
            print("Nope! Guess again!")
            guess = choice(("heads", "tails"))
            if toss == guess:
                print("You got it!")
            else:
                print("Nope. You are really bad at this game.")


if __name__ == "__main__":
    wrapper1()
    wrapper2()
