"""Converts time from 12-hour format to 24-hour format."""

import re

TIME_SEPARATOR = "to"
TIME_REGEX = r"([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
SEPARATOR_REGEX = rf"(.*)\s{TIME_SEPARATOR}\s(.*)"


def extract_time_groups(time: str):
    """Returns the time components as arguments based on given regex."""
    match = re.fullmatch(TIME_REGEX, time)
    if not match:
        raise ValueError("Invalid time format")

    return {
        "hour": int(match.group(1)),
        "minute": int(match.group(2) or 0),  # Minute is optionally provided
        "meridiem": match.group(3),
    }


def convert(duration: str) -> str:
    """Converts 12-hour time to 24-hour time."""

    match = re.fullmatch(SEPARATOR_REGEX, duration)
    if not match:
        raise ValueError("Invalid duration format")

    time_from_groups, time_to_groups = match.groups()

    time_from = format_24_hour(**extract_time_groups(time_from_groups))
    time_to = format_24_hour(**extract_time_groups(time_to_groups))

    return f"{time_from} {TIME_SEPARATOR} {time_to}"


def format_24_hour(meridiem: str, hour: int, minute: int = 0) -> str:
    """Formats time to 24-hour from 12-hour."""

    if meridiem == "PM" and hour != 12:
        hour = (hour + 12) % 24
    elif meridiem == "AM" and hour == 12:
        hour = 0

    result = f"{hour:02d}:{minute:02d}"
    return result


def main() -> str:
    """Interface to control all other functions."""
    time_12_hour = input("Hours: ")
    result = convert(time_12_hour)
    return result


if __name__ == "__main__":
    print(main())
