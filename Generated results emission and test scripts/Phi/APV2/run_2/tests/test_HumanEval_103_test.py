You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 import unittest
from HumanEval_103_code import rounded_avg

class TestRoundedAverage(unittest.TestCase):

    def test_rounded_avg_with_positive_integers(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")

    def test_rounded_avg_with_n_greater_than_m(self):
        self.assertEqual(rounded_avg(7, 5), -1)

    def test_rounded_avg_with_zero_range(self):
        self.assertEqual(rounded_avg(1, 1), "0b1")

    def test_rounded_avg_with_single_number(self):
        self.assertEqual(rounded_avg(5, 5), "0b101")

    def test_rounded_avg_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            rounded_avg(-1, 5)

    def test_rounded_avg_with_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            rounded_avg(1.5, 5)

if __name__ == '__main__':
    unittest.main()