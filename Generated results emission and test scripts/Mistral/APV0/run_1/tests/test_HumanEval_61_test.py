Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_61_code import correct_bracketing
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def correct_bracketing(brackets: str):
    """brackets is a string of "(" and ")".
    Return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

 Here is a unittest test script for the `correct_bracketing` function:


import unittest
from HumanEval_61_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_single_opening_bracket(self):
        self.assertFalse(correct_bracketing("("))

    def test_single_closing_bracket(self):
        self.assertFalse(correct_bracketing(")"))

    def test_correct_bracketing(self):
        self.assertTrue(correct_bracketing("()"))
        self.assertTrue(correct_bracketing("(()())"))

    def test_incorrect_bracketing(self):
        self.assertFalse(correct_bracketing(")(()"))
        self.assertFalse(correct_bracketing("()("))
        self.assertFalse(correct_bracketing("(())"))
        self.assertFalse(correct_bracketing("()))"))

if __name__ == '__main__':
    unittest.main()


This script includes a test case for an empty string, single opening bracket, single closing bracket, correctly bracketed strings, and incorrectly bracketed strings. It should cover all the edge cases and provide a comprehensive test for the `correct_bracketing` function.