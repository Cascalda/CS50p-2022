"""A basic calculator."""


def math_interpreter(integer_1: float, operator: str, integer_2: float) -> float:
    """Calculates with simple operator."""

    match operator:
        case "+":
            return integer_1 + integer_2
        case "-":
            return integer_1 - integer_2
        case "*":
            return integer_1 * integer_2
        case "/":
            return integer_1 / integer_2
        case _:
            raise ValueError(f"{operator} operator not supported.")


def main() -> None:
    """Interface to control all other functions."""

    user_input = input("Expression: ")
    num_1, oper, num_2 = user_input.split()

    results = math_interpreter(float(num_1), oper, float(num_2))
    print(results)


if __name__ == "__main__":
    main()
