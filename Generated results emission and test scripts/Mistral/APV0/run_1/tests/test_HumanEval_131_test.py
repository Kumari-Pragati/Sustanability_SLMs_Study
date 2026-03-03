Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `digits` function:


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
        self.assertEqual(digits(12345), 225)

    def test_digits_6789(self):
        self.assertEqual(digits(6789), 45)

    def test_digits_0(self):
        self.assertEqual(digits(0), 0)

    def test_digits_negative_number(self):
        self.assertEqual(digits(-123), 0)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases for the `digits` function, including cases where the input is a single digit, multiple digits, and a negative number. The test cases cover the edge cases where all digits are even and the base case where the input is 0.