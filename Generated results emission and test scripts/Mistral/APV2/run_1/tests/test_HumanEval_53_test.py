You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_53_code import add
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

 Here is a complete unittest test suite for the `add` function:


import unittest
from HumanEval_53_code import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(10, 20), 30)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, -7), -12)
        self.assertEqual(add(-10, -20), -30)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-5, 7), 2)
        self.assertEqual(add(-10, 20), 10)

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_add_positive_numbers` checks that the function correctly adds positive numbers.
2. `test_add_zero` checks that the function correctly adds zero to both numbers.
3. `test_add_negative_numbers` checks that the function correctly adds negative numbers.
4. `test_add_mixed_numbers` checks that the function correctly adds a mix of positive and negative numbers.

Each test case uses the `assertEqual` method to compare the expected output with the actual output of the `add` function. If the function works correctly, the test suite will pass without any errors. If there are any issues with the function, the test suite will fail, indicating that the function needs to be fixed.