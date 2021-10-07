"""
Python Basics
"""


def wrapper():
    """
    wrapper function
    """
    print(2 + 2)
    print(2)
    print(2 + 3 * 6)
    print((2 + 3) * 6)
    print(48565878 * 578453)
    print(2 ** 8)
    print(23 / 7)
    print(23 // 7)
    print(23 % 7)
    print(2 + 2)
    print((5 - 1) * ((7 + 1) / (3 - 1)))
    print(5)
    print(42 + 5 * 2)
    print("Hello world!")
    print("Alice" + "Bob")
    print("Alice")
    print("Alice" * 5)

    spam = 40
    print(spam)
    eggs = 2
    print(spam + eggs)
    print(spam + eggs + spam)
    spam = spam + 2
    print(spam)
    spam = "Hello"
    print(spam)
    spam = "Goodbye"

    print(spam)
    print(len("hello"))
    print(len("My very energetic monster just scarfed nachos."))
    print(len(""))
    print(f"I am {29} years old.")
    print(str(29))
    print("I am " + str(29) + " years old.")
    print(str(0))
    print(str(-3.14))
    print(int("42"))
    print(int("-99"))
    print(int(1.25))
    print(int(1.99))
    print(float("3.14"))
    print(float(10))

    spam = input("Enter a number: ")
    print(spam)
    spam = int(spam)
    print(spam)
    print(spam * 10 / 5)
    print(float("99.99"))
    print(int(7.7))
    print(int(7.7) + 1)
    print(42 == "42")
    print(42 == 42.0)
    print(42.0 == 42.000)


if __name__ == "__main__":
    wrapper()
