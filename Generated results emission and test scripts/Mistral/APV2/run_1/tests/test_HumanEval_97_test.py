You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the provided `multiply` function:


import unittest
from HumanEval_97_code import multiply

class TestMultiply(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)

    def test_multiply_zero(self):
        self.assertEqual(multiply(2020, 1851), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(14, -15), 20)

    def test_edge_cases(self):
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. Testing the multiplication of positive numbers.
2. Testing the multiplication of zero.
3. Testing the multiplication of negative numbers.
4. Testing edge cases (multiplication of 0, 1, and -1 with both positive and negative numbers).

The test suite uses the `unittest.TestCase` class to define test methods and the `assertEqual` method to check the expected and actual results.