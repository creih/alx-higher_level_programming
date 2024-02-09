#!/usr/bin/python3
"""
this file is for task 1 of this project
"""


class Base:
    __nbr_obj = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            __nbr_obj +=1
            self.id = __nbr_obj