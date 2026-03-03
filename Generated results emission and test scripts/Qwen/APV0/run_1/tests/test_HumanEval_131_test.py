system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to test
from HumanEval_131_code import digits

class TestDigits(unittest.TestCase):

    def test_digits(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)
        self.assertEqual(digits(2468), 0)

if __name__ == '__main__':
    unittest.main()


This script imports the `digits` function from the `HumanEval_131_code` module and defines a class `TestDigits` that inherits from `unittest.TestCase`. It contains a method `test_digits` which tests the `digits` function with various inputs and compares the output against expected results using assertions. The `unittest.main()` call at the end makes the test cases executable when run as a standalone script.