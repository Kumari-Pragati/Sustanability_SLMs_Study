You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_161_code import solve

class TestSolve(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(solve("1234"), "4321")

    def test_letters(self):
        self.assertEqual(solve("ab"), "AB")

    def test_special_chars(self):
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_no_letters(self):
        self.assertEqual(solve("123#$%"), "%%$#321")

    def test_mixed_chars(self):
        self.assertEqual(solve("aB12#$%"), "Ab12%%$#")

    def test_empty_string(self):
        self.assertEqual(solve(""), "")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- `test_numbers`: Tests the function with a string of only numbers.
- `test_letters`: Tests the function with a string of only letters.
- `test_special_chars`: Tests the function with a string of special characters.
- `test_no_letters`: Tests the function with a string that doesn't contain any letters.
- `test_mixed_chars`: Tests the function with a string that contains a mix of letters and other characters.
- `test_empty_string`: Tests the function with an empty string.

Each test checks if the output of the function matches the expected result.