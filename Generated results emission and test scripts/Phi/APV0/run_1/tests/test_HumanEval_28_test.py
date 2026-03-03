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
    return ''.join(strings)

 import unittest
from HumanEval_28_code import concatenate

class TestConcatenateFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_string(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_mixed_strings(self):
        self.assertEqual(concatenate(['a', '1', 'b', '2', 'c', '3']), 'abc123')

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            concatenate(['a', 1, 'b'])

if __name__ == '__main__':
    unittest.main()