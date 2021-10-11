"""
factorial log
"""
from logging import debug, basicConfig, DEBUG


def factorial(num):
    """
    wrapper function
    """
    debug(f"Start of factorial({num})")
    total = 1
    for i in range(1, num + 1):
        total *= i
        debug("i is " + str(i) + ", total is " + str(total))
    debug(f"End of factorial({num})")
    return total


if __name__ == "__main__":
    basicConfig(level=DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    debug("Start of program")
    print(factorial(5))
    debug("End of program")
