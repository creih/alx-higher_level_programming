#!/usr/bin/python3
"""this is the file for my base tests."""
import unittest
from .base import Base
from .rectangle import Rectangle
from .square import Square


class TestBase(unittest.TestCase):
    """this is the testcase class"""
    
    def test_create_rectangle(self):
        """tests for rectangle initiation"""
        rectangle = Rectangle(10, 5)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertIsInstance(rectangle, Base)

    def test_create_square(self):
        """tests for square initiation"""
        square = Square(5)
        self.assertIsInstance(square, Square)
        self.assertIsInstance(square, Rectangle)
        self.assertIsInstance(square, Base)

    def test_area_rectangle(self):
        """test the area calculation."""
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.area(), 50)

    def test_area_square(self):
        """ Test calculating area of a Square"""
        square = Square(5)
        self.assertEqual(square.area(), 25)

if __name__ == '__main__':
    unittest.main()