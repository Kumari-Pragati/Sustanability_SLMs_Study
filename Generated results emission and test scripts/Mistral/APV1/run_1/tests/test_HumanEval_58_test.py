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
    return sorted(list(ret))

 Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_58_code import common

class TestCommonFunction(unittest.TestCase):

    def test_common_unique_elements(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])
        self.assertEqual(common([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]), [])
        self.assertEqual(common([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(common([], []), [])
        self.assertEqual(common([1], []), [])
        self.assertEqual(common([], [1]), [])

    def test_common_empty_lists(self):
        self.assertEqual(common([], []), [])

    def test_common_one_element_lists(self):
        self.assertEqual(common([1], [1]), [1])
        self.assertEqual(common([1], [2]), [])
        self.assertEqual(common([2], [1]), [])

    def test_common_duplicates(self):
        self.assertEqual(common([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to check the function's behavior with different input combinations, including unique elements, duplicates, empty lists, and one-element lists. It also checks the sorted and unique output of the function.