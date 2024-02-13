#!/usr/bin/python3
"""
this is the file for task 6
"""


class BaseGeometry:
    """
    this is the class of area and other methods.
    """
    def area(self):
        """this is the area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this is to validate value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
