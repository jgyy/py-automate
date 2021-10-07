"""
Functions
"""
from random import randint
from time import sleep


def wrapper1():
    """
    wrapper function part 1
    """
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")

    def hello(name):
        print("Hello, " + name)

    hello("Alice")
    hello("Bob")

    def say_hello(name):
        print("Hello, " + name)

    say_hello("Al")

    def get_answer(answer_number):
        answers = {
            1: "It is certain",
            2: "It is decidedly so",
            3: "Yes",
            4: "Reply hazy try again",
            5: "Ask again later",
            6: "Concentrate and ask again",
            7: "My reply is no",
            8: "Outlook not so good",
            9: "Very doubtful",
        }
        return answers[answer_number]

    ran = randint(1, 9)
    fortune = get_answer(ran)
    print(fortune)
    ran = randint(1, 9)
    fortune = get_answer(ran)
    print(fortune)
    print(get_answer(randint(1, 9)))

    spam = print("Hello!")
    print(spam is None)
    print("Hello")
    print("World")
    print("Hello", end="")
    print("World")
    print("cats", "dogs", "mice")
    print("cats", "dogs", "mice", sep=",")


def wrapper2():
    """
    wrapper function part 2
    """

    def aaa():
        print("a() starts")
        bbb()
        ddd()
        print("a() returns")

    def bbb():
        print("b() starts")
        ccc()
        print("b() returns")

    def ccc():
        print("c() starts")
        print("c() returns")

    def ddd():
        print("d() starts")
        print("d() returns")

    aaa()
    bbb()
    ccc()
    ccc()
    bbb()
    ddd()
    ddd()
    aaa()
    eggs = 42

    def spam(divide_by=1):
        return 42 / divide_by

    def bacon():
        eggs = "bacon"
        print(eggs)

    def ham():
        print(eggs)

    spam()
    bacon()
    ham()
    print(eggs)
    try:
        print(spam(2))
        print(spam(12))
        print(spam(0))
        print(spam(1))
    except ZeroDivisionError:
        print("Error: Invalid argument.")

    indent = 0
    indent_increasing = True
    try:
        while True:
            print(" " * indent, end="")
            print("********")
            sleep(randint(0, 9) / 100)
            if indent_increasing:
                indent = indent + 1
                if indent == 20:
                    indent_increasing = False
            else:
                indent = indent - 1
                if indent == 0:
                    indent_increasing = True
    except KeyboardInterrupt:
        print("Exiting while loop")


if __name__ == "__main__":
    wrapper1()
    wrapper2()
