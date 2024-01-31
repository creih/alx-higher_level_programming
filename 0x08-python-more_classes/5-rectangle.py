#!/usr/bin/python3
"""this s task 5 file"""


class Rectangle:
    """this is the class for task5"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width != 0 and self._height != 0:
            return (2 * (self._width + self._height))
        else:
            return 0

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join([str("#") * self._width for _ in range(self._height)])

    def __repr__(self):
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        print("Bye rectangle...")
