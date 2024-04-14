"""Repeats what the user has said but with playful delay."""


def play_it_back() -> str:
    """Play what the user said back to them with style."""
    message = input("Whatcha say?? ")
    return message.replace(" ", "...")


def main() -> None:
    """Interface to control all other functions."""
    print(play_it_back())


if __name__ == "__main__":
    main()
