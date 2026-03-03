Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return bin(round(summation / (m - n + 1)))

 Here is a unittest test script for the `rounded_avg` function:


import unittest
from HumanEval_103_code import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_rounded_avg(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")
        self.assertEqual(rounded_avg(34, 40), "0b100000")
        self.assertEqual(rounded_avg(41, 41), "0b1")
        self.assertEqual(rounded_avg(42, 42), "0b10")
        self.assertEqual(rounded_avg(1, 1), "0b1")
        self.assertEqual(rounded_avg(5, 5), "0b101")
        self.assertEqual(rounded_avg(20, 20), "0b10100")
        self.assertEqual(rounded_avg(33, 33), "0b100001")
        self.assertEqual(rounded_avg(40, 40), "0b1000000")
        self.assertEqual(rounded_avg(41, 41), "0b1000001")
        self.assertEqual(rounded_avg(42, 42), "0b1000010")
        self.assertEqual(rounded_avg(100, 150), "0b111111111")
        self.assertEqual(rounded_avg(151, 200), "0b1111111110")
        self.assertEqual(rounded_avg(201, 250), "0b11111111110")
        self.assertEqual(rounded_avg(251, 300), "0b111111111110")
        self.assertEqual(rounded_avg(301, 350), "0b1111111111110")
        self.assertEqual(rounded_avg(351, 400), "0b11111111111110")
        self.assertEqual(rounded_avg(401, 450), "0b111111111111110")
        self.assertEqual(rounded_avg(451, 500), "0b1111111111111110")
        self.assertEqual(rounded_avg(501, 550), "0b11111111111111110")
        self.assertEqual(rounded_avg(551, 600), "0b111111111111111110")
        self.assertEqual(rounded_avg(601, 650), "0b1111111111111111110")
        self.assertEqual(rounded_avg(651, 700), "0b11111111111111111110")
        self.assertEqual(rounded_avg(701, 750), "0b111111111111111111110")
        self.assertEqual(rounded_avg(751, 800), "0b1111111111111111111110")
        self.assertEqual(rounded_avg(801, 850), "0b11111111111111111111110")