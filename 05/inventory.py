"""
inventory.py
"""


def display_inventory(inventory):
    """
    wrapper function
    """
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + " " + key)
        item_total += value
    print("Total number of items: " + str(item_total))


if __name__ == "__main__":
    stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    display_inventory(stuff)
