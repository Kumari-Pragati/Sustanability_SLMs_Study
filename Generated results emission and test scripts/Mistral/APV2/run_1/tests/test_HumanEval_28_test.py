You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `concatenate` function:


import unittest
from HumanEval_28_code import concatenate

class TestConcatenate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_string(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            concatenate([1, 2, 3])

    def test_empty_string(self):
        self.assertEqual(concatenate(['', 'b', 'c']), 'bxc')

    def test_whitespace(self):
        self.assertEqual(concatenate(['a ', 'b', ' c']), 'ab c')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty list, a single string, multiple strings, mixed types, an empty string, and whitespace. The `assertRaises` method is used to test for exceptions when passing non-string values to the function.