user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_27_code import flip_case

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):

    def test_flip_case_lowercase(self):
        self.assertEqual(flip_case('hello'), 'HELLO')

    def test_flip_case_uppercase(self):
        self.assertEqual(flip_case('HELLO'), 'hello')

    def test_flip_case_mixedcase(self):
        self.assertEqual(flip_case('HeLlO'), 'hElLo')

    def test_flip_case_empty_string(self):
        self.assertEqual(flip_case(''), '')

    def test_flip_case_single_character(self):
        self.assertEqual(flip_case('a'), 'A')

    def test_flip_case_multiple_spaces(self):
        self.assertEqual(flip_case('   '),'  ')

    def test_flip_case_non_alphabetic_characters(self):
        self.assertEqual(flip_case('Hello!'), 'hELLO!')

    def test_flip_case_punctuation(self):
        self.assertEqual(flip_case('Hello, World!'), 'hELLO, wORLD!')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following scenarios:

- Flipping lowercase characters to uppercase and uppercase to lowercase
- Handling empty strings
- Handling single characters
- Handling multiple spaces
- Handling non-alphabetic characters
- Handling punctuation

Each test method starts with the prefix `test_` and uses the `assertEqual` method to check if the output of the `flip_case` function matches the expected output.