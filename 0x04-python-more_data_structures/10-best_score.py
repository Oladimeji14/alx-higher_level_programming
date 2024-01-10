#!/usr/bin/python3

def best_score(dictionary):
    return max(dictionary, key=dictionary.get) if dictionary else None
