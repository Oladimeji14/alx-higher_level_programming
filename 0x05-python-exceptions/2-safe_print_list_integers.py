#!/usr/bin/python3
def custom_print_list_integers(custom_list=[], limit=0):
    count = 0
    for idx in range(limit):
        try:
            print("{:d}".format(custom_list[idx]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return
