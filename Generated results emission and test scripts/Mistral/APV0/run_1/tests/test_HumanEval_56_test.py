Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_56_code import correct_bracketing
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def correct_bracketing(brackets: str):
    """brackets is a string of "<" and ">".
    Return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

 Here is a unittest test script for the `correct_bracketing` function:


import unittest
from HumanEval_56_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_single_opening_bracket(self):
        self.assertFalse(correct_bracketing("<"))

    def test_single_closing_bracket(self):
        self.assertFalse(correct_bracketing(">"))

    def test_single_pair(self):
        self.assertTrue(correct_bracketing("<>"))

    def test_multiple_pairs(self):
        self.assertTrue(correct_bracketing("<<><>>"))

    def test_mismatched_brackets(self):
        self.assertFalse(correct_bracketing("><<>"))
        self.assertFalse(correct_bracketing("><"))
        self.assertFalse(correct_bracketing("<<>"))
        self.assertFalse(correct_bracketing(">>"))

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty string, single opening and closing brackets, single pairs, multiple pairs, and mismatched brackets. It uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.