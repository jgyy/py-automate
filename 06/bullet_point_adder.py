"""
Adds Wikipedia bullet points to the start
of each line of text on the clipboard.
"""
from pyperclip import copy, paste


def wrapper():
    """
    Separate lines and add stars.
    loop through all indexes for "lines" list
    add star to each string in "lines" list
    """
    text = paste()
    lines = text.split("\n")
    for i, j in enumerate(lines):
        lines[i] = "* " + j
    text = "\n".join(lines)
    copy(text)
    print(text)


if __name__ == "__main__":
    copy(
        """
1234567890
1234567890
1234567890
1234567890
    """
    )
    wrapper()
