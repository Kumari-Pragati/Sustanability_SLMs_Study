user

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
    return resultassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_161_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_solve_1(self):
        self.assertEqual(solve("1234"), "4321")

    def test_solve_2(self):
        self.assertEqual(solve("ab"), "AB")

    def test_solve_3(self):
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_solve_4(self):
        self.assertEqual(solve("Hello World"), "hELLO wORLD")

    def test_solve_5(self):
        self.assertEqual(solve("1234567890"), "0987654321")

    def test_solve_6(self):
        self.assertEqual(solve("abcdefghijklmnopqrstuvwxyz"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_solve_7(self):
        self.assertEqual(solve("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "abcdefghijklmnopqrstuvwxyz")

    def test_solve_8(self):
        self.assertEqual(solve("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), "0987654321zyxwvutsrqponmlkjihgfedcba")

if __name__ == '__main__':
    unittest.main()


This script includes 8 test cases to cover different scenarios:

- Test cases 1-3 cover the base cases mentioned in the problem statement.
- Test cases 4-5 cover cases where the input string contains only digits.
- Test cases 6-7 cover cases where the input string contains only uppercase or lowercase letters.
- Test case 8 covers a case where the input string contains a mix of digits, uppercase letters, and lowercase letters.