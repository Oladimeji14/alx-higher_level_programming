#!/usr/bin/python3

def print_sorted_dictionary(dictionary):
    for key in sorted(dictionary.keys()):
        print("{}: {}".format(key, dictionary[key]))
