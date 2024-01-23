class Square:
    """Class to define a square.

    This class represents a square and includes a private instance attribute `size`.
    It provides properties and setters for `size`, a method for area computation,
    and supports comparators based on the square area.

    Attributes:
        size (float or int): Private instance attribute representing the size of the square.

    """

    def __init__(self, size=0):
        """Initializes a new Square instance with an optional size.

        Args:
            size (float or int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.

        """
        self.size = size

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
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.

        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Computes and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator based on square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator based on square area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator based on square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator based on square area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparator based on square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator based on square area."""
        return self.area() <= other.area()
