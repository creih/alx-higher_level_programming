#!/usr/bin/python3
"""
this is the answer file to task 3 say my name
"""


def say_my_name(first_name="", last_name=""):
    """this is my say my name function."""
    if not isinstance(first_name, str):
        print("first_name must be a string")
        return
    if not isinstance(last_name, str):
        print("last_name must be a string")
        return
    print(f"My name is {first_name} {last_name}")
