system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Importing the function from the given module
from HumanEval_53_code import add

class TestAddition(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()


This test suite includes a `TestAddition` class that inherits from `unittest.TestCase`. It contains a single method `test_addition`, which uses assertions (`self.assertEqual`) to check if the `add` function returns the correct results when called with different inputs. The `unittest.main()` call at the end of the script runs the tests when this file is executed directly.