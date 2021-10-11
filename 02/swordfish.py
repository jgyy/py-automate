"""
swordfish
"""


def wrapper():
    """
    wrapper function
    """
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


if __name__ == "__main__":
    wrapper()
