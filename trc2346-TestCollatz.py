#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

'''
This module tests Collatz.py functions.
'''

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_calc

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):

    '''
    Contains test cases for Collatz.py
    '''
    # ----
    # read
    # ----

    def test_read(self):
        '''
        Test a basic read case.
        '''
        line = "1 10\n"
        ival, jval = collatz_read(line)
        self.assertEqual(ival, 1)
        self.assertEqual(jval, 10)

    # ----
    # calc
    # ----

    def test_calc_1(self):
        '''
        Test base case.
        '''
        vval = collatz_calc(1)
        self.assertEqual(vval, 1)

    def test_calc_2(self):
        '''
        Test a small number.
        '''
        vval = collatz_calc(10)
        self.assertEqual(vval, 7)

    def test_calc_3(self):
        '''
        Test a large number.
        '''
        vval = collatz_calc(999999)
        self.assertEqual(vval, 259)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        '''
        Test a known range.
        '''
        vval = collatz_eval(1, 10)
        self.assertEqual(vval, 20)

    def test_eval_2(self):
        '''
        Test a known range.
        '''
        vval = collatz_eval(100, 200)
        self.assertEqual(vval, 125)

    def test_eval_3(self):
        '''
        Test a known range..
        '''
        vval = collatz_eval(201, 210)
        self.assertEqual(vval, 89)

    def test_eval_4(self):
        '''
        Test a higher numbered range.
        '''
        vval = collatz_eval(900, 1000)
        self.assertEqual(vval, 174)

    def test_eval_5(self):
        '''
        Test reversed number order.
        '''
        vval = collatz_eval(200, 100)
        self.assertEqual(vval, 125)

    def test_eval_6(self):
        '''
        Test where start and end are the same.
        '''
        vval = collatz_eval(500, 500)
        self.assertEqual(vval, 111)

    def test_eval_7(self):
        '''
        Test entire valid range.
        '''
        vval = collatz_eval(1, 999999)
        self.assertEqual(vval, 525)

    def test_eval_8(self):
        '''
        Test a single meta-cache range.
        '''
        vval = collatz_eval(1, 1000)
        self.assertEqual(vval, 179)

    def test_eval_9(self):
        '''
        Test a range that partially covers two meta-cache ranges.
        '''
        vval = collatz_eval(1002, 2999)
        self.assertEqual(vval, 217)

    def test_eval_10(self):
        '''
        Test a range that does not cover the first meta-cache
        range but covers the entire last range.
        '''
        vval = collatz_eval(1002, 3000)
        self.assertEqual(vval, 217)

    # -----
    # print
    # -----

    def test_print(self):
        '''
        Test a basic print case.
        '''
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        '''
        Test a basic input sample.
        '''
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        '''
        Test the basic input sample with the i and j values reversed.
        '''
        reader = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_3(self):
        '''
        Test the basic input sample with an empty line inserted.
        '''
        reader = StringIO("1 10\n100 200\n\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

# pylint: disable=W0105
'''
I am getting a warning about
'String statement has no effect'
because of this comment block.
Temporarily disabling warning.
'''
""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1

% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK

% coverage-3.5 report -m                   >> TestCollatz.out

% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
# pylint: enable=W0105
