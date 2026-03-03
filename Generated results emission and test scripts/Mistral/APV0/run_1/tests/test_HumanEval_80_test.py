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

 Here is a unittest test script for the `is_happy` function:


import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):
    def test_is_happy(self):
        self.assertTrue(is_happy("abcd"))
        self.assertTrue(is_happy("adb"))
        self.assertFalse(is_happy("aabb"))
        self.assertFalse(is_happy("xyy"))
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))

    def test_edge_cases(self):
        self.assertFalse(is_happy(""))
        self.assertFalse(is_happy("abc"))
        self.assertTrue(is_happy("abcde"))
        self.assertFalse(is_happy("aaa"))
        self.assertTrue(is_happy("abcdefg"))

if __name__ == '__main__':
    unittest.main()


This test script includes two test functions: `test_is_happy` and `test_edge_cases`. The `test_is_happy` function tests the function with the examples provided in the function documentation, while the `test_edge_cases` function tests the function with edge cases such as empty strings, strings of length 3, and strings with more than 3 distinct consecutive letters.