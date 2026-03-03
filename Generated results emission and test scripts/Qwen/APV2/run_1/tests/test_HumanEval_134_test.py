system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_134_code import check_if_last_char_is_a_letter
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False


assistant

import unittest

# Provided function to be tested
from HumanEval_134_code import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_check_if_last_char_is_a_letter(self):
        self.assertEqual(check_if_last_char_is_a_letter("apple pie"), False)
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e"), True)
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e "), False)
        self.assertEqual(check_if_last_char_is_a_letter(""), False)

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases covering various scenarios as described in the docstring of `check_if_last_char_is_a_letter`. It uses the `assertEqual` method to verify the correctness of the function against expected outcomes.