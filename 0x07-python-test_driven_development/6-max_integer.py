#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(input_list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(input_list) == 0:
        return None
    result = input_list[0]
    i = 1
    while i < len(input_list):
        if input_list[i] > result:
            result = input_list[i]
        i += 1
    return result
