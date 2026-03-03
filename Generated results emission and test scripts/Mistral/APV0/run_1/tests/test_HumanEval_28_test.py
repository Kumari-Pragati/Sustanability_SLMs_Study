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

 Here is a unittest test script for the `concatenate` function:


import unittest
from HumanEval_28_code import concatenate

class TestConcatenate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_element(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_elements(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            concatenate(['a', 1, 'b'])

    def test_empty_string(self):
        self.assertEqual(concatenate(['', 'a', 'b']), 'ab')

    def test_whitespace(self):
        self.assertEqual(concatenate(['a', ' ', 'b']), 'a b')

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty list, a single element, multiple elements, mixed types, an empty string, and whitespace. The `assertRaises` method is used to test for a TypeError when passing a list with mixed types.