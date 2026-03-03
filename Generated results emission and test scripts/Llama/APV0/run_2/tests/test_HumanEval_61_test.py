user

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
    return depth == 0assistant

Here is the unittest test script for the `correct_bracketing` function:

import unittest
from HumanEval_61_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_single_opening_bracket(self):
        self.assertFalse(correct_bracketing("("))

    def test_single_closing_bracket(self):
        self.assertFalse(correct_bracketing(")"))

    def test_balanced_brackets(self):
        self.assertTrue(correct_bracketing("()"))

    def test_unbalanced_brackets(self):
        self.assertFalse(correct_bracketing(")(("))

    def test_nested_brackets(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_mixed_opening_and_closing_brackets(self):
        self.assertFalse(correct_bracketing(")(("))

    def test_long_string_with_balanced_brackets(self):
        self.assertTrue(correct_bracketing("((()))"))

    def test_long_string_with_unbalanced_brackets(self):
        self.assertFalse(correct_bracketing("((()))("))

if __name__ == '__main__':
    unittest.main()

This script defines a `TestCorrectBracketing` class that contains 8 test methods, each testing a specific scenario for the `correct_bracketing` function. The test methods use the `assert` statement to verify that the function returns the expected result for each input.

You can run this script directly to execute the tests. If all tests pass, you should see a message indicating that all tests were successful. If any tests fail, you will see an error message indicating which test failed and why.