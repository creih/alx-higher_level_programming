#!/usr/bin/python3
"""
this is the file for task 1.
"""


# class MyList(list):
#     """
#     thios is the required class for inheritting list
#     """

#     def print_sorted(self):
#         """THIS PRINTS the list"""
#         print(sorted(self))
class MyList(list):
    """
    thios is the required class for inheritting list
    """
    def __init__(self, *args):
        """THIS PRINTS the list"""
        super().__init__(*args)

    def __str__(self):
        """THIS PRINTS the list"""
        return super().__str__()

    def append(self, item):
        """THIS PRINTS the list"""
        super().append(item)

    def print_sorted(self):
        """THIS PRINTS the list"""
        sorted_list = sorted(self)
        print(sorted_list)
