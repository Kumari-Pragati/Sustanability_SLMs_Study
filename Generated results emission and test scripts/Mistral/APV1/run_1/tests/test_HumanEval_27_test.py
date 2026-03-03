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
    return string.swapcase()

 Here is a comprehensive unittest test suite for the given Python function `flip_case()`. I've added several test cases to cover various scenarios:


import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')

    def test_all_uppercase(self):
        self.assertEqual(flip_case('HELLO'), 'hELLO')

    def test_all_lowercase(self):
        self.assertEqual(flip_case('hello'), 'HELLO')

    def test_mixed_case(self):
        self.assertEqual(flip_case('HeLLo wOrLd'), 'hELLo wOrld')

    def test_special_characters(self):
        self.assertEqual(flip_case('Hello123!@#'), 'hELLO123!@#')

    def test_whitespace(self):
        self.assertEqual(flip_case(' Hello   World '), ' h  ELLO   WORLD ')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty string, all uppercase, all lowercase, mixed case, special characters, and whitespace. It will help you ensure that the `flip_case()` function works as expected in various scenarios.