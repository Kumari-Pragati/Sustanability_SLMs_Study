Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_161_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_no_letters(self):
        self.assertEqual(solve("1234"), "4321")

    def test_letters_case_reversed(self):
        self.assertEqual(solve("ab"), "AB")
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_mixed_string(self):
        self.assertEqual(solve("aBc123"), "AbC123")
        self.assertEqual(solve("HelloWorld"), "hELLOwORLD")
        self.assertEqual(solve("Python3.8"), "pYTHON3.8")

    def test_empty_string(self):
        self.assertEqual(solve(""), "")

    def test_string_with_spaces(self):
        self.assertEqual(solve("Hello World"), "DLROWolleh")

    def test_string_with_special_characters(self):
        self.assertEqual(solve("#a@C"), "#A@c")
        self.assertEqual(solve("!@#$%^&*()_+"), "!@#$%^&*()_+")

if __name__ == '__main__':
    unittest.main()