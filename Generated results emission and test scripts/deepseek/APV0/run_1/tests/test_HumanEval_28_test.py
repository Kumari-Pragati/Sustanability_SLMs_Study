You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


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
        self.assertEqual(concatenate(['a', ' ', 'b', ' ', 'c']), 'a b c ')

    def test_with_numbers(self):
        self.assertEqual(concatenate(['1', '2', '3']), '123')

    def test_with_special_characters(self):
        self.assertEqual(concatenate(['!', '@', '#']), '!@#')

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestConcatenate` that inherits from `unittest.TestCase`. It includes several test methods to test the `concatenate` function with different types of input. Each method uses the `assertEqual` method to check if the output of the function matches the expected result.

Please note that you need to have the `HumanEval_28_code` module with the `concatenate` function defined in it for this script to work.