You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `digits`. The test cases cover various scenarios including edge cases, positive integers with odd and even number of odd digits, and negative integers.


import unittest
from HumanEval_131_code import digits

class TestDigitsFunction(unittest.TestCase):

    def test_digits_positive_integer_with_odd_digits(self):
        self.assertEqual(digits(235), 15)
        self.assertEqual(digits(12345), 15)
        self.assertEqual(digits(98765), 9)

    def test_digits_positive_integer_with_even_digits(self):
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(100), 0)
        self.assertEqual(digits(2020), 0)

    def test_digits_positive_integer_with_one_odd_digit(self):
        self.assertEqual(digits(12), 1)
        self.assertEqual(digits(102), 2)
        self.assertEqual(digits(120), 0)

    def test_digits_positive_integer_with_multiple_odd_digits(self):
        self.assertEqual(digits(123), 3)
        self.assertEqual(digits(1234), 12)
        self.assertEqual(digits(12345), 15)

    def test_digits_zero(self):
        self.assertEqual(digits(0), 0)

    def test_digits_negative_integer(self):
        self.assertEqual(digits(-1), 1)
        self.assertEqual(digits(-235), 15)
        self.assertEqual(digits(-2020), 0)

if __name__ == '__main__':
    unittest.main()


This test suite uses the built-in `unittest` module to create a test case class `TestDigitsFunction`. Inside this class, there are several test methods that cover various scenarios for the `digits` function. The `unittest.main()` function is called at the end to run the tests.