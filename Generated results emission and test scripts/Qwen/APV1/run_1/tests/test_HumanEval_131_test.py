system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_131_code import digits

class TestDigits(unittest.TestCase):

    def test_digits(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)
        self.assertEqual(digits(2468), 0)
        self.assertEqual(digits(13579), 945)
        self.assertEqual(digits(2222), 0)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestDigits` class that inherits from `unittest.TestCase`. It contains a single method `test_digits`, which tests various cases using assertions to ensure the `digits` function behaves as expected. The `assertEqual` methods check if the output of the `digits` function matches the expected results. If any assertion fails, it will raise an error indicating what went wrong.