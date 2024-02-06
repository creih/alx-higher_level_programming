#!/usr/bin/python3
"""This module will be for the task 0 of the 0x0B file I/O alx project"""
import json


def save_to_json_file(my_obj, filename):
    """this is the function to turn obj into json data"""
    with open(filename, 'w', encoding='Utf-8') as file:
        json.dump(my_obj, file)
    file.close()
