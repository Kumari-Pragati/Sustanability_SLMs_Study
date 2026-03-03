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

 import unittest
from HumanEval_61_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_single_opening_bracket(self):
        self.assertFalse(correct_bracketing("("))

    def test_balanced_brackets(self):
        self.assertTrue(correct_bracketing("()"))

    def test_multiple_opening_and_closing_brackets(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_unbalanced_brackets(self):
        self.assertFalse(correct_bracketing(")(()"))

    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_single_closing_bracket(self):
        self.assertFalse(correct_bracketing(")"))

    def test_multiple_opening_and_closing_brackets_with_spaces(self):
        self.assertTrue(correct_bracketing("( () )"))

    def test_nested_brackets(self):
        self.assertTrue(correct_bracketing("( ( ) )"))

    def test_no_brackets(self):
        self.assertTrue(correct_bracketing(""))

if __name__ == '__main__':
    unittest.main()