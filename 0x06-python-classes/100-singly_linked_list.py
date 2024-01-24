#!/usr/bin/python3
"""this is for the actual task at hand"""


class Node:
    """Class to define a node of a singly linked list.

    This class for node of private instance attribute data and next_node

    Attributes:
        data (int): Private instance attribute representing the data of node
        next_node (Node): Private instance for the next node in linked list.

    """

    def __init__(self, data, n_node=None):
        """Initializes a new Node instance with data and optional next_node.

        Args:
            data (int): The data for the node.
            next_node : The next node in the linked list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node

        """
        self.data = data
        self.n_node = n_node

    @property
    def data(self):
        """Getter property for the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter property for the data of the node.

        Args:
            value: The data to set.

        Raises:
            TypeError: If value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Getter property for the next node in the linked list."""
        return self.__n_node

    @next_node.setter
    def next_node(self, value):
        """Setter property for the next node in the linked list.

        Args:
            value: The next node to set.

        Raises:
            TypeError: If value is not a Node.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__n_node = value


"""this is for the singly linked list"""


class SinglyLinkedList:
    """Class to define a singly linked list.

    This class for linked list with private instance attribute `head`.

    """

    def __init__(self):
        """Simple instantiation of a SinglyLinkedList."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node in correct sorted position in list (incre order).

        Args:
            value: The value to be inserted into the list.

        """
        new_node = Node(value)

        if self.head is None or self.head.data > value:
            new_node.n_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.n_node is not None and current.n_node.data < value:
                current = current.n_node

            new_node.n_node = current.n_node
            current.n_node = new_node

    def __str__(self):
        """Prints the entire list in stdout, one node number per line."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.n_node
        return result.rstrip()
