Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_22_code import filter_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any Python values only for integers.
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

 Here is a unittest test script for the `filter_integers` function:


import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):
    def test_filter_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])
        self.assertEqual(filter_integers([1, 2, 3, 4.0, 5]), [1, 2, 3, 5])
        self.assertEqual(filter_integers([1, 2, '3', 4]), [1, 2, 3])
        self.assertEqual(filter_integers([]), [])
        self.assertEqual(filter_integers([None]), [])
        self.assertEqual(filter_integers([True]), [])
        self.assertEqual(filter_integers([False]), [])
        self.assertEqual(filter_integers([1.1, 2.0, 3.0]), [])

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the expected behavior of the `filter_integers` function, as well as some edge cases to ensure the function works correctly with different types of inputs. The test cases are defined within the `TestFilterIntegers` class, and the test suite is run using `unittest.main()`.