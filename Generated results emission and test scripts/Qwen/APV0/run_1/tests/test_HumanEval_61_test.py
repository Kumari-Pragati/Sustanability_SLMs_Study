system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return depth == 0


assistant

import unittest

# Import the function to be tested
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
        self.assertFalse(correct_bracketing("))(("))

if __name__ == '__main__':
    unittest.main()


This script imports the `correct_bracketing` function and defines several test cases using the `assert` method to check the correctness of the function. The `unittest` module provides a framework for writing tests that can be run automatically.