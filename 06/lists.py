"""
Lists
"""
from random import randint, shuffle, choice
from time import sleep
from copy import copy, deepcopy


def wrapper1():
    """
    wrapper function part 1
    """
    print([1, 2, 3])
    print(["cat", "bat", "rat", "elephant"])
    print(["hello", 3.1415, True, None, 42])
    spam = ["cat", "bat", "rat", "elephant"]

    print(spam)
    print(spam[0])
    print(spam[1])
    print(spam[2])
    print(spam[3])
    print(["cat", "bat", "rat", "elephant"][3])
    print("Hello, " + spam[0])
    print("The " + spam[1] + " ate the " + spam[0] + ".")

    spam = ["cat", "bat", "rat", "elephant"]
    print(spam[1])
    print(spam[int(1.0)])
    spam = [["cat", "bat"], [10, 20, 30, 40, 50]]
    print(spam[0])
    print(spam[0][1])
    print(spam[1][4])
    print(spam[-1])

    spam = ["cat", "bat", "rat", "elephant"]
    print(spam[0:4])
    print(spam[1:3])
    print(spam[0:-1])
    spam = ["cat", "bat", "rat", "elephant"]
    print(spam[:2])
    print(spam[1:])
    print(spam[:])

    spam = ["cat", "dog", "moose"]
    print(len(spam))
    spam = ["cat", "bat", "rat", "elephant"]
    spam[1] = "aardvark"
    print(spam)
    spam[2] = spam[1]
    print(spam)
    spam[-1] = 12345

    print(spam)
    print([1, 2, 3] + ["A", "B", "C"])
    print(["X", "Y", "Z"] * 3)
    spam = [1, 2, 3]
    spam = spam + ["A", "B", "C"]
    print(spam)
    spam = ["cat", "bat", "rat", "elephant"]
    del spam[2]
    print(spam)
    del spam[2]
    print(spam)


def wrapper2():
    """
    wrapper function part 2
    """
    cat_name1 = "Zophie"
    cat_name2 = "Pooka"
    cat_name3 = "Simon"
    cat_name4 = "Lady Macbeth"
    cat_name5 = "Fat-tail"
    cat_name6 = "Miss Cleo"
    print("Enter the name of cat 1:")
    print("Enter the name of cat 2:")
    print("Enter the name of cat 3:")
    print("Enter the name of cat 4:")
    print("Enter the name of cat 5:")
    print("Enter the name of cat 6:")
    print("The cat names are:")
    print(
        cat_name1
        + " "
        + cat_name2
        + " "
        + cat_name3
        + " "
        + cat_name4
        + " "
        + cat_name5
        + " "
        + cat_name6
    )

    cat_names = []
    while True:
        print(
            "Enter the name of cat "
            + str(len(cat_names) + 1)
            + " (Or enter nothing to stop.):"
        )
        name = input()
        if name == "":
            break
        cat_names = cat_names + [name]
    print("The cat names are:")
    for name in cat_names:
        print("  " + name)
    for i in range(4):
        print(i)
    for i in [0, 1, 2, 3]:
        print(i)
    supplies = ["pens", "staplers", "flamethrowers", "binders"]
    for i, j in enumerate(supplies):
        print("Index " + str(i) + " in supplies is: " + j)


def wrapper3():
    """
    wrapper function part 3
    """
    print("howdy" in ["hello", "hi", "howdy", "heyas"])
    spam = ["hello", "hi", "howdy", "heyas"]
    print("cat" in spam)
    print("howdy" not in spam)
    print("cat" not in spam)
    my_pets = ["Zophie", "Pooka", "Fat-tail"]
    print("Enter a pet name:")
    name = "test"

    if name not in my_pets:
        print("I do not have a pet named " + name)
    else:
        print(name + " is my pet.")
    supplies = ["pens", "staplers", "flamethrowers", "binders"]
    for index, item in enumerate(supplies):
        print("Index " + str(index) + " in supplies is: " + item)

    pets = ["Dog", "Cat", "Moose"]
    print(choice(pets))
    people = ["Alice", "Bob", "Carol", "David"]
    shuffle(people)
    print(people)
    shuffle(people)
    print(people)

    spam = 42
    spam = spam + 1
    print(spam)
    spam = 42
    spam += 1
    print(spam)
    spam += 1
    spam = spam + 1
    spam -= 1
    spam = spam - 1
    spam *= 1
    spam = spam * 1
    spam /= 1
    spam = spam / 1
    spam %= 1
    spam = spam % 1
    print(spam)
    spam = "Hello,"
    spam += " world!"
    print(spam)


def wrapper4():
    """
    wrapper function part 4
    """
    bacon = ["Zophie"]
    bacon *= 3
    print(bacon)
    spam = ["hello", "hi", "howdy", "heyas"]
    print(spam.index("hello"))
    print(spam.index("heyas"))
    spam = ["Zophie", "Pooka", "Fat-tail", "Pooka"]
    print(spam.index("Pooka"))
    spam = ["cat", "dog", "bat"]
    spam.append("moose")
    print(spam)
    spam = ["cat", "dog", "bat"]
    spam.insert(1, "chicken")
    print(spam)

    eggs = "hello"
    print(eggs)
    bacon = 42
    spam = ["cat", "bat", "rat", "elephant"]
    spam.remove("bat")
    print(spam)
    spam = ["cat", "bat", "rat", "elephant"]
    spam = ["cat", "bat", "rat", "cat", "hat", "cat"]
    spam.remove("cat")
    print(spam)
    spam = [2, 5, 3.14, 1, -7]
    spam.sort()
    print(spam)
    spam = ["ants", "cats", "dogs", "badgers", "elephants"]
    spam.sort()
    print(spam)

    spam.sort(reverse=True)
    print(spam)
    spam = [1, 3, 2, 4, "Alice", "Bob"]
    spam = ["Alice", "ants", "Bob", "badgers", "Carol", "cats"]
    spam.sort()
    print(spam)
    spam = ["a", "z", "A", "Z"]
    spam.sort(key=str.lower)
    print(spam)
    spam = ["cat", "dog", "moose"]
    spam.reverse()
    print(spam)
    spam = ["apples", "oranges", "bananas", "cats"]
    print(spam)
    print("Four score and seven " + "years ago...")


def wrapper5():
    """
    wrapper function part 5
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

    name = "Zophie"
    print(name[0])
    print(name[-2])
    print(name[0:4])
    print("Zo" in name)
    print("z" in name)
    print("p" not in name)
    for i in name:
        print("* * * " + i + " * * *")

    name = "Zophie a cat"
    name = "Zophie a cat"
    new_name = name[0:7] + "the" + name[8:12]
    print(name)
    print(new_name)
    eggs = [1, 2, 3]
    eggs = [4, 5, 6]
    print(eggs)
    eggs = [1, 2, 3]
    del eggs[2]
    del eggs[1]
    del eggs[0]

    eggs.append(4)
    eggs.append(5)
    eggs.append(6)
    print(eggs)
    eggs = ("hello", 42, 0.5)
    print(eggs[0])
    print(eggs[1:3])
    print(len(eggs))
    eggs = ("hello", 42, 0.5)
    type(("hello",))
    type(("hello"))
    tuple(["cat", "dog", 5])
    list(("cat", "dog", 5))
    list("hello")


def wrapper6():
    """
    wrapper function part 6
    """
    spam = 42
    cheese = spam
    spam = 100
    print(spam)
    print(cheese)
    spam = [0, 1, 2, 3, 4, 5]
    cheese = spam
    cheese[1] = "Hello!"

    print(spam)
    print(cheese)
    print(id("Howdy"))
    bacon = "Hello"
    print(id(bacon))
    bacon += " world!"
    print(id(bacon))
    eggs = ["cat", "dog"]
    print(id(eggs))
    eggs.append("moose")
    print(id(eggs))
    eggs = ["bat", "rat", "cow"]
    print(id(eggs))

    eggs = lambda x: x.append("Hello")
    spam = [1, 2, 3]
    print(eggs(spam))
    print(spam)
    print([1, 2, 3, "Hello"])
    spam = ["A", "B", "C", "D"]
    print(id(spam))
    cheese = copy(spam)
    print(id(cheese))
    cheese[1] = 42
    print(spam)
    print(cheese)


def wrapper7():
    """
    wrapper function part 7
    """
    width = 60
    height = 20
    next_cells = []
    for xxx in range(width):
        column = []
        for yyy in range(height):
            value = "#" if randint(0, 1) == 0 else " "
            column.append(value)
        next_cells.append(column)
    while True:
        print("\n\n\n\n\n")
        current_cells = deepcopy(next_cells)
        for yyy in range(height):
            for xxx in range(width):
                print(current_cells[xxx][yyy], end="")
            print()
        for xxx in range(width):
            for yyy in range(height):
                left_coord = (xxx - 1) % width
                right_coord = (xxx + 1) % width
                above_coord = (yyy - 1) % height
                below_coord = (yyy + 1) % height
                num_neighbors = 0
                if any(
                    "#" in a
                    for a in [
                        current_cells[left_coord][above_coord],
                        current_cells[xxx][above_coord],
                        current_cells[right_coord][above_coord],
                        current_cells[left_coord][yyy],
                        current_cells[right_coord][yyy],
                        current_cells[left_coord][below_coord],
                        current_cells[xxx][below_coord],
                        current_cells[right_coord][below_coord],
                    ]
                ):
                    num_neighbors += 1
                if current_cells[xxx][yyy] == "#" and num_neighbors in (2, 3):
                    next_cells[xxx][yyy] = "#"
                elif current_cells[xxx][yyy] == " " and num_neighbors == 3:
                    next_cells[xxx][yyy] = "#"
                else:
                    next_cells[xxx][yyy] = " "
        sleep(1)
        if randint(0, 9) >= 5:
            break


def wrapper8():
    """
    wrapper function part 8
    """
    grid = [
        [".", ".", ".", ".", ".", "."],
        [".", "O", "O", ".", ".", "."],
        ["O", "O", "O", "O", ".", "."],
        ["O", "O", "O", "O", "O", "."],
        [".", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "."],
        ["O", "O", "O", "O", ".", "."],
        [".", "O", "O", ".", ".", "."],
        [".", ".", ".", ".", ".", "."],
    ]
    gridt = [
            "".join([grid[indexr][indexc] for indexr, _ in enumerate(grid)])
            for indexc, _ in enumerate(grid[0])
        ]
    for i in gridt:
        print("".join(i))


if __name__ == "__main__":
    wrapper1()
    wrapper2()
    wrapper3()
    wrapper4()
    wrapper5()
    wrapper6()
    wrapper7()
    wrapper8()
