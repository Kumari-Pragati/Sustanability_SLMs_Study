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

 Here is a simple unittest test script for the provided `add` function. The test cases cover the basic addition of positive integers, negative integers, and zero.


import unittest
from HumanEval_53_code import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_integers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(100, 200), 300)

    def test_add_negative_integers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, -7), -12)
        self.assertEqual(add(-100, -200), -300)

    def test_add_zero(self):
        self.assertEqual(add(0, 3), 3)
        self.assertEqual(add(-3, 0), -3)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()


Save this script as `test_add.py` and run it using the command `python test_add.py`. The test cases will be executed, and you should see a green bar if all tests pass. If any test fails, the specific test case and the expected and actual results will be displayed.