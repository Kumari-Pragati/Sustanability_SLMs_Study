Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_154_code import cycpattern_check
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i + l] == pat[j:j + l]:
                return True
    return False

 import unittest
from HumanEval_154_code import cycpattern_check

class TestCycpatternCheck(unittest.TestCase):

    def test_cycpattern_check_false_not_substring(self):
        self.assertFalse(cycpattern_check("abcd", "abd"))

    def test_cycpattern_check_true_substring(self):
        self.assertTrue(cycpattern_check("hello", "ell"))

    def test_cycpattern_check_false_not_rotation(self):
        self.assertFalse(cycpattern_check("whassup", "psus"))

    def test_cycpattern_check_true_rotation(self):
        self.assertTrue(cycpattern_check("abab", "baa"))

    def test_cycpattern_check_false_rotation_not_substring(self):
        self.assertFalse(cycpattern_check("efef", "eeff"))

    def test_cycpattern_check_true_rotation_substring(self):
        self.assertTrue(cycpattern_check("himenss", "simen"))

    def test_cycpattern_check_false_rotation_not_substring_with_longer_word(self):
        self.assertFalse(cycpattern_check("abcdefgh", "hgfedcba"))

    def test_cycpattern_check_true_rotation_substring_with_longer_word(self):
        self.assertTrue(cycpattern_check("abcdefgh", "cdefgab"))

if __name__ == '__main__':
    unittest.main()