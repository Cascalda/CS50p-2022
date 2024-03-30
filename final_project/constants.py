"""Contains the constants that are required for password generation files."""

import string

from english_words import get_english_words_set


MIN_PASSWORD_CHAR: int = 8
MAX_PASSWORD_CHAR: int = 128
RANGE_PASSWORD_CHAR: tuple[int, int] = (MIN_PASSWORD_CHAR, MAX_PASSWORD_CHAR)


MIN_PASSPHRASE_WORDS: int = 4
MAX_PASSPHRASE_WORDS: int = 20
RANGE_PASSPHRASE_WORDS: tuple[int, int] = (MIN_PASSPHRASE_WORDS, MAX_PASSPHRASE_WORDS)


MAX_SEPARATOR_LENGTH: int = 3
DEFAULT_SEPARATOR: str = "_"


CHARACTERS: dict[str, str] = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "numbers": string.digits,
    "special characters": string.punctuation,
}


RANDOM_CAPS_DISPLAY: dict[str, str] = {
    "first": "Uppercap first letter of each word",
    "last": "Uppercap last letter of each word",
    "any-one": "Uppercap any letter",
    "all": "Uppercap all words",
}

WORDS: list[str] = sorted(get_english_words_set(sources=["web2"]))
