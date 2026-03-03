You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_53_code import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, -7), -12)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-5, 7), 2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

if __name__ == '__main__':
    unittest.main()


This script includes four test cases:

1. `test_add_positive_numbers`: Tests the function with two positive integers.
2. `test_add_negative_numbers`: Tests the function with two negative integers.
3. `test_add_positive_and_negative_numbers`: Tests the function with a positive and a negative integer.
4. `test_add_zero`: Tests the function with zero and a non-zero integer.

Each test case uses the `assertEqual` method to check if the result of the `add` function matches the expected result. If the result is not as expected, the test will fail.

Please note that the `HumanEval_53_code` module and the `add` function should be defined in your Python environment for this script to work.