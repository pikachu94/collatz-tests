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

    def test_read(self):
        str_input = "1 10\n"
        i_read, j_read = collatz_read(str_input)
        self.assertEqual(i_read, 1)
        self.assertEqual(j_read, 10)

    def test_read_2(self):
        str_input = "100 200"
        i_read, j_read = collatz_read(str_input)
        self.assertEqual(i_read, 100)
        self.assertEqual(j_read, 200)

    def test_read_3(self):
        str_input = "201 210"
        i_read, j_read = collatz_read(str_input)
        self.assertEqual(i_read, 201)
        self.assertEqual(j_read, 210)

    def test_read_4(self):
        str_input = "900 1000"
        i_read, j_read = collatz_read(str_input)
        self.assertEqual(i_read, 900)
        self.assertEqual(j_read, 1000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        max_cycle = collatz_eval(100, 200)
        self.assertEqual(max_cycle, 125)

    def test_eval_3(self):
        max_cycle = collatz_eval(201, 210)
        self.assertEqual(max_cycle, 89)

    def test_eval_4(self):
        max_cycle = collatz_eval(900, 1000)
        self.assertEqual(max_cycle, 174)

    def test_eval_5(self):
        max_cycle = collatz_eval(95, 10)
        self.assertEqual(max_cycle, 116)

    # -----
    # print
    # -----

    def test_print(self):
        w_input = StringIO()
        collatz_print(w_input, 1, 10, 20)
        self.assertEqual(w_input.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w_input = StringIO()
        collatz_print(w_input, 100, 200, 125)
        self.assertEqual(w_input.getvalue(), "100 200 125\n")

    def test_print_3(self):
        w_input = StringIO()
        collatz_print(w_input, 201, 210, 89)
        self.assertEqual(w_input.getvalue(), "201 210 89\n")

    def test_print_4(self):
        w_input = StringIO()
        collatz_print(w_input, 900, 1000, 174)
        self.assertEqual(w_input.getvalue(), "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 10\n100 200\n\n201 210\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n")

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
