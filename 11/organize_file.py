"""
Organizing Files
"""
from os import chdir, listdir, unlink, walk
from os.path import dirname, abspath, join, basename, exists
import re
from re import VERBOSE
from shutil import copy, move
from zipfile import ZipFile, ZIP_DEFLATED
from send2trash import send2trash

PATH = dirname(__file__) + "\\"


def wrapper1():
    """
    wrapper function part 1
    """
    print("qwdefrwdefr")
    chdir(PATH)
    copy(f"{PATH}spam.txt", f"{PATH}deliciou.txt")
    copy(f"{PATH}spam.txt", f"{PATH}bacon.txt")
    copy(f"{PATH}eggs.txt", f"{PATH}delicious\\eggs2.txt")
    chdir(PATH)
    copy(f"{PATH}bacon.txt", f"{PATH}eggss")
    move(f"{PATH}bacon.txt", f"{PATH}eggss\\new_bacon.txt")

    for filename in listdir():
        if filename.endswith(".rxt"):
            unlink(filename)
    for filename in listdir():
        if filename.endswith(".rxt"):
            print(filename)
    with open(f"{PATH}bacon.txt", "a", encoding="utf-8") as bacon_file:
        bacon_file.write("Bacon is not a vegetable.")

    send2trash(f"{PATH}bacon.txt")
    for folder_name, subfolders, filenames in walk(f"{PATH}delicious"):
        print("The current folder is " + folder_name)
        for subfolder in subfolders:
            print("SUBFOLDER OF " + folder_name + ": " + subfolder)
        for filename in filenames:
            print("FILE INSIDE " + folder_name + ": " + filename)
        print("")
    chdir(PATH)

    with ZipFile(f"{PATH}example.zip") as example_zip:
        example_zip.namelist()
        spam_info = example_zip.getinfo(f"{PATH}spam.txt")
        print(spam_info.file_size)
        print(spam_info.compress_size)
        print(
            "Compressed file is",
            f"{round(spam_info.file_size / spam_info.compress_size, 2)}x smaller!",
        )
        chdir(PATH)
        example_zip.extractall()
        example_zip.extract(f"{PATH}spam.txt")
        example_zip.extract(f"{PATH}spam.txt", f"{PATH}folders")
    with ZipFile(f"{PATH}new.zip", "w") as new_zip:
        new_zip.write(f"{PATH}spam.txt", compress_type=ZIP_DEFLATED)


def wrapper2():
    """
    wrapper function part 2
    """
    date_pattern = re.compile(
        r"""^(.*?)        # all text before the date
        ((0|1)?\d)-       # one or two digits for the month
        ((0|1|2|3)?\d)-   # one or two digits for the day
        ((19|20)\d\d)     # four digits for the year
        (.*?)$            # all text after the date
        """,
        VERBOSE,
    )
    for amer_filename in listdir("."):
        mon = date_pattern.search(amer_filename)
        if mon is None:
            continue
        before_part = mon.group(1)
        month_part = mon.group(2)
        day_part = mon.group(4)
        year_part = mon.group(6)
        after_part = mon.group(8)
        date_pattern = re.compile(
            r"""^(1)    # all text before the date
            (2 (3) )-   # one or two digits for the month
            (4 (5) )-   # one or two digits for the day
            (6 (7) )    # four digits for the year
            (8)$        # all text after the date
            """,
            VERBOSE,
        )
        euro_filename = (
            before_part + day_part + "-" + month_part + "-" + year_part + after_part
        )
        abs_working_dir = abspath(".")
        amer_filename = join(abs_working_dir, amer_filename)
        euro_filename = join(abs_working_dir, euro_filename)
        print(f'Renaming "{amer_filename}" to "{euro_filename}"...')

    def backup_to_zip(folder):
        folder = abspath(folder)
        number = 1
        while True:
            zip_filename = basename(folder) + "_" + str(number) + ".zip"
            if not exists(zip_filename):
                break
            number = number + 1
        print(f"Creating {zip_filename}...")
        with ZipFile(zip_filename, "w") as backup_zip:
            print("Done.")
            for foldername, _, filenames in walk(folder):
                print(f"Adding files in {foldername}...")
                backup_zip.write(foldername)
                for filename in filenames:
                    new_base = basename(folder) + "_"
                    if filename.startswith(new_base) and filename.endswith(".zip"):
                        continue
                    backup_zip.write(join(foldername, filename))
            print("Done.")

    backup_to_zip(f"{PATH}delicious")


if __name__ == "__main__":
    wrapper1()
    wrapper2()
