#!/usr/bin/python3
class Square:
    """Class to define a square.

    This class represents a square and has a private instance attribute `size`.
    The size is validated during instantiation.

    Attributes:
        size (int): Private instance attribute representing the size of the square.

    """

    def __init__(self, size=0):
        """Initializes a new Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size