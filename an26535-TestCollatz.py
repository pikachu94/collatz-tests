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

    def test_read1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read2(self):
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read3(self):
        s = "210 201\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 210)
        self.assertEqual(j, 201)

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

    def test_eval_5(self):
        v = collatz_eval(1, 9999)
        self.assertEqual(v, 262)

    def test_eval_6(self):
        v = collatz_eval(379341, 379868)
        self.assertEqual(v, 361)

    def test_eval_7(self):
        v = collatz_eval(869222, 869573)
        self.assertEqual(v, 388)

    def test_eval_8(self):
        v = collatz_eval(500, 101)
        self.assertEqual(v, 144)

    def test_eval_9(self):
        v = collatz_eval(3000, 340)
        self.assertEqual(v, 217)

    def test_eval_10(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_11(self):
        v = collatz_eval(9999, 9998)
        self.assertEqual(v, 92)

    def test_eval_12(self):
        v = collatz_eval(20, 20)
        self.assertEqual(v, 8)

    def test_eval_13(self):
        v = collatz_eval(418, 50117)
        self.assertEqual(v, 324)

    
    # -----
    # print
    # -----

    def test_print1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2(self):
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    def test_print3(self):
        w = StringIO()
        collatz_print(w, 100000, 1, 1)
        self.assertEqual(w.getvalue(), "100000 1 1\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve3(self):
        r = StringIO("10 10\n5 5\n1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 10 7\n5 5 6\n1 1 1\n")

    def test_solve4(self):
        r = StringIO("\n")
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