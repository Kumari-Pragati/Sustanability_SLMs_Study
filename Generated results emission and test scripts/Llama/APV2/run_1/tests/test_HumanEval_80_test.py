system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return Trueassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):

    def test_is_happy(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))
        self.assertTrue(is_happy("abcd"))
        self.assertFalse(is_happy("aabb"))
        self.assertTrue(is_happy("adb"))
        self.assertFalse(is_happy("xyy"))

    def test_is_happy_short_string(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("ab"))

    def test_is_happy_long_string(self):
        self.assertTrue(is_happy("abcdefgh"))
        self.assertTrue(is_happy("abcdefghijklmnopqrstuvwxyz"))

    def test_is_happy_string_with_repeated_chars(self):
        self.assertFalse(is_happy("aaaa"))
        self.assertFalse(is_happy("aabbcc"))

    def test_is_happy_string_with_distinct_chars(self):
        self.assertTrue(is_happy("abcd"))
        self.assertTrue(is_happy("wxyz"))

if __name__ == '__main__':
    unittest.main()