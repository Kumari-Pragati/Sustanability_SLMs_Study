user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_36_code import fizz_buzz
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ansassistant

Here is the unittest test script for the `fizz_buzz` function:

import unittest
from HumanEval_36_code import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(50), 0)
        self.assertEqual(fizz_buzz(78), 2)
        self.assertEqual(fizz_buzz(79), 3)
        self.assertEqual(fizz_buzz(100), 6)
        self.assertEqual(fizz_buzz(101), 7)
        self.assertEqual(fizz_buzz(110), 8)
        self.assertEqual(fizz_buzz(111), 9)
        self.assertEqual(fizz_buzz(130), 10)
        self.assertEqual(fizz_buzz(131), 11)
        self.assertEqual(fizz_buzz(132), 12)
        self.assertEqual(fizz_buzz(133), 13)
        self.assertEqual(fizz_buzz(134), 14)
        self.assertEqual(fizz_buzz(135), 15)
        self.assertEqual(fizz_buzz(136), 16)
        self.assertEqual(fizz_buzz(137), 17)
        self.assertEqual(fizz_buzz(138), 18)
        self.assertEqual(fizz_buzz(139), 19)
        self.assertEqual(fizz_buzz(140), 20)
        self.assertEqual(fizz_buzz(141), 21)
        self.assertEqual(fizz_buzz(142), 22)
        self.assertEqual(fizz_buzz(143), 23)
        self.assertEqual(fizz_buzz(144), 24)
        self.assertEqual(fizz_buzz(145), 25)
        self.assertEqual(fizz_buzz(146), 26)
        self.assertEqual(fizz_buzz(147), 27)
        self.assertEqual(fizz_buzz(148), 28)
        self.assertEqual(fizz_buzz(149), 29)
        self.assertEqual(fizz_buzz(150), 30)
        self.assertEqual(fizz_buzz(151), 31)
        self.assertEqual(fizz_buzz(152), 32)
        self.assertEqual(fizz_buzz(153), 33)
        self.assertEqual(fizz_buzz(154), 34)
        self.assertEqual(fizz_buzz(155), 35)
        self.assertEqual(fizz_buzz(156), 36)
        self.assertEqual(fizz_buzz(157), 37)
        self.assertEqual(fizz_buzz(158), 38)
        self.assertEqual(fizz_buzz(159), 39)
        self.assertEqual(fizz_buzz(160), 40)
        self.assertEqual(fizz_buzz(161), 41)
        self.assertEqual(fizz_buzz(162), 42)
        self.assertEqual(fizz_buzz(163), 43)
        self.assertEqual(fizz_buzz(164), 44)
        self.assertEqual(fizz_buzz(165), 45)
        self.assertEqual(fizz_buzz(166), 46)
        self.assertEqual(fizz_buzz(167), 47)
        self.assertEqual(fizz_buzz(168), 48)
        self.assertEqual(fizz_buzz(169), 49)
        self.assertEqual(fizz_buzz(170), 50)
        self.assertEqual(fizz_buzz(171), 51)
        self.assertEqual(fizz_buzz(172), 52)
        self.assertEqual(fizz_buzz(173), 53)
        self.assertEqual(fizz_buzz(174), 54)
        self.assertEqual(fizz_buzz(175), 55)
        self.assertEqual(fizz_buzz(176), 56)
        self.assertEqual(fizz_buzz(177), 57)
        self.assertEqual(fizz_buzz(178), 58)
        self.assertEqual(fizz_buzz(179), 59)
        self.assertEqual(fizz_buzz(180), 60)
        self.assertEqual(fizz_buzz(181), 61)
        self.assertEqual(fizz_buzz(182), 62)
        self.assertEqual(fizz_buzz(183), 63)
        self.assertEqual(fizz_buzz(184), 64)
        self.assertEqual(fizz_buzz(185), 65)
        self.assertEqual(fizz_buzz(186), 66)
        self.assertEqual(fizz_buzz(187), 67)
        self.assertEqual(fizz_buzz(188), 68)
        self.assertEqual(fizz_buzz(189), 69)
        self.assertEqual(fizz_buzz(190), 70)
        self.assertEqual(fizz_buzz(191), 71)
        self.assertEqual(fizz_buzz(192), 72)
        self.assertEqual(fizz_buzz(193), 73)
        self.assertEqual(fizz_buzz(194), 74)
        self.assertEqual(fizz_buzz(195), 75)
        self.assertEqual(fizz_buzz(196), 76)
        self.assertEqual(fizz_buzz(197), 77)