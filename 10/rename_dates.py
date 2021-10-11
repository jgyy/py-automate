"""
Renames filenames with American MM-DD-YYYY date format
to European DD-MM-YYYY.
"""
from os import listdir
from os.path import abspath, join
import re
from re import VERBOSE


def wrapper():
    """
    Create a regex that matches files with the American date format.
    Loop over the files in the working directory.
    Skip files without a date.
    Get the different parts of the filename.
    Form the European-style filename.
    Get the full, absolute file paths.
    Rename the files.
    """
    date_pattern = re.compile(
        r"""^(.*?)
        ((0|1)?\d)-
        ((0|1|2|3)?\d)-
        ((19|20)\d\d)
        (.*?)$
        """,
        VERBOSE,
    )
    for amer_filename in listdir("."):
        moo = date_pattern.search(amer_filename)
        if moo is None:
            continue
        before_part = moo.group(1)
        month_part = moo.group(2)
        day_part = moo.group(4)
        year_part = moo.group(6)
        after_part = moo.group(8)
        euro_filename = (
            before_part + day_part + "-" + month_part + "-" + year_part + after_part
        )
        abs_working_dir = abspath(".")
        amer_filename = join(abs_working_dir, amer_filename)
        euro_filename = join(abs_working_dir, euro_filename)
        print(f'Renaming "{amer_filename}" to "{euro_filename}"...')


if __name__ == "__main__":
    wrapper()
