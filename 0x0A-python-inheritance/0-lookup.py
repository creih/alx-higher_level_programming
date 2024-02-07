#!/usr/bin/python3
"""
this is the task 0 file
"""


def lookup(obj):
    """this function returns a list of object."""
    filt_attr = dir(obj)
    for one in filt_attr:
        if not one.startswith("__"):
            filtered = one
    return filtered
