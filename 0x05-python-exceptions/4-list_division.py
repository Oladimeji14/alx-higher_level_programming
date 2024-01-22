#!/usr/bin/python3
def custom_safe_division(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
