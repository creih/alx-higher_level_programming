#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(upper_char), end="")
    print()
