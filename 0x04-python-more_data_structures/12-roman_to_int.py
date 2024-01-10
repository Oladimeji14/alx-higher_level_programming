#!/usr/bin/python3

def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_values = [roman_numerals[char] for char in roman_string] + [0]
    result = 0

    for i in range(len(numeral_values) - 1):
        if numeral_values[i] >= numeral_values[i + 1]:
            result += numeral_values[i]
        else:
            result -= numeral_values[i]

    return result
