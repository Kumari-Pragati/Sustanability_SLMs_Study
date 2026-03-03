user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_155_code import even_odd_count

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_even_odd_count_positive(self):
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(456), (2, 0))
        self.assertEqual(even_odd_count(789), (0, 3))
        self.assertEqual(even_odd_count(123456), (3, 3))

    def test_even_odd_count_negative(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(-456), (2, 0))
        self.assertEqual(even_odd_count(-789), (0, 3))
        self.assertEqual(even_odd_count(-123456), (3, 3))

    def test_even_odd_count_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_even_odd_count_single_digit(self):
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(1), (0, 1))
        self.assertEqual(even_odd_count(2), (1, 0))
        self.assertEqual(even_odd_count(3), (0, 1))
        self.assertEqual(even_odd_count(4), (1, 0))
        self.assertEqual(even_odd_count(5), (0, 1))
        self.assertEqual(even_odd_count(6), (1, 0))
        self.assertEqual(even_odd_count(7), (0, 1))
        self.assertEqual(even_odd_count(8), (1, 0))
        self.assertEqual(even_odd_count(9), (0, 1))

    def test_even_odd_count_edge_cases(self):
        self.assertEqual(even_odd_count(123456789), (3, 6))
        self.assertEqual(even_odd_count(-123456789), (3, 6))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive and negative numbers, zero, single-digit numbers, and edge cases. It checks that the function correctly counts the number of even and odd digits in each input.