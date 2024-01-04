#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    
    # Create a dictionary mapping operators to corresponding functions
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    
    # Check if the provided operator is valid
    if argv[2] in operators:
        num1 = int(argv[1])
        num2 = int(argv[3])
        operator_func = operators[argv[2]]
        result = operator_func(num1, num2)
        print('{:d} {:s} {:d} = {:d}'.format(num1, argv[2], num2, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    
    exit(0)
