You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_80_code import is_happy
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

    Examples:
        is_happy("a") => False
        is_happy("aa") => False
        is_happy("abcd") => True
        is_happy("aabb") => False
        is_happy("adb") => True
        is_happy("xyy") => False
    """

    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            return False
    return True


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):

    def test_single_char(self):
        self.assertFalse(is_happy("a"))

    def test_double_chars(self):
        self.assertFalse(is_happy("aa"))

    def test_happy_string(self):
        self.assertTrue(is_happy("abcd"))

    def test_unhappy_string(self):
        self.assertFalse(is_happy("aabb"))

    def test_happy_string_with_repetition(self):
        self.assertTrue(is_happy("adb"))

    def test_unhappy_string_with_repetition(self):
        self.assertFalse(is_happy("xyy"))

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to cover different scenarios. It checks if the function correctly identifies happy and unhappy strings, and it also checks if the function correctly handles strings with repeated characters.

Please note that the `HumanEval_80_code` module and the `is_happy` function should be defined in a separate Python file for this script to work.