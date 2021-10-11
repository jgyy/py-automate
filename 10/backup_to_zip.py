"""
# Copies an entire folder and its contents into
# a zip file whose filename increments.
"""
from os import walk
from os.path import abspath, basename, exists, join
from zipfile import ZipFile


def backup_to_zip(folder):
    """
    Backup the entire contents of "folder" into a zip file.
    make sure folder is absolute
    Figure out the filename this code should used based on what files already exist.
    Create the zip file.
    Walk the entire folder tree and compress the files in each folder.
    Add the current folder to the ZIP file.
    Add all the files in this folder to the ZIP file.
    don't backup the backup ZIP files
    """
    folder = abspath(folder)
    number = 1
    while True:
        zip_filename = basename(folder) + "_" + str(number) + ".zip"
        if not exists(zip_filename):
            break
        number = number + 1
    print(f"Creating {zip_filename}...")
    with ZipFile(zip_filename, "w") as backup_zip:
        for foldername, _, filenames in walk(folder):
            print(f"Adding files in {foldername}...")
            backup_zip.write(foldername)
            for filename in filenames:
                if filename.startswith(basename(folder) + "_") and filename.endswith(
                    ".zip"
                ):
                    continue
                backup_zip.write(join(foldername, filename))
    print("Done.")


if __name__ == "__main__":
    BACKUP = "\\".join(__file__.split("\\")[:-2])
    backup_to_zip(BACKUP)
