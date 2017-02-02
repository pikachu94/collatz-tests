#!/usr/bin/env python3
# pylint: disable=R0904

"""
TestCollatz runs Unit tests for Collatz.py
"""

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import (
    collatz_read,
    collatz_eval,
    collatz_print,
    collatz_solve,
    calculate_max_in_interval,
    collatz_range_memo,
    cycle_length,
    collatz_memo
)

# -----------
# TestCollatz
# -----------


class TestCollatzpy(TestCase):
    """
    a class of unit tests for Collatz.py
    """

    # ----
    # read
    # ----

    def test_read_1(self):
        """
        string the input
        i_value the beginning of the range inclusive
        j_value the end of the range inclusive
        """

        string = "1 10\n"
        i_value, j_value = collatz_read(string)
        self.assertEqual(i_value, 1)
        self.assertEqual(j_value, 10)

    def test_read_2(self):
        """
        string the input
        i_value the beginning of the range inclusive
        j_value the end of the range inclusive
        """
        string = "20 30\n"
        i_value, j_value = collatz_read(string)
        self.assertEqual(i_value, 20)
        self.assertEqual(j_value, 30)

    def test_read_3(self):
        """
        string the input
        i_value the beginning of the range inclusive
        j_value the end of the range inclusive
        """
        string = "50 1\n"
        i_value, j_value = collatz_read(string)
        self.assertEqual(i_value, 50)
        self.assertEqual(j_value, 1)

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1(self):
        """
        num the value for which to calculate the cycle length
        cycle_length
        """
        num = 23123
        cycle = cycle_length(num)
        self.assertEqual(cycle, 70)

    def test_cycle_length_2(self):
        """
        num the value for which to calculate the cycle length
        cycle the cycle length
        """
        num = 123
        cycle = cycle_length(num)
        self.assertEqual(cycle, 47)

    def test_cycle_length_3(self):
        """
        num the value for which to calculate the cycle length
        cycle_length
        """
        num = 9023
        cycle = cycle_length(num)
        self.assertEqual(cycle, 154)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_eval(1, 10)
        self.assertEqual(max_cycle, 20)

    def test_eval_2(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_eval(201, 210)
        self.assertEqual(max_cycle, 89)

    def test_eval_3(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_eval(900, 1050)
        self.assertEqual(max_cycle, 174)

    def test_eval_4(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_eval(3034, 217)
        self.assertEqual(max_cycle, 217)

    def test_eval_5(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_eval(5000, 5000)
        self.assertEqual(max_cycle, 29)

    def test_eval_6(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_eval(1, 999999)
        self.assertEqual(max_cycle, 525)

    def test_eval_7(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_eval(1650, 1800)
        self.assertEqual(max_cycle, 180)

    # ------------------
    # collatz_range_memo
    # ------------------

    #Testing in intervals of INTERVAL (150)
    def test_range_memo_1(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_range_memo(1650, 1800)
        self.assertEqual(max_cycle, 180)

    #Testing in intervals smaller than INTERVAL (150)
    def test_range_memo_2(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_range_memo(13, 50)
        self.assertEqual(max_cycle, 112)

    #Testing in intervals greater than INTERVAL (150)
    #With remainder
    def test_range_memo_3(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_range_memo(175, 375)
        self.assertEqual(max_cycle, 144)

    # -------------------------
    # calculate_max_in_interval
    # -------------------------

    def test_max_in_interval_1(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = calculate_max_in_interval(1, 20)
        self.assertEqual(max_cycle, 21)

    def test_max_in_interval_2(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = calculate_max_in_interval(345346, 456450)
        self.assertEqual(max_cycle, 449)

    def test_max_in_interval_3(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = calculate_max_in_interval(344, 4550)
        self.assertEqual(max_cycle, 238)

    # ------------
    # collatz_memo
    # ------------

    def test_collatz_memo_1(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_memo(20)
        self.assertEqual(max_cycle, 8)

    def test_collatz_memo_2(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_memo(22355)
        self.assertEqual(max_cycle, 163)

    def test_collatz_memo_3(self):
        """
        max_cycle the maximum cycle length
        """
        max_cycle = collatz_memo(999999)
        self.assertEqual(max_cycle, 259)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        writer a writer
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        writer a writer
        """
        writer = StringIO()
        collatz_print(writer, 100, 200, 125)
        self.assertEqual(writer.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """
        writer a writer
        """
        writer = StringIO()
        collatz_print(writer, 201, 210, 89)
        self.assertEqual(writer.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        reader a reader
        writer a writer
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        reader a reader
        writer a writer
        """
        reader = StringIO("1 500\n43 1\n642 200000\n134 10105\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 500 144\n43 1 112\n642 200000 383\n134 10105 262\n")

    def test_solve_3(self):
        """
        reader a reader
        writer a writer
        """
        reader = StringIO("234 13204\n41 399\n10000 999\n\n12 12931\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "234 13204 268\n41 399 144\n10000 999 262\n12 12931 268\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

"""
#pragma: no cover
"""
