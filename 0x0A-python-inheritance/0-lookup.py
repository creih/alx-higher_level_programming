#!/usr/bin/python3
"""
this is the task 0 file
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    atts = dir(obj)
    for item in atts:
        if item.startswith("__"):
            filtered_attributes_and_methods = item
    return filtered_attributes_and_methods
