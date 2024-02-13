#!/usr/bin/python3
"""
this is the file for task 1.
"""


class MyList(list):
    """
    thios is the required class for inheritting list
    """
    def __init__(self):
        """this is to initialise the MyList class"""
        self.list = list

    def print_sorted(self):
        """THIS PRINTS the list"""
        if (isinstance(list, int)):
            return(sorted(list))
