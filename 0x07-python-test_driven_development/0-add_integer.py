#!/usr/bin/python3
import unittest


def add_integer(a, b=98):
    """this is a python function to add 2 ints"""
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
        a = int(a)
        b = int(b)
    return (int(a) + int(b))
