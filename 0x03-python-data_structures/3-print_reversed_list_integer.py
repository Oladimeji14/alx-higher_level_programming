#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    [print("{:d}".format(elm)) for elm in reversed(my_list)] if my_list else None
