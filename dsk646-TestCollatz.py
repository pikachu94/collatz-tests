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


class TestCollatz(TestCase):
    """
    # read
    """

    def test_read(self):
        """
        # read test 1
        """
        string = "1 10\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    # ----
    # eval
    # ----

    def test_eval_1_10(self):
        """
        # eval test 1
        """
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_100_200(self):
        """
        # eval test 2
        """
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_201_210(self):
        """
        # eval test 3
        """
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_900_1000(self):
        """
        # eval test 4
        """
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_1_10_swap(self):
        """
        # eval test 1
        """
        val = collatz_eval(10, 1)
        self.assertEqual(val, 20)

    def test_eval_100_200_swap(self):
        """
        # eval test 2
        """
        val = collatz_eval(200, 100)
        self.assertEqual(val, 125)

    def test_eval_201_210_swap(self):
        """
        # eval test 3
        """
        val = collatz_eval(210, 201)
        self.assertEqual(val, 89)

    def test_eval_900_100_swap(self):
        """
        # eval test 4
        """
        val = collatz_eval(1000, 900)
        self.assertEqual(val, 174)

    def test_eval_15842(self):
        """
        # eval test 15842
        """
        self.assertEqual(collatz_eval(15842, 15842), 54)

    def test_eval_23824(self):
        """
        # eval test 23824
        """
        self.assertEqual(collatz_eval(23824, 23824), 52)

    def test_eval_23949(self):
        """
        # eval test 23949
        """
        self.assertEqual(collatz_eval(23949, 23949), 52)

    def test_eval_34580(self):
        """
        # eval test 34580
        """
        self.assertEqual(collatz_eval(34580, 34580), 37)

    def test_eval_46074(self):
        """
        # eval test 46074
        """
        self.assertEqual(collatz_eval(46074, 46074), 115)

    def test_eval_77915(self):
        """
        # eval test 77915
        """
        self.assertEqual(collatz_eval(77915, 77915), 170)

    def test_eval_83752(self):
        """
        # eval test 83752
        """
        self.assertEqual(collatz_eval(83752, 83752), 90)

    def test_eval_97999(self):
        """
        # eval test 97999
        """
        self.assertEqual(collatz_eval(97999, 97999), 129)

    def test_eval_110406(self):
        """
        # eval test 110406
        """
        self.assertEqual(collatz_eval(110406, 110406), 155)

    def test_eval_116511(self):
        """
        # eval test 116511
        """
        self.assertEqual(collatz_eval(116511, 116511), 106)

    def test_eval_134534(self):
        """
        # eval test 134534
        """
        self.assertEqual(collatz_eval(134534, 134534), 114)

    def test_eval_136276(self):
        """
        # eval test 136276
        """
        self.assertEqual(collatz_eval(136276, 136276), 132)

    def test_eval_143178(self):
        """
        # eval test 143178
        """
        self.assertEqual(collatz_eval(143178, 143178), 220)

    def test_eval_151995(self):
        """
        # eval test 151995
        """
        self.assertEqual(collatz_eval(151995, 151995), 57)

    def test_eval_152146(self):
        """
        # eval test 152146
        """
        self.assertEqual(collatz_eval(152146, 152146), 171)

    def test_eval_155761(self):
        """
        # eval test 155761
        """
        self.assertEqual(collatz_eval(155761, 155761), 52)

    def test_eval_187023(self):
        """
        # eval test 187023
        """
        self.assertEqual(collatz_eval(187023, 187023), 135)

    def test_eval_196653(self):
        """
        # eval test 196653
        """
        self.assertEqual(collatz_eval(196653, 196653), 55)

    def test_eval_227232(self):
        """
        # eval test 227232
        """
        self.assertEqual(collatz_eval(227232, 227232), 94)

    def test_eval_232479(self):
        """
        # eval test 232479
        """
        self.assertEqual(collatz_eval(232479, 232479), 200)

    def test_eval_232845(self):
        """
        # eval test 232845
        """
        self.assertEqual(collatz_eval(232845, 232845), 76)

    def test_eval_247490(self):
        """
        # eval test 247490
        """
        self.assertEqual(collatz_eval(247490, 247490), 63)

    def test_eval_250228(self):
        """
        # eval test 250228
        """
        self.assertEqual(collatz_eval(250228, 250228), 45)

    def test_eval_252843(self):
        """
        # eval test 252843
        """
        self.assertEqual(collatz_eval(252843, 252843), 81)

    def test_eval_256401(self):
        """
        # eval test 256401
        """
        self.assertEqual(collatz_eval(256401, 256401), 102)

    def test_eval_258286(self):
        """
        # eval test 258286
        """
        self.assertEqual(collatz_eval(258286, 258286), 164)

    def test_eval_264391(self):
        """
        # eval test 264391
        """
        self.assertEqual(collatz_eval(264391, 264391), 71)

    def test_eval_266258(self):
        """
        # eval test 266258
        """
        self.assertEqual(collatz_eval(266258, 266258), 94)

    def test_eval_268920(self):
        """
        # eval test 268920
        """
        self.assertEqual(collatz_eval(268920, 268920), 71)

    def test_eval_271692(self):
        """
        # eval test 271692
        """
        self.assertEqual(collatz_eval(271692, 271692), 102)

    def test_eval_279938(self):
        """
        # eval test 279938
        """
        self.assertEqual(collatz_eval(279938, 279938), 53)

    def test_eval_288252(self):
        """
        # eval test 288252
        """
        self.assertEqual(collatz_eval(288252, 288252), 252)

    def test_eval_292051(self):
        """
        # eval test 292051
        """
        self.assertEqual(collatz_eval(292051, 292051), 221)

    def test_eval_319046(self):
        """
        # eval test 319046
        """
        self.assertEqual(collatz_eval(319046, 319046), 79)

    def test_eval_322126(self):
        """
        # eval test 322126
        """
        self.assertEqual(collatz_eval(322126, 322126), 123)

    def test_eval_334309(self):
        """
        # eval test 334309
        """
        self.assertEqual(collatz_eval(334309, 334309), 185)

    def test_eval_340022(self):
        """
        # eval test 340022
        """
        self.assertEqual(collatz_eval(340022, 340022), 198)

    def test_eval_342972(self):
        """
        # eval test 342972
        """
        self.assertEqual(collatz_eval(342972, 342972), 136)

    def test_eval_357169(self):
        """
        # eval test 357169
        """
        self.assertEqual(collatz_eval(357169, 357169), 118)

    def test_eval_363856(self):
        """
        # eval test 363856
        """
        self.assertEqual(collatz_eval(363856, 363856), 43)

    def test_eval_366708(self):
        """
        # eval test 366708
        """
        self.assertEqual(collatz_eval(366708, 366708), 35)

    def test_eval_378844(self):
        """
        # eval test 378844
        """
        self.assertEqual(collatz_eval(378844, 378844), 180)

    def test_eval_384309(self):
        """
        # eval test 384309
        """
        self.assertEqual(collatz_eval(384309, 384309), 87)

    def test_eval_391767(self):
        """
        # eval test 391767
        """
        self.assertEqual(collatz_eval(391767, 391767), 131)

    def test_eval_392378(self):
        """
        # eval test 392378
        """
        self.assertEqual(collatz_eval(392378, 392378), 118)

    def test_eval_405341(self):
        """
        # eval test 405341
        """
        self.assertEqual(collatz_eval(405341, 405341), 193)

    def test_eval_407595(self):
        """
        # eval test 407595
        """
        self.assertEqual(collatz_eval(407595, 407595), 113)

    def test_eval_424364(self):
        """
        # eval test 424364
        """
        self.assertEqual(collatz_eval(424364, 424364), 126)

    def test_eval_446193(self):
        """
        # eval test 446193
        """
        self.assertEqual(collatz_eval(446193, 446193), 64)

    def test_eval_464995(self):
        """
        # eval test 464995
        """
        self.assertEqual(collatz_eval(464995, 464995), 170)

    def test_eval_471392(self):
        """
        # eval test 471392
        """
        self.assertEqual(collatz_eval(471392, 471392), 77)

    def test_eval_472354(self):
        """
        # eval test 472354
        """
        self.assertEqual(collatz_eval(472354, 472354), 108)

    def test_eval_494623(self):
        """
        # eval test 494623
        """
        self.assertEqual(collatz_eval(494623, 494623), 170)

    def test_eval_512816(self):
        """
        # eval test 512816
        """
        self.assertEqual(collatz_eval(512816, 512816), 103)

    def test_eval_529739(self):
        """
        # eval test 529739
        """
        self.assertEqual(collatz_eval(529739, 529739), 103)

    def test_eval_531053(self):
        """
        # eval test 531053
        """
        self.assertEqual(collatz_eval(531053, 531053), 134)

    def test_eval_550076(self):
        """
        # eval test 550076
        """
        self.assertEqual(collatz_eval(550076, 550076), 178)

    def test_eval_596120(self):
        """
        # eval test 596120
        """
        self.assertEqual(collatz_eval(596120, 596120), 160)

    def test_eval_605313(self):
        """
        # eval test 605313
        """
        self.assertEqual(collatz_eval(605313, 605313), 67)

    def test_eval_606176(self):
        """
        # eval test 606176
        """
        self.assertEqual(collatz_eval(606176, 606176), 235)

    def test_eval_619018(self):
        """
        # eval test 619018
        """
        self.assertEqual(collatz_eval(619018, 619018), 191)

    def test_eval_625895(self):
        """
        # eval test 625895
        """
        self.assertEqual(collatz_eval(625895, 625895), 85)

    def test_eval_625958(self):
        """
        # eval test 625958
        """
        self.assertEqual(collatz_eval(625958, 625958), 54)

    def test_eval_649554(self):
        """
        # eval test 649554
        """
        self.assertEqual(collatz_eval(649554, 649554), 178)

    def test_eval_655510(self):
        """
        # eval test 655510
        """
        self.assertEqual(collatz_eval(655510, 655510), 186)

    def test_eval_656841(self):
        """
        # eval test 656841
        """
        self.assertEqual(collatz_eval(656841, 656841), 67)

    def test_eval_662792(self):
        """
        # eval test 662792
        """
        self.assertEqual(collatz_eval(662792, 662792), 155)

    def test_eval_664136(self):
        """
        # eval test 664136
        """
        self.assertEqual(collatz_eval(664136, 664136), 142)

    def test_eval_669056(self):
        """
        # eval test 669056
        """
        self.assertEqual(collatz_eval(669056, 669056), 62)

    def test_eval_687550(self):
        """
        # eval test 687550
        """
        self.assertEqual(collatz_eval(687550, 687550), 199)

    def test_eval_699649(self):
        """
        # eval test 699649
        """
        self.assertEqual(collatz_eval(699649, 699649), 106)

    def test_eval_714770(self):
        """
        # eval test 714770
        """
        self.assertEqual(collatz_eval(714770, 714770), 150)

    def test_eval_721217(self):
        """
        # eval test 721217
        """
        self.assertEqual(collatz_eval(721217, 721217), 212)

    def test_eval_738979(self):
        """
        # eval test 738979
        """
        self.assertEqual(collatz_eval(738979, 738979), 212)

    def test_eval_765243(self):
        """
        # eval test 765243
        """
        self.assertEqual(collatz_eval(765243, 765243), 150)

    def test_eval_783999(self):
        """
        # eval test 783999
        """
        self.assertEqual(collatz_eval(783999, 783999), 225)

    def test_eval_799763(self):
        """
        # eval test 799763
        """
        self.assertEqual(collatz_eval(799763, 799763), 194)

    def test_eval_806644(self):
        """
        # eval test 806644
        """
        self.assertEqual(collatz_eval(806644, 806644), 194)

    def test_eval_809076(self):
        """
        # eval test 809076
        """
        self.assertEqual(collatz_eval(809076, 809076), 132)

    def test_eval_813818(self):
        """
        # eval test 813818
        """
        self.assertEqual(collatz_eval(813818, 813818), 62)

    def test_eval_820049(self):
        """
        # eval test 820049
        """
        self.assertEqual(collatz_eval(820049, 820049), 238)

    def test_eval_839869(self):
        """
        # eval test 839869
        """
        self.assertEqual(collatz_eval(839869, 839869), 176)

    def test_eval_849126(self):
        """
        # eval test 849126
        """
        self.assertEqual(collatz_eval(849126, 849126), 264)

    def test_eval_861412(self):
        """
        # eval test 861412
        """
        self.assertEqual(collatz_eval(861412, 861412), 57)

    def test_eval_874945(self):
        """
        # eval test 874945
        """
        self.assertEqual(collatz_eval(874945, 874945), 114)

    def test_eval_896347(self):
        """
        # eval test 896347
        """
        self.assertEqual(collatz_eval(896347, 896347), 140)

    def test_eval_897227(self):
        """
        # eval test 897227
        """
        self.assertEqual(collatz_eval(897227, 897227), 96)

    def test_eval_902401(self):
        """
        # eval test 902401
        """
        self.assertEqual(collatz_eval(902401, 902401), 233)

    def test_eval_916483(self):
        """
        # eval test 916483
        """
        self.assertEqual(collatz_eval(916483, 916483), 109)

    def test_eval_925566(self):
        """
        # eval test 925566
        """
        self.assertEqual(collatz_eval(925566, 925566), 140)

    def test_eval_936775(self):
        """
        # eval test 936775
        """
        self.assertEqual(collatz_eval(936775, 936775), 339)

    def test_eval_937464(self):
        """
        # eval test 937464
        """
        self.assertEqual(collatz_eval(937464, 937464), 215)

    def test_eval_939702(self):
        """
        # eval test 939702
        """
        self.assertEqual(collatz_eval(939702, 939702), 171)

    def test_eval_945110(self):
        """
        # eval test 945110
        """
        self.assertEqual(collatz_eval(945110, 945110), 202)

    def test_eval_946083(self):
        """
        # eval test 946083
        """
        self.assertEqual(collatz_eval(946083, 946083), 78)

    def test_eval_978086(self):
        """
        # eval test 978086
        """
        self.assertEqual(collatz_eval(978086, 978086), 197)

    def test_eval_978963(self):
        """
        # eval test 978963
        """
        self.assertEqual(collatz_eval(978963, 978963), 153)

    def test_eval_979417(self):
        """
        # eval test 979417
        """
        self.assertEqual(collatz_eval(979417, 979417), 122)

    def test_eval_981766(self):
        """
        # eval test 981766
        """
        self.assertEqual(collatz_eval(981766, 981766), 184)

    def test_eval_985633(self):
        """
        # eval test 985633
        """
        self.assertEqual(collatz_eval(985633, 985633), 153)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        # print test 1
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        # print test 2
        """
        writer = StringIO()
        collatz_print(writer, 100, 200, 125)
        self.assertEqual(writer.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """
        # print test 3
        """
        writer = StringIO()
        collatz_print(writer, 201, 210, 89)
        self.assertEqual(writer.getvalue(), "201 210 89\n")

    def test_print_4(self):
        """
        # print test 4
        """
        writer = StringIO()
        collatz_print(writer, 900, 1000, 174)
        self.assertEqual(writer.getvalue(), "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        # solve test 1
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        # solve test 2
        """
        reader = StringIO("1 100\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 100 119\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

