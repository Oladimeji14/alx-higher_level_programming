#!/usr/bin/python3
def uppercase(s):
    """Prints a string in uppercase followed by a new line."""
    for char in s:
        print("{:c}".format(ord(char) - 32) if 'a' <= char <= 'z' else char, end="")
    print()
