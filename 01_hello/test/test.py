#!/usr/bin/env python3
"""tests for do_math.py"""

import os
from do_math import addition, division, main
from subprocess import getstatusoutput, getoutput

prg = './do_math.py'

def test_addition():
    assert addition(1, 2) == 3
    assert addition(3, 3) == 6
    assert addition(0, 0) == 0
    assert addition(0, 3) == 3
    assert addition(0, -3) == -3
    assert addition(-2, -5) == -7
    assert addition(2, -5) == -3

def test_division():
    assert division(4, 2) == 2
    assert division(0, 3) == 0
    assert division(3, 0) == None
    assert division(-3, 1) == -3
    assert division(-6, -2) == 3
    assert division(5, 2) == 2.5
    assert division(1, 4) == 0.25
    assert division(-1, 4) == -0.25
    assert division(5, -2) == -2.5
    assert division(-5, -2) == 2.5
    assert division(-1, -4) == 0.25


def get_output(a, op, b):
    if b == 0 and op == "/":
        return None
    return float(getoutput(f'python3 {prg} {a} {op} {b}').strip())

def get_answers(op, answers):
    for i in range(-1, 2):
        for j in range(-1, 2):
            assert get_output(i, op, j) == answers[0]
            answers.pop(0)

def test_main():
    add_answers = [-2, -1, 0, -1, 0, 1, 0, 1, 2]
    sub_answers = [0, -1, -2, 1, 0, -1, 2, 1, 0]
    mul_answers = [1, 0, -1, 0, 0, 0, -1, 0, 1]
    div_answers = [1, None, -1, 0, None, 0, -1, None, 1]
    get_answers("+", add_answers)
    get_answers("-", sub_answers)
    get_answers("mult", mul_answers)
    get_answers("/", div_answers)

def main():
    test_addition()

if __name__ == "__main__":
    main()