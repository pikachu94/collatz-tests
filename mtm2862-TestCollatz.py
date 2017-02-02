#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------
''' Tests the collatz program '''

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, do_collatz

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    ''' Main tests for each function of collatz '''
    # ----
    # read
    # ----

    def test_read_1(self):
        ''' Test read 1 '''
        start = "1 10\n"
        i, j = collatz_read(start)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        ''' Test read 2 '''
        start = "1 1\n"
        i, j = collatz_read(start)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)

    def test_read_3(self):
        ''' Test read 3 '''
        start = "999999 0\n"
        i, j = collatz_read(start)
        self.assertEqual(i, 999999)
        self.assertEqual(j, 0)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        ''' Test eval 1 '''
        result = collatz_eval(1, 10)
        self.assertEqual(result, 20)

    def test_eval_2(self):
        ''' Test eval 2 '''
        result = collatz_eval(100, 200)
        self.assertEqual(result, 125)

    def test_eval_3(self):
        ''' Test eval 3 '''
        result = collatz_eval(201, 210)
        self.assertEqual(result, 89)

    def test_eval_4(self):
        ''' Test eval 4 '''
        result = collatz_eval(900, 1000)
        self.assertEqual(result, 174)

    def test_eval_5(self):
        ''' Test eval 5 '''
        result = collatz_eval(1, 1)
        self.assertEqual(result, 1)

    def test_eval_6(self):
        ''' Test eval 6 '''
        result = collatz_eval(500, 1)
        self.assertEqual(result, 144)

    def test_eval_7(self):
        ''' Test eval 7 '''
        result = collatz_eval(1, 5000)
        self.assertEqual(result, 238)

    def test_eval_8(self):
        ''' Test eval 8 '''
        self.assertRaises(AssertionError, collatz_eval, -1, -5)
        # This should fail

    def test_eval_9(self):
        ''' Test eval 9 '''
        result = collatz_eval(1, 999999)
        self.assertEqual(result, 525)

    def test_eval_10(self):
        ''' Test eval 10 '''
        result = collatz_eval(10971, 11999)
        self.assertEqual(result, 268)

    # ----
    # do_collatz
    # ----

    def test_do_1(self):
        ''' Test do 1 '''
        result = do_collatz(1)
        self.assertEqual(result, 1)

    def test_do_2(self):
        ''' Test do 2 '''
        result = do_collatz(55405)
        self.assertEqual(result, 79)

    def test_do_3(self):
        ''' Test do 3 '''
        result = do_collatz(999999)
        self.assertEqual(result, 259)

    # -----
    # print
    # -----

    def test_print_1(self):
        ''' Test print 1 '''
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        ''' Test print 2 '''
        writer = StringIO()
        collatz_print(writer, 8, 2, 500)
        self.assertEqual(writer.getvalue(), "8 2 500\n")

    def test_print_3(self):
        ''' Test print 3 '''
        writer = StringIO()
        collatz_print(writer, 999999, 0, 1)
        self.assertEqual(writer.getvalue(), "999999 0 1\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        ''' Test solve 1 '''
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        ''' Test solve 2 '''
        reader = StringIO("900 1000\n1 1\n500 1\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "900 1000 174\n1 1 1\n500 1 144\n")

    def test_solve_3(self):
        ''' Test solve 3 '''
        reader = StringIO("584 585\n586 587\n588 589\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "584 585 119\n586 587 119\n588 589 119\n")

    def test_solve_4(self):
        ''' Test solve 4 '''
        reader = StringIO("        \n")
        writer = StringIO()
        collatz_solve(reader, writer)

# ----
# main
# ----

if __name__ == "__main__":
    main()

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
