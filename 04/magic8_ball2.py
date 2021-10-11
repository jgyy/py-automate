"""
magic 8 ball 2
"""
from random import randint


def wrapper():
    """
    wrapper function
    """
    messages = [
        "It is certain",
        "It is decidedly so",
        "Yes definitely",
        "Reply hazy try again",
        "Ask again later",
        "Concentrate and ask again",
        "My reply is no",
        "Outlook not so good",
        "Very doubtful",
    ]
    print(messages[randint(0, len(messages) - 1)])


if __name__ == "__main__":
    wrapper()
