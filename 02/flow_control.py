"""
Flow Control
"""
from random import randint


def wrapper1():
    """
    wrapper function part 1
    """
    spam = True
    print(spam)
    print(42 == 99)
    print(2 != 3)
    print("hello" == "hello")
    print("hello" == "Hello")
    print("dog" != "cat")
    print(True)
    print(42 == "42")
    print(42 < 100)
    print(42 > 100)

    egg_count = 42
    print(egg_count <= 42)
    my_age = 29
    print(my_age >= 10)
    print(True and True)
    print(True and False)
    print(False or True)
    print(False or False)
    print(not True)
    print((4 < 5) and (5 < 6))
    print((4 < 5) and (9 < 6))
    print((1 == 2) or True)
    print(2 + 2 == 4 and 2 + 2 != 5 and 2 * 2 == 2 + 2)

    name = "Mary"
    password = "swordfish"
    age = 3000
    if name == "Mary":
        print("Hello, Mary")
        if password == "swordfish":
            print("Access granted.")
        else:
            print("Wrong password.")
    if name == "Alice":
        print("Hi, Alice.")
    if name == "Alice":
        print("Hi, Alice.")
    else:
        print("Hello, stranger.")
    if name == "Alice":
        print("Hi, Alice.")
    elif age < 12:
        print("You are not Alice, kiddo.")


def wrapper2():
    """
    wrapper function part 2
    """
    name = "Carol"
    age = 3000
    if name == "Alice":
        print("Hi, Alice.")
    elif age < 12:
        print("You are not Alice, kiddo.")
    elif age > 2000:
        print("Unlike you, Alice is not an undead, immortal vampire.")
    elif age > 100:
        print("You are not Alice, grannie.")

    name = "Carol"
    age = 3000
    if name == "Alice":
        print("Hi, Alice.")
    elif age < 12:
        print("You are not Alice, kiddo.")
    elif age > 100:
        print("You are not Alice, grannie.")
    elif age > 2000:
        print("Unlike you, Alice is not an undead, immortal vampire.")

    name = "Carol"
    age = 3000
    if name == "Alice":
        print("Hi, Alice.")
    elif age < 12:
        print("You are not Alice, kiddo.")
    else:
        print("You are neither Alice nor a little kid.")
    spam = 0
    if spam < 5:
        print("Hello, world.")
        spam = spam + 1


def wrapper3():
    """
    wrapper function part 3
    """
    spam = 0
    while spam < 5:
        print("Hello, world.")
        spam = spam + 1
    name = ""
    while name != "name":
        print("Please type your '''name'''.")
        name = input()
    print("Thank you!")
    while True:
        print("Please type your '''name'''.")
        name = input()
        if name == "name":
            break
    print("Thank you!")
    while True:
        print("Who are you?")
        name = input()
        if name != "Joe":
            continue
        print("Hello, Joe. What is the password? (It is a fish.)")
        password = input()
        if password == "swordfish":
            break
    print("Access granted.")
    while not name:
        print("Enter your name:")
        name = input()
    print("How many guests will you have?")
    num_of_guests = int(input())
    if num_of_guests:
        print("Be sure to have enough room for all your guests.")
    print("Done")
    print("My name is")
    for i in range(5):
        print("Jimmy Five Times (" + str(i) + ")")
    total = 0
    for num in range(101):
        total = total + num
    print(total)


def wrapper4():
    """
    wrapper function part 4
    """
    print("My name is")
    i = 0
    while i < 5:
        print("Jimmy Five Times (" + str(i) + ")")
        i = i + 1
    for i in range(12, 16):
        print(i)
    for i in range(0, 10, 2):
        print(i)
    for i in range(5, -1, -1):
        print(i)
    for i in range(5):
        print(randint(1, 10))
    while True:
        print("Type exit to exit.")
        response = input()
        if response == "exit":
            break
        print("You typed " + response + ".")


def wrapper5():
    """
    wrapper function part 5
    """
    secret_number = randint(1, 20)
    print("I am thinking of a number between 1 and 20.")
    for guesses_taken in range(1, 7):
        print("Take a guess.")
        guess = int(input())
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break
    if guess == secret_number:
        print("Good job! You guessed my number in " + str(guesses_taken) + "guesses!")
    else:
        print("Nope. The number I was thinking of was " + str(secret_number))
    secret_number = randint(1, 20)
    print("I am thinking of a number between 1 and 20.")
    for guesses_taken in range(1, 7):
        print("Take a guess.")
        guess = int(input())
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break
    if guess == secret_number:
        print("Good job! You guessed my number in " + str(guesses_taken) + " guesses!")
    else:
        print("Nope. The number I was thinking of was " + str(secret_number))


def wrapper6():
    """
    wrapper function part 6
    """
    print("ROCK, PAPER, SCISSORS")
    wins = 0
    losses = 0
    ties = 0
    while True:
        print(f"{wins} Wins, {losses} Losses, %s {ties}")
        while True:
            print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
            player_move = input()
            if player_move in ("q", "r", "p", "s"):
                break
            print("Type one of r, p, s, or q.")
        if player_move == "r":
            print("ROCK versus...")
        elif player_move == "p":
            print("PAPER versus...")
        elif player_move == "s":
            print("SCISSORS versus...")
        random_number = randint(1, 3)
        if random_number == 1:
            print("ROCK")
        elif random_number == 2:
            print("PAPER")
        elif random_number == 3:
            print("SCISSORS")
        if randint(0, 9) >= 8:
            break


def wrapper7():
    """
    wrapper function part 7
    """
    print((5 > 4) and (3 == 5))
    print(5 <= 4)
    print((5 > 4) or (3 == 5))
    print(not ((5 > 4) or (3 == 5)))
    print((True and True) and False)
    print((not False) or (not True))
    spam = 0
    if spam == 10:
        print("eggs")
        if spam > 5:
            print("bacon")
        else:
            print("ham")
        print("spam")
    print("spam")


if __name__ == "__main__":
    wrapper1()
    wrapper2()
    wrapper3()
    wrapper4()
    wrapper5()
    wrapper6()
    wrapper7()
