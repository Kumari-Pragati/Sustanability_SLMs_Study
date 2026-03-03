system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_28_code import concatenate
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def concatenate(strings: List[str]) -> str:
    """Concatenate list of strings into a single string.
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


assistant

import unittest

# Provided function
from HumanEval_28_code import concatenate

class TestConcatenate(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_element(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_elements(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:
- The first case checks if an empty list returns an empty string.
- The second case verifies that a single-element list correctly contains just that element.
- The third case tests concatenating multiple elements into one string.