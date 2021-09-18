# main.py
import sys

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return None
    else:
        return a / b


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        return addition(a, b)
    if sys.argv[2] == "-":
        return subtraction(a, b)
    if sys.argv[2] == "mult":
        return multiplication(a, b)
    if sys.argv[2] == "/":
        return division(a, b)



if __name__ == "__main__":
    print(main())