system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


assistant

import unittest

# Provided function
from HumanEval_61_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_single_open(self):
        self.assertFalse(correct_bracketing("("))

    def test_single_close(self):
        self.assertFalse(correct_bracketing(")"))

    def test_balanced(self):
        self.assertTrue(correct_bracketing("()"))
        self.assertTrue(correct_bracketing("(()())"))

    def test_unbalanced(self):
        self.assertFalse(correct_bracketing(")("))
        self.assertFalse(correct_bracketing(")(()))"))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various cases including single open and close brackets, balanced strings, and unbalanced strings as per the provided examples.