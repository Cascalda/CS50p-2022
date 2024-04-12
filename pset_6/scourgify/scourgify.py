"""Make a cleaner version of the files containing first and last names."""

import sys
from csv import DictReader, DictWriter
from typing import IO

FILES_TO_OPEN = sys.argv[1:]
DESIRED_FILE_TYPE = "csv"
DESIRED_ARG_NUM = 3


def format_check(files: list[str]) -> None:
    """Check the format of command line."""

    if len(sys.argv) < DESIRED_ARG_NUM:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > DESIRED_ARG_NUM:
        sys.exit("Too many command-line arguments")

    for file in files:
        if not file.endswith(f".{DESIRED_FILE_TYPE}"):
            sys.exit(f"Not a csv file. Perhaps missing '.{DESIRED_FILE_TYPE}'?")


def scourgify(csv_in: IO[str], csv_out: IO[str]) -> None:
    """Make the format of a csv file prettier."""
    file_in = DictReader(csv_in)
    fieldnames = ("first", "last", "house")
    file_out = DictWriter(csv_out, fieldnames=fieldnames)
    file_out.writeheader()

    for row in file_in:
        last_name, first_name = row["name"].split(", ")
        house = row["house"]
        file_out.writerow(
            {
                "first": first_name,
                "last": last_name,
                "house": house,
            }
        )


def main() -> None:
    """Interface to control all other functions."""
    format_check(FILES_TO_OPEN)

    try:
        file_in, file_out = FILES_TO_OPEN

        with (
            open(file_in, mode="r", encoding="utf-8") as csv_in,
            open(file_out, mode="w", encoding="utf-8") as csv_out,
        ):
            scourgify(csv_in, csv_out)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
