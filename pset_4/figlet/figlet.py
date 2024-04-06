"""Use pyfiglet to make fonts."""

import sys
import random

from pyfiglet import Figlet

figlet = Figlet()


def font_converter() -> None:
    """Converts text into different fonts."""
    font_command = sys.argv[1:]

    if len(font_command) == 0:
        random_font = random.choice(figlet.getFonts())
        figlet.setFont(font=random_font)

    else:
        prompt, type_ = font_command

        command_checks = {
            "Length": len(font_command) == 2,
            "Prompt": prompt in ("-f", "--font"),
            "Font": type_ in figlet.getFonts(),
        }

        if all(command_checks.values()):
            figlet.setFont(font=type_)

        else:
            raise RuntimeError


def main() -> None:
    """Interface to control all other functions."""
    try:
        font_converter()
        text = input("Input: ")
        print(figlet.renderText(text))
    except RuntimeError:
        sys.exit("Only empty prompt or prompt with -f or --font is accepted")


if __name__ == "__main__":
    main()
