user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_58_code import common

class TestCommonFunction(unittest.TestCase):

    def test_common_elements(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])

    def test_common_elements_with_duplicates(self):
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

    def test_common_elements_with_empty_lists(self):
        self.assertEqual(common([], [5, 7, 1, 5, 9, 653, 121]), [])
        self.assertEqual(common([5, 7, 1, 5, 9, 653, 121], []), [])

    def test_common_elements_with_single_element_lists(self):
        self.assertEqual(common([1], [1]), [1])
        self.assertEqual(common([1], [2]), [])

    def test_common_elements_with_all_elements_in_common(self):
        self.assertEqual(common([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_common_elements_with_no_common_elements(self):
        self.assertEqual(common([1, 2, 3], [4, 5, 6]), [])

    def test_common_elements_with_negative_numbers(self):
        self.assertEqual(common([-1, -2, -3], [-1, -2, -3]), [-1, -2, -3])

    def test_common_elements_with_floating_point_numbers(self):
        self.assertEqual(common([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]), [1.0, 2.0, 3.0])

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure the function is working correctly in different scenarios. It tests for common elements, empty lists, single-element lists, lists with all elements in common, lists with no common elements, lists with negative numbers, and lists with floating point numbers.