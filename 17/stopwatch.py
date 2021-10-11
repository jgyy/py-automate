"""
A simple stopwatch program.
"""
from time import time


def wrapper():
    """
    Display the program's instructions.
    press Enter to begin
    get the first lap's start time
    Start tracking the lap times.
    reset the last lap time
    Handle the Ctrl-C exception to keep its error message from displaying.
    """
    print(
        "Press enter to begin. Afterwards,",
        "press ENTER to 'click' the stopwatch. Press Ctrl-C to quit.",
    )
    input()
    print("Started.")
    start_time = time()
    last_time = start_time
    lap_num = 1
    try:
        while True:
            input()
            lap_time = round(time() - last_time, 2)
            total_time = round(time() - start_time, 2)
            print(f"Lap #{lap_num}: {total_time}, ({lap_time})", end="")
            lap_num += 1
            last_time = time()
    except KeyboardInterrupt:
        print("\nDone.")


if __name__ == "__main__":
    wrapper()
