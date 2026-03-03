system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return ''.join(strings)assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_28_code import concatenate

class TestConcatenate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_element_list(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_element_list(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_list_with_spaces(self):
        self.assertEqual(concatenate(['a', 'b', 'c ', 'd']), 'abc d')

    def test_list_with_newlines(self):
        self.assertEqual(concatenate(['a', 'b', 'c\n', 'd']), 'abc\nd')

    def test_list_with_tabs(self):
        self.assertEqual(concatenate(['a', 'b', 'c\t', 'd']), 'abc\t d')

if __name__ == '__main__':
    unittest.main()