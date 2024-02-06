#!/usr/bin/python3
"""this is the task 8 file response"""
import json


def class_to_json(obj):
    """Returns a dictionary description for JSON serialization of an object."""
    json_dict = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
            
    return json_dict