#!/usr/bin/python3
"""
this is the task 0 file
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    # Get the list of all attributes and methods
    attributes_and_methods = dir(obj)
    # Filter out attributes and methods starting with double underscores
    filtered_attributes_and_methods = [item for item in attributes_and_methods if item.startswith("__")]
    return filtered_attributes_and_methods
