#!/usr/bin/python3
"""
this is the file for task 1.
"""


class MyList(list):
    """
    thios is the required class for inheritting list
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
