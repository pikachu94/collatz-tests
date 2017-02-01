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
import random
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_len

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_3(self):
        s = "210 201\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 210)
        self.assertEqual(j, 201)

    def test_read_4(self):
        s = "123456 54367"
        i, j = collatz_read(s)
        self.assertEqual(i, 123456)
        self.assertEqual(j, 54367)

    def test_read_5(self):
        s = "1 999999"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 999999)

    def test_read_6(self):
        s = " \n"
        i, j = collatz_read(s)
        self.assertEqual(i, -1)
        self.assertEqual(j, -1)

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
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    def test_eval_6(self):
        v = collatz_eval(7000, 5644)
        self.assertEqual(v, 262)

    def test_eval_7(self):
        v = collatz_eval(20000, 22222)
        self.assertEqual(v, 269)

    # ----
    # eval
    # ----

    def test_len_1(self):
        v = collatz_len(5)
        self.assertEqual(v, 6)

    def test_len_2(self):
        v = collatz_len(10)
        self.assertEqual(v, 7)

    def test_len_3(self):
        v = collatz_len(1)
        self.assertEqual(v, 1)

    def test_len_4(self):
        v = collatz_len(900)
        self.assertEqual(v, 55)

    def test_len_5(self):
        v = collatz_len(23456)
        self.assertEqual(v, 101)

    def test_len_6(self):
        v = collatz_len(12678)
        self.assertEqual(v, 56)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 100000, 1, 1)
        self.assertEqual(w.getvalue(), "100000 1 1\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 1, 999999, 525)
        self.assertEqual(w.getvalue(), "1 999999 525\n")

    def test_print_5(self):
        w = StringIO()
        collatz_print(w, 201, 210, 192)
        self.assertEqual(w.getvalue(), "201 210 192\n")

    def test_print_6(self):
        w = StringIO()
        collatz_print(w, 3678, 4523, 176)
        self.assertEqual(w.getvalue(), "3678 4523 176\n")

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
        r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_3(self):
        r = StringIO("10 10\n5 5\n1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 10 7\n5 5 6\n1 1 1\n")

    def test_solve_4(self):
        r = StringIO(" \n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

    def test_solve_5(self):
        r = StringIO("10 10\n100 200\n926 100\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 10 7\n100 200 125\n926 100 179\n")

    def test_solve_6(self):
        r = StringIO("1 999999\n\n525 1")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 999999 525\n525 1 144\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
