#!/usr/bin/python3
"""
this is the file with func to print a # of squares
"""
def print_square(size):
    """
    this is the print square to print square of #
    """
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, int):
        for ivert in range(0, size):
            for yhori in range(0, size):
                print("#", end="")
            print()
    else:
        raise TypeError("size must be an integer")
