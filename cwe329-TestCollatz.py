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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length

"""
TestCollatz.py tests Collatz.py
"""
# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """
    The following are unit tests that test functions in Collatz.py
    """

    # ----
    # read
    # ----

    def test_read_1(self):
        """ Test 1 10 """
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        """ Test 100 200 """
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_3(self):
        """ Test 201 210 """
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """ Test 1 10 """
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        """ Test 100 200 """
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        """ Test 201 210 """
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        """ Test 900 1000 """
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # -----
    # print
    # -----

    def test_print_1(self):
        """ Test 1 10 20 """
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """ Test 100 200 125 """
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """ Test 201 210 89 """
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """ Test solve for set 1 """
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """ Test solve for set 2 """
        r = StringIO("1 10\n10 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n10 10 7\n")

    def test_solve_3(self):
        """ Test solve for set 3 (reverse input)"""
        r = StringIO("10 1\n1 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n1 10 20\n")

    def test_solve_4(self):
        """ Test solve for set 4 (zero length ranges)"""
        r = StringIO("1 1\n2 2\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n2 2 2\n")

    def test_solve_5(self):
        """ Test solve for set 5 (blank line)"""
        r = StringIO("\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

    # --------------------
    # collatz_cycle_length
    # --------------------

    def test_collatz_cycle_length_1(self):
        """ Test edge case 1 """
        l = collatz_cycle_length(1)
        self.assertEqual(l, 1)

    def test_collatz_cycle_length_2(self):
        """ Test edge case 2 """
        l = collatz_cycle_length(2)
        self.assertEqual(l, 2)

    def test_collatz_cycle_length_3(self):
        """ Test edge case 1 """
        l = collatz_cycle_length(3)
        self.assertEqual(l, 8)

    def test_collatz_cycle_length_4(self):
        """ Test 10 """
        l = collatz_cycle_length(10)
        self.assertEqual(l, 7)

    def test_collatz_cycle_length_5(self):
        """ Test edge case 999999 """
        l = collatz_cycle_length(999999)
        self.assertEqual(l, 259)

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover """
