"""Prints out the pretty menu of regular and sicilian pizzas."""

import sys
from csv import DictReader
from typing import IO

from tabulate import tabulate

FILE_TO_OPEN = sys.argv[1]
DESIRED_FILE_TYPE = "csv"
DESIRED_ARG_NUM = 2


def format_check(file) -> None:
    """Check the format of command line."""

    if len(sys.argv) < DESIRED_ARG_NUM:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > DESIRED_ARG_NUM:
        sys.exit("Too many command-line arguments")

    if not file.endswith(f".{DESIRED_FILE_TYPE}"):
        sys.exit(f"Not a Python file. Perhaps missing '.{DESIRED_FILE_TYPE}'?")


def prettify_menu(file: IO[str]) -> str:
    """Make the format of a csv file prettier."""

    menu = DictReader(file)
    pretty_menu = tabulate(menu, headers="keys", tablefmt="grid")

    return pretty_menu


def main() -> str:
    """Interface to control all other functions."""
    format_check(FILE_TO_OPEN)

    try:
        with open(FILE_TO_OPEN, mode="r", encoding="utf-8") as csvfile:
            pretty_menu = prettify_menu(csvfile)
    except FileNotFoundError:
        sys.exit("File does not exist")

    return pretty_menu


if __name__ == "__main__":
    result = main()
    print(result)
