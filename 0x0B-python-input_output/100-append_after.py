#!/usr/bin/python3
"""this is for the advanced task thing"""


def append_after(filename="", search_string="", new_string=""):
    """Insert line of text to file after each line containing specific str"""
    with open(filename, 'r+', encoding='Utf-8') as doc:
        lines = doc.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string + '\n')
        doc.seek(0)
        doc.writelines(lines)
