#!/usr/bin/python3
"""this is for  the advanced task thing"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing a specific string."""
    with open(filename, 'r+',encoding='Utf-8') as doc:
        lines = doc.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string + '\n')
        doc.seek(0)
        doc.writelines(lines)
        append_after("example.txt", "specific string", "new line to insert")