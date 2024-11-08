"""Make the So Long, Farewell song in The Sound of Music have proper oxford commas"""

import inflect

inflect = inflect.engine()


def oxford_comma():
    """Forms a sentence with oxford commas"""
    try:
        names = []

        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        to_oxford_comma = inflect.join(names)
        print(f"\nAdieu, adieu, to {to_oxford_comma}")


if __name__ == "__main__":
    oxford_comma()
