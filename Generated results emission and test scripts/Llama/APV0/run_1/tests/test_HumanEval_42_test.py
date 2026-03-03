user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_42_code import incr_list
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [e + 1 for e in l]assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):

    def test_incr_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

    def test_incr_list_empty(self):
        self.assertEqual(incr_list([]), [])

    def test_incr_list_single_element(self):
        self.assertEqual(incr_list([10]), [11])

    def test_incr_list_negative_numbers(self):
        self.assertEqual(incr_list([-1, -2, -3]), [-0, -1, -2])

    def test_incr_list_float_numbers(self):
        self.assertEqual(incr_list([1.5, 2.5, 3.5]), [2.5, 3.5, 4.5])

    def test_incr_list_mixed_types(self):
        with self.assertRaises(TypeError):
            incr_list([1, 2, '3'])

if __name__ == '__main__':
    unittest.main()


This script includes tests for the following cases:
- The function works correctly with a list of integers.
- The function works correctly with an empty list.
- The function works correctly with a list containing a single element.
- The function works correctly with a list containing negative numbers.
- The function works correctly with a list containing float numbers.
- The function raises a TypeError when given a list containing non-integer values.