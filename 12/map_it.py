"""
Launches a map in the browser using an address from the command line or clipboard.
"""
import webbrowser
from sys import argv
from pyperclip import paste


def wrapper():
    """
    Get address from command line.
    Get address from clipboard.
    """
    if len(argv) > 1:
        address = ' '.join(argv[1:])
    else:
        address = paste()
    webbrowser.open('https://www.google.com/maps/place/' + address)


if __name__ == "__main__":
    wrapper()
