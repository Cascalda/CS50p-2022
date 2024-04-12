"""Calculates the number of lines in a file."""

import sys
from typing import IO

FILE_TO_OPEN = sys.argv[1]
DESIRED_FILE_TYPE = "py"
DESIRED_ARG_TYPE = 2


def format_check(file) -> None:
    """Check the format of command line."""

    if len(sys.argv) < DESIRED_ARG_TYPE:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > DESIRED_ARG_TYPE:
        sys.exit("Too many command-line arguments")

    if not file.endswith(f".{DESIRED_FILE_TYPE}"):
        sys.exit(f"Not a Python file. Perhaps missing '.{DESIRED_FILE_TYPE}'?")


def is_empty_line(line):
    """Checks if the line given is empty."""
    empty_line_condition = (not line, line.startswith("#"))
    return any(empty_line_condition)


def get_lines(file: IO[str]) -> int:
    """Get the number of lines in a file."""
    lines = [_.strip(" \n") for _ in file.readlines()]
    lines_total = len(lines)

    for line in lines:
        if is_empty_line(line):
            lines_total -= 1

    return lines_total


def main() -> int:
    """Interface to control all other functions."""
    format_check(FILE_TO_OPEN)

    try:
        with open(FILE_TO_OPEN, mode="r", encoding="utf-8") as pyfile:
            num_lines = get_lines(pyfile)
    except FileNotFoundError:
        sys.exit("File does not exist")

    return num_lines


if __name__ == "__main__":
    result = main()
    print(result)
