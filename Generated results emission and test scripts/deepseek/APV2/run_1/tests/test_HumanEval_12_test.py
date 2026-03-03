You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the provided Python function:


import unittest
from HumanEval_12_code import longest

class TestLongest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_longest_string(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_same_length_strings(self):
        self.assertEqual(longest(['aaa', 'bbb', 'ccc']), 'aaa')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following scenarios:

- An empty list as input.
- A list with a single string.
- A list with multiple strings of different lengths.
- A list with multiple strings of the same length, where the function should return the first one.
- A list with strings of the same length, where the function should return the first one.

Please note that the function `longest` is assumed to be in a file named `HumanEval_12_code.py` in the same directory as the test file. If the function is in a different location, you will need to adjust the import statement accordingly.