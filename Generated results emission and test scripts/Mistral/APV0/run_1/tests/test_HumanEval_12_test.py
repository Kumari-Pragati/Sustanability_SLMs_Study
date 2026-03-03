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
            return s

 Here is a unittest test script for the `longest` function:


import unittest
from HumanEval_12_code import longest

class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')
        self.assertEqual(longest(['A']), 'A')
        self.assertEqual(longest(['Hello']), 'Hello')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')
        self.assertEqual(longest(['aa', 'ab', 'ac', 'ba', 'bb', 'bc']), 'aa')
        self.assertEqual(longest(['aaa', 'aa', 'a', 'ab', 'ba', 'bb', 'bc']), 'aaa')

    def test_strings_of_same_length(self):
        self.assertEqual(longest(['aa', 'bb', 'cc']), 'aa')
        self.assertEqual(longest(['aaa', 'aa', 'a']), 'aaa')

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty list, single strings, multiple strings, and strings of the same length. It uses the `assertEqual` method to compare the expected and actual results and the `assertIsNone` method to check if the function returns `None` for an empty list.