"""
buggy adding program
"""


def wrapper():
    """
    wrapper function
    """
    print('Enter the first number to add:')
    first = input()
    print('Enter the second number to add:')
    second = input()
    print('Enter the third number to add:')
    third = input()
    print('The sum is ' + first + second + third)


if __name__ == "__main__":
    wrapper()
