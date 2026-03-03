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

 import unittest
from HumanEval_58_code import common

class TestCommonFunction(unittest.TestCase):

    def test_common_elements(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])

    def test_common_elements_with_duplicates(self):
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

    def test_empty_lists(self):
        self.assertEqual(common([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(common([1], [1]), [1])

    def test_no_common_elements(self):
        self.assertEqual(common([1, 2, 3], [4, 5, 6]), [])

    def test_common_elements_in_reverse_order(self):
        self.assertEqual(common([653, 2, 5], [5, 1, 653]), [1, 5, 653])

    def test_common_elements_with_none(self):
        self.assertEqual(common([1, 2, 3], None), [])

    def test_common_elements_with_empty_list(self):
        self.assertEqual(common([1, 2, 3], []), [])

    def test_common_elements_with_non_list_input(self):
        with self.assertRaises(TypeError):
            common("not a list", [1, 2, 3])

if __name__ == '__main__':
    unittest.main()