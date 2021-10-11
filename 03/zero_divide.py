"""
zero divide
"""


def spam(divide_by):
    """
    wrapper function
    """
    return 42 / divide_by


if __name__ == "__main__":
    try:
        print(spam(2))
        print(spam(12))
        print(spam(0))
        print(spam(1))
    except ZeroDivisionError:
        print("Error: Invalid argument.")
