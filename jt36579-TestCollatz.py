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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_eval_single

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

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
        v = collatz_eval(5, 4)
        self.assertEqual(v, 6)

    def test_eval_6(self):
        v = collatz_eval(2, 2)
        self.assertEqual(v, 2)

    def test_eval_7(self):
        v = collatz_eval(4, 5)
        self.assertEqual(v, 6)

    # -----------
    # eval single
    # -----------

    def test_eval_single_1(self):
        v = collatz_eval_single(1)
        self.assertEqual(v, 1)

    def test_eval_single_2(self):
        v = collatz_eval_single(0)
        self.assertEqual(v, -1)

    def test_eval_single_3(self):
        v = collatz_eval_single(2)
        self.assertEqual(v, 2)

    def test_eval_single_4(self):
        v = collatz_eval_single(777)
        self.assertEqual(v, 34)

    def test_eval_single_5(self):
        v = collatz_eval_single(380)
        self.assertEqual(v, 108)

    def test_eval_single_6(self):
        v = collatz_eval_single(500)
        self.assertEqual(v, 111)

    def test_eval_single_7(self):
        v = collatz_eval_single(35)
        self.assertEqual(v, 14)

    def test_eval_single_8(self):
        v = collatz_eval_single(-3)
        self.assertEqual(v, -1)

    def test_eval_single_9(self):
        v = collatz_eval_single(980)
        self.assertEqual(v, 24)

    def test_eval_single_10(self):
        v = collatz_eval_single(99999)
        self.assertEqual(v, 227)

    def test_eval_single_11(self):
        v = collatz_eval_single(4)
        self.assertEqual(v, 3)

    def test_eval_single_12(self):
        v = collatz_eval_single(5)
        self.assertEqual(v, 6)
    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

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
