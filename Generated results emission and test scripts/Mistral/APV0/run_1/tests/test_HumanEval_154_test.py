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

 Here is a unittest test script for the `cycpattern_check` function:


import unittest
from HumanEval_154_code import cycpattern_check

class TestCycpatternCheck(unittest.TestCase):
    def test_cycpattern_check(self):
        self.assertFalse(cycpattern_check("abcd", "abd"))
        self.assertTrue(cycpattern_check("hello", "ell"))
        self.assertFalse(cycpattern_check("whassup", "psus"))
        self.assertTrue(cycpattern_check("abab", "baa"))
        self.assertFalse(cycpattern_check("efef", "eeff"))
        self.assertTrue(cycpattern_check("himenss", "simen"))
        self.assertFalse(cycpattern_check("abc", "bc"))
        self.assertTrue(cycpattern_check("aaa", "a"))
        self.assertFalse(cycpattern_check("", ""))
        self.assertFalse(cycpattern_check("abc", "def"))

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the edge cases and some additional test cases to ensure the function works correctly. You can run this script directly to test the `cycpattern_check` function.