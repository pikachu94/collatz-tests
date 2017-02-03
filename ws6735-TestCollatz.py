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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, get_cycle_length, valid_for_cache

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        input_str = "1 10\n"
        i, j = collatz_read(input_str)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        input_str = "30 30\n"
        i, j = collatz_read(input_str)
        self.assertEqual(i, 30)
        self.assertEqual(j, 30)

    def test_read_3(self):
        input_str = "20 2\n"
        i, j = collatz_read(input_str)
        self.assertEqual(i, 20)
        self.assertEqual(j, 2)

    def test_read_4(self):
        input_str = "1 0\n"
        i, j = collatz_read(input_str)
        self.assertEqual(i, 1)
        self.assertEqual(j, 0)

    def test_read_5(self):
        input_str = "0 0\n"
        i, j = collatz_read(input_str)
        self.assertEqual(i, 0)
        self.assertEqual(j, 0)

    # ----
    # valid_for_cache
    # ----

    def test_valid_for_cache_1(self):
        result = valid_for_cache(1)
        self.assertEqual(result, True)

    def test_valid_for_cache_2(self):
        result = valid_for_cache(1000000)
        self.assertEqual(result, False)

    def test_valid_for_cache_3(self):
        result = valid_for_cache(999999)
        self.assertEqual(result, True)

    # ----
    # get_cycle_length
    # ----

    def test_get_cycle_length_1(self):
        cyc_len = get_cycle_length(1)
        self.assertEqual(cyc_len, 1)

    def test_get_cycle_length_2(self):
        cyc_len = get_cycle_length(2)
        self.assertEqual(cyc_len, 2)

    def test_get_cycle_length_3(self):
        cyc_len = get_cycle_length(10)
        self.assertEqual(cyc_len, 7)

    def test_get_cycle_length_4(self):
        cyc_len = get_cycle_length(56268)
        self.assertEqual(cyc_len, 110)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        value = collatz_eval(1, 1)
        self.assertEqual(value, 1)

    def test_eval_6(self):
        value = collatz_eval(2, 2)
        self.assertEqual(value, 2)

    def test_eval_7(self):
        value = collatz_eval(10, 1)
        self.assertEqual(value, 20)

    def test_eval_8(self):
        value = collatz_eval(200, 100)
        self.assertEqual(value, 125)
    # -----
    # print
    # -----

    def test_print_1(self):
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        writer = StringIO()
        collatz_print(writer, 1, 1, 1)
        self.assertEqual(writer.getvalue(), "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        input_str = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(input_str, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        input_str = StringIO("1 10\n")
        writer = StringIO()
        collatz_solve(input_str, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n")

    def test_solve_3(self):
        input_str = StringIO("\n\n1 10\n")
        writer = StringIO()
        collatz_solve(input_str, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n")

    def test_solve_4(self):
        input_str = StringIO("\n\n1 10\n  \n\n")
        writer = StringIO()
        collatz_solve(input_str, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n")

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
