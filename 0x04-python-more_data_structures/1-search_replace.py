#!/usr/bin/python3

def search_replace(lst, target, replacement):
    return [replacement if element == target else element for element in lst]
