#!/usr/bin/python3
"""
this is the file with func to print a # of squares
"""
def print_square(size):
    """
    this is the print square to print square of #
    """
    # if not type(size) is int:
    #     raise TypeError("size must be an integer")
    # if size < 0:
    #     raise ValueError("size must be >= 0")
    # if isinstance(size, float) and size < 0:
    #     raise TypeError("size must be an integer")
    try:
        if isinstance(size, int):
            for ivert in range(0, size):
                for yhori in range(0, size):
                    print("#", end="")
                print()
    except TypeError:
        print("size must be an integer")
    except ValueError:
        print("size must be >= 0")
# print_square(-0.8)
