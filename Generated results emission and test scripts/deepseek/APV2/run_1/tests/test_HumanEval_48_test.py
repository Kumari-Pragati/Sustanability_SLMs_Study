You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_48_code import is_palindrome
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('abba'))

    def test_odd_length_palindrome(self):
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('abc'))
        self.assertFalse(is_palindrome('abcd'))
        self.assertFalse(is_palindrome('zbcd'))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following scenarios:

- An empty string is a palindrome.
- A string with a single character is a palindrome.
- A string that is a palindrome with an even length.
- A string that is a palindrome with an odd length.
- A string that is not a palindrome.

Each test method calls the `is_palindrome` function with a specific input and checks if the output is as expected.