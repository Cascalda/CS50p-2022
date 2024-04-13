"""Changes middle endian dates to big endian dates"""

ACCEPTED_MONTHS = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12",
}


class InvalidDateError(Exception):
    """Used for catching invalid delimiters, month names, and dates."""


def extract_date(date: str) -> tuple[str, str, str]:
    """Formats American dates to ISO dates"""
    year, month, day = "", "", ""

    # Extracting day, month, year while checking for format validity
    if "/" in date:
        month, day, year = date.split("/")
        if not (month.isdigit() and day.isdigit and year.isdigit()):
            raise InvalidDateError("Only numbers allowed in MM/DD/YYYY format.")

    elif "," in date:
        month_day, year = date.split(",")
        month, day = month_day.split()
        month = ACCEPTED_MONTHS.get(month)
        if not month:
            raise InvalidDateError("No such month name.")

    else:
        raise InvalidDateError("Delimiter not accepted.")

    # Checking for date validity
    # Assumes date parts are always in numeric form
    if int(day) >= 31 or int(month) > 12:
        raise InvalidDateError("Invalid day or month.")

    return (year, month, day)


def convert_to_iso(year, month, day):
    """Convert the date to iso format."""
    return f"{year}-{int(month):02d}-{int(day):02d}"


def main():
    """Interface to control all other functions"""

    while True:
        date = input("Date (MM/DD/YYYY or Month DD, YYYY): ").strip()

        try:
            year, month, day = extract_date(date)
            iso_date = convert_to_iso(year, month, day)
            print(iso_date)
            break

        except InvalidDateError as e:
            print(e)


if __name__ == "__main__":
    main()
