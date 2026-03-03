You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_134_code import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_last_char_is_a_letter(self):
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e "))
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))
        self.assertFalse(check_if_last_char_is_a_letter(""))
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e1"))
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e!"))
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e_"))

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestCheckIfLastCharIsALetter` that inherits from `unittest.TestCase`. It includes a method `test_last_char_is_a_letter` that tests the `check_if_last_char_is_a_letter` function with various inputs. The `unittest.main()` at the end runs the tests when the script is run directly.

Please note that the function `check_if_last_char_is_a_letter` is expected to be in a file named `HumanEval_134_code.py` in the same directory as the test script.