#!/usr/bin/python3
"""
Defines a text-indentation function.
"""


def text_indentation(input_text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args:
        input_text (str): The text to print.
        
    Raises:
        TypeError: If input_text is not a string.
    """
    if not isinstance(input_text, str):
        raise TypeError("input_text must be a string")

    c = 0
    while c < len(input_text) and input_text[c] == ' ':
        c += 1

    while c < len(input_text):
        print(input_text[c], end="")
        if input_text[c] == "\n" or input_text[c] in ".?:":
            if input_text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(input_text) and input_text[c] == ' ':
                c += 1
            continue
        c += 1
