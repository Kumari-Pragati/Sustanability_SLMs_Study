user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_58_code import common
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_58_code import common

class TestCommonFunction(unittest.TestCase):

    def test_common_elements(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])
        self.assertEqual(common([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(common([1, 1, 1], [1, 1, 1]), [1])
        self.assertEqual(common([], [1, 2, 3]), [])
        self.assertEqual(common([1, 2, 3], []), [])

    def test_empty_lists(self):
        self.assertEqual(common([], []), [])
        self.assertEqual(common([1, 2, 3], []), [])
        self.assertEqual(common([], [1, 2, 3]), [])

    def test_single_element_lists(self):
        self.assertEqual(common([1], [1]), [1])
        self.assertEqual(common([1], [2]), [])
        self.assertEqual(common([1, 2], [1]), [1])
        self.assertEqual(common([1, 2], [2]), [2])

if __name__ == '__main__':
    unittest.main()


This script includes four test cases:

- `test_common_elements`: This test case checks the function with different input lists and expected output lists.
- `test_empty_lists`: This test case checks the function with empty lists as input.
- `test_single_element_lists`: This test case checks the function with single-element lists as input.

The `assertEqual` method is used to compare the output of the function with the expected output. If the output does not match the expected output, the test case fails and an error message is displayed.