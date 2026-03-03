You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return string.swapcase()


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):
    def test_all_lowercase(self):
        self.assertEqual(flip_case('hello'), 'HELLO')

    def test_all_uppercase(self):
        self.assertEqual(flip_case('HELLO'), 'hello')

    def test_mixed_case(self):
        self.assertEqual(flip_case('HeLLo'), 'hEllO')

    def test_numbers_and_special_chars(self):
        self.assertEqual(flip_case('h3ll0!'), 'H3LL0!')

    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

1. All lowercase characters.
2. All uppercase characters.
3. Mixed case characters.
4. Numbers and special characters.
5. An empty string.

Each test checks if the `flip_case` function correctly flips the case of the input string.