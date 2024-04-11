"""Vanity Plates and whether they are valid"""

from string import punctuation


def is_valid_plate(plate_char: str) -> bool:
    """Checks validity of vanity plates"""

    # Checks validity in this particular order
    validity_checks = {
        "Length": 2 <= len(plate_char) <= 6,
        "First 2 Characters": plate_char[0:2].isalpha(),
        "Special Characters": set(plate_char).isdisjoint(punctuation),
        "Number Conditions": num_condition_check(plate_char),
    }

    return all(validity_checks.values())


def num_condition_check(plate_to_check: str) -> bool:
    """To validate conditions for numbers in the plate"""

    for index, char in enumerate(plate_to_check):
        if char.isdigit():
            if int(char) == 0:  # first digit is 0
                return False

            return plate_to_check[
                index:
            ].isdigit()  # all succeeding characters are digits

    return True  # no digits


def main():
    """Interface to control all other functions"""

    plate = input("Plate: ")
    if is_valid_plate(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
