system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return sum(ord(char) if char.isupper() else 0 for char in s)assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_single_uppercase(self):
        self.assertEqual(digitSum("A"), 65)

    def test_multiple_uppercase(self):
        self.assertEqual(digitSum("ABC"), 78)

    def test_mixed_case(self):
        self.assertEqual(digitSum("aAbC"), 78)

    def test_all_lowercase(self):
        self.assertEqual(digitSum("abc"), 0)

    def test_all_non_alphabetic(self):
        self.assertEqual(digitSum("123"), 0)

    def test_mixed_case_and_non_alphabetic(self):
        self.assertEqual(digitSum("a1A"), 65)

if __name__ == '__main__':
    unittest.main()