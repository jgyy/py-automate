"""
exit example
"""
import sys


def wrapper():
    """
    wrapper function
    """
    while True:
        print('Type exit to exit.')
        response = input()
        if response == 'exit':
            sys.exit()
        print('You typed ' + response + '.')


if __name__ == "__main__":
    wrapper()
