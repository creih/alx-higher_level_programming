#!/usr/bin/python3
"""
this is the file for task 1.
"""


class MyList(list):
    """
    thios is the required class for inheritting list
    """

    def print_sorted(self):
        """THIS PRINTS the list"""
        sorted_list = sorted(self)
        for num in sorted_list:
            if isinstance(num, int):
                print("[{}]".format(num, end=", "))
