"""This module will include all the unit tests for my Collatz."""

#!/usr/bin/enmax_cycle_valpython3

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
    """This class is for unit testings"""
    # ----
    # read
    # ----

    def test_read_1(self):
        """
        read in two integers and check if the read is correct
        """
        input_str = "1 10\n"
        i, j = collatz_read(input_str)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        """
        read in two integers and check if the read is correct
        """
        input_str = "500 1000\n"
        i, j = collatz_read(input_str)
        self.assertEqual(i, 500)
        self.assertEqual(j, 1000)

    def test_read_3(self):
        """
        read in two integers and check if the read is correct
        """
        input_str = "25 25\n"
        i, j = collatz_read(input_str)
        self.assertEqual(i, 25)
        self.assertEqual(j, 25)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        compute the 2 input ints for the max cycle length
        assert if the max cycle length is correct
        """
        max_cycle_val = collatz_eval(1, 10)
        self.assertEqual(max_cycle_val, 20)

    def test_eval_2(self):
        """
        compute the 2 input ints for the max cycle length
        assert if the max cycle length is correct
        """
        max_cycle_val = collatz_eval(100, 200)
        self.assertEqual(max_cycle_val, 125)

    def test_eval_3(self):
        """
        compute the 2 input ints for the max cycle length
        assert if the max cycle length is correct
        """
        max_cycle_val = collatz_eval(1000, 900)
        self.assertEqual(max_cycle_val, 174)

    # ----------------
    # max cycle length
    # ----------------

    def test_cycle_1(self):
        """
        compute the 2 input ints for the max cycle length
        assert if the max cycle length is correct
        """
        max_cycle_val = cycle_length(1)
        self.assertEqual(max_cycle_val, 1)

    def test_cycle_2(self):
        """
        compute the 2 input ints for the max cycle length
        assert if the max cycle length is correct
        """
        max_cycle_val = cycle_length(2)
        self.assertEqual(max_cycle_val, 2)

    def test_cycle_3(self):
        """
        compute the 2 input ints for the max cycle length
        assert if the max cycle length is correct
        """
        max_cycle_val = cycle_length(500000)
        self.assertEqual(max_cycle_val, 152)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        print out the input values and the max cycle length
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        print out the input values and the max cycle length
        """
        writer = StringIO()
        collatz_print(writer, 100, 200, 125)
        self.assertEqual(writer.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """
        print out the input values and the max cycle length
        """
        writer = StringIO()
        collatz_print(writer, 201, 210, 89)
        self.assertEqual(writer.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        testing multiple pairs of ints and comparing it to the expected output
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        testing multiple pairs of ints and comparing it to the expected output
        """
        reader = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_3(self):
        """
        testing multiple pairs of ints and comparing it to the expected output
        """
        reader = StringIO(" ")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "")

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
