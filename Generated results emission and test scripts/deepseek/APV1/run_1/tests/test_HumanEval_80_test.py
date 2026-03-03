You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):

    def test_length_less_than_3(self):
        self.assertEqual(is_happy("a"), False)
        self.assertEqual(is_happy("aa"), False)

    def test_consecutive_letters_are_same(self):
        self.assertEqual(is_happy("abcd"), True)
        self.assertEqual(is_happy("aabb"), False)
        self.assertEqual(is_happy("adb"), True)
        self.assertEqual(is_happy("xyy"), False)

    def test_consecutive_letters_are_not_distinct(self):
        self.assertEqual(is_happy("aaa"), False)
        self.assertEqual(is_happy("bbb"), False)
        self.assertEqual(is_happy("ccc"), False)
        self.assertEqual(is_happy("abc"), True)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_length_less_than_3` checks if the function returns False for strings of length less than 3.
2. `test_consecutive_letters_are_same` checks if the function returns True for strings where every 3 consecutive letters are distinct, and False otherwise.
3. `test_consecutive_letters_are_not_distinct` checks if the function returns False for strings where there are 3 consecutive letters that are the same.

Please note that the function `is_happy` should be defined in a file named `HumanEval_80_code.py` for this test suite to work.