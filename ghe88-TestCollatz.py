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
import functools

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

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

    # test added
    def test_read_1(self):
        s = "1 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 999999)

    # test added
    def test_read_2(self):
        s = "0 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 1)

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

    # test added
    def test_eval_5(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)
    """
    #test added
    def test_eval_6(self):
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)
    """
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

    # test added
    def test_solve_2(self):
        r = StringIO("1 1\n1 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n1 10000 262\n")

    # test added
    def test_solve_3(self):
        r = StringIO("10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n")

    # test added
    def test_solve_4(self):
        r = StringIO("1 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 999999 525\n")

    # test added
    def test_solve_5(self):
        r = StringIO(
            "697967 581514\n397453 357688\n246243 583987\n148824 161769\n861515 116192\n647847 668866\n196600 581551\n853620 903447\n863502 107428\n659289 259417\n906402 244848\n95060 913610\n565430 749654\n689642 399266\n434306 520342\n895922 851501\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "697967 581514 509\n397453 357688 436\n246243 583987 470\n148824 161769 383\n861515 116192 525\n647847 668866 442\n196600 581551 470\n853620 903447 445\n863502 107428 525\n659289 259417 509\n906402 244848 525\n95060 913610 525\n565430 749654 509\n689642 399266 509\n434306 520342 470\n895922 851501 445\n")

    # test added
    def test_solve_4(self):
        r = StringIO(
            "900 1000\n100 200\n397453 357688\n647847 668866\n895922 851501\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "900 1000 174\n100 200 125\n397453 357688 436\n647847 668866 442\n895922 851501 445\n")

    # test added
    def test_solve_5(self):
        r = StringIO(" ")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "")

    # test added
    def test_solve_6(self):
        r = StringIO("1 10\n6 10\n10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n6 10 20\n10 1 20\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1
% cat TestCollatz.out
% coverage-3.5 report -m                   >> TestCollatz.out
% cat TestCollatz.out
"""
