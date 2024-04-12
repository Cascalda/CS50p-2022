"""Tests fuel.py from pset_3."""

import pytest

from fuel import convert, gauge


# pylint: disable=missing-function-docstring


def test_convert():
    fractions_percentages = (
        ("3/7", 43),
        ("3/4", 75),
        ("5/9", 56),
        ("0/41", 0),
        ("91/91", 100),
    )
    for fraction, expected_percentage in fractions_percentages:
        assert convert(fraction) == expected_percentage

    with pytest.raises(ZeroDivisionError):
        convert("51/0")

    with pytest.raises(ValueError):
        convert("431/110")


def test_gauge_indicators():
    percentages_indicators = (
        (0, "E"),
        (1, "E"),
        (99, "F"),
        (100, "F"),
        (45, "45%"),
        (98, "98%"),
    )

    for percentage, expected_indicator in percentages_indicators:
        assert gauge(percentage) == expected_indicator


if __name__ == "__main__":
    pytest.main()
