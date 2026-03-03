You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `flip_case` function:


import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')

    def test_single_character(self):
        self.assertEqual(flip_case('a'), 'A')
        self.assertEqual(flip_case('A'), 'a')

    def test_mixed_case(self):
        self.assertEqual(flip_case('Hello World'), 'hELLO wORLD')
        self.assertEqual(flip_case('THE QUICK BROWN FOX'), 'tHE qUICK bROWN fOX')

    def test_special_characters(self):
        self.assertEqual(flip_case('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '!@#$%^&*()_+-=[]{}|;:'\'<>,./')

    def test_whitespace(self):
        self.assertEqual(flip_case(' Hello   World '), ' hELLO   wORLD ')

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as an empty string, single characters, mixed cases, special characters, and whitespace. It uses the `assertEqual` method to compare the expected and actual results.