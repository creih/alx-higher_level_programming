#!/usr/bin/python3
"""This module will be for the task 0 of the 0x0B file I/O alx project"""


def write_file(filename="", text=""):
    """this is the function to write text to file"""
    with open(filename, 'w', encoding='Utf-8') as doc:
        doc.write(text)
    doc.close()
    return len(text)
