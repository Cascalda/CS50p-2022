"""Converting Emoticons to Emojis."""


def convert(message: str) -> str:
    """Convert emojicons in a message to emojis."""
    emojicon_to_emojis = {
        ":)": "🙂",
        ":(": "🙁",
    }

    for emojicon, emoji in emojicon_to_emojis.items():
        message = message.replace(emojicon, emoji)

    return message


def main() -> None:
    """Interface to control all other functions."""
    user_input = input("Say something with emoticons! ")
    result = convert(user_input)
    print(result)


if __name__ == "__main__":
    main()
