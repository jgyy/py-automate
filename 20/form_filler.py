"""
Automatically fills in the form.
"""
from time import sleep
from pyautogui import click, typewrite, press


def wrapper():
    """
    Set these to the correct coordinates for your particular computer.
    Give the user a chance to kill the script.
    Wait until the form page has loaded.
    Fill out the Name field.
    Fill out the Greatest Fear(s) field.
    Fill out the Source of Wizard Powers field.
    Fill out the Robocop field.
    Fill out the Additional comments field.
    Click Submit.
    Wait until form page has loaded.
    Click the Submit another response link.
    """
    name_field = (648, 319)
    submit_another_link = (760, 224)
    form_data = [
        {
            "name": "Alice",
            "fear": "eavesdroppers",
            "source": "wand",
            "robocop": 4,
            "comments": "Tell Bob I said hi.",
        },
        {
            "name": "Bob",
            "fear": "bees",
            "source": "amulet",
            "robocop": 4,
            "comments": "n/a",
        },
        {
            "name": "Carol",
            "fear": "puppets",
            "source": "crystal ball",
            "robocop": 1,
            "comments": "Please take the puppets out of the break room.",
        },
        {
            "name": "Alex Murphy",
            "fear": "ED-209",
            "source": "money",
            "robocop": 5,
            "comments": "Protect the innocent. Serve the public trust. Uphold the law.",
        },
    ]
    for person in form_data:
        print(">>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<")
        sleep(5)
        print(f"Entering {person['name']} info...")
        click(name_field[0], name_field[1])
        typewrite(person["name"] + "\t")
        typewrite(person["fear"] + "\t")
        if person["source"] == "wand":
            typewrite(["down", "\t"])
        elif person["source"] == "amulet":
            typewrite(["down", "down", "\t"])
        elif person["source"] == "crystal ball":
            typewrite(["down", "down", "down", "\t"])
        elif person["source"] == "money":
            typewrite(["down", "down", "down", "down", "\t"])
        if person["robocop"] == 1:
            typewrite([" ", "\t"])
        elif person["robocop"] == 2:
            typewrite(["right", "\t"])
        elif person["robocop"] == 3:
            typewrite(["right", "right", "\t"])
        elif person["robocop"] == 4:
            typewrite(["right", "right", "right", "\t"])
        elif person["robocop"] == 5:
            typewrite(["right", "right", "right", "right", "\t"])
        typewrite(person["comments"] + "\t")
        press("enter")
        print("Clicked Submit.")
        sleep(5)
        click(submit_another_link[0], submit_another_link[1])


if __name__ == "__main__":
    wrapper()
