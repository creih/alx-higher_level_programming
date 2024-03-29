#!/usr/bin/python3
"""the rectangle with height and width"""


class Rectangle:
    """this is the inside of our rectanle"""
    def __init__(self, width=0, height=0):
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.Rectangle_width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.Rectangle_width = value

    @property
    def height(self):
        return self.Rectangle_height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.Rectangle_height = value
