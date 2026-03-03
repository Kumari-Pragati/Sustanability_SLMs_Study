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

 import unittest
from HumanEval_53_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-5, -7), -12)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, -0), 0)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add(10, -5), 5)
        self.assertEqual(add(-1, -1), -2)

    def test_add_large_numbers(self):
        self.assertEqual(add(100000, 200000), 300000)
        self.assertEqual(add(-50000, -20000), -70000)

if __name__ == '__main__':
    unittest.main()