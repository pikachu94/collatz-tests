#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

"""
Unit tests for Collatz.py
"""
# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    Tests for various methods in Collatz.py
    """
    # ----
    # read
    # ----

    def test_read1(self):
        """
        collatz_read unit test
        """
        line = "1 10\n"
        i, j = collatz_read(line)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read2(self):
        """
        collatz_read unit test
        """
        line = "100 10\n"
        i, j = collatz_read(line)
        self.assertEqual(i, 100)
        self.assertEqual(j, 10)

    def test_read3(self):
        """
        collatz_read unit test
        """
        line = "1 99999\n"
        i, j = collatz_read(line)
        self.assertEqual(i, 1)
        self.assertEqual(j, 99999)
    # ----
    # eval
    # ----
    def test_eval_1(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(1, 10)
        self.assertEqual(num, 20)

    def test_eval_2(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(100, 200)
        self.assertEqual(num, 125)

    def test_eval_3(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(201, 210)
        self.assertEqual(num, 89)

    def test_eval_4(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(900, 1000)
        self.assertEqual(num, 174)

    def test_eval_5(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(1, 1)
        self.assertEqual(num, 1)

    def test_eval_6(self):
        """
        collatz_eval unit test
        """
        with self.assertRaises(AssertionError):
            collatz_eval(1, 1000000000000)

    def test_eval_7(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval("\n", "don't work")
        self.assertEqual(num, -1)

    def test_eval_8(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(10, 1)
        self.assertEqual(num, 20)

    def test_eval_9(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(999998, 999999)
        self.assertEqual(num, 259)

    def test_eval10(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(1, 100000)
        self.assertEqual(num, 351)

    def test_eval11(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(1, 999999)
        self.assertEqual(num, 525)

    def test_eval12(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(500000, 999999)
        self.assertEqual(num, 525)

    def test_eval13(self):
        """
        collatz_eval unit test
        """
        num = collatz_eval(500000, "fail")
        self.assertEqual(num, -1)
    # -----
    # print
    # -----

    def test_print1(self):
        """
        collatz_print unit test
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print2(self):
        """
        collatz_print unit test
        """
        writer = StringIO()
        collatz_print(writer, 2, 20, 40)
        self.assertEqual(writer.getvalue(), "2 20 40\n")

    def test_print3(self):
        """
        collatz_print unit test
        """
        writer = StringIO()
        collatz_print(writer, 40, 10, 10)
        self.assertEqual(writer.getvalue(), "40 10 10\n")

    # -----
    # solve
    # -----
    def test_solve1(self):
        """
        collatz_solve unit test
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        """
        collatz_solve unit test
        """
        reader = StringIO("953742 921015\n77706 527706\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "953742 921015 507\n77706 527706 470\n")

    def test_solve3(self):
        """
        collatz_solve unit test
        """
        reader = StringIO("332296 5781\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "332296 5781 443\n")

    def test_solve4(self):
        """
        collatz_solve unit test
        """
        reader = StringIO("   \n")
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
