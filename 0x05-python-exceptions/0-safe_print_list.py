#!/usr/bin/python3

def custom_print_list(input_list=[], limit=0):
    count = 0
    for index in range(limit):
        try:
            print(input_list[index], end="")
            count += 1
        except IndexError:
            break
    print("")

# Example Usage:
my_custom_list = ["apple", "banana", "cherry", "date"]
custom_print_list(my_custom_list, 3)
