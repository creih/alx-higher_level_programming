import unittest
from models.rectangle import Rectangle as rect

class RectangleTestCase(unittest.TestCase):

  def test_area(self):
    self.assertEqual(self.rectangle.area(), 50)

  def test_isSquare(self):
    self.assertFalse(self.rectangle.isSquare())
    self.rectangle.width = 5
    self.assertTrue(self.rectangle.isSquare())

  def test_error(self):
    self.rectangle.width = "A"
    with self.assertRaises(TypeError):
      a = self.rectangle.perimeter()

  def setUp(self):
    self.rectangle = rect.Rectangle(5 ,10)

if __name__ == '__main__':
  unittest.main()
