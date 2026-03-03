You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_12_code import longest
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s

 Here is the complete unittest test suite for the `longest` function:


import unittest
from HumanEval_12_code import longest

class TestLongestString(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')
        self.assertEqual(longest(['A']), 'A')
        self.assertEqual(longest(['1']), '1')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')
        self.assertEqual(longest(['aa', 'ab', 'ac']), 'aa')
        self.assertEqual(longest(['A', 'B', 'C']), 'A')
        self.assertEqual(longest(['1', '11', '111']), '111')

    def test_strings_of_same_length(self):
        self.assertEqual(longest(['aaa', 'aa', 'a']), 'aaa')
        self.assertEqual(longest(['AAA', 'AA', 'A']), 'AAA')
        self.assertEqual(longest(['111', '11', '1']), '111')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty list, single strings, multiple strings, strings of the same length, and a mix of uppercase and lowercase strings. It uses the `unittest.TestCase.assertEqual` method to compare the expected and actual results and the `unittest.TestCase.assertIsNone` method to check for None values.