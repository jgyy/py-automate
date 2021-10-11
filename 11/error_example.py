"""
error example
"""


def spam():
    """
    spam function
    """
    bacon()


def bacon():
    """
    bacon function
    """
    raise Exception("This is the error message.")


if __name__ == "__main__":
    spam()
