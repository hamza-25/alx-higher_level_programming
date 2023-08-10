#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys
if __name__ == "__main__":
    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    oper = sys.argv[2]
    fun_oper = {"+": add, "-": sub, "*": mul, "/": div}
    if oper not in fun_oper:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, oper, b, fun_oper[oper](a, b)))
