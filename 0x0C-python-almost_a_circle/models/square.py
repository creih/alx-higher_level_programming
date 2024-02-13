#!/usr/bin/python3
"""this file is from almost a circle task 10"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class is for the impolementation of square"""

    def __init__(self, size, x=0, y=0, id=None):
        """this method inherits all functionality from class Rectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """this is the getter for width"""
        return self.width

    @size.setter
    def size(self, value):
        """size's setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """simply the return when obj called"""
        sms = "[square] ({}) {}/{} - {}"
        return sms.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """this is for updating the values of attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """return the dict rep of the square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
