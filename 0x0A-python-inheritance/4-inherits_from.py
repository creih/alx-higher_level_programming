#!/usr/bin/python3
"""file for task 4"""


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) != a_class