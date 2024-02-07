#!/usr/bin/python3
"""
this is the task 0 file
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    atts = dir(obj)
    for item in atts:
        if not item.startswith("__"):
            filtered = [item]
    return filtered
