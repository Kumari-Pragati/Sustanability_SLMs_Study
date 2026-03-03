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

 Here is a unittest test script for the provided function:


import unittest
from HumanEval_161_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(solve("1234"), "4321")
        self.assertEqual(solve("ab"), "AB")
        self.assertEqual(solve("#a@C"), "#A@c")
        self.assertEqual(solve("ABC"), "ABC")
        self.assertEqual(solve("abc"), "ABC")
        self.assertEqual(solve(""), "")
        self.assertEqual(solve("1A2B3C"), "3C2B1A")
        self.assertEqual(solve("!@#$%^&*()_+-=[]{}|;':\"<>,.?/"), "/.,>'\":;|}{_+=*(&)()_+-=[email protected]#$%^&*!")

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various inputs. The test cases cover strings with only numbers, only letters (both uppercase and lowercase), a mix of numbers and letters, an empty string, and a string with special characters.