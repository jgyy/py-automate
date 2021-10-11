"""
Removes the header from all CSV files in the current working directory.
"""
from os import makedirs, listdir
from os.path import join, dirname
from csv import reader, writer


def wrapper():
    """
    Loop through every file in the current working directory.
    skip non-csv files
    Read the CSV file in (skipping first row).
    skip first row
    Write out the CSV file.
    """
    path = dirname(__file__) + "\\"
    makedirs(path + "header_removed", exist_ok=True)
    for csv_filename in listdir(path + "headers"):
        if not csv_filename.endswith(".csv"):
            continue
        print("Removing header from " + csv_filename + "...")
        csv_rows = []
        with open(f"{path}headers\\{csv_filename}", encoding="utf-8") as csv_file_obj:
            reader_obj = reader(csv_file_obj)
            for row in reader_obj:
                if reader_obj.line_num == 1:
                    continue
                csv_rows.append(row)
        with open(
            join(path + "header_removed", csv_filename),
            "w",
            newline="",
            encoding="utf-8",
        ) as csv_file_obj:
            csv_writer = writer(csv_file_obj)
            for row in csv_rows:
                csv_writer.writerow(row)


if __name__ == "__main__":
    wrapper()
