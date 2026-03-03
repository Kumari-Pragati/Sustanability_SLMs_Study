You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_66_code import digitSum
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    if s == "":
        return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_no_uppercase_letters(self):
        self.assertEqual(digitSum("abc"), 0)

    def test_all_uppercase_letters(self):
        self.assertEqual(digitSum("ABCD"), 294)

    def test_mixed_case_letters(self):
        self.assertEqual(digitSum("AbCdEfGhIjKlMnOpQrStUvWxYz"), 1045)

    def test_single_uppercase_letter(self):
        self.assertEqual(digitSum("A"), 65)

    def test_single_lowercase_letter(self):
        self.assertEqual(digitSum("a"), 0)

    def test_special_characters(self):
        self.assertEqual(digitSum("!@#$%^&*()"), 0)

    def test_numbers_in_string(self):
        self.assertEqual(digitSum("1234567890"), 0)

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestDigitSum` that inherits from `unittest.TestCase`. Each method in this class is a test case that tests the `digitSum` function with different inputs. The `assertEqual` method is used to check if the output of the `digitSum` function matches the expected output.

Please note that the `digitSum` function is expected to be in a file named `HumanEval_66_code.py` in the same directory as this test script. The function should be defined in that file as follows:


def digitSum(s):
    if s == "":
        return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)


To run the test script, you can simply execute it in a Python environment. The `unittest` module will automatically run all the test methods and report the results.