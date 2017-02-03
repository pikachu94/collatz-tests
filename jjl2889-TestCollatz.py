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


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    # Personally added tests
    def test_read2(self):
        s = "1 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 999999)
    def test_read3(self):
        s = "200000 400000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  200000)
        self.assertEqual(j, 400000)
    def test_read4(self):
        s = "100 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 100)

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

    # Personally added tests
    def test_eval_5(self):
        v = collatz_eval(1,999999)
        self.assertEqual(v,525)
    def test_eval_6(self):
        v = collatz_eval(10000,20000)
        self.assertEqual(v,279)
    # Check to see if it gracefully handles
    # an incorrect range
    def test_eval_7(self):
        v = collatz_eval(100,0)
        self.assertEqual(v,119)

    # -----
    # print
    # -----

    def test_print1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # Personally added tests
    def test_print2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")
    def test_print3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")
    def test_print4(self):
        w = StringIO()
        collatz_print(w, 1, 999999, 525)
        self.assertEqual(w.getvalue(), "1 999999 525\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # Personally added tests
    def test_solve2(self):
        r = StringIO("500000 600000\n500000 700000\n500000 800000\n500000 900000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "500000 600000 470\n500000 700000 509\n500000 800000 509\n500000 900000 525\n")

    def test_solve3(self):
        r = StringIO("1 2\n2 3\n3 4\n4 5\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 2 2\n2 3 8\n3 4 8\n4 5 6\n")

    def test_solve4(self):
        r = StringIO("50 100\n150 200\n250 300\n350 400\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "50 100 119\n150 200 125\n250 300 123\n350 400 126\n")

    def test_solve5(self):
        r = StringIO("0 0\n0 1\n-100 0\n-200 200\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "0 0 0\n0 1 1\n-100 0 0\n-200 200 125\n")

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
