You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `filter_integers` function:


import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(filter_integers([]), [])

    def test_all_integers(self):
        self.assertListEqual(filter_integers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_mixed_types(self):
        self.assertListEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

    def test_all_non_integers(self):
        self.assertListEqual(filter_integers(['a', 3.14, {}, []]), [])

    def test_float(self):
        self.assertListEqual(filter_integers([1, 2, 3.14]), [1, 2])

    def test_string(self):
        self.assertListEqual(filter_integers(['a', '1', '2']), [])

    def test_list(self):
        self.assertListEqual(filter_integers([[], [1, 2, 3]]), [])

    def test_dict(self):
        self.assertListEqual(filter_integers({'key': 1, 'another_key': 2}), [1, 2])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as an empty list, all integers, mixed types, all non-integers, floats, strings, lists, and dictionaries. It uses the `assertListEqual` method to compare the expected and actual outputs.