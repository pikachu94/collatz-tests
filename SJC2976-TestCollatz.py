
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

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
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_SJC1(self):
        s = "100 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 1000)

    def test_read_SJC2(self):
        s = "100 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 100)

    def test_read_SJC3(self):
        s = "999 10000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 999)
        self.assertEqual(j, 10000)



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

    def test_eval_SJC1(self):
        v = collatz_eval(850, 875)
        self.assertEqual(v, 179)

    def test_eval_SJC2(self):
        v = collatz_eval(705, 700)
        self.assertEqual(v, 171)

    def test_eval_SJC3(self):
        v = collatz_eval(100, 100)
        self.assertEqual(v, 26)

    def test_eval_SJC4(self):
        v = collatz_eval(0, 20000)
        self.assertEqual(v, 279)

    def test_eval_SJC5(self):
        v = collatz_eval(20000, 19999)
        self.assertEqual(v, 67)

    def test_eval_SJC6(self):
        v = collatz_eval(10, 20000)
        self.assertEqual(v, 279)

    def test_eval_SJC7(self):
        v = collatz_eval(1034, 20000)
        self.assertEqual(v, 279)

    def test_eval_SJC8(self):
        v = collatz_eval(24, 304)
        self.assertEqual(v, 128)

    def test_eval_SJC9(self):
        v = collatz_eval(24, 3024)
        self.assertEqual(v, 217)

    def test_eval_SJC10(self):
        v = collatz_eval(3, 30)
        self.assertEqual(v, 112)

    def test_eval_SJC11(self):
        v = collatz_eval(0, 27)
        self.assertEqual(v, 112)

    def test_eval_SJC12(self):
        v = collatz_eval(21, 30)
        self.assertEqual(v, 112)

    def test_eval_SJC13(self):
        v = collatz_eval(0, 999999)
        self.assertEqual(v, 525)

    # -----
    # print 
    # -----


    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_SJC1(self):
        w = StringIO()
        collatz_print(w, 850, 875, 179)
        self.assertEqual(w.getvalue(), "850 875 179\n")

    def test_print_SJC2(self):
        w = StringIO()
        collatz_print(w, 100, 1000, 179)
        self.assertEqual(w.getvalue(), "100 1000 179\n")

    def test_print_SJC3(self):
        w = StringIO()
        collatz_print(w, 100, 100, 26)
        self.assertEqual(w.getvalue(), "100 100 26\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_SJC1(self):
        r = StringIO("850 875\n100 1000\n100 100\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "850 875 179\n100 1000 179\n100 100 26\n")

    def test_solve_SJC2(self):
        r = StringIO("700 705\n8 9\n212 289\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "700 705 171\n8 9 20\n212 289 128\n")

    def test_solve_SJC3(self):
        r = StringIO("24 304\n699 701\n5 1500\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "24 304 128\n699 701 83\n5 1500 182\n") 

    def test_solve_SJC4(self):
        r = StringIO("\n24 304\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "24 304 128\n") 
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
