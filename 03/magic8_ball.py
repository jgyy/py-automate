"""
magic 8 ball
"""
from random import randint


def get_answer(answer_number):
    """
    wrapper function
    """
    answers = {
        1: "It is certain",
        2: "It is decidely decidedly so",
        3: "Yes",
        4: "Reply hazy try again",
        5: "Ask again later",
        6: "Concentrate and ask again",
        7: "My reply is no",
        8: "Outlook not so good",
        9: "Very doubtful",
    }
    return answers[answer_number]


if __name__ == "__main__":
    ran = randint(1, 9)
    FORTUNE = get_answer(ran)
    print(FORTUNE)
