user

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
    return [x for x in values if isinstance(x, int)]assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])
        self.assertEqual(filter_integers([1, 2, 'a', 3.14, 4, 5.6]), [1, 2, 3, 4])
        self.assertEqual(filter_integers(['a', 'b', 'c']), [])
        self.assertEqual(filter_integers([1, 2, 3.14, 4, 5.6]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_list_with_single_integer(self):
        self.assertEqual(filter_integers([5]), [5])

    def test_list_with_single_non_integer(self):
        self.assertEqual(filter_integers(['a']), [])

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to cover different scenarios:

- `test_filter_integers`: This test case checks the function with different lists of mixed types.
- `test_empty_list`: This test case checks the function with an empty list.
- `test_list_with_single_integer`: This test case checks the function with a list containing a single integer.
- `test_list_with_single_non_integer`: This test case checks the function with a list containing a single non-integer.