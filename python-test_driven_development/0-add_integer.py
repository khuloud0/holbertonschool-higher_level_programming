#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""

def add_integer(a, b=98):
    """Add two integers or floats casted to integers.

    Raises:
        TypeError: if a or b are not integers or floats
        TypeError: if a or b are NaN or Infinity
    """
    # Check if a is int/float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is int/float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN and Infinity
    if a != a or a in [float("inf"), float("-inf")]:
        raise TypeError("a must be an integer")

    if b != b or b in [float("inf"), float("-inf")]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
