#!/usr/bin/python3
"""this is my file for task 6."""
import json


def load_from_json_file(filename):
    """the function here gets an object for the file"""
    with open(filename, 'r', encoding='Utf-8') as docs:
        objects = json.load(docs)