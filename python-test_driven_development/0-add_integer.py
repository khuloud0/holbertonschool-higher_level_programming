#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (after casting to int).

    Args:
        a: first number
        b: second number, default = 98

    Returns:
        int: addition of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
