You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
    return result

 Here is the complete unittest test suite for the provided `solve` function:


import unittest
from HumanEval_161_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(solve(""), "")

    def test_only_digits(self):
        self.assertEqual(solve("1234"), "4321")
        self.assertEqual(solve("0987"), "7890")

    def test_only_letters(self):
        self.assertEqual(solve("ab"), "AB")
        self.assertEqual(solve("AB"), "ab")
        self.assertEqual(solve("Hello"), "hELLO")
        self.assertEqual(solve("hello"), "HELLO")

    def test_mixed_case(self):
        self.assertEqual(solve("HeLLo"), "heLLo")
        self.assertEqual(solve("HELLO"), "heLLo")
        self.assertEqual(solve("1h3ll0"), "1h3LL0")

    def test_special_characters(self):
        self.assertEqual(solve("#a@C"), "#A@c")
        self.assertEqual(solve("!@#$%^&*()_+-=[]{}|;':\"<>,.?/~`"), "!@#$%^&*()_+-=[]{}|;':\"<>,.?/~`")

    def test_all_digits_reversed(self):
        self.assertEqual(solve("4321"), "1234")
        self.assertEqual(solve("7890"), "0987")

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty string, only digits, only letters, mixed case, special characters, and all digits reversed.