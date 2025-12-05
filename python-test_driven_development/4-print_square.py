#!/usr/bin/python3
"""
Module that prints a square with '#'
"""


def print_square(size):
    """
    Prints a square of size `size` using '#'.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """

    # Check type
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print square
    for i in range(size):
        print("#" * size)
