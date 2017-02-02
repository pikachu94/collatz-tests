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

"""To read and write strings"""
from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):

    """Test Case Class"""
    # ----
    # read
    # ----

    def test_read(self):
        """test case input for 1 10"""
        string = "1 10\n"
        num1, num2 = collatz_read(string)
        self.assertEqual(num1, 1)
        self.assertEqual(num2, 10)

    # My test cases

    def test_read1(self):
        """test case input for 100 200"""
        string = "100 200\n"
        num1, num2 = collatz_read(string)
        self.assertEqual(num1, 100)
        self.assertEqual(num2, 200)

    def test_read2(self):
        """test case input for 201 210"""
        string = "201 210\n"
        num1, num2 = collatz_read(string)
        self.assertEqual(num1, 201)
        self.assertEqual(num2, 210)

    def test_read3(self):
        """test case input for 900 1000"""
        string = "900 1000\n"
        num1, num2 = collatz_read(string)
        self.assertEqual(num1, 900)
        self.assertEqual(num2, 1000)

    def test_read4(self):
        """test case input for 1 1"""
        string = "1 1\n"
        num1, num2 = collatz_read(string)
        self.assertEqual(num1, 1)
        self.assertEqual(num2, 1)

    def test_read5(self):
        """test case input for empty line"""
        string = "\n"
        num1, num2 = collatz_read(string)
        self.assertEqual(num1, -1)
        self.assertEqual(num2, -1)
    # ----
    # eval
    # ----

    def test_eval_1(self):
        """test case eval for 1 10 20"""
        maxcycles = collatz_eval(1, 10)
        self.assertEqual(maxcycles, 20)

    def test_eval_2(self):
        """test case eval for 100 200 125"""
        maxcycles = collatz_eval(100, 200)
        self.assertEqual(maxcycles, 125)

    def test_eval_3(self):
        """test case eval for 201 210 89"""
        maxcycles = collatz_eval(201, 210)
        self.assertEqual(maxcycles, 89)

    def test_eval_4(self):
        """test case eval for 900 1000 174"""
        maxcycles = collatz_eval(900, 1000)
        self.assertEqual(maxcycles, 174)

    # My test cases

    def test_eval_5(self):
        """test case eval for 500 1500 182"""
        maxcycles = collatz_eval(500, 1500)
        self.assertEqual(maxcycles, 182)

    def test_eval_6(self):
        """test case eval for 1000 2001 182"""
        maxcycles = collatz_eval(1000, 2001)
        self.assertEqual(maxcycles, 182)

    def test_eval_7(self):
        """test case eval for 1 1 1"""
        maxcycles = collatz_eval(1, 1)
        self.assertEqual(maxcycles, 1)

    def test_eval_8(self):
        """test case eval for 5000 15000 276"""
        maxcycles = collatz_eval(5000, 15000)
        self.assertEqual(maxcycles, 276)

    def test_eval_9(self):
        """test case eval for 1 5000000 597"""
        maxcycles = collatz_eval(1, 5000000)
        self.assertEqual(maxcycles, 597)
    # -----
    # print
    # -----

    def test_print(self):
        """test case eval for range 1 10 20"""
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # My Test Cases

    def test_print1(self):
        """test case eval for range 100 200 125"""
        writer = StringIO()
        collatz_print(writer, 100, 200, 125)
        self.assertEqual(writer.getvalue(), "100 200 125\n")

    def test_print2(self):
        """test case eval for range 201 210 89"""
        writer = StringIO()
        collatz_print(writer, 201, 210, 89)
        self.assertEqual(writer.getvalue(), "201 210 89\n")

    def test_print3(self):
        """test case eval for range 900 1000 174"""
        writer = StringIO()
        collatz_print(writer, 900, 1000, 174)
        self.assertEqual(writer.getvalue(), "900 1000 174\n")

    def test_print4(self):
        """test case eval for range 1 1 1"""
        writer = StringIO()
        collatz_print(writer, 1, 1, 1)
        self.assertEqual(writer.getvalue(), "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """eval for basic given tests cases"""
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # My Test Cases

    def test_solve1(self):
        """test case for empty line"""
        reader = StringIO("\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "")

    def test_solve2(self):
        """test case solve 2"""
        reader = StringIO("1 1 1\n\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 1 1\n")

    def test_solve3(self):
        """test case solve 3"""
        reader = StringIO("10 1 20\n\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "10 1 20\n")
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
