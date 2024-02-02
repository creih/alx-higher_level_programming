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


# class TestAddition(unittest.TestCase):
#     """this is the tests class"""
#     def test_add_positive_numbers(self):
#         result = add_numbers(3, 5)
#         self.assertEqual(result, 8)

#     def test_add_negative_numbers(self):
#         result = add_numbers(-2, -4)
#         self.assertEqual(result, -6)

#     def test_add_mixed_numbers(self):
#         result = add_numbers(10, -3)
#         self.assertEqual(result, 7)

# if __name__ == '__main__':
#     unittest.main()