system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
        return productassistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_131_code import digits

class TestDigits(unittest.TestCase):

    def test_digits(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)
        self.assertEqual(digits(12345), 15)
        self.assertEqual(digits(24680), 0)
        self.assertEqual(digits(111), 111)
        self.assertEqual(digits(222), 0)
        self.assertEqual(digits(123456), 30)
        self.assertEqual(digits(1234567), 315)
        self.assertEqual(digits(12345678), 3150)

if __name__ == '__main__':
    unittest.main()