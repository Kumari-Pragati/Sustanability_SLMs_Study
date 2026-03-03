system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function
from HumanEval_12_code import longest

class TestLongest(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_equal_length_strings(self):
        self.assertEqual(longest(['aaa', 'bbb', 'ccc']), 'aaa')
        self.assertEqual(longest(['ddd', 'eee', 'fff']), 'ddd')

if __name__ == '__main__':
    unittest.main()


This unittest test suite covers various scenarios including an empty list, single element, multiple elements with different lengths, and equal-length strings. It uses assertions to check that the `longest` function behaves as expected under these conditions.