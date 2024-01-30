#!/usr/bin/python3
"""this file will make the task 3"""


class Rectangle:
    """this is the class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        result = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                result += '#' * self.__width + '\n'
        return result[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
