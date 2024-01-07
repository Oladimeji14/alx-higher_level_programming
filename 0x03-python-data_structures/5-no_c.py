#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for element in my_string:
        if element.lower() != "c":
            new_string += element
    return new_string
