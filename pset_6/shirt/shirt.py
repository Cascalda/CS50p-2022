"""Make a cleaner version of the files containing first and last names."""

import sys

from PIL import Image, ImageOps

FILES_TO_OPEN = sys.argv[1:]
GIVEN_FILE_TYPES = {file.rsplit(".", maxsplit=1)[-1] for file in FILES_TO_OPEN}
DESIRED_FILE_TYPES = {"jpg", "jpeg", "png"}
DESIRED_ARG_NUM = 3
OVERLAY_FILE_NAME = "shirt.png"


def length_check() -> None:
    """Check for invalid length of command line arguments."""
    if len(sys.argv) < DESIRED_ARG_NUM:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > DESIRED_ARG_NUM:
        sys.exit("Too many command-line arguments")


def file_format_check() -> None:
    """Check for invalid file formats."""

    if GIVEN_FILE_TYPES > DESIRED_FILE_TYPES:
        sys.exit("Not a valid file")

    if len(GIVEN_FILE_TYPES) > 1:
        sys.exit("Input and output have different extensions")


def format_check() -> None:
    """Check the format of command line."""
    length_check()
    file_format_check()


# Unfortunately, I can't provide a type for overlay and background
# Both Image class and Image module have the same name, so there is conflict
def put_shirt_on(overlay, background, file_out: str) -> None:
    """Make the format of a csv file prettier."""
    in_edit = ImageOps.fit(background, overlay.size)
    in_edit.paste(overlay, mask=overlay)
    in_edit.save(file_out)


def main() -> None:
    """Interface to control all other functions."""
    format_check()

    try:
        file_in, file_out = FILES_TO_OPEN

        with (
            Image.open(OVERLAY_FILE_NAME) as overlay,
            Image.open(file_in) as background,
        ):
            put_shirt_on(overlay, background, file_out)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
