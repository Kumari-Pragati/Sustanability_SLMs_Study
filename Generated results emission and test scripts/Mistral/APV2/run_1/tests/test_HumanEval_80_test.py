You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
    return True

 Here is the complete unittest test suite for the `is_happy` function:


import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):

    def test_is_happy_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_is_happy_single_char(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("A"))
        self.assertFalse(is_happy("0"))
        self.assertFalse(is_happy("!"))

    def test_is_happy_two_chars(self):
        self.assertFalse(is_happy("aa"))
        self.assertFalse(is_happy("AA"))
        self.assertFalse(is_happy("00"))
        self.assertFalse(is_happy("!!"))

    def test_is_happy_three_chars(self):
        self.assertTrue(is_happy("abc"))
        self.assertTrue(is_happy("ABC"))
        self.assertTrue(is_happy("012"))
        self.assertTrue(is_happy("!@#"))

    def test_is_happy_consecutive_chars(self):
        self.assertFalse(is_happy("aaa"))
        self.assertFalse(is_happy("AAA"))
        self.assertFalse(is_happy("000"))
        self.assertFalse(is_happy("!!!"))

    def test_is_happy_longer_strings(self):
        self.assertTrue(is_happy("abcdabc"))
        self.assertTrue(is_happy("ABCDEFG"))
        self.assertTrue(is_happy("0123456"))
        self.assertTrue(is_happy("!@#$%"))

    def test_is_happy_strings_with_repeated_chars(self):
        self.assertFalse(is_happy("aab"))
        self.assertFalse(is_happy("AAB"))
        self.assertFalse(is_happy("010"))
        self.assertFalse(is_happy("!!!"))

    def test_is_happy_strings_with_adjacent_repeated_chars(self):
        self.assertFalse(is_happy("aaa"))
        self.assertFalse(is_happy("Aaa"))
        self.assertFalse(is_happy("000"))
        self.assertFalse(is_happy("!!!"))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as empty strings, single characters, two characters, longer strings, and strings with repeated characters. It uses the `unittest.TestCase.assertFalse()` and `unittest.TestCase.assertTrue()` methods to verify the expected results.