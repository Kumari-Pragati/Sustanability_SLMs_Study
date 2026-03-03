You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_131_code import digits
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit % 2 == 1:
            product = product * int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_131_code import digits

class TestDigits(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(3), 3)
        self.assertEqual(digits(5), 5)
        self.assertEqual(digits(7), 7)
        self.assertEqual(digits(9), 9)

    def test_multiple_digits(self):
        self.assertEqual(digits(235), 15)
        self.assertEqual(digits(123456), 15)
        self.assertEqual(digits(2468), 0)

    def test_large_number(self):
        self.assertEqual(digits(123456789), 9*7*5*3*1)

    def test_even_number(self):
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(2), 0)
        self.assertEqual(digits(6), 0)
        self.assertEqual(digits(8), 0)

    def test_negative_number(self):
        self.assertEqual(digits(-1), 1)
        self.assertEqual(digits(-3), 3)
        self.assertEqual(digits(-5), 5)
        self.assertEqual(digits(-7), 7)
        self.assertEqual(digits(-9), 9)

    def test_zero(self):
        self.assertEqual(digits(0), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for single digit numbers, multiple digit numbers, large numbers, even numbers, negative numbers, and zero. It checks that the function returns the correct product of odd digits for each of these cases.