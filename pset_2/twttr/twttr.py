"""Removes vowels in words"""

VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")


def vowel_remove(characters: str) -> str:
    """Removes vowels like twttr does"""

    shortened = ""
    for char in characters:
        if char not in VOWELS:
            shortened += char

    return shortened


def main():
    """Interface to control all other functions"""

    user_input = input("Input: ")
    result = vowel_remove(user_input)
    print(result)


if __name__ == "__main__":
    main()
