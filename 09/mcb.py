"""
mcb.py - Saves and loads pieces of text to the clipboard.
Usage: py.exe mcb.py save <keyword> - Saves clipboard to keyword.
       py.exe mcb.py <keyword> - Loads keyword to clipboard.
       py.exe mcb.py list - Loads all keywords to clipboard.
"""
import shelve
from sys import argv
from pyperclip import copy, paste


def wrapper():
    """
    Save clipboard content.
    List keywords and load content.
    """
    mcb_shelf = shelve.open('mcb')
    if len(argv) == 3 and argv[1].lower() == 'save':
        mcb_shelf[argv[2]] = paste()
    elif len(argv) == 2:
        if argv[1].lower() == 'list':
            copy(str(list(mcb_shelf.keys())))
        elif argv[1] in mcb_shelf:
            copy(mcb_shelf[argv[1]])
    mcb_shelf.close()


if __name__ == "__main__":
    wrapper()
