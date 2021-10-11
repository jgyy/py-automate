"""
coin flip
"""
from random import randint


def wrapper():
    """
    wrapper function
    """
    heads = 0
    for i in range(1, 1001):
        if randint(0, 1) == 1:
            heads = heads + 1
        if i == 500:
            print("Halfway done!")
    print("Heads came up " + str(heads) + " times.")


if __name__ == "__main__":
    wrapper()
