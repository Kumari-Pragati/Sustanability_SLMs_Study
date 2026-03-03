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

 import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_single_character(self):
        self.assertFalse(is_happy("a"))

    def test_two_identical_characters(self):
        self.assertFalse(is_happy("aa"))

    def test_happy_string(self):
        self.assertTrue(is_happy("abcd"))

    def test_not_happy_string_with_repeated_letters(self):
        self.assertFalse(is_happy("aabb"))

    def test_happy_string_with_distinct_letters(self):
        self.assertTrue(is_happy("adb"))

    def test_not_happy_string_with_two_identical_consecutive_letters(self):
        self.assertFalse(is_happy("xyy"))

if __name__ == '__main__':
    unittest.main()