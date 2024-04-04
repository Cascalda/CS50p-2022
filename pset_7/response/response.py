"""Validate proper emails."""

import validators


def validate_email() -> None:
    """Interface to control all other functions."""
    given_email = input("Whats your email address? ")
    if validators.email(given_email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    validate_email()
