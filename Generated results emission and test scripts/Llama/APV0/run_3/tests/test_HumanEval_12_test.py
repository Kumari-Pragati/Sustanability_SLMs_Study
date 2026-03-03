user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
            return sassistant

Here is the unittest test script for the `longest` function:

import unittest
from HumanEval_12_code import longest

class TestLongest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements_list(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_multiple_elements_list_with_ties(self):
        self.assertEqual(longest(['a', 'aa', 'aaa']), 'a')
        self.assertEqual(longest(['abc', 'abcd', 'abcde']), 'abc')

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            longest(['a', 1, 'c'])

if __name__ == '__main__':
    unittest.main()

This script tests the `longest` function with various inputs, including:

* An empty list
* A list with a single element
* A list with multiple elements, including ties
* A list with non-string elements (which should raise a `TypeError`)

You can run this script directly to see the test results.