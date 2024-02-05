#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, class_to_check):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        class_to_check (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of class_to_check - True.
        Otherwise - False.
    """
    if type(obj) == class_to_check:
        return True
    return False
