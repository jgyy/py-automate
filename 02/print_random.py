"""
print random
"""
from random import randint


def wrapper():
    """
    wrapper function
    """
    for _ in range(5):
        print(randint(1, 10))


if __name__ == "__main__":
    wrapper()
