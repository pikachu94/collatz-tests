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

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read2(self):
        s = "1000 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1000)
        self.assertEqual(j, 1000)

    def test_read3(self):
        s = "10000000000 999999999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10000000000)
        self.assertEqual(j, 999999999999)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(10000, 999)
        self.assertEqual(v, 262)

    def test_eval_6(self):
        v = collatz_eval(6171, 6171)
        self.assertEqual(v, 262)

    def test_eval_7(self):
        v = collatz_eval(10000, 100000)
        self.assertEqual(v, 351)

    def test_eval_8(self):
        v = collatz_eval(777, 777)
        self.assertEqual(v, 34)

    def test_eval_9(self):
        v = collatz_eval(10000, 1000000)
        self.assertEqual(v, 525)

    def test_eval_10(self):
        v = collatz_eval(1, 1000000)
        self.assertEqual(v, 525)

    # -----
    # print
    # -----

    def test_print1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print3(self):
        w = StringIO()
        collatz_print(w, 1000, 1023, 24)
        self.assertEqual(w.getvalue(), "1000 1023 24\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        r = StringIO("1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n")

    def test_solve3(self):
        r = StringIO("500 599\n123 1234\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "500 599 137\n123 1234 182\n")

    def test_solve_rev(self):
        r = StringIO("10000 999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10000 999 262\n")

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
