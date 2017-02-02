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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        string = "1 10\n"
        ith, jth = collatz_read(string)
        self.assertEqual(ith, 1)
        self.assertEqual(jth, 10)

    def test_read_2(self):
        string = "100 200\n"
        ith, jth = collatz_read(string)
        self.assertEqual(ith, 100)
        self.assertEqual(jth, 200)

    def test_read_3(self):
        string = "200 300\n"
        ith, jth = collatz_read(string)
        self.assertEqual(ith, 200)
        self.assertEqual(jth, 300)

    def test_read_4(self):
        string = "\n"
        ith, jth = collatz_read(string)
        self.assertEqual(ith, None)
        self.assertEqual(jth, None)

    # ----
    # cycle
    # ----

    def test_cycle_1(self):
        temp = cycle_length(1)
        self.assertEqual(temp, 1)

    def test_cycle_2(self):
        temp = cycle_length(10)
        self.assertEqual(temp, 7)

    def test_cycle_3(self):
        temp = cycle_length(11)
        self.assertEqual(temp, 15)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        temp = collatz_eval(999999, 1)
        self.assertEqual(temp, 525)

    def test_eval_2(self):
        temp = collatz_eval(100, 200)
        self.assertEqual(temp, 125)

    def test_eval_3(self):
        temp = collatz_eval(201, 210)
        self.assertEqual(temp, 89)

    def test_eval_4(self):
        temp = collatz_eval(900, 1000)
        self.assertEqual(temp, 174)

    def test_eval_5(self):
        temp = collatz_eval(1000, 900)
        self.assertEqual(temp, 174)

    def test_eval_6(self):
        temp = collatz_eval(10, 10)
        self.assertEqual(temp, 7)

    def test_eval_7(self):
        temp = collatz_eval(10, 1)
        self.assertEqual(temp, 20)

    def test_eval_8(self):
        temp = collatz_eval(113383, 113383)
        self.assertEqual(temp, 248)

    def test_eval_9(self):
        temp = collatz_eval(1, 10)
        self.assertEqual(temp, 20)

    def test_eval_11(self):
        temp = collatz_eval(112, 236)
        self.assertEqual(temp, 128)

    def test_eval_12(self):
        temp = collatz_eval(1, 1)
        self.assertEqual(temp, 1)

    def test_eval_13(self):
        temp = collatz_eval(151, 1)
        self.assertEqual(temp, 122)

    def test_eval_14(self):
        temp = collatz_eval(999999, 999999)
        self.assertEqual(temp, 259)

    def test_eval_15(self):
        temp = collatz_eval(151, 305)
        self.assertEqual(temp, 43)

    def test_eval_16(self):
        temp = collatz_eval(149, 305)
        self.assertEqual(temp, 43)

    def test_eval_17(self):
        temp = collatz_eval(299, 555555)
        self.assertEqual(temp, 470)

    def test_eval_18(self):
        temp = collatz_eval(50, 350)
        self.assertEqual(temp, 144)

    # -----
    # print
    # -----

    def test_print(self):
        write = StringIO()
        collatz_print(write, 1, 10, 20)
        self.assertEqual(write.getvalue(), '1 10 20\n')

    # -----
    # solve
    # -----

    def test_solve_1(self):
        read = StringIO('100 200\n201 210\n900 1000\n')
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), '100 200 125\n201 210 89\n900 1000 174\n')

    def test_solve_2(self):
        read = StringIO('1 10\n\n900 1000')
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), '1 10 20\n900 1000 174\n')

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
