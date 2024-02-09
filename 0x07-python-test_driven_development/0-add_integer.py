#!/usr/bin/python3
"""
this file is for returning sum of 2 ints as task 0 
required.
"""


def add_integer(a, b=98):
    """this is a python function to add 2 ints"""
    if not (isinstance(a, (int, float))):
        print("a must be an integer")
        return
    if not (isinstance(b, (int, float))):
        print("b must be an integer")
        return
    a = int(a)
    b = int(b)
    return (a + b)
