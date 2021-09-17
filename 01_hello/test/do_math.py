# main.py
import sys

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        print(addition(a, b))
    if sys.argv[2] == "-":
        print(subtraction(a, b))
    if sys.argv[2] == "*":
        print(multiplication(a, b))
    if sys.argv[2] == "/":
        print(division(a, b))



if __name__ == "__main__":
    main()