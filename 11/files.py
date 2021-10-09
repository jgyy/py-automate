"""
Reading and Writing Files
"""
from os import getcwd, chdir, listdir
from os.path import (
    join,
    abspath,
    isabs,
    relpath,
    basename,
    dirname,
    sep,
    getsize,
    exists,
    isfile,
    isdir,
    split,
)
from sys import argv
import shelve
from random import shuffle, sample
from pprint import pformat
from pyperclip import copy, paste


def wrapper1():
    """
    wrapper function part 1
    """
    directory = dirname(__file__)
    print(join("usr", "bin", "spam"))
    my_files = ["accounts.txt", "details.csv", "invite.docx"]
    for filename in my_files:
        print(join("C:\\Users\\asweigart", filename))
    print(getcwd())
    chdir("C:\\Windows\\System32")
    print(getcwd())
    chdir("C:\\Windows")
    print(abspath("."))
    print(abspath(".\\Scripts"))
    print(isabs("."))
    print(isabs(abspath(".")))
    print(relpath("C:\\Windows", "C:\\"))
    print(relpath("C:\\Windows", "C:\\spam\\eggs"))
    print(getcwd())
    chdir(directory)

    path = "C:\\Windows\\System32\\calc.exe"
    print(basename(path))
    print(dirname(path))
    calc_file_path = "C:\\Windows\\System32\\calc.exe"
    print(split(calc_file_path))
    print((dirname(calc_file_path), basename(calc_file_path)))
    print(calc_file_path.split(sep))
    print("/usr/bin".split(sep))
    print(getsize("C:\\Windows\\System32\\calc.exe"))
    print(listdir("C:\\Windows\\System32"))

    total_size = 0
    for filename in listdir("C:\\Windows\\System32"):
        total_size = total_size + getsize(join("C:\\Windows\\System32", filename))
    print(total_size)
    print(exists("C:\\Windows"))
    print(exists("C:\\some_made_up_folder"))
    print(isdir("C:\\Windows\\System32"))
    print(isfile("C:\\Windows\\System32"))
    print(isdir("C:\\Windows\\System32\\calc.exe"))
    print(isfile("C:\\Windows\\System32\\calc.exe"))
    print(exists("D:\\"))

    with open(f"{directory}\\hello.txt", encoding="utf-8") as hello_file:
        hello_content = hello_file.read()
        print(hello_content)
    with open(f"{directory}\\sonnet29.txt", encoding="utf-8") as sonnet_file:
        print(sonnet_file.readlines())
    with open(f"{directory}\\bacon.txt", "r+", encoding="utf-8") as bacon_file:
        bacon_file.write("Hello world!\n")
        bacon_file.write("Bacon is not a vegetable.")
        content = bacon_file.read()
        print(content)


def wrapper2():
    """
    wrapper function part 2
    """
    shelf_file = shelve.open("mydata")
    cats = ["Zophie", "Pooka", "Simon"]
    shelf_file["cats"] = cats
    shelf_file = shelve.open("mydata")
    type(shelf_file)
    print(shelf_file["cats"])
    shelf_file = shelve.open("mydata")
    list(shelf_file.keys())
    list(shelf_file.values())
    shelf_file.close()
    cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
    print(pformat(cats))

    with open("my_cats.py", "w", encoding="utf-8") as file_obj:
        file_obj.write("cats = " + pformat(cats) + "\n")
    capitals = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "Saint Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne",
    }

    for quiz_num in range(35):
        with open(
            f"capitalsquiz{quiz_num + 1}.txt", "w", encoding="utf-8"
        ) as quiz_file, open(
            f"capitalsquiz_answers{quiz_num + 1}.txt", "w", encoding="utf-8"
        ) as answer_key_file:
            quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
            quiz_file.write((" " * 20) + f"State Capitals Quiz (Form {quiz_num + 1})")
            quiz_file.write("\n\n")
            states = list(capitals.keys())
            shuffle(states)
            for question_num in range(50):
                correct_answer = capitals[states[question_num]]
                wrong_answers = list(capitals.values())
                del wrong_answers[wrong_answers.index(correct_answer)]
                wrong_answers = sample(wrong_answers, 3)
                answer_options = wrong_answers + [correct_answer]
                shuffle(answer_options)
                quiz_file.write(
                    f"{question_num + 1}. What is the capital of {states[question_num]}?\n"
                )
                for i in range(4):
                    quiz_file.write(f" {'ABCD'[i]}. {answer_options[i]}\n")
                quiz_file.write("\n")
                answer_key_file.write(
                    f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n"
                )

    mcb_shelf = shelve.open("mcb")
    if len(argv) == 3 and argv[1].lower() == "save":
        mcb_shelf[argv[2]] = paste()
    elif len(argv) == 2:
        if argv[1].lower() == "list":
            copy(str(list(mcb_shelf.keys())))
        elif argv[1] in mcb_shelf:
            copy(mcb_shelf[argv[1]])
    mcb_shelf.close()


if __name__ == "__main__":
    wrapper1()
    wrapper2()
