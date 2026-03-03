system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_161_code import solve
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def solve(s):
    """
    You are given a string s.
    - If s[i] is a letter, reverse its case (lower <-> upper).
    - Otherwise, keep it as it is.
    - If the string contains no letters, reverse the string entirely.

    Examples:
        solve("1234") -> "4321"
        solve("ab")   -> "AB"
        solve("#a@C") -> "#A@c"
    """
    flg = 0
    new_str = []

    for i in s:
        if i.isalpha():
            new_str.append(i.swapcase())
            flg = 1
        else:
            new_str.append(i)

    result = "".join(new_str)
    if flg == 0:
        return result[::-1]
    return resultassistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_161_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_string_with_no_letters(self):
        self.assertEqual(solve("1234"), "4321")

    def test_string_with_letters(self):
        self.assertEqual(solve("ab"), "AB")

    def test_string_with_letters_and_non_letters(self):
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_string_with_all_uppercase_letters(self):
        self.assertEqual(solve("ABC"), "ABC")

    def test_string_with_all_lowercase_letters(self):
        self.assertEqual(solve("abc"), "abc")

    def test_string_with_mixed_case_letters(self):
        self.assertEqual(solve("aBc"), "AbC")

    def test_string_with_no_characters(self):
        self.assertEqual(solve(""), "")

if __name__ == '__main__':
    unittest.main()