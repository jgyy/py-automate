"""
all my cats 1
"""


def wrapper():
    """
    wrapper function
    """
    print("Enter the name of cat 1:")
    cat_name1 = input()
    print("Enter the name of cat 2:")
    cat_name2 = input()
    print("Enter the name of cat 3:")
    cat_name3 = input()
    print("Enter the name of cat 4:")
    cat_name4 = input()
    print("Enter the name of cat 5:")
    cat_name5 = input()
    print("Enter the name of cat 6:")
    cat_name6 = input()
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


if __name__ == "__main__":
    wrapper()
