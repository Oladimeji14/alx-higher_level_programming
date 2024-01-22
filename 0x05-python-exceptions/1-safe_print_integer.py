#!/usr/bin/python3

def custom_print_number(input_value):
    try:
        print("{:d}".format(input_value))
        return True
    except (ValueError, TypeError):
        return False
