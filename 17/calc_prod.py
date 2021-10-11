"""
calculate product
"""
from time import time


def wrapper():
    """
    Calculate the product of the first 100,000 numbers.
    """
    start_time = time()
    product = 1
    for i in range(1, 100000):
        product *= i
    end_time = time()
    print(f"The result is {len(str(product))} digits long.")
    print(f"Took {end_time - start_time} seconds to calculate.")


if __name__ == "__main__":
    wrapper()
