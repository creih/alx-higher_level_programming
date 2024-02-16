#!/usr/bin/python3
"""this is the test for base class"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_auto_assign_id(self):
        """Test if Base() assigns an ID automatically."""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

if __name__ == '__main__':
    unittest.main()