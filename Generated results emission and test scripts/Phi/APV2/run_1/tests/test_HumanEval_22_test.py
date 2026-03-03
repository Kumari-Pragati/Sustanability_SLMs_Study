You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 
import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers_with_mixed_types(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

    def test_filter_integers_with_only_integers(self):
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

    def test_filter_integers_with_no_integers(self):
        self.assertEqual(filter_integers(['a', 'b', 'c']), [])

    def test_filter_integers_with_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_filter_integers_with_single_integer(self):
        self.assertEqual(filter_integers([42]), [42])

    def test_filter_integers_with_negative_integers(self):
        self.assertEqual(filter_integers([-1, -2, -3]), [-1, -2, -3])

    def test_filter_integers_with_positive_integers(self):
        self.assertEqual(filter_integers([1, 2, 3]), [1, 2, 3])

    def test_filter_integers_with_mixed_sign_integers(self):
        self.assertEqual(filter_integers([-1, 2, -3, 4]), [-1, -3, 2, 4])

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios to ensure that the `filter_integers` function works as expected. It tests the function with different types of input, including lists with a mix of integers, non-integers, empty lists, single integers, negative integers, and positive integers. Each test case uses the `assertEqual` method to compare the output of the `filter_integers` function with the expected result. Running this test suite will execute all the test cases and report any failures or errors.