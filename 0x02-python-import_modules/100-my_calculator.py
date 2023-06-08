#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def handle_operation(a, operator, b):
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    a, operator, b = args
    a = int(a)
    b = int(b)

    handle_operation(a, operator, b)
