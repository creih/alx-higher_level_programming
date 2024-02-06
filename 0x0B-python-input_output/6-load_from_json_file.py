#!/usr/bin/python3
"""this is my file for task 6."""


def load_from_json_file(filename):
    with open(filename, 'r', encoding='Utf-8') as doc:
        for chars in doc:
            return json.loads(chars)