system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_58_code import common

class TestCommonFunction(unittest.TestCase):

    def test_common_elements(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])

    def test_common_elements_with_duplicates(self):
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

    def test_common_elements_with_no_common_elements(self):
        self.assertEqual(common([5, 3, 2, 8], [4, 6, 7]), [])

    def test_common_elements_with_empty_lists(self):
        self.assertEqual(common([], []), [])

    def test_common_elements_with_one_empty_list(self):
        self.assertEqual(common([1, 2, 3], []), [])

    def test_common_elements_with_common_elements_in_order(self):
        self.assertEqual(common([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_common_elements_with_common_elements_in_reverse_order(self):
        self.assertEqual(common([3, 2, 1], [1, 2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()