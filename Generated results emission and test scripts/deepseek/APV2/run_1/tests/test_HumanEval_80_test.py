You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):

    def test_short_strings(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))

    def test_same_consecutive_letters(self):
        self.assertFalse(is_happy("abcd"))
        self.assertFalse(is_happy("aabb"))
        self.assertFalse(is_happy("xyy"))

    def test_distinct_consecutive_letters(self):
        self.assertTrue(is_happy("adb"))

    def test_edge_cases(self):
        self.assertFalse(is_happy(""))
        self.assertFalse(is_happy("a" * 300))

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_short_strings`: Tests strings of length less than 3.
2. `test_same_consecutive_letters`: Tests strings where there are consecutive letters that are the same.
3. `test_distinct_consecutive_letters`: Tests strings where every 3 consecutive letters are distinct.
4. `test_edge_cases`: Tests edge cases, including an empty string and a string of length 300 with all the same letters.

Please note that the `HumanEval_80_code` module and the `is_happy` function should be defined in a separate Python file for this test suite to work.