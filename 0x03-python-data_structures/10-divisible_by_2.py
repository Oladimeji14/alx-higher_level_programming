#!/usr/bin/python3

def divisible_by_2(input_list=[]):
    output_list = [False if num % 2 else True for num in input_list] if input_list else []
    return output_list
