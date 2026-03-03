user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given Python function:

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
        self.assertEqual(concatenate(['a','', 'b', 'c']), 'a b c')

    def test_list_with_newlines(self):
        self.assertEqual(concatenate(['a', '\n', 'b', 'c']), 'a\nb c')

    def test_list_with_tabs(self):
        self.assertEqual(concatenate(['a', '\t', 'b', 'c']), 'a\tb c')

if __name__ == '__main__':
    unittest.main()


This script includes tests for the following scenarios:

- An empty list
- A list with a single element
- A list with multiple elements
- A list with spaces
- A list with newlines
- A list with tabs

Each test case uses the `assertEqual` method to check if the output of the `concatenate` function matches the expected output.