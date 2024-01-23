#!/usr/bin/python3
"""this is the implementatin of adv task"""
class Square:
    """Class to define a square.

    This class reps square and private instance attributes `size`, `position`.
    It provides properties and setters for both attributes,methods for area 
    and printing the square.

    Attributes:
        size (int): Private instance attribute rep size of square.
        position (tuple): Private instance rep the position of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance with optional size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional):squareposition. Defaults to (0, 0).

        Raises:
            TypeError: If size not int or position not tuple of 2 + integers.
            ValueError: If size less than 0 or position contains - integers.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter property for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter property for the size of the square.

        Args:
            value: The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Getter property for the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter property for the position of the square.

        Args:
            value: The position to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains non-positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Computes and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character '#'."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String rep like my_print()."""
        result = ""
        if self.__size == 0:
            return result

        for _ in range(self.__position[1]):
            result += "\n"

        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"

        return result.rstrip()
