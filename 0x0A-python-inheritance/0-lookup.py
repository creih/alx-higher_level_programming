#!/usr/bin/python3
"""
this is the task 0 file
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    
    attributes_and_methods = dir(obj)
    
    filtered_attributes_and_methods = [item for item in attributes_and_methods if not item.startswith("__")]
    return filtered_attributes_and_methods