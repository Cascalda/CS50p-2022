"""Calculate the energy using E = mc^2."""


def energy(mass: int) -> int:
    """Return the energy given the mass."""
    speed_of_light = 300_000_000  # to closest hundred million
    return mass * (speed_of_light**2)


def main() -> None:
    """Interface to control all other functions."""
    user_input = int(input("m: "))
    result = energy(user_input)
    print(result)


if __name__ == "__main__":
    main()
