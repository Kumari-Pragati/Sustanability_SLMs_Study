You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_10_code import make_palindrome
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_10_code import make_palindrome, is_palindrome

class TestMakePalindrome(unittest.TestCase):
    def test_make_palindrome(self):
        self.assertEqual(make_palindrome(''), '')
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')
        self.assertEqual(make_palindrome('race'), 'racecar')
        self.assertEqual(make_palindrome('abc'), 'abcba')
        self.assertEqual(make_palindrome('12321'), '12321')

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('aa'))
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('abcba'))
        self.assertFalse(is_palindrome('abc'))
        self.assertFalse(is_palindrome('abcd'))

if __name__ == '__main__':
    unittest.main()


This script includes two test cases: one for the `make_palindrome` function and one for the `is_palindrome` function. Each test case includes a series of assertions to check that the function's output matches the expected result.

Please note that the `make_palindrome` function's behavior is not defined for the input 'race', as it does not have a palindrome at the beginning. The function will not work correctly for such inputs.

Also, the `is_palindrome` function is a simple function that checks if a string is a palindrome. It does not have any complex logic or edge cases to test.

Please replace `HumanEval_10_code` with the actual module where your functions are defined.