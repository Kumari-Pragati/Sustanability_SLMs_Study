Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_30_code import get_positive
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [e for e in l if e > 0]

 Here is a unittest test script for the `get_positive` function:


import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):

    def test_get_positive(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])
        self.assertEqual(get_positive([]), [])
        self.assertEqual(get_positive([0]), [0])
        self.assertEqual(get_positive([-100, -200, -300]), [])
        self.assertEqual(get_positive([100, 200, 300]), [100, 200, 300])
        self.assertEqual(get_positive([-1, 0, 1]), [1])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various input lists, including empty lists, lists with only positive numbers, lists with only negative numbers, and lists with both positive and negative numbers. The test cases are defined within the `TestGetPositive` class, and the test suite is run using `unittest.main()`.