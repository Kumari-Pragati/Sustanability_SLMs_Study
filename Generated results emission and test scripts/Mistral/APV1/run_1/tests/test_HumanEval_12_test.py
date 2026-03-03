You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_12_code import longest

class TestLongestString(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')
        self.assertEqual(longest(['A']), 'A')
        self.assertEqual(longest(['Z']), 'Z')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')
        self.assertEqual(longest(['aa', 'ab', 'ac']), 'ac')
        self.assertEqual(longest(['AA', 'AB', 'AC']), 'AC')

    def test_strings_of_same_length(self):
        self.assertEqual(longest(['aaa', 'aa', 'a']), 'aaa')
        self.assertEqual(longest(['AAA', 'AA', 'A']), 'AAA')
        self.assertEqual(longest(['z', 'zz', 'zzz']), 'zzz')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty list, single strings, multiple strings, and strings of the same length. It uses the `assertIsNone`, `assertEqual` methods provided by the `unittest.TestCase` class to verify the correctness of the function.