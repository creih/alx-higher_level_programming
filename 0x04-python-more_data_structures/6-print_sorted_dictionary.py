#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    zitondetse = sorted(a_dictionary.keys())
    for key in zitondetse:
        print("{}: {}".format(key, a_dictionary[key]))
