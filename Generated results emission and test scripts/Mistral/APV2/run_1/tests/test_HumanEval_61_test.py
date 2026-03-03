You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `correct_bracketing` function:


import unittest
from HumanEval_61_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_single_opening_bracket(self):
        self.assertFalse(correct_bracketing("("))

    def test_single_closing_bracket(self):
        self.assertFalse(correct_bracketing(")"))

    def test_single_pair(self):
        self.assertTrue(correct_bracketing("()"))

    def test_multiple_pairs(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_mismatched_brackets(self):
        self.assertFalse(correct_bracketing(")(()"))
        self.assertFalse(correct_bracketing("()("))
        self.assertFalse(correct_bracketing("(())"))
        self.assertFalse(correct_bracketing("()()("))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty string, single opening and closing brackets, single pairs, multiple pairs, and mismatched brackets. It uses the `unittest.TestCase.assertTrue()` and `unittest.TestCase.assertFalse()` methods to verify the expected results.