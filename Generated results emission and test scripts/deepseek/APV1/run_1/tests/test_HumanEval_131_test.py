You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


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
        self.assertEqual(digits(325), 15)
        self.assertEqual(digits(246), 0)
        self.assertEqual(digits(346), 0)
        self.assertEqual(digits(123456), 15)

    def test_even_numbers(self):
        self.assertEqual(digits(2), 0)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(6), 0)
        self.assertEqual(digits(8), 0)
        self.assertEqual(digits(2468), 0)

    def test_large_numbers(self):
        self.assertEqual(digits(123456789), 9)
        self.assertEqual(digits(987654321), 9)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for single-digit numbers, multiple-digit numbers, even numbers, and large numbers. It checks that the function returns the correct product of odd digits for each of these cases.