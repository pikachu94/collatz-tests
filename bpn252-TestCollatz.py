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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_max_range, collatz_check_range

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

    # tests written by ben

    def test_read_1(self):
        s = "100 200 \n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_2(self):
        s = "201 210 \n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)

    def test_read_3(self):
        s = "5  2\n"
        i, j = collatz_read(s)
        self.assertNotEqual(i, 1)
        self.assertNotEqual(j, 1)

    def test_read_4(self):
        s = "324234234  1111111\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 324234234)
        self.assertEqual(j, 1111111)

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

    # tests written by ben

    def test_eval_5(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_7(self):
        v = collatz_eval(5, 8)
        self.assertNotEqual(v, 20)

    def test_eval_8(self):
        v = collatz_eval(1, 1000000)
        self.assertEqual(v, 525)

    # ---------
    # max_range
    # ---------

    # to others in cs373: remove this if you are testing my unit tests

    def test_max_range_1(self):
        v = collatz_max_range(1, 10)
        self.assertEqual(v, 20)

    def test_max_range_2(self):
        v = collatz_max_range(10, 1)
        self.assertEqual(v, 20)

    def test_max_range_3(self):
        v = collatz_max_range(535474, 839606)
        self.assertEqual(v, 525)

    def test_max_range_4(self):
        v = collatz_max_range(535474, 839606)
        self.assertEqual(v, 525)

    # -----------
    # check_range
    # -----------

    # to others in cs373: remove this if you are testing my unit tests

    def test_check_range_1(self):
        v = collatz_check_range(5,9)
        self.assertEqual(v,[5,9])

    def test_check_range_2(self):
        v = collatz_check_range(6,3)
        self.assertEqual(v,[3,6])

    def test_check_range_3(self):
        v = collatz_check_range(1,10)
        self.assertEqual(v,[5,10])

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # tests written by ben

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, -5, 10, 1)
        self.assertEqual(w.getvalue(), "-5 10 1\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1, 10, 1)
        self.assertNotEqual(w.getvalue(), "1 10s 1\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(
            w, 10000000000000000000000000, 9999999999, 9324324234234234)
        self.assertEqual(
            w.getvalue(), "10000000000000000000000000 9999999999 9324324234234234\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # tests written by ben

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertNotEqual(
            w.getvalue(), "EXTRA STUFF 1 10 2\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("121 455\n47002 47666\n89 53468\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "121 455 144\n47002 47666 314\n89 53468 340\n")

    def test_solve_3(self):
        r = StringIO("121 455\n47002 47666\n89 53468\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertNotEqual(
            w.getvalue(), "")

    # sphere feeds in empty lines

    def test_solve_4(self):
        r = StringIO("          ")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "")

    def test_solve_5(self):
        r = StringIO("")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
ben@pride:~/Desktop/cs373-collatz$ coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1
ben@pride:~/Desktop/cs373-collatz$ cat TestCollatz.out
...............................
----------------------------------------------------------------------
Ran 31 tests in 57.527s

OK
ben@pride:~/Desktop/cs373-collatz$ coverage-3.5 report -m                   >> TestCollatz.out
ben@pride:~/Desktop/cs373-collatz$ cat TestCollatz.out
...............................
----------------------------------------------------------------------
Ran 31 tests in 57.527s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          58      0     24      1    99%   84->86
TestCollatz.py     126      0      0      0   100%
------------------------------------------------------------
TOTAL              184      0     24      1    99%

"""
