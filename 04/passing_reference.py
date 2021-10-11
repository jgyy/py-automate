"""
passing reference
"""


def eggs(some_parameter):
    """
    wrapper function
    """
    some_parameter.append('Hello')
    return some_parameter


if __name__ == "__main__":
    spam = [1, 2, 3]
    spam = eggs(spam)
    print(spam)
