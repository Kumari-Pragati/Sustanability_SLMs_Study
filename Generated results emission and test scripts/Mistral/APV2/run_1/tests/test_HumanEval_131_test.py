You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `digits` function:


import unittest
from HumanEval_131_code import digits

class TestDigitsFunction(unittest.TestCase):

    def test_digits_1(self):
        self.assertEqual(digits(1), 1)

    def test_digits_4(self):
        self.assertEqual(digits(4), 0)

    def test_digits_235(self):
        self.assertEqual(digits(235), 15)

    def test_digits_10(self):
        self.assertEqual(digits(10), 0)

    def test_digits_12345(self):
        self.assertEqual(digits(12345), 15)

    def test_digits_67890(self):
        self.assertEqual(digits(67890), 0)

    def test_digits_123456789(self):
        self.assertEqual(digits(123456789), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases for different inputs, including single-digit numbers, numbers with only odd digits, numbers with only even digits, and numbers with a mix of odd and even digits. The test cases use the `assertEqual` method to compare the expected output with the actual output of the `digits` function.