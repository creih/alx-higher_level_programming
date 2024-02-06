#!/usr/bin/python3
"""This module will be for the task 0 of the 0x0B file I/O alx project"""


def read_file(filename=""):
    """this is the function to read text file and print it to the stdout"""
    with open(filename, 'r', encoding='Utf-8') as doc:
        print(doc.read())
    doc.close()