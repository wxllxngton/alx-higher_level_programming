#!/usr/bin/python3

"""
Module: 100
"""

class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The next node in the linked list.

    Methods:
        __init__(data, next_node=None): Initializes a Node instance with the given data and next node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance with the given data and next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The next node in the linked list (default is None).

        Raises:
            TypeError: If the provided data is not an integer.
            TypeError: If the provided next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If the provided data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If the provided next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.

    Methods:
        __init__(): Initializes an empty SinglyLinkedList.
        sorted_insert(value): Inserts a new node into the linked list in the correct sorted position.
        __str__(): Returns a string representation of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty SinglyLinkedList.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node into the linked list in the correct sorted position.

        Args:
            value (int): The value of the node to be inserted.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
