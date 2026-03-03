user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_103_code import rounded_avg

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """

    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation += i
    return bin(round(summation / (m - n + 1)))assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_103_code import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_rounded_avg(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")
        self.assertEqual(rounded_avg(5, 5), "0b10")
        self.assertEqual(rounded_avg(10, 10), "0b1010")
        self.assertEqual(rounded_avg(1, 1), "0b1")
        self.assertEqual(rounded_avg(2, 2), "0b10")
        self.assertEqual(rounded_avg(3, 3), "0b11")
        self.assertEqual(rounded_avg(4, 4), "0b100")
        self.assertEqual(rounded_avg(5, 5), "0b1010")
        self.assertEqual(rounded_avg(6, 6), "0b1100")
        self.assertEqual(rounded_avg(7, 7), "0b1110")
        self.assertEqual(rounded_avg(8, 8), "0b10000")
        self.assertEqual(rounded_avg(9, 9), "0b10011")
        self.assertEqual(rounded_avg(10, 10), "0b10100")
        self.assertEqual(rounded_avg(11, 11), "0b10110")
        self.assertEqual(rounded_avg(12, 12), "0b11000")
        self.assertEqual(rounded_avg(13, 13), "0b11011")
        self.assertEqual(rounded_avg(14, 14), "0b11100")
        self.assertEqual(rounded_avg(15, 15), "0b11110")
        self.assertEqual(rounded_avg(16, 16), "0b100000")
        self.assertEqual(rounded_avg(17, 17), "0b100011")
        self.assertEqual(rounded_avg(18, 18), "0b100100")
        self.assertEqual(rounded_avg(19, 19), "0b100111")
        self.assertEqual(rounded_avg(20, 20), "0b101000")
        self.assertEqual(rounded_avg(21, 21), "0b101010")
        self.assertEqual(rounded_avg(22, 22), "0b101100")
        self.assertEqual(rounded_avg(23, 23), "0b101110")
        self.assertEqual(rounded_avg(24, 24), "0b110000")
        self.assertEqual(rounded_avg(25, 25), "0b110010")
        self.assertEqual(rounded_avg(26, 26), "0b110100")
        self.assertEqual(rounded_avg(27, 27), "0b110110")
        self.assertEqual(rounded_avg(28, 28), "0b111000")
        self.assertEqual(rounded_avg(29, 29), "0b111010")
        self.assertEqual(rounded_avg(30, 30), "0b111100")
        self.assertEqual(rounded_avg(31, 31), "0b111110")
        self.assertEqual(rounded_avg(32, 32), "0b1000000")
        self.assertEqual(rounded_avg(33, 33), "0b1000011")
        self.assertEqual(rounded_avg(34, 34), "0b1000100")
        self.assertEqual(rounded_avg(35, 35), "0b1000111")
        self.assertEqual(rounded_avg(36, 36), "0b1001000")
        self.assertEqual(rounded_avg(37, 37), "0b1001011")
        self.assertEqual(rounded_avg(38, 38), "0b1001100")
        self.assertEqual(rounded_avg(39, 39), "0b1001111")
        self.assertEqual(rounded_avg(40, 40), "0b1010000")
        self.assertEqual(rounded_avg(41, 41), "0b1010011")
        self.assertEqual(rounded_avg(42, 42), "0b1010100")
        self.assertEqual(rounded_avg(43, 43), "0b1010111")
        self.assertEqual(rounded_avg(44, 44), "0b1011000")
        self.assertEqual(rounded_avg(45, 45), "0b1011011")
        self.assertEqual(rounded_avg(46, 46), "0b1011100")
        self.assertEqual(rounded_avg(47, 47), "0b1011111")
        self.assertEqual(rounded_avg(48, 48), "0b1100000