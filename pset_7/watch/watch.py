"""Extracts the shortened youtube link from html tag."""

import re


def parse(line: str) -> str | None:
    """Finds the youtube url and gives back the shortened link."""
    if iframe_match := re.search(
        r"""
        <iframe\s+src="  # Match the iframe tag with src attribute
        (  # Full url
             https?://(?:www.)?youtube.com/embed/  # YouTube embed URL
            ([\w-]{11})  # Video ID
        )
        "></iframe>
        """,
        line,
        re.VERBOSE,
    ):
        video_id = iframe_match.group(2)  # Extract only the needed value
        return f"https://youtu.be/{video_id}"

    return None


def main() -> str | None:
    """Interface to control all other functions."""
    line = input("HTML: ")
    return parse(line)


if __name__ == "__main__":
    result = main()
    print(result)
