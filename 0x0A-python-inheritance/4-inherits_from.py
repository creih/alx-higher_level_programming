#!/usr/bin/python3
"""file for task 4"""


def inherits_from(obj, a_class):
    """this function checks for true or not if obj is instance of a class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class