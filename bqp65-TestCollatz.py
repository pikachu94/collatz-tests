""" Unit tests for Collatz. """
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, find_cycle_length

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):

    """ Class of unit tests for Collatz. """
    # ----
    # read
    # ----

    def test_read_1(self):
        """ Tests collatz_read to make sure input is read in correctly. """
        string = "1 10\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        """ Tests collatz_read to make sure input is read in correctly. """
        string = "200 1000\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 200)
        self.assertEqual(j, 1000)

    def test_read_3(self):
        """ Tests collatz_read to make sure input is read in correctly. """
        string = "500 853\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 500)
        self.assertEqual(j, 853)

    def test_read_4(self):
        """ Tests collatz_read to make sure input is read in correctly. """
        string = "1 999999\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 1)
        self.assertEqual(j, 999999)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Tests collatz_eval to make sure max cycle length is caluclated
        correctly.
        """
        max_cycle = collatz_eval(1, 10)
        self.assertEqual(max_cycle, 20)

    def test_eval_2(self):
        """
        Tests collatz_eval to make sure max cycle length is caluclated
        correctly.
        """
        max_cycle = collatz_eval(100, 200)
        self.assertEqual(max_cycle, 125)

    def test_eval_3(self):
        """
        Tests collatz_eval to make sure max cycle length is caluclated
        correctly.
        """
        max_cycle = collatz_eval(201, 210)
        self.assertEqual(max_cycle, 89)

    def test_eval_4(self):
        """
        Tests collatz_eval to make sure max cycle length is caluclated
        correctly.
        """
        max_cycle = collatz_eval(900, 1000)
        self.assertEqual(max_cycle, 174)

    # -----------------
    # find_cycle_length
    # -----------------

    def test_cycle_len_1(self):
        """ Tests that the cycle length of a number is correct. """
        length = find_cycle_length(1)
        self.assertEqual(length, 1)

    def test_cycle_len_2(self):
        """ Tests that the cycle length of a number is correct. """
        length = find_cycle_length(16)
        self.assertEqual(length, 5)

    def test_cycle_len_3(self):
        """ Tests that the cycle length of a number is correct. """
        length = find_cycle_length(10)
        self.assertEqual(length, 7)

    # -----
    # print
    # -----

    def test_print_1(self):
        """ Tests collatz_print to make sure results are printed correctly. """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """ Tests collatz_print to make sure results are printed correctly. """
        writer = StringIO()
        collatz_print(writer, 100, 200, 125)
        self.assertEqual(writer.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """ Tests collatz_print to make sure results are printed correctly. """
        writer = StringIO()
        collatz_print(writer, 201, 210, 89)
        self.assertEqual(writer.getvalue(), "201 210 89\n")

    def test_print_4(self):
        """ Tests collatz_print to make sure results are printed correctly. """
        writer = StringIO()
        collatz_print(writer, 92755, 539533, 470)
        self.assertEqual(writer.getvalue(), "92755 539533 470\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """ Tests that all pieces of Collatz are working together correctly."""
        input_string = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        output = StringIO()
        collatz_solve(input_string, output)
        self.assertEqual(
            output.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """ Tests that all pieces of Collatz are working together correctly."""
        input_string = StringIO("1 1\n2 1\n999 1000\n")
        output = StringIO()
        collatz_solve(input_string, output)
        self.assertEqual(
            output.getvalue(), "1 1 1\n2 1 2\n999 1000 112\n")

    def test_solve_3(self):
        """ Tests that all pieces of Collatz are working together correctly."""
        input_string = StringIO("43100 57848\n822555 88326\n486168 318413\n")
        output = StringIO()
        collatz_solve(input_string, output)
        self.assertEqual(
            output.getvalue(), "43100 57848 340\n822555 88326 509\n486168 318413 449\n")

    def test_solve_4(self):
        """ Tests that all pieces of Collatz are working together correctly."""
        input_string = StringIO("50 50\n150 2000\n1 2000\n")
        output = StringIO()
        collatz_solve(input_string, output)
        self.assertEqual(
            output.getvalue(), "50 50 25\n150 2000 182\n1 2000 182\n")

    def test_solve_5(self):
        """ Tests that all pieces of Collatz are working together correctly."""
        input_string = StringIO("1 1\n2 2\n8 8\n")
        output = StringIO()
        collatz_solve(input_string, output)
        self.assertEqual(
            output.getvalue(), "1 1 1\n2 2 2\n8 8 4\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()
