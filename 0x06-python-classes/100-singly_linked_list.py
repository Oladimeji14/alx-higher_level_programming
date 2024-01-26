#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, value, next_node=None):
        """Initialize a new Node.

        Args:
            value (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = value
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError("data must be an integer")
        self.__data = new_value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, new_next_node):
        if not isinstance(new_next_node, Node) and new_next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = new_next_node


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, new_value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            new_value (int): The new Node to insert.
        """
        new_node = Node(new_value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > new_value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < new_value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
