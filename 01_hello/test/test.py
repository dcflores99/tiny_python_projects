#!/usr/bin/env python3
"""tests for hello.py"""

import os
from do_math import addition
from do_math import division
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

def main():
    test_addition()

if __name__ == "__main__":
    main()