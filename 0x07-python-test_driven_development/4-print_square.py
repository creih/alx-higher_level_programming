#!/usr/bin/python3
"""
this is the file with func to print a # of squares
"""
def print_square(size):
    """
    this is the print square to print square of #
    """
    if (isinstance(size, int)):
        for ivert in range(0, size):
            for yhori in range(0, size):
                print("#")
            print()
