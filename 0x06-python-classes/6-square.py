#!/usr/bin/python3
""" class about possible square actions"""


class Square:
    """Class to define a square.

    This class represents a square and includes private instance attributes `size` and `position`.
    It provides properties and setters for both attributes, as well as methods for area computation
    and printing the square.

    Attributes:
        size (int): Private instance attribute representing the size of the square.
        position (tuple): Private instance attribute representing the position of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance with optional size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or position contains non-positive integers.

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
