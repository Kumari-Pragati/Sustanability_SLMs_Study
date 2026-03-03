user

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
    return x + yassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_53_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_two_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_two_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add(2, -3), -1)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000, 2000), 3000)

if __name__ == '__main__':
    unittest.main()


This script includes five test cases to cover different scenarios:

- `test_add_two_positive_numbers`: Tests the function with two positive numbers.
- `test_add_two_negative_numbers`: Tests the function with two negative numbers.
- `test_add_positive_and_negative_numbers`: Tests the function with one positive and one negative number.
- `test_add_zero`: Tests the function with two zeros.
- `test_add_large_numbers`: Tests the function with two large numbers.

Each test case uses the `assertEqual` method to check if the result of the function is as expected. If the result is not as expected, the test will fail and an error message will be displayed.