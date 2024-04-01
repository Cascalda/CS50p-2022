"""Contains the functions that are required for password generation."""

from random import choice, choices, randint, sample
from inspect import stack
from constants import (
    CHARACTERS,
    DEFAULT_SEPARATOR,
    MAX_SEPARATOR_LENGTH,
    RANDOM_CAPS_DISPLAY,
    RANGE_PASSPHRASE_WORDS,
    RANGE_PASSWORD_CHAR,
    WORDS,
)


# ===== Helper Functions =====
def get_valid_length(access_key_range: tuple[int, int]) -> int:
    """Obtain a valid length from the user."""
    min_length, max_length = access_key_range
    print(
        f"""
          Length must be between {min_length} and {max_length}.
        """
    )

    morpheme_type = {
        "generate_password": "character",
        "generate_passphrase": "word",
    }
    caller = stack()[1].function

    while True:
        morpheme = morpheme_type.get(caller, None)

        try:
            length = input(f"\nEnter length of {morpheme}s: ")
            if not length.isdigit():
                raise ValueError("Only integers accepted. Please try again.")

            length = int(length)

            if length < min_length or length > max_length:
                raise ValueError("Invalid length. Please try again.")

            return length

        except ValueError as e:
            print(e)
            continue


def get_character_pool() -> set[str]:
    """Get character pool(s) to include from the user."""
    flags_included = set()

    while not flags_included:
        print(
            """
            Press 'y' if u wish to include the following, skipping otherwise:
            - At least 1 condition is required.
        """
        )
        for flag in CHARACTERS:
            include_flag = input(f">>> Include {flag}? ").lower() == "y"
            if include_flag:
                flags_included.add(flag)

    return flags_included


def get_separator() -> str:
    """Obtains a valid separator from the user."""

    while True:
        separator = (
            input(f">>> Enter separator (Default '{DEFAULT_SEPARATOR}'): ")
            or DEFAULT_SEPARATOR
        )

        if len(separator) <= MAX_SEPARATOR_LENGTH:
            return separator

        print(f"Up to {MAX_SEPARATOR_LENGTH} characters are accepted.")


def get_random_uppercase_flag() -> str:
    """Get random capitalisation choice from the user."""
    print(
        f"""
        Choose a random capitalisation option:
        {', '.join(RANDOM_CAPS_DISPLAY)}
        """
    )

    while True:
        flag = input("\nYour choice: ")
        if flag in RANDOM_CAPS_DISPLAY:
            return flag

        print("No such choice. Please try again.")


def randomly_capitalise(word: str, flag: str) -> str:
    """Capitalises a random letter of each word according to the users choice."""

    default = word.lower()

    match flag:
        case "first":
            return choice((word.capitalize(), default))

        case "last":
            capitalised_last = word[:-1] + word[-1].upper()
            return choice((capitalised_last, default))

        case "any-one":
            random_index = randint(0, len(word) - 1)

            capitalised_random = (
                word[:random_index]
                + word[random_index].upper()
                + word[random_index + 1 :]
            )
            return capitalised_random

        case "all":
            return "".join(choice((letter.upper(), letter.lower())) for letter in word)

        case _:
            return word


# ===== Main Functions =====
def generate_password() -> str:
    """Generates a secure password."""
    length = get_valid_length(RANGE_PASSWORD_CHAR)
    included_flags = get_character_pool()

    character_pool = "".join(CHARACTERS[flag] for flag in included_flags)

    # Used random.choices to allow repetition, which increases unpredictability
    return "".join(choices(character_pool, k=length))


def generate_passphrase() -> str:
    """Generates a secure passphrase."""
    length = get_valid_length(RANGE_PASSPHRASE_WORDS)
    separator = get_separator()
    random_uppercase_choice = get_random_uppercase_flag()

    # Used random.sample to avoid repeating words,
    # making it harder to be brute-forced, especially for short passphrases
    return separator.join(
        randomly_capitalise(word, random_uppercase_choice)
        for word in sample(WORDS, k=length)
    )


def get_access_key() -> str:
    """Chooses the type of access key the user wants."""
    while True:
        # Prompt "password" instead of "access key" as "password" is more colloquial
        flag = input("\nPassword or Passphrase: ").lower()
        match = {
            "password": generate_password,
            "passphrase": generate_passphrase,
        }
        generator = match.get(flag, None)

        if generator is None:
            print("Only 'password' or 'passphrase' are accepted.")
        else:
            access_key = generator()
            return access_key


# ===== Entry Point =====
def main() -> None:
    """Interface to control all other functions."""
    while True:
        access_key = get_access_key()
        print(f"\nThis is your password: {access_key}")

        if input("\nGenerate another? (y/n) ").lower() != "y":
            break

    print("\nHave a nice day ahead! 😄")


if __name__ == "__main__":
    main()
