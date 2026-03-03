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
    return [e + 1 for e in l]

 Here is a unittest test script for the `incr_list` function:


import unittest
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(incr_list([]), [])

    def test_single_element(self):
        self.assertEqual(incr_list([0]), [1])
        self.assertEqual(incr_list([5]), [6])

    def test_multiple_elements(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

    def test_negative_numbers(self):
        self.assertEqual(incr_list([-1, -2, -3]), [-0, -1, -2])
        self.assertEqual(incr_list([-5, -3, -5, -2, -3, -3, -9, 0, -123]), [-4, -2, -4, -1, -2, -2, -8, 1, -122])

if __name__ == '__main__':
    unittest.main()


This test script includes four test cases:

1. An empty list
2. A single-element list
3. A list with multiple elements
4. A list containing negative numbers

You can run this script directly to test the `incr_list` function.