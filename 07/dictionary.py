"""
Dictionaries
"""
from pprint import pprint


def wrapper1():
    """
    wrapper function part 1
    """
    my_cat = {"size": "fat", "color": "gray", "disposition": "loud"}
    print(my_cat["size"])
    print("My cat has " + my_cat["color"] + " fur.")
    print("My cat has gray fur.")
    spam = {12345: "Luggage Combination", 42: "The Answer"}
    spam = ["cats", "dogs", "moose"]
    bacon = ["dogs", "moose", "cats"]
    print(spam == bacon)
    eggs = {"name": "Zophie", "species": "cat", "age": "8"}
    ham = {"species": "cat", "age": "8", "name": "Zophie"}
    print(eggs == ham)
    spam = {"name": "Zophie", "age": 7}
    birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}

    while True:
        print("Enter a name: (blank to quit)")
        name = input()
        if name == "":
            break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have birthday information for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
    print("Birthday database updated.")
    spam = {"color": "red", "age": 42}

    for value in spam.values():
        print(value)
    for k in spam:
        print(k)
    for i in spam.items():
        print(i)
    print(("color", "red"))
    print(("age", 42))
    spam = {"color": "red", "age": 42}
    print(spam.keys())
    print(list(spam.keys()))
    spam = {"color": "red", "age": 42}
    for k, value in spam.items():
        print("Key: " + k + " Value: " + str(value))


def wrapper2():
    """
    wrapper function part 2
    """
    spam = {"name": "Zophie", "age": 7}
    print("name" in spam)
    print("Zophie" in spam.values())
    print("color" in spam)
    print("color" not in spam.keys())
    print("color" in spam)
    picnic_items = {"apples": 5, "cups": 2}
    print("I am bringing " + str(picnic_items.get("cups", 0)) + " cups.")
    print("I am bringing " + str(picnic_items.get("eggs", 0)) + " eggs.")
    picnic_items = {"apples": 5, "cups": 2}
    spam = {"name": "Pooka", "age": 5}

    if "color" not in spam:
        spam["color"] = "black"
    spam = {"name": "Pooka", "age": 5}
    spam.setdefault("color", "black")
    print(spam)
    spam.setdefault("color", "white")
    print(spam)
    message = (
        "It was a bright cold day in April, and the clocks were striking thirteen."
    )
    count = {}

    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    print(count)
    message = (
        "It was a bright cold day in April, and the clocks were striking thirteen."
    )
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    pprint(count)


def wrapper3():
    """
    wrapper function part 3
    """
    the_board = {
        "top-L": " ",
        "top-M": " ",
        "top-R": " ",
        "mid-L": " ",
        "mid-M": " ",
        "mid-R": " ",
        "low-L": " ",
        "low-M": " ",
        "low-R": " ",
    }

    def print_board(board):
        print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
        print("-+-+-")
        print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
        print("-+-+-")
        print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])

    print_board(the_board)
    turn = "X"
    for _ in range(9):
        print_board(the_board)
        print("Turn for " + turn + ". Move on which space?")
        move = input()
        the_board[move] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    print_board(the_board)
    all_guests = {
        "Alice": {"apples": 5, "pretzels": 12},
        "Bob": {"ham sandwiches": 3, "apples": 2},
        "Carol": {"cups": 3, "apple pies": 1},
    }

    def total_brought(guests, item):
        num_brought = 0
        for _, value in guests.items():
            num_brought = num_brought + value.get(item, 0)
        return num_brought

    print("Number of things being brought:")
    print(" - Apples         " + str(total_brought(all_guests, "apples")))
    print(" - Cups           " + str(total_brought(all_guests, "cups")))
    print(" - Cakes          " + str(total_brought(all_guests, "cakes")))
    print(" - Ham Sandwiches " + str(total_brought(all_guests, "ham sandwiches")))
    print(" - Apple Pies     " + str(total_brought(all_guests, "apple pies")))
    stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}

    def display_inventory(inventory):
        print("Inventory:")
        item_total = 0
        for k, value in inventory.items():
            print(value, k)
            item_total += value
        print("Total number of items: " + str(item_total))

    display_inventory(stuff)

    def add_to_inventory(inventory, added_items):
        for i in added_items:
            if inventory.get(i):
                inventory[i] += 1
            else:
                inventory[i] = 1
        return inventory

    inv = {"gold coin": 42, "rope": 1}
    dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)


if __name__ == "__main__":
    wrapper1()
    wrapper2()
    wrapper3()
