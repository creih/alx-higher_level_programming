#!/usr/bin/python3
"""this is for the task 7 in 0x0B"""
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
import sys


arguments = sys.argv[1:]
try:
    items = load_from_json_file('add_item.json')
except FileNotFoundError:
    items = []
items.extend(arguments)
save_to_json_file(items, 'add_item.json')