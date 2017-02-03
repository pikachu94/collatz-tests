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

import sys
# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_1(self):
        s = "3 34\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  3)
        self.assertEqual(j, 34)

    def test_read_2(self):
        s = "90 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  90)
        self.assertEqual(j, 100)

    def test_read_3(self):
        s = "90123 31290\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  90123)
        self.assertEqual(j, 31290)

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
        v = collatz_eval(710776, 59321)
        self.assertEqual(v, 509)

    def test_eval_6(self):
        v = collatz_eval(63400, 498014)
        self.assertEqual(v, 449)

    def test_eval_7(self):
        v = collatz_eval(968678, 300967)
        self.assertEqual(v, 525)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")
    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 63400, 498014, 449)
        self.assertEqual(w.getvalue(), "63400 498014 449\n")

    # -----
    # solve
    # -----
    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1(self):
        r = StringIO("509202 124798\n543463 329903\n 440407 240549\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "509202 124798 449\n543463 329903 470\n440407 240549 449\n")
    def test_solve_2(self):
        r = StringIO("153113 340535\n590019 965327\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "153113 340535 443\n590019 965327 525\n")
    def test_solve_3(self):
        r = StringIO("591485 849788\n186887 489654\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "591485 849788 525\n186887 489654 449\n")
    def test_solve_4(self):
        r = StringIO("209554 59117\n49733 371607\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "209554 59117 383\n49733 371607 443\n")

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