#!/usr/bin/python3
"""this python file is for the answer of 13 advanced task."""


def add_attribute(obj, attr, value):
    """
    this is the function in charge for addin attribute
    """
    setattr(obj, attr, value)
    if hasattr(obj, attr):
        return obj
    else:
        raise TypeError("can't add new attribute")
