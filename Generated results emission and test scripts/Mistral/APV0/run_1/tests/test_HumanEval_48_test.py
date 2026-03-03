Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `is_palindrome` function:


import unittest
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        for char in ['a', 'A', '0', '9', '!', '.']:
            self.assertTrue(is_palindrome(char))

    def test_palindrome(self):
        for palindrome in ['aba', 'level', 'racecar', 'deified', 'rotor', 'madam', 'radar']:
            self.assertTrue(is_palindrome(palindrome))

    def test_non_palindrome(self):
        for non_palindrome in ['zbcd', 'hello', 'world', 'python', 'javascript']:
            self.assertFalse(is_palindrome(non_palindrome))

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty string, single characters, palindromes, and non-palindromes. The test cases are organized in a class called `TestIsPalindrome`, and each test case is a method that starts with `test_`. The test cases use the `assertTrue` and `assertFalse` methods to verify the expected behavior of the `is_palindrome` function.