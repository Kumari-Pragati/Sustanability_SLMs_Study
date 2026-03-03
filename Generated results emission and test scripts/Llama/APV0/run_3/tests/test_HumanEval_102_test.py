user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_102_code import choose_num
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(12, 12), -1)
        self.assertEqual(choose_num(14, 16), 14)
        self.assertEqual(choose_num(15, 16), 14)
        self.assertEqual(choose_num(16, 16), -1)
        self.assertEqual(choose_num(17, 18), 16)
        self.assertEqual(choose_num(18, 20), 18)
        self.assertEqual(choose_num(20, 20), -1)
        self.assertEqual(choose_num(1, 2), 2)
        self.assertEqual(choose_num(2, 3), 2)
        self.assertEqual(choose_num(3, 4), 4)
        self.assertEqual(choose_num(4, 5), 4)
        self.assertEqual(choose_num(5, 6), 4)
        self.assertEqual(choose_num(6, 7), 4)
        self.assertEqual(choose_num(7, 8), 6)
        self.assertEqual(choose_num(8, 9), 8)
        self.assertEqual(choose_num(9, 10), 8)
        self.assertEqual(choose_num(10, 11), 8)
        self.assertEqual(choose_num(11, 12), 8)
        self.assertEqual(choose_num(12, 13), -1)
        self.assertEqual(choose_num(13, 14), 12)
        self.assertEqual(choose_num(14, 15), 12)
        self.assertEqual(choose_num(15, 16), 12)
        self.assertEqual(choose_num(16, 17), 12)
        self.assertEqual(choose_num(17, 18), 12)
        self.assertEqual(choose_num(18, 19), 12)
        self.assertEqual(choose_num(19, 20), 12)
        self.assertEqual(choose_num(20, 21), -1)
        self.assertEqual(choose_num(21, 22), 20)
        self.assertEqual(choose_num(22, 23), 20)
        self.assertEqual(choose_num(23, 24), 20)
        self.assertEqual(choose_num(24, 25), 20)
        self.assertEqual(choose_num(25, 26), 20)
        self.assertEqual(choose_num(26, 27), 20)
        self.assertEqual(choose_num(27, 28), 20)
        self.assertEqual(choose_num(28, 29), 20)
        self.assertEqual(choose_num(29, 30), 20)
        self.assertEqual(choose_num(30, 31), -1)
        self.assertEqual(choose_num(31, 32), 28)
        self.assertEqual(choose_num(32, 33), 28)
        self.assertEqual(choose_num(33, 34), 28)
        self.assertEqual(choose_num(34, 35), 28)
        self.assertEqual(choose_num(35, 36), 28)
        self.assertEqual(choose_num(36, 37), 28)
        self.assertEqual(choose_num(37, 38), 28)
        self.assertEqual(choose_num(38, 39), 28)
        self.assertEqual(choose_num(39, 40), 28)
        self.assertEqual(choose_num(40, 41), -1)
        self.assertEqual(choose_num(41, 42), 36)
        self.assertEqual(choose_num(42, 43), 36)
        self.assertEqual(choose_num(43, 44), 36)
        self.assertEqual(choose_num(44, 45), 36)
        self.assertEqual(choose_num(45, 46), 36)
        self.assertEqual(choose_num(46, 47), 36)
        self.assertEqual(choose_num(47, 48), 36)
        self.assertEqual(choose_num(48, 49), 36)
        self.assertEqual(choose_num(49, 50), 36)
        self.assertEqual(choose_num(50, 51), -1)
        self.assertEqual(choose_num(51, 52), 44)
        self.assertEqual(choose_num(52, 53), 44)
        self.assertEqual(choose_num(53, 54), 44)
        self.assertEqual(choose_num(54, 55), 44)
        self.assertEqual(choose_num(55, 56), 44)
        self.assertEqual(choose_num(56, 57), 44)
        self.assertEqual(choose_num(