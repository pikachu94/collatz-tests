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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, find_cycle_helper, find_cycle_length

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "200 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  200)
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
    
    def test_eval_5(self):
        v = collatz_eval(1000,900)
        self.assertEqual(v, 174)

    def test_eval_6(self):
        v = collatz_eval(10,1)
        self.assertEqual(v, 20)

    def test_eval_7(self):
        v = collatz_eval(566157,889789)
        self.assertEqual(v, 525)


    # -----
    # cycle
    # -----

    def test_cycle_1(self):
        v = find_cycle_helper({1: 1}, 1, 10)
        self.assertEqual(v, 20)

    def test_cycle_2(self):
        v = find_cycle_helper({1: 1}, 100, 200)
        self.assertEqual(v, 125)

    def test_cycle_3(self):
        v = find_cycle_helper({1: 1}, 900, 1000)
        self.assertEqual(v, 174)

    def test_cycle_4(self):
        v = find_cycle_length(1, {1: 1})
        self.assertEqual(v, 1)

    def test_cycle_5(self):
        v = find_cycle_length(2, {1: 1})
        self.assertEqual(v, 2)

    def test_cycle_6(self):
        v = find_cycle_length(3, {1: 1})
        self.assertEqual(v, 8)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

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

# ----
# main
# ----

if __name__ == "__main__":
    main()


