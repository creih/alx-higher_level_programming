#!/usr/bin/python3
"""
this is the file for task 8 class
"""
base_geom = __import__(7-base_geometry).BaseGeometry 


class Rectangle(BaseGeometry):
    """this is the class for the rectangle class"""
    def __init__(self, width, height):
        """initialisation of Rectangle clas"""
        self.__width = width
        if (isinstance(height, int) and height >= 0):
            self.__height = height