You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_97_code import multiply
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.

    Examples:
    multiply(148, 412) ➞ 16
    multiply(19, 28) ➞ 72
    multiply(2020, 1851) ➞ 0
    multiply(14, -15) ➞ 20
    """

    return abs(a % 10) * abs(b % 10)


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_97_code import multiply

class TestMultiply(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiply(14, -15), 20)

    def test_zero(self):
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(10, 0), 0)

    def test_single_digit_numbers(self):
        self.assertEqual(multiply(5, 7), 35)
        self.assertEqual(multiply(9, 9), 81)

if __name__ == '__main__':
    unittest.main()


This script includes four test cases:

1. `test_positive_numbers`: Tests the function with positive integers.
2. `test_negative_numbers`: Tests the function with negative integers.
3. `test_zero`: Tests the function with zero.
4. `test_single_digit_numbers`: Tests the function with single-digit numbers.

Please note that the function `multiply` is assumed to be in a file named `HumanEval_97_code.py` in the same directory as the test script. If the function is in a different location, you will need to import it accordingly.