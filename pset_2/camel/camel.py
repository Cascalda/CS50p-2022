"""Convert camelCase characters into snake case."""

SEPARATOR = "_"


def snake_caser(camel_case: str) -> str:
    """Brings the snake_case out of camelCase."""

    snake_cased = ""

    for char in camel_case:
        if char.islower():
            snake_cased += char
        else:
            to_snake_case = f"{SEPARATOR}{char.lower()}"
            snake_cased += to_snake_case

    return snake_cased


def main() -> None:
    """Interface to control all other functions."""

    user_input = input("camelCase: ")

    result = snake_caser(user_input)
    print(result)


if __name__ == "__main__":
    main()
