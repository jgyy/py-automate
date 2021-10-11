"""
box print
"""


def box_print(symbol, width, height):
    """
    wrapper function
    """
    if len(symbol) != 1:
        raise NameError("Symbol must be a single character string.")
    if width <= 2:
        raise NameError("Width must be greater than 2.")
    if height <= 2:
        raise NameError("Height must be greater than 2.")
    print(symbol * width)
    for _ in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)


if __name__ == "__main__":
    for sym, w, h in (("*", 4, 4), ("O", 20, 5), ("x", 1, 3), ("ZZ", 3, 3)):
        try:
            box_print(sym, w, h)
        except NameError as err:
            print("An exception happened: " + str(err))
