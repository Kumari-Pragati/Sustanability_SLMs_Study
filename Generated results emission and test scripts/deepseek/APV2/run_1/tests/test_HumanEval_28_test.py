You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_28_code import concatenate

class TestConcatenate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_string(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_with_spaces(self):
        self.assertEqual(concatenate(['a', ' ', 'b', ' ', 'c']), 'a b c')

    def test_with_numbers(self):
        self.assertEqual(concatenate(['1', '2', '3']), '123')

    def test_with_special_characters(self):
        self.assertEqual(concatenate(['!', '@', '#']), '!@#')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty list, a list with a single string, multiple strings, strings with spaces, numbers, and special characters.